package fr.majado.carnet;

import android.content.Intent;
import android.content.res.Configuration;
import android.net.Uri;
import android.os.Build;
import android.os.Bundle;
import android.os.SystemClock;
import android.webkit.JavascriptInterface;
import android.webkit.ValueCallback;
import android.webkit.WebChromeClient;
import android.webkit.WebResourceRequest;
import android.webkit.WebResourceResponse;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.widget.Toast;

import androidx.activity.OnBackPressedCallback;
import androidx.activity.result.ActivityResultLauncher;
import androidx.activity.result.contract.ActivityResultContracts;
import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.splashscreen.SplashScreen;
import androidx.webkit.WebSettingsCompat;
import androidx.webkit.WebViewAssetLoader;
import androidx.webkit.WebViewClientCompat;
import androidx.webkit.WebViewFeature;

import java.io.FileInputStream;
import java.io.OutputStream;
import java.nio.charset.StandardCharsets;

/**
 * Carnet : l'appli web (dist/) tourne dans une WebView, servie depuis les assets de l'APK
 * sous une origine https stable (localStorage conservé, aucun réseau nécessaire).
 * Le pont "Android" (window.Android côté JS) gère l'export de fichier ; l'import passe par
 * le sélecteur de fichiers du système.
 */
public class MainActivity extends AppCompatActivity {
    private static final String HOME = "https://" + WebViewAssetLoader.DEFAULT_DOMAIN + "/index.html";

    private WebView web;
    private Updater updater;
    private long launchedAt, resumedAt;
    private long servedBuild;                 // build de la version actuellement affichée
    private ValueCallback<Uri[]> fileChooser; // import : <input type="file">
    private String pendingExport;             // export : JSON en attente d'un emplacement

    private final ActivityResultLauncher<Intent> pickFile = registerForActivityResult(
        new ActivityResultContracts.StartActivityForResult(), r -> {
            if (fileChooser == null) return;
            Uri[] out = null;
            if (r.getResultCode() == RESULT_OK && r.getData() != null && r.getData().getData() != null)
                out = new Uri[] { r.getData().getData() };
            fileChooser.onReceiveValue(out);
            fileChooser = null;
        });

    private final ActivityResultLauncher<Intent> createFile = registerForActivityResult(
        new ActivityResultContracts.StartActivityForResult(), r -> {
            String json = pendingExport;
            pendingExport = null;
            if (json == null || r.getResultCode() != RESULT_OK || r.getData() == null || r.getData().getData() == null) return;
            try (OutputStream os = getContentResolver().openOutputStream(r.getData().getData(), "wt")) {
                if (os == null) throw new IllegalStateException();
                os.write(json.getBytes(StandardCharsets.UTF_8));
                Toast.makeText(this, R.string.export_ok, Toast.LENGTH_SHORT).show();
            } catch (Exception e) {
                Toast.makeText(this, R.string.export_err, Toast.LENGTH_SHORT).show();
            }
        });

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        SplashScreen.installSplashScreen(this);
        super.onCreate(savedInstanceState);

        web = new WebView(this);
        setContentView(web);
        web.setBackgroundColor(getColor(R.color.ground)); // pas de flash blanc au lancement

        WebSettings s = web.getSettings();
        s.setJavaScriptEnabled(true);
        s.setDomStorageEnabled(true); // localStorage : toutes les données de l'appli
        s.setAllowFileAccess(false);
        s.setAllowContentAccess(true);
        s.setSupportZoom(false);
        s.setBuiltInZoomControls(false);
        s.setDisplayZoomControls(false);
        s.setCacheMode(WebSettings.LOAD_DEFAULT);

        // Mode sombre : on laisse l'appli web appliquer son propre thème via prefers-color-scheme.
        if (WebViewFeature.isFeatureSupported(WebViewFeature.ALGORITHMIC_DARKENING))
            WebSettingsCompat.setAlgorithmicDarkeningAllowed(s, false);
        if (Build.VERSION.SDK_INT < 33 && WebViewFeature.isFeatureSupported(WebViewFeature.FORCE_DARK)) {
            boolean night = (getResources().getConfiguration().uiMode & Configuration.UI_MODE_NIGHT_MASK) == Configuration.UI_MODE_NIGHT_YES;
            WebSettingsCompat.setForceDark(s, night ? WebSettingsCompat.FORCE_DARK_ON : WebSettingsCompat.FORCE_DARK_OFF);
            if (WebViewFeature.isFeatureSupported(WebViewFeature.FORCE_DARK_STRATEGY))
                WebSettingsCompat.setForceDarkStrategy(s, WebSettingsCompat.DARK_STRATEGY_WEB_THEME_DARKENING_ONLY);
        }

        // Fichiers servis depuis l'APK, sauf index.html si une version plus récente a été téléchargée.
        updater = new Updater(this);
        final WebViewAssetLoader.AssetsPathHandler assets = new WebViewAssetLoader.AssetsPathHandler(this);
        final WebViewAssetLoader loader = new WebViewAssetLoader.Builder()
            .addPathHandler("/", path -> {
                if (("index.html".equals(path) || path.isEmpty()) && updater.useDownloaded()) {
                    try { return new WebResourceResponse("text/html", "utf-8", new FileInputStream(updater.indexFile())); }
                    catch (Exception ignored) { /* on retombe sur la version de l'APK */ }
                }
                return assets.handle(path);
            })
            .build();

        web.setWebViewClient(new WebViewClientCompat() {
            @Override
            public WebResourceResponse shouldInterceptRequest(WebView v, WebResourceRequest req) {
                return loader.shouldInterceptRequest(req.getUrl());
            }

            @Override
            public boolean shouldOverrideUrlLoading(@NonNull WebView v, @NonNull WebResourceRequest req) {
                Uri u = req.getUrl();
                if (WebViewAssetLoader.DEFAULT_DOMAIN.equals(u.getHost())) return false;
                try { startActivity(new Intent(Intent.ACTION_VIEW, u)); } catch (Exception ignored) {}
                return true; // liens externes : navigateur du téléphone
            }
        });

        web.setWebChromeClient(new WebChromeClient() {
            @Override
            public boolean onShowFileChooser(WebView v, ValueCallback<Uri[]> cb, FileChooserParams p) {
                if (fileChooser != null) fileChooser.onReceiveValue(null);
                fileChooser = cb;
                Intent i = new Intent(Intent.ACTION_OPEN_DOCUMENT).addCategory(Intent.CATEGORY_OPENABLE).setType("*/*");
                try { pickFile.launch(i); } catch (Exception e) { fileChooser = null; return false; }
                return true;
            }
        });

        web.addJavascriptInterface(new Bridge(), "Android");

        if (savedInstanceState != null) web.restoreState(savedInstanceState);
        if (web.getUrl() == null) web.loadUrl(HOME);
        servedBuild = updater.currentBuild();
        launchedAt = SystemClock.elapsedRealtime();
        updater.checkInBackground(0, autoListener);

        // Bouton Retour : l'appli web décide (retour à l'onglet Séance), sinon on quitte.
        getOnBackPressedDispatcher().addCallback(this, new OnBackPressedCallback(true) {
            @Override
            public void handleOnBackPressed() {
                web.evaluateJavascript(
                    "(function(){try{return !!(window.androidBack&&window.androidBack())}catch(e){return false}})()",
                    v -> { if (!"true".equals(v)) finish(); });
            }
        });
    }

    @Override
    protected void onStart() {
        super.onStart();
        // Retour dans l'appli : nouvelle vérification (au plus une par minute).
        resumedAt = SystemClock.elapsedRealtime();
        updater.checkInBackground(60 * 1000L, autoListener);
    }

    /** Vérification automatique : on applique tout de suite si l'utilisateur vient d'ouvrir ou de revenir dans l'appli,
     *  sinon l'appli web affiche une bannière « Mettre à jour ». */
    private final Updater.Listener autoListener = new Updater.Listener() {
        @Override public void onUpdated(long build) { onUpdateReady(build, true); }
        @Override public void onUpToDate() { if (updater.currentBuild() > servedBuild) onUpdateReady(updater.currentBuild(), true); }
    };

    /** Vérification demandée par le bouton de l'appli web : on rend compte dans tous les cas. */
    private final Updater.Listener manualListener = new Updater.Listener() {
        @Override public void onUpdated(long build) { onUpdateReady(build, false); }
        @Override public void onUpToDate() {
            if (updater.currentBuild() > servedBuild) onUpdateReady(updater.currentBuild(), false);
            else js("window.carnetUpdateNone && window.carnetUpdateNone()");
        }
        @Override public void onError() { js("window.carnetUpdateError && window.carnetUpdateError()"); }
    };

    private void onUpdateReady(long build, boolean auto) {
        runOnUiThread(() -> {
            if (isFinishing() || isDestroyed()) return;
            long now = SystemClock.elapsedRealtime();
            if (auto && (now - launchedAt < 5000 || now - resumedAt < 5000)) reloadWeb();
            else js("window.carnetUpdateReady ? window.carnetUpdateReady(" + build + ") : Android.reload()");
        });
    }

    private void reloadWeb() {
        servedBuild = updater.currentBuild();
        web.reload();
    }

    private void js(String code) {
        runOnUiThread(() -> { if (!isFinishing() && !isDestroyed()) web.evaluateJavascript(code, null); });
    }

    @Override
    protected void onSaveInstanceState(@NonNull Bundle out) {
        super.onSaveInstanceState(out);
        web.saveState(out);
    }

    @Override
    protected void onDestroy() {
        web.destroy();
        super.onDestroy();
    }

    /** Fonctions exposées à la page sous window.Android. */
    private class Bridge {
        @JavascriptInterface
        public void saveFile(String name, String content) {
            pendingExport = content;
            Intent i = new Intent(Intent.ACTION_CREATE_DOCUMENT)
                .addCategory(Intent.CATEGORY_OPENABLE)
                .setType("application/json")
                .putExtra(Intent.EXTRA_TITLE, name);
            runOnUiThread(() -> createFile.launch(i));
        }

        /** Applique la version téléchargée (bouton « Mettre à jour » de la bannière). */
        @JavascriptInterface
        public void reload() { runOnUiThread(MainActivity.this::reloadWeb); }

        /** Vérifie tout de suite s'il y a une nouvelle version (bouton dans l'onglet Suivi). */
        @JavascriptInterface
        public void checkUpdate() { updater.checkInBackground(0, manualListener); }

        /** Numéro de build de la version affichée. */
        @JavascriptInterface
        public String build() { return String.valueOf(servedBuild); }
    }
}

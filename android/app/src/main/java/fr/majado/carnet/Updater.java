package fr.majado.carnet;

import android.content.Context;
import android.content.SharedPreferences;

import org.json.JSONObject;

import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.nio.charset.StandardCharsets;

/**
 * Mise à jour automatique de l'appli web embarquée.
 * dist/version.json (dans l'APK) contient un numéro de build et l'adresse où l'appli est publiée
 * (GitHub Pages). Au lancement, on lit version.json à cette adresse ; si le build y est plus récent,
 * on télécharge index.html dans le stockage interne, et c'est lui qui est servi ensuite.
 * Si un APK plus récent est réinstallé, le fichier téléchargé devenu obsolète est supprimé.
 */
final class Updater {
    interface Listener {
        void onUpdated(long build);
        default void onUpToDate() {}
        default void onError() {}
    }

    private static final String PREFS = "carnet.updater";
    private static final String KEY_BUILD = "downloadedBuild", KEY_URL = "url", KEY_LAST = "lastCheck";

    private final Context ctx;

    Updater(Context ctx) { this.ctx = ctx.getApplicationContext(); }

    File indexFile() { return new File(new File(ctx.getFilesDir(), "web"), "index.html"); }

    /** Adresse de publication : celle apprise en ligne, sinon celle embarquée dans l'APK. */
    String baseUrl() {
        String u = prefs().getString(KEY_URL, "");
        if (u.isEmpty()) u = embedded().optString("url", "");
        if (!u.isEmpty() && !u.endsWith("/")) u += "/";
        return u;
    }

    long embeddedBuild() { return embedded().optLong("build", 0); }
    long downloadedBuild() { return prefs().getLong(KEY_BUILD, 0); }

    /** Vrai si la version téléchargée est plus récente que celle de l'APK ; sinon on l'efface. */
    boolean useDownloaded() {
        if (!indexFile().exists()) return false;
        if (downloadedBuild() > embeddedBuild()) return true;
        indexFile().delete();
        prefs().edit().remove(KEY_BUILD).apply();
        return false;
    }

    long currentBuild() { return useDownloaded() ? downloadedBuild() : embeddedBuild(); }

    /** Vérifie en arrière-plan, au plus une fois par intervalle donné (ms, 0 = toujours). */
    void checkInBackground(long minIntervalMs, Listener l) {
        String base = baseUrl();
        if (base.isEmpty()) { if (l != null) l.onError(); return; }
        long now = System.currentTimeMillis();
        if (minIntervalMs > 0 && now - prefs().getLong(KEY_LAST, 0) < minIntervalMs) return;
        prefs().edit().putLong(KEY_LAST, now).apply();
        new Thread(() -> {
            try {
                long b = check(base);
                if (l != null) { if (b > 0) l.onUpdated(b); else l.onUpToDate(); }
            } catch (Exception e) { if (l != null) l.onError(); /* hors ligne, serveur absent : on réessaiera */ }
        }, "carnet-updater").start();
    }

    private long check(String base) throws Exception {
        JSONObject remote = new JSONObject(fetch(base + "version.json?t=" + System.currentTimeMillis()));
        String newUrl = remote.optString("url", "");
        if (!newUrl.isEmpty() && !newUrl.equals(prefs().getString(KEY_URL, ""))) prefs().edit().putString(KEY_URL, newUrl).apply();
        long build = remote.optLong("build", 0);
        if (build <= currentBuild()) return 0;
        String html = fetch(base + "index.html?b=" + build);
        if (html.length() < 10_000 || !html.contains("</html>")) throw new IOException("index.html incomplet");
        File dir = indexFile().getParentFile();
        if (dir != null) dir.mkdirs();
        File tmp = new File(dir, "index.html.tmp");
        try (OutputStream os = new FileOutputStream(tmp)) { os.write(html.getBytes(StandardCharsets.UTF_8)); }
        if (!tmp.renameTo(indexFile())) {
            indexFile().delete();
            if (!tmp.renameTo(indexFile())) throw new IOException("rename");
        }
        prefs().edit().putLong(KEY_BUILD, build).apply();
        return build;
    }

    private JSONObject embedded() {
        try (InputStream in = ctx.getAssets().open("version.json")) { return new JSONObject(read(in)); }
        catch (Exception e) { return new JSONObject(); }
    }

    private static String fetch(String url) throws IOException {
        HttpURLConnection c = (HttpURLConnection) new URL(url).openConnection();
        c.setConnectTimeout(8000);
        c.setReadTimeout(15000);
        c.setUseCaches(false);
        try {
            if (c.getResponseCode() != 200) throw new IOException("HTTP " + c.getResponseCode());
            try (InputStream in = c.getInputStream()) { return read(in); }
        } finally { c.disconnect(); }
    }

    private static String read(InputStream in) throws IOException {
        ByteArrayOutputStream bo = new ByteArrayOutputStream();
        byte[] b = new byte[8192];
        int n;
        while ((n = in.read(b)) > 0) bo.write(b, 0, n);
        return bo.toString("UTF-8");
    }

    private SharedPreferences prefs() { return ctx.getSharedPreferences(PREFS, Context.MODE_PRIVATE); }
}

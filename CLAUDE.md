# Carnet — contexte pour Claude Code

Appli web mobile (PWA) en un seul fichier, sans framework ni dépendance. Français partout.

Qui est l'utilisateur, ce qui a été décidé (prise de masse, épaule, créatine…), les repas et les séances en clair :
@CONTEXTE.md
Après toute modification de `plan/gen.py` ou `plan/prog.py`, relancer `gen_contexte.py` (il régénère les tableaux de CONTEXTE.md).

## Où est quoi
- `app.template.html` : tout le code de l'appli. CSS en tête, JS en bas. Le marqueur `__DATA__` est remplacé par `data.json` au build.
- `build_data.py` : extrait les données depuis `plan/prog.py` (séances) et `plan/gen.py` (repas, courses, règles). **Ne pas dupliquer ces données dans le template** : on change le plan à la source, puis on rebuild.
- `build.py` : produit `dist/` (index.html, sw.js avec nom de cache horodaté, `version.json` = numéro de build + adresse de publication).
  `publish.ps1` prend le Python de `%LOCALAPPDATA%\android-toolchain` s'il existe, sinon le `python` du PATH ; `gh` n'est requis que pour la toute première publication.
- **Flux normal après toute modification du plan ou du template : `.\publish.ps1`** (build + commit + push GitHub Pages).
  L'appli Android sur le téléphone se met à jour toute seule au lancement suivant. Pas besoin de recompiler l'APK.

## Conventions
- État global `S`, persisté dans `localStorage` sous la clé `carnet.v1`. Toute mutation passe par `save()`. Lectures/écritures dans `try/catch`.
- Quatre vues, une fonction `render*()` par onglet, qui reconstruit `#app` en innerHTML puis attache les handlers. Pas de framework.
- Dates au format ISO `AAAA-MM-JJ`, `dow()` renvoie 0 pour lundi.
- Cibles tactiles ≥ 44 px, pas de dépendance réseau (Google Fonts a des fallbacks système).
- Mode sombre via `prefers-color-scheme`, jamais de couleur définie dans un seul thème.
- Design « Papier » : fond `--ground` chaud, cartes blanches `--surface` à grand rayon (22 px) et ombre douce, contrôles 14 px, pastilles 999 px. Titres et texte en Plus Jakarta Sans, chiffres en JetBrains Mono (`font-variant-numeric: tabular-nums`). Vert `--green` (repas, validation), bleu `--blue` (séance), terre `--clay` (repos, alertes), chacun avec sa teinte `--*-tint` pour les fonds de pastille. Toutes les couleurs sont des variables définies dans `:root` puis redéfinies dans `@media (prefers-color-scheme: dark)`.

## Tester
`.\serve.ps1` (ou `python3 -m http.server 8765 --directory dist`) puis ouvrir `http://localhost:8765` dans un navigateur en mode mobile (412 × 915). Il existe un script Playwright de référence dans `../test_app.mjs`.

## Ne pas faire
- Ne pas inventer de données nutritionnelles ou d'exercices dans le JS : ils viennent du plan.
- Ne pas ajouter de suivi par compte ou de synchronisation cloud sans que l'utilisateur le demande.
- Ne pas casser la clé `carnet.v1` : si le schéma change, migrer dans `load()`.

## Appli Android (android/)
- Projet natif Java (pas de Kotlin, pas de Capacitor) : `MainActivity` charge `dist/` depuis les assets via `WebViewAssetLoader`
  (origine `https://appassets.androidplatform.net/`, donc `localStorage` stable). `dist/` est monté comme dossier d'assets dans
  `app/build.gradle` : ne rien copier à la main.
- Pont JS : `window.Android.saveFile(nom, contenu)` (export via `ACTION_CREATE_DOCUMENT`). Le template teste `window.Android`
  pour choisir entre ce pont et le téléchargement blob ; le service worker n'est pas enregistré dans l'appli Android.
- Pont mise à jour : `Android.checkUpdate()` (bouton « Vérifier les mises à jour » dans Suivi), `Android.reload()` (bannière
  `#update` « Mettre à jour »), `Android.build()`. Android appelle `window.carnetUpdateReady / carnetUpdateNone / carnetUpdateError`.
  Application automatique si l'appli vient d'être ouverte ou de revenir au premier plan (< 5 s), sinon bannière.
- `window.androidBack()` dans le template : appelé par le bouton Retour ; renvoie `true` s'il a géré (retour à Séance), sinon l'appli se ferme.
- Mise à jour automatique : `Updater.java` lit `version.json` à l'adresse `url` (déduite du dépôt GitHub par `build.py`),
  télécharge `index.html` dans `filesDir/web/` si le build distant est plus récent, et `MainActivity` sert ce fichier à la place
  de l'asset. Un APK réinstallé plus récent supprime le téléchargement obsolète.
- Build APK : `.\build-apk.ps1`, uniquement si le code Android change (outils dans `%LOCALAPPDATA%\android-toolchain`).
  Incrémenter `versionCode` à chaque APK diffusé. `dist/carnet.apk` est exclu des assets (`ignoreAssetsPattern`). Ne jamais perdre `android/carnet-release.jks` + `keystore.properties`.
- Couleurs de la barre d'état / splash : `res/values*/colors.xml`, à garder alignées sur `--ground` / `--surface` du template.

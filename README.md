# Carnet — séances, repas, courses

Appli web installable sur Android (et iPhone). Elle tourne entièrement sur le téléphone :
aucun compte, aucun serveur, les données restent en local.

## Ce qu'elle fait

- **Séance** : la séance du jour s'ouvre toute seule (lundi J1, mardi J2, jeudi J3, vendredi J4).
  Pour chaque série : poids et répétitions avec des boutons + / −, une case « faite » qui lance
  le minuteur de repos (vibration à la fin), et la dernière performance affichée sous chaque exercice.
  « Terminer la séance » enregistre l'historique.
- **Repas** : les 7 jours du plan, quantités en cru, kcal et protéines par repas, cases à cocher.
- **Courses** : la liste de la semaine à cocher rayon par rayon, « Nouvelle semaine » pour repartir à zéro.
- **Suivi** : pesée du matin, moyenne hebdomadaire et verdict automatique selon les règles de pilotage,
  tour de taille, courbe sur 6 semaines, progression des charges exercice par exercice, export / import.

## Version web (PWA) : installer depuis Chrome

Alternative à l'APK ci-dessous, sans rien installer : la même adresse GitHub Pages s'ouvre dans Chrome.

L'appli doit être servie en **https** pour s'installer comme une vraie appli (icône, plein écran,
hors connexion). Le plus simple : GitHub Pages, gratuit.

```bash
# depuis ce dossier, avec Claude Code ou à la main
gh repo create carnet --public --source=. --push
gh api -X POST repos/{owner}/carnet/pages -f "source[branch]=main" -f "source[path]=/dist"
```

Puis sur le téléphone, ouvrir `https://<ton-compte>.github.io/carnet/` dans Chrome
→ menu ⋮ → **Ajouter à l'écran d'accueil**. Une fois ouverte une première fois, elle fonctionne sans réseau.

Sans hébergement, `dist/index.html` s'ouvre aussi directement dans Chrome sur le téléphone
(par Fichiers ou Drive) : tout marche sauf l'installation en plein écran et le mode hors connexion.

## Appli Android native (APK) et mise à jour automatique

Le dossier `android/` contient un projet Android natif qui embarque `dist/` dans une WebView :
icône, écran de démarrage, plein écran, mode sombre, hors ligne sans rien configurer, bouton Retour,
export via « Enregistrer sous » et import via le sélecteur de fichiers du téléphone.

**Mettre à jour le plan sur le téléphone** (repas, séances, courses, ou l'appli elle-même) :

```powershell
.\publish.ps1
```

Ce script reconstruit `dist/`, l'envoie sur GitHub et GitHub Pages le publie. À l'ouverture suivante,
l'appli sur le téléphone compare `version.json` en ligne avec sa version, télécharge la nouvelle
`index.html` si besoin et l'applique (tout de suite si l'appli vient de s'ouvrir, sinon au lancement d'après).
Aucune réinstallation, données conservées. Sans réseau, l'appli continue avec la version qu'elle a.

Première fois : compte GitHub gratuit nécessaire (le script ouvre la page de connexion), dépôt public
`carnet` créé automatiquement (GitHub Pages n'est gratuit que pour les dépôts publics : le plan et le code
sont visibles, jamais tes pesées ni ton historique, qui restent sur le téléphone).

**Reconstruire l'APK** (seulement si le code Android change, ou pour la toute première installation) :

```powershell
.uild-apk.ps1
```

Produit `carnet.apk` (release, signé) et le copie dans `dist/`, donc après `publish.ps1` il est téléchargeable
depuis le téléphone à `https://<compte>.github.io/carnet/carnet.apk`. Sinon : câble, Drive ou mail, puis ouvrir
le fichier sur le téléphone (autoriser l'installation depuis cette source). Avec le débogage USB : `adb install -r carnet.apk`.

- La chaîne de build (JDK 17, Gradle 8.9, SDK Android, Python portable, gh) vit dans `%LOCALAPPDATA%\android-toolchain`,
  rien n'est installé au niveau système.
- **Signature** : `android/carnet-release.jks` + `android/keystore.properties`, exclus de git. À sauvegarder : sans cette clé,
  un nouvel APK ne peut pas remplacer celui installé (il faudrait désinstaller, et perdre les données).
- Pour diffuser un nouvel APK, augmenter `versionCode` dans `android/app/build.gradle`.
- Les données restent dans le stockage local de l'appli ; désinstaller l'appli les efface.
  **Exporter mes données** ouvre la boîte « Enregistrer sous » d'Android.

## Structure

| Fichier | Rôle |
|---|---|
| `app.template.html` | L'appli entière (HTML + CSS + JS), avec un marqueur `__DATA__` |
| `build_data.py` | Lit le plan (`plan/prog.py`, `plan/gen.py`) et produit `data.json` |
| `build.py` | Injecte `data.json` dans le template → `dist/index.html`, copie manifest, icônes, service worker |
| `manifest.json`, `sw.js`, `icon-*.png` | Ce qui rend l'appli installable et utilisable hors ligne |
| `dist/` | **Le dossier à publier** (aussi embarqué dans l'APK) |
| `android/` | Projet Android natif (WebView) qui embarque `dist/` |
| `build-apk.ps1` | Construit `carnet.apk` (installe la chaîne de build au premier lancement) |
| `publish.ps1` | Reconstruit `dist/` et publie sur GitHub Pages : le téléphone se met à jour tout seul |
| `serve.ps1` | Serveur de test local (Python absent) : `.\serve.ps1` puis http://localhost:8765 |

Une seule source de vérité : le plan vit dans `prog.py` et `gen.py`. Modifier un exercice ou un
repas là-bas, puis `python3 build.py`, met à jour l'appli **et** les fiches A4.

## Faire évoluer l'appli avec Claude Code

Ouvrir un terminal dans ce dossier et lancer `claude`. Le fichier `CLAUDE.md` explique le projet.
Exemples de demandes qui marchent bien :

- « Ajoute un onglet Photos pour une photo tous les 28 jours »
- « Mets un rappel de la semaine allégée toutes les 6 semaines »
- « Ajoute le cru → cuit dans l'onglet Repas »
- « Fais un graphique des kilos soulevés par semaine »

Après chaque modification : `.\publish.ps1` (build + commit + push). GitHub Pages se met à jour en une
minute, et le téléphone récupère la nouvelle version à l'ouverture suivante. Le nom de cache du service worker
et le numéro de build sont générés automatiquement.

## Sauvegarde

Les données sont dans le stockage local du navigateur. Effacer les données de Chrome les efface.
Le bouton **Exporter mes données** (onglet Suivi) produit un fichier JSON à garder quelque part ;
**Importer** le recharge.

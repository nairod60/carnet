# Publie l'appli : reconstruit dist/ puis l'envoie sur GitHub (GitHub Pages).
# Le téléphone récupère la nouvelle version tout seul au lancement suivant de l'appli.
#   .\publish.ps1                     -> message de commit automatique
#   .\publish.ps1 "Ajout du J5"       -> message personnalisé
# Première fois : nécessite un compte GitHub (le script ouvre la page de connexion) ; le dépôt "carnet"
# est créé automatiquement, puis l'APK est reconstruit avec l'adresse de publication et publié dans dist/.
param([string]$Message = "")
$ErrorActionPreference = "Continue"  # git/gh écrivent des infos sur stderr : on contrôle les codes de retour nous-mêmes
$root = $PSScriptRoot
$tc = Join-Path $env:LOCALAPPDATA "android-toolchain"
$python = Join-Path $tc "python\python.exe"
$gh = Join-Path $tc "gh\bin\gh.exe"
foreach ($t in $python, $gh) { if (-not (Test-Path $t)) { throw "Outil introuvable : $t" } }

Push-Location $root
try {
    # 1. dépôt git + compte GitHub
    if (-not (Test-Path ".git")) { git init -b main | Out-Null }
    & $gh auth status *> $null
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Connexion à GitHub nécessaire (une seule fois) : suis les instructions, un code s'affichera à copier dans le navigateur." -ForegroundColor Yellow
        & $gh auth login --hostname github.com --git-protocol https --web
        if ($LASTEXITCODE -ne 0) { throw "Connexion GitHub échouée" }
    }
    & $gh auth setup-git *> $null
    $owner = (& $gh api user --jq .login)
    $hasRemote = ((git remote) -contains "origin")
    if (-not $hasRemote) {
        Write-Host "Création du dépôt GitHub $owner/carnet (public : GitHub Pages est gratuit uniquement pour les dépôts publics)."
        & $gh repo create carnet --public --source=. --remote=origin
        if ($LASTEXITCODE -ne 0) { throw "Création du dépôt échouée" }
    }

    # 2. build (l'adresse GitHub Pages est déduite du dépôt et écrite dans dist/version.json)
    & $python build.py
    if ($LASTEXITCODE -ne 0) { throw "build.py a échoué" }
    $url = (Get-Content "dist/version.json" -Raw | ConvertFrom-Json).url
    if (-not $url) { throw "Adresse de publication introuvable (dépôt GitHub sans remote origin ?)" }

    # 3. APK : reconstruit si absent ou si l'adresse de publication embarquée a changé
    $urlFile = "android\published-url.txt"
    $apkUrl = if (Test-Path $urlFile) { (Get-Content $urlFile -Raw).Trim() } else { "" }
    if (-not (Test-Path "dist\carnet.apk") -or $apkUrl -ne $url) {
        Write-Host "Reconstruction de l'APK avec l'adresse de mise à jour $url ..."
        & (Join-Path $root "build-apk.ps1")
        if ($LASTEXITCODE -ne 0 -or -not (Test-Path "dist\carnet.apk")) { throw "build-apk.ps1 a échoué" }
        [IO.File]::WriteAllText((Join-Path $root $urlFile), $url + "`n")
    }

    # 4. commit + push
    git add -A
    if (-not $Message) { $Message = "Mise à jour du " + (Get-Date -Format "yyyy-MM-dd HH:mm") }
    git diff --cached --quiet
    if ($LASTEXITCODE -ne 0) { git commit -q -m $Message } else { Write-Host "Rien de nouveau à publier." }
    git push -u origin main
    if ($LASTEXITCODE -ne 0) { throw "git push a échoué" }

    # 5. Branche gh-pages = contenu de dist/ uniquement (GitHub Pages ne sert que la racine ou docs/)
    $sha = (git subtree split --prefix dist main)
    if ($LASTEXITCODE -ne 0 -or -not $sha) { throw "git subtree split a échoué" }
    git push -f origin "${sha}:refs/heads/gh-pages"
    if ($LASTEXITCODE -ne 0) { throw "push gh-pages a échoué" }

    # 6. GitHub Pages sur la branche gh-pages : activé la première fois
    & $gh api "repos/$owner/carnet/pages" *> $null
    if ($LASTEXITCODE -ne 0) {
        & $gh api -X POST "repos/$owner/carnet/pages" -f "source[branch]=gh-pages" -f "source[path]=/" | Out-Null
        & $gh api -X POST "repos/$owner/carnet/pages/builds" *> $null  # première construction du site
        Write-Host "GitHub Pages activé. Première publication : compte 1 à 2 minutes avant que l'adresse réponde."
    }
    Write-Host ""
    Write-Host "Publié : $url" -ForegroundColor Green
    Write-Host "Le téléphone se mettra à jour tout seul à la prochaine ouverture de l'appli (connexion internet nécessaire)."
    Write-Host "APK à installer depuis le téléphone (première fois) : ${url}carnet.apk"
} finally { Pop-Location }

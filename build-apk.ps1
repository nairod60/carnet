# Construit l'APK Android de Carnet :  .\build-apk.ps1      (ou  .\build-apk.ps1 -Debug)
# Résultat : carnet.apk dans ce dossier (à copier sur le téléphone et ouvrir pour installer).
#
# Outils (aucune installation système, tout est dans %LOCALAPPDATA%\android-toolchain) :
#   JDK 17 (Temurin), Gradle 8.9, Android SDK (command-line tools, platform 34, build-tools 34.0.0).
# La première fois, le script installe le SDK Android (~600 Mo) après avoir demandé
# d'accepter sa licence : https://developer.android.com/studio/terms
param([switch]$Debug)
$ErrorActionPreference = "Stop"
$root = $PSScriptRoot
$tc = Join-Path $env:LOCALAPPDATA "android-toolchain"
$jdk = Get-ChildItem -Path $tc -Directory -Filter "jdk-17*" | Select-Object -First 1
if (-not $jdk) { throw "JDK 17 introuvable dans $tc" }
$env:JAVA_HOME = $jdk.FullName
$env:ANDROID_HOME = Join-Path $tc "sdk"
$env:ANDROID_SDK_ROOT = $env:ANDROID_HOME
$env:Path = "$($env:JAVA_HOME)\bin;$($env:ANDROID_HOME)\platform-tools;$env:Path"

$sdkmanager = Join-Path $env:ANDROID_HOME "cmdline-tools\latest\bin\sdkmanager.bat"
if (-not (Test-Path $sdkmanager)) { throw "Android command-line tools introuvables : $sdkmanager" }

if (-not (Test-Path (Join-Path $env:ANDROID_HOME "platforms\android-34")) -or -not (Test-Path (Join-Path $env:ANDROID_HOME "build-tools\34.0.0"))) {
    Write-Host ""
    Write-Host "Le SDK Android n'est pas encore installé. Pour l'installer, il faut accepter" -ForegroundColor Yellow
    Write-Host "les conditions d'utilisation du SDK Android : https://developer.android.com/studio/terms" -ForegroundColor Yellow
    $r = Read-Host "Accepter la licence et installer le SDK (~600 Mo) ? [o/N]"
    if ($r -notmatch '^[oOyY]') { throw "Installation annulée." }
    # Répond 'y' à chaque licence, puis installe les paquets nécessaires
    1..12 | ForEach-Object { "y" } | & $sdkmanager --licenses | Out-Null
    & $sdkmanager "platform-tools" "platforms;android-34" "build-tools;34.0.0"
    if ($LASTEXITCODE -ne 0) { throw "sdkmanager a échoué (code $LASTEXITCODE)" }
}

# Indique au projet où est le SDK
$sdkDir = $env:ANDROID_HOME.Replace("\", "\\").Replace(":", "\:")
[IO.File]::WriteAllText((Join-Path $root "android\local.properties"), "sdk.dir=$sdkDir`n")

# Reconstruit dist/ (plan + template) avant de l'embarquer
$python = Join-Path $tc "python\python.exe"
if (-not (Test-Path $python)) { throw "Python portable introuvable : $python" }
Push-Location $root
try { & $python build.py; if ($LASTEXITCODE -ne 0) { throw "build.py a échoué" } } finally { Pop-Location }

# Build
Push-Location (Join-Path $root "android")
try {
    $task = if ($Debug) { "assembleDebug" } else { "assembleRelease" }
    & .\gradlew.bat $task --console=plain
    if ($LASTEXITCODE -ne 0) { throw "Build échoué (code $LASTEXITCODE)" }
} finally { Pop-Location }

$apk = if ($Debug) { "android\app\build\outputs\apk\debug\app-debug.apk" } else { "android\app\build\outputs\apk\release\app-release.apk" }
Copy-Item (Join-Path $root $apk) (Join-Path $root "carnet.apk") -Force
if (-not $Debug) { Copy-Item (Join-Path $root $apk) (Join-Path $root "dist\carnet.apk") -Force }  # publié avec le site : téléchargeable depuis le téléphone
$size = [math]::Round((Get-Item (Join-Path $root "carnet.apk")).Length / 1MB, 1)
Write-Host ""
Write-Host "OK : $root\carnet.apk ($size Mo)" -ForegroundColor Green
Write-Host "Copie ce fichier sur le téléphone (câble, Drive, mail) et ouvre-le pour l'installer."
Write-Host "Pour installer directement par câble USB (débogage USB activé) : adb install -r carnet.apk"

@echo off
rem Double-clic = publier l'appli (build + commit + push GitHub Pages). Equivalent de .\publish.ps1 dans PowerShell.
cd /d "%~dp0"
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0publish.ps1"
echo.
pause

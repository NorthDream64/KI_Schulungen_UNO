@echo off
chcp 65001 >nul
cd /d "%~dp0.."
where node >nul 2>nul
if errorlevel 1 (
  echo.
  echo   Node.js ist nicht installiert oder nicht im Suchpfad.
  echo   Ohne Node.js kann die Pruefung nicht laufen.
  echo   Download: https://nodejs.org
  echo.
  pause
  exit /b 1
)
node "Werkzeuge\pruefe_quizze.js"
echo.
pause

@echo off
chcp 65001 >nul
cd /d "%~dp0.."
git config core.hooksPath Werkzeuge/githooks
if errorlevel 1 (
  echo   Fehler beim Einrichten. Laeuft dieses Skript im Repo-Ordner?
) else (
  echo.
  echo   Eingerichtet. Die Pruefung laeuft ab jetzt bei jedem "git commit"
  echo   automatisch mit. Rueckgaengig machen mit:
  echo       git config --unset core.hooksPath
  echo.
)
pause

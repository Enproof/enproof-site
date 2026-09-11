@echo off
cd /d "%~dp0..\.."
echo current-dir="%CD%"
echo python scripts/bump-version.py patch
python scripts/bump-version.py patch
pause

@echo off
cd /d "%~dp0..\.."
echo current-dir="%CD%"
echo python scripts/bump-version.py minor
python scripts/bump-version.py minor
pause

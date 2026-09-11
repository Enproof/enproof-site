@echo off
cd /d "%~dp0..\.."
echo current-dir="%CD%"
echo python scripts/bump-version.py major
python scripts/bump-version.py major
pause

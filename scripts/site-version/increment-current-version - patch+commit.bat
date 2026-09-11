@echo off
cd /d "%~dp0..\.."
echo python scripts/bump-version.py patch --commit
python scripts/bump-version.py patch --commit
pause

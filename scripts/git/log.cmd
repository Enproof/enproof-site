@echo off
echo list last X commits in descending order

cd ..
echo git log -20 --oneline
git log -20 --oneline

rem git log --grep="expedit"

rem git log -6 
pause
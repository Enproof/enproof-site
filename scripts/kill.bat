@echo off
echo killing all python processes...
taskkill   /IM "python.exe" /F
tasklist | findstr /i " python  "
echo python killed
pause
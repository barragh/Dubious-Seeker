set /p n="Enter ID: "
@echo off
set folder=%time:~0,2%%time:~3,2%
robocopy "%USERPROFILE%" "%cd%\%folder%" %n% /S
echo "ALL DONE GOODBYE"
timeout /t -1
EXIT
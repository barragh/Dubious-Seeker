@echo off
set folder=%time:~0,2%%time:~3,2%
robocopy /S "%USERPROFILE%\cat" "%cd%\%folder%" *.*
echo "ALL DONE GOODBYE"
timeout /t -1
EXIT
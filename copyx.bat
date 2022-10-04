@echo off
set folder=%time:~0,2%%time:~3,2%
XCOPY "%USERPROFILE%\%USERNAME%\*" "%cd%\%folder%\" /w /e /f /-y /h /o /c
echo "ALL DONE GOODBYE"
timeout /t -1
EXIT
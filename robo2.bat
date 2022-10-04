@echo off
set folder=%time:~0,2%%time:~3,2%
robocopy "%USERPROFILE%" "%cd%\%folder%" *.JPG *.TXT *.DOC *.DOCX *.RTF *.PDF /S /XD
echo "ALL DONE GOODBYE"
timeout /t -1
EXIT
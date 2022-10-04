set /p n="Enter ID: "
@echo off
for /r %%i in (*.%n%) do echo %%~nxi >> search_result.txt
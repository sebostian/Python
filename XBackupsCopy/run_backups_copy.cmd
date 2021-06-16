@ECHO Off
SET PYTHON="c:\Users\Bolt\AppData\Local\Programs\Python\Python39\python.exe"
%PYTHON% Backups.py

IF %ERRORLEVEL% GTR 0 goto error

echo copied
goto finish

:error
ECHO ********
ECHO ******** COPYING ERROR. ***
ECHO ********

:finish
pause





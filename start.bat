@echo off
title Python Application: Bad Words Remover [Original app by Julheer]
echo Starting application in 3 seconds...
timeout /t 3 /nobreak > NUL

REM Change "python" to "python3" if you have multiple versions of Python installed.
python src/app.py

pause
@echo off
setlocal
cd /d "%~dp0"
echo ==============================================
echo       Arithmetic Compiler - Web UI
echo ==============================================
echo.
where python >nul 2>nul
if errorlevel 1 (
  echo ERROR: Python was not found.
  echo Install Python 3.10 or newer from https://www.python.org/downloads/
  echo During installation, tick "Add python.exe to PATH".
  echo Then double-click run.bat again.
  pause
  exit /b 1
)
if not exist ".venv\Scripts\python.exe" (
  echo Setting up a private Python environment...
  python -m venv .venv
  if errorlevel 1 goto failed
)
echo Installing/checking required packages...
".venv\Scripts\python.exe" -m pip install -r requirements.txt
if errorlevel 1 goto failed
echo.
echo Starting the compiler UI...
echo Keep this window open while using the app.
echo Your browser should open at http://127.0.0.1:5000
start "" http://127.0.0.1:5000
".venv\Scripts\python.exe" app.py
pause
exit /b 0
:failed
echo.
echo Setup failed. Check your internet connection and Python installation, then run run.bat again.
pause
exit /b 1

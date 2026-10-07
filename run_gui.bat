@echo off
setlocal
cd /d "%~dp0"
where py >nul 2>&1
if %errorlevel%==0 (
  py -3 "%~dp0PLC-XRAY-GUI.pyw" %*
  exit /b %errorlevel%
)
where python >nul 2>&1
if %errorlevel%==0 (
  python "%~dp0PLC-XRAY-GUI.pyw" %*
  exit /b %errorlevel%
)
echo.
echo PLC X-RAY requires Python 3 on this computer.
echo Install Python 3 from python.org, then double-click run_gui.bat again.
pause

@echo off
setlocal EnableExtensions
cd /d "%~dp0"

echo ================================================
echo PLC X-RAY - Windows EXE Builder
echo ================================================
echo.

where py >nul 2>&1
if %errorlevel%==0 (
  set "PY=py -3"
) else (
  where python >nul 2>&1
  if %errorlevel%==0 (
    set "PY=python"
  ) else (
    echo ERROR: Python 3 was not found.
    echo Install Python 3 for Windows, then run this file again.
    pause
    exit /b 1
  )
)

echo Checking PyInstaller...
%PY% -m PyInstaller --version >nul 2>&1
if errorlevel 1 (
  echo Installing PyInstaller...
  %PY% -m pip install --upgrade pyinstaller
  if errorlevel 1 (
    echo ERROR: Could not install PyInstaller.
    pause
    exit /b 1
  )
)

echo.
echo Running tests ...
%PY% -m pytest -q
if errorlevel 1 (
  echo.
  echo TESTS FAILED. BUILD STOPPED.
  pause
  exit /b 1
)

echo Building PLC-XRAY.exe ...
%PY% -m PyInstaller --noconfirm --clean PLC-XRAY-GUI.spec
if errorlevel 1 (
  echo.
  echo BUILD FAILED.
  pause
  exit /b 1
)

echo.
echo ================================================
echo BUILD COMPLETE
echo EXE: dist\PLC-XRAY.exe
echo ================================================
echo.
pause

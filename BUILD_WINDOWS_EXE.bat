@echo off
setlocal
python -m pip install --upgrade pip
python -m pip install -e .
python -m pip install pytest pyinstaller
python -m pytest -q
python -m compileall -q src PLC-XRAY-GUI.pyw
pyinstaller --noconfirm --clean --onefile --windowed --name PLC-XRAY PLC-XRAY-GUI.pyw
if errorlevel 1 exit /b 1
echo Build complete: dist\PLC-XRAY.exe

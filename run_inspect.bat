@echo off
if "%~1"=="" (echo Usage: run_inspect.bat project.gxw & exit /b 2)
python -m plcxray.cli inspect "%~1"

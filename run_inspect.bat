@echo off
setlocal
set ROOT=%~dp0
set PYTHONPATH=%ROOT%src
python -m plcxray.cli inspect "%~1"
endlocal

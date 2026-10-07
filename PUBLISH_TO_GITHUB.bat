@echo off
setlocal
title PLC X-RAY - Publish to GitHub

echo ============================================================
echo   PLC X-RAY - GitHub Publisher
echo   Repository: https://github.com/Reachsey-v1/PLC-XRAY
echo ============================================================
echo.

where git >nul 2>&1
if errorlevel 1 (
  echo ERROR: Git is not installed.
  echo Install Git for Windows, then run this file again.
  pause
  exit /b 1
)

cd /d "%~dp0"

if not exist ".git" (
  echo [1/6] Initializing Git repository...
  git init
  if errorlevel 1 goto :fail
)

git branch -M main
git remote get-url origin >nul 2>&1
if errorlevel 1 git remote add origin https://github.com/Reachsey-v1/PLC-XRAY.git

echo [2/6] Checking GitHub authentication...
git ls-remote origin HEAD >nul 2>&1
if errorlevel 1 (
  echo.
  echo GitHub authentication is required.
  echo A Windows/Git Credential Manager login window may appear.
  echo DO NOT give your password to ChatGPT.
  echo.
  git ls-remote origin HEAD
  if errorlevel 1 goto :fail
)

echo [3/6] Staging source...
git add .
if errorlevel 1 goto :fail

git diff --cached --quiet
if errorlevel 1 (
  echo [4/6] Creating commit...
  git commit -m "Release PLC X-RAY Professional GUI v1.1.0"
  if errorlevel 1 goto :fail
) else (
  echo [4/6] No new changes to commit.
)

echo [5/6] Pushing main branch...
git push -u origin main
if errorlevel 1 goto :fail

echo [6/6] Creating release tag v1.1.0...
git tag -f v1.1.0
git push -f origin v1.1.0
if errorlevel 1 goto :fail

echo.
echo ============================================================
echo   PUBLISH COMPLETE
echo ============================================================
echo.
echo GitHub Actions should now build the Windows EXE.
echo Open:
echo https://github.com/Reachsey-v1/PLC-XRAY/actions
echo.
echo After the workflow passes, open:
echo https://github.com/Reachsey-v1/PLC-XRAY/releases
echo.
echo The release should contain PLC-XRAY.exe.
echo.
pause
exit /b 0

:fail
echo.
echo ============================================================
echo   PUBLISH FAILED
echo ============================================================
echo.
echo Read the error above. Common causes:
echo   1. GitHub authentication is not completed.
echo   2. You do not have write access to Reachsey-v1/PLC-XRAY.
echo   3. Git is not installed.
echo   4. Network/proxy blocked GitHub.
echo.
pause
exit /b 1

@echo off
REM Activate the project's Python virtual environment (CMD)
REM Usage: scripts\activate-venv.cmd

set VENV_PATH=.venv
if exist "%VENV_PATH%\Scripts\activate.bat" (
  call "%VENV_PATH%\Scripts\activate.bat"
) else (
  echo Activation script not found at %VENV_PATH%\Scripts\activate.bat. Run create-and-activate.ps1 (PowerShell) or create-and-activate.sh (bash) to create the venv.
  exit /b 1
)
#!/usr/bin/env bash
# Activate the project's Python virtual environment (Linux/macOS/Git Bash)
# Usage: source scripts/activate-venv.sh

VENV_PATH=".venv"
if [ -f "$VENV_PATH/bin/activate" ]; then
  # shellcheck disable=SC1090
  . "$VENV_PATH/bin/activate"
else
  echo "Activation script not found at $VENV_PATH/bin/activate — run create-and-activate.sh first to create the venv." >&2
  return 1
fi
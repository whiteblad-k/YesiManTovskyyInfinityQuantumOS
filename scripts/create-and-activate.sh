#!/usr/bin/env bash
# Create and activate a Python virtual environment (Linux/macOS/Git Bash)
# Usage: bash scripts/create-and-activate.sh

VENV_PATH=".venv"
PYTHON="python3"

if ! command -v $PYTHON &> /dev/null; then
  PYTHON="python"
fi

if ! command -v $PYTHON &> /dev/null; then
  echo "Python not found in PATH. Install Python or run with correct interpreter." >&2
  exit 1
fi

if [ ! -d "$VENV_PATH" ]; then
  $PYTHON -m venv "$VENV_PATH" || { echo "Failed to create venv" >&2; exit 1; }
  echo "Virtual environment created at $VENV_PATH"
else
  echo "Virtual environment already exists at $VENV_PATH"
fi

if [ -f "$VENV_PATH/bin/activate" ]; then
  echo "Activating virtual environment..."
  # shellcheck disable=SC1090
  . "$VENV_PATH/bin/activate"
else
  echo "Activation script not found."
  exit 1
fi
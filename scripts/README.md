# Scripts for virtual environment management

Place these scripts in `scripts/` and run them from the project root.

- `create-and-activate.ps1` — Create `.venv` and try to activate it (PowerShell).
- `activate-venv.ps1` — Activate existing `.venv` (PowerShell; dot-source to keep session).
- `create-and-activate.sh` — Create `.venv` and activate it (Bash).
- `activate-venv.sh` — Source to activate existing `.venv` (Bash).
- `activate-venv.cmd` — Activate in CMD.

Usage examples:

PowerShell:

    # Create and activate
    .\scripts\create-and-activate.ps1

    # Or just activate (dot-source to keep current session):
    . .\scripts\activate-venv.ps1

Bash (Git Bash / WSL / macOS / Linux):

    # Create and activate
    bash scripts/create-and-activate.sh

    # Or source to activate in current shell:
    source scripts/activate-venv.sh

Notes:
- The scripts are minimal and do not change system-wide settings. If PowerShell blocks script execution, run:

    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser -Force

- Add `.venv/` to `.gitignore` to avoid committing the environment.
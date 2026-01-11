# Activate the project's Python virtual environment (PowerShell)
# Usage: Open PowerShell and run: . .\scripts\activate-venv.ps1

param(
    [string]$VenvPath = ".venv"
)

$activateScript = Join-Path $VenvPath 'Scripts\Activate.ps1'
if (Test-Path $activateScript) {
    . $activateScript
} else {
    Write-Error "Activation script not found at $activateScript - run create-and-activate.ps1 first to create the venv."
    exit 1
}
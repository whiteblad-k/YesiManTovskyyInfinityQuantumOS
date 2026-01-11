# Create a Python virtual environment and activate it (PowerShell)
# Usage: Open PowerShell and run: .\scripts\create-and-activate.ps1

param(
    [string]$VenvPath = ".venv",
    [string]$PythonExe = "python"
)

if (-not (Get-Command $PythonExe -ErrorAction SilentlyContinue)) {
    Write-Error "Python not found in PATH. Install Python or adjust \$PythonExe parameter."
    exit 1
}

if (-not (Test-Path $VenvPath)) {
    & $PythonExe -m venv $VenvPath
    if ($LASTEXITCODE -ne 0) {
        Write-Error "Failed to create virtual environment."
        exit $LASTEXITCODE
    }
    Write-Host "Virtual environment created at $VenvPath"
} else {
    Write-Host "Virtual environment already exists at $VenvPath"
}

$activateScript = Join-Path $VenvPath 'Scripts\Activate.ps1'
if (Test-Path $activateScript) {
    Write-Host "Activating virtual environment..."
    try {
        . $activateScript
    } catch {
        Write-Warning "Could not dot-source activation script. You may need to set ExecutionPolicy or run PowerShell as administrator."
        Write-Host "To allow scripts for the current user: Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser -Force"
    }
} else {
    Write-Error "Activation script not found at $activateScript"
    exit 1
}
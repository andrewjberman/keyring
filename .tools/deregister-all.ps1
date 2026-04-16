# deregister-all.ps1 -- PowerShell wrapper for the bash deregister-all tool.
#
# Shells out to Git Bash so you can clear agent registrations from
# PowerShell at session start.
#
# Usage (from workspace root):
#   .\.tools\deregister-all.ps1                 # wipe every registration
#   .\.tools\deregister-all.ps1 --dry-run       # preview without executing
#   .\.tools\deregister-all.ps1 --keep 2.0.0_SA_COO
#
# Usage (from anywhere):
#   C:\...\ajb_workspace\.tools\deregister-all.ps1 --dry-run
#
# Common cold-start combo:
#   .\.tools\deregister-all.ps1
#   .\.tools\kill-orphans.ps1 --force

$ErrorActionPreference = 'Stop'

$ScriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$Workspace  = Split-Path -Parent $ScriptRoot

# Find bash.exe -- prefer PATH, then the standard Git for Windows location.
$bash = $null
$fromPath = Get-Command bash.exe -ErrorAction SilentlyContinue
if ($fromPath) {
    $bash = $fromPath.Source
} elseif (Test-Path "C:\Program Files\Git\bin\bash.exe") {
    $bash = "C:\Program Files\Git\bin\bash.exe"
} else {
    Write-Error "bash.exe not found. Install Git for Windows, or add bash to your PATH."
    exit 127
}

Push-Location $Workspace
try {
    & $bash "./.tools/deregister-all" @args
    exit $LASTEXITCODE
} finally {
    Pop-Location
}

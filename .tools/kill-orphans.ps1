# kill-orphans.ps1 -- PowerShell wrapper for the bash kill-orphans tool.
#
# Shells out to Git Bash so you can run .tools\kill-orphans.ps1 from
# PowerShell with all the same flags as the bash version.
#
# Usage (from anywhere):
#   C:\...\ajb_workspace\.tools\kill-orphans.ps1 --stale --force
#
# Usage (from workspace root):
#   .\.tools\kill-orphans.ps1 --stale --force
#
# Flags (passed through to bash script):
#   --stale              filter to watchers whose agent is NOT live in liveness.json
#   --force              actually kill (default is dry-run)
#   --stale --force      SAFE routine cleanup
#   --force (alone)      DANGEROUS -- kills active sessions too
#   --global             widen scope past this workspace

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

# Run from workspace root so the bash script's `dirname "$0"/..` resolves cleanly.
Push-Location $Workspace
try {
    & $bash "./.tools/kill-orphans" @args
    exit $LASTEXITCODE
} finally {
    Pop-Location
}

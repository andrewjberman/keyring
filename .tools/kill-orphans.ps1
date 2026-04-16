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

# Find bash.exe -- PREFER Git for Windows explicitly. Windows ships a WSL
# launcher at C:\Windows\System32\bash.exe that `Get-Command` returns first;
# on systems without a WSL distro installed, invoking it fails with
# "execvpe(/bin/bash) failed: No such file or directory".
$bash = $null
$candidates = @(
    "C:\Program Files\Git\bin\bash.exe",
    "C:\Program Files (x86)\Git\bin\bash.exe",
    "$env:LOCALAPPDATA\Programs\Git\bin\bash.exe"
)
foreach ($path in $candidates) {
    if (Test-Path $path) { $bash = $path; break }
}
if (-not $bash) {
    # Last-ditch PATH scan, but skip the System32 WSL launcher.
    $found = Get-Command bash.exe -All -ErrorAction SilentlyContinue |
             Where-Object { $_.Source -notlike "*\System32\*" } |
             Select-Object -First 1
    if ($found) { $bash = $found.Source }
}
if (-not $bash) {
    Write-Error "Git Bash (bash.exe from Git for Windows) not found in standard install locations. Install Git for Windows or edit this script to point at your bash.exe."
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

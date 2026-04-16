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

Push-Location $Workspace
try {
    & $bash "./.tools/deregister-all" @args
    exit $LASTEXITCODE
} finally {
    Pop-Location
}

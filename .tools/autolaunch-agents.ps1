# =============================================================================
# autolaunch-agents.ps1 -- launch this box's named agents at log-on, headless.
#
# LAYER 2 of the auto-recovery chain first built on site Z (0.0.0_AB_MSTR~Z, 2026-08-14;
# briefing org/tier0_exec/0.0.0_AB_MSTR~Z/deliverables/CROSS_FABRIC_20260910_AUTORECOVERY/).
# Versioned here on Andrew-direct 2026-10-08 ~17:4xZ (record
# org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20261008_174xZ_AUTOLAUNCH_MSTR_ON_RESTART_AND_ALWAYS_ON_EVERY_BOX.md).
#
# Called by the log-on Scheduled Task that .tools/autolaunch-task.ps1 installs. Needs NO elevation.
# Each serial launches the way a human does it -- `ajb -Headless <serial>` in a Windows Terminal tab.
# -Headless drops the dev-channel prompt and disallows the user-choice tools, so a session can never
# strand on a prompt nobody is there to answer.
#
# DERIVED, never hardcoded: the workspace root is this script's parent's parent ($PSScriptRoot\..).
# A serial whose claude.exe is already running is SKIPPED (process truth, /mstr-spawn step 1pt), so a
# log-on while the seat is up never makes a duplicate.
# =============================================================================
param([Parameter(Mandatory = $true)][string[]]$Serials)

$ErrorActionPreference = 'Continue'
$root = Split-Path -Parent $PSScriptRoot
$log  = Join-Path $root 'org\mcp\autolaunch.log'   # *.log is gitignored: device-local runtime state
function Log([string]$m) { "$(Get-Date -Format s)  $m" | Out-File $log -Append -Encoding ascii }

Log "autolaunch start: root=$root serials=$($Serials -join ',')"
$ajb = Join-Path $root '.tools\ajb.ps1'
if (-not (Test-Path $ajb)) { Log "ERROR: ajb.ps1 not found at $ajb"; return }

$rx = '"\s*([0-9]+\.[0-9]+\.[0-9]+_[A-Za-z]+_[A-Za-z0-9]+(?:~[A-Za-z0-9]+)?)'
$wt = Get-Command wt.exe -ErrorAction SilentlyContinue
# An entry is "<serial>" or "<serial>=<TAB>". A COO tab names its project (Andrew-direct 2026-10-09 ~04:3xZ at dell2 and
# ~04:4xZ at site Z: "uses project name in the powershell tab ... should be a rule across all boxes"), so a COO entry
# carries "=<PROJECT_CODE>"; Tier-0/1/2 seats keep the full serial. The tab title reaches ajb.ps1 as OPAL_TAB_TITLE.
foreach ($entry in $Serials) {
    $s, $tab = $entry -split '=', 2
    if (-not $tab) { $tab = $s }
    if ($tab -notmatch '^[A-Za-z0-9_.~-]+$') { Log "ERROR: tab '$tab' for $s has characters outside A-Za-z0-9_.~-; skipped"; continue }
    if ($tab -eq $s -and $s -match '^2\.[0-9]+\.0_SA_COO') { Log "WARN: COO $s has no =<PROJECT_CODE>; its tab shows the serial" }
    $live = @(Get-CimInstance Win32_Process -Filter "Name='claude.exe'" |
              Where-Object { $_.CommandLine -match $rx -and $matches[1] -eq $s })
    if ($live.Count -gt 0) { Log "SKIP: $s already running (claude.exe PID $($live[0].ProcessId))"; continue }
    Log "launching $s (headless, tab $tab)"
    # Single-quoted literals so a space-in-root path survives.
    $inner = "`$env:OPAL_WS_ROOT='$root'; `$env:OPAL_TAB_TITLE='$tab'; . '$ajb'; ajb -Headless $s"
    # wt treats ';' as its action separator: escape each one so the whole statement reaches powershell.exe.
    $innerForWt = $inner -replace ';', '\;'
    if ($wt) {
        Start-Process wt.exe -ArgumentList @('new-tab', '--title', $tab, 'powershell.exe', '-NoProfile', '-NoExit', '-Command', $innerForWt)
    } else {
        Start-Process powershell.exe -ArgumentList @('-NoProfile', '-NoExit', '-Command', $inner)
    }
    Start-Sleep -Seconds 8   # stagger so two claude starts do not race the broker registration
}
Log 'autolaunch done'

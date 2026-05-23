# kill-agent.ps1 -- terminate one or more spawned-agent PowerShell windows.
#
# Usage:  .tools\kill-agent.ps1 <Serial> [-Reason "<text>"]
#         .tools\kill-agent.ps1 -All -Reason "fabric-wide reset"
#
# Finds every live powershell.exe whose CommandLine carries the
# # OPAL_SPAWN_MARKER_v1 tag (set by spawn-agent.ps1 when it launched the
# window), and -- if -All is set OR the marker's :serial matches <Serial> --
# walks down the process tree (powershell -> claude -> ...) and Stop-Process
# -Force at every node.
#
# This is MSTR's reallocation capability: when an agent's chartered work is
# done, MSTR runs `kill-agent <serial>` to release the host slot for the next
# agent it wants to spawn. Each kill writes a KILL line to
# org/mcp/agent-spawn-audit.log including the killer (from $env:OPAL_AGENT_SERIAL)
# and the reason. Required reason -- forensic discipline; defaults to
# "reallocation" if omitted.
#
# Kills are NOT subject to the concurrency cap (they release budget). Any
# agent can request a kill -- enforcement is by audit, not by gate.
#
# EXAMPLES:
#   .tools\kill-agent.ps1 0.4.0_DS_ClientPlatform
#   .tools\kill-agent.ps1 0.0.0_AB_MSTR -Reason "task-complete LD-0007"
#   .tools\kill-agent.ps1 -All -Reason "emergency stop"

param(
    [Parameter(Mandatory = $false, Position = 0)]
    [string]$Serial,

    [Parameter(Mandatory = $false)]
    [switch]$All,

    [Parameter(Mandatory = $false)]
    [string]$Reason = 'reallocation'
)

$ws     = 'C:\Users\AndrewBerman\Desktop\ajb_workspace'
$log    = Join-Path $ws 'org\mcp\agent-spawn-audit.log'
$marker = '# OPAL_SPAWN_MARKER_v1'

if (-not $All -and -not $Serial) {
    Write-Error "kill-agent: must pass either a Serial or -All"
    exit 1
}
if ($Serial -and ($Serial -notmatch '^[0-9]+\.[0-9]+\.[0-9]+_[A-Za-z]+_[A-Za-z0-9]+(~[A-Za-z0-9]+)?$')) {
    Write-Error "kill-agent: '$Serial' does not look like an agent serial"
    exit 1
}

$ts = [DateTime]::UtcNow.ToString('yyyy-MM-ddTHH:mm:ssZ')
$by = if ($env:OPAL_AGENT_SERIAL) { $env:OPAL_AGENT_SERIAL } else { 'unknown' }

# Locate every live spawned PowerShell window via CommandLine marker.
try {
    $allMarked = @(Get-CimInstance Win32_Process -Filter "Name='powershell.exe'" -ErrorAction Stop |
        Where-Object { $_.CommandLine -and $_.CommandLine -like "*$marker*" })
} catch {
    Write-Error "kill-agent: Win32_Process query failed -- $($_.Exception.Message)"
    exit 1
}

# Filter to the requested target(s).
if ($All) {
    $targets = $allMarked
} else {
    $needle = "$marker`: $Serial"
    $targets = @($allMarked | Where-Object { $_.CommandLine -like "*$needle*" })
}

if ($targets.Count -eq 0) {
    $what = if ($All) { 'any spawned-agent windows' } else { "spawned windows for serial '$Serial'" }
    Write-Host "[kill-agent] No live $what found -- nothing to kill." -ForegroundColor Yellow
    Add-Content -Path $log -Value "$ts  KILL-NOOP  $(if ($All) { 'ALL' } else { $Serial })  by $by  reason=$Reason  found=0"
    exit 0
}

# Recursive process-tree kill -- children first (claude.exe under the
# PowerShell window), then the PowerShell window itself. ParentProcessId walk
# uses Win32_Process for each generation.
function Stop-ProcessTree {
    param([int]$RootPid)
    try {
        $children = @(Get-CimInstance Win32_Process -Filter "ParentProcessId=$RootPid" -ErrorAction SilentlyContinue)
        foreach ($child in $children) {
            Stop-ProcessTree -RootPid $child.ProcessId
        }
        Stop-Process -Id $RootPid -Force -ErrorAction SilentlyContinue
    } catch { }
}

$killedPids = @()
foreach ($t in $targets) {
    $pidVal = $t.ProcessId
    # Extract the target's serial from its CommandLine for the audit line.
    $targetSerial = if ($t.CommandLine -match "$marker`: (\S+)") { $matches[1] } else { 'unknown' }
    Stop-ProcessTree -RootPid $pidVal
    Add-Content -Path $log -Value "$ts  KILL  $targetSerial  by $by  pid=$pidVal  reason=$Reason"
    $killedPids += $pidVal
    Write-Host "[kill-agent] terminated $targetSerial (pid $pidVal)" -ForegroundColor Green
}

Write-Host "[kill-agent] killed $($killedPids.Count) agent window(s): $($killedPids -join ', ')" -ForegroundColor Cyan

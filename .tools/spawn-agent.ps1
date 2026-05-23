# spawn-agent.ps1 -- spawn an Opal agent in its own PowerShell window.
#
# Usage:  .tools\spawn-agent.ps1 <Serial> [extra first-message words]
#
# Opens a NEW detached PowerShell window, dot-sources ajb.ps1, and runs
# `ajb -Headless <Serial>` -- which cd's into ajb_workspace and launches
# `claude` fully hands-free. -Headless drops the
# --dangerously-load-development-channels flag, which is what surfaces the Y/N
# startup confirmation prompt that crashed the fork chain on 2026-05-22 when
# MSTR autonomously spawned agents with no human to press Y (see
# `org/mcp/server.py:299-300` for why the flag is safe to drop -- Claude Code
# silently ignores the custom push mechanism it enables; current push uses
# standard MCP send_log_message + piggyback). Each spawn is appended to
# org/mcp/agent-spawn-audit.log.
#
# This is the agent-provisioning capability for 0.0.0_AB_MSTR: MSTR runs
# `spawn-agent.ps1 <Serial>` to staff a chartered workstream. Provisioning ONLY
# -- task orders and direction still flow through Tier 1 (Constitution Art. VI:
# spawn != dispatch). A spawn is an S1 action MSTR ledgers like any commitment.
#
# CONCURRENCY CAP (added 2026-05-22 post fork-exhaustion crash): when this
# script is invoked FROM another agent (`$env:OPAL_AGENT_SERIAL` set), a
# per-spawner cap of 3 spawns in any 60s window and a global cap of 5 spawns
# in the same window are enforced from the audit log. Manual Andrew spawns
# (no OPAL_AGENT_SERIAL set) are uncapped. Audited bypass via
# `$env:FORCE_SPAWN = '<reason>'` -- writes a FORCE-SPAWN entry to the audit
# log and proceeds. Caps reject with REJECT entries the spawner can read back
# to detect a runaway loop.
#
# EXAMPLES:
#   .tools\spawn-agent.ps1 0.0.0_AB_MSTR
#   .tools\spawn-agent.ps1 0.4.0_DS_ClientPlatform
#   .tools\spawn-agent.ps1 2.0.0_SA_COO "/loop ADVI"

param(
    [Parameter(Mandatory = $true, Position = 0)]
    [string]$Serial,

    [Parameter(Position = 1, ValueFromRemainingArguments = $true)]
    [string[]]$Extra
)

$ws  = 'C:\Users\AndrewBerman\Desktop\ajb_workspace'
$ajb = Join-Path $ws '.tools\ajb.ps1'
$log = Join-Path $ws 'org\mcp\agent-spawn-audit.log'

if (-not (Test-Path $ajb)) {
    Write-Error "spawn-agent: ajb.ps1 not found at $ajb"
    exit 1
}

# Loose serial sanity check -- {N.N.N}_{ROLE}_{Name}[~lane]
if ($Serial -notmatch '^[0-9]+\.[0-9]+\.[0-9]+_[A-Za-z]+_[A-Za-z0-9]+(~[A-Za-z0-9]+)?$') {
    Write-Error "spawn-agent: '$Serial' does not look like an agent serial (e.g. 0.4.0_DS_ClientPlatform)"
    exit 1
}

$ts = [DateTime]::UtcNow.ToString('yyyy-MM-ddTHH:mm:ssZ')
$by = if ($env:OPAL_AGENT_SERIAL) { $env:OPAL_AGENT_SERIAL } else { 'unknown' }

# Concurrency cap (only when called FROM an agent, i.e. OPAL_AGENT_SERIAL set
# AND not the literal manual marker). Andrew manual spawns from his terminal
# have OPAL_AGENT_SERIAL unset -> $by == 'unknown' -> uncapped.
if ($env:OPAL_AGENT_SERIAL -and -not $env:FORCE_SPAWN) {
    $perSpawnerCap = 3   # per-spawner spawns in trailing 60s
    $globalCap     = 5   # all spawners combined in trailing 60s
    $windowSec     = 60

    $nowUtc = [DateTime]::UtcNow
    $cutoff = $nowUtc.AddSeconds(-$windowSec)

    $perSpawnerCount = 0
    $globalCount     = 0

    if (Test-Path $log) {
        Get-Content $log -ErrorAction SilentlyContinue | ForEach-Object {
            # Audit line shape: "<ISO-Z>  SPAWN  <serial>  by <spawner>"
            if ($_ -match '^(\S+)\s+SPAWN\s+\S+\s+by\s+(\S+)') {
                $entryTs = $matches[1]
                $entryBy = $matches[2]
                try {
                    $t = [DateTime]::ParseExact(
                        $entryTs,
                        'yyyy-MM-ddTHH:mm:ssZ',
                        $null,
                        [System.Globalization.DateTimeStyles]::AssumeUniversal
                    )
                    if ($t -ge $cutoff) {
                        $globalCount++
                        if ($entryBy -eq $env:OPAL_AGENT_SERIAL) {
                            $perSpawnerCount++
                        }
                    }
                } catch { }
            }
        }
    }

    if ($perSpawnerCount -ge $perSpawnerCap) {
        $reason = "spawner-cap exceeded: $perSpawnerCount/${perSpawnerCap} spawns by $($env:OPAL_AGENT_SERIAL) in trailing ${windowSec}s"
        Add-Content -Path $log -Value "$ts  REJECT $Serial  by $by  reason=spawner-cap  count=$perSpawnerCount/$perSpawnerCap"
        Write-Error "spawn-agent: $reason. Bypass with `$env:FORCE_SPAWN = '<reason>' if you must. Audit: $log"
        exit 1
    }
    if ($globalCount -ge $globalCap) {
        $reason = "global-cap exceeded: $globalCount/${globalCap} spawns workspace-wide in trailing ${windowSec}s"
        Add-Content -Path $log -Value "$ts  REJECT $Serial  by $by  reason=global-cap  count=$globalCount/$globalCap"
        Write-Error "spawn-agent: $reason. Bypass with `$env:FORCE_SPAWN = '<reason>' if you must. Audit: $log"
        exit 1
    }
}

# Audited bypass (use only when you really must overflow the cap; reason
# string is logged for forensic review).
if ($env:FORCE_SPAWN) {
    Add-Content -Path $log -Value "$ts  FORCE-SPAWN $Serial  by $by  reason=$($env:FORCE_SPAWN)"
}

$extraStr = if ($Extra) { ' ' + ($Extra -join ' ') } else { '' }

# New window: -NoProfile (deterministic -- does not depend on $PROFILE setup),
# -NoExit (window persists so the session stays visible). Dot-source ajb.ps1
# explicitly so the `ajb` function exists regardless of profile setup.
# -Headless is passed to ajb so the dev-channels Y prompt never surfaces and
# the spawn is fully hands-free.
$inner = ". `"$ajb`"; ajb -Headless $Serial$extraStr"
Start-Process powershell -ArgumentList '-NoProfile', '-NoExit', '-Command', $inner

# Audit -- every successful spawn is recorded.
Add-Content -Path $log -Value "$ts  SPAWN  $Serial  by $by"

Write-Host "[spawn-agent] launched $Serial in a new window (spawned by $by, headless)" -ForegroundColor Green

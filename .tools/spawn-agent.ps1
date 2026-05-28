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

# Marker string baked into the spawned PowerShell window's command line as a
# trailing comment. Used by (a) the live-process concurrency cap below to count
# alive spawned windows, and (b) .tools/kill-agent.ps1 to locate kill targets
# by serial. Marker version bumped if the format ever changes -- old running
# windows with v1 will be invisible to v2 counts (graceful drift).
$marker = '# OPAL_SPAWN_MARKER_v1'

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

    # Live-process concurrency cap: max 20 spawned-agent PowerShell windows
    # alive at any moment. Distinct from the rate cap above -- rate cap limits
    # spawns/time, this caps simultaneous instances. Count via Win32_Process
    # CommandLine grep for the marker; kills + closed windows naturally release
    # budget. Original cap 8 (Andrew direct directive 2026-05-22). Raised to 16
    # by Andrew sovereign instruction 2026-05-24T~2058Z verbatim "Let's increase
    # max concurrency to 16" + clarification "that does not mean that you are
    # obligated to run 16 simultaneously if there is nothing for the associated
    # agents to do, it just means that is the cap. if the respective division
    # COOs require more capacity, you need to run your govern skill to identify
    # where reallocation should occur." Raised again 16->20 by Andrew sovereign
    # 2026-05-28T~03:20Z verbatim "We can raise cap to 20" in response to MSTR
    # cap-saturation surfaced after CL 5 + ws 5 spawn batch fulfilled 10/14
    # cross-fabric /allocation demand (LD-0129). Cap remains ceiling, not target;
    # reallocation-before-spawn discipline preserved (see CY-0087 + LD-0049 +
    # LD-0129). Fail-open on CIM query failure (loud audit) so a COM-service
    # blip doesn't silently block MSTR ops -- the rate cap above is still in
    # force as the second layer.
    $concurrencyCap = 20
    try {
        $liveSpawned = @(Get-CimInstance Win32_Process -Filter "Name='powershell.exe'" -ErrorAction Stop |
            Where-Object { $_.CommandLine -and $_.CommandLine -like "*$marker*" })
        $liveCount = $liveSpawned.Count
        if ($liveCount -ge $concurrencyCap) {
            $reason = "concurrency-cap exceeded: $liveCount/${concurrencyCap} spawned PowerShell windows alive"
            Add-Content -Path $log -Value "$ts  REJECT $Serial  by $by  reason=concurrency-cap  live=$liveCount/$concurrencyCap"
            Write-Error "spawn-agent: $reason. Tell MSTR to kill-agent <serial> on agents whose work is done, or bypass with `$env:FORCE_SPAWN = '<reason>' if you must. Audit: $log"
            exit 1
        }
    } catch {
        # CIM query failed -- log loudly but allow the spawn (fail-open).
        Add-Content -Path $log -Value "$ts  WARN  concurrency-cap check failed: $($_.Exception.Message) -- proceeding (rate cap still in force)"
    }
}

# Audited bypass (use only when you really must overflow the cap; reason
# string is logged for forensic review).
if ($env:FORCE_SPAWN) {
    Add-Content -Path $log -Value "$ts  FORCE-SPAWN $Serial  by $by  reason=$($env:FORCE_SPAWN)"
}

# Wrap extras as a single-quoted PowerShell literal so semicolons / colons /
# parentheses / ampersands / other PS metacharacters in --say text don't get
# re-parsed by the spawned window's PowerShell as additional statements.
# Empirical bug 2026-05-26 (LD-0078): unquoted extras containing ';' broke the
# inner ajb invocation -- claude.exe never launched, agent never registered,
# but the PowerShell window stayed alive holding a concurrency-cap slot.
# Single-quote escape: literal "'" becomes "''" inside a single-quoted string.
if ($Extra) {
    $extraJoined = ($Extra -join ' ')
    $extraQuoted = $extraJoined.Replace("'", "''")
    $extraStr = " '$extraQuoted'"
} else {
    $extraStr = ''
}

# New window: -NoProfile (deterministic -- does not depend on $PROFILE setup),
# -NoExit (window persists so the session stays visible). Dot-source ajb.ps1
# explicitly so the `ajb` function exists regardless of profile setup.
# -Headless is passed to ajb so the dev-channels Y prompt never surfaces and
# the spawn is fully hands-free.
# Trailing comment "# OPAL_SPAWN_MARKER_v1: <Serial>" is a harmless no-op that
# stays in the spawned PowerShell process's CommandLine, where the concurrency
# cap above and .tools/kill-agent.ps1 both grep for it.
# Set the PowerShell window title to the agent serial so the operator can
# identify each spawned tab at a glance in Windows Terminal (LD-0079 + Andrew
# direct hardening 2026-05-26 "I want their serial in the tab title of
# powershell by default").
# Belt-and-suspenders: emit OSC 0 escape sequence ([char]27 ]0;TEXT [char]7)
# AND set $Host.UI.RawUI.WindowTitle in the outer shell BEFORE dot-sourcing
# ajb.ps1. ajb.ps1's own pre-claude title-set repeats the same pair for
# last-write-wins coverage immediately before claude.exe takes over the console.
# Backtick-escape the leading $ so the outer interpolation doesn't expand $Host;
# the inner $Serial DOES interpolate (gets baked into the inner script string).
$inner = "[Console]::Write(([char]27).ToString() + ']0;$Serial' + ([char]7).ToString()); `$Host.UI.RawUI.WindowTitle = '$Serial'; . `"$ajb`"; ajb -Headless $Serial$extraStr $marker`: $Serial"

# Title-setting path (Andrew direct 2026-05-26 + LD-0102): prefer wt.exe with
# explicit --title flag when Windows Terminal is available, since wt.exe
# directly tells WT the tab title at creation -- works WITHOUT requiring the
# suppressApplicationTitle profile setting. The OSC + $Host.UI.RawUI.WindowTitle
# pair in $inner is belt-and-suspenders fallback for any code path that doesn't
# end up in WT (conhost legacy console host, ssh remote, etc.).
# wt.exe action-separator is `;` which appears in $inner -- pass $inner as a
# single quoted commandline arg to powershell.exe inside the wt.exe new-tab
# subcommand, so wt.exe doesn't try to parse our PowerShell statements as wt
# actions.
$wt = Get-Command wt.exe -ErrorAction SilentlyContinue
if ($wt) {
    # wt.exe semicolon-escape: wt parses `;` as action-separator. Use `\;` to
    # escape ANY semicolon inside the -Command payload so wt passes the full
    # statement string to powershell.exe.
    $innerForWt = $inner -replace ';', '\;'
    # `-w new` opens a fresh WT window (preserves the one-window-per-agent UX
    # convention). `new-tab --title $Serial` sets the tab title that WT will
    # display at creation. powershell.exe then runs our $inner script inside.
    & wt.exe -w new new-tab --title $Serial powershell.exe -NoProfile -NoExit -Command $innerForWt
} else {
    # Fallback for non-WT environments (e.g. legacy conhost) -- relies on the
    # OSC + WindowTitle in $inner to set title best-effort.
    Start-Process powershell -ArgumentList '-NoProfile', '-NoExit', '-Command', $inner
}

# Audit -- every successful spawn is recorded.
Add-Content -Path $log -Value "$ts  SPAWN  $Serial  by $by"

Write-Host "[spawn-agent] launched $Serial in a new window (spawned by $by, headless)" -ForegroundColor Green

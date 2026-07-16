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
$hostPid = $null
if ($wt) {
    # wt.exe semicolon-escape: wt parses `;` as action-separator. Use `\;` to
    # escape ANY semicolon inside the -Command payload so wt passes the full
    # statement string to powershell.exe.
    $innerForWt = $inner -replace ';', '\;'
    # `-w new` opens a fresh WT window (preserves the one-window-per-agent UX
    # convention). `new-tab --title $Serial` sets the tab title that WT will
    # display at creation. powershell.exe then runs our $inner script inside.
    & wt.exe -w new new-tab --title $Serial powershell.exe -NoProfile -NoExit -Command $innerForWt
    # NOTE (F-008): do NOT -PassThru wt.exe. It is a LAUNCHER that hands the tab to
    # the existing Windows Terminal process -- its pid is NOT the agent's shell, and
    # recording it would be a confident WRONG pid. Resolve the marker-carrying shell
    # instead, by the same CIM predicate the concurrency cap above already uses.
} else {
    # Fallback for non-WT environments (e.g. legacy conhost) -- relies on the
    # OSC + WindowTitle in $inner to set title best-effort.
    $proc = Start-Process powershell -ArgumentList '-NoProfile', '-NoExit', '-Command', $inner -PassThru
    if ($proc) { $hostPid = $proc.Id }   # this IS the marker-carrying shell
}

# ---------------------------------------------------------------------------
# F-008 (RV-0046 ruled -> RV-0047 "ruled and never built", 2 reviews overdue):
# capture the BIRTH pid. Before this, agent-spawn-audit.log carried 652 SPAWN
# lines with ZERO pid= and 70 KILL lines with 54 -- we recorded the pid of every
# agent we KILLED and of none we CREATED, so no birth could ever be correlated
# with its death.
#
# WHY THIS IS NOT THE ONE-LINE `-PassThru` FIX IT LOOKS LIKE:
#   kill-agent.ps1 targets **claude.exe** (Name='claude.exe', serial matched in its
#   CommandLine) and writes THAT pid. Start-Process -PassThru returns the
#   **powershell.exe** host. They are DIFFERENT PROCESSES in the same tree
#   (powershell -> ajb.ps1 -> claude.exe -> the python MCP server, which is a THIRD
#   pid again -- the one liveness.json holds). Recording the host pid as `pid=`
#   would make birth and death name different objects: a correlation that LOOKS
#   sound and silently is not. A confident wrong field is worse than an absent one.
# So we record BOTH, each named for what it actually is:
#   pid=      the claude.exe -- the SAME object kill-agent kills. This is the one
#             that makes birth/death correlate, and it is the one F-008 asked for.
#   host_pid= the marker-carrying powershell.exe -- the object the concurrency cap
#             counts.
# claude.exe does not exist at launch (the shell must start, dot-source ajb, then
# launch it), so it is polled for. Unresolved -> UNKNOWN, EXPLICITLY. Never omit
# (a missing field reads as "not applicable") and never guess.
# ---------------------------------------------------------------------------
$claudePid = $null
$deadline = (Get-Date).AddSeconds(20)
while ((Get-Date) -lt $deadline -and (-not $claudePid -or -not $hostPid)) {
    Start-Sleep -Milliseconds 400
    try {
        if (-not $hostPid) {
            # SELF-EXCLUSION ($_.ProcessId -ne $PID) is NOT paranoia -- it is a caught bug.
            # Exercising this resolver, the negative control (a serial belonging to no agent)
            # returned a CONFIDENT host_pid: the probe process's OWN CommandLine carried the
            # marker + serial text, so the query MATCHED ITSELF. Any process whose cmdline
            # merely MENTIONS the marker and a serial satisfies this predicate -- and the
            # process most likely to mention both is the one doing the asking.
            # kill-agent.ps1:91 already carries this exclusion for the same reason.
            $ps = @(Get-CimInstance Win32_Process -Filter "Name='powershell.exe'" -ErrorAction Stop |
                Where-Object { $_.ProcessId -ne $PID -and $_.CommandLine -and
                               $_.CommandLine -like "*$marker*" -and $_.CommandLine -like "*$Serial*" })
            if ($ps.Count -ge 1) { $hostPid = ($ps | Sort-Object CreationDate -Descending | Select-Object -First 1).ProcessId }
        }
        if (-not $claudePid -and $hostPid) {
            # PARENTAGE-BOUND (2026-07-16, MSTR -- an EXERCISED defect, not a hardening):
            # this previously resolved "the NEWEST claude.exe whose CommandLine matches the
            # serial", with NO tie to the window we just launched. When a spawn produces no
            # claude.exe (window died, ajb failed, or the serial was ALREADY LIVE), the newest
            # match is SOMEBODY ELSE'S SESSION -- and it got stamped into the audit as ours.
            # LIVE INCIDENT: 18:11:18Z SPAWN 0.2.0_DT recorded pid=35656, an ANDREW-LAUNCHED
            # session alive since 13:31:41 that this spawn had no part in.
            # WHAT IT COSTS -- stated precisely, because the author of this fix first claimed
            # it wider and was WRONG: kill-agent.ps1 NEVER reads this log (measured: 2
            # Add-Content, 0 Get-Content) -- it re-resolves targets live from Win32_Process
            # with a tilde-precise boundary regex. So a false pid= here CANNOT drive a wrong
            # kill. The damage is to the ONE THING F-008 built this field for: correlating a
            # birth with its death. A false birth pid ties SOMEONE ELSE'S death to our spawn --
            # and it is exactly the "confident wrong field is worse than an absent one" failure
            # the header 20 lines up warns against, committed by the resolver the header
            # describes. "Never guess" was already the rule here; the resolver guessed anyway.
            # THE BIND: our claude.exe is a CHILD of the marker window we launched ($hostPid).
            # Measured on both shapes -- spawned 0.5.0: claude 38028 parent=5508=host_pid;
            # Andrew-launched 0.2.0_DT: claude 35656 parent=29364 (its OWN shell, never ours).
            # Parentage is what makes "ours" decidable; a serial match never could.
            # It also retires the substring hazard here for free: a base-serial spawn used to
            # be able to match a ~LANE's claude.exe ("*0.5.0_AE_OpalETL*" matches
            # "0.5.0_AE_OpalETL~A"), but OUR child carries the right serial by construction.
            # Requires $hostPid first -- hence the -and above. No host, no claim: UNKNOWN.
            $cl = @(Get-CimInstance Win32_Process -Filter "Name='claude.exe'" -ErrorAction Stop |
                Where-Object { $_.ProcessId -ne $PID -and $_.ParentProcessId -eq $hostPid })
            if ($cl.Count -ge 1) { $claudePid = ($cl | Sort-Object CreationDate -Descending | Select-Object -First 1).ProcessId }
        }
    } catch {
        # CIM unavailable -- fail-open (same posture as the concurrency cap above).
        # The spawn already happened; we lose the pid, we do NOT lose the agent.
        break
    }
}
$pidField = if ($claudePid) { "pid=$claudePid" } else { "pid=UNKNOWN" }
$hostField = if ($hostPid) { "host_pid=$hostPid" } else { "host_pid=UNKNOWN" }

# Audit -- every successful spawn is recorded.
Add-Content -Path $log -Value "$ts  SPAWN  $Serial  by $by  $pidField  $hostField"

Write-Host "[spawn-agent] launched $Serial in a new window (spawned by $by, headless)" -ForegroundColor Green

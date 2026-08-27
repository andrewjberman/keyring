# spawn-agent.ps1 -- spawn an Opal agent in its own PowerShell window.
#
# Usage:  .tools\spawn-agent.ps1 <Serial> [extra first-message words]
#
# Opens a NEW detached PowerShell window, dot-sources ajb.ps1, and runs
# `ajb -Headless <Serial>` -- fully hands-free (no Y/N startup prompt, so an
# autonomous spawn never stalls with nobody at the keyboard). Every spawn is
# appended to org/mcp/agent-spawn-audit.log.
#
# This is MSTR's agent-provisioning capability. Provisioning ONLY -- task
# orders and direction still flow through Tier 1 (spawn != dispatch).
#
# CAPS (enforced only when invoked FROM an agent, i.e. OPAL_AGENT_SERIAL set;
# manual operator spawns are uncapped):
#   - rate: 3 spawns/spawner and 5 workspace-wide in any trailing 60s window
#   - concurrency: max 20 spawned windows alive at once (ceiling, not a target)
# Audited bypass: $env:FORCE_SPAWN = '<reason>'. Rejects write REJECT lines the
# spawner can read back to detect a runaway loop.
#
# EXAMPLES:
#   .tools\spawn-agent.ps1 0.0.0_AB_MSTR
#   .tools\spawn-agent.ps1 2.0.0_SA_COO "/loop ADVI"

param(
    [Parameter(Mandatory = $true, Position = 0)]
    [string]$Serial,

    # Optional per-session model / reasoning-effort overrides, threaded through
    # to `ajb -Model/-Effort` -> `claude --model/--effort`. Unset = claude default.
    [string]$Model,
    [string]$Effort,

    [Parameter(Position = 1, ValueFromRemainingArguments = $true)]
    [string[]]$Extra
)

# --- Tier-2 model/effort DERIVED DEFAULT (Andrew-direct 2026-08-24) ---------
# VERBATIM: "For future reference, tier2 agents should always be instantiated
# with opus 5 model on extra high effort."
# Tier 2 (Senior) is 0.Y.0 where Y > 0; Tier 3 (Junior) is 0.Y.Z where Y > 0, Z > 0
# (org/ORG_CHART.md:13-14). BOTH are covered as of 2026-08-26.
# EXTENDED TO TIER 3 -- Andrew-direct 2026-08-26 ~15:0xZ, asked and answered explicitly
# after 0.6.2_AE_PartnerETL~A (a Tier-3 serial) spawned WITHOUT the default while its four
# Tier-2 peers got it, and had to be killed and respawned by hand to match. Hand-passing
# the flags per spawn is the stale-hand-copied-list failure the derived form exists to kill.
# A ~lane suffix is an instance marker, not a tier -- 0.4.0_DS_X~G is Tier 2.
#
# DERIVED, NEVER HARDCODED PER CALL. "Always" is a property of the SPAWN PATH,
# not of the operator's memory: six lanes were seated by hand the day he said
# it, and a context-clear or a successor MSTR loses the instruction silently
# while every spawn still looks normal. That is the failure this closes.
#
# An EXPLICIT -Model/-Effort ALWAYS WINS -- this only fills an unset flag, so
# it is a default, not an override, and never a gate on anyone's choice.
$tierDefaulted = @()
if ($Serial -match '^0\.([0-9]+)\.[0-9]+_' -and [int]$Matches[1] -gt 0) {
    if (-not $Model)  { $Model  = 'claude-opus-5'; $tierDefaulted += 'model=claude-opus-5' }
    if (-not $Effort) { $Effort = 'xhigh';         $tierDefaulted += 'effort=xhigh' }
}
# SAY SO WHEN YOU DEFAULT. A silent default and an explicit choice look
# identical in the audit log, so an operator cannot tell whether the tier rule
# fired or someone typed the flags -- and a default nobody can see is one
# nobody can find when it is wrong.
if ($tierDefaulted.Count -gt 0) {
    Write-Host "[spawn-agent] tier-2 default applied for ${Serial}: $($tierDefaulted -join ', ') (Andrew-direct 2026-08-24; pass -Model/-Effort to override)"
}

# Repo root from THIS FILE'S OWN LOCATION (never a user path -- a second device
# clones elsewhere and every spawn/kill/audit path must follow the clone).
# OPAL_WS_ROOT: device-level escape hatch, checked FIRST -- an env var lives
# outside the repo, per machine, so it can never be pushed. Unset is normal.
if ($env:OPAL_WS_ROOT -and (Test-Path -LiteralPath $env:OPAL_WS_ROOT)) {
    $ws = (Resolve-Path -LiteralPath $env:OPAL_WS_ROOT).Path
} else {
    $ws = Split-Path -Parent $PSScriptRoot
}
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

# Rate caps (agent-invoked spawns only; manual operator spawns have
# OPAL_AGENT_SERIAL unset -> uncapped).
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
    # alive at any moment (Andrew-set; a ceiling, never a target -- reallocate
    # before spawning). Distinct from the rate cap: this caps simultaneous
    # instances. Counted via Win32_Process CommandLine match on the marker.
    # Fail-open on CIM failure (loud audit line) so a COM blip doesn't silently
    # block MSTR ops -- the rate cap above remains in force as the second layer.
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

# Audited bypass (reason string logged for forensic review).
if ($env:FORCE_SPAWN) {
    Add-Content -Path $log -Value "$ts  FORCE-SPAWN $Serial  by $by  reason=$($env:FORCE_SPAWN)"
}

# Wrap extras as a single-quoted PowerShell literal so PS metacharacters (';',
# ':', '(', '&', ...) in the extra words are not re-parsed by the spawned
# window's PowerShell as additional statements -- an unquoted ';' kills the
# inner ajb invocation while the window stays alive holding a cap slot.
# Single-quote escape: literal "'" becomes "''".
if ($Extra) {
    $extraJoined = ($Extra -join ' ')
    $extraQuoted = $extraJoined.Replace("'", "''")
    $extraStr = " '$extraQuoted'"
} else {
    $extraStr = ''
}

# Model/effort flags for the inner ajb invocation. Single-quoted for the same
# metacharacter reason; values carry no semicolons (claude-validated vocab),
# so the wt.exe `;`-escape pass below is unaffected.
$moFlags = ''
if ($Model)  { $moFlags += " -Model '$($Model.Replace("'", "''"))'" }
if ($Effort) { $moFlags += " -Effort '$($Effort.Replace("'", "''"))'" }

# Inner script for the new window: -NoProfile (deterministic), -NoExit (window
# persists). Dot-sources ajb.ps1 explicitly so `ajb` exists regardless of
# profile setup; -Headless keeps the spawn fully hands-free. The trailing
# "# OPAL_SPAWN_MARKER_v1: <Serial>" comment is a no-op that stays in the
# process CommandLine, where the concurrency cap and kill-agent.ps1 grep for
# it. Title is set OSC 0 + WindowTitle belt-and-suspenders (ajb.ps1 repeats
# the pair immediately before claude.exe takes the console).
$inner = "[Console]::Write(([char]27).ToString() + ']0;$Serial' + ([char]7).ToString()); `$Host.UI.RawUI.WindowTitle = '$Serial'; . `"$ajb`"; ajb -Headless$moFlags $Serial$extraStr $marker`: $Serial"

# Title path: prefer wt.exe with an explicit --title at tab CREATION (works
# without the suppressApplicationTitle setting); the OSC/WindowTitle pair in
# $inner is the fallback for non-WT hosts (conhost, ssh).
$wt = Get-Command wt.exe -ErrorAction SilentlyContinue
$hostPid = $null
# Resolve the ajb.ps1 path the wt payload will carry BEFORE choosing a branch:
# if it cannot be made space-free, wt is not a usable transport on this box
# (see the space-in-path note below) and Start-Process must be used instead.
$ajbForWt = $null
try { $ajbForWt = (New-Object -ComObject Scripting.FileSystemObject).GetFile($ajb).ShortPath } catch { $ajbForWt = $null }
if (-not $ajbForWt) { $ajbForWt = $ajb }
$usableWt = [bool]$wt -and ($ajbForWt -notmatch ' ')
if (-not $usableWt -and $wt) {
    Write-Host "[spawn-agent] wt.exe present but ajb.ps1 path is not space-free ($ajbForWt) -- routing to Start-Process so the payload survives CommandLineToArgvW."
}
if ($usableWt) {
    # wt parses `;` as its action-separator -> escape every `;` as `\;` so the
    # full statement string reaches powershell.exe.
    #
    # SPACE-IN-PATH: wt hands its trailing commandline to CreateProcess via
    # CommandLineToArgvW, which CONSUMES `"` characters -- a dot-sourced
    # `. "$ajb"` arrives BARE and splits on whitespace, fatal on any clone path
    # containing a space (and silent on one that doesn't). `\"` escaping does
    # NOT survive the two parser layers (measured). Fix: dot-source the 8.3
    # SHORT path, which contains no spaces, so the payload carries no double
    # quotes at all; if 8.3 is disabled on the volume, the $usableWt guard
    # routes to Start-Process, which passes the payload intact as a single
    # -ArgumentList element. Note this script never observes the child's fate
    # -- the sound oracle for a live agent is its own register_agent, not our
    # "launched" print.
    $innerWtPayload = "[Console]::Write(([char]27).ToString() + ']0;$Serial' + ([char]7).ToString()); `$Host.UI.RawUI.WindowTitle = '$Serial'; . $ajbForWt; ajb -Headless$moFlags $Serial$extraStr $marker`: $Serial"
    $innerForWt = $innerWtPayload -replace ';', '\;'
    # `-w new` opens a fresh WT window (one-window-per-agent UX convention).
    & wt.exe -w new new-tab --title $Serial powershell.exe -NoProfile -NoExit -Command $innerForWt
    # Do NOT -PassThru wt.exe: it is a LAUNCHER that hands the tab to the
    # existing Windows Terminal process -- its pid is NOT the agent's shell,
    # and recording it would be a confident wrong pid. The marker-carrying
    # shell is resolved below by the same CIM predicate the cap uses.
} else {
    # Fallback for non-WT environments -- relies on the OSC + WindowTitle in
    # $inner to set the title best-effort.
    $proc = Start-Process powershell -ArgumentList '-NoProfile', '-NoExit', '-Command', $inner -PassThru
    if ($proc) { $hostPid = $proc.Id }   # this IS the marker-carrying shell
}

# ---------------------------------------------------------------------------
# Birth-pid capture (F-008). Two DIFFERENT processes, each named for what it is:
#   pid=      the claude.exe -- the same object kill-agent.ps1 kills; this is
#             what lets a birth be correlated with its death.
#   host_pid= the marker-carrying powershell.exe -- the object the concurrency
#             cap counts.
# claude.exe does not exist at launch (shell -> ajb -> claude), so it is polled
# for. Unresolved -> UNKNOWN, EXPLICITLY -- never omitted (a missing field
# reads as "not applicable") and never guessed (a confident wrong field is
# worse than an absent one).
# ---------------------------------------------------------------------------
$claudePid = $null
$deadline = (Get-Date).AddSeconds(20)
while ((Get-Date) -lt $deadline -and (-not $claudePid -or -not $hostPid)) {
    Start-Sleep -Milliseconds 400
    try {
        if (-not $hostPid) {
            # SELF-EXCLUSION ($_.ProcessId -ne $PID) is load-bearing: this
            # process's OWN CommandLine mentions the marker + serial, so the
            # query would match itself. kill-agent.ps1 carries the same
            # exclusion for the same reason.
            $ps = @(Get-CimInstance Win32_Process -Filter "Name='powershell.exe'" -ErrorAction Stop |
                Where-Object { $_.ProcessId -ne $PID -and $_.CommandLine -and
                               $_.CommandLine -like "*$marker*" -and $_.CommandLine -like "*$Serial*" })
            if ($ps.Count -ge 1) { $hostPid = ($ps | Sort-Object CreationDate -Descending | Select-Object -First 1).ProcessId }
        }
        if (-not $claudePid -and $hostPid) {
            # PARENTAGE-BOUND: our claude.exe is a CHILD of the marker window we
            # launched ($hostPid). A newest-match-by-serial resolver can stamp
            # SOMEBODY ELSE'S session into the audit whenever our spawn produced
            # no claude.exe (window died / serial already live), and a base-serial
            # substring can match a ~lane's session. Parentage makes "ours"
            # decidable; a serial match never can. No host, no claim: UNKNOWN.
            $cl = @(Get-CimInstance Win32_Process -Filter "Name='claude.exe'" -ErrorAction Stop |
                Where-Object { $_.ProcessId -ne $PID -and $_.ParentProcessId -eq $hostPid })
            if ($cl.Count -ge 1) { $claudePid = ($cl | Sort-Object CreationDate -Descending | Select-Object -First 1).ProcessId }
        }
    } catch {
        # CIM unavailable -- fail-open (same posture as the concurrency cap).
        # The spawn already happened; we lose the pid, we do NOT lose the agent.
        break
    }
}
$pidField = if ($claudePid) { "pid=$claudePid" } else { "pid=UNKNOWN" }
$hostField = if ($hostPid) { "host_pid=$hostPid" } else { "host_pid=UNKNOWN" }

# Audit -- every successful spawn is recorded.
Add-Content -Path $log -Value "$ts  SPAWN  $Serial  by $by  $pidField  $hostField"

Write-Host "[spawn-agent] launched $Serial in a new window (spawned by $by, headless)" -ForegroundColor Green

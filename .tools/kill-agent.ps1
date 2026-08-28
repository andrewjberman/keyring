# kill-agent.ps1 -- terminate one or more spawned-agent PowerShell windows.
#
# Usage:  .tools\kill-agent.ps1 <Serial> [-Reason "<text>"]
#         .tools\kill-agent.ps1 -All -Reason "fabric-wide reset"
#
# Finds every live agent by its claude.exe process (the serial is in the
# claude.exe CommandLine for BOTH manual `clb`/`ajb` launches AND headless
# spawn-agent windows -- the universal match) and Stop-Process -Force the claude
# tree. The spawn-agent host window is killed too IF it carries the
# # OPAL_SPAWN_MARKER_v1 tag (releases the concurrency-cap slot); a manual
# interactive shell is left alone. Orphan inbox-watch.sh watchers for the killed
# serial are swept. Modes: `<serial>` (one lane, tilde-precise) | `<serial> -All`
# (that serial's family: base + ~lanes) | `-All` (entire fabric, minus self).
#
# This is the fabric's reallocation capability, invoked via /mstr-kill by
# 0.0.0_AB_MSTR (device/fabric infra) or 2.0.0_SA_COO (work population) -- a COO
# function in addition to MSTR since Andrew-direct 2026-08-28: when an agent's
# chartered work is done, the caller runs `kill-agent <serial>` to release the host
# slot for the next agent it wants to spawn. Each kill writes a KILL line to
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

# Resolve the workspace from this script's own location -- a hardcoded user
# path silently drops every KILL audit line on any other device's clone.
$ws     = Split-Path -Parent $PSScriptRoot
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

# Locate every live agent via its claude.exe process. The agent serial is always
# in the claude.exe CommandLine (the first-message arg) for BOTH manual `clb`/`ajb`
# launches AND headless spawn-agent windows -- so claude.exe is the UNIVERSAL match.
# (The old approach matched the OPAL_SPAWN_MARKER on spawn-agent's powershell window,
# which does NOT exist on hand-launched agents -- so manual `clb <serial>` agents
# were invisible to kill-agent. Matching claude.exe fixes that.)
try {
    $allClaude = @(Get-CimInstance Win32_Process -Filter "Name='claude.exe'" -ErrorAction Stop |
        Where-Object { $_.CommandLine })
} catch {
    Write-Error "kill-agent: Win32_Process query failed -- $($_.Exception.Message)"
    exit 1
}

# First serial-shaped token in a commandline (for audit labels).
$serialPat = '[0-9]+\.[0-9]+\.[0-9]+_[A-Za-z]+_[A-Za-z0-9]+(?:~[A-Za-z0-9]+)?'

# Filter to the requested target(s). Boundaries: leading (?<![\w~]) + trailing
# (?![~\w]) make a BASE serial precise (won't catch its own ~lanes) and block
# mid-token bleed (e.g. 3.1.0_SA_CVO won't match 3.1.0_SA_CVOX or ...~B).
if ($All -and $Serial) {
    # FAMILY mode (serial + -All): base serial + ALL its ~lanes (e.g.
    # 3.1.0_SA_CVO + ~A/~B/~C). Optional ~lane suffix then a boundary -- catches the
    # whole family, does NOT bleed into a different serial. EXPLICIT opt-in
    # family-kill (the old accidental base-substring-sweep, now deliberate).
    $needleRe = '(?<![\w~])' + [regex]::Escape($Serial) + '(~[A-Za-z0-9]+)?(?![~\w])'
    $targets = @($allClaude | Where-Object { $_.CommandLine -match $needleRe })
} elseif ($All) {
    # FABRIC-WIDE (-All alone): every live agent -- EXCEPT (a) the requester's own
    # session (no suicide mid-command) and (b) the MSTR conductor (kill MSTR only
    # by explicit serial `kill 0.0.0_AB_MSTR`, never via a blanket sweep). So
    # `kill -All` = "all workers + Tier-1, keep the conductor."
    $selfRe = if ($by -and $by -ne 'unknown') { '(?<![\w~])' + [regex]::Escape($by) + '(?![~\w])' } else { $null }
    $targets = @($allClaude | Where-Object {
        (-not ($selfRe -and $_.CommandLine -match $selfRe)) -and
        ($_.CommandLine -notmatch '(?<![\w~])[0-9]+\.[0-9]+\.[0-9]+_AB_MSTR(~[A-Za-z0-9]+)?(?![~\w])')
    })
} else {
    # SINGLE TILDE-PRECISE match: serial must NOT be continued by a ~lane suffix or
    # word char. A suffixed serial (~B) was already precise; this makes bare-base
    # precise too. To kill base + all tildes, use `<serial> -All`.
    #
    # SELF-EXCLUSION (D0_TIGHTENING.TO-4): a seat must never kill ITSELF on a
    # single-serial match -- a self-inflicted outage, and the expensive shape is
    # mid-reap (the seat dies holding the work it was reaping for). `-All` alone
    # has excluded self since it was written (see $selfRe above); the single-serial
    # path did not, so the one form an agent actually types at itself was the one
    # form unguarded.
    #
    # The comparison IS the whole check, and that is a property of tilde-precision
    # rather than an assumption: the needle regex below is bounded (?<![\w~]) /
    # (?![~\w]), so a bare base needle cannot match its own ~lane and a ~lane
    # needle cannot match its base. Therefore in THIS branch the only commandline
    # that can be the caller's own is one whose serial equals the needle exactly.
    #
    # BOTH LIMBS ARE LOAD-BEARING (K-1): suppress the kill AND print the exclusion.
    # A silent no-kill is indistinguishable from a broken matcher -- the caller
    # would read "nothing happened" identically in both worlds.
    #
    # Returns early rather than emptying $targets: falling through to the
    # zero-targets branch would run the orphan-watcher reaper against $Serial and
    # sweep the CALLER'S OWN live inbox watcher -- deafening the seat this guard
    # exists to protect, while printing "nothing to kill".
    if ($by -ne 'unknown' -and $Serial -eq $by) {
        Write-Host "[kill-agent] SELF-EXCLUDED: '$Serial' is the caller's own serial (OPAL_AGENT_SERIAL) -- refusing to kill self. Nothing killed, no watcher reaped." -ForegroundColor Yellow
        Add-Content -Path $log -Value "$ts  KILL-SELF-EXCLUDED  $Serial  by $by  reason=$Reason  found=0  watchers_reaped=0"
        exit 0
    }
    if ($by -eq 'unknown') {
        # Not evaluable is NOT the same as not-self. Say so out loud rather than
        # proceeding under a silent assumption the guard held.
        Write-Host "[kill-agent] WARN: OPAL_AGENT_SERIAL is unset -- self-exclusion could NOT be evaluated for '$Serial'. Proceeding; verify you are not killing yourself." -ForegroundColor Yellow
    }
    $needleRe = '(?<![\w~])' + [regex]::Escape($Serial) + '(?![~\w])'
    $targets = @($allClaude | Where-Object { $_.CommandLine -match $needleRe })
}

if ($targets.Count -eq 0) {
    $what = if ($All -and $Serial) { "live agent for serial-family '$Serial' (base + ~lanes)" } elseif ($All) { 'any live agents' } else { "live agent for serial '$Serial'" }
    $auditTgt = if ($All -and $Serial) { "$Serial+lanes" } elseif ($All) { 'ALL' } else { $Serial }
    # Agent's claude is already gone -- but reap any orphan inbox-watch.sh <serial>
    # watcher left behind (deaf poller), so `kill <serial>` is clean either way.
    $reaped = 0
    if ($Serial) {
        try {
            $watcherRe = "inbox-watch\.sh\s+'?" + [regex]::Escape($Serial) + $(if ($All) { '(~[A-Za-z0-9]+)?' }) + '(?![~\w])'
            @(Get-CimInstance Win32_Process -ErrorAction SilentlyContinue |
                Where-Object { $_.CommandLine -and $_.CommandLine -match 'inbox-watch\.sh' -and $_.CommandLine -match $watcherRe }) |
                ForEach-Object { Stop-Process -Id $_.ProcessId -Force -ErrorAction SilentlyContinue; $reaped++ }
        } catch { }
    }
    $tail = if ($reaped -gt 0) { " (reaped $reaped orphan watcher(s))" } else { '' }
    Write-Host "[kill-agent] No $what found -- nothing to kill.$tail" -ForegroundColor Yellow
    Add-Content -Path $log -Value "$ts  KILL-NOOP  $auditTgt  by $by  reason=$Reason  found=0  watchers_reaped=$reaped"
    exit 0
}

# Recursive process-tree kill -- children first, then the node.
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

$killedPids     = @()
$killedSerials  = @()
foreach ($t in $targets) {
    $claudePid    = $t.ProcessId
    $targetSerial = if ($t.CommandLine -match $serialPat) { $matches[0] } else { 'unknown' }
    $killedSerials += $targetSerial

    # 1. Kill claude.exe + its descendants (bash, python, watcher children).
    Stop-ProcessTree -RootPid $claudePid

    # 2. Kill the HOST window ONLY if it's a spawn-agent window (carries the
    #    marker) -- releases the concurrency-cap slot + closes the window. If the
    #    parent is a manual interactive shell (no marker), LEAVE it so we don't
    #    nuke the operator's terminal; it just returns to a prompt.
    try {
        $parent = Get-CimInstance Win32_Process -Filter "ProcessId=$($t.ParentProcessId)" -ErrorAction SilentlyContinue
        if ($parent -and $parent.Name -eq 'powershell.exe' -and $parent.CommandLine -and ($parent.CommandLine -like "*$marker*")) {
            Stop-ProcessTree -RootPid $parent.ProcessId
        }
    } catch { }

    Add-Content -Path $log -Value "$ts  KILL  $targetSerial  by $by  pid=$claudePid  reason=$Reason"
    $killedPids += $claudePid
    Write-Host "[kill-agent] terminated $targetSerial (claude pid $claudePid)" -ForegroundColor Green
}

# 3. Cleanup: kill orphaned inbox-watch.sh <serial> bash watchers for the killed
#    serials (they reparent to PID 1, so they're outside claude's tree). Leaves
#    no deaf-orphan watcher behind.
try {
    $bashProcs = @(Get-CimInstance Win32_Process -ErrorAction SilentlyContinue |
        Where-Object { $_.CommandLine -and $_.CommandLine -match 'inbox-watch\.sh' })
    foreach ($b in $bashProcs) {
        foreach ($ks in ($killedSerials | Sort-Object -Unique)) {
            if ($ks -ne 'unknown' -and $b.CommandLine -match ("inbox-watch\.sh\s+'?" + [regex]::Escape($ks) + '(?![~\w])')) {
                Stop-Process -Id $b.ProcessId -Force -ErrorAction SilentlyContinue
                break
            }
        }
    }
} catch { }

Write-Host "[kill-agent] killed $($killedPids.Count) agent(s): $($killedPids -join ', ')" -ForegroundColor Cyan

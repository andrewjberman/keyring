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

# SEAT BOUNDARY (CT-ab-4): a target is matched by its LAUNCH serial, and a tree holding a foreign seat is never stopped.
. (Join-Path $PSScriptRoot 'seat-boundary.ps1')

if (-not $All -and -not $Serial) {
    Write-Error "kill-agent: must pass either a Serial or -All"
    exit 1
}
if ($Serial -and ($Serial -notmatch '^[0-9]+\.[0-9]+\.[0-9]+_[A-Za-z]+_[A-Za-z0-9_]+(~[A-Za-z0-9]+)?$')) {
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
$serialPat = '[0-9]+\.[0-9]+\.[0-9]+_[A-Za-z]+_[A-Za-z0-9_]+(?:~[A-Za-z0-9]+)?'

# Filter to the requested target(s). Boundaries: leading (?<![\w~]) + trailing
# (?![~\w]) make a BASE serial precise (won't catch its own ~lanes) and block
# mid-token bleed (e.g. 3.1.0_SA_CVO won't match 3.1.0_SA_CVOX or ...~B).
if ($All -and $Serial) {
    # FAMILY mode (serial + -All): base serial + ALL its ~lanes (e.g.
    # 3.1.0_SA_CVO + ~A/~B/~C). Optional ~lane suffix then a boundary -- catches the
    # whole family, does NOT bleed into a different serial. EXPLICIT opt-in
    # family-kill (the old accidental base-substring-sweep, now deliberate).
    $needleRe = '(?<![\w~])' + [regex]::Escape($Serial) + '(~[A-Za-z0-9]+)?(?![~\w])'
    # CT-ab-4: the needle alone matched a serial NAMED in another seat's hint; keep only the launch serial (or its ~lanes).
    $targets = @($allClaude | Where-Object { $_.CommandLine -match $needleRe -and (Test-LaunchSerialMatch -CommandLine $_.CommandLine -Serial $Serial -Family) })
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
    # CT-ab-4: the needle alone matched a serial NAMED in another seat's hint; keep only the launch serial.
    $targets = @($allClaude | Where-Object { $_.CommandLine -match $needleRe -and (Test-LaunchSerialMatch -CommandLine $_.CommandLine -Serial $Serial) })
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

# SEAT BOUNDARY (CT-ab-4, CT-ac-2). Every target's tree is planned before anything is stopped.
# The judged serial is the NAMED serial (single or family), else the target's own launch serial.
# Selected = every pid this run targets, so a fabric-wide sweep does not refuse its own seats.
# CT-ac-2: a foreign seat ENDS THE WALK at that seat -- the seat and its subtree are left running and each is
# named (SKIPPED line and KILL log). Everything else under the tree is stopped. A seat that cannot be judged
# (unreadable command line) is the floor: that whole tree is refused, as the whole-tree refusal was.
$selectedPids   = @($targets | ForEach-Object { [int]$_.ProcessId })
$boundaryFamily = [bool]($All -and $Serial)
$boundarySerial = $null
function Get-TreePlan {
    param([int]$RootPid)
    try {
        $procs = @(Get-CimInstance Win32_Process -ErrorAction Stop |
            Select-Object ProcessId, ParentProcessId, Name, CommandLine)
        # Two judges read one process list: the boundary judge (Test-SeatBoundary) must report every seat root
        # the plan skips, or the tree is refused as unevaluated.
        $judged = @(Test-SeatBoundary -RootPid $RootPid -TargetSerial $boundarySerial -Family:$boundaryFamily -Selected $selectedPids -Processes $procs)
        $plan = Get-SeatSubtreePids -RootPid $RootPid -TargetSerial $boundarySerial -Family:$boundaryFamily -Selected $selectedPids -Processes $procs
        $judgedPids = @($judged | ForEach-Object { [int]$_.ProcessId })
        $unjudged = @($plan.Skip | Where-Object { $_.IsSeat -and ($judgedPids -notcontains [int]$_.ProcessId) })
        if ($unjudged.Count -gt 0) {
            $names = ($unjudged | ForEach-Object { "$($_.Serial)@$($_.ProcessId)" }) -join ', '
            return [PSCustomObject]@{ Ok = $false; Plan = $null; Err = "skipped seat(s) not in the boundary judgement: $names" }
        }
        return [PSCustomObject]@{ Ok = $true; Plan = $plan; Err = '' }
    } catch {
        return [PSCustomObject]@{ Ok = $false; Plan = $null; Err = $_.Exception.Message }
    }
}
function Invoke-TreeStop {
    # Stops the planned Kill pids of one tree. Returns Stopped=$false (nothing stopped) on the floor or an
    # unevaluable tree; otherwise Stopped=$true with the Skip list of seats left running.
    param([int]$RootPid, [string]$Tree, [string]$Target)
    $tp = Get-TreePlan -RootPid $RootPid
    if (-not $tp.Ok) {
        Write-SeatRefusal -Tree $Tree -RootPid $RootPid -Target $Target -Verdict ([PSCustomObject]@{ Ok = $false; Foreign = @(); Err = $tp.Err })
        return [PSCustomObject]@{ Stopped = $false; Skip = @() }
    }
    if (@($tp.Plan.Unclassified).Count -gt 0) {
        $why = (@($tp.Plan.Unclassified) | ForEach-Object { "$($_.Name) pid $($_.ProcessId) ($($_.Reason))" }) -join '; '
        Write-SeatRefusal -Tree $Tree -RootPid $RootPid -Target $Target -Verdict ([PSCustomObject]@{ Ok = $false; Foreign = @(); Err = "unclassified seat: $why" })
        return [PSCustomObject]@{ Stopped = $false; Skip = @() }
    }
    foreach ($line in @(Format-SkipLines -Skip $tp.Plan.Skip)) {
        Write-Host "[kill-agent] $line" -ForegroundColor Yellow
    }
    foreach ($kpid in @($tp.Plan.Kill)) {
        Stop-Process -Id $kpid -Force -ErrorAction SilentlyContinue
    }
    return [PSCustomObject]@{ Stopped = $true; Skip = @($tp.Plan.Skip) }
}
function Write-SeatRefusal {
    param([string]$Tree, [int]$RootPid, [string]$Target, $Verdict)
    if (-not $Verdict.Ok) {
        Write-Host "[kill-agent] REFUSED: seat boundary -- $Tree of pid $RootPid (target $Target) could not be evaluated, so not stopped: $($Verdict.Err)" -ForegroundColor Red
        Add-Content -Path $log -Value "$ts  KILL-REFUSED  $Target  by $by  pid=$RootPid  tree=$Tree  foreign=UNEVALUATED  reason=$Reason"
        return
    }
    foreach ($f in $Verdict.Foreign) {
        Write-Host "[kill-agent] REFUSED: seat boundary -- $Tree of pid $RootPid (target $Target) holds foreign seat $($f.Serial) at pid $($f.ProcessId); tree not stopped." -ForegroundColor Red
    }
    $list = (@($Verdict.Foreign) | ForEach-Object { "$($_.Serial)@$($_.ProcessId)" }) -join ','
    Add-Content -Path $log -Value "$ts  KILL-REFUSED  $Target  by $by  pid=$RootPid  tree=$Tree  foreign=$list  reason=$Reason"
}

$killedPids     = @()
$killedSerials  = @()
$refused        = @()
foreach ($t in $targets) {
    $claudePid    = $t.ProcessId
    $ownSerial    = Get-LaunchSerial -CommandLine $t.CommandLine
    $targetSerial = if ($ownSerial) { $ownSerial } else { 'unknown' }
    $boundarySerial = if ($Serial) { $Serial } else { $ownSerial }
    $skipped = @()

    # 1. Stop claude.exe + its non-seat descendants (bash, python, watcher children). A foreign seat under it is
    #    skipped with its subtree (CT-ac-2); an unclassified seat refuses the tree.
    $claudeTree = Invoke-TreeStop -RootPid $claudePid -Tree 'claude tree' -Target $targetSerial
    if (-not $claudeTree.Stopped) {
        $refused += $claudePid
        continue
    }
    $skipped += @($claudeTree.Skip)
    $killedSerials += $targetSerial

    # 2. Kill the HOST window ONLY if it's a spawn-agent window (carries the
    #    marker) -- releases the concurrency-cap slot + closes the window. If the
    #    parent is a manual interactive shell (no marker), LEAVE it so we don't
    #    nuke the operator's terminal; it just returns to a prompt.
    try {
        $parent = Get-CimInstance Win32_Process -Filter "ProcessId=$($t.ParentProcessId)" -ErrorAction SilentlyContinue
        if ($parent -and $parent.Name -eq 'powershell.exe' -and $parent.CommandLine -and ($parent.CommandLine -like "*$marker*")) {
            $hostTree = Invoke-TreeStop -RootPid $parent.ProcessId -Tree 'host shell' -Target $targetSerial
            if (-not $hostTree.Stopped) {
                $refused += $parent.ProcessId
            } else {
                $skipped += @($hostTree.Skip)
            }
        }
    } catch { }

    Add-Content -Path $log -Value "$ts  KILL  $targetSerial  by $by  pid=$claudePid  reason=$Reason$(Format-SkipLogSuffix -Skip $skipped)"
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
if (@($refused).Count -gt 0) {
    Write-Host "[kill-agent] REFUSED $(@($refused).Count) tree(s) on the seat boundary -- each named above; nothing under a foreign seat was stopped." -ForegroundColor Red
    exit 2
}

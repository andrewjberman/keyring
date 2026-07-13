<#
.SYNOPSIS
  mem-sentinel -- NAME THE RUNAWAY BEFORE IT TAKES THE HOST DOWN.

.WHY THIS EXISTS (2026-07-13, the WindowsTerminal outage)
  A python.exe (PID 19224) grew to 39.9GB -> 43.2GB of COMMIT. Windows diagnosed low-virtual-memory
  twice (08:16:17Z, 08:17:56Z), dwm.exe crashed, and at 08:19:20Z WindowsTerminal.exe -- which was
  HOSTING EVERY AGENT TAB -- faulted and took the whole fabric with it. Eight agents died at once.

  *** AND WE COULD NOT SAY WHAT THE PROCESS WAS. *** By the time anyone looked it was gone. There is
  no process-creation audit on this box; no agent transcript showed a heavy python job; PID adjacency
  to the claude.exe in the same event was suggestive and NOT sufficient. The mechanism was INFERRED
  and therefore NON-ACTIONABLE (CLAUDE.md Rule 22) -- so the ONE thing that can recur is the one thing
  we cannot name. This sentinel exists to make the next one NAME ITSELF, while it is still alive.

  THE MEASURED HEADROOM, and it is why this is not paranoia:
      system Commit Limit  = 46.2 GB
      the leaker           = 43.2 GB
  A SINGLE PROCESS CONSUMED ESSENTIALLY THE ENTIRE MACHINE'S COMMIT BUDGET. There is no margin here.

.WHAT IT DOES / DOES NOT DO
  DOES:     poll cheaply, and the moment any process crosses a private-bytes threshold (or the system
            commit ratio crosses its own), RECORD IT WITH ITS COMMAND LINE and emit one stdout line.
  DOES NOT: kill anything. Ever. Killing is an operator action (CLAUDE.md Agent Autonomy: human
            confirmation for anything unrecoverable). A sentinel that reaps is a sentinel nobody
            trusts to run. This one only ever tells you what it saw.

  >> A WARN IN A LOG IS NOT A GATE (CLAUDE.md Rule 22a) -- and this is NOT claiming to be one. It is an
     INSTRUMENT, not a control. It cannot prevent the next outage. It can only ensure that when the
     next one happens we know WHAT DID IT instead of inferring from an event-log tombstone. <<

.METRIC
  PrivateMemorySize64 (private bytes / commit charge) -- NOT WorkingSet (physical RAM, misses a
  process that is committing without touching) and NOT VirtualMemorySize64 (reserved address space:
  bash.exe reads 2052 GB on this box and means nothing by it). The Resource-Exhaustion-Detector
  reports COMMIT, so commit is what we watch. Read via Get-Process -- no WMI on the hot path.

.SELF-TEST
  -SelfTest allocates a real ~1.5GB python process and asserts the sentinel NAMES it.
  *** A CONTROL THAT CANNOT FAIL IS NOT A CONTROL (CLAUDE.md Rule 22a). *** A sentinel that has never
  been observed to fire has not been shown that it can. Run the self-test before trusting a quiet log.

.EXAMPLES
  powershell -File .tools/mem-sentinel.ps1 -Once              # one pass, print current state
  powershell -File .tools/mem-sentinel.ps1 -SelfTest          # PROVE it fires (positive control)
  powershell -File .tools/mem-sentinel.ps1                    # stream (arm under the Monitor tool)
#>
[CmdletBinding()]
param(
    [double] $ThresholdGB    = 4.0,     # per-process private bytes -> WARN  (normal python here: <0.1GB)
    [double] $AlarmGB        = 8.0,     # per-process private bytes -> ALARM
    [double] $CommitWarnPct  = 85.0,    # system committed/limit    -> ALARM (the machine, not a process)
    [int]    $IntervalSec    = 20,
    [double] $RegrowthGB     = 1.0,     # re-emit for a known PID only after it grows this much more
    [string] $LogPath        = "$PSScriptRoot\..\org\mcp\mem-sentinel-events.jsonl",
    [switch] $Once,
    [switch] $SelfTest
)

$ErrorActionPreference = 'Continue'

function Get-CommitState {
    # Perf counters, not WMI: WMI went unresponsive during the very incident this watches for, and an
    # instrument that dies with its subject is not an instrument.
    try {
        $c = (Get-Counter '\Memory\Committed Bytes','\Memory\Commit Limit' -ErrorAction Stop).CounterSamples
        return @{ CommittedGB = $c[0].CookedValue/1GB; LimitGB = $c[1].CookedValue/1GB }
    } catch {
        return @{ CommittedGB = -1; LimitGB = -1 }   # UNKNOWN. Never silently 0 -- absence != zero.
    }
}

function Get-CmdLine([int] $ProcId) {
    # Only ever called for a process that ALREADY tripped a threshold -- so one WMI call, not N.
    # If WMI is hung (it was, during the incident) we say so rather than emit a blank and let a
    # reader mistake "could not read" for "no command line".
    try {
        $p = Get-CimInstance Win32_Process -Filter "ProcessId=$ProcId" -OperationTimeoutSec 5 -ErrorAction Stop
        if ($p -and $p.CommandLine) { return $p.CommandLine }
        return '<no CommandLine exposed>'
    } catch { return '<UNREADABLE: WMI/CIM did not answer>' }
}

$script:Seen = @{}    # pid -> the private-GB at which we last emitted (de-dupe / regrowth gate)

function Invoke-Pass {
    $now    = (Get-Date).ToUniversalTime().ToString('yyyy-MM-ddTHH:mm:ssZ')
    $commit = Get-CommitState
    $events = @()

    foreach ($p in (Get-Process -ErrorAction SilentlyContinue)) {
        $privGB = $p.PrivateMemorySize64 / 1GB
        if ($privGB -lt $ThresholdGB) { continue }

        $prior = $script:Seen[$p.Id]
        if ($null -ne $prior -and ($privGB - $prior) -lt $RegrowthGB) { continue }   # already reported, not materially bigger
        $script:Seen[$p.Id] = $privGB

        $level = if ($privGB -ge $AlarmGB) { 'ALARM' } else { 'WARN' }
        $start = try { $p.StartTime.ToUniversalTime().ToString('yyyy-MM-ddTHH:mm:ssZ') } catch { 'unknown' }

        $events += [pscustomobject]@{
            ts           = $now
            level        = $level
            pid          = $p.Id
            name         = $p.ProcessName
            private_gb   = [math]::Round($privGB, 2)
            workingset_gb= [math]::Round($p.WorkingSet64/1GB, 2)
            started_utc  = $start
            committed_gb = [math]::Round($commit.CommittedGB, 1)
            commit_limit_gb = [math]::Round($commit.LimitGB, 1)
            command_line = (Get-CmdLine $p.Id)
        }
    }

    # The MACHINE-level arm. A swarm of mid-size processes can exhaust commit with no single one
    # crossing the per-process threshold -- the per-process arm is structurally blind to that.
    if ($commit.LimitGB -gt 0) {
        $pct = 100.0 * $commit.CommittedGB / $commit.LimitGB
        if ($pct -ge $CommitWarnPct -and -not $script:CommitFired) {
            $script:CommitFired = $true
            $events += [pscustomobject]@{
                ts = $now; level = 'ALARM'; pid = 0; name = '<SYSTEM COMMIT>'
                private_gb = [math]::Round($commit.CommittedGB,1); workingset_gb = 0
                started_utc = 'n/a'
                committed_gb = [math]::Round($commit.CommittedGB,1)
                commit_limit_gb = [math]::Round($commit.LimitGB,1)
                command_line = "system commit at $([math]::Round($pct,1))% of limit -- the host is close to the 2026-07-13 failure mode"
            }
        } elseif ($pct -lt ($CommitWarnPct - 5)) { $script:CommitFired = $false }
    }

    foreach ($e in $events) {
        # stdout: ONE line per event -- this is the Monitor tool's event stream.
        "MEM-SENTINEL {0} pid={1} {2} private={3}GB ws={4}GB started={5} commit={6}/{7}GB cmd={8}" -f `
            $e.level, $e.pid, $e.name, $e.private_gb, $e.workingset_gb, $e.started_utc,
            $e.committed_gb, $e.commit_limit_gb, $e.command_line
        try {
            $dir = Split-Path -Parent $LogPath
            if (-not (Test-Path $dir)) { New-Item -ItemType Directory -Force $dir | Out-Null }
            ($e | ConvertTo-Json -Compress) | Out-File -FilePath $LogPath -Append -Encoding utf8
        } catch { }   # never let a log failure kill the sentinel
    }
    return $events.Count
}

if ($SelfTest) {
    # *** POSITIVE CONTROL. Could this sentinel have fired? Prove it, do not assert it. ***
    "mem-sentinel SELF-TEST -- allocating a real ~1.5GB python and asserting the sentinel NAMES it."
    ""
    $py = (Get-Command python -ErrorAction SilentlyContinue).Source
    if (-not $py) { "FAIL: no python on PATH -- SELF-TEST NOT RUN (that is not a pass)."; exit 1 }

    $ThresholdGB = 1.0; $AlarmGB = 99; $script:Seen = @{}
    $tmpLog = [IO.Path]::GetTempFileName(); $LogPath = $tmpLog

    # NEGATIVE CONTROL FIRST: with the hog not yet grown, does it stay quiet? (An instrument that
    # fires on everything is as useless as one that fires on nothing.)
    $quiet = Invoke-Pass
    "  negative control (no hog yet): emitted $quiet event(s) at >=1GB"

    # Run the hog from a FILE, not `-c`. Start-Process -ArgumentList does NOT quote an element
    # containing spaces on PS 5.1, so `-c 'import time; x = ...'` reached python as `-c import` and
    # the hog DIED INSTANTLY (exit 1) -- and the first version of this self-test then printed
    # "the hog ran and the sentinel did NOT name it" and FAILED THE SENTINEL.
    # *** THAT IS A NULL THAT MEANS TWO THINGS (CLAUDE.md Rule 22a, F4): it collapsed COULD-NOT-OBSERVE
    #     into OBSERVED-NOTHING and condemned a working instrument for a defect in its own harness. ***
    # So now the harness must PROVE THE HOG IS REAL before it is allowed to judge the sentinel.
    $hogPy = Join-Path ([IO.Path]::GetTempPath()) "mem_sentinel_hog_$PID.py"
    "import time`nx = bytearray(1600*1024*1024)`ntime.sleep(25)`n" | Out-File -FilePath $hogPy -Encoding ascii
    $proc = Start-Process -FilePath $py -PassThru -WindowStyle Hidden -ArgumentList @($hogPy)
    "  spawned hog pid=$($proc.Id); waiting for it to commit..."
    Start-Sleep -Seconds 6

    # ---- PRECONDITION: is the hog ALIVE and ACTUALLY BIG? If not, the sentinel is not on trial. ----
    $hog = Get-Process -Id $proc.Id -ErrorAction SilentlyContinue
    if (-not $hog) {
        try { $ec = $proc.ExitCode } catch { $ec = '?' }
        "  HOG DIED (exit=$ec) -- it never allocated anything."
        ""
        "SELF-TEST INCONCLUSIVE -- INSTRUMENT BREAK IN THE HARNESS, NOT A VERDICT ON THE SENTINEL."
        "  The sentinel was never given anything to see. 'Could not observe' is NOT 'observed nothing'."
        Remove-Item $hogPy,$tmpLog -ErrorAction SilentlyContinue
        exit 2
    }
    $hogGB = [math]::Round($hog.PrivateMemorySize64/1GB, 2)
    "  hog is ALIVE at ${hogGB}GB private (threshold ${ThresholdGB}GB)"
    if ($hogGB -lt $ThresholdGB) {
        ""
        "SELF-TEST INCONCLUSIVE -- the hog never grew past the threshold. Nothing to detect."
        try { Stop-Process -Id $proc.Id -Force -ErrorAction SilentlyContinue } catch { }
        Remove-Item $hogPy,$tmpLog -ErrorAction SilentlyContinue
        exit 2
    }

    # ---- NOW the sentinel is on trial, against a hog we have INDEPENDENTLY confirmed is real. ----
    $script:Seen = @{}
    [void](Invoke-Pass)
    $hit = $false; $named = $null
    if (Test-Path $tmpLog) {
        foreach ($line in (Get-Content $tmpLog)) {
            $o = $line | ConvertFrom-Json
            if ($o.pid -eq $proc.Id) { $hit = $true; $named = $o }
        }
    }
    try { Stop-Process -Id $proc.Id -Force -ErrorAction SilentlyContinue } catch { }
    Remove-Item $hogPy,$tmpLog -ErrorAction SilentlyContinue

    ""
    if ($hit) {
        "SELF-TEST PASS -- the sentinel SAW a hog it had no prior knowledge of, and NAMED it:"
        "    pid          = $($named.pid)"
        "    private_gb   = $($named.private_gb)"
        "    command_line = $($named.command_line)"
        ""
        "  The negative control above (0 events before the hog existed) proves it is not merely"
        "  firing on everything. It has now been OBSERVED TO FIRE, and OBSERVED TO STAY QUIET."
        "  A quiet log from here is EVIDENCE. Before this run it was only silence."
        exit 0
    }
    "SELF-TEST FAIL -- a CONFIRMED ${hogGB}GB process was live and the sentinel did NOT name it."
    "  This is a real verdict (the hog was verified alive and over threshold). DO NOT TRUST THE SENTINEL."
    exit 1
}

if ($Once) {
    $n = Invoke-Pass
    if ($n -eq 0) {
        $c = Get-CommitState
        "MEM-SENTINEL OK -- no process at or above ${ThresholdGB}GB private. commit=$([math]::Round($c.CommittedGB,1))/$([math]::Round($c.LimitGB,1))GB"
    }
    exit 0
}

# stream mode -- arm under the Monitor tool; emits only on threshold crossings, so a quiet stream is quiet.
while ($true) {
    [void](Invoke-Pass)
    Start-Sleep -Seconds $IntervalSec
}

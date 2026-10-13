<#
  kill-maint.ps1 -- engine for the /kill maintenance skill.

  Two modes clear recurring cruft WITHOUT ever touching a live Claude agent
  session or the fabric comms infra:

    scripts : four classes (2026-10-08, GC FAST FIX FF1+FF2):
              ORPHAN   bash/py outside every live claude tree past the Monitor
                       cap (a dead session's Bash-tool shells included);
              NATIVE   typeperf/awk/gawk/tail/timeout outside every live claude
                       tree past the Monitor cap (the dell1 typeperf leak);
              REPLACED an older inbox-watch / agent-poller for one serial, or an
                       older agentbus watch; the newest copy is kept;
              ORPHANED an inbox-watch / agent-poller whose serial has no live MCP
                       server in org/mcp/liveness.json.
              A DECLARED detached job (.tools/detached-job.sh marker, within
              its max runtime) and anything running in a WORKER worktree
              (linked worktree, leaf or branch wk-*) are never ORPHAN/NATIVE.
              broker.py / server.py / agentbus-consumer.py, an in-flight
              safe-commit/merge/deploy/apply, commit-worker, commit-gate or
              terraform, and anything in a drain-* worktree are never targets. Execute stops each target's
              WHOLE TREE (taskkill /T), never one PID.

    apps    : bloat GUI apps (Edge, Chrome, Teams, Tailscale, Copilot, ...).
              NEVER a Claude-driven / Playwright-automation browser, never a
              session host (powershell/WindowsTerminal/conhost), never a
              hard-denied system or security(EDR) process.

  DRY-RUN by default. Nothing dies unless -Execute is passed. ASCII-only output
  (CLAUDE.md: no non-ASCII in anything that runs/logs on this estate).

  PS 5.1 compatible (no ternary / ?? / ?.).
#>
param(
  [ValidateSet('scripts','apps','all')] [string]$Mode = 'all',
  [switch]$Execute,          # absent = DRY-RUN (default). Present = stop each target's WHOLE TREE (taskkill /T).
  [switch]$IncludeWebView2,  # opt-in: also kill msedgewebview2 (embedded in Search/Outlook; respawns)
  [switch]$IncludeOneDrive,  # opt-in: also kill OneDrive (WARNING: Schwab pipeline delivers via OneDrive)
  [int]$MinAgeSeconds = 60,  # scripts mode: only kill orphans older than this (avoids spawn-race)
  # scripts mode: a process OUTSIDE every live claude tree is a generic candidate only past this age. A live seat's
  # Monitor is DETACHED from claude.exe in the Windows process table (its wrapper parent is gone -- measured on the
  # laptop 2026-10-08: a live inbox-watch reads parent DEAD), so ancestry cannot tell a live Monitor from a leaked
  # one. The harness kills every Monitor at 1800 s; past 1800 s + 60 s no live Monitor owns it.
  [int]$MonitorCapSeconds = 1860,
  # scripts mode: a tree started by the Windows Task Scheduler (root parented to the Schedule service host) is exempt
  # from ORPHAN/NATIVE while younger than this (6 h); past it the tree is a candidate again.
  [int]$ScheduledCapSeconds = 21600,
  [int[]]$OnlyPid,           # restrict targets to these PIDs (operator spot-kill; the exercise harness)
  [string]$LivenessPath = '',# default: <workspace>/org/mcp/liveness.json beside this script's .tools/
  [string]$AuditLog = '',    # default: <workspace>/org/mcp/agent-spawn-audit.log (one KILL-MAINT line per stopped tree)
  # UNATTENDED (Andrew-direct 2026-10-08 ~16:4xZ): scripts mode + Execute, run by the box's scheduled task. Refuses to
  # stop anything (and logs KILL-MAINT-ABORT) when the session map is empty while an agent runs, or when more than
  # -MaxTargets trees qualify (a classifier fault looks like a flood). Always logs one KILL-MAINT-RUN line.
  [switch]$Unattended,
  [int]$MaxTargets = 25,
  [switch]$Json
)

$ErrorActionPreference = 'Stop'
if ($Unattended) { $Mode = 'scripts'; $Execute = [switch]$true }   # apps mode is never unattended

# ---- one process snapshot (PID, PPID, Name, CommandLine, WorkingSetSize, CreationDate) ----
$all = Get-CimInstance Win32_Process
$byId = @{}
foreach ($p in $all) { $byId[[int]$p.ProcessId] = $p }
# parent -> children index, built once (the walks below were O(N) per step: ~160 s under Task Scheduler priority)
$kids = @{}
foreach ($p in $all) {
  $pp = [int]$p.ParentProcessId; $me = [int]$p.ProcessId
  if ($pp -eq $me) { continue }
  if (-not $kids.ContainsKey($pp)) { $kids[$pp] = New-Object System.Collections.Generic.List[int] }
  $kids[$pp].Add($me)
}
$runClock = [Diagnostics.Stopwatch]::StartNew()

function MB($bytes) { if ($bytes) { [math]::Round($bytes/1MB,0) } else { 0 } }

# ---- SESSION SHELLS: every live Claude Code and Codex session, with its PIDs assigned ------------------------
# Andrew-direct 2026-10-08 ~16:4xZ: unattended runs are fine "as long as there is a clear mechanism of assigning PIDs
# to Claude Code and Codex session shells. Those should never be killed by these kind of operations".
# A SESSION = its AGENT ROOT(S) (claude.exe / codex.exe) + its SESSION SHELL (the outermost shell above the root,
# below the terminal: the window the seat was launched in) + EVERY descendant of that shell. Measured on the laptop
# 2026-10-08: WindowsTerminal -> powershell.exe -> claude.exe | codex.exe (app-server + TUI) -> the agent's tools.
# Every PID in a session is protected in every mode. Name-matched claude*/codex* processes are protected too, even
# when no session resolves for them (belt and braces).
$agentRootRx = '^(claude|codex)\.exe$'
$shellRx     = '^(powershell|pwsh|cmd|bash|sh)\.exe$'
function Get-Subtree([int]$root) {
  $set = New-Object System.Collections.Generic.HashSet[int]
  [void]$set.Add($root)
  $q = New-Object System.Collections.Generic.Queue[int]
  $q.Enqueue($root)
  while ($q.Count -gt 0) {
    $cur = $q.Dequeue()
    if ($kids.ContainsKey($cur)) {
      foreach ($kid in $kids[$cur]) { if ($set.Add($kid)) { $q.Enqueue($kid) } }
    }
  }
  return ,$set
}
$sessionByHost = @{}
foreach ($r in @($all | Where-Object { $_.Name -match $agentRootRx })) {
  $rid = [int]$r.ProcessId
  $hostId = $rid; $cur = $r; $hops = 0
  while ($hops -lt 8) {
    $pp = [int]$cur.ParentProcessId
    if (-not $byId.ContainsKey($pp)) { break }
    $par = $byId[$pp]
    if ($par.Name -notmatch $shellRx) { break }
    $hostId = $pp; $cur = $par; $hops++
  }
  if (-not $sessionByHost.ContainsKey($hostId)) {
    $sessionByHost[$hostId] = [PSCustomObject]@{
      Host = $hostId; HostName = $byId[$hostId].Name; Roots = (New-Object System.Collections.Generic.List[string])
      Kind = ''; Serials = (New-Object System.Collections.Generic.List[string]); Pids = $null
    }
  }
  $sessionByHost[$hostId].Roots.Add(("{0}:{1}" -f ($r.Name -replace '\.exe$',''), $rid))
}
$sessions = @($sessionByHost.Values | Sort-Object Host)
$protectedTree = New-Object System.Collections.Generic.HashSet[int]
foreach ($s in $sessions) {
  $s.Pids = Get-Subtree $s.Host
  $kinds = @($s.Roots | ForEach-Object { $_.Split(':')[0] } | Sort-Object -Unique)
  if ($kinds -contains 'claude' -and $kinds -contains 'codex') { $s.Kind = 'Claude+Codex' }
  elseif ($kinds -contains 'codex') { $s.Kind = 'Codex' } else { $s.Kind = 'Claude Code' }
  foreach ($x in $s.Pids) { [void]$protectedTree.Add($x) }
}
foreach ($p in @($all | Where-Object { $_.Name -match 'claude|codex' })) {
  foreach ($x in (Get-Subtree ([int]$p.ProcessId))) { [void]$protectedTree.Add($x) }
}
$agentRootCount = @($all | Where-Object { $_.Name -match $agentRootRx }).Count

# ---- MSYS LINK: a session's Git Bash work keeps its session through MSYS's own parent chain ----------------------
# Git Bash fork/exec leaves a Windows ParentProcessId that has already exited, so a live seat's Bash-tool job or
# Monitor command (sleep, timeout, safe-commit, typeperf...) reads as parentless in Win32_Process. MSYS keeps the
# real chain: `ps -al` gives PID, PPID and WINPID. Measured on the laptop 2026-10-08: a Monitor's sleep chains
# sleep -> bash -> timeout -> bash whose WINPID is a Bash-tool shell inside the session; a background job's sleep
# chains to the Bash-tool shell likewise. Every MSYS descendant of an in-session WINPID joins that session, with its
# Windows subtree. When the session ends its shells die, the MSYS chain breaks (PPID 1), and the work is reapable.
$msysOk = $false
$psExe = $null
foreach ($b in @($all | Where-Object { $_.Name -eq 'bash.exe' -and $_.ExecutablePath -match '\\usr\\bin\\bash\.exe$' })) {
  $cand = Join-Path (Split-Path -Parent $b.ExecutablePath) 'ps.exe'
  if (Test-Path $cand) { $psExe = $cand; break }
}
if (-not $psExe) {
  $g = Get-Command git.exe -ErrorAction SilentlyContinue
  if ($g) { $cand = Join-Path (Split-Path -Parent (Split-Path -Parent $g.Source)) 'usr\bin\ps.exe'; if (Test-Path $cand) { $psExe = $cand } }
}
$msysRows = @()
if ($psExe) {
  try {
    $prevEap = $ErrorActionPreference; $ErrorActionPreference = 'Continue'
    $psOut = & $psExe -al 2>$null
    $ErrorActionPreference = $prevEap
    foreach ($ln in @($psOut | Select-Object -Skip 1)) {
      $tok = @(($ln.Trim()) -split '\s+')
      if ($tok.Count -gt 0 -and $tok[0] -notmatch '^\d+$') { $tok = @($tok | Select-Object -Skip 1) }   # status flag column
      if ($tok.Count -ge 4 -and $tok[0] -match '^\d+$' -and $tok[1] -match '^\d+$' -and $tok[3] -match '^\d+$') {
        $msysRows += [PSCustomObject]@{ Pid = [int]$tok[0]; PPid = [int]$tok[1]; WinPid = [int]$tok[3] }
      }
    }
    if ($msysRows.Count -gt 0) { $msysOk = $true }
  } catch { $msysOk = $false }
}
$msysJoined = 0
if ($msysOk) {
  $winToSession = @{}
  foreach ($s in $sessions) { foreach ($x in $s.Pids) { $winToSession[[int]$x] = $s } }
  $msysSession = @{}   # msys pid -> session
  $changed = $true; $guard = 0
  while ($changed -and $guard -lt 50) {
    $changed = $false; $guard++
    foreach ($r in $msysRows) {
      if ($msysSession.ContainsKey($r.Pid)) { continue }
      $s = $null
      if ($winToSession.ContainsKey($r.WinPid)) { $s = $winToSession[$r.WinPid] }
      elseif ($msysSession.ContainsKey($r.PPid)) { $s = $msysSession[$r.PPid] }
      if ($s -ne $null) {
        $msysSession[$r.Pid] = $s; $changed = $true
        foreach ($x in (Get-Subtree $r.WinPid)) {
          if (-not $winToSession.ContainsKey([int]$x)) {
            $winToSession[[int]$x] = $s; [void]$s.Pids.Add([int]$x); [void]$protectedTree.Add([int]$x); $msysJoined++
          }
        }
      }
    }
  }
} else {
  [Console]::Error.WriteLine("WARN: no MSYS process table (Git Bash ps.exe not found or empty) -- session map covers Windows ancestry only")
}

# ---- fabric comms infra (cmdline match; these are DETACHED from claude) ----
# inbox-watch monitors + MCP server + broker + pollers live under org/mcp and are
# parented to Monitor/broker hosts, NOT the claude tree -- must match by cmdline.
# Comms infra is never a GENERIC orphan. The owner-keyed rows below (watcher, poller,
# agentbus watch) are graded by OWNER instead: REPLACED (an older copy for one owner)
# or ORPHANED (the owner serial is not live). broker/server/consumer are never targets.
$infraCmd = 'org[\\/]mcp[\\/]|inbox-watch\.sh|agent-poller\.py|broker\.py|[\\/]server\.py|agentbus-sqs\.sh|agentbus-consumer\.py'
# A ' -c ' row is a Bash-tool shell or Monitor wrapper whose text QUOTES the command; it is
# never the infra row itself (the /watcher census rule).
$ownerPatterns = @(
  @{ Kind = 'inbox-watch';    Rx = 'inbox-watch\.sh"?\s+(\S+)\s+stream' },
  @{ Kind = 'agent-poller';   Rx = 'agent-poller\.py"?\s+(\S+)' },
  @{ Kind = 'agentbus-watch'; Rx = 'agentbus-sqs\.sh"?\s+(watch)\b' }
)
# Never a target in any class: a process working inside a drain worktree (CTO FAST_FIX ruling item 6).
$drainCmd = '[\\/]drain-'
# Never a target in any class: in-flight lock holders. A seat's Bash-tool call runs these through an MSYS fork whose
# Windows parent has already exited, so a LIVE seat's safe-commit / safe-apply reads as outside every claude tree
# (measured on the laptop 2026-10-08: an in-flight safe-apply and safe-commit, parents dead). Stopping one mid-flight
# leaves a merge open, a lock held, or a terraform apply half-landed.
# A running git hook is in-flight work too (safe-merge hooks run 15-45 min): exercised 2026-10-08 16:55Z, a test run
# with the Monitor cap lowered to 5 s stopped a live seat's 8-second-old `bash .git\hooks/pre-commit`.
$inFlightCmd = 'safe-(commit|merge|deploy|apply)\.sh|commit-worker\.sh|commit-gate\.sh|terraform|[\\/]hooks[\\/](pre|post|prepare|commit)-[a-z-]+'

# ---- DECLARED DETACHED JOBS and WORKER WORKTREES: never ORPHAN / NATIVE ------------------------------------------
# 0.0.0_AB_MSTR msgs 107412 + 107416 (2026-10-08): a deliberate detached job (site Z's AMGT_HARVST backfill from the
# repo's .runtime checkpoint; dell2's worker gold-run loops in C:/dev/wk-* worktrees) sits outside every claude tree
# past the Monitor cap, so the age predicate alone stopped it as ORPHAN. Two exemptions, both printed on every run:
#   DECLARED  a live marker under <git common dir>/detached-jobs/*.json written by .tools/detached-job.sh, within its
#             declared max runtime, whose process existed when the marker was written (a reused PID never matches).
#             The marked process's Windows subtree AND its MSYS descendants are exempt; an expired marker exempts nothing.
#   WORKTREE  a process whose command line, or whose cwd (MSYS /proc/<pid>/cwd, else its nearest MSYS ancestor's, else the
#             Windows process's own current directory read from its PEB), is
#             under a WORKER worktree: a linked worktree (`git worktree list --porcelain`) whose leaf or branch is wk-*.
# SEAT BOUNDARY (CT-ab-4): a tree holding a claude.exe seat with another launch serial is never stopped by taskkill /T.
. (Join-Path $PSScriptRoot 'seat-boundary.ps1')
$root0 = Split-Path -Parent $PSScriptRoot
$gitExe0 = (Get-Command git.exe -ErrorAction SilentlyContinue)
$commonDir = $null
if ($gitExe0) {
  try {
    $prevEap = $ErrorActionPreference; $ErrorActionPreference = 'Continue'
    $commonDir = (& $gitExe0.Source -C $root0 rev-parse --path-format=absolute --git-common-dir 2>$null)
    $ErrorActionPreference = $prevEap
  } catch { $commonDir = $null }
}
if (-not $commonDir -and (Test-Path (Join-Path $root0 '.git') -PathType Container)) { $commonDir = Join-Path $root0 '.git' }
$declaredSet = New-Object System.Collections.Generic.HashSet[int]
$declaredBy  = @{}   # winpid -> "owner: purpose"
$markerNotes = New-Object System.Collections.Generic.List[string]
if ($commonDir -and (Test-Path (Join-Path $commonDir 'detached-jobs'))) {
  foreach ($mf in @(Get-ChildItem (Join-Path $commonDir 'detached-jobs') -Filter '*.json' -ErrorAction SilentlyContinue)) {
    try { $mk = Get-Content $mf.FullName -Raw | ConvertFrom-Json } catch { $markerNotes.Add(("UNREADABLE {0}" -f $mf.Name)); continue }
    $wp = 0; try { $wp = [int]$mk.winpid } catch { $wp = 0 }
    $declAt = $null; try { $declAt = [datetime]::Parse([string]$mk.declared_at).ToUniversalTime() } catch { $declAt = $null }
    $maxS = 0; try { $maxS = [int]$mk.max_seconds } catch { $maxS = 0 }
    $label = ("{0}: {1}" -f $mk.owner, $mk.purpose)
    if ($wp -le 0 -or -not $declAt -or $maxS -le 0) { $markerNotes.Add(("MALFORMED {0}" -f $mf.Name)); continue }
    if (-not $byId.ContainsKey($wp)) { $markerNotes.Add(("GONE {0} (pid {1} not running; {2})" -f $mf.Name, $wp, $label)); continue }
    if ((Get-Date).ToUniversalTime() -gt $declAt.AddSeconds($maxS)) { $markerNotes.Add(("EXPIRED {0} (pid {1}, {2}s past; {3})" -f $mf.Name, $wp, [int]((Get-Date).ToUniversalTime() - $declAt.AddSeconds($maxS)).TotalSeconds, $label)); continue }
    $pc = $byId[$wp].CreationDate
    if ($pc -and $pc.ToUniversalTime() -gt $declAt.AddSeconds(10)) { $markerNotes.Add(("REUSED {0} (pid {1} started after the marker; {2})" -f $mf.Name, $wp, $label)); continue }
    foreach ($x in (Get-Subtree $wp)) { [void]$declaredSet.Add([int]$x); $declaredBy[[int]$x] = $label }
    $markerNotes.Add(("LIVE {0} (pid {1}; {2})" -f $mf.Name, $wp, $label))
  }
}
# SCHEDULED: a job the Windows Task Scheduler started (its root's parent is the Schedule service host) is a deliberate
# job, never an ORPHAN. Measured 2026-10-13 03:39Z on dell1: the "Opal MDPF_DEMQUE daily draw" task (state Running, 72 h
# limit) read as five ORPHAN targets at 69 minutes, past the Monitor cap. Exempt while younger than -ScheduledCapSeconds
# (a runaway past the cap is a target again); the subtree and its MSYS descendants ride the DECLARED propagation below.
$schedPid = 0
try { $schedSvc = Get-CimInstance Win32_Service -Filter "Name='Schedule'" -ErrorAction Stop; $schedPid = [int]$schedSvc.ProcessId } catch { $schedPid = 0 }
if ($schedPid -gt 0) {
  $nowSch = (Get-Date).ToUniversalTime()
  foreach ($sp in @($all | Where-Object { [int]$_.ParentProcessId -eq $schedPid -and $_.Name -match '^(bash|sh|python|pythonw|powershell|pwsh|cmd)\.exe$' })) {
    $sc = $sp.CreationDate
    if (-not $sc) { continue }
    $ageSch = [int]($nowSch - $sc.ToUniversalTime()).TotalSeconds
    if ($ageSch -gt $ScheduledCapSeconds) { $markerNotes.Add(("SCHEDULED-EXPIRED pid {0} ({1}s old, cap {2}s)" -f $sp.ProcessId, $ageSch, $ScheduledCapSeconds)); continue }
    $labSch = ("SCHEDULED Task Scheduler job pid {0} started {1:HH:mm}Z" -f $sp.ProcessId, $sc.ToUniversalTime())
    foreach ($x in (Get-Subtree ([int]$sp.ProcessId))) { [void]$declaredSet.Add([int]$x); $declaredBy[[int]$x] = $labSch }
    $markerNotes.Add(("LIVE {0}" -f $labSch))
  }
}
# MSYS descendants of a declared PID (Git Bash fork/exec breaks the Windows parent chain; MSYS keeps it)
if ($msysOk -and $declaredSet.Count -gt 0) {
  $msysDecl = New-Object System.Collections.Generic.HashSet[int]
  foreach ($r in $msysRows) { if ($declaredSet.Contains($r.WinPid)) { [void]$msysDecl.Add($r.Pid) } }
  $changed = $true; $guard = 0
  while ($changed -and $guard -lt 50) {
    $changed = $false; $guard++
    foreach ($r in $msysRows) {
      if (-not $msysDecl.Contains($r.Pid) -and $msysDecl.Contains($r.PPid)) {
        [void]$msysDecl.Add($r.Pid); $changed = $true
        $lab = $null
        foreach ($q in $msysRows) { if ($q.Pid -eq $r.PPid -and $declaredBy.ContainsKey($q.WinPid)) { $lab = $declaredBy[$q.WinPid] } }
        foreach ($x in (Get-Subtree $r.WinPid)) { [void]$declaredSet.Add([int]$x); if ($lab) { $declaredBy[[int]$x] = $lab } }
      }
    }
  }
}
function Norm-Posix([string]$p) {
  if (-not $p) { return '' }
  $p = $p.Trim().Replace('\', '/').ToLower()
  if ($p -match '^/cygdrive/([a-z])(/.*)?$') { $p = '/' + $matches[1] + $matches[2] }
  elseif ($p -match '^([a-z]):(/.*)?$') { $p = '/' + $matches[1] + $matches[2] }
  return $p.TrimEnd('/')
}
$workerTrees = New-Object System.Collections.Generic.List[string]
if ($gitExe0) {
  try {
    $prevEap = $ErrorActionPreference; $ErrorActionPreference = 'Continue'
    $wtOut = @(& $gitExe0.Source -C $root0 worktree list --porcelain 2>$null)
    $ErrorActionPreference = $prevEap
    $cur = $null; $first = $true
    foreach ($ln in ($wtOut + @(''))) {
      if ($ln -match '^worktree (.+)$') { $cur = @{ Path = $matches[1]; Branch = '' } ; continue }
      if ($ln -match '^branch refs/heads/(.+)$' -and $cur) { $cur.Branch = $matches[1]; continue }
      if ($ln -eq '' -and $cur) {
        if (-not $first -and ((Split-Path -Leaf $cur.Path) -match '^wk-' -or $cur.Branch -match '^wk-')) { $workerTrees.Add((Norm-Posix $cur.Path)) }
        $first = $false; $cur = $null
      }
    }
  } catch { [Console]::Error.WriteLine("WARN: git worktree list unreadable -- WORKTREE exemption covers no tree this run") }
}
function Under-WorkerTree([string]$text) {
  # $text is a command line or a cwd; a worker tree matches in any of its three spellings, as a whole path segment
  if (-not $text) { return $null }
  $t = $text.Replace('\', '/').ToLower()
  foreach ($w in $workerTrees) {
    $forms = @($w)
    if ($w -match '^/([a-z])(/.*)$') { $forms += @(($matches[1] + ':' + $matches[2]), ('/cygdrive' + $w)) }
    foreach ($f in $forms) { if ($t -match ([regex]::Escape($f) + '([/"'' ]|$)')) { return $w } }
  }
  return $null
}

# ---- owner liveness: serial -> live MCP server pid (liveness.json, pid confirmed as a server.py) ----
if (-not $LivenessPath) { $LivenessPath = Join-Path (Split-Path -Parent $PSScriptRoot) 'org\mcp\liveness.json' }
if (-not $AuditLog)     { $AuditLog     = Join-Path (Split-Path -Parent $PSScriptRoot) 'org\mcp\agent-spawn-audit.log' }
$liveSerials = $null   # $null = UNREADABLE: no owner verdict, so no ORPHANED target this run (fail closed)
try {
  $lj = Get-Content $LivenessPath -Raw -ErrorAction Stop | ConvertFrom-Json
  $liveSerials = @{}
  foreach ($e in $lj.PSObject.Properties) {
    $lp = 0
    try { $lp = [int]$e.Value.pid } catch { $lp = 0 }
    # a Claude seat's liveness pid is its MCP server.py; a Codex seat's is its codex-agent-heartbeat.py
    if ($lp -gt 0 -and $byId.ContainsKey($lp) -and $byId[$lp].CommandLine -match 'server\.py|codex-agent-heartbeat\.py') {
      $liveSerials[$e.Name] = $lp
      # bind the serial to the session whose subtree holds that pid
      foreach ($s in $sessions) { if ($s.Pids.Contains($lp)) { $s.Serials.Add($e.Name) } }
    }
  }
} catch {
  [Console]::Error.WriteLine(("WARN: liveness unreadable ({0}) -- ORPHANED class disabled this run" -f $LivenessPath))
}
# A file that PARSES but yields ZERO live owners while sessions are up is not a verdict either (dell2 08:31Z: a read
# during a rewrite left an empty map, every owner-keyed poller was classed ORPHANED, 16 were killed). Fail closed.
if ($null -ne $liveSerials -and $liveSerials.Count -eq 0 -and @($sessions).Count -gt 0) {
  [Console]::Error.WriteLine(("WARN: liveness parsed but 0 owner serial(s) live with {0} session(s) up -- ORPHANED class disabled this run" -f @($sessions).Count))
  $liveSerials = $null
}

function Write-Audit([string]$line) {
  # one ASCII line to the audit log; an append failure never fails the run
  try {
    $line = ($line -replace '[^\x20-\x7E]', '?')
    [IO.File]::AppendAllText($AuditLog, $line + "`n", [Text.Encoding]::ASCII)
  } catch {
    [Console]::Error.WriteLine(("WARN: audit append failed ({0}): {1}" -f $AuditLog, $_.Exception.Message))
  }
}
$runBy = $env:OPAL_AGENT_SERIAL
if (-not $runBy) { if ($Unattended) { $runBy = 'kill-maint-task' } else { $runBy = 'unknown' } }
function UtcNow { (Get-Date).ToUniversalTime().ToString('yyyy-MM-ddTHH:mm:ssZ') }

function Get-Descendants([int]$root) {
  $seen = New-Object System.Collections.Generic.HashSet[int]
  $q = New-Object System.Collections.Generic.Queue[int]
  $q.Enqueue($root)
  while ($q.Count -gt 0) {
    $cur = $q.Dequeue()
    if ($kids.ContainsKey($cur)) {
      foreach ($kid in $kids[$cur]) { if ($kid -ne $root -and $seen.Add($kid)) { $q.Enqueue($kid) } }
    }
  }
  return ,$seen
}

# ---- HARD DENY: never kill, in any mode, even if a pattern over-matches -----
$denyName = '^(System|Idle|Registry|csrss|wininit|winlogon|services|lsass|smss|' +
            'fontdrvhost|dwm|explorer|conhost|OpenConsole|WindowsTerminal|wt|' +
            'powershell|pwsh|WerFault|sihost|ctfmon|RuntimeBroker|taskhostw|' +
            'svchost|spoolsv|dllhost|claude|codex|SearchHost|StartMenuExperienceHost)(\.exe)?$'
# security / EDR -- IT-managed, killing is both futile and a security event:
$denySecurity = 'EPSecurityService|EPIntegrationService|Sysmon|Huntress|Sentinel|MsMpEng|SecurityHealth|Defender|CSFalcon|CrowdStrike'

function Is-Denied($proc) {
  if ($proc.Name -match $denyName) { return $true }
  if ($proc.Name -match $denySecurity) { return $true }
  if ($proc.CommandLine -and $proc.CommandLine -match $denySecurity) { return $true }
  return $false
}

$targets = New-Object System.Collections.Generic.List[object]
$kept    = New-Object System.Collections.Generic.List[object]   # owner-keyed infra left alone (the negative control)
$exempt  = New-Object System.Collections.Generic.List[object]   # DECLARED / WORKTREE generic candidates left alone

function Add-ScriptTarget($proc, [string]$cls, [string]$why) {
  $a = $null
  if ($proc.CreationDate) { $a = ((Get-Date) - $proc.CreationDate).TotalSeconds }
  $cl = ''
  if ($proc.CommandLine) { $cl = ($proc.CommandLine -replace '\s+',' ') }
  $targets.Add([PSCustomObject]@{
    Category = 'script'
    Class    = $cls
    Id       = [int]$proc.ProcessId
    Created  = $proc.CreationDate
    Name     = $proc.Name
    MB       = MB $proc.WorkingSetSize
    AgeSec   = if ($a -ne $null) { [math]::Round($a,0) } else { 'na' }
    Reason   = "$cls -- $why"
    Cmd      = $cl.Substring(0,[Math]::Min(120,$cl.Length))
  })
}

# ============================ SCRIPTS MODE ==================================
# Classes:
#   ORPHAN    bash/py outside every live claude tree, older than the Monitor cap (incl. a dead session's Bash-tool shells)
#   NATIVE    typeperf/awk/gawk/tail/timeout outside every live claude tree, older than the Monitor cap (the dell1 leak)
#   REPLACED  an older copy of an owner-keyed infra row (watcher/poller per serial; agentbus watch per box); newest kept
#   ORPHANED  an owner-keyed watcher/poller whose serial has no live MCP server in liveness.json
if ($Mode -eq 'scripts' -or $Mode -eq 'all') {
  $now = Get-Date
  $ownerRows = @{}
  $genericCands = New-Object System.Collections.Generic.List[object]
  foreach ($p in $all) {
    if ($p.Name -notmatch '^(bash|python|pythonw|py|typeperf|awk|gawk|tail|timeout)\.exe$') { continue }
    $procId = [int]$p.ProcessId
    if (Is-Denied $p) { continue }
    if ($protectedTree.Contains($procId)) { continue }                       # live-claude descendant
    $cmd = ''
    if ($p.CommandLine) { $cmd = $p.CommandLine }
    if (-not $cmd) { continue }                                              # unreadable command line: cannot classify, never
    if ($cmd -match $drainCmd) { continue }                                  # drain worktree: never
    if ($cmd -match $inFlightCmd) { continue }                               # in-flight lock holder: never
    # age guard: skip very young procs (parent link may not have resolved yet)
    $age = $null
    if ($p.CreationDate) { $age = ($now - $p.CreationDate).TotalSeconds }
    if ($age -ne $null -and $age -lt $MinAgeSeconds) { continue }
    if ($cmd -match $infraCmd) {                                              # comms infra: owner-keyed or never
      if ($cmd -notmatch ' -c ') {
        foreach ($op in $ownerPatterns) {
          if ($cmd -match $op.Rx) {
            $k = $op.Kind + '|' + $matches[1]
            if (-not $ownerRows.ContainsKey($k)) { $ownerRows[$k] = New-Object System.Collections.Generic.List[object] }
            $ownerRows[$k].Add($p)
            break
          }
        }
      }
      continue
    }
    if ($age -eq $null -or $age -lt $MonitorCapSeconds) { continue }        # could still be a live seat's Monitor
    $genericCands.Add($p)
  }
  # the two exemptions (DECLARED, WORKTREE) are read for the generic candidates only; cwd costs one bash call
  $cwdOf = @{}   # winpid -> cwd (MSYS /proc/<msys pid>/cwd, else the nearest MSYS ancestor's)
  if ($msysOk -and $genericCands.Count -gt 0 -and $workerTrees.Count -gt 0) {
    $msysByWin = @{}; $msysByPid = @{}
    foreach ($r in $msysRows) { $msysByWin[$r.WinPid] = $r; $msysByPid[$r.Pid] = $r }
    $want = New-Object System.Collections.Generic.List[int]
    $chain = @{}   # winpid -> msys pids, self first then ancestors
    foreach ($c in $genericCands) {
      $w = [int]$c.ProcessId; $lst = New-Object System.Collections.Generic.List[int]
      # an exec'd MSYS process gets a new WINPID under the original Windows process (measured: `bash -c "sleep N"`
      # leaves bash.exe as the Windows stub and the MSYS row carries sleep's WINPID), so read the first subtree row
      $anchor = $null
      if ($msysByWin.ContainsKey($w)) { $anchor = $w } else { foreach ($x in (Get-Subtree $w)) { if ($msysByWin.ContainsKey([int]$x)) { $anchor = [int]$x; break } } }
      if ($anchor -ne $null) {
        $r = $msysByWin[$anchor]; $hops = 0
        while ($r -and $hops -lt 12) { $lst.Add($r.Pid); [void]$want.Add($r.Pid); if ($msysByPid.ContainsKey($r.PPid) -and $r.PPid -ne $r.Pid) { $r = $msysByPid[$r.PPid] } else { $r = $null }; $hops++ }
      }
      $chain[$w] = $lst
    }
    $bashExe = Join-Path (Split-Path -Parent $psExe) 'bash.exe'
    if ($want.Count -gt 0 -and (Test-Path $bashExe)) {
      try {
        $prevEap = $ErrorActionPreference; $ErrorActionPreference = 'Continue'
        # no double quote inside the script text: PS 5.1 mangles embedded quotes in a native argument
        $cwdOut = @(& $bashExe -c 'for p; do echo $p $(readlink /proc/$p/cwd 2>/dev/null); done' _ @($want | Sort-Object -Unique) 2>$null)
        $ErrorActionPreference = $prevEap
        $cwdByMsys = @{}
        foreach ($ln in $cwdOut) { if ($ln -match '^(\d+) (.+)$') { $cwdByMsys[[int]$matches[1]] = $matches[2] } }
        foreach ($w in @($chain.Keys)) { foreach ($mp in $chain[$w]) { if ($cwdByMsys.ContainsKey($mp)) { $cwdOf[$w] = $cwdByMsys[$mp]; break } } }
      } catch { [Console]::Error.WriteLine("WARN: MSYS cwd read failed -- WORKTREE exemption reads command lines only this run") }
    }
  }
  # NATIVE cwd (AMGT_HARVST, dell1 08:08:36Z, 1.0.0_SA_CTO msg 107868): a native python.exe whose launching bash has exited
  # has no MSYS row, so its worktree was invisible when its command line carried a RELATIVE path, and it was stopped as
  # ORPHAN. Read the Windows process's own current directory from its PEB (read-only: QUERY_INFORMATION + VM_READ, a
  # 64-bit target only) for every candidate the MSYS read left without a cwd. Owner 4.0.0_SA_CRO~B (built by 4.0.0_SA_CRO).
  if ($genericCands.Count -gt 0 -and $workerTrees.Count -gt 0) {
    try {
      if (-not ('OpalProcCwd' -as [type])) {
        Add-Type -TypeDefinition @'
using System; using System.Runtime.InteropServices; using System.Text;
public static class OpalProcCwd {
  [StructLayout(LayoutKind.Sequential)] struct PBI { public IntPtr Exit; public IntPtr Peb; public IntPtr Aff; public IntPtr Pri; public IntPtr Pid; public IntPtr Par; }
  [DllImport("ntdll.dll")] static extern int NtQueryInformationProcess(IntPtr h, int c, ref PBI p, int len, out int ret);
  [DllImport("kernel32.dll", SetLastError = true)] static extern IntPtr OpenProcess(int access, bool inherit, int pid);
  [DllImport("kernel32.dll", SetLastError = true)] static extern bool ReadProcessMemory(IntPtr h, IntPtr addr, byte[] buf, IntPtr size, out IntPtr read);
  [DllImport("kernel32.dll", SetLastError = true)] static extern bool IsWow64Process(IntPtr h, out bool wow);
  [DllImport("kernel32.dll")] static extern bool CloseHandle(IntPtr h);
  public static string Get(int pid) {
    if (IntPtr.Size != 8) return null;
    IntPtr h = OpenProcess(0x0410, false, pid);
    if (h == IntPtr.Zero) return null;
    try {
      bool wow; if (IsWow64Process(h, out wow) && wow) return null;
      PBI p = new PBI(); int ret; IntPtr rd;
      if (NtQueryInformationProcess(h, 0, ref p, Marshal.SizeOf(p), out ret) != 0) return null;
      byte[] b = new byte[8];
      if (!ReadProcessMemory(h, IntPtr.Add(p.Peb, 0x20), b, (IntPtr)8, out rd)) return null;
      IntPtr pp = (IntPtr)BitConverter.ToInt64(b, 0);
      byte[] us = new byte[16];
      if (!ReadProcessMemory(h, IntPtr.Add(pp, 0x38), us, (IntPtr)16, out rd)) return null;
      int len = BitConverter.ToUInt16(us, 0);
      if (len <= 0) return null;
      byte[] s = new byte[len];
      if (!ReadProcessMemory(h, (IntPtr)BitConverter.ToInt64(us, 8), s, (IntPtr)len, out rd)) return null;
      return Encoding.Unicode.GetString(s);
    } finally { CloseHandle(h); }
  }
}
'@
      }
      foreach ($c in $genericCands) {
        $w = [int]$c.ProcessId
        if (-not $cwdOf.ContainsKey($w)) { $d = [OpalProcCwd]::Get($w); if ($d) { $cwdOf[$w] = $d } }
      }
    } catch { [Console]::Error.WriteLine("WARN: native cwd read failed -- WORKTREE exemption reads MSYS cwd and command lines only this run") }
  }
  foreach ($p in $genericCands) {
    $procId = [int]$p.ProcessId
    if ($declaredSet.Contains($procId)) {
      $exempt.Add([PSCustomObject]@{ Id = $procId; Name = $p.Name; Why = ("DECLARED job ({0})" -f $declaredBy[$procId]) }); continue
    }
    $wt = Under-WorkerTree $p.CommandLine
    $via = 'command line'
    if (-not $wt -and $cwdOf.ContainsKey($procId)) { $wt = Under-WorkerTree $cwdOf[$procId]; $via = 'cwd' }
    if ($wt) { $exempt.Add([PSCustomObject]@{ Id = $procId; Name = $p.Name; Why = ("WORKTREE {0} ({1})" -f $wt, $via) }); continue }
    if ($p.Name -match '^(typeperf|awk|gawk|tail|timeout)\.exe$') {
      Add-ScriptTarget $p 'NATIVE' ("native long-runner outside every live claude tree, older than the {0}s Monitor cap" -f $MonitorCapSeconds)
    } else {
      Add-ScriptTarget $p 'ORPHAN' ("bash/py outside every live claude tree, older than the {0}s Monitor cap, not comms infra" -f $MonitorCapSeconds)
    }
  }
  foreach ($k in @($ownerRows.Keys)) {
    $kind  = $k.Substring(0, $k.IndexOf('|'))
    $owner = $k.Substring($k.IndexOf('|') + 1)
    $rows  = @($ownerRows[$k] | Sort-Object CreationDate -Descending)
    $ownerLive = $true                                     # agentbus watch is per box: no serial owner
    if ($kind -ne 'agentbus-watch' -and $liveSerials -ne $null) { $ownerLive = $liveSerials.ContainsKey($owner) }
    if (-not $ownerLive) {
      foreach ($r in $rows) { Add-ScriptTarget $r 'ORPHANED' ("{0} for {1} -- no live MCP server for that serial in liveness.json" -f $kind, $owner) }
      continue
    }
    $kept.Add([PSCustomObject]@{ Kind = $kind; Owner = $owner; Id = [int]$rows[0].ProcessId; Copies = $rows.Count })
    for ($i = 1; $i -lt $rows.Count; $i++) {
      Add-ScriptTarget $rows[$i] 'REPLACED' ("older {0} for {1}; newest PID {2} kept" -f $kind, $owner, $rows[0].ProcessId)
    }
  }
}

# ============================== APPS MODE ===================================
if ($Mode -eq 'apps' -or $Mode -eq 'all') {
  # standalone bloat apps (main + child procs all matched by name):
  # TAILSCALE REMOVED FROM THIS LIST 2026-08-13 -- IT IS REMOTE-ACCESS INFRASTRUCTURE, NOT BLOAT.
  # Andrew-direct the same evening: "i need private access to remote in to that device at any time"
  # + "I recommend we set up a tailscale remote now so this never happens again". Tailscale is the
  # transport for that access AND -- per the freeze-#11 investigation (LD-0409) -- the instrument
  # that makes the site Z box's only recurring failure class attributable at all: it is how someone
  # reaches a wedged box to force a dump.
  # >> THE HAZARD THIS CLOSES IS SELF-INFLICTED AND WAS LIVE ON BOTH BOXES: this reaper matched
  # tailscale/tailscaled/tailscale-ipn BY NAME, so a routine `/kill apps go` would have severed the
  # remote path -- on the laptop TODAY (tailscaled + tailscale-ipn are running here right now), and
  # on site Z the moment it is installed. A maintenance tool that reaps the estate's own remote
  # access is exactly the "it never happens again" failure Andrew's instruction is aimed at. <<
  # Caught by 0.0.0_AB_MSTR~Z while prepping the install; verified independently at this seat
  # against both this engine and .claude/skills/kill/SKILL.md.
  # NOTE the sibling GUI process is `tailscale-ipn`; the SERVICE is `Tailscale`/`tailscaled` and was
  # never reachable by this process sweep anyway -- removing all three keeps the name set honest
  # rather than leaving a partial guard that reads as protection.
  $appName = '^(msedge|chrome|chromium|ms-teams|Teams|' +
             'mscopilot|mscopilot_proxy|copilot|Spotify|Slack|Discord|Zoom|WhatsApp|Skype|' +
             'GoogleUpdate|SpotifyWebHelper)(\.exe)?$'
  # Playwright / Claude-automation browser guard: a browser we must NOT kill.
  $automationCmd = '--remote-debugging|ms-playwright|--headless|playwright[\\/]|--enable-automation'

  foreach ($p in $all) {
    $procId = [int]$p.ProcessId
    $isApp = ($p.Name -match $appName)
    if ($IncludeWebView2 -and $p.Name -match '^msedgewebview2(\.exe)?$') { $isApp = $true }
    if ($IncludeOneDrive  -and $p.Name -match '^OneDrive') { $isApp = $true }
    if (-not $isApp) { continue }
    if (Is-Denied $p) { continue }
    if ($protectedTree.Contains($procId)) { continue }                        # launched by live claude
    if ($p.CommandLine -and $p.CommandLine -match $automationCmd) { continue } # Playwright/automation browser
    $cl = ''
    if ($p.CommandLine) { $cl = ($p.CommandLine -replace '\s+',' ') }
    $targets.Add([PSCustomObject]@{
      Category = 'app'
      Id       = $procId
      Name     = $p.Name
      MB       = MB $p.WorkingSetSize
      AgeSec   = 'na'
      Reason   = 'bloat app (not claude/playwright, not a session host)'
      Cmd      = $cl.Substring(0,[Math]::Min(120,$cl.Length))
    })
  }
}


# ============================== REPORT ======================================
if ($OnlyPid) {
  $narrowed = New-Object System.Collections.Generic.List[object]
  foreach ($t in $targets) { if ($OnlyPid -contains [int]$t.Id) { $narrowed.Add($t) } }
  $targets = $narrowed
}
$totalMB = ($targets | Measure-Object MB -Sum).Sum
if (-not $totalMB) { $totalMB = 0 }
$sessionPidCount = 0
foreach ($s in $sessions) { $sessionPidCount += $s.Pids.Count }

if ($Json) {
  [PSCustomObject]@{
    mode=$Mode; execute=[bool]$Execute; unattended=[bool]$Unattended; count=$targets.Count; reclaim_mb=$totalMB;
    sessions=@($sessions | ForEach-Object { [PSCustomObject]@{ kind=$_.Kind; host=$_.Host; host_name=$_.HostName;
      roots=@($_.Roots); serials=@($_.Serials); pids=@($_.Pids) } });
    targets=$targets; kept=$kept; exempt=$exempt; markers=@($markerNotes); worker_trees=@($workerTrees)
  } | ConvertTo-Json -Depth 5
  if (-not $Execute) { return }
}

$modeLabel = $Mode.ToUpper()
if ($Unattended) { $banner = "UNATTENDED EXECUTE" } elseif ($Execute) { $banner = "EXECUTE" } else { $banner = "DRY-RUN (nothing killed)" }
Write-Output "=== /kill $modeLabel -- $banner ==="

# THE SESSION MAP -- printed on every run: which PIDs belong to which Claude Code / Codex session (never targets)
Write-Output ""
if ($msysOk) { $msysNote = ("{0} joined via the MSYS chain" -f $msysJoined) } else { $msysNote = 'MSYS chain UNAVAILABLE' }
Write-Output ("--- session shells: {0} session(s), {1} PIDs ({2}), never targets ---" -f $sessions.Count, $sessionPidCount, $msysNote)
foreach ($s in $sessions) {
  $ser = '(no serial bound)'
  if ($s.Serials.Count -gt 0) { $ser = ($s.Serials -join ',') }
  Write-Output ("  {0,-12} shell PID {1,-6} {2,-15} roots {3,-28} {4,4} PIDs  {5}" -f $s.Kind, $s.Host, $s.HostName, ($s.Roots -join ','), $s.Pids.Count, $ser)
}
Write-Output ("protected: {0} PIDs (session shells + claude*/codex* trees) + comms-infra (server/broker/consumer never; watcher/poller/agentbus watch by owner) + in-flight safe-*/terraform + drain-* worktrees + hard-deny system/EDR" -f $protectedTree.Count)
if ($liveSerials -ne $null) { $nLive = $liveSerials.Count } else { $nLive = 'UNREADABLE' }
Write-Output ("owners: {0} serial(s) live in {1}; Monitor cap {2}s" -f $nLive, $LivenessPath, $MonitorCapSeconds)
if ($kept.Count -gt 0) {
  Write-Output ""
  Write-Output "--- owner-keyed infra KEPT (owner live; newest copy) ---"
  $kept | Sort-Object Kind, Owner | ForEach-Object {
    Write-Output ("  KEEP PID {0,-6} {1,-15} {2}  (copies={3})" -f $_.Id, $_.Kind, $_.Owner, $_.Copies)
  }
}
Write-Output ""
Write-Output ("--- deliberate detached jobs: {0} marker(s), {1} worker worktree(s); {2} candidate(s) EXEMPT ---" -f $markerNotes.Count, $workerTrees.Count, $exempt.Count)
foreach ($n in $markerNotes) { Write-Output ("  MARKER {0}" -f $n) }
foreach ($e in $exempt) { Write-Output ("  EXEMPT PID {0,-6} {1,-15} {2}" -f $e.Id, $e.Name, $e.Why) }

# UNATTENDED GUARDS: refuse to act on a run that looks wrong; log why
if ($Unattended) {
  $abort = ''
  $msysLive = @($all | Where-Object { $_.ExecutablePath -match '\\usr\\bin\\' }).Count
  if ($agentRootCount -gt 0 -and $sessions.Count -eq 0) { $abort = "agent processes running ($agentRootCount) but the session map is empty" }
  elseif ($msysLive -gt 0 -and -not $msysOk) { $abort = "Git Bash processes running ($msysLive) but no MSYS process table -- a session's bash work cannot be assigned" }
  elseif ($targets.Count -gt $MaxTargets) { $abort = ("{0} targets exceed -MaxTargets {1}" -f $targets.Count, $MaxTargets) }
  if ($abort) {
    Write-Output ""
    Write-Output "ABORT: $abort -- nothing stopped."
    Write-Audit ("{0}  KILL-MAINT-ABORT  by {1}  host={2}  sessions={3}  targets={4}  reason={5}" -f (UtcNow), $runBy, $env:COMPUTERNAME, $sessions.Count, $targets.Count, $abort)
    return
  }
}

if ($targets.Count -eq 0) {
  Write-Output ""
  Write-Output "OK: no kill targets found. Nothing to do."
  if ($Unattended) {
    Write-Audit ("{0}  KILL-MAINT-RUN  by {1}  host={2}  sessions={3}  session_pids={4}  targets=0  killed=0  failed=0  msys_ok={5}  msys_rows={6}  msys_joined={7}  ms={8}" -f (UtcNow), $runBy, $env:COMPUTERNAME, $sessions.Count, $sessionPidCount, $msysOk, $msysRows.Count, $msysJoined, $runClock.ElapsedMilliseconds)
  }
  return
}

# grouped summary
Write-Output ""
Write-Output "--- summary by process ---"
$targets | Group-Object Name | Sort-Object { ($_.Group | Measure-Object MB -Sum).Sum } -Descending | ForEach-Object {
  $g = $_.Group
  $m = ($g | Measure-Object MB -Sum).Sum
  Write-Output ("  {0,-24} x{1,-3} {2,6} MB" -f $_.Name, $_.Count, $m)
}
Write-Output ("  {0,-24}      {1,6} MB reclaimable" -f 'TOTAL', $totalMB)

# detail
Write-Output ""
Write-Output "--- targets ---"
$targets | Sort-Object Category, Name | ForEach-Object {
  Write-Output ("  [{0}] PID {1,-6} {2,-22} {3,5}MB age={4,-5} :: {5}" -f $_.Category, $_.Id, $_.Name, $_.MB, $_.AgeSec, $_.Reason)
}

if (-not $Execute) {
  Write-Output ""
  Write-Output "DRY-RUN: re-run with -Execute (skill: '/kill $Mode go') to apply."
  return
}

# ----------------------------- KILL -----------------------------------------
Write-Output ""
Write-Output "--- killing ---"
$killed = 0; $failed = 0; $freed = 0
# WHOLE-TREE stop (taskkill /T). Stop-Process on one PID orphans native children: measured on the laptop
# 2026-10-08, stopping a bash wrapper left its typeperf + awk running; taskkill /T left none.
foreach ($t in $targets) {
  # a tree stop must never reach a session shell or an agent: skip any tree holding a protected PID or a claude/codex
  $desc = Get-Descendants $t.Id
  $sessionBelow = $false
  foreach ($d in $desc) {
    if ($protectedTree.Contains($d)) { $sessionBelow = $true }
    if ($byId.ContainsKey($d) -and $byId[$d].Name -match 'claude|codex') { $sessionBelow = $true }
    if ($declaredSet.Contains([int]$d)) { $sessionBelow = $true }
  }
  if ($sessionBelow -or $protectedTree.Contains([int]$t.Id)) {
    Write-Output ("  SKIP: PID {0,-6} {1,-22} its tree holds a session PID or a declared job" -f $t.Id, $t.Name)
    continue
  }
  # re-read the PID: gone (an earlier tree stop took it) or REUSED since the snapshot means hands off
  $now1 = Get-CimInstance Win32_Process -Filter ("ProcessId={0}" -f $t.Id)
  if (-not $now1) {
    Write-Output ("  SKIP: PID {0,-6} {1,-22} already exited" -f $t.Id, $t.Name)
    continue
  }
  if ($t.PSObject.Properties['Created'] -and $t.Created -and $now1.CreationDate -ne $t.Created) {
    Write-Output ("  SKIP: PID {0,-6} {1,-22} was reused since the snapshot" -f $t.Id, $t.Name)
    continue
  }
  # SEAT BOUNDARY (CT-ab-4): judged on the target's own launch serial; a foreign seat anywhere under it refuses this target.
  $tSerial = Get-LaunchSerial -CommandLine $now1.CommandLine
  $foreignSeats = $null; $seatErr = ''
  try { $foreignSeats = @(Test-SeatBoundary -RootPid ([int]$t.Id) -TargetSerial $tSerial) } catch { $seatErr = $_.Exception.Message }
  if ($null -eq $foreignSeats -or @($foreignSeats).Count -gt 0) {
    if ($null -eq $foreignSeats) {
      Write-Output ("  REFUSED: seat boundary -- PID {0,-6} {1,-22} not evaluated, not stopped: {2}" -f $t.Id, $t.Name, $seatErr)
    } else {
      foreach ($f in $foreignSeats) {
        Write-Output ("  REFUSED: seat boundary -- PID {0,-6} {1,-22} holds foreign seat {2} at pid {3}; tree not stopped" -f $t.Id, $t.Name, $f.Serial, $f.ProcessId)
      }
      $foreignList = (@($foreignSeats) | ForEach-Object { "$($_.Serial)@$($_.ProcessId)" }) -join ','
      Write-Audit ("{0}  KILL-MAINT-REFUSED  by {1}  pid={2}  name={3}  foreign={4}  reason=seat-boundary" -f (UtcNow), $runBy, $t.Id, $t.Name, $foreignList)
    }
    continue
  }
  $prevEap = $ErrorActionPreference; $ErrorActionPreference = 'Continue'
  $tkOut = (& taskkill.exe /T /F /PID $t.Id 2>&1 | Out-String).Trim()
  $tkRc = $LASTEXITCODE
  $ErrorActionPreference = $prevEap
  if ($tkRc -eq 0) {
    $killed++; $freed += $t.MB
    Write-Output ("  OK:   stopped tree PID {0,-6} {1,-22} (+{2} descendant(s), {3}MB)" -f $t.Id, $t.Name, $desc.Count, $t.MB)
    # RECORD every stop (Andrew-direct 2026-10-08 ~16:2xZ: "keeps a record of what it stopped"), beside the
    # KILL / KILL-ORPHAN lines of kill-agent.ps1 and kill-orphans.
    $cls = $t.Category
    if ($t.PSObject.Properties['Class'] -and $t.Class) { $cls = $t.Class }
    Write-Audit ("{0}  KILL-MAINT  {1}  by {2}  pid={3}  name={4}  descendants={5}  reason={6}  cmd={7}" -f (UtcNow), $cls, $runBy, $t.Id, $t.Name, $desc.Count, $t.Reason, $t.Cmd)
  } elseif (-not (Get-Process -Id $t.Id -ErrorAction SilentlyContinue)) {
    Write-Output ("  SKIP: PID {0,-6} {1,-22} already exited" -f $t.Id, $t.Name)
  } else {
    $failed++
    Write-Output ("  WARN: could not stop tree PID {0,-6} {1,-22} -- rc={2} {3}" -f $t.Id, $t.Name, $tkRc, $tkOut)
  }
}
Write-Output ""
Write-Output ("DONE: killed {0}, failed {1}, ~{2}MB reclaimed." -f $killed, $failed, $freed)
if ($Unattended) {
  Write-Audit ("{0}  KILL-MAINT-RUN  by {1}  host={2}  sessions={3}  session_pids={4}  targets={5}  killed={6}  failed={7}  msys_ok={8}  msys_rows={9}  msys_joined={10}  ms={11}" -f (UtcNow), $runBy, $env:COMPUTERNAME, $sessions.Count, $sessionPidCount, $targets.Count, $killed, $failed, $msysOk, $msysRows.Count, $msysJoined, $runClock.ElapsedMilliseconds)
}

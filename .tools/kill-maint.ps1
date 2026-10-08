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
  [int[]]$OnlyPid,           # restrict targets to these PIDs (operator spot-kill; the exercise harness)
  [string]$LivenessPath = '',# default: <workspace>/org/mcp/liveness.json beside this script's .tools/
  [switch]$Json
)

$ErrorActionPreference = 'Stop'

# ---- one process snapshot (PID, PPID, Name, CommandLine, WorkingSetSize, CreationDate) ----
$all = Get-CimInstance Win32_Process
$byId = @{}
foreach ($p in $all) { $byId[[int]$p.ProcessId] = $p }

function MB($bytes) { if ($bytes) { [math]::Round($bytes/1MB,0) } else { 0 } }

# ---- live-claude descendant closure (protected by session-ancestry) --------
$claudePids = @($all | Where-Object { $_.Name -match 'claude' } | ForEach-Object { [int]$_.ProcessId })
$protectedTree = New-Object System.Collections.Generic.HashSet[int]
$queue = New-Object System.Collections.Generic.Queue[int]
foreach ($c in $claudePids) { [void]$protectedTree.Add($c); $queue.Enqueue($c) }
while ($queue.Count -gt 0) {
  $cur = $queue.Dequeue()
  foreach ($p in $all) {
    if ([int]$p.ParentProcessId -eq $cur) {
      $kid = [int]$p.ProcessId
      if ($protectedTree.Add($kid)) { $queue.Enqueue($kid) }
    }
  }
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
$inFlightCmd = 'safe-(commit|merge|deploy|apply)\.sh|commit-worker\.sh|commit-gate\.sh|terraform'

# ---- owner liveness: serial -> live MCP server pid (liveness.json, pid confirmed as a server.py) ----
if (-not $LivenessPath) { $LivenessPath = Join-Path (Split-Path -Parent $PSScriptRoot) 'org\mcp\liveness.json' }
$liveSerials = $null   # $null = UNREADABLE: no owner verdict, so no ORPHANED target this run (fail closed)
try {
  $lj = Get-Content $LivenessPath -Raw -ErrorAction Stop | ConvertFrom-Json
  $liveSerials = @{}
  foreach ($e in $lj.PSObject.Properties) {
    $lp = 0
    try { $lp = [int]$e.Value.pid } catch { $lp = 0 }
    if ($lp -gt 0 -and $byId.ContainsKey($lp) -and $byId[$lp].CommandLine -match 'server\.py') { $liveSerials[$e.Name] = $lp }
  }
} catch {
  [Console]::Error.WriteLine(("WARN: liveness unreadable ({0}) -- ORPHANED class disabled this run" -f $LivenessPath))
}

function Get-Descendants([int]$root) {
  $seen = New-Object System.Collections.Generic.HashSet[int]
  $q = New-Object System.Collections.Generic.Queue[int]
  $q.Enqueue($root)
  while ($q.Count -gt 0) {
    $cur = $q.Dequeue()
    foreach ($p in $all) {
      if ([int]$p.ParentProcessId -eq $cur -and [int]$p.ProcessId -ne $root) {
        $kid = [int]$p.ProcessId
        if ($seen.Add($kid)) { $q.Enqueue($kid) }
      }
    }
  }
  return ,$seen
}

# ---- HARD DENY: never kill, in any mode, even if a pattern over-matches -----
$denyName = '^(System|Idle|Registry|csrss|wininit|winlogon|services|lsass|smss|' +
            'fontdrvhost|dwm|explorer|conhost|OpenConsole|WindowsTerminal|wt|' +
            'powershell|pwsh|WerFault|sihost|ctfmon|RuntimeBroker|taskhostw|' +
            'svchost|spoolsv|dllhost|claude|SearchHost|StartMenuExperienceHost)(\.exe)?$'
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
  foreach ($p in $all) {
    if ($p.Name -notmatch '^(bash|python|pythonw|py|typeperf|awk|gawk|tail|timeout)\.exe$') { continue }
    $procId = [int]$p.ProcessId
    if (Is-Denied $p) { continue }
    if ($protectedTree.Contains($procId)) { continue }                       # live-claude descendant
    $cmd = ''
    if ($p.CommandLine) { $cmd = $p.CommandLine }
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

if ($Json) {
  [PSCustomObject]@{
    mode=$Mode; execute=[bool]$Execute; count=$targets.Count; reclaim_mb=$totalMB;
    targets=$targets; kept=$kept
  } | ConvertTo-Json -Depth 5
  if (-not $Execute) { return }
}

$modeLabel = $Mode.ToUpper()
if ($Execute) { $banner = "EXECUTE" } else { $banner = "DRY-RUN (nothing killed)" }
Write-Output "=== /kill $modeLabel -- $banner ==="
Write-Output ("protected: {0} live-claude-tree PIDs + comms-infra (server/broker/consumer never; watcher/poller/agentbus watch by owner) + in-flight safe-*/terraform + drain-* worktrees + hard-deny system/EDR" -f $protectedTree.Count)
if ($liveSerials -ne $null) { $nLive = $liveSerials.Count } else { $nLive = 'UNREADABLE' }
Write-Output ("owners: {0} serial(s) with a live MCP server in {1}; Monitor cap {2}s" -f $nLive, $LivenessPath, $MonitorCapSeconds)
if ($kept.Count -gt 0) {
  Write-Output ""
  Write-Output "--- owner-keyed infra KEPT (owner live; newest copy) ---"
  $kept | Sort-Object Kind, Owner | ForEach-Object {
    Write-Output ("  KEEP PID {0,-6} {1,-15} {2}  (copies={3})" -f $_.Id, $_.Kind, $_.Owner, $_.Copies)
  }
}

if ($targets.Count -eq 0) {
  Write-Output ""
  Write-Output "OK: no kill targets found. Nothing to do."
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
  # a tree stop must never reach a claude session
  $desc = Get-Descendants $t.Id
  $claudeBelow = $false
  foreach ($d in $desc) { if ($byId.ContainsKey($d) -and $byId[$d].Name -match 'claude') { $claudeBelow = $true } }
  if ($claudeBelow) {
    Write-Output ("  SKIP: PID {0,-6} {1,-22} has a claude process beneath it" -f $t.Id, $t.Name)
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
  $prevEap = $ErrorActionPreference; $ErrorActionPreference = 'Continue'
  $tkOut = (& taskkill.exe /T /F /PID $t.Id 2>&1 | Out-String).Trim()
  $tkRc = $LASTEXITCODE
  $ErrorActionPreference = $prevEap
  if ($tkRc -eq 0) {
    $killed++; $freed += $t.MB
    Write-Output ("  OK:   stopped tree PID {0,-6} {1,-22} (+{2} descendant(s), {3}MB)" -f $t.Id, $t.Name, $desc.Count, $t.MB)
  } elseif (-not (Get-Process -Id $t.Id -ErrorAction SilentlyContinue)) {
    Write-Output ("  SKIP: PID {0,-6} {1,-22} already exited" -f $t.Id, $t.Name)
  } else {
    $failed++
    Write-Output ("  WARN: could not stop tree PID {0,-6} {1,-22} -- rc={2} {3}" -f $t.Id, $t.Name, $tkRc, $tkOut)
  }
}
Write-Output ""
Write-Output ("DONE: killed {0}, failed {1}, ~{2}MB reclaimed." -f $killed, $failed, $freed)

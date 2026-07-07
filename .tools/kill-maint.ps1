<#
  kill-maint.ps1 -- engine for the /kill maintenance skill.

  Two modes clear recurring cruft WITHOUT ever touching a live Claude agent
  session or the fabric comms infra:

    scripts : orphan bash.exe / python.exe / py.exe NOT tied to a live claude
              session and NOT fabric comms infra (server.py / broker.py /
              agent-poller.py / inbox-watch.sh). These are leftover gold runs,
              dead watchers, abandoned diagnostics -- the memory-pressure class.

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
  [switch]$Execute,          # absent = DRY-RUN (default). Present = actually Stop-Process.
  [switch]$IncludeWebView2,  # opt-in: also kill msedgewebview2 (embedded in Search/Outlook; respawns)
  [switch]$IncludeOneDrive,  # opt-in: also kill OneDrive (WARNING: Schwab pipeline delivers via OneDrive)
  [int]$MinAgeSeconds = 60,  # scripts mode: only kill orphans older than this (avoids spawn-race)
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

# ---- fabric comms infra protect (cmdline match; these are DETACHED from claude) ----
# inbox-watch monitors + MCP server + broker + pollers live under org/mcp and are
# parented to Monitor/broker hosts, NOT the claude tree -- must match by cmdline.
$infraCmd = 'org[\\/]mcp[\\/]|inbox-watch\.sh|agent-poller\.py|broker\.py|[\\/]server\.py'

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

# ============================ SCRIPTS MODE ==================================
if ($Mode -eq 'scripts' -or $Mode -eq 'all') {
  $now = Get-Date
  foreach ($p in $all) {
    if ($p.Name -notmatch '^(bash|python|pythonw|py)\.exe$') { continue }
    $procId = [int]$p.ProcessId
    if (Is-Denied $p) { continue }
    if ($protectedTree.Contains($procId)) { continue }                       # live-claude descendant
    if ($p.CommandLine -and $p.CommandLine -match $infraCmd) { continue }    # comms infra
    if ($p.CommandLine -and $p.CommandLine -match '\.claude[\\/]shell-snapshots') { continue } # Bash-tool shell
    # age guard: skip very young procs (parent link may not have resolved yet)
    $age = $null
    if ($p.CreationDate) { $age = ($now - $p.CreationDate).TotalSeconds }
    if ($age -ne $null -and $age -lt $MinAgeSeconds) { continue }
    $cl = ''
    if ($p.CommandLine) { $cl = ($p.CommandLine -replace '\s+',' ') }
    $targets.Add([PSCustomObject]@{
      Category = 'script'
      Id       = $procId
      Name     = $p.Name
      MB       = MB $p.WorkingSetSize
      AgeSec   = if ($age -ne $null) { [math]::Round($age,0) } else { 'na' }
      Reason   = 'orphan bash/py -- not under a live claude session, not fabric comms infra'
      Cmd      = $cl.Substring(0,[Math]::Min(120,$cl.Length))
    })
  }
}

# ============================== APPS MODE ===================================
if ($Mode -eq 'apps' -or $Mode -eq 'all') {
  # standalone bloat apps (main + child procs all matched by name):
  $appName = '^(msedge|chrome|chromium|ms-teams|Teams|tailscale|tailscaled|tailscale-ipn|' +
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
$totalMB = ($targets | Measure-Object MB -Sum).Sum
if (-not $totalMB) { $totalMB = 0 }

if ($Json) {
  [PSCustomObject]@{
    mode=$Mode; execute=[bool]$Execute; count=$targets.Count; reclaim_mb=$totalMB;
    targets=$targets
  } | ConvertTo-Json -Depth 5
  if (-not $Execute) { return }
}

$modeLabel = $Mode.ToUpper()
if ($Execute) { $banner = "EXECUTE" } else { $banner = "DRY-RUN (nothing killed)" }
Write-Output "=== /kill $modeLabel -- $banner ==="
Write-Output ("protected: {0} live-claude-tree PIDs + comms-infra (server/broker/poller/inbox-watch) + hard-deny system/EDR" -f $protectedTree.Count)

if ($targets.Count -eq 0) {
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
# kill non-'claude-named' first is moot (denied); order children-last not required with -Force.
foreach ($t in $targets) {
  try {
    Stop-Process -Id $t.Id -Force -ErrorAction Stop
    $killed++; $freed += $t.MB
    Write-Output ("  OK:   killed PID {0,-6} {1,-22} ({2}MB)" -f $t.Id, $t.Name, $t.MB)
  } catch {
    # already gone (child died with parent) is a benign success-ish
    if (-not $byId.ContainsKey($t.Id) -or -not (Get-Process -Id $t.Id -ErrorAction SilentlyContinue)) {
      Write-Output ("  SKIP: PID {0,-6} {1,-22} already exited" -f $t.Id, $t.Name)
    } else {
      $failed++
      Write-Output ("  WARN: could not kill PID {0,-6} {1,-22} -- {2}" -f $t.Id, $t.Name, $_.Exception.Message)
    }
  }
}
Write-Output ""
Write-Output ("DONE: killed {0}, failed {1}, ~{2}MB reclaimed." -f $killed, $failed, $freed)

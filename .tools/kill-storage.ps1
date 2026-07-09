<#
  kill-storage.ps1 -- engine for `/kill storage`.

  Reclaims disk from KNOWN junk-accumulation areas. Unlike the process reaper
  (kill-maint.ps1, a denylist), storage uses an ALLOWLIST: it will ONLY ever
  delete paths that live strictly UNDER a vetted junk root, and only their
  children -- never a root itself, never a repo file, never a live session's
  scratchpad. Recursive deletion is on the CLAUDE.md human-confirmation list, so
  this is DRY-RUN by default and never auto-runs; -Execute is the operator's
  explicit trigger.

  Default set (no flags): claude-scratch + user-temp + win-temp + crash-dumps.
  Opt-in (data-loss or slow-to-rebuild): -Caches -Pycache -RecycleBin -Docker
  (-DockerVolumes). ASCII-only output. PS 5.1 compatible.
#>
param(
  [switch]$Execute,
  [int]$StaleHours   = 2,    # scratchpad: delete session dirs idle longer than this
  [int]$TempAgeDays  = 1,    # temp: delete items older than this
  [switch]$Caches,           # opt-in: pip / bun / npm caches
  [switch]$Pycache,          # opt-in: workspace __pycache__ (WARNING: some .pyc are git-tracked)
  [switch]$WorkspaceScratch, # opt-in: regenerable workspace scratch dirs (.runtmp/.playwright-mcp/...)
  [switch]$RecycleBin,       # opt-in: empty the Recycle Bin
  [switch]$Docker,           # opt-in: docker container/image/builder prune (stopped/dangling only)
  [switch]$DockerVolumes,    # opt-in: ALSO docker volume prune (WARNING: deletes unused volume DATA)
  [switch]$Json
)
$ErrorActionPreference = 'SilentlyContinue'
$now = Get-Date

# -------- path canonicalization + the ALLOWLIST safety gate ------------------
function Canon($p) {
  if (-not $p) { return $null }
  $i = Get-Item -LiteralPath $p -Force -ErrorAction SilentlyContinue
  if ($i) { return $i.FullName.TrimEnd('\') }
  try { return ([System.IO.Path]::GetFullPath($p)).TrimEnd('\') } catch { return $p.TrimEnd('\') }
}
# The ONLY roots anything may be deleted under (workspace handled separately for __pycache__):
$SAFE_ROOTS = @(
  (Canon "$env:LOCALAPPDATA\Temp\claude"),
  (Canon $env:TEMP), (Canon $env:TMP),
  (Canon 'C:\Windows\Temp'),
  (Canon "$env:LOCALAPPDATA\CrashDumps"),
  (Canon "$env:LOCALAPPDATA\pip\Cache"),
  (Canon "$env:USERPROFILE\.bun\install\cache"),
  (Canon "$env:LOCALAPPDATA\npm-cache")
) | Where-Object { $_ } | Select-Object -Unique
$WORKSPACE = Canon 'C:\Users\AndrewBerman\Desktop\ajb_workspace'
$CUR_SESSION = $env:CLAUDE_CODE_SESSION_ID

# Regenerable workspace scratch roots (-WorkspaceScratch). We delete only their CHILDREN,
# never the dir itself: skills reference .runtmp as a scratch path and expect it to exist.
# Enumerated literally + verified git-ignored at run time (see Assert-ScratchRoot) -- the
# enumeration is the allowlist, and an unlisted dir is never reachable.
$WS_SCRATCH_NAMES = @('.runtmp', '.playwright-mcp', '.frontend-dev', '.ruff_cache')

# A dir qualifies as a scratch root only if it is a DIRECT child of the workspace, is in
# the literal allowlist, is not a reparse point, and git confirms it is IGNORED. The
# git check is the belt: if someone ever tracks one of these, we refuse to touch it.
# (This guard is deliberately stronger than -Pycache's, which can delete tracked .pyc.)
function Assert-ScratchRoot($name) {
  if ($WS_SCRATCH_NAMES -notcontains $name) { return $false }
  $p = Canon (Join-Path $WORKSPACE $name)
  if (-not $p -or -not (Test-Path -LiteralPath $p)) { return $false }
  if ((Split-Path $p -Parent) -ne $WORKSPACE) { return $false }          # direct child only
  $it = Get-Item -LiteralPath $p -Force -ErrorAction SilentlyContinue
  if ($it -and ($it.Attributes -band [IO.FileAttributes]::ReparsePoint)) { return $false }
  & git -C $WORKSPACE check-ignore -q -- $name 2>$null                    # 0 = ignored
  $ignored = ($LASTEXITCODE -eq 0)
  $global:LASTEXITCODE = 0            # don't leak git's rc -- it makes a clean dry-run look failed
  if (-not $ignored) { return $false }                                    # tracked/unignored -> refuse
  return $true
}

# A target is deletable only if it is a STRICT descendant of a safe root (not the
# root itself) and is not a reparse point (junction/symlink that could redirect).
function Assert-Deletable($fullPath, [switch]$AllowWorkspacePycache, [switch]$AllowWorkspaceScratch) {
  $c = Canon $fullPath
  if (-not $c) { return $false }
  $item = Get-Item -LiteralPath $c -Force -ErrorAction SilentlyContinue
  if ($item -and ($item.Attributes -band [IO.FileAttributes]::ReparsePoint)) { return $false } # junction/symlink
  foreach ($r in $SAFE_ROOTS) {
    if ($c.Length -gt $r.Length -and $c.ToLower().StartsWith(($r.ToLower() + '\'))) { return $true }
  }
  if ($AllowWorkspacePycache) {
    # workspace deletes are permitted ONLY for a dir literally named __pycache__ under the repo
    if ($c.Length -gt $WORKSPACE.Length -and $c.ToLower().StartsWith(($WORKSPACE.ToLower()+'\')) `
        -and (Split-Path $c -Leaf) -eq '__pycache__') { return $true }
  }
  if ($AllowWorkspaceScratch) {
    # permitted ONLY for STRICT descendants of an allowlisted, git-ignored scratch root
    foreach ($n in $WS_SCRATCH_NAMES) {
      $r = Canon (Join-Path $WORKSPACE $n)
      if (-not $r) { continue }
      if ($c.Length -gt $r.Length -and $c.ToLower().StartsWith(($r.ToLower()+'\'))) { return $true }
    }
  }
  return $false
}

$targets = New-Object System.Collections.Generic.List[object]
$dockerOps = New-Object System.Collections.Generic.List[object]

function Size-Of($path) {
  $s = (Get-ChildItem -LiteralPath $path -Recurse -File -Force -ErrorAction SilentlyContinue | Measure-Object Length -Sum).Sum
  if ($s) { [math]::Round($s/1MB,1) } else { 0 }
}
function Add-Target($path, $cat, $reason, [switch]$WsPycache, [switch]$WsScratch) {
  if (-not (Assert-Deletable $path -AllowWorkspacePycache:$WsPycache -AllowWorkspaceScratch:$WsScratch)) { return } # HARD gate
  $targets.Add([PSCustomObject]@{ Category=$cat; Path=$path; MB=(Size-Of $path); Reason=$reason })
}

# ============================ CATEGORIES ====================================

# 1. claude scratchpad -- dead session dirs (protect current + anything <StaleHours idle)
$scratch = Canon "$env:LOCALAPPDATA\Temp\claude"
if ($scratch -and (Test-Path $scratch)) {
  Get-ChildItem $scratch -Recurse -Directory -Force -ErrorAction SilentlyContinue |
    Where-Object { $_.Name -match '^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-' } | ForEach-Object {
      $d = $_
      if ($d.Name -eq $CUR_SESSION) { return }                                 # never the current session
      if (($now - $d.LastWriteTime).TotalHours -le $StaleHours) { return }      # protect active sessions
      Add-Target $d.FullName 'claude-scratch' ("dead session dir, idle {0}h" -f [math]::Round(($now-$d.LastWriteTime).TotalHours,0))
    }
}

# 2. user temp + 3. windows temp -- top-level items older than TempAgeDays.
#    EXCLUDE the 'claude' subdir (handled by category 1 with its own protection).
foreach ($t in @((Canon $env:TEMP), (Canon 'C:\Windows\Temp'))) {
  if (-not $t -or -not (Test-Path $t)) { continue }
  $label = if ($t -like '*Windows*') { 'win-temp' } else { 'user-temp' }
  Get-ChildItem $t -Force -ErrorAction SilentlyContinue | ForEach-Object {
    if ($_.FullName -eq $scratch) { return }                                    # never the claude scratch root
    if (($now - $_.LastWriteTime).TotalDays -lt $TempAgeDays) { return }        # only aged items
    Add-Target $_.FullName $label ("temp item older than {0}d" -f $TempAgeDays)
  }
}

# 4. crash dumps
$cd = Canon "$env:LOCALAPPDATA\CrashDumps"
if ($cd -and (Test-Path $cd)) {
  Get-ChildItem $cd -Force -ErrorAction SilentlyContinue | ForEach-Object { Add-Target $_.FullName 'crash-dumps' 'crash dump' }
}

# 5. caches (opt-in)
if ($Caches) {
  foreach ($pair in @(@('pip',"$env:LOCALAPPDATA\pip\Cache"), @('bun',"$env:USERPROFILE\.bun\install\cache"), @('npm',"$env:LOCALAPPDATA\npm-cache"))) {
    $cp = Canon $pair[1]
    if ($cp -and (Test-Path $cp)) {
      Get-ChildItem $cp -Force -ErrorAction SilentlyContinue | ForEach-Object { Add-Target $_.FullName ("cache-"+$pair[0]) 'package cache (regenerable)' }
    }
  }
}

# 6. workspace __pycache__ (opt-in; WARNING some .pyc are git-tracked -> repo deletions)
if ($Pycache) {
  Get-ChildItem $WORKSPACE -Recurse -Directory -Filter '__pycache__' -Force -ErrorAction SilentlyContinue | ForEach-Object {
    Add-Target $_.FullName 'pycache' 'workspace __pycache__ (may include tracked .pyc)' -WsPycache
  }
}

# 6b. workspace scratch dirs (opt-in). Children only -- the dir itself survives, because
#     .claude/skills/{cloud-ops,deck-gen,find,prod-deploy} reference .runtmp as a scratch path.
#     Each root must be allowlisted by literal name AND confirmed git-ignored (Assert-ScratchRoot).
if ($WorkspaceScratch) {
  foreach ($n in $WS_SCRATCH_NAMES) {
    if (-not (Assert-ScratchRoot $n)) {
      Write-Output ("  SKIP scratch root '{0}': absent, tracked, not git-ignored, or a reparse point" -f $n)
      continue
    }
    $root = Canon (Join-Path $WORKSPACE $n)
    Get-ChildItem -LiteralPath $root -Force -ErrorAction SilentlyContinue | ForEach-Object {
      Add-Target $_.FullName ('ws-scratch/'+$n) 'regenerable workspace scratch (dir itself preserved)' -WsScratch
    }
  }
}

# 7. docker (opt-in) -- prune only STOPPED containers / DANGLING images / build cache.
#    Running containers (e.g. ka_testing runtime) are NOT touched by these prunes.
if ($Docker) {
  if (-not (Get-Command docker -ErrorAction SilentlyContinue)) {
    $dockerOps.Add(@{ desc='docker not on PATH -- skipped'; cmd=$null })
  } else {
    docker info 2>&1 | Out-Null                          # daemon-liveness probe (CLI-present != daemon-up)
    if ($LASTEXITCODE -ne 0) {
      $dockerOps.Add(@{ desc='docker CLI present but daemon NOT running -- skipped (start Docker Desktop first)'; cmd=$null })
    } else {
      $dockerOps.Add(@{ desc='stopped containers'; cmd=@('container','prune','-f') })
      $dockerOps.Add(@{ desc='dangling images';    cmd=@('image','prune','-f') })
      $dockerOps.Add(@{ desc='build cache';         cmd=@('builder','prune','-f') })
      if ($DockerVolumes) { $dockerOps.Add(@{ desc='UNUSED VOLUMES (data loss)'; cmd=@('volume','prune','-f') }) }
    }
  }
}

# ============================== REPORT ======================================
$totalMB = ($targets | Measure-Object MB -Sum).Sum; if (-not $totalMB) { $totalMB = 0 }
if ($Execute) { $banner = 'EXECUTE (deleting)' } else { $banner = 'DRY-RUN (nothing deleted)' }
Write-Output "=== /kill STORAGE -- $banner ==="
Write-Output ("safe-roots: {0} allowlisted junk roots | current session {1} protected | scratchpad stale-gate {2}h | temp-age {3}d" -f $SAFE_ROOTS.Count, $CUR_SESSION, $StaleHours, $TempAgeDays)

if ($targets.Count -eq 0 -and $dockerOps.Count -eq 0) { Write-Output "OK: nothing to reclaim."; return }

Write-Output ""
Write-Output "--- by category ---"
$targets | Group-Object Category | Sort-Object { ($_.Group | Measure-Object MB -Sum).Sum } -Descending | ForEach-Object {
  Write-Output ("  {0,-16} {1,4} item(s)  {2,8} MB" -f $_.Name, $_.Count, [math]::Round((($_.Group|Measure-Object MB -Sum).Sum),0))
}
Write-Output ("  {0,-16}          {1,8} MB reclaimable" -f 'TOTAL', [math]::Round($totalMB,0))
if ($Docker) {
  Write-Output ""
  Write-Output "--- docker (run `docker system df` for reclaimable) ---"
  foreach ($op in $dockerOps) { if ($op.cmd) { Write-Output ("  docker {0}   [{1}]" -f ($op.cmd -join ' '), $op.desc) } else { Write-Output ("  {0}" -f $op.desc) } }
}

if (-not $Execute) {
  Write-Output ""
  Write-Output "DRY-RUN: re-run with -Execute (skill: '/kill storage go') to delete. Recursive deletion -- review the categories above first."
  if ($Json) { [PSCustomObject]@{ mode='storage'; reclaim_mb=$totalMB; count=$targets.Count; categories=($targets|Group-Object Category|%{@{cat=$_.Name;mb=(($_.Group|Measure-Object MB -Sum).Sum)}}) } | ConvertTo-Json -Depth 5 }
  return
}

# ----------------------------- DELETE ---------------------------------------
Write-Output ""
Write-Output "--- deleting ---"
$freed = 0; $del = 0; $skip = 0
foreach ($t in $targets) {
  if (-not (Assert-Deletable $t.Path -AllowWorkspacePycache:($t.Category -eq 'pycache') -AllowWorkspaceScratch:($t.Category -like 'ws-scratch/*'))) { $skip++; Write-Output ("  SKIP: {0} failed re-validation" -f $t.Path); continue } # re-assert at delete time
  try {
    Remove-Item -LiteralPath $t.Path -Recurse -Force -ErrorAction Stop
    $del++; $freed += $t.MB
  } catch {
    $skip++; Write-Output ("  SKIP: {0} ({1})" -f $t.Path, $_.Exception.Message.Split([Environment]::NewLine)[0])
  }
}
Write-Output ("FILES: deleted {0}, skipped {1} (locked/in-use), ~{2} MB reclaimed." -f $del, $skip, [math]::Round($freed,0))

if ($Docker) {
  Write-Output ""
  Write-Output "--- docker prune ---"
  foreach ($op in $dockerOps) {
    if (-not $op.cmd) { Write-Output ("  {0}" -f $op.desc); continue }
    Write-Output ("  docker {0} [{1}] ..." -f ($op.cmd -join ' '), $op.desc)
    & docker @($op.cmd) 2>&1 | Select-Object -Last 2 | ForEach-Object { Write-Output ("    {0}" -f $_) }
  }
}
Write-Output ""
Write-Output "DONE."

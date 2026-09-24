# cleanup-disk.ps1 -- /cleanup skill engine (Andrew-direct 2026-09-17, "We need a skill called
# /cleanup that identifies these recurrent storage pools and remediates them, which is usually
# just deleting them. The only one that requires more review is the active worktrees, and policy
# surrounding their deletion.")
#
# Built from a live incident, 2026-09-17: disk was at 5.02 GB free / 97.9% used on a 237 GB
# volume. ~14 GB was reclaimed by hand in three passes -- fully-merged git worktrees, orphaned
# worktree-directory husks, and leftover Terraform provider extraction files -- before this
# script existed. Everything below is that same process, made repeatable.
#
# POOLS (registry -- add a new pool here as the next recurring bloat class is found; do not grow
# an existing pool's identify logic to cover an unrelated class):
#
#   terraform-provider-temp   AUTO-DELETE   AppData\Local\Temp\terraform-provider* leftover FILES
#                                            (not directories -- confirmed by attribute, 2026-09-17).
#                                            Every `terraform` invocation (incl. safe-apply.sh) that
#                                            does not exit perfectly clean leaves one behind; ~149 MB
#                                            each; 53 of them were 5.92 GB on this box alone.
#
#   terraform-provider-cache  AUTO-DELETE   `.terraform/providers` directories under a NON-LIVE linked
#                                            worktree's infra/aws/terraform tree. `terraform init`
#                                            writes one full copy of the AWS provider (686 MB at
#                                            v5.100.0) PER ROOT PER WORKTREE with no shared plugin
#                                            cache -- 10 roots = 6.71 GB per worktree. Measured
#                                            2026-09-20: 28 such dirs in four idle worktrees were
#                                            18.78 GB and took this box to 0 bytes free mid-round.
#                                            Re-creatable by `terraform init` from the committed
#                                            lock file; NO state, planfile or scratch is touched.
#                                            The main checkout and any LIVE worktree are skipped.
#
#   orphaned-worktree-dirs    AUTO-DELETE   directories that SIT INSIDE a known worktree-staging
#                                            root (wherever `git worktree list` currently has
#                                            entries, plus .worktrees/ and C:\tmp as defaults) but
#                                            that `git worktree list` does NOT know about -- i.e.
#                                            already `rm -rf`'d by hand without `git worktree
#                                            remove`, or a create that never finished. No git claim
#                                            exists on these; there is nothing to lose. Still listed
#                                            (name + byte count) before deletion, not silent, in
#                                            case something was deliberately parked outside git's
#                                            view -- this has never happened, but the check is free.
#
#   merged-worktrees          AUTO-DELETE   REGISTERED worktrees, excluded from the LIVE set below,
#                                            whose HEAD is an ancestor of origin/CLOUD (the one trunk
#                                            since 2026-09-24). Zero commits at risk -- the merge already
#                                            carries every byte of it. Removed via `git worktree
#                                            remove` (never raw rm, so git's own admin/ bookkeeping
#                                            stays consistent) and the branch is deleted with it.
#
#   unmerged-worktrees        REVIEW ONLY   REGISTERED worktrees, excluded from LIVE, carrying at
#                                            least one commit absent from origin/CLOUD (the one trunk
#                                            since 2026-09-24). THIS IS THE POOL ANDREW NAMED: the local
#                                            worktree is the ONLY copy of that commit's content, so
#                                            THIS SCRIPT NEVER DELETES HERE. It prints the full list
#                                            (path, branch, commits ahead, size, last-write) and
#                                            stops. Disposal policy is a content question -- is each
#                                            unlanded commit's SUBSTANCE already on HEAD by some
#                                            other route (superseded, safe) or not (unique, never
#                                            delete without its project owner) -- and that needs a
#                                            content diff, not a file-age heuristic, which is exactly
#                                            what the /cleanup skill routes to 3.0.0_SA_CVO. See
#                                            .claude/skills/cleanup/SKILL.md "The worktree policy."
#
# THE LIVE-WORKTREE DEFINITION -- the one thing every pool above must get right, because it is the
# entire difference between routine hygiene and destroying an in-progress worker's only checkout:
# a worktree is LIVE, and no pool above may touch it, if EITHER:
#   (a) its own most-recent file write is within -LiveWindowHours (default 6) of NOW, or
#   (b) its path is named in -ExcludePath (belt-and-suspenders for a known long-running job).
# (a) is a heuristic, not a certainty -- a worker that has been silently stuck for 7 hours would
# read as non-live. That is the SAFE direction for a heuristic to be wrong in: it can delay
# cleanup of something that is actually dead, never delete something that is actually alive faster
# than 6 hours. Narrow the window only with real evidence a round's cadence is faster than that.
#
# Usage:
#   cleanup-disk.ps1                          # scan + auto-remediate the safe pools; list+stop on the review pool
#   cleanup-disk.ps1 -DryRun                  # scan + report every pool, delete nothing anywhere
#   cleanup-disk.ps1 -Pool <name>              # run exactly one registered pool (comma-separated for >1)
#   cleanup-disk.ps1 -LiveWindowHours <n>      # override the live-worktree recency window (default 6)
#   cleanup-disk.ps1 -ExcludePath <path>       # repeatable; a path (worktree or Temp-pool item) never touched
#   cleanup-disk.ps1 -RepoRoot <path>          # default: derived from this script's own location

[CmdletBinding()]
param(
    [switch]$DryRun,
    [string[]]$Pool = @('terraform-provider-temp', 'terraform-provider-cache', 'orphaned-worktree-dirs', 'merged-worktrees', 'unmerged-worktrees'),
    [int]$LiveWindowHours = 6,
    [string[]]$ExcludePath = @(),
    [string]$RepoRoot = $(Split-Path -Parent $PSScriptRoot)
)

$ErrorActionPreference = 'Stop'
Push-Location $RepoRoot
try {

$_excludeNorm = $ExcludePath | ForEach-Object { $_.Replace('\', '/').TrimEnd('/').ToLowerInvariant() }
$_liveCutoff = (Get-Date).AddHours(-$LiveWindowHours)

function Test-Excluded([string]$Path) {
    $n = $Path.Replace('\', '/').TrimEnd('/').ToLowerInvariant()
    return $_excludeNorm -contains $n
}

function Get-DirSizeBytes([string]$Path) {
    $sum = (Get-ChildItem -LiteralPath $Path -Recurse -Force -ErrorAction SilentlyContinue |
        Measure-Object -Property Length -Sum -ErrorAction SilentlyContinue).Sum
    if ($null -eq $sum) { return 0 }
    return $sum
}

function Format-GB([double]$Bytes) { "{0:N2} GB" -f ($Bytes / 1GB) }

# --- shared: the registered-worktree table, read ONCE, everything below keys off it -------------
function Get-WorktreeTable {
    $porcelain = & git worktree list --porcelain 2>$null
    $rows = @()
    $wt = $null
    foreach ($line in $porcelain) {
        if ($line -match '^worktree (.+)$') { $wt = $Matches[1] }
        elseif ($line -match '^branch (.+)$' -and $wt) {
            $rows += [PSCustomObject]@{ Path = $wt; Branch = $Matches[1]; Detached = $false }
            $wt = $null
        }
        elseif ($line -eq 'detached' -and $wt) {
            $rows += [PSCustomObject]@{ Path = $wt; Branch = '(detached)'; Detached = $true }
            $wt = $null
        }
    }
    return $rows
}

function Test-WorktreeLive([string]$Path) {
    if (Test-Excluded $Path) { return $true }
    if (-not (Test-Path -LiteralPath $Path)) { return $false }
    try {
        $newest = (Get-ChildItem -LiteralPath $Path -Recurse -Force -ErrorAction SilentlyContinue |
            Sort-Object LastWriteTime -Descending | Select-Object -First 1).LastWriteTime
        if (-not $newest) { $newest = (Get-Item -LiteralPath $Path -Force).LastWriteTime }
        return $newest -ge $_liveCutoff
    } catch { return $true }   # can't read it -> treat as live, the safe direction
}

# =================================================================================================
# POOL: terraform-provider-temp
# =================================================================================================
function Invoke-PoolTerraformTemp {
    $temp = Join-Path $env:LOCALAPPDATA 'Temp'
    if (-not (Test-Path $temp)) { Write-Output "[terraform-provider-temp] $temp does not exist -- skip"; return }
    $items = Get-ChildItem -LiteralPath $temp -Force -ErrorAction SilentlyContinue |
        Where-Object { $_.Name -like 'terraform-provider*' -and -not (Test-Excluded $_.FullName) }
    $totalBytes = 0
    foreach ($f in $items) { $totalBytes += $(if ($f.PSIsContainer) { Get-DirSizeBytes $f.FullName } else { $f.Length }) }
    Write-Output ("[terraform-provider-temp] found {0} item(s), {1}" -f $items.Count, (Format-GB $totalBytes))
    if ($items.Count -eq 0) { return }
    if ($DryRun) { Write-Output "[terraform-provider-temp] DRY RUN -- would delete all of the above"; return }
    $removed = 0; $skipped = 0
    foreach ($f in $items) {
        try { Remove-Item -LiteralPath $f.FullName -Recurse -Force -ErrorAction Stop; $removed++ }
        catch { $skipped++; Write-Output ("[terraform-provider-temp] SKIPPED (in use): {0} -- {1}" -f $f.Name, $_.Exception.Message) }
    }
    Write-Output ("[terraform-provider-temp] removed {0}, skipped {1} (locked by a live process)" -f $removed, $skipped)
}

# =================================================================================================
# POOL: terraform-provider-cache
# =================================================================================================
function Invoke-PoolTerraformProviderCache {
    $mainRoot = (& git rev-parse --show-toplevel 2>$null)
    if ($mainRoot) { $mainRoot = $mainRoot.Replace('\', '/').TrimEnd('/').ToLowerInvariant() }
    $targets = @(); $liveSkipped = 0; $totalBytes = 0
    foreach ($row in (Get-WorktreeTable)) {
        $norm = $row.Path.Replace('\', '/').TrimEnd('/').ToLowerInvariant()
        if ($norm -eq $mainRoot) { continue }                      # the shared checkout is never touched
        $tfRoot = Join-Path $row.Path 'infra/aws/terraform'
        if (-not (Test-Path -LiteralPath $tfRoot)) { continue }
        $dirs = @(Get-ChildItem -LiteralPath $tfRoot -Recurse -Directory -Force -Filter '.terraform' -ErrorAction SilentlyContinue |
            ForEach-Object { Join-Path $_.FullName 'providers' } | Where-Object { Test-Path -LiteralPath $_ })
        if ($dirs.Count -eq 0) { continue }
        if (Test-WorktreeLive $row.Path) {
            $liveSkipped++
            Write-Output ("[terraform-provider-cache] LIVE (written inside the {0}h window) -- untouched: {1}  ({2} provider dir(s))" -f $LiveWindowHours, $row.Path, $dirs.Count)
            continue
        }
        $bytes = 0; foreach ($d in $dirs) { $bytes += Get-DirSizeBytes $d }
        $totalBytes += $bytes
        $targets += [PSCustomObject]@{ Path = $row.Path; Dirs = $dirs; Bytes = $bytes }
    }
    $dirCount = 0; foreach ($x in $targets) { $dirCount += $x.Dirs.Count }
    Write-Output ("[terraform-provider-cache] found {0} provider dir(s) in {1} non-live worktree(s), {2}; {3} live worktree(s) skipped" -f $dirCount, $targets.Count, (Format-GB $totalBytes), $liveSkipped)
    foreach ($x in $targets) { Write-Output ("   {0,10}   {1,2} dir(s)   {2}" -f (Format-GB $x.Bytes), $x.Dirs.Count, $x.Path) }
    if ($targets.Count -eq 0) { return }
    if ($DryRun) { Write-Output "[terraform-provider-cache] DRY RUN -- would delete the provider dirs above (terraform init restores them)"; return }
    $removed = 0; $skipped = 0
    foreach ($x in $targets) { foreach ($d in $x.Dirs) {
        try { Remove-Item -LiteralPath $d -Recurse -Force -ErrorAction Stop; $removed++ }
        catch { $skipped++; Write-Output ("[terraform-provider-cache] SKIPPED (in use): {0} -- {1}" -f $d, $_.Exception.Message) }
    } }
    Write-Output ("[terraform-provider-cache] removed {0}, skipped {1} (locked by a live process)" -f $removed, $skipped)
}

# =================================================================================================
# POOL: orphaned-worktree-dirs
# =================================================================================================
function Invoke-PoolOrphanedDirs {
    # ROOT DISCOVERY IS THE ONE DANGEROUS PART OF THIS POOL. A stray worktree living directly in a
    # general-purpose folder (e.g. someone ran `git worktree add` straight into Desktop) must NEVER
    # promote that folder to a "root" this pool scans -- every OTHER unrelated thing sitting beside
    # it (personal files, other projects) would then read as an "orphan" and be listed for deletion.
    # Caught live on 2026-09-17: a stray worktree at Desktop\scty-build made Desktop itself a
    # candidate root, and Desktop\OPAL_WORLD_MODEL, Desktop\ADVI_REFACTOR and several transcript
    # folders were about to print as orphaned-and-deletable. Never shipped past -DryRun.
    #
    # So a directory only counts as a worktree-staging ROOT if it hosts 2+ registered worktrees
    # (a genuine pool, like .worktrees/ or C:\tmp) -- a parent with exactly one worktree in it is a
    # one-off, not a pool, and is never scanned. On top of that, a fixed denylist of personal/
    # profile-root directories is NEVER treated as a root regardless of what lives inside it.
    $wt = Get-WorktreeTable
    $registeredNorm = $wt.Path | ForEach-Object { $_.Replace('\', '/').TrimEnd('/').ToLowerInvariant() }
    $parentCounts = $wt.Path | ForEach-Object { Split-Path $_ -Parent } | Group-Object
    $roots = @($parentCounts | Where-Object { $_.Count -ge 2 } | ForEach-Object { $_.Name })
    foreach ($fallback in @((Join-Path $RepoRoot '.worktrees'), 'C:\tmp')) {
        if ((Test-Path $fallback) -and ($roots -notcontains $fallback)) { $roots += $fallback }
    }
    $denylist = @(
        $env:USERPROFILE,
        (Join-Path $env:USERPROFILE 'Desktop'),
        (Join-Path $env:USERPROFILE 'Documents'),
        (Join-Path $env:USERPROFILE 'Downloads')
    ) | ForEach-Object { $_.Replace('\', '/').TrimEnd('/').ToLowerInvariant() }
    $roots = @($roots | Where-Object { ($_.Replace('\', '/').TrimEnd('/').ToLowerInvariant()) -notin $denylist })
    $orphans = @()
    foreach ($root in $roots) {
        if (-not (Test-Path $root)) { continue }
        Get-ChildItem -LiteralPath $root -Force -Directory -ErrorAction SilentlyContinue | ForEach-Object {
            $n = $_.FullName.Replace('\', '/').TrimEnd('/').ToLowerInvariant()
            if (($registeredNorm -notcontains $n) -and -not (Test-Excluded $_.FullName)) {
                # The live window binds THIS pool too. Measured 2026-09-18: a dry run listed
                # .worktrees\verify-lt-3-1 for deletion 30 minutes after its last write -- an
                # unregistered directory is not a DEAD one; a seat's scratch checkout looks identical.
                if (Test-WorktreeLive $_.FullName) {
                    Write-Output ("[orphaned-worktree-dirs] LIVE (written inside the {0}h window) -- untouched: {1}" -f $LiveWindowHours, $_.FullName)
                } else { $orphans += $_ }
            }
        }
    }
    $totalBytes = 0
    foreach ($o in $orphans) { $totalBytes += (Get-DirSizeBytes $o.FullName) }
    Write-Output ("[orphaned-worktree-dirs] found {0} unregistered dir(s) under {1} root(s), {2}" -f $orphans.Count, $roots.Count, (Format-GB $totalBytes))
    foreach ($o in $orphans) {
        $sz = Get-DirSizeBytes $o.FullName
        Write-Output ("  {0,10}  {1}  (modified {2})" -f (Format-GB $sz), $o.FullName, $o.LastWriteTime)
    }
    if ($orphans.Count -eq 0) { return }
    if ($DryRun) { Write-Output "[orphaned-worktree-dirs] DRY RUN -- would delete all of the above, then git worktree prune"; return }
    foreach ($o in $orphans) { Remove-Item -LiteralPath $o.FullName -Recurse -Force -ErrorAction SilentlyContinue }
    & git worktree prune 2>$null
    Write-Output "[orphaned-worktree-dirs] removed; git worktree prune run"
}

# =================================================================================================
# POOLS: merged-worktrees (AUTO-DELETE) + unmerged-worktrees (REVIEW ONLY)
# Split from ONE pass over the registered table, because both need the same ahead/merged read.
# =================================================================================================
function Invoke-PoolWorktreeSplit([bool]$RunMerged, [bool]$RunUnmerged) {
    # NOTE: this function is called as a bare statement (`Invoke-PoolWorktreeSplit ...`), never
    # `$x = Invoke-PoolWorktreeSplit ...` and never piped -- every Write-Output call below is a
    # PowerShell function's OUTPUT STREAM, same channel as an implicit return. Capturing the call
    # with `$null = ...` (tried once, 2026-09-17) swallows ALL of it, not just a trailing return
    # value -- the fix was removing the `return @{...}` this function used to end with, not the
    # capture. Do not reintroduce either half.
    git fetch origin *> $null
    $wt = Get-WorktreeTable | Where-Object { $_.Path.Replace('\', '/').TrimEnd('/') -ne $RepoRoot.Replace('\', '/').TrimEnd('/') }
    $merged = @(); $unmerged = @(); $live = @(); $gone = @()
    foreach ($row in $wt) {
        # A registered worktree whose directory no longer exists (removed by hand, or by another
        # live seat's own cleanup, without `git worktree remove`) is a GHOST REGISTRATION, not a
        # content question -- there is nothing at $row.Path for `git -C` to read. `git worktree
        # prune` is the correct fix, run once below; this loop must not call `git -C` on it.
        if (-not (Test-Path -LiteralPath $row.Path)) { $gone += $row; continue }
        if (Test-WorktreeLive $row.Path) { $live += $row; continue }
        # ONE TRUNK since 2026-09-24 (Andrew-direct "recs approved", card 1 (a), LD-0613): origin/SITEZ is retired
        # (tip = tag archive/SITEZ-20260924), so "fully merged" means an ancestor of origin/CLOUD alone. The old
        # two-ref AND would read every worktree as unmerged once the second ref is gone.
        & git -C $row.Path merge-base --is-ancestor HEAD origin/CLOUD 2>$null | Out-Null
        $mergedCloud = ($LASTEXITCODE -eq 0)
        $aheadCloud = [int](& git -C $row.Path rev-list --count "origin/CLOUD..HEAD" 2>$null)
        $row | Add-Member -NotePropertyName AheadOfCloud -NotePropertyValue $aheadCloud
        $row | Add-Member -NotePropertyName MergedCloud -NotePropertyValue $mergedCloud
        $row | Add-Member -NotePropertyName SizeBytes -NotePropertyValue (Get-DirSizeBytes $row.Path)
        if ($mergedCloud) { $merged += $row } else { $unmerged += $row }
    }
    if ($gone.Count -gt 0) {
        Write-Output ("[worktree-split] {0} registered worktree(s) whose directory no longer exists -- pruning git's own record, not touched as content" -f $gone.Count)
        foreach ($row in $gone) { Write-Output ("  GONE  {0}  [{1}]" -f $row.Path, $row.Branch) }
        if (-not $DryRun) { & git worktree prune 2>&1 | Out-Null }
    }
    Write-Output ("[worktree-split] {0} live (untouched), {1} fully-merged, {2} carrying unlanded commits" -f $live.Count, $merged.Count, $unmerged.Count)

    if ($RunMerged) {
        $freed = 0
        foreach ($row in $merged) { $freed += $row.SizeBytes }
        Write-Output ("[merged-worktrees] {0} worktree(s), {1}" -f $merged.Count, (Format-GB $freed))
        foreach ($row in $merged) {
            Write-Output ("  {0,10}  {1}  [{2}]" -f (Format-GB $row.SizeBytes), $row.Path, $row.Branch)
            if (-not $DryRun) {
                & git worktree remove --force $row.Path 2>&1 | Out-Null
                $branchName = $row.Branch -replace '^refs/heads/', ''
                & git branch -D $branchName 2>&1 | Out-Null
            }
        }
        if ($DryRun -and $merged.Count -gt 0) { Write-Output "[merged-worktrees] DRY RUN -- would remove all of the above + delete their branches" }
    }

    if ($RunUnmerged) {
        Write-Output "[unmerged-worktrees] REVIEW ONLY -- nothing below is touched by this script:"
        foreach ($row in ($unmerged | Sort-Object AheadOfCloud -Descending)) {
            $branchName = $row.Branch -replace '^refs/heads/', ''
            Write-Output ("  {0,4} ahead   {1,10}   {2}   [{3}]" -f $row.AheadOfCloud, (Format-GB $row.SizeBytes), $row.Path, $branchName)
        }
        if ($unmerged.Count -gt 0) {
            Write-Output ""
            Write-Output "Policy (.claude/skills/cleanup/SKILL.md): each of these is the ONLY copy of its unlanded"
            Write-Output "commit(s). Route to 3.0.0_SA_CVO (or the project's own reviewer) for a per-commit"
            Write-Output "SUPERSEDED-vs-UNIQUE content verdict before anything is deleted. Never auto-remediated."
        }
    }
}

# =================================================================================================
# RUN
# =================================================================================================
$freeBefore = (Get-CimInstance Win32_LogicalDisk -Filter "DeviceID='$($RepoRoot.Substring(0,2))'").FreeSpace
Write-Output ("/cleanup -- free space before: {0}" -f (Format-GB $freeBefore))
Write-Output ("pools: {0}{1}" -f ($Pool -join ', '), $(if ($DryRun) { '  (DRY RUN)' } else { '' }))
Write-Output ""

if ($Pool -contains 'terraform-provider-temp') { Invoke-PoolTerraformTemp; Write-Output "" }
if ($Pool -contains 'terraform-provider-cache') { Invoke-PoolTerraformProviderCache; Write-Output "" }
if ($Pool -contains 'orphaned-worktree-dirs')  { Invoke-PoolOrphanedDirs; Write-Output "" }
$runMerged = $Pool -contains 'merged-worktrees'
$runUnmerged = $Pool -contains 'unmerged-worktrees'
if ($runMerged -or $runUnmerged) { Invoke-PoolWorktreeSplit -RunMerged:$runMerged -RunUnmerged:$runUnmerged; Write-Output "" }

$freeAfter = (Get-CimInstance Win32_LogicalDisk -Filter "DeviceID='$($RepoRoot.Substring(0,2))'").FreeSpace
Write-Output ("/cleanup -- free space after:  {0}  (freed {1})" -f (Format-GB $freeAfter), (Format-GB ($freeAfter - $freeBefore)))

} finally { Pop-Location }

<#
.SYNOPSIS
  Identify and kill orphaned/zombie bash.exe processes left behind by the agent commit storm.

.DESCRIPTION
  A "zombie" bash here = a bash.exe whose parent process no longer exists in the
  process table (true orphan) OR a bash.exe that has consumed no CPU and been
  idle longer than -IdleMinutes.

  Default mode is DRY RUN (list only). Pass -Execute to actually terminate.

.PARAMETER Execute
  Actually kill the matched processes. Without this flag, the script only lists them.

.PARAMETER IdleMinutes
  Treat a bash.exe with 0 recent CPU and start time older than this many minutes
  as a zombie even if its parent is still alive. Default 30.

.PARAMETER IncludeIdle
  Include the "idle but parent alive" category in addition to true orphans.
  Without this flag, ONLY true orphans (dead parent) are targeted - safest mode.

.EXAMPLE
  .\kill-zombie-bash.ps1                       # dry run, true orphans only
  .\kill-zombie-bash.ps1 -IncludeIdle          # dry run, orphans + long-idle
  .\kill-zombie-bash.ps1 -Execute              # kill true orphans
  .\kill-zombie-bash.ps1 -IncludeIdle -Execute # kill orphans + long-idle
#>

[CmdletBinding()]
param(
    [switch]$Execute,
    [int]$IdleMinutes = 30,
    [switch]$IncludeIdle
)

$ErrorActionPreference = 'Stop'

$allBash = Get-CimInstance Win32_Process -Filter "Name='bash.exe'"
if (-not $allBash) {
    Write-Output "No bash.exe processes running. Nothing to do."
    return
}

$allPids = (Get-Process | Select-Object -ExpandProperty Id) | Sort-Object -Unique
$now = Get-Date
$idleThreshold = $now.AddMinutes(-$IdleMinutes)

$orphans = @()
$idle = @()

foreach ($b in $allBash) {
    $proc = $null
    try { $proc = Get-Process -Id $b.ProcessId -ErrorAction Stop } catch { continue }

    $parentAlive = $allPids -contains $b.ParentProcessId
    $startTime = $proc.StartTime
    $cpu = if ($proc.CPU) { [math]::Round($proc.CPU,1) } else { 0 }
    $wsMB = [math]::Round($proc.WorkingSet64/1MB,1)

    $row = [PSCustomObject]@{
        ProcId      = $b.ProcessId
        PPID        = $b.ParentProcessId
        ParentAlive = $parentAlive
        StartTime   = $startTime
        AgeMin      = [math]::Round(($now - $startTime).TotalMinutes,0)
        CPU_s       = $cpu
        WS_MB       = $wsMB
        CmdLine     = if ($b.CommandLine) {
                          $b.CommandLine.Substring(0,[Math]::Min(120,$b.CommandLine.Length))
                      } else { '<unreadable>' }
    }

    if (-not $parentAlive) {
        $orphans += $row
    } elseif ($startTime -lt $idleThreshold -and $cpu -lt 1) {
        $idle += $row
    }
}

$targets = @()
$targets += $orphans
if ($IncludeIdle) { $targets += $idle }

Write-Output ""
Write-Output "=== TRUE ORPHANS (parent PID no longer exists): $($orphans.Count) ==="
if ($orphans) { $orphans | Format-Table -AutoSize -Wrap } else { Write-Output "  none" }

Write-Output ""
$idleHeader = "=== LONG-IDLE (parent alive, age > " + $IdleMinutes + "m, CPU < 1s): " + $idle.Count + " ==="
Write-Output $idleHeader
if ($idle) { $idle | Format-Table -AutoSize -Wrap } else { Write-Output "  none" }

Write-Output ""
Write-Output "Total targets in current mode: $($targets.Count)"
if (-not $IncludeIdle) {
    Write-Output "(orphans only - pass -IncludeIdle to also target long-idle bashes)"
}

if (-not $Execute) {
    Write-Output ""
    Write-Output "DRY RUN. Re-run with -Execute to actually kill the targets above."
    return
}

if ($targets.Count -eq 0) {
    Write-Output "Nothing to kill."
    return
}

Write-Output ""
Write-Output "Executing kills..."
$killed = 0
$failed = 0
foreach ($t in $targets) {
    try {
        Stop-Process -Id $t.ProcId -Force -ErrorAction Stop
        $killed++
        Write-Output "  killed PID $($t.ProcId)"
    } catch {
        $failed++
        Write-Output ("  FAILED PID " + $t.ProcId + ": " + $_.Exception.Message)
    }
}
Write-Output ""
Write-Output "Done. Killed: $killed   Failed: $failed"

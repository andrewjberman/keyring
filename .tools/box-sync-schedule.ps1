# box-sync-schedule.ps1 -- install, inspect or remove the per-box Windows scheduled task that runs .tools/box-sync.sh.
#
# Andrew-direct 2026-10-08 ~20:1xZ, VERBATIM: "I think B is the stable long-term solution." (B = a scheduled task on each
# box, no agent involved). Record: org/tier1_exec/4.0.0_SA_CRO~A/deliverables/ANDREW_DIRECT_20261008_201xZ_BOX_SYNC_SCHEDULED_TASK_B.md
# Owner: 4.0.0_SA_CRO~A. Nothing here is device-specific: the repo root, Git Bash, and the box name are DERIVED (LD-0405).
#
# USAGE (Windows PowerShell 5.1, on the box, as the interactive user whose git credentials push to origin):
#   powershell -NoProfile -File .tools\box-sync-schedule.ps1 -Status
#   powershell -NoProfile -File .tools\box-sync-schedule.ps1 -Install       # registers (or replaces) this box's task
#   powershell -NoProfile -File .tools\box-sync-schedule.ps1 -RunNow        # runs the task once, now
#   powershell -NoProfile -File .tools\box-sync-schedule.ps1 -Uninstall
#
# THE SLOTS -- EVERY 10 MINUTES, the integrator first (Andrew-direct 2026-10-09 ~03:1xZ, "Sure I lik eit", approving
# 4.0.0_SA_CRO~B's recommendation; record org/tier1_exec/4.0.0_SA_CRO~B/deliverables/ANDREW_DIRECT_20261009_031xZ_BOX_SYNC_EVERY_10_MIN.md;
# replaces the 30-minute table of Andrew ~18:0xZ, design section 10). Each cycle: the laptop folds every box into CLOUD, then
# each box takes CLOUD. Worst-case box-to-box lag ~20 minutes (was ~55).
#   laptop  :00 :10 :20 ...  integrate, then its own box pass   serial 0.0.0_AB_MSTR (the one integrator)
#   sitez   :02 :12 :22 ...  box pass                           serial 0.0.0_AB_MSTR~Z
#   dell1   :04 :14 :24 ...  box pass                           serial 0.0.0_AB_MSTR~DELL1
#   dell2   :06 :16 :26 ...  box pass                           serial 0.0.0_AB_MSTR~DELL2
# The task runs only while the user is logged on (Interactive logon), so git uses that user's stored credentials. It
# never starts a second copy while one runs (MultipleInstances IgnoreNew; box-sync's own pass lock is the second
# guard; a slot that meets a running pass is skipped, never overlapped), and it stops a run that passes 25 minutes. Output is appended to <git common dir>\box-sync-task.log; each run's
# outcome is also one BOX-SYNC row in org/git-author-override-audit.log.

param([switch]$Install, [switch]$Uninstall, [switch]$Status, [switch]$RunNow)

$ErrorActionPreference = 'Stop'
$TaskName = 'Opal box-sync'
$Every = 10   # minutes between passes (was 30)
$Slots = @{
  'laptop' = @{ Minute = 0; Serial = '0.0.0_AB_MSTR';       Modes = @('integrate', 'box') }
  'sitez'  = @{ Minute = 2; Serial = '0.0.0_AB_MSTR~Z';     Modes = @('box') }
  'dell1'  = @{ Minute = 4; Serial = '0.0.0_AB_MSTR~DELL1'; Modes = @('box') }
  'dell2'  = @{ Minute = 6; Serial = '0.0.0_AB_MSTR~DELL2'; Modes = @('box') }
}

function Fail($m) { Write-Output "ERROR: $m"; exit 1 }

# --- derive everything
$root = (& git -C $PSScriptRoot rev-parse --show-toplevel 2>$null)
if (-not $root) { Fail "cannot resolve the repo root from $PSScriptRoot" }
$common = (& git -C $root rev-parse --path-format=absolute --git-common-dir 2>$null)
$gitExe = (Get-Command git.exe -ErrorAction SilentlyContinue).Source
if (-not $gitExe) { Fail "git.exe is not on PATH" }
# Walk up from git.exe to the Git root that holds bin\bash.exe. The first git.exe on PATH may be cmd\git.exe,
# bin\git.exe or ucrt64\bin\git.exe (site Z, 2026-10-08: 0.0.0_AB_MSTR~Z, relay RELAY_SITEZ_BOXSYNC_INSTALLER_DEFECT_20261008_2053Z.md),
# so a fixed number of Split-Paths is wrong on some box.
$bash = $null
$dir = Split-Path $gitExe
for ($i = 0; $i -lt 5 -and $dir; $i++) {
  $cand = Join-Path $dir 'bin\bash.exe'
  if (Test-Path $cand) { $bash = $cand; break }
  $dir = Split-Path $dir
}
if (-not $bash) { Fail "Git Bash (bin\bash.exe) not found in any parent of $gitExe" }
$box = $env:AGENTBUS_DEVICE
if (-not $box) { $box = [Environment]::GetEnvironmentVariable('AGENTBUS_DEVICE', 'User') }
if (-not $box) { Fail "AGENTBUS_DEVICE is not set (process or user environment); refusing to guess the box" }
$box = $box.Trim().ToLower()
if (-not $Slots.ContainsKey($box)) { Fail "box '$box' has no slot in the table (known: $($Slots.Keys -join ', '))" }
$slot = $Slots[$box]
$log = Join-Path $common 'box-sync-task.log'

if ($Status -or -not ($Install -or $Uninstall -or $RunNow)) {
  Write-Output "box=$box  minute=:0$($slot.Minute) then every $Every min  serial=$($slot.Serial)  modes=$($slot.Modes -join ' then ')"
  Write-Output "repo=$root  bash=$bash  log=$log"
  $t = Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue
  if ($t) {
    $i = Get-ScheduledTaskInfo -TaskName $TaskName
    Write-Output "task: $($t.State)  last=$($i.LastRunTime) result=$($i.LastTaskResult)  next=$($i.NextRunTime)"
  } else { Write-Output "task: NOT INSTALLED" }
  if (Test-Path $log) { Write-Output "--- last lines of $log"; Get-Content $log -Tail 6 }
  exit 0
}

if ($Uninstall) {
  if (Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue) {
    Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false
    Write-Output "OK: removed task '$TaskName' on box $box"
  } else { Write-Output "SKIP: task '$TaskName' is not installed on box $box" }
  exit 0
}

if ($RunNow) { Start-ScheduledTask -TaskName $TaskName; Write-Output "OK: started '$TaskName' on box $box; read -Status in a minute"; exit 0 }

# --- install: one action runs the box's modes in order, appending to the log
$rootFwd = $root -replace '\\', '/'
$logFwd = $log -replace '\\', '/'
$runs = ($slot.Modes | ForEach-Object { "bash .tools/box-sync.sh $_" }) -join '; '
$cmd = "cd '$rootFwd' && export OPAL_AGENT_SERIAL='$($slot.Serial)' AGENTBUS_DEVICE='$box' && " +
       "{ echo `"=== `$(date -u +%Y-%m-%dT%H:%M:%SZ) box-sync task ($box)`"; $runs; } >> '$logFwd' 2>&1"
$action = New-ScheduledTaskAction -Execute $bash -Argument "-lc `"$($cmd -replace '"', '\"')`""
$now = Get-Date
$first = $now.Date.AddHours($now.Hour).AddMinutes($slot.Minute)
while ($first -le $now) { $first = $first.AddMinutes($Every) }
$trigger = New-ScheduledTaskTrigger -Once -At $first -RepetitionInterval (New-TimeSpan -Minutes $Every) -RepetitionDuration (New-TimeSpan -Days 3650)
$settings = New-ScheduledTaskSettingsSet -MultipleInstances IgnoreNew -ExecutionTimeLimit (New-TimeSpan -Minutes 25) `
  -StartWhenAvailable -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries
$principal = New-ScheduledTaskPrincipal -UserId "$env:USERDOMAIN\$env:USERNAME" -LogonType Interactive -RunLevel Limited
Register-ScheduledTask -TaskName $TaskName -Action $action -Trigger $trigger -Settings $settings -Principal $principal `
  -Description "Runs .tools/box-sync.sh ($($slot.Modes -join ' then ')) for box $box every $Every min from :0$($slot.Minute). Andrew-direct 2026-10-08 ~20:1xZ (option B); 10-minute cycle Andrew-direct 2026-10-09 ~03:1xZ. Owner 4.0.0_SA_CRO~A." -Force | Out-Null
Write-Output "OK: installed '$TaskName' on box ${box} -- first run $first, then every $Every min; serial $($slot.Serial); log $log"

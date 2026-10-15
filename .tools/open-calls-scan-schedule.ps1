# open-calls-scan-schedule.ps1 -- install, inspect or remove the per-box Windows scheduled task that runs
# .tools/open-calls-scan.py every 10 minutes.
#
# Andrew-direct 2026-10-09 ~00:0xZ, VERBATIM (part): "there should be a "notification" function that scans that json per box
# every 10 min and if it has open-calls on it, the CTO on that box has to adjudicate." Record:
# org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261009_000xZ_KEEP_WORK_DRIVING_OPEN_CALL_QUEUE_CROSS_ADJUDICATION_AND_NEXT_CALLS_ON_EMPTY_TICK.md
# Design: org/tier1_exec/4.0.0_SA_CRO~B/deliverables/DESIGN_KEEP_WORK_DRIVING_20261009.md. Owner 4.0.0_SA_CRO~B.
# Nothing here is device-specific: the repo root, python and the box name are DERIVED (LD-0405). Pattern:
# .tools/box-sync-schedule.ps1.
#
# USAGE (Windows PowerShell 5.1, on the box, as the interactive user):
#   powershell -NoProfile -File .tools\open-calls-scan-schedule.ps1 -Status
#   powershell -NoProfile -File .tools\open-calls-scan-schedule.ps1 -Install     # registers (or replaces) this box's task
#   powershell -NoProfile -File .tools\open-calls-scan-schedule.ps1 -RunNow      # runs the task once, now
#   powershell -NoProfile -File .tools\open-calls-scan-schedule.ps1 -Uninstall
#
# THE SLOTS (first minute of each 10-minute cycle; staggered so the boxes do not read S3 in the same second):
#   the n-th box of org/devices/DEVICES.json (register order) at :01, :04, :07, :09 (1 + 3n, capped at 9); today laptop :01
#   sitez :04 dell1 :07 dell2 :09. The table is computed from the register below, not listed here.
# The task runs only while the user is logged on, never starts a second copy while one runs, and stops a run past
# 9 minutes (under the 10-minute cadence; a pass past 5 minutes was killed before its heartbeat). Output is appended to <git common dir>\open-calls-scan-task.log.

param([switch]$Install, [switch]$Uninstall, [switch]$Status, [switch]$RunNow)

$ErrorActionPreference = 'Stop'
$TaskName = 'Opal open-calls scan'

function Fail($m) { Write-Output "ERROR: $m"; exit 1 }

$root = (& git -C $PSScriptRoot rev-parse --show-toplevel 2>$null)
if (-not $root) { Fail "cannot resolve the repo root from $PSScriptRoot" }
$root = $root -replace '/', '\'
$common = (& git -C $root rev-parse --path-format=absolute --git-common-dir 2>$null)
$python = (Get-Command python.exe -ErrorAction SilentlyContinue).Source
if (-not $python) { Fail "python.exe is not on PATH" }
$pythonw = Join-Path (Split-Path $python) 'pythonw.exe'   # windowless: no console flashes on the user's screen every 10 min
if (-not (Test-Path $pythonw)) { Fail "pythonw.exe not found beside $python" }
$box = $env:AGENTBUS_DEVICE
if (-not $box) { $box = [Environment]::GetEnvironmentVariable('AGENTBUS_DEVICE', 'User') }
if (-not $box) { Fail "AGENTBUS_DEVICE is not set (process or user environment); refusing to guess the box" }
$box = $box.Trim().ToLower()
# THE SLOTS come from the device register (org/devices/DEVICES.json, NFRA_CTLPLN FWD-2), never from a list here: the n-th box in
# register order runs at minute 1 + 3n of the 10-minute cycle, capped at :09 (a box past the fourth shares :09). OPAL_DEVICE_REGISTER
# points at another register file (fixtures and proofs only), as lib/devices.py reads it.
$regFile = $env:OPAL_DEVICE_REGISTER
if (-not $regFile) { $regFile = Join-Path $root 'org\devices\DEVICES.json' }
try { $devs = @((Get-Content -Raw -Encoding UTF8 $regFile | ConvertFrom-Json).devices) } catch { Fail "device register unreadable at ${regFile}: $($_.Exception.Message)" }
if ($devs.Count -eq 0) { Fail "device register at $regFile lists no devices" }
$Slots = [ordered]@{}
for ($n = 0; $n -lt $devs.Count; $n++) { $Slots[[string]$devs[$n].name] = [Math]::Min(1 + 3 * $n, 9) }
if (-not $Slots.Contains($box)) { Fail "box '$box' has no slot in the table (known: $($Slots.Keys -join ', '))" }
$minute = $Slots[$box]
$log = Join-Path ($common -replace '/', '\') 'open-calls-scan-task.log'

if ($Status -or -not ($Install -or $Uninstall -or $RunNow)) {
  Write-Output "box=$box  minute=:0$minute then every 10 min  repo=$root  pythonw=$pythonw  log=$log"
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

# --- install: pythonw runs the pass windowless and appends its own output to the log
$action = New-ScheduledTaskAction -Execute $pythonw -Argument ".tools\open-calls-scan.py --log `"$log`"" -WorkingDirectory $root
$now = Get-Date
$first = $now.Date.AddHours($now.Hour).AddMinutes($minute)
while ($first -le $now) { $first = $first.AddMinutes(10) }
$trigger = New-ScheduledTaskTrigger -Once -At $first -RepetitionInterval (New-TimeSpan -Minutes 10) -RepetitionDuration (New-TimeSpan -Days 3650)
$settings = New-ScheduledTaskSettingsSet -MultipleInstances IgnoreNew -ExecutionTimeLimit (New-TimeSpan -Minutes 9) `
  -StartWhenAvailable -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries
$principal = New-ScheduledTaskPrincipal -UserId "$env:USERDOMAIN\$env:USERNAME" -LogonType Interactive -RunLevel Limited
Register-ScheduledTask -TaskName $TaskName -Action $action -Trigger $trigger -Settings $settings -Principal $principal `
  -Description "Runs .tools/open-calls-scan.py for box $box every 10 minutes from :0$minute. Andrew-direct 2026-10-09 ~00:0xZ. Owner 4.0.0_SA_CRO~B." -Force | Out-Null
Write-Output "OK: installed '$TaskName' on box ${box} -- first run $first, then every 10 min; log $log"

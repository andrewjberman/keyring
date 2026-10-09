# =============================================================================
# autolaunch-task.ps1 -- install / remove / read this box's LOG-ON auto-launch task (layer 2).
#
#   powershell -NoProfile -File .tools\autolaunch-task.ps1 -Serials 0.0.0_AB_MSTR      # install (current user)
#   powershell -NoProfile -File .tools\autolaunch-task.ps1 -Status                     # read
#   powershell -NoProfile -File .tools\autolaunch-task.ps1 -Teardown                   # remove
#
# The task fires at LOG-ON of the current user (30 s delay), not at boot. With no auto-login (layer 1, an
# elevated posture change that is Andrew's call per box), a restart waits at the lock screen until someone
# logs on. No elevation needed. Record: see .tools\autolaunch-agents.ps1 header.
# =============================================================================
param([string[]]$Serials, [switch]$Status, [switch]$Teardown)
# `powershell -File ... -Serials a,b` binds ONE string "a,b" (an array literal only binds in-process), so a multi-seat
# roster registered only its first seat (dell1 manager, bus b0081fa0). Split every entry on commas so both forms work.
$Serials = @($Serials | ForEach-Object { $_ -split ',' } | ForEach-Object { $_.Trim() } | Where-Object { $_ })

$TaskName = 'OPAL_autolaunch_agents'
$engine   = Join-Path $PSScriptRoot 'autolaunch-agents.ps1'
$user     = "$env:USERDOMAIN\$env:USERNAME"

if ($Teardown) {
    if (Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue) {
        Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false
        Write-Output "OK: task '$TaskName' removed."
    } else { Write-Output "OK: task '$TaskName' not present." }
    return
}
if ($Status -or -not $Serials) {
    $t = Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue
    if (-not $t) { Write-Output "ABSENT: no task '$TaskName' on $env:COMPUTERNAME."; return }
    $i = Get-ScheduledTaskInfo -TaskName $TaskName
    Write-Output ("PRESENT: '{0}' state={1} user={2} last_run={3} last_result={4}" -f $TaskName, $t.State, $t.Principal.UserId, $i.LastRunTime, $i.LastTaskResult)
    Write-Output ("  action: {0} {1}" -f $t.Actions[0].Execute, $t.Actions[0].Arguments)
    return
}

$serialArg = ($Serials | ForEach-Object { "'$_'" }) -join ','
$arg = ('-NoProfile -ExecutionPolicy Bypass -Command "& ''{0}'' -Serials {1}"' -f $engine, $serialArg)
$act = New-ScheduledTaskAction -Execute 'powershell.exe' -Argument $arg -WorkingDirectory (Split-Path -Parent $PSScriptRoot)
$trg = New-ScheduledTaskTrigger -AtLogOn -User $user
$trg.Delay = 'PT30S'
$prn = New-ScheduledTaskPrincipal -UserId $user -LogonType Interactive -RunLevel Limited
$set = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -ExecutionTimeLimit ([TimeSpan]::Zero)
Register-ScheduledTask -TaskName $TaskName -Action $act -Trigger $trg -Principal $prn -Settings $set -Force -ErrorAction Stop | Out-Null
$t = Get-ScheduledTask -TaskName $TaskName
Write-Output ("OK: '{0}' registered for {1}, state={2}, at log-on +30 s, launches: {3}" -f $TaskName, $user, $t.State, ($Serials -join ', '))

# estate-capture-schedule.ps1 -- B6-2: the device-side daily schedule for estate-capture.py
# (TO F3_CAPTURE_UPLOADER.B6; governing spec ANDREW_DIRECT_20260811_BUILD_B6_AND_COMPLETION_SPEC.md)
#
# GROUP-W DECLARATION (CTO 3a gate check b): this schedule is the FLOOR, never event-only.
# The capture pipeline's production trigger is THIS daily task -- manual/ad-hoc runs of
# estate-capture.py --upload are accelerators, and no event-driven trigger exists or may
# substitute for the floor ("a pipeline whose only trigger is another pipeline's success
# has no schedule and is a defect").
#
# CADENCE: daily 06:30 LOCAL. Each run uploads today-so-far plus the prior 7 UTC days
# (--catchup-days 7), all idempotent per-day overwrites -- so a laptop that was off or
# lidded self-heals a week of day files on its next morning run. A day with zero captured
# input is a LOUD NO-PARTITION refusal, never a silent empty object (no-data-day law,
# CVO 3b rider a) -- Task Scheduler history shows rc=2 on an all-empty window by design.
#
# MORATORIUM FRAMING (CTO-confirmed): this is a CAPTURE/ARCHIVE CADENCE -- "a schedule
# that ARCHIVES is a route." It is not a monitor/checker/alerter and builds no alerting.
#
# SITE-Z IS A DECLARED GAP: this registration covers ONE device. Until site-Z registers
# the same task, "every single text" is device-scoped and each day's object says whose.
#
# DISABLE:  schtasks /Change /TN OpalEstateCaptureDaily /DISABLE
# REMOVE:   .\estate-capture-schedule.ps1 -Action Unregister
param(
    [ValidateSet('Register', 'Unregister', 'Status')]
    [string]$Action = 'Status'
)

$TaskName = 'OpalEstateCaptureDaily'
$Tool = Join-Path $PSScriptRoot 'estate-capture.py'
$LogFile = Join-Path $env:USERPROFILE '.claude\estate-capture-schedule.log'

if ($Action -eq 'Register') {
    $Python = (Get-Command python).Source
    if (-not (Test-Path $Tool)) { Write-Error "tool not found: $Tool"; exit 2 }
    # cmd /c wrapper so stdout+stderr append to a device-local log the operator can read.
    $Arg = "/c `"`"$Python`" `"$Tool`" --upload --catchup-days 7 >> `"$LogFile`" 2>&1`""
    $TaskAction = New-ScheduledTaskAction -Execute 'cmd.exe' -Argument $Arg
    $Trigger = New-ScheduledTaskTrigger -Daily -At '06:30'
    $Settings = New-ScheduledTaskSettingsSet -StartWhenAvailable
    Register-ScheduledTask -TaskName $TaskName -Action $TaskAction -Trigger $Trigger `
        -Settings $Settings -Description ('B6-2 estate text-input capture upload (daily floor; ' +
        'catchup 7 days; TO F3_CAPTURE_UPLOADER.B6). Disable: schtasks /Change /TN ' +
        $TaskName + ' /DISABLE') -Force | Out-Null
    Write-Output "OK: registered '$TaskName' -- daily 06:30 local, StartWhenAvailable, log $LogFile"
    exit 0
}
if ($Action -eq 'Unregister') {
    Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false
    Write-Output "OK: unregistered '$TaskName'"
    exit 0
}
$t = Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue
if ($null -eq $t) { Write-Output "ABSENT: '$TaskName' is not registered on this device"; exit 1 }
$info = $t | Get-ScheduledTaskInfo
Write-Output ("PRESENT: '{0}' state={1} nextrun={2} lastrun={3} lastresult={4}" -f `
    $TaskName, $t.State, $info.NextRunTime, $info.LastRunTime, $info.LastTaskResult)

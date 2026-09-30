# Register the ONE-TIME HARVST first-light Scheduled Task (the install-schedule.ps1 convention: the signed-in user,
# Interactive, no stored password -- headed Chrome needs the desktop). The task removes itself after it runs.
# No StartWhenAvailable: a first light that missed its time must not run late into other jobs' windows.
param(
    [Parameter(Mandatory = $true)][string]$At,          # local time, e.g. '2026-10-01 05:00'
    [Parameter(Mandatory = $true)][string]$Python,
    [string]$ScriptArgs = '--no-residential',
    [string]$TaskName = 'OPAL_HARVST_first_light'
)
$ErrorActionPreference = 'Stop'
$wrapper = Join-Path $PSScriptRoot 'run-first-light.ps1'
if (-not (Test-Path -LiteralPath $Python -PathType Leaf)) { throw "Python executable missing: $Python" }
if (Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue) { throw "A task named $TaskName already exists; refusing to replace it" }
$arguments = '-NoProfile -ExecutionPolicy Bypass -WindowStyle Hidden -File "' + $wrapper + '" -Python "' + $Python +
             '" -ScriptArgs "' + $ScriptArgs + '" -TaskName "' + $TaskName + '" -SelfRemove'
$repoRoot = (& git -C $PSScriptRoot rev-parse --show-toplevel).Trim()
$action = New-ScheduledTaskAction -Execute 'powershell.exe' -Argument $arguments -WorkingDirectory $repoRoot
$identity = [System.Security.Principal.WindowsIdentity]::GetCurrent().Name
$principal = New-ScheduledTaskPrincipal -UserId $identity -LogonType Interactive -RunLevel Limited
$trigger = New-ScheduledTaskTrigger -Once -At ([datetime]::ParseExact($At, 'yyyy-MM-dd HH:mm', [Globalization.CultureInfo]::InvariantCulture))
$settings = New-ScheduledTaskSettingsSet -MultipleInstances IgnoreNew -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries `
            -ExecutionTimeLimit (New-TimeSpan -Minutes 45)
$task = New-ScheduledTask -Action $action -Principal $principal -Trigger $trigger -Settings $settings `
        -Description 'HARVST first light (one-time; 4.0.0_SA_CRO~Z with 2.0.0_SA_COO~H msg 27390). Removes itself.'
Register-ScheduledTask -TaskName $TaskName -InputObject $task | Out-Null
Get-ScheduledTask -TaskName $TaskName | Select-Object TaskName, State
Get-ScheduledTaskInfo -TaskName $TaskName | Select-Object NextRunTime

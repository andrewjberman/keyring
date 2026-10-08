<#
  kill-maint-task.ps1 -- install / remove / read the box's UNATTENDED reaper (Windows Task Scheduler).

  Andrew-direct 2026-10-08 ~16:4xZ: "I dont mind if the killer runs unattended as long as there is a clear mechanism
  of assigning PIDs to Claude Code and Codex session shells. Those should never be killed by these kind of
  operations". The mechanism is kill-maint.ps1's SESSION MAP (printed on every run); this task runs
  `kill-maint.ps1 -Unattended` on a cadence. Every run writes one KILL-MAINT-RUN (or KILL-MAINT-ABORT) line and one
  KILL-MAINT line per stopped tree to org/mcp/agent-spawn-audit.log.

  Usage:  .tools\kill-maint-task.ps1 -Status
          .tools\kill-maint-task.ps1 -Install [-Minutes 15]
          .tools\kill-maint-task.ps1 -Uninstall
  Paths are derived from this script's location (LD-0405: no device-specific logic). PS 5.1 compatible. ASCII only.
#>
param(
  [switch]$Install,
  [switch]$Uninstall,
  [switch]$Status,
  [int]$Minutes = 15
)
$ErrorActionPreference = 'Stop'
$TaskName = 'Opal kill-maint unattended'
$engine   = Join-Path $PSScriptRoot 'kill-maint.ps1'
$audit    = Join-Path (Split-Path -Parent $PSScriptRoot) 'org\mcp\agent-spawn-audit.log'

if ($Install) {
  if (-not (Test-Path $engine)) { throw "engine not found: $engine" }
  # Output goes to a last-run file, never to the console: under a headless console with no reader each write
  # stalls (measured 2026-10-08: the same run took ~151 s under the task vs 1.6 s interactive).
  $lastRun = Join-Path $env:TEMP 'opal-kill-maint-last-run.log'
  $arg = ('-NoProfile -NonInteractive -ExecutionPolicy Bypass -Command "& ''{0}'' -Unattended *> ''{1}''"' -f $engine, $lastRun)
  # conhost --headless (Windows 11) runs the console with no window at all; without it the hidden window still flashes
  $conhost = Join-Path $env:SystemRoot 'System32\conhost.exe'
  $useHeadless = $false
  if (Test-Path $conhost) {
    $prevEap = $ErrorActionPreference; $ErrorActionPreference = 'Continue'
    & $conhost --headless cmd.exe /c exit 0 2>$null | Out-Null
    if ($LASTEXITCODE -eq 0) { $useHeadless = $true }
    $ErrorActionPreference = $prevEap
  }
  if ($useHeadless) {
    $action = New-ScheduledTaskAction -Execute $conhost -Argument ('--headless powershell.exe ' + $arg) -WorkingDirectory (Split-Path -Parent $PSScriptRoot)
  } else {
    $action = New-ScheduledTaskAction -Execute 'powershell.exe' -Argument $arg -WorkingDirectory (Split-Path -Parent $PSScriptRoot)
  }
  $trigger  = New-ScheduledTaskTrigger -Once -At (Get-Date).AddMinutes(1) `
                -RepetitionInterval (New-TimeSpan -Minutes $Minutes) -RepetitionDuration (New-TimeSpan -Days 3650)
  $settings = New-ScheduledTaskSettingsSet -MultipleInstances IgnoreNew -ExecutionTimeLimit (New-TimeSpan -Minutes 10) `
                -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable
  # Interactive logon as the current user: no admin right and no stored password needed (S4U needs admin -- refused
  # "Access is denied" on the laptop 2026-10-08). The task runs while the user is logged on, which is when seats run.
  $principal = New-ScheduledTaskPrincipal -UserId ("{0}\{1}" -f $env:USERDOMAIN, $env:USERNAME) -LogonType Interactive -RunLevel Limited
  Register-ScheduledTask -TaskName $TaskName -Action $action -Trigger $trigger -Settings $settings -Principal $principal -Force -ErrorAction Stop | Out-Null
  if (-not (Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue)) { throw "ERROR: '$TaskName' not found after Register-ScheduledTask" }
  Write-Output ("OK: installed '{0}' every {1} min (headless={2}) -> {3} -Unattended" -f $TaskName, $Minutes, $useHeadless, $engine)
  Write-Output ("    record: KILL-MAINT-RUN / KILL-MAINT-ABORT / KILL-MAINT lines in {0}" -f $audit)
  Write-Output ("    full output of the last run: {0}" -f $lastRun)
  return
}
if ($Uninstall) {
  if (Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue) {
    Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false
    Write-Output "OK: removed '$TaskName'"
  } else { Write-Output "SKIP: '$TaskName' is not installed" }
  return
}
# default: -Status
$t = Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue
if (-not $t) { Write-Output "NOT INSTALLED: '$TaskName'"; return }
$i = Get-ScheduledTaskInfo -TaskName $TaskName
Write-Output ("INSTALLED: '{0}' state={1} last_run={2} last_result={3} next_run={4}" -f $TaskName, $t.State, $i.LastRunTime, $i.LastTaskResult, $i.NextRunTime)
if (Test-Path $audit) {
  Write-Output "last runs (from the audit log):"
  Get-Content $audit -Tail 400 | Where-Object { $_ -match 'KILL-MAINT-(RUN|ABORT)' } | Select-Object -Last 5 | ForEach-Object { Write-Output ("  " + $_) }
}

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [ValidatePattern('^[^\\/]+$')]
    [string]$Serial,

    [Parameter(Mandatory = $true)]
    [ValidatePattern('^[0-9a-fA-F-]{36}$')]
    [string]$ThreadId,

    [Parameter(Mandatory = $true)]
    [ValidateRange(1, [int]::MaxValue)]
    [int]$LegacyCodexPid,

    [string]$Workspace = ''
)

$ErrorActionPreference = 'Stop'

$handoffScriptRoot = $PSScriptRoot
if ([string]::IsNullOrWhiteSpace($handoffScriptRoot)) {
    $handoffScriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
}
if ([string]::IsNullOrWhiteSpace($Workspace)) {
    $Workspace = (Resolve-Path -LiteralPath (
        Join-Path -Path $handoffScriptRoot -ChildPath '..\..'
    )).Path
}
else {
    $Workspace = (Resolve-Path -LiteralPath $Workspace).Path
}

$legacy = Get-CimInstance Win32_Process -Filter "ProcessId = $LegacyCodexPid"
if ($legacy -and $legacy.Name -ne 'codex.exe') {
    throw "PID $LegacyCodexPid is $($legacy.Name), not the legacy codex.exe. Refusing to wait on an unrelated process."
}

$handoffTitle = $Serial
$Host.UI.RawUI.WindowTitle = $handoffTitle
try {
    [Console]::Title = $handoffTitle
}
catch {
    # RawUI remains the primary path for hosts without a console handle.
}
if ($env:WT_SESSION -and -not [Console]::IsOutputRedirected) {
    $escape = [char]27
    $bell = [char]7
    [Console]::Write("${escape}]0;${handoffTitle}${bell}")
}
if ($legacy) {
    Write-Host "Waiting for legacy embedded Codex PID $LegacyCodexPid to exit, then resuming $Serial..."
    Wait-Process -Id $LegacyCodexPid
    Start-Sleep -Milliseconds 500
}
else {
    Write-Host "Legacy Codex PID $LegacyCodexPid is already absent; resuming $Serial now."
}

& (Join-Path $handoffScriptRoot 'start-codex-seat.ps1') `
  -Serial $Serial `
  -ThreadId $ThreadId `
  -Workspace $Workspace

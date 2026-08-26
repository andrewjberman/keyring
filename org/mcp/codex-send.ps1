# codex-send.ps1 -- canonical single-command outbound message for Codex seats.
# Thin wrapper over codex-send.py (identity validation + canonical routing +
# broker delivery + structured receipt live there).
#
#   .\org\mcp\codex-send.ps1 -To 2.0.0_SA_COO -Subject "..." -Body "..."
#   .\org\mcp\codex-send.ps1 -To 2.0.0_SA_COO -Subject "..." -BodyFile msg.md
#
# -FromSerial defaults to $env:OPAL_AGENT_SERIAL (exported by ajb2 into the
# seat's process tree); the python layer refuses a mismatch either way.
[CmdletBinding()]
param(
    [string]$FromSerial = $env:OPAL_AGENT_SERIAL,

    [Parameter(Mandatory = $true)]
    [string]$To,

    [Parameter(Mandatory = $true)]
    [string]$Subject,

    [string]$Body,

    [string]$BodyFile
)
$ErrorActionPreference = 'Stop'
if ([string]::IsNullOrWhiteSpace($FromSerial)) {
    Write-Error 'codex-send: OPAL_AGENT_SERIAL is unset and -FromSerial was not given.'
    exit 2
}
if (-not $Body -and -not $BodyFile) {
    Write-Error 'codex-send: pass -Body or -BodyFile.'
    exit 2
}
$root = $PSScriptRoot
if ([string]::IsNullOrWhiteSpace($root)) {
    $root = Split-Path -Parent $MyInvocation.MyCommand.Path
}
$sender = Join-Path $root 'codex-send.py'
$sendArgs = @('-u', $sender, '--from-serial', $FromSerial, '--to', $To, '--subject', $Subject)
if ($BodyFile) { $sendArgs += @('--body-file', $BodyFile) }
else { $sendArgs += @('--body', $Body) }
& python @sendArgs
exit $LASTEXITCODE

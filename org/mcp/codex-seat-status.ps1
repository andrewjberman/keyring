# codex-seat-status.ps1 -- machine-readable Codex seat readiness probe.
# Thin wrapper: ALL conjunction logic lives in codex-seat-status.py so the
# arms are unit-testable. Exit 0 only on the full green conjunction.
#
#   .\org\mcp\codex-seat-status.ps1 -Serial 4.0.0_SA_CRO~A
#   .\org\mcp\codex-seat-status.ps1 -Serial 4.0.0_SA_CRO~A -Json
[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [ValidatePattern('^[^\\/]+$')]
    [string]$Serial,

    [switch]$Json
)
$ErrorActionPreference = 'Stop'
$root = $PSScriptRoot
if ([string]::IsNullOrWhiteSpace($root)) {
    $root = Split-Path -Parent $MyInvocation.MyCommand.Path
}
$probe = Join-Path $root 'codex-seat-status.py'
$probeArgs = @('-u', $probe, '--serial', $Serial)
if ($Json) { $probeArgs += '--json' }
& python @probeArgs
exit $LASTEXITCODE

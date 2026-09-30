# HARVST first light -- the Scheduled Task's action. Runs harvest_first_light.py once, logs everything, and
# (with -SelfRemove) unregisters its own one-time task afterwards, success or failure.
param(
    [Parameter(Mandatory = $true)][string]$Python,
    [string]$ScriptArgs = '--no-residential',
    [string]$TaskName = '',
    [switch]$SelfRemove
)
$ErrorActionPreference = 'Continue'
$repoRoot = (& git -C $PSScriptRoot rev-parse --show-toplevel).Trim()
Set-Location -LiteralPath $repoRoot
$logDir = Join-Path $repoRoot '.runtime\harvest-first-light'
New-Item -ItemType Directory -Force -Path $logDir | Out-Null
$stamp = (Get-Date).ToUniversalTime().ToString('yyyyMMddTHHmmssZ')
$log = Join-Path $logDir ("task-" + $stamp + ".log")
$script = Join-Path $PSScriptRoot 'harvest_first_light.py'
"START $stamp python=$Python args=$ScriptArgs task=$TaskName" | Out-File -FilePath $log -Encoding utf8
try {
    $argList = @($script) + ($ScriptArgs -split ' ' | Where-Object { $_ })
    $env:PYTHONIOENCODING = 'utf-8'
    & $Python @argList 2>&1 | ForEach-Object { "$_" } | Out-File -FilePath $log -Append -Encoding utf8
    "EXIT $LASTEXITCODE" | Out-File -FilePath $log -Append -Encoding utf8
} finally {
    if ($SelfRemove -and $TaskName) {
        try {
            Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false -ErrorAction Stop
            "TASK-REMOVED $TaskName" | Out-File -FilePath $log -Append -Encoding utf8
        } catch {
            "TASK-REMOVE-FAILED $TaskName : $($_.Exception.Message)" | Out-File -FilePath $log -Append -Encoding utf8
        }
    }
    "END $((Get-Date).ToUniversalTime().ToString('yyyyMMddTHHmmssZ'))" | Out-File -FilePath $log -Append -Encoding utf8
}

# wt-tab-title-setup.ps1 -- make a seat's tab title stick on this box.
#
# Usage:  powershell -NoProfile -File .tools\wt-tab-title-setup.ps1
#
# claude.exe rewrites the terminal title at run time, so a tab titled at launch by
# .tools\spawn-agent.ps1 (full serial, or a COO's -Tab <PROJECT_CODE>) only keeps that title
# when Windows Terminal has profiles.defaults.suppressApplicationTitle = true. This script
# sets that one key (idempotent), backs the settings file up first, and reads the key back.
# Andrew-direct 2026-10-08 ~19:0xZ at dell1: every box uses this same script and spawn-agent.ps1.

$pkg = Get-ChildItem (Join-Path $env:LOCALAPPDATA 'Packages') -Filter 'Microsoft.WindowsTerminal*' -Directory -ErrorAction SilentlyContinue |
    Select-Object -First 1
if (-not $pkg) { Write-Host 'ERROR: Windows Terminal package not found under LOCALAPPDATA\Packages'; exit 1 }
$settings = Join-Path $pkg.FullName 'LocalState\settings.json'
if (-not (Test-Path -LiteralPath $settings)) { Write-Host "ERROR: settings.json not found at $settings"; exit 1 }

$raw = [System.IO.File]::ReadAllText($settings)
$doc = $raw | ConvertFrom-Json
if ($doc.profiles.defaults -and $doc.profiles.defaults.suppressApplicationTitle -eq $true) {
    Write-Host "OK: suppressApplicationTitle already true ($settings)"
    exit 0
}

$backup = "$settings.bak-$((Get-Date).ToUniversalTime().ToString('yyyyMMddTHHmmssZ'))"
Copy-Item -LiteralPath $settings -Destination $backup
if (-not $doc.profiles.defaults) {
    $doc.profiles | Add-Member -NotePropertyName defaults -NotePropertyValue ([pscustomobject]@{}) -Force
}
$doc.profiles.defaults | Add-Member -NotePropertyName suppressApplicationTitle -NotePropertyValue $true -Force
[System.IO.File]::WriteAllText($settings, ($doc | ConvertTo-Json -Depth 32), (New-Object System.Text.UTF8Encoding($false)))

$check = ([System.IO.File]::ReadAllText($settings) | ConvertFrom-Json).profiles.defaults.suppressApplicationTitle
if ($check -eq $true) { Write-Host "OK: suppressApplicationTitle = true (backup $backup)"; exit 0 }
Write-Host "ERROR: read-back is '$check', not true; restore from $backup"
exit 1

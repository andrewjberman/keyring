# fix-rdp-nla.ps1 -- make this box reachable by Remote Desktop when NLA sign-in fails (an Entra account from a
# device that cannot pass Network Level Authentication).
#
# What it does, as Andrew gave it (Andrew-direct 2026-10-07 at the 0.0.0_AB_MSTR~Z terminal):
#   1. NLA off:        ...\Terminal Server\WinStations\RDP-Tcp  UserAuthentication = 0
#   2. RDP on:         ...\Terminal Server                      fDenyTSConnections = 0
#   3. Firewall:       Enable-NetFirewallRule -DisplayGroup "Remote Desktop"
#   4. Restart-Service TermService -Force   (an open RDP session on this box is dropped)
# Then it reads all four back and prints what it found.
#
# The four acts need elevation. Run from an elevated shell they run directly; otherwise they run through a
# one-shot scheduled task at highest privilege (the invoking user must be a local administrator), which is
# created, run and deleted, with its temp file removed.
#
# WHAT THIS WIDENS: step 1 removes the pre-session authentication of RDP, and step 3 enables the built-in
# "Remote Desktop" rules on every network profile they cover, not only the tailnet. -TailnetOnly replaces step 3
# with one inbound rule for TCP 3389 from 100.64.0.0/10 and leaves the built-in group as it is.
#
# usage:  powershell -NoProfile -ExecutionPolicy Bypass -File .tools\fix-rdp-nla.ps1 [-TailnetOnly] [-ReadOnly]
#         -ReadOnly prints the current state and changes nothing.
param([switch]$TailnetOnly, [switch]$ReadOnly)

$ErrorActionPreference = 'Stop'
$ts = 'HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server'
$rdp = "$ts\WinStations\RDP-Tcp"

function Read-State {
    $nla = (Get-ItemProperty -Path $rdp -Name UserAuthentication -ErrorAction SilentlyContinue).UserAuthentication
    $deny = (Get-ItemProperty -Path $ts -Name fDenyTSConnections -ErrorAction SilentlyContinue).fDenyTSConnections
    $grp = @(Get-NetFirewallRule -DisplayGroup 'Remote Desktop' -ErrorAction SilentlyContinue)
    $on = @($grp | Where-Object { $_.Enabled -eq 'True' }).Count
    $tn = @(Get-NetFirewallRule -DisplayName 'RDP - Tailscale tailnet only (TCP-In)' -ErrorAction SilentlyContinue | Where-Object { $_.Enabled -eq 'True' }).Count
    $svc = (Get-Service TermService).Status
    "UserAuthentication (NLA; 0 = off)      : $nla"
    "fDenyTSConnections (0 = RDP allowed)   : $deny"
    "built-in Remote Desktop rules enabled  : $on of $($grp.Count)"
    "tailnet-only RDP rule enabled          : $tn"
    "TermService                            : $svc"
    return ($nla -eq 0 -and $deny -eq 0 -and $svc -eq 'Running' -and ($on -gt 0 -or $tn -gt 0))
}

if ($ReadOnly) { Read-State | ForEach-Object { if ($_ -is [string]) { $_ } }; exit 0 }

if ($TailnetOnly) {
    $fw = 'if (-not (Get-NetFirewallRule -DisplayName "RDP - Tailscale tailnet only (TCP-In)" -ErrorAction SilentlyContinue)) { New-NetFirewallRule -DisplayName "RDP - Tailscale tailnet only (TCP-In)" -Direction Inbound -Protocol TCP -LocalPort 3389 -RemoteAddress 100.64.0.0/10 -Action Allow | Out-Null } else { Enable-NetFirewallRule -DisplayName "RDP - Tailscale tailnet only (TCP-In)" }'
} else {
    $fw = 'Enable-NetFirewallRule -DisplayGroup "Remote Desktop"'
}
$body = @"
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" -Name UserAuthentication -Value 0 -Type DWord
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server" -Name fDenyTSConnections -Value 0 -Type DWord
$fw
Restart-Service TermService -Force
"@

$elevated = ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
"before:"; Read-State | ForEach-Object { if ($_ -is [string]) { "  $_" } }

if ($elevated) {
    "running the four acts directly (this shell is elevated)"
    Invoke-Expression $body
} else {
    "this shell is not elevated: running the four acts through a one-shot scheduled task at highest privilege"
    $path = Join-Path $env:TEMP 'fixrdp.ps1'
    $body | Out-File -FilePath $path -Encoding ascii
    schtasks /create /tn FixRDP /tr "powershell -NoProfile -ExecutionPolicy Bypass -File `"$path`"" /sc once /st 00:00 /rl highest /f
    if ($LASTEXITCODE -ne 0) { Remove-Item $path -Force -ErrorAction SilentlyContinue; "ERROR: the scheduled task could not be created (rc=$LASTEXITCODE). Nothing was changed. Run this script from an elevated shell."; exit 1 }
    schtasks /run /tn FixRDP
    Start-Sleep -Seconds 8
    schtasks /delete /tn FixRDP /f
    Remove-Item $path -Force -ErrorAction SilentlyContinue
}

"after:"
$ok = $false
Read-State | ForEach-Object { if ($_ -is [string]) { "  $_" } else { $ok = $_ } }
if ($ok) { "OK: NLA is off, RDP is allowed, a firewall rule is enabled and TermService is running."; exit 0 }
"ERROR: the read-back does not show all four. The acts did not all land; read the lines above."
exit 1

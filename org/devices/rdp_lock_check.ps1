# rdp_lock_check.ps1 -- NFRA_CTLPLN CT-b-2 (FWD-14). READ-ONLY: never changes a firewall rule.
# Lists every ENABLED inbound rule whose local port includes 3389 or whose display group is
# "Remote Desktop"; a rule is LOCKED when its remote address set is exactly the tailnet range.
$ErrorActionPreference = 'Stop'
$box = $env:AGENTBUS_DEVICE
if (-not $box) { $box = [Environment]::GetEnvironmentVariable('AGENTBUS_DEVICE', 'User') }
if (-not $box) { $box = [Environment]::GetEnvironmentVariable('AGENTBUS_DEVICE', 'Machine') }
if (-not $box) { $box = $env:COMPUTERNAME }

function Test-Tailnet([string[]]$addrs) {
    if (-not $addrs -or $addrs.Count -ne 1) { return $false }
    return ($addrs[0] -eq '100.64.0.0/10' -or $addrs[0] -eq '100.64.0.0/255.192.0.0')
}

$rules = @()
foreach ($r in (Get-NetFirewallRule -Direction Inbound -Enabled True)) {
    $port = $r | Get-NetFirewallPortFilter
    $hit = ($r.DisplayGroup -eq 'Remote Desktop')
    foreach ($p in @($port.LocalPort)) {
        foreach ($tok in ([string]$p -split ',')) {
            $t = $tok.Trim()
            if ($t -eq '3389') { $hit = $true }
            elseif ($t -match '^(\d+)-(\d+)$' -and [int]$Matches[1] -le 3389 -and [int]$Matches[2] -ge 3389) { $hit = $true }
        }
    }
    if (-not $hit) { continue }
    $addr = ($r | Get-NetFirewallAddressFilter).RemoteAddress
    $rules += [pscustomobject]@{
        Name = $r.DisplayName; Protocol = [string]$port.Protocol; Profile = [string]$r.Profile
        Remote = (@($addr) -join ','); Locked = (Test-Tailnet @($addr))
    }
}
foreach ($x in $rules) {
    Write-Output ("rule name='{0}' protocol={1} profile={2} remote={3} locked={4}" -f $x.Name, $x.Protocol, $x.Profile, $x.Remote, $x.Locked)
}
$n = @($rules).Count
$k = @($rules | Where-Object { $_.Locked }).Count
$all = ($n -gt 0 -and $k -eq $n)
Write-Output ("RDP-LOCK box={0} rules={1} locked={2} all_locked={3}" -f $box, $n, $k, $all)

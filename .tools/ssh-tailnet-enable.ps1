#Requires -Version 5.1
<#
  ssh-tailnet-enable.ps1 -- turns on key-only OpenSSH over the tailnet on THIS Windows box.

  A person runs it ONCE per box from an ELEVATED PowerShell (no agent session is elevated):
    powershell -NoProfile -ExecutionPolicy Bypass -File .tools\ssh-tailnet-enable.ps1 -PublicKey <key-file-or-line> [-DisablePassword]

  Modes:
    (none)           apply: steps A-E in order, each idempotent, then a receipt. Needs elevation.
    -Plan            read-only: prints BEFORE and what each step WOULD change, writes a receipt with "mode":"plan".
                     Changes nothing; runs unelevated.
    -Rollback        stops and disables sshd and removes the tailnet firewall rule, and nothing else.
    -SelfTest        no admin, no machine change: parses this file and runs the fake-backend cases.

  The device comes from AGENTBUS_DEVICE. The default receipt folder is org/devices/state/<device>/ under the
  repo root (git rev-parse --show-toplevel). A key body is never printed or stored: only type, comment and SHA256.
  Step E never turns password authentication off in the run that first installs a key; it refuses instead.
#>
[CmdletBinding()]
param(
    [string[]]$PublicKey = @(),
    [switch]$DisablePassword,
    [switch]$Plan,
    [switch]$Rollback,
    [switch]$SelfTest,
    [string]$ReceiptDir = ''
)

Set-StrictMode -Version 2
$ErrorActionPreference = 'Stop'

$script:Here        = $PSScriptRoot
$script:SelfPath    = $PSCommandPath
$script:CapName     = 'OpenSSH.Server~~~~0.0.1.0'
$script:DefRule     = 'OpenSSH SSH Server (sshd)'
$script:TailRule    = 'OpenSSH Server (Tailscale only)'
$script:TailWant    = '100.64.0.0/10'
$script:ShellWant   = "$env:SystemRoot\System32\WindowsPowerShell\v1.0\powershell.exe"
$script:ShellKey    = 'HKLM:\SOFTWARE\OpenSSH'
$script:KeysPath    = "$env:ProgramData\ssh\administrators_authorized_keys"
$script:CfgPath     = "$env:ProgramData\ssh\sshd_config"
$script:RollbackLines = @(
    'Stop-Service sshd',
    'Set-Service sshd -StartupType Disabled',
    'Remove-NetFirewallRule -DisplayName "OpenSSH Server (Tailscale only)"'
)
$script:Backend  = @{}
$script:MutCount = 0
$script:MutLog   = @()
$script:PlanOnly = $false
$script:Fake     = @{}

function Say {
    param([string]$Line)
    Write-Host $Line
}

# Every backend call goes through here. Any 'Do.' op is a machine mutation; -Plan forbids them outright.
function Invoke-Op {
    param([string]$Name, [object[]]$OpArgs = @())
    if ($Name.StartsWith('Do.')) {
        if ($script:PlanOnly) { throw ('BUG: mutating op ' + $Name + ' requested in plan mode') }
        $script:MutCount = $script:MutCount + 1
        $script:MutLog = @($script:MutLog) + $Name
    }
    if (-not $script:Backend.ContainsKey($Name)) { throw ('BUG: no backend op ' + $Name) }
    $sb = $script:Backend[$Name]
    return (& $sb @OpArgs)
}

function Set-RealBackend {
    $script:Backend = @{
        'Read.IsElevated' = {
            $who = [Security.Principal.WindowsIdentity]::GetCurrent()
            $pr = New-Object Security.Principal.WindowsPrincipal($who)
            return [bool]$pr.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
        }
        'Read.Capability' = {
            try {
                $c = Get-WindowsCapability -Online -Name $script:CapName -ErrorAction Stop
                return ([string]$c.State -eq 'Installed')
            } catch {
                return $null
            }
        }
        'Read.Sshd' = {
            $svc = Get-Service -Name 'sshd' -ErrorAction SilentlyContinue
            if ($null -eq $svc) { return [pscustomobject]@{ Status = 'absent'; StartType = 'absent' } }
            return [pscustomobject]@{ Status = [string]$svc.Status; StartType = [string]$svc.StartType }
        }
        'Read.Rules' = {
            param($name)
            $rows = @()
            foreach ($r in @(Get-NetFirewallRule -DisplayName $name -ErrorAction SilentlyContinue)) {
                $addrs = @($r | Get-NetFirewallAddressFilter -ErrorAction SilentlyContinue | ForEach-Object { [string]$_.RemoteAddress })
                $rows += [pscustomobject]@{ Enabled = ([string]$r.Enabled -eq 'True'); RemoteAddress = ($addrs -join ',') }
            }
            return $rows
        }
        'Read.KeyFile' = {
            if (-not (Test-Path -LiteralPath $script:KeysPath)) {
                return [pscustomobject]@{ Exists = $false; Readable = $true; Lines = @() }
            }
            try {
                return [pscustomobject]@{ Exists = $true; Readable = $true; Lines = @([IO.File]::ReadAllLines($script:KeysPath)) }
            } catch {
                return [pscustomobject]@{ Exists = $true; Readable = $false; Lines = @() }
            }
        }
        'Read.KeyAcl' = {
            try {
                $acl = Get-Acl -LiteralPath $script:KeysPath
                $sids = @()
                foreach ($rule in @($acl.Access)) {
                    if ([string]$rule.AccessControlType -ne 'Allow') { return $false }
                    if ([string]$rule.FileSystemRights -notmatch 'FullControl') { return $false }
                    $sids += [string]$rule.IdentityReference.Translate([Security.Principal.SecurityIdentifier]).Value
                }
                $have = (@($sids | Sort-Object -Unique)) -join ','
                $want = (@('S-1-5-18', 'S-1-5-32-544') | Sort-Object) -join ','
                return ([bool]$acl.AreAccessRulesProtected -and ($have -eq $want))
            } catch {
                return $null
            }
        }
        'Read.DefaultShell' = {
            $v = Get-ItemProperty -Path $script:ShellKey -Name 'DefaultShell' -ErrorAction SilentlyContinue
            if ($null -eq $v) { return '' }
            return [string]$v.DefaultShell
        }
        'Read.SshdConfig' = {
            if (-not (Test-Path -LiteralPath $script:CfgPath)) {
                return [pscustomobject]@{ Exists = $false; Readable = $false; Lines = @() }
            }
            try {
                return [pscustomobject]@{ Exists = $true; Readable = $true; Lines = @([IO.File]::ReadAllLines($script:CfgPath)) }
            } catch {
                return [pscustomobject]@{ Exists = $true; Readable = $false; Lines = @() }
            }
        }
        'Read.RepoRoot' = {
            $top = @(& git -C $script:Here rev-parse --show-toplevel)
            if ($LASTEXITCODE -ne 0 -or $top.Count -eq 0) { return $null }
            return ([string]$top[0]).Trim()
        }
        'Rec.Write' = {
            param($dir, $name, $text)
            if (-not (Test-Path -LiteralPath $dir)) { New-Item -ItemType Directory -Force -Path $dir | Out-Null }
            $full = Join-Path $dir $name
            [IO.File]::WriteAllText($full, ($text + "`r`n"), (New-Object Text.UTF8Encoding($false)))
            return $full
        }
        'Do.AddCapability' = { Add-WindowsCapability -Online -Name $script:CapName | Out-Null }
        'Do.SetAuto'       = { Set-Service -Name 'sshd' -StartupType Automatic }
        'Do.StartSshd'     = { Start-Service -Name 'sshd' }
        'Do.StopSshd'      = { Stop-Service -Name 'sshd' }
        'Do.SetDisabled'   = { Set-Service -Name 'sshd' -StartupType Disabled }
        'Do.Restart'       = { Restart-Service -Name 'sshd' }
        'Do.DisableRule'   = { param($name) Disable-NetFirewallRule -DisplayName $name }
        'Do.NewRule'       = {
            New-NetFirewallRule -DisplayName $script:TailRule -Direction Inbound -Protocol TCP -LocalPort 22 -Action Allow -RemoteAddress $script:TailWant -Profile Any | Out-Null
        }
        'Do.SetRule'       = { param($name, $addr) Set-NetFirewallRule -DisplayName $name -RemoteAddress $addr -Enabled True }
        'Do.RemoveRule'    = { param($name) Remove-NetFirewallRule -DisplayName $name }
        'Do.SetShell'      = {
            param($v)
            if (-not (Test-Path -LiteralPath $script:ShellKey)) { New-Item -Path $script:ShellKey -Force | Out-Null }
            Set-ItemProperty -Path $script:ShellKey -Name 'DefaultShell' -Value $v
        }
        'Do.WriteKeys'     = { param($lines) Set-Content -LiteralPath $script:KeysPath -Value $lines -Encoding ASCII }
        'Do.SetKeyAcl'     = {
            & icacls.exe $script:KeysPath /inheritance:r /grant:r '*S-1-5-18:F' /grant:r '*S-1-5-32-544:F' | Out-Null
            if ($LASTEXITCODE -ne 0) { throw ('icacls rc=' + $LASTEXITCODE) }
        }
        'Do.WriteSshdConfig' = {
            param($lines)
            $stamp = (Get-Date).ToUniversalTime().ToString('yyyyMMddTHHmmssfffZ', [Globalization.CultureInfo]::InvariantCulture)
            $bak = $script:CfgPath + '.ssh-enable-' + $stamp + '.bak'
            Copy-Item -LiteralPath $script:CfgPath -Destination $bak -Force
            [IO.File]::WriteAllLines($script:CfgPath, [string[]]$lines, (New-Object Text.UTF8Encoding($false)))
            return $bak
        }
    }
}

function Set-FakeBackend {
    $script:Backend = @{
        'Read.IsElevated'    = { [bool]$script:Fake.Elevated }
        'Read.Capability'    = { [bool]$script:Fake.Cap }
        'Read.Sshd'          = {
            if (-not $script:Fake.Svc.Present) { return [pscustomobject]@{ Status = 'absent'; StartType = 'absent' } }
            return [pscustomobject]@{ Status = [string]$script:Fake.Svc.Status; StartType = [string]$script:Fake.Svc.Start }
        }
        'Read.Rules'         = {
            param($name)
            $o = @($script:Fake.Rules | Where-Object { $_.DisplayName -eq $name } | ForEach-Object {
                [pscustomobject]@{ Enabled = [bool]$_.Enabled; RemoteAddress = [string]$_.RemoteAddress }
            })
            return $o
        }
        'Read.KeyFile'       = {
            if ($script:Fake.KeyExists) { return [pscustomobject]@{ Exists = $true; Readable = $true; Lines = @($script:Fake.KeyLines) } }
            return [pscustomobject]@{ Exists = $false; Readable = $true; Lines = @() }
        }
        'Read.KeyAcl'        = { [bool]$script:Fake.AclOk }
        'Read.DefaultShell'  = { [string]$script:Fake.Shell }
        'Read.SshdConfig'    = { [pscustomobject]@{ Exists = $true; Readable = $true; Lines = @($script:Fake.CfgLines) } }
        'Read.RepoRoot'      = { 'FAKE-REPO-ROOT' }
        'Rec.Write'          = {
            param($dir, $name, $text)
            $script:Fake.Receipts = @($script:Fake.Receipts) + $text
            return ('FAKE:' + $name)
        }
        'Do.AddCapability'   = {
            $script:Fake.Cap = $true
            $script:Fake.Svc = @{ Present = $true; Status = 'Stopped'; Start = 'Manual' }
            # the real install creates the default firewall rule, ENABLED (Private, remote Any, port 22)
            if (@($script:Fake.Rules | Where-Object { $_.DisplayName -eq $script:DefRule }).Count -eq 0) {
                $script:Fake.Rules = @($script:Fake.Rules) + [pscustomobject]@{ DisplayName = $script:DefRule; Enabled = $true; RemoteAddress = 'Any' }
            }
        }
        'Do.SetAuto'         = { $script:Fake.Svc.Start = 'Automatic' }
        'Do.StartSshd'       = { $script:Fake.Svc.Status = 'Running' }
        'Do.StopSshd'        = { $script:Fake.Svc.Status = 'Stopped' }
        'Do.SetDisabled'     = { $script:Fake.Svc.Start = 'Disabled' }
        'Do.Restart'         = { $script:Fake.Svc.Status = 'Running' }
        'Do.DisableRule'     = {
            param($name)
            foreach ($r in @($script:Fake.Rules)) { if ($r.DisplayName -eq $name) { $r.Enabled = $false } }
        }
        'Do.NewRule'         = {
            $script:Fake.Rules = @($script:Fake.Rules) + [pscustomobject]@{ DisplayName = $script:TailRule; Enabled = $true; RemoteAddress = $script:TailWant }
        }
        'Do.SetRule'         = {
            param($name, $addr)
            foreach ($r in @($script:Fake.Rules)) { if ($r.DisplayName -eq $name) { $r.RemoteAddress = $addr; $r.Enabled = $true } }
        }
        'Do.RemoveRule'      = { param($name) $script:Fake.Rules = @($script:Fake.Rules | Where-Object { $_.DisplayName -ne $name }) }
        'Do.SetShell'        = { param($v) $script:Fake.Shell = $v }
        'Do.WriteKeys'       = { param($lines) $script:Fake.KeyExists = $true; $script:Fake.KeyLines = @($lines); $script:Fake.AclOk = $false }
        'Do.SetKeyAcl'       = { $script:Fake.AclOk = $true }
        'Do.WriteSshdConfig' = { param($lines) $script:Fake.CfgLines = @($lines); return 'FAKE-BAK' }
    }
}

function New-Fake {
    param(
        [string[]]$KeyLines = @(),
        [string]$PwLine = '#PasswordAuthentication yes',
        [string]$TailAddr = 'absent',
        [bool]$DefEnabled = $true,
        [bool]$Installed = $true
    )
    $cfg = @('Port 22', $PwLine, 'Subsystem sftp sftp-server.exe', 'Match Group administrators', '       AuthorizedKeysFile __PROGRAMDATA__/ssh/administrators_authorized_keys')
    # a box that has never had the OpenSSH capability holds no default rule either (the install creates it)
    $rules = @()
    if ($Installed) {
        $rules = @([pscustomobject]@{ DisplayName = $script:DefRule; Enabled = $DefEnabled; RemoteAddress = 'Any' })
    }
    if ($TailAddr -ne 'absent') {
        $rules += [pscustomobject]@{ DisplayName = $script:TailRule; Enabled = $true; RemoteAddress = $TailAddr }
    }
    $svc = @{ Present = $true; Status = 'Stopped'; Start = 'Manual' }
    if (-not $Installed) { $svc = @{ Present = $false; Status = 'absent'; Start = 'absent' } }
    $script:Fake = @{
        Elevated  = $true
        Cap       = [bool]$Installed
        Svc       = $svc
        Rules     = $rules
        Shell     = ''
        KeyExists = ($KeyLines.Count -gt 0)
        KeyLines  = @($KeyLines)
        AclOk     = $false
        CfgLines  = $cfg
        Receipts  = @()
    }
    $script:MutLog = @()
}

# One key line -> entry (type, blob, comment, SHA256 fingerprint). Returns $null for anything that is not one key line.
function ConvertTo-KeyEntry {
    param([string]$Line)
    if ($Line -cmatch '[^\x20-\x7E]') { return $null }
    $m = [regex]::Match($Line, '^(ssh-ed25519|ssh-rsa|ssh-dss|ecdsa-sha2-nistp256|ecdsa-sha2-nistp384|ecdsa-sha2-nistp521|sk-ssh-ed25519@openssh\.com|sk-ecdsa-sha2-nistp256@openssh\.com)\s+([A-Za-z0-9+/]+={0,2})(?:\s+(.*))?$')
    if (-not $m.Success) { return $null }
    $blob = $m.Groups[2].Value
    try { $raw = [Convert]::FromBase64String($blob) } catch { return $null }
    $sha = [System.Security.Cryptography.SHA256]::Create()
    $fp = 'SHA256:' + [Convert]::ToBase64String($sha.ComputeHash($raw)).TrimEnd('=')
    return [pscustomobject]@{ Type = $m.Groups[1].Value; Blob = $blob; Comment = $m.Groups[3].Value; Fingerprint = $fp; Line = $Line }
}

# Key lines inside an existing key file. Comment and blank lines are not keys.
function Get-KeyEntries {
    param([string[]]$Lines)
    $rows = @()
    foreach ($ln in @($Lines)) {
        $t = ([string]$ln).Trim()
        $m = [regex]::Match($t, '^(ssh-[A-Za-z0-9@.-]+|ecdsa-[A-Za-z0-9@.-]+|sk-[A-Za-z0-9@.-]+)\s+([A-Za-z0-9+/]+={0,2})(?:\s+(.*))?$')
        if ($m.Success) {
            $rows += [pscustomobject]@{ Type = $m.Groups[1].Value; Blob = $m.Groups[2].Value; Comment = $m.Groups[3].Value; Line = $t }
        }
    }
    return $rows
}

# -PublicKey items: each is a key-file path or a literal key line. Any bad line refuses the whole run.
function Get-InputKeys {
    param([string[]]$Items)
    $keys = @()
    $seen = @()
    $n = 0
    foreach ($item in @($Items)) {
        $n = $n + 1
        $isFile = $false
        try { $isFile = [bool](Test-Path -LiteralPath $item -PathType Leaf) } catch { $isFile = $false }
        if ($isFile) {
            try { $cands = @([IO.File]::ReadAllLines($item)) } catch {
                return [pscustomobject]@{ Ok = $false; Error = ('REFUSED: public key input ' + $n + ' is a file that cannot be read'); Keys = @() }
            }
        } else {
            $cands = @([string]$item)
        }
        foreach ($c in $cands) {
            $t = ([string]$c).Trim()
            if ($t -eq '' -or $t.StartsWith('#')) { continue }
            $e = ConvertTo-KeyEntry $t
            if ($null -eq $e) {
                return [pscustomobject]@{ Ok = $false; Error = ('REFUSED: public key input ' + $n + ' is not one OpenSSH public key line (body not printed)'); Keys = @() }
            }
            if ($seen -notcontains $e.Blob) { $seen += $e.Blob; $keys += $e }
        }
    }
    return [pscustomobject]@{ Ok = $true; Error = ''; Keys = $keys }
}

# First uncommented PasswordAuthentication in the GLOBAL section (before the first Match block). Absent = 'default'.
function Get-PasswordAuth {
    param([string[]]$Lines)
    foreach ($ln in @($Lines)) {
        if ($ln -match '^\s*Match\s') { break }
        if ($ln -match '^\s*PasswordAuthentication\s+(\S+)') { return ([string]$matches[1]).ToLower() }
    }
    return 'default'
}

# sshd_config with PasswordAuthentication set to no in the GLOBAL section. A new line goes BEFORE the first Match
# block, because a line after it would be scoped to that Match block.
function Get-NewSshdConfig {
    param([string[]]$Lines)
    $end = $Lines.Count
    for ($i = 0; $i -lt $Lines.Count; $i++) {
        if ($Lines[$i] -match '^\s*Match\s') { $end = $i; break }
    }
    $out = New-Object System.Collections.ArrayList
    $found = $false
    for ($i = 0; $i -lt $Lines.Count; $i++) {
        if ($i -eq $end -and -not $found) { [void]$out.Add('PasswordAuthentication no'); $found = $true }
        $ln = $Lines[$i]
        if ($i -lt $end -and $ln -match '^\s*PasswordAuthentication\s') {
            if (-not $found) { [void]$out.Add('PasswordAuthentication no'); $found = $true }
            continue
        }
        [void]$out.Add($ln)
    }
    if (-not $found) { [void]$out.Add('PasswordAuthentication no') }
    return ,([string[]]$out.ToArray())
}

# Reads the live state into one object. Pub holds exactly the six receipt keys; the rest is internal.
function Get-Observed {
    $o = @{}
    $o.Elevated = [bool](Invoke-Op 'Read.IsElevated')
    $o.Cap      = Invoke-Op 'Read.Capability'
    $o.Svc      = Invoke-Op 'Read.Sshd'
    $o.Tail     = @(Invoke-Op 'Read.Rules' -OpArgs @($script:TailRule))
    $o.Def      = @(Invoke-Op 'Read.Rules' -OpArgs @($script:DefRule))
    $o.KeyFile  = Invoke-Op 'Read.KeyFile'
    $o.Acl      = Invoke-Op 'Read.KeyAcl'
    $o.Shell    = [string](Invoke-Op 'Read.DefaultShell')
    $o.Cfg      = Invoke-Op 'Read.SshdConfig'
    $o.KeyEntries = @()
    $o.KeyCount = $null
    if ([bool]$o.KeyFile.Readable) {
        $o.KeyEntries = @(Get-KeyEntries $o.KeyFile.Lines)
        $o.KeyCount = $o.KeyEntries.Count
    }
    $o.PwAuth = $null
    if ([bool]$o.Cfg.Readable) { $o.PwAuth = Get-PasswordAuth $o.Cfg.Lines }
    $defOn = (@($o.Def | Where-Object { $_.Enabled }).Count -gt 0)
    $tailAddr = 'absent'
    if ($o.Tail.Count -gt 0) { $tailAddr = [string]$o.Tail[0].RemoteAddress }
    $o.Pub = [ordered]@{
        sshd_status                 = [string]$o.Svc.Status
        sshd_start_type             = [string]$o.Svc.StartType
        tailnet_rule_remote_address = $tailAddr
        default_rule_enabled        = [bool]$defOn
        key_lines                   = $o.KeyCount
        password_auth               = $o.PwAuth
    }
    return $o
}

function Add-Act {
    param($List, [string]$Step, [string]$Op, [object[]]$OpArgs = @(), [string]$Text, [hashtable]$Set = @{})
    [void]$List.Add([pscustomobject]@{ Step = $Step; Op = $Op; OpArgs = $OpArgs; Text = $Text; Set = $Set })
}

# Builds the ordered action list from an observation. Apply plans from the BEFORE read and RE-PLANS from a fresh read
# right after A.service installs the capability (Invoke-SshEnable), because the install creates the default rule.
# -Plan prints it; Pred is the predicted AFTER (each action's Set applied in order).
function New-Plan {
    param($Obs, [string]$Kind, $Keys, [bool]$DisablePass)
    $acts = New-Object System.Collections.ArrayList
    $refuse = ''
    $restart = $false
    if ($Kind -eq 'rollback') {
        $svcOn = ([string]$Obs.Svc.Status -ne 'absent')
        if ($svcOn -and ([string]$Obs.Svc.Status -eq 'Running')) {
            Add-Act $acts 'R.stop' 'Do.StopSshd' @() 'R.stop Stop-Service sshd' @{ sshd_status = 'Stopped' }
        }
        if ($svcOn -and ([string]$Obs.Svc.StartType -ne 'Disabled')) {
            Add-Act $acts 'R.disable' 'Do.SetDisabled' @() 'R.disable Set-Service sshd -StartupType Disabled' @{ sshd_start_type = 'Disabled' }
        }
        if ($Obs.Tail.Count -gt 0) {
            Add-Act $acts 'R.rule' 'Do.RemoveRule' @($script:TailRule) ('R.rule Remove-NetFirewallRule "' + $script:TailRule + '"') @{ tailnet_rule_remote_address = 'absent' }
        }
    } else {
        # A. service
        $cap = $Obs.Cap
        if ($null -eq $cap) { $cap = ([string]$Obs.Svc.Status -ne 'absent') }
        $st = [string]$Obs.Svc.Status
        $sa = [string]$Obs.Svc.StartType
        if (-not [bool]$cap) {
            Add-Act $acts 'A.service' 'Do.AddCapability' @() 'A.service Add-WindowsCapability OpenSSH.Server' @{ sshd_status = 'Stopped'; sshd_start_type = 'Manual' }
            $st = 'Stopped'
            $sa = 'Manual'
        }
        if ($sa -ne 'Automatic') {
            Add-Act $acts 'A.service' 'Do.SetAuto' @() 'A.service Set-Service sshd -StartupType Automatic' @{ sshd_start_type = 'Automatic' }
            $sa = 'Automatic'
        }
        if ($st -ne 'Running') {
            Add-Act $acts 'A.service' 'Do.StartSshd' @() 'A.service Start-Service sshd' @{ sshd_status = 'Running' }
            $st = 'Running'
        }

        # B. firewall
        $defOn = (@($Obs.Def | Where-Object { $_.Enabled }).Count -gt 0)
        if ($defOn) {
            Add-Act $acts 'B.firewall' 'Do.DisableRule' @($script:DefRule) ('B.firewall Disable-NetFirewallRule "' + $script:DefRule + '"') @{ default_rule_enabled = $false }
        }
        $tailNew = 'B.firewall New-NetFirewallRule "' + $script:TailRule + '" -Direction Inbound -Protocol TCP -LocalPort 22 -Action Allow -RemoteAddress ' + $script:TailWant + ' -Profile Any'
        $tc = $Obs.Tail.Count
        if ($tc -eq 0) {
            Add-Act $acts 'B.firewall' 'Do.NewRule' @() $tailNew @{ tailnet_rule_remote_address = $script:TailWant }
        } elseif ($tc -gt 1) {
            Add-Act $acts 'B.firewall' 'Do.RemoveRule' @($script:TailRule) ('B.firewall Remove-NetFirewallRule "' + $script:TailRule + '" (duplicates)') @{ tailnet_rule_remote_address = 'absent' }
            Add-Act $acts 'B.firewall' 'Do.NewRule' @() $tailNew @{ tailnet_rule_remote_address = $script:TailWant }
        } else {
            $r = $Obs.Tail[0]
            if (([string]$r.RemoteAddress -ne $script:TailWant) -or (-not [bool]$r.Enabled)) {
                Add-Act $acts 'B.firewall' 'Do.SetRule' @($script:TailRule, $script:TailWant) ('B.firewall Set-NetFirewallRule "' + $script:TailRule + '" -RemoteAddress ' + $script:TailWant + ' -Enabled True') @{ tailnet_rule_remote_address = $script:TailWant }
            }
        }

        # C. default shell
        if ([string]$Obs.Shell -ne $script:ShellWant) {
            Add-Act $acts 'C.default_shell' 'Do.SetShell' @($script:ShellWant) 'C.default_shell set HKLM OpenSSH DefaultShell' @{}
            $restart = $true
        }

        # D. keys and their ACL
        $kf = $Obs.KeyFile
        $existing = @()
        $existingBlobs = @()
        if ([bool]$kf.Readable) {
            $existing = @($kf.Lines)
            $existingBlobs = @($Obs.KeyEntries | ForEach-Object { $_.Blob })
        }
        $newKeys = @()
        foreach ($k in @($Keys)) {
            if ([bool]$kf.Readable -and ($existingBlobs -contains $k.Blob)) { continue }
            $newKeys += $k
        }
        if ($newKeys.Count -gt 0) {
            $allLines = @($existing) + @($newKeys | ForEach-Object { $_.Line })
            $desc = @($newKeys | ForEach-Object { [string]$_.Type + ' ' + [string]$_.Comment + ' ' + [string]$_.Fingerprint })
            $keySet = $null
            if ([bool]$kf.Readable) { $keySet = ([int]$Obs.KeyCount) + $newKeys.Count }
            Add-Act $acts 'D.keys' 'Do.WriteKeys' @(,([string[]]$allLines)) ('D.keys added ' + ($desc -join ' | ')) @{ key_lines = $keySet }
            $restart = $true
        }
        $willExist = ([bool]$kf.Exists -or ($newKeys.Count -gt 0))
        if ($willExist -and (($newKeys.Count -gt 0) -or ($Obs.Acl -ne $true))) {
            Add-Act $acts 'D.acl' 'Do.SetKeyAcl' @() 'D.acl icacls administrators_authorized_keys: inheritance off, SYSTEM and Administrators only' @{}
            $restart = $true
        }

        # E. password authentication (never in the run that first installs a key)
        if ($DisablePass) {
            if (-not [bool]$kf.Readable) {
                $refuse = 'key file unreadable (run elevated to decide); password auth left on'
            } elseif ([int]$Obs.KeyCount -lt 1) {
                $refuse = 'no key present, password auth left on'
            } elseif (-not [bool]$Obs.Cfg.Readable) {
                $refuse = 'sshd_config unreadable; password auth left on'
            } elseif ([string]$Obs.PwAuth -ne 'no') {
                $newCfg = Get-NewSshdConfig $Obs.Cfg.Lines
                Add-Act $acts 'E.password_auth' 'Do.WriteSshdConfig' @(,([string[]]$newCfg)) 'E.password_auth sshd_config PasswordAuthentication no (backup written beside it)' @{ password_auth = 'no' }
                $restart = $true
            }
        }

        if ($restart) {
            Add-Act $acts 'restart' 'Do.Restart' @() 'restart sshd (Restart-Service sshd)' @{}
        }
    }

    $pred = [ordered]@{}
    foreach ($k in @($Obs.Pub.Keys)) { $pred[$k] = $Obs.Pub[$k] }
    foreach ($a in @($acts.ToArray())) {
        foreach ($k in @($a.Set.Keys)) { $pred[$k] = $a.Set[$k] }
    }
    return [pscustomobject]@{ Acts = @($acts.ToArray()); Pred = $pred; Refuse = $refuse }
}

function Copy-Pub {
    param($P)
    $o = [ordered]@{}
    foreach ($k in @($P.Keys)) { $o[$k] = $P[$k] }
    return ,$o
}

function Format-Pub {
    param($P)
    $parts = @()
    foreach ($k in @($P.Keys)) {
        $v = $P[$k]
        if ($null -eq $v) { $parts += ($k + '=null') } else { $parts += ($k + '=' + [string]$v) }
    }
    return ($parts -join ' ')
}

function Build-Receipt {
    param([string]$Mode, [string]$Device, $Before, $After, [string[]]$Changed)
    $utc = (Get-Date).ToUniversalTime().ToString('yyyy-MM-dd\THH:mm:ss\Z', [Globalization.CultureInfo]::InvariantCulture)
    $r = [ordered]@{
        mode          = $Mode
        device        = $Device
        utc           = $utc
        before        = (Copy-Pub $Before)
        after         = (Copy-Pub $After)
        changed_steps = @($Changed)
        rollback      = @($script:RollbackLines)
    }
    return (ConvertTo-Json -InputObject $r -Compress -Depth 5)
}

function Write-Receipt {
    param([string]$Dir, [string]$Json)
    $stamp = (Get-Date).ToUniversalTime().ToString('yyyyMMddTHHmmssfffZ', [Globalization.CultureInfo]::InvariantCulture)
    $name = 'ssh_enable_' + $stamp + '.json'
    return (Invoke-Op 'Rec.Write' -OpArgs @($Dir, $name, $Json))
}

function Show-Rollback {
    Say 'ROLLBACK (undo, from an elevated PowerShell, or run this script with -Rollback):'
    foreach ($l in @($script:RollbackLines)) { Say ('  ' + $l) }
}

function Invoke-SshEnable {
    param([string]$Mode, [string]$Kind, [string]$Device, [string]$Dir, [string[]]$Items, [bool]$DisablePass)
    $script:PlanOnly = ($Mode -eq 'plan')
    $muts0 = $script:MutCount
    $res = [pscustomobject]@{ Exit = 0; Refused = $false; Note = ''; Changed = @(); Muts = 0; Receipt = ''; Path = '' }

    if ([string]::IsNullOrEmpty($Device) -or ($Device.Trim() -eq '')) {
        Say 'REFUSED: AGENTBUS_DEVICE unset'
        $res.Exit = 2; $res.Refused = $true; $res.Note = 'AGENTBUS_DEVICE unset'
        return $res
    }

    $keyRes = Get-InputKeys -Items $Items
    if (-not $keyRes.Ok) {
        Say $keyRes.Error
        $res.Exit = 2; $res.Refused = $true; $res.Note = $keyRes.Error
        return $res
    }
    $keys = @($keyRes.Keys)
    if ($Kind -eq 'rollback' -and $keys.Count -gt 0) { Say 'NOTE: -PublicKey is ignored by -Rollback' }

    $obs = Get-Observed
    if ($Mode -ne 'plan') {
        if (-not [bool]$obs.Elevated) {
            Say 'REFUSED: not elevated; run from an elevated PowerShell (nothing changed)'
            $res.Exit = 2; $res.Refused = $true; $res.Note = 'not elevated'
            return $res
        }
        if (($Kind -eq 'enable') -and ($keys.Count -gt 0) -and (-not [bool]$obs.KeyFile.Readable)) {
            Say 'REFUSED: key file unreadable; not writing over it (nothing changed)'
            $res.Exit = 2; $res.Refused = $true; $res.Note = 'key file unreadable'
            return $res
        }
    }

    $dirFull = ''
    if ([string]::IsNullOrEmpty($Dir)) {
        $root = Invoke-Op 'Read.RepoRoot'
        if ([string]::IsNullOrEmpty([string]$root)) {
            Say 'REFUSED: repo root unresolved (git rev-parse --show-toplevel failed)'
            $res.Exit = 2; $res.Refused = $true; $res.Note = 'repo root unresolved'
            return $res
        }
        $dirFull = Join-Path ([string]$root) ('org/devices/state/' + $Device)
    } elseif ([IO.Path]::IsPathRooted($Dir)) {
        $dirFull = $Dir
    } else {
        $dirFull = [IO.Path]::GetFullPath((Join-Path (Get-Location).ProviderPath $Dir))
    }

    $pl = New-Plan -Obs $obs -Kind $Kind -Keys $keys -DisablePass $DisablePass
    Say ('SSH-ENABLE mode=' + $Mode + ' kind=' + $Kind + ' device=' + $Device)
    Say ('BEFORE ' + (Format-Pub $obs.Pub))
    Say ('BEFORE sshd_capability=' + [string]$obs.Cap + ' elevated=' + [string]$obs.Elevated + ' default_shell_ok=' + [string]($obs.Shell -eq $script:ShellWant))
    Say ('BEFORE key_file exists=' + [string]$obs.KeyFile.Exists + ' readable=' + [string]$obs.KeyFile.Readable + ' acl_ok=' + [string]$obs.Acl + ' key_lines=' + [string]$obs.KeyCount)

    if ($Mode -eq 'plan') {
        if ($pl.Acts.Count -eq 0) { Say 'WOULD CHANGE: nothing' }
        foreach ($a in @($pl.Acts)) { Say ('WOULD ' + $a.Text) }
        if (@($pl.Acts | Where-Object { $_.Op -eq 'Do.AddCapability' }).Count -gt 0) {
            Say 'NOTE: the install creates the default firewall rule; apply re-reads after A.service and disables it in B if enabled'
        }
        if ($pl.Refuse -ne '') { Say ('WOULD REFUSE: ' + $pl.Refuse) }
        $changed = @($pl.Acts | ForEach-Object { [string]$_.Text })
        $json = Build-Receipt -Mode 'plan' -Device $Device -Before $obs.Pub -After $pl.Pred -Changed $changed
        $path = Write-Receipt -Dir $dirFull -Json $json
        Say ('RECEIPT ' + [string]$path)
        Say $json
        Show-Rollback
        $res.Exit = 0
        $res.Changed = $changed
        $res.Receipt = $json
        $res.Path = [string]$path
        $res.Muts = $script:MutCount - $muts0
        return $res
    }

    $changedDone = @()
    $failed = $false
    $errMsg = ''
    $queue = @($pl.Acts)
    $qi = 0
    while ($qi -lt $queue.Count) {
        if ($failed) { break }
        $a = $queue[$qi]
        $qi = $qi + 1
        try {
            $ret = Invoke-Op -Name $a.Op -OpArgs $a.OpArgs
            $changedDone += [string]$a.Text
            Say ('DID ' + $a.Text)
            if ($a.Op -eq 'Do.WriteSshdConfig') { Say ('BACKUP ' + [string]$ret) }
            if ($a.Op -eq 'Do.AddCapability') {
                # step A just created the install's default firewall rule (enabled). The BEFORE plan cannot see it,
                # so re-read the live state and re-plan the rest; step B then disables that rule. Once only: the
                # capability's own act is never re-queued.
                $obsR = Get-Observed
                $pl = New-Plan -Obs $obsR -Kind $Kind -Keys $keys -DisablePass $DisablePass
                $queue = @($pl.Acts | Where-Object { $_.Op -ne 'Do.AddCapability' })
                $qi = 0
                Say ('REPLAN after A.service default_rule_enabled=' + [string]$obsR.Pub['default_rule_enabled'] + ' remaining=' + [string]$queue.Count)
            }
        } catch {
            $failed = $true
            $errMsg = $_.Exception.Message
        }
    }
    $obs2 = Get-Observed
    Say ('AFTER ' + (Format-Pub $obs2.Pub))
    $exit = 0
    $refused = $false
    if ($failed) {
        Say ('ERROR ' + $errMsg + ' (AFTER above is the state reached)')
        $exit = 1
    } elseif ($pl.Refuse -ne '') {
        Say ('REFUSED: ' + $pl.Refuse)
        $refused = $true
        $exit = 2
    }
    $json = Build-Receipt -Mode $Mode -Device $Device -Before $obs.Pub -After $obs2.Pub -Changed $changedDone
    $path = Write-Receipt -Dir $dirFull -Json $json
    Say ('RECEIPT ' + [string]$path)
    Say $json
    Show-Rollback
    $res.Exit = $exit
    $res.Refused = $refused
    $res.Changed = $changedDone
    $res.Receipt = $json
    $res.Path = [string]$path
    $res.Muts = $script:MutCount - $muts0
    return $res
}

function Invoke-Case {
    param([int]$N, [string]$Name, [scriptblock]$Body)
    $ok = $false
    try {
        $out = @(& $Body)
        $ok = ($out.Count -gt 0) -and [bool]$out[$out.Count - 1]
    } catch {
        Say ('  case error: ' + $_.Exception.Message)
        $ok = $false
    }
    Say ('CASE ' + $N + ' ' + $Name + ' ok=' + [string]$ok)
    return $ok
}

function Invoke-SelfTest {
    $blobA = [Convert]::ToBase64String([byte[]](1..51 | ForEach-Object { [byte](($_ * 7) % 256) }))
    $blobB = [Convert]::ToBase64String([byte[]](1..51 | ForEach-Object { [byte](($_ * 11 + 3) % 256) }))
    $lineA = 'ssh-ed25519 ' + $blobA + ' selftest-key-a'
    $lineB = 'ssh-ed25519 ' + $blobB + ' selftest-key-b'

    $tok = $null
    $perr = $null
    [void][System.Management.Automation.Language.Parser]::ParseFile($script:SelfPath, [ref]$tok, [ref]$perr)
    $parseCount = 0
    if ($null -ne $perr) { $parseCount = @($perr).Count }
    Say ('SSH-ENABLE-PARSE errors=' + $parseCount)

    Set-FakeBackend
    $results = @()

    # 1. -Plan calls zero mutating cmdlets
    $results += (Invoke-Case 1 'plan-zero-mutations' {
        New-Fake -KeyLines @($lineA)
        $r = Invoke-SshEnable -Mode 'plan' -Kind 'enable' -Device 'selftest' -Dir 'FAKE-DIR' -Items @($lineB) -DisablePass $true
        $rc = @($script:Fake.Receipts)
        ($r.Muts -eq 0) -and ($rc.Count -gt 0) -and ([string]$rc[$rc.Count - 1]).Contains('"mode":"plan"')
    })

    # 2. no key present + -DisablePassword: REFUSED, PasswordAuthentication untouched
    $results += (Invoke-Case 2 'no-key-refuses-password' {
        New-Fake -KeyLines @()
        $r = Invoke-SshEnable -Mode 'apply' -Kind 'enable' -Device 'selftest' -Dir 'FAKE-DIR' -Items @($lineA) -DisablePass $true
        $pwNo = @($script:Fake.CfgLines | Where-Object { $_ -match '^\s*PasswordAuthentication\s+no' }).Count
        $untouched = (@($script:Fake.CfgLines) -contains '#PasswordAuthentication yes')
        ($r.Exit -eq 2) -and ([bool]$r.Refused) -and ($pwNo -eq 0) -and $untouched -and (@($script:MutLog) -notcontains 'Do.WriteSshdConfig')
    })

    # 3. second run changes nothing
    $results += (Invoke-Case 3 'second-run-idempotent' {
        New-Fake -KeyLines @($lineA)
        $r1 = Invoke-SshEnable -Mode 'apply' -Kind 'enable' -Device 'selftest' -Dir 'FAKE-DIR' -Items @($lineA) -DisablePass $true
        $r2 = Invoke-SshEnable -Mode 'apply' -Kind 'enable' -Device 'selftest' -Dir 'FAKE-DIR' -Items @($lineA) -DisablePass $true
        $pw = Get-PasswordAuth $script:Fake.CfgLines
        ($r1.Exit -eq 0) -and ($r1.Muts -gt 0) -and ($r2.Exit -eq 0) -and (@($r2.Changed).Count -eq 0) -and ($r2.Muts -eq 0) -and ($pw -eq 'no')
    })

    # 4. firewall rewrites an Any tailnet rule to the tailnet range and disables the default rule
    $results += (Invoke-Case 4 'firewall-rewrites-any' {
        New-Fake -TailAddr 'Any'
        $r = Invoke-SshEnable -Mode 'apply' -Kind 'enable' -Device 'selftest' -Dir 'FAKE-DIR' -Items @() -DisablePass $false
        $tr = @($script:Fake.Rules | Where-Object { $_.DisplayName -eq $script:TailRule })
        $dr = @($script:Fake.Rules | Where-Object { $_.DisplayName -eq $script:DefRule })
        ($r.Exit -eq 0) -and ($tr.Count -eq 1) -and ([string]$tr[0].RemoteAddress -eq $script:TailWant) -and ([bool]$tr[0].Enabled) -and (-not [bool]$dr[0].Enabled) -and (@($script:MutLog) -contains 'Do.SetRule')
    })

    # 5. AGENTBUS_DEVICE unset refuses before anything else
    $results += (Invoke-Case 5 'device-unset-refuses' {
        New-Fake
        $r = Invoke-SshEnable -Mode 'plan' -Kind 'enable' -Device '' -Dir 'FAKE-DIR' -Items @($lineA) -DisablePass $true
        $rc = @($script:Fake.Receipts)
        ($r.Exit -eq 2) -and ($r.Note -eq 'AGENTBUS_DEVICE unset') -and (@($script:MutLog).Count -eq 0) -and ($rc.Count -eq 0)
    })

    # 6. no key body in the receipt
    $results += (Invoke-Case 6 'no-key-body-in-receipt' {
        New-Fake
        $r = Invoke-SshEnable -Mode 'apply' -Kind 'enable' -Device 'selftest' -Dir 'FAKE-DIR' -Items @($lineA) -DisablePass $false
        $rc = @($script:Fake.Receipts)
        $rec = [string]$rc[$rc.Count - 1]
        ($r.Exit -eq 0) -and (-not $rec.Contains($blobA)) -and $rec.Contains('SHA256:') -and $rec.Contains('"mode":"apply"')
    })

    # 7. fresh install (no capability, no default rule): the default rule step A creates is disabled by step B
    $results += (Invoke-Case 7 'fresh-install-default-rule-disabled' {
        New-Fake -Installed $false
        $r = Invoke-SshEnable -Mode 'apply' -Kind 'enable' -Device 'selftest' -Dir 'FAKE-DIR' -Items @() -DisablePass $false
        $dr = @($script:Fake.Rules | Where-Object { $_.DisplayName -eq $script:DefRule })
        $tr = @($script:Fake.Rules | Where-Object { $_.DisplayName -eq $script:TailRule })
        ($r.Exit -eq 0) -and (@($script:MutLog) -contains 'Do.AddCapability') -and (@($script:MutLog) -contains 'Do.DisableRule') -and ($dr.Count -eq 1) -and (-not [bool]$dr[0].Enabled) -and ($tr.Count -eq 1) -and ([bool]$tr[0].Enabled)
    })

    $k = @($results | Where-Object { $_ -eq $true }).Count
    $n = 7
    $all = (($k -eq $n) -and ($parseCount -eq 0))
    Say ('SSH-ENABLE-SELFTEST cases=' + $k + '/' + $n + ' ok=' + [string]$all)
    if ($all) { return 0 }
    return 1
}

# ---- main ----
Set-RealBackend
if ($SelfTest) {
    $code = Invoke-SelfTest
    exit ([int]$code)
}

$deviceName = [string]$env:AGENTBUS_DEVICE
if ($Plan) { $runMode = 'plan' } elseif ($Rollback) { $runMode = 'rollback' } else { $runMode = 'apply' }
if ($Rollback) { $runKind = 'rollback' } else { $runKind = 'enable' }
$res = Invoke-SshEnable -Mode $runMode -Kind $runKind -Device $deviceName -Dir $ReceiptDir -Items @($PublicKey) -DisablePass ([bool]$DisablePassword)
exit ([int]$res.Exit)

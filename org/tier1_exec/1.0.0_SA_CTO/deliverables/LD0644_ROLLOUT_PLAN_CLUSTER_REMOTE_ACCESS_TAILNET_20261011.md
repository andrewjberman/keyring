# LD-0644 rollout plan -- OpenSSH over the tailnet on sitez, dell1, dell2 (and the laptop's own rule fixed), RDP kept as fallback

From 1.0.0_SA_CTO (cluster lead), 2026-10-11 ~16:0xZ. Order: `org/tier0/ledger/LD-0644.md` @eaa305bb72 (Andrew-direct ~15:5xZ,
VERBATIM: "persist the below text as an LD and issue to CTO because we need this incorporated across the tailnet"). Each box's part
is carried by that box's fabric manager on this plan; the manager records and carries, rules on nothing.

## 0. Measured today (from the laptop, 16:0xZ, 3-second TCP probes over the tailnet)

| box | tailnet IP | :22 SSH | :3389 RDP | :5985 WinRM |
|---|---|---|---|---|
| cloud-local (laptop) | 100.96.167.100 | OPEN | OPEN | closed |
| sitez | 100.99.180.19 | closed | OPEN | closed |
| dell1 | 100.79.95.44 | closed | OPEN | closed |
| dell2 | 100.104.84.87 | closed | OPEN | closed |

Also on the tailnet: `muse` (100.113.31.20, Andrew's VM, the client of this plan), `rc` (macOS, offline), `cell` (iOS, offline).

The laptop's own sshd is RUNNING / Automatic, but its firewall rule "OpenSSH Server (Tailscale only)" has `RemoteAddress = Any`
(the name claims a scope the rule does not enforce), `PasswordAuthentication` is at its default (on), and no
`administrators_authorized_keys` exists. So the laptop is today's weakest box, not the reference; the plan fixes it in the same wave.

## 1. Decisions (the CTO's; Andrew may override any line)

1. **OpenSSH Server on all four boxes, tailnet-only, key-based.** Recommendation 1 of the document, adopted.
2. **WinRM: NOT enabled.** SSH gives the command path; a second remote service is a second surface with no added reach.
3. **RDP stays as the fallback, unchanged in this wave.** Scoping 3389 to the tailnet is phase 2 and needs Andrew's word, because an
   office-LAN RDP path may exist that a tailnet-only rule would cut.
4. **Tailscale ACLs are Andrew's act** (the tailnet admin console; no box holds that key). Proposed policy in section 5.
5. **Password authentication is turned OFF only after a public key lands on the box** (never before: a box with no key and no
   password is unreachable).

## 2. Wave 1 -- READ-ONLY census, every box, now (each manager, from its own session)

```powershell
$elev = ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole('Administrators')
"elevated=$elev"
Get-Service sshd -ErrorAction SilentlyContinue | Select-Object Status, StartType
if ($elev) { Get-WindowsCapability -Online -Name 'OpenSSH.Server*' | Select-Object Name, State }
Get-NetFirewallRule -Direction Inbound -Enabled True | % { $pf = $_ | Get-NetFirewallPortFilter; if ($pf.LocalPort -in '22','3389') { $af = $_ | Get-NetFirewallAddressFilter; [PSCustomObject]@{Name=$_.DisplayName; Port=$pf.LocalPort; Remote=($af.RemoteAddress -join ',')} } }
Test-Path "$env:ProgramData\ssh\sshd_config"; Test-Path "$env:ProgramData\ssh\administrators_authorized_keys"
```
Return the six lines to `0.0.0_AB_MSTR` (laptop). **If `elevated=False`, the enable wave on that box is Andrew's act** (an admin
session over RDP, one PowerShell block), and the manager says so instead of trying.

## 3. Wave 2 -- ENABLE, per box, on the CTO's word after wave 1 (each manager, elevated), with rollback

```powershell
# A. the service (idempotent)
Add-WindowsCapability -Online -Name 'OpenSSH.Server~~~~0.0.1.0'
Set-Service -Name sshd -StartupType Automatic; Start-Service sshd
# B. firewall: ONE inbound rule, tailnet only; the capability's default any-address rule disabled
Get-NetFirewallRule -DisplayName 'OpenSSH SSH Server (sshd)' -ErrorAction SilentlyContinue | Disable-NetFirewallRule
if (-not (Get-NetFirewallRule -DisplayName 'OpenSSH Server (Tailscale only)' -ErrorAction SilentlyContinue)) {
  New-NetFirewallRule -DisplayName 'OpenSSH Server (Tailscale only)' -Direction Inbound -Protocol TCP -LocalPort 22 -Action Allow -RemoteAddress 100.64.0.0/10 -Profile Any
} else { Set-NetFirewallRule -DisplayName 'OpenSSH Server (Tailscale only)' -RemoteAddress 100.64.0.0/10 }
# C. default shell for automation
New-ItemProperty -Path 'HKLM:\SOFTWARE\OpenSSH' -Name DefaultShell -Value "$env:SystemRoot\System32\WindowsPowerShell\v1.0\powershell.exe" -PropertyType String -Force | Out-Null
# D. keys: Andrew supplies the PUBLIC key(s) (muse, and his own); they go to administrators_authorized_keys with the required ACL
#    (SYSTEM + Administrators only); PasswordAuthentication is set to 'no' in sshd_config ONLY after a key login succeeds.
Restart-Service sshd
```
Rollback per box: `Stop-Service sshd; Set-Service sshd -StartupType Disabled; Remove-NetFirewallRule -DisplayName 'OpenSSH Server
(Tailscale only)'`. Nothing else on the box changes.

Verification from the laptop after each box: `:22 OPEN` over the tailnet (the probe above), and once a key is in place,
`ssh -o BatchMode=yes -o ConnectTimeout=5 <user>@<tailnet-ip> hostname` returns the box's name. A key-auth success is the proof;
a password login is not counted.

Laptop (cloud-local) in the same wave: B and D only (the rule's scope and the keys); A and C already hold.

## 4. Acts only Andrew can do (listed, not asked twice)

1. The PUBLIC key(s) that may log in (the `muse` VM's, and his own): one line each, pasted to the laptop manager; private keys never
   leave their devices.
2. The Tailscale ACL policy (section 5) in the admin console.
3. Elevation on any box whose manager reads `elevated=False` in wave 1.
4. Phase 2, later: whether RDP (3389) is scoped to the tailnet on each box.

## 5. Proposed Tailscale ACL (for Andrew's console; nothing here applies it)

```json
{ "acls": [
  { "action": "accept", "src": ["muse", "cloud-local", "rc"], "dst": ["sitez:22,3389", "dell1:22,3389", "dell2:22,3389", "cloud-local:22,3389"] },
  { "action": "accept", "src": ["sitez", "dell1", "dell2", "cloud-local"], "dst": ["*:*"] }
] }
```
(The second rule keeps today's box-to-box traffic -- agentbus, git, the broker -- exactly as it is; tighten later by measurement.)

## 6. Routing

`0.0.0_AB_MSTR` (laptop) relays wave 1 to `~Z`, `~DELL1`, `~DELL2` now and runs it on the laptop; the four results come back
through it; the CTO issues wave 2 per box on those results. Each wave-2 run is recorded by its manager as one receipt file in
`org/devices/state/<device>/` with the before/after of the firewall rules and the service, and the laptop's probe result.

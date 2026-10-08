# ANDREW-DIRECT 2026-10-07 ~22:4xZ -- condense the RDP fix into a script, commit it, have the laptop MSTR run it

Given at the `0.0.0_AB_MSTR~Z` terminal (site Z), in-session.

## Verbatim

"Can you condense this into a script, commit it, and get the laptop MSTR to run it? [pasted block] . I am trying to use
tailnet from device "rc" but cloud-local tailnet is having issues via entra"

## The pasted block, as he gave it

```
Send the agent on cloud-local this PowerShell block to run as andrew:

$ps = @'
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" -Name UserAuthentication -Value 0 -Type DWord
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server" -Name fDenyTSConnections -Value 0 -Type DWord
Enable-NetFirewallRule -DisplayGroup "Remote Desktop"
Restart-Service TermService -Force
'@
$path = "$env:TEMP\fixrdp.ps1"
$ps | Out-File -FilePath $path -Encoding ascii
schtasks /create /tn FixRDP /tr "powershell -NoProfile -ExecutionPolicy Bypass -File `"$path`"" /sc once /st 00:00 /rl highest /f
schtasks /run /tn FixRDP
Start-Sleep -Seconds 8
schtasks /delete /tn FixRDP /f
Remove-Item $path -Force
```

## What this seat does with it

- `.tools/fix-rdp-nla.ps1`: the same four acts and the same one-shot scheduled-task route, run with no switch. Added:
  a read-back of the four values after, a direct path when the shell is already elevated, a refusal that changes
  nothing when the task cannot be created, `-ReadOnly` (state only), and `-TailnetOnly` (one rule for TCP 3389 from
  100.64.0.0/10 in place of enabling the built-in group). The default is his block, not the narrower switch.
- The script's text goes to the laptop `0.0.0_AB_MSTR` on the agent bus, with its sha256, to run with no switch on
  the laptop (cloud-local) as his user. Site Z is not changed: `-ReadOnly` here read NLA on and the tailnet-only rule.
- Stated to him, not decided for him: the block turns off Network Level Authentication and enables the built-in
  Remote Desktop firewall rules on every profile they cover, which is wider than the tailnet.

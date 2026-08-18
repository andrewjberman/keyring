# ANDREW-DIRECT 2026-08-18 ~19:3xZ — RDP-over-tailnet: he handles it WITH MSTR~Z at the box

**Channel:** Andrew at the LAPTOP terminal -> laptop MSTR -> agentbus relay to site Z
(MessageId c034efd3-6270-45c4-a859-353d1892d1a8, received 20:16:26Z, ACKed 4a84fd01 at 20:18Z).

**VERBATIM (as relayed by 0.0.0_AB_MSTR laptop):**
> "relay to MSTR~Z i will handle it with them on that box"

**Relayer-carried context (laptop MSTR, grounded on its own probes 19:2xZ):** Andrew is at the
office and wants to LIVE-TEST the tailscale channel now; the remaining gap is RDP over the
tailnet. He will work the box-side change WITH MSTR~Z at the Bloomberg box himself — expect him
at/near the console; the act is his+ours, not the laptop's. Laptop probe: tunnel healthy both
directions (5ms pong, currently DIRECT via office LAN 172.16.200.184); tcp/3389 to
100.99.180.19 over the tailnet = REFUSED. Laptop recommendation: scope the allow rule to the
Tailscale range only (100.64.0.0/10), never LAN/public. Test sequence after enable: laptop
`mstsc /v:100.99.180.19` (same-LAN direct), then an off-LAN variant (phone-hotspot laptop or
cellular phone) to prove the remote path.

## Box-side ground truth (MSTR~Z, read-only, 20:18Z — nothing changed)

| surface | state |
|---|---|
| `fDenyTSConnections` | **1 = RDP DISABLED** — this alone explains the REFUSED probe |
| NLA (`RDP-Tcp UserAuthentication`) | 1 (on — keep) |
| TermService | Stopped, StartType Manual (starts on demand when RDP enabled) |
| Firewall "Remote Desktop" group | 3 builtin rules present, **all Enabled=False**, Profile Any, UNSCOPED (any remote address) |
| Other 3389 rules | none |
| Tailscale | interface `Tailscale` 100.99.180.19, NetworkCategory Private, service Running, peer andrew 100.96.167.100 |

## Planned change (STAGED ONLY — executes on Andrew's word at console, act is his+ours)

1. Enable RDP: `Set-ItemProperty 'HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server' fDenyTSConnections 0`
   (raw registry path does NOT auto-enable firewall rules — so ingress stays exactly what we open in step 2).
2. Scoped ingress, tailnet ONLY (per laptop rec, agreed):
   `New-NetFirewallRule -DisplayName 'RDP - Tailscale tailnet only (TCP-In)' -Direction Inbound -Protocol TCP -LocalPort 3389 -RemoteAddress 100.64.0.0/10 -Action Allow`
   Builtin unscoped "Remote Desktop" group rules stay DISABLED — LAN/public 3389 remains closed.
3. Keep NLA on. Verify TermService starts; verify effective exposure = tailnet only
   (`Test-NetConnection` from laptop LAN-side should still REFUSE if we bind tighter later; the
   scoping control is the RemoteAddress predicate).
4. Andrew's test: `mstsc /v:100.99.180.19` same-LAN, then off-LAN variant for the remote path.

**Rollback:** delete the one named rule + set `fDenyTSConnections` back to 1 — two commands,
same window.

**Recorded by:** 0.0.0_AB_MSTR~Z, session f155df1b. Broadcast: laptop MSTR is the relayer
(holds it); site-Z live fabric = BG seat, notified via MCP same turn. No site-Z COO/CTO live.

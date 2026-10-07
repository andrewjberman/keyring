# ANDREW-DIRECT 2026-10-07 ~13:3xZ (1.0.0_SA_CTO terminal) -- Andrew runs administrator commands on the Dells himself

## His words, VERBATIM

> "I can run admin on the Dell boxes, if there is something that they need, have MSTR write both of them with the command line command and I will run it in an escalated shell./"

## Scope, as written (no wider, no narrower)

- WHO runs it: Andrew, in an elevated shell, on dell1 and dell2.
- HOW it reaches him: `0.0.0_AB_MSTR` writes both Dells the command-line command.
- WHEN: "if there is something that they need".
- It does not grant any agent elevation on a Dell, and it names no specific command.

## What prompted it

This seat's ruling on `2.0.0_SA_COO~C` msg 106261 (the bun no-egress measure on the Dells runs behind a temporary Windows Firewall
outbound block on bun.exe) said a Dell whose manager cannot add a firewall rule does not run the measure.

## First use (this seat's act, same turn)

Asked of `0.0.0_AB_MSTR`: write each Dell the three lines for Andrew's elevated shell, with that Dell's own resolved bun.exe path
filled in by its manager (an elevated shell may not share the seat's PATH):

1. Add: `New-NetFirewallRule -DisplayName "opal-bun-measure-block" -Direction Outbound -Program "<that Dell's bun.exe path>" -Action Block`
2. Show: `Get-NetFirewallRule -DisplayName "opal-bun-measure-block" | Format-List DisplayName,Enabled,Direction,Action`
3. Remove, after the measure reads back: `Remove-NetFirewallRule -DisplayName "opal-bun-measure-block"`

Between 2 and 3 the Dell's seat runs `python org/devices/kit_bun_no_egress.py selfcheck` and
`python org/devices/kit_bun_no_egress.py measure --loopback-registry-only --out <file>` (commit 3b95b7c3aa).

**Broadcast:** to `0.0.0_AB_MSTR` same turn. **Push state:** stated in the commit report.

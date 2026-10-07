# ANDREW-DIRECT 2026-10-07 ~05:41Z -- push the /freshness dev-only change to portal DEV; and he RDPs to site Z daily from "rc"

Given at the `0.0.0_AB_MSTR~Z` terminal (site Z), in-session. Three messages.

## Verbatim

~05:35Z: "if we run the RDP command on sitez, would that lock out littledog from using RDP or could they still use
splashtop?"

~05:40Z: "i use RDP to this device daily from the "rc" tailnet device"

~05:41Z: "also yes you can use you can push the dev-only change to portal DEV"

## The push (done on that word)

- Candidate: portal `8ddfe409` (AMGT_RESAPP AMGT-ba-27; `2.0.0_SA_COO~Z` msg 30642), CTO-approved @d18b424454. A
  fast-forward over origin DEV `659104f4`; 5 files, +324/-250. `src/App.tsx` gains `requiresDev: true` on the nav entry
  and `requireDev` on the route.
- Result: origin DEV `659104f4` -> `8ddfe409` (ls-remote read 05:4xZ). PROD unchanged at `ab3191d0`.
- Not covered by this word: any PROD promote. On PROD the page is still visible to every internal user until one runs.

## RDP facts read on site Z at ~05:40Z (unelevated)

- A custom inbound rule already exists and is enabled: "RDP - Tailscale tailnet only (TCP-In)", action Allow, remote
  address 100.64.0.0/255.192.0.0 (the tailnet range, the same set as 100.64.0.0/10).
- The three built-in "Remote Desktop" group rules are disabled, remote address Any.
- `rc` is 100.98.173.75, inside that range. Splashtop Remote Service and N-able Take Control are installed and running.

## Scope as read (surfaced, not adjudicated)

- The RDP messages are questions and a fact about his own access; they are not read as an order to apply or to skip
  the firewall command. That stays his act (ruling 2026-10-06 ~23:45Z, card 5 (a)).

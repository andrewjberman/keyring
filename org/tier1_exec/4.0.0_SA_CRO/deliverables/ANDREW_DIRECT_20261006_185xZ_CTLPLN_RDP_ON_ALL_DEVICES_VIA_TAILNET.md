# Andrew-direct, 2026-10-06 ~18:5xZ (2:5x PM Eastern), at the 4.0.0_SA_CRO terminal -- VERBATIM

Channel: typed by Andrew into the 4.0.0_SA_CRO (base) session while this seat was finishing the four-box census and plan.

> BY the way, something that needs to be included in the NFRA_CTLPLN is that we need RDP on all devices accessible via
> tailnet

A second message, minutes later, VERBATIM:

> When you finish your docs here, I want to make sure that is featured, then i want you to go through the NFRA_CTLPLN
> and identify if that is already covered, if it is not it is going to need to be. Because we are going to need to have
> that RDP ability from any device in the tailnet, namely the macbook

## Check result (this seat, ~19:0xZ)

NOT covered: the NFRA_CTLPLN PRD, STATUS.md, `org/devices/DEVICES.json`, the brief and the proposal mention RDP, Remote
Desktop, Tailscale or the tailnet zero times. MEASURED from the laptop: the tailnet holds the laptop (100.96.167.100),
site Z (100.99.180.19), the MacBook (100.98.173.75), an offline iPhone and a device named `muse`; port 3389 answers over
the tailnet on the laptop and on site Z. The Dells are not on it. Featured in
`docs/briefs/four-box-acceleration-plan-20261006.md` section 3a.

## What it states (as written, not widened)

NFRA_CTLPLN gains a requirement: Remote Desktop (RDP) on every device -- laptop, site Z, dell1, dell2 -- reachable over
the tailnet (the Tailscale private network), from any device on the tailnet, the MacBook first. It is an addition to the confirmed endpoint, so it goes to `1.0.0_SA_CTO`
as an endpoint change. Not stated by him, and so not decided here: who may connect, whether RDP is reachable only over
the tailnet (never the public internet), and whether it is part of a box's bring-up (round 2) or later.

## Routing

One line to `1.0.0_SA_CTO` naming this record. Carried into `docs/briefs/four-box-acceleration-plan-20261006.md`
section 3 as a bring-up step.

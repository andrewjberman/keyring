# ANDREW_DIRECT 2026-10-20 ~15:27Z -- NFRA_FIDUPL: Andrew expects to RDP into the box to hand-seed the sign-in

- **Channel:** in-session, Claude Code terminal, dell1, to `4.0.0_SA_CRO~FIDELITY`
- **Time:** 2026-10-20 ~15:27Z (11:27 AM ET)
- **Context:** said in reply to the CRO's REC (c) that he hand-seed a device-trusted session on the box's browser.

## Verbatim

> Yes I need to RDP into it most likely

## Status -- likely moot (surfaced, not adjudicated)

Minutes after this, `1.0.0_SA_CTO~DELL1` msg 8683 relayed the COO's real cause of the `redirect-info` 400: the stored
Wealthscape username and password were saved **wrapped in angle brackets** (Validation Failure 0102;
`org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/2.0.0_SA_COO~P1/FU-x-1_credential_shape_finding.md`). The brackets came
from the CRO's own example `{"username": "<Wealthscape ID>", "password": "<password>"}`, taken literally. So the
sign-in failure was a credential-shape bug, not yet a device check. **A hand-seed via RDP is likely NOT needed.**

Two facts for the decision if a hand-seed is still wanted after the secret is rewritten:
1. The box `i-028e830f7226cc685` is **Linux/UNIX** (t3.medium), so native Windows RDP does not attach; it needs xrdp or
   a VNC, or a Windows box.
2. Fidelity's device layer (ThreatMetrix in the capture) probes local RDP/VNC/TeamViewer ports. A remote-desktop
   listener that is up during an automated login run is exactly what it flags, so any such service should be off during
   the morning runs. This is the CTO's design call.

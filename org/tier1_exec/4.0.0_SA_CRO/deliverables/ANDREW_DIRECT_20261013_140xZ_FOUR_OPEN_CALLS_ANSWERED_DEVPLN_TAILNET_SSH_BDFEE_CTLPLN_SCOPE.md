# Andrew-direct 2026-10-13 ~14:0xZ (laptop, 4.0.0_SA_CRO terminal) -- four open calls answered

Answering the CRO's `/open-calls` frame of ~14:02Z (cluster read: 13 open, 1 fork + 12 acts; plus three NFRA_CTLPLN decisions
from the 2026-10-13 re-grade `org/tier1_exec/3.0.0_SA_CVO/deliverables/NFRA_CTLPLN_FWD_REGRADE_20261013.md` @69e690cebf).

## VERBATIM

> "1.) Yes let's get this brief sorted and folded in as a laptop project NFRA_DEVPLN. I want it separated from CTLPLN because
> CTLPLN is getting too large and there are many goals included in CTLPLN that we need to parse out and get moving because CTLPLN
> work on this box has completely drawn to a close. I will ask you to analyze why this is and where we can make progress there
> after addressing these calls. 2.) "muse" also needs to be able to remote into laptop. Currently we have rdp access from "rc"
> into laptop so that is acceptable there, however having global connected ssh would be very helpful for various control plane
> ops from "rc" "muse" and "cloud-local" (laptop). The key with ssh is that we want ssh to be functional within tailnet devices
> only, no external ssh available nor any external rdp available (aside from IT services like splashtop). 3.) Yes that is fine.
> 4.) Recs approved. One clarification is needed. The "bid" is not for active registered projects, it is for ad hoc bug fixes
> and etc that come in over teams/outlook via the COMMS_ASSIST channel, which needs to be approved at my discretion over that
> COMMS_ASSIST channel."

## Applied

| call | Andrew's answer | route |
|---|---|---|
| 1. portal DEV -> PROD promote | The per-box portal DEV approval work becomes its own laptop project, **NFRA_DEVPLN**, separate from NFRA_CTLPLN. The CRO's brief is its L1. The whole-DEV promote holds until it lands (the REC was not refused). The CTLPLN stall analysis is a later ask. | CRO writes the brief (`/brief-create`); `1.0.0_SA_CTO` runs L2/L3 (register NFRA_DEVPLN, placement laptop) |
| 2. laptop SSH | Neither (a) nor (b) as offered. SSH works between tailnet devices only: from "rc", "muse" and "cloud-local" (the laptop) for control-plane ops, and "muse" must be able to remote into the laptop. No SSH or RDP from outside the tailnet, except IT remote-support services such as Splashtop. RDP from "rc" into the laptop stays. | `1.0.0_SA_CTO`: an ENDPOINT change to NFRA_CTLPLN FWD-27 (and FWD-14's reach), Andrew's word above |
| 3. BD fee tool (site Z `sitez-20261011T224736Z-1b36`) | Yes: admit the 2 unprofiled callers by profile and grant, then ship the deny. | relayed via `0.0.0_AB_MSTR` to site Z's `1.0.0_SA_CTO~Z` / `2.0.0_SA_COO~O`, who close the row on this record |
| 4. NFRA_CTLPLN scope | Recs approved: keep FWD-11, park FWD-9, drop FWD-13 as written. Clarification: the "bid" is for ad hoc bug fixes and similar work arriving over Teams/Outlook through COMM_ASSIST, not for registered projects, and its placement is approved at Andrew's discretion over the COMM_ASSIST channel. | `1.0.0_SA_CTO`: PRD addendum (FWD-9 parked, FWD-13 re-scoped or moved to COMM_ASSIST on this clarification) |

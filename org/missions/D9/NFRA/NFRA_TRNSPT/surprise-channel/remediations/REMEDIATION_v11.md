# NFRA_TRNSPT: remediations, round 23

<sweep_watermark>2026-10-12T17:16Z</sweep_watermark>

Round 23 slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-12T17:16Z. L8 input: `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/2.0.0_SA_COO~T2/R23_CLOSE.md`
(blob ff8aae793c, msg 6434). No judgment criterion. Follows ADJUDICATION_v15.
Graduated, round label v24: 4 rows, OPEN. ARMED: 0. Still OPEN where it stands: D2-S15 (BLOCKING, REMEDIATION_v10, owner
`1.0.0_SA_CTO~DELL2`): the 4 Monday meetings read_refused again and research_meeting refused on every fire 13:00Z-17:00Z today.
Carried by the close record, not rows (the CTO's FWD grades): FWD-3's wording for the 4 Monday meetings; the draft route's first live
`COMMENTARY-POST` and 200, still UNEXERCISED LIVE (post_census reads 0 drafts since the switch). A scheduled LANDING run is now measured
(row D2-S34: 14:00Z, 239 MB of 1024 MB), so the decomposition's memory bar on a landing run is read.

```json
[
 {
  "id": "NFRA_TRNSPT-D2-S25",
  "project": "NFRA_TRNSPT",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The second reader of the transcripts tier trusts IAM user Opal_Terminal alone; its one Active key, minted 2026-07-10, has no recorded use. The parked FWD-8 ADMITTED read depends on a machine holding that key.",
  "evidence": ["investigation row NFRA_TRNSPT-D2-S25", "CTO msg 4290"],
  "remedy": "Andrew's word on where the key lives (or that it is rotated or deactivated); FWD-8's ADMITTED read follows it. Nobody acts on the key without his word.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v24",
  "remediation": {"state": "OPEN", "owner": "1.0.0_SA_CTO~DELL2", "round": "v24"},
  "closed": false
 },
 {
  "id": "NFRA_TRNSPT-D2-S27",
  "project": "NFRA_TRNSPT",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "comp-iam answers 'No role matching' for an IAM role whose Terraform name is computed (a local from NAMES.json), which is the form LGIC rule 30 requires. It fails silent, and the blind set grows with each canon-conformant role.",
  "evidence": ["investigation row NFRA_TRNSPT-D2-S27"],
  "remedy": "comp-iam resolves computed names (locals and jsondecode), or cross-checks against its live census and says when a name was skipped. A tool order for comp-iam's owner; this project only routes it.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v24",
  "remediation": {"state": "OPEN", "owner": "1.0.0_SA_CTO~DELL2", "round": "v24"},
  "closed": false
 },
 {
  "id": "NFRA_TRNSPT-D2-S29",
  "project": "NFRA_TRNSPT",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The gateway's OneDrive search returns none of five files a folder listing shows in the same drive, so its zero is not an absence; no file tool reads another user's drive.",
  "evidence": ["investigation row NFRA_TRNSPT-D2-S29", "CTO msg 4439"],
  "remedy": "NFRA_OPLGTW (site Z) states the search tool's coverage or fixes it; until then no consumer reads a search zero as 'no such file'. Routed cross-fabric by the CTO.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v24",
  "remediation": {"state": "OPEN", "owner": "1.0.0_SA_CTO~DELL2", "round": "v24"},
  "closed": false
 },
 {
  "id": "NFRA_TRNSPT-D2-S32",
  "project": "NFRA_TRNSPT",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "safe-apply's CROSSBOX-DEPLOY limb printed verdict=STOP on a fully paired code-only apply: its OPEN-DEPLOY arm unions sentinels from 69 worktree HEADs (2 of 3 hits were ledgers closed at shared HEAD) and its OPEN-CALL arm matches the bare token 'transcripts'. Under ENFORCE the act would have been refused.",
  "evidence": ["investigation row NFRA_TRNSPT-D2-S32"],
  "remedy": "The limb's owner discounts a sentinel absent at shared HEAD and matches open calls on roots, not tokens, before the limb moves to ENFORCE.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v24",
  "remediation": {"state": "OPEN", "owner": "1.0.0_SA_CTO~DELL2", "round": "v24"},
  "closed": false
 }
]
```

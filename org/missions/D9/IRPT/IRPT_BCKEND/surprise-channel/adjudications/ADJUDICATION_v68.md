# IRPT_BCKEND: CVO adjudication, round 167 (workstream ~P)

<sweep_watermark>2026-10-12T21:08Z</sweep_watermark>

L8 compile by `3.0.0_SA_CVO` (seated on dell2), 2026-10-12T21:08:00Z, on msg 6555 (`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_167_P_DRAIN_END_20261012.md`, blob 0322ee98d6; six orders IB-pr-481 to IB-pr-486 on PRD
ADDENDUM v0.51 and the round-166 analysis section 3a). No judgment criterion.
4 new rows and 3 earlier rows dismissed below; 1 graduates in `remediations/REMEDIATION_v44.md` (D2-W337-S2, disarmed: the digest gate fails
safe). ARMED after: 0.

```json
[
 {
  "id": "IRPT_BCKEND-C-S350",
  "project": "IRPT_BCKEND",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-12T21:08:00Z",
  "one_line": "Round 167 (~P). Dismissed: Round 167's new rows. D2-S110 (BLOCKING; the check refused its own required key, amended @193a3e10ed, and a record with an SQS url still FAILs); D2-W337-S1 (the face named a READ file the folder never held; the record was read); D2-W338-S1 (three portal tests fail at the DEV head in files the order did not touch; the issuer reproduced them with the DEV-head adapter, so they are not this change's); D2-S111 (the disarm owner's evidence for D2-W337-S2, carried by that row's remediation).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_BCKEND-D2-S110",
   "IRPT_BCKEND-D2-W337-S1",
   "IRPT_BCKEND-D2-W338-S1",
   "IRPT_BCKEND-D2-S111"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
  "world_is": "IB-pr-481 to IB-pr-486 are complete; round-close-check --round 167 --workstream ~P reads MAY-CLOSE (6 orders, judgment 0). Nothing applied: irpt-performance-adapter reads kMB8xCI9... LastModified 14:11:01Z (this seat, 21:0xZ). ARMED after this compile: 0.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigation rows D2-S110, D2-W337-S1, D2-W338-S1, D2-S111",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_167_P_DRAIN_END_20261012.md (blob 0322ee98d6, msg 6555)",
    "this seat's reads 2026-10-12T21:0xZ: six order files <status>complete</status>; merge-base --is-ancestor HEAD yes for b66c5435ec, b4b05687cd, 58b92e9e35, e8c52f9379, 1e42cbef6f, fe0e518aaf, 193a3e10ed, 9bc2c883f6; git diff --stat c16bf9d7bb^ HEAD on both schema copies: empty",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~337/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-482.md lines 46 and 51"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A check defect closed by amendment, a face wording error, failures that predate the change, and a disarm record carried by its row."
 },
 {
  "id": "IRPT_BCKEND-C-S351",
  "project": "IRPT_BCKEND",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-12T21:08:00Z",
  "one_line": "Round 167 (~P). Dismissed: Earlier rows closed. D2-W334-S2 (BLOCKING): both PerformanceReport.schema.json copies are restored to the frozen v1 bytes (IB-pr-481 @b66c5435ec; this seat's `git diff c16bf9d7bb^ HEAD` on both files reads empty), and v0.50's schema bullet is withdrawn. D2-W331-S2 (BLOCKING): the IB-pr-482 never-widen packet prints the moves beside the reach (orion SI 750 of 894, YTD 76 of 200, QTD 7 of 7, 1Y 106 of 240; 49F equal), packet line 46 read by this seat. D2-W333-S1: ycharts/research rides the resident package (IB-pr-485 @1e42cbef6f), and the live host's bindings carry no commentary queue (IB-pr-486, read 20:14:28Z), so nothing is broken live.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_BCKEND-D2-W334-S2",
   "IRPT_BCKEND-D2-W331-S2",
   "IRPT_BCKEND-D2-W333-S1"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
  "world_is": "IB-pr-481 to IB-pr-486 are complete; round-close-check --round 167 --workstream ~P reads MAY-CLOSE (6 orders, judgment 0). Nothing applied: irpt-performance-adapter reads kMB8xCI9... LastModified 14:11:01Z (this seat, 21:0xZ). ARMED after this compile: 0.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigation rows D2-W334-S2, D2-W331-S2, D2-W333-S1",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_167_P_DRAIN_END_20261012.md (blob 0322ee98d6, msg 6555)",
    "this seat's reads 2026-10-12T21:0xZ: six order files <status>complete</status>; merge-base --is-ancestor HEAD yes for b66c5435ec, b4b05687cd, 58b92e9e35, e8c52f9379, 1e42cbef6f, fe0e518aaf, 193a3e10ed, 9bc2c883f6; git diff --stat c16bf9d7bb^ HEAD on both schema copies: empty",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~337/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-482.md lines 46 and 51"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Remedied by merged code and a live read."
 }
]
```

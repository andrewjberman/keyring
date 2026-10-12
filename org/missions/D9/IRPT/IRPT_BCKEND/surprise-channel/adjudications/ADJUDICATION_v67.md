# IRPT_BCKEND: CVO adjudication, round 166 (workstream ~P)

<sweep_watermark>2026-10-12T19:58Z</sweep_watermark>

L8 compile by `3.0.0_SA_CVO` (seated on dell2), 2026-10-12T19:58:00Z, on msgs 6511 and 6513 (`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_166_P_DRAIN_END_20261012.md`, blob 6f7a87658e; five orders IB-pr-476 to
IB-pr-480 on the CTO's round-166 analysis, msg 6503). No judgment criterion.
3 new rows and 5 earlier rows dismissed below; 3 graduate in `remediations/REMEDIATION_v43.md`, 2 BLOCKING. ARMED after: 0 (D2-W328-S1 is
repaired by merged code that no release has carried).

```json
[
 {
  "id": "IRPT_BCKEND-C-S348",
  "project": "IRPT_BCKEND",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-12T19:58:00Z",
  "one_line": "Round 166 (~P). Dismissed: Round 166's new rows. D2-W334-S3 (BLOCKING; the check validated the fixture's wrapper, amended @90e1fc439f); D2-W331-S1 (a test fixture used PRICE_MISSING, a status the producer never writes; under C-CHAINCLAIM item 3 it reads inferred, and no assertion was weakened); D2-W334-S1 (the two schema copies differ in 49 lines; folded into D2-W334-S2, which graduates).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_BCKEND-D2-W334-S3",
   "IRPT_BCKEND-D2-W331-S1",
   "IRPT_BCKEND-D2-W334-S1"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
  "world_is": "IB-pr-476 to IB-pr-480 are complete; round-close-check --round 166 --workstream ~P reads MAY-CLOSE (5 orders, judgment 0). ARMED after this compile: 0.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigation rows D2-W334-S3, D2-W331-S1, D2-W334-S1",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_166_P_DRAIN_END_20261012.md (blob 6f7a87658e, msgs 6511 and 6513)",
    "this seat's reads 2026-10-12T19:5xZ: the five order files read <status>complete</status>; merge-base --is-ancestor HEAD yes for 6a875f0dfd, 4a5b22e661, 386a9276ed, c16bf9d7bb, 2f37f16b65, 90e1fc439f, 9216f0ea15"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A check defect closed by amendment, a fixture the contract made wrong, and a row carried by a graduating row."
 },
 {
  "id": "IRPT_BCKEND-C-S349",
  "project": "IRPT_BCKEND",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-12T19:58:00Z",
  "one_line": "Round 166 (~P). Dismissed: Earlier rows closed by round 166's merged code or measure, each drain an ancestor of HEAD (this seat's read). D2-W328-S1 (ARMED in REMEDIATION_v42): a challenged stored-bundle probe now ends the capture with no fresh sign-in (IB-pr-477 @4a5b22e661; arm (a) 0 credential reads, 0 sign-in POSTs, 0 secret writes); no released byte ever carried the defect, so the disarm is the merge. D2-W328-S2: the pair gate is `discriminating !== true` (same order). D2-W309-S2: the packager reads `commentary_ref` from the sibling attribute (IB-pr-478 @386a9276ed); its successor is D2-W333-S1. D2-W315-S3: no reader of the landed prices store exists under investor-reporting/ (IB-pr-480 @2f37f16b65, 664 files, 0 hits, positive control the writer), so it is retired as a source, as v0.49 ruled. D2-W321-S2: its premise is false; all three absences ALWAYS hold for a holdings answer, so PARTIAL on every holdings answer is the true statement (IB-pr-476 @6a875f0dfd, read from code).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_BCKEND-D2-W328-S1",
   "IRPT_BCKEND-D2-W328-S2",
   "IRPT_BCKEND-D2-W309-S2",
   "IRPT_BCKEND-D2-W315-S3",
   "IRPT_BCKEND-D2-W321-S2"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
  "world_is": "IB-pr-476 to IB-pr-480 are complete; round-close-check --round 166 --workstream ~P reads MAY-CLOSE (5 orders, judgment 0). ARMED after this compile: 0.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigation rows D2-W328-S1, D2-W328-S2, D2-W309-S2, D2-W315-S3, D2-W321-S2",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_166_P_DRAIN_END_20261012.md (blob 6f7a87658e, msgs 6511 and 6513)",
    "this seat's reads 2026-10-12T19:5xZ: the five order files read <status>complete</status>; merge-base --is-ancestor HEAD yes for 6a875f0dfd, 4a5b22e661, 386a9276ed, c16bf9d7bb, 2f37f16b65, 90e1fc439f, 9216f0ea15"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Remedied by merged code, or closed by a measure that answers the row."
 }
]
```

# IRPT_BCKEND: CVO adjudication, round 187 (workstream ~P)

<sweep_watermark>2026-10-14T01:36:31Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-14T01:36:31Z, on msg 7416 (`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_187_P_DRAIN_END_20261014.md @754b9f4570`). Two orders, 3 of 3 PASS each, no judgment
criterion; nothing applied. This seat re-ran IB187-1-AC1 to AC3: all PASS. 6 rows dismissed below; nothing graduates while IB-pr-497 is
parked. For the CTO: Cottonwood can produce all 19 activity columns, Inflection 17 (no lot table); the producer reads one source today.

```json
[
 {
  "id": "IRPT_BCKEND-C-S371",
  "project": "IRPT_BCKEND",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-14T01:36:31Z",
  "one_line": "Round 187 (~P), no judgment criterion. Dismissed: D2-W370-S1 (the issuer's docstring step the check's hunk-label rule rejects; documented in run_backfill's docstring instead, no code consequence); D2-W371-S1 to -S4 and D2-S157 (readings carried to the CTO for the multi-firm producer build: Inflection's transactions in two places with two writers and two column sets, three account key spaces not compared, Inflection's realized and in-kind columns ABSENT for want of a lot-level table). Stay open with the issuer: D2-S152, D2-S155, D2-S156 (the IR Holdings class rule, round 188), D2-S145 to -S147, D2-S150, D2-S153.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_BCKEND-D2-W370-S1",
   "IRPT_BCKEND-D2-W371-S1",
   "IRPT_BCKEND-D2-W371-S2",
   "IRPT_BCKEND-D2-W371-S3",
   "IRPT_BCKEND-D2-W371-S4",
   "IRPT_BCKEND-D2-S157"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
  "world_is": "TO-IB-pr-523 and TO-IB-pr-524 are complete (order files read); merges 0009c27ae2 and 8dfd755758 on HEAD. A build and a read only: irpt-49f-reporting-gold-lambda unchanged live per the packet; nothing uploaded, applied or invoked. Two person-reads still owed (the catalogue, the export). IB-pr-497 parked; IB-pr-456 waits on Andrew's PROD execution ID. Still ARMED with the issuer: W349-S1, W361-S1, W348-S2, W368-S2.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigation rows D2-W370-S1, D2-W371-S1, D2-W371-S2, D2-W371-S3, D2-W371-S4, D2-S157",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_187_P_DRAIN_END_20261014.md @754b9f4570 (msg 7416)",
    "this seat's run 2026-10-14T01:36 of IB187-1-AC1 to AC3 from TO-IB-pr-523 on the shared tree: all PASS (96 tests pass and the change is confined; the lots-only arm touches neither the returns nor the class emit; the default path is unchanged and malformed stage values are refused by name)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "An issuer wording defect with no code consequence, and source readings carried to the producer build."
 }
]
```

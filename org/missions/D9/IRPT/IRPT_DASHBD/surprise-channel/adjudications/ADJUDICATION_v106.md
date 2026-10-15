# IRPT_DASHBD: CVO adjudication, round 138 (workstream B-49F, ~D2): the households claim of the report-build handler

<sweep_watermark>2026-10-15T21:20Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T21:20Z, on msg 8662 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND138_141_B49F_DRAIN_END_20261015.md` @90ac6e0037, blob 55a406ca98; one packet covers rounds 138-141, adjudicated as v106-v109, one per round). Graded by this lane under rule 5 of `CTO_RULING_DELL2_IRPT_DASHBD_FOUR_WORKSTREAMS_AT_ROUND_114_20261015.md` (CTO msg 8009). One order, TO-DB-b-271 (WORLD by its infra path; worker ~220; merged @f25b913caf). No judgment criterion. Re-run here: DB138-1-AC1..AC3, 3 of 3 PASS (rc 0); round-close MAY-CLOSE. The struck DB118-3-AC3 still FAILS (rc 1), unmet. No remediation row.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S43",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T21:20:00Z",
  "one_line": "Round 138 B-49F: each filled day's object carries households_as_of and households_claim held in its parquet schema metadata, with the columns unchanged; a built day states the claim, the date, accounts_dropped and households_no_rows; no id reaches the output. 3 of 3 PASS re-run, 56 handler tests. This is the code that round 139 deployed (its handler.py equals reporting-gold-cot/handler.py at 9369b4ffd2; see v107). Row D2-W220-S1 (one earlier exact-GET assertion moved from 2 to 3 by the mandated re-read) is inert, accepted.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-W220-S1"
  ],
  "spec_asserts": "Spine L9/L10: a criterion is re-run; A_VALUE_MUST_CARRY_ITS_CLAIM (the households membership is held, not measured, and says so).",
  "world_is": "The households claim is in the handler and in the deployed objects (v107). FWD-1's thread is not met.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T21:0xZ: DB138-1-AC1..AC3 PASS rc 0",
    "investigation row D2-W220-S1",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND138_141_B49F_DRAIN_END_20261015.md blob 55a406ca98 (msg 8662)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "One inert worker row."
 }
]
```

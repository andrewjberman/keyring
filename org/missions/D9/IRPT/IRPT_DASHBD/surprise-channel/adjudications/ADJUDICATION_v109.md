# IRPT_DASHBD: CVO adjudication, round 141 (workstream B-49F, ~D2): the chain cap of the report-build handler

<sweep_watermark>2026-10-15T21:20Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T21:20Z, on msg 8662 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND138_141_B49F_DRAIN_END_20261015.md` @90ac6e0037, blob 55a406ca98; one packet covers rounds 138-141, adjudicated as v106-v109, one per round). Graded by this lane under rule 5 of `CTO_RULING_DELL2_IRPT_DASHBD_FOUR_WORKSTREAMS_AT_ROUND_114_20261015.md` (CTO msg 8009). One order, TO-DB-b-274 (WORLD by its infra path; worker ~222; merged @24b4b16305). No judgment criterion. Re-run here: DB141-1-AC1..AC3, 3 of 3 PASS (rc 0); round-close MAY-CLOSE. The re-pointed round-131 criteria DB131-1-AC1..AC3 now PASS here (the red-by-design state v101 named is closed). The struck DB118-3-AC3 still FAILS (rc 1), unmet. No remediation row.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S46",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T21:20:00Z",
  "one_line": "Round 141 B-49F: every chain carries a budget (chain_left 0 to 9) in its self-invoke payload, refused before any call when bad. The probe drives a whole chain: from {} over 32 owed days it builds exactly 10 days and stops. 3 of 3 PASS re-run, 56 tests. REPO CODE ONLY: the deployed function holds round 138's handler without chain_left (v107, by content). The cap is not live until its own code-update pair (a safe-apply of a 0/1/0 plan) lands, which keeps D2-S95 ARMED. Rows: D2-W222-S1 (one assertion now reads the day key only) and D2-W222-S2 (budget zero with no ARN returns the present form) are inert, accepted. D2-S94 (~D2) disarms D2-S92 (the two-era splice), citing round 135's guard test that spans 2026-06-22 and 2026-07-10, refuses a mix with zero puts and reads NOT_SPANNED before the floor. GROUNDED for the report-build consumer: DB135-1-AC2 passes on the landed tree (v101). The CTO's analysis asked for exactly this test-backed disarm.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-W222-S1",
   "IRPT_DASHBD-D2-W222-S2",
   "IRPT_DASHBD-D2-S94"
  ],
  "spec_asserts": "Spine L9/L10: a criterion is re-run; a disarm is graded on its evidence; code is live only when deployed by its pair.",
  "world_is": "The chain cap exists in repo code and is not deployed. The round-131 probes are green again. D2-S92 is disarmed for its one consumer.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T21:0xZ: DB141-1-AC1..AC3 PASS rc 0; DB131-1-AC1..AC3 PASS rc 0",
    "deployed handler.py without chain_left (ADJUDICATION_v107)",
    "investigation rows D2-W222-S1, D2-W222-S2, D2-S92, D2-S94, D2-S95",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND138_141_B49F_DRAIN_END_20261015.md blob 55a406ca98 (msg 8662)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Two inert worker rows, and a test-backed disarm of D2-S92 that this seat re-checked. D2-S95 stays ARMED until the code-update pair."
 }
]
```

# IRPT_CUSTDY: CVO adjudication, round 6

<sweep_watermark>2026-10-07T14:5xZ</sweep_watermark>

Round 6 L8 compile by `3.0.0_SA_CVO` (seated on dell2), 2026-10-07 ~15:1xZ. L8 input: `org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/2.0.0_SA_COO~K2/IRPT_CUSTDY_ROUND_6_DRAIN_END_20261007.md @7f88b5be96` (msg 738). 3 of 3 orders complete and VALID:
CU-f-1 and CU-f-3 @65511fc814 (portal e355d193, not on DEV), CU-f-2 @0143c19ac1. 0 JUDGMENT criteria. 4 rows, all dismissed below. Clocks
advanced in place in REMEDIATION_v5: S10, W13-S2 and W12-S1 REMEDIATED and closed. ARMED: 0. Still OPEN: W1-S1, W4-S1, W9-S5. FWD-1 NOT
LIVE: hops 1-4 run on real data for all 18 granted accounts inside 120 s; hop 5 waits on IRPT_BCKEND's print kind and the template's DEV
landing (Andrew's word).

```json
[
 {
  "id": "IRPT_CUSTDY-C-S6",
  "project": "IRPT_CUSTDY",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-07T15:10Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "Round 6's four rows are dismissed: W14-S1 (the not-covered portal test builds its document inline), W14-S2 (the inherited tracer test, retired by CU-f-2), W14-S3 (the probe's cost was sequential silver reads, not a listing; fixed by prefetch and filter) and S12 (the round's real-run grade). S10, W13-S2 and W12-S1 are closed in place.",
  "adjudicates": [
   "IRPT_CUSTDY-W14-S1",
   "IRPT_CUSTDY-W14-S2",
   "IRPT_CUSTDY-W14-S3",
   "IRPT_CUSTDY-S12"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
  "world_is": "The suite on CLOUD is green with the tracer retired (this seat re-ran it: 147 passed, 0 failed), so S10 is REMEDIATED and closed. CU-f-1's real run puts each of the 4 not-covered accounts alone in its own document with a non-empty reason, and validate_document admits 14 of 14; W13-S2 is REMEDIATED and closed. CU-f-3 bounds the anchor probe: the issuer's timed re-run reads 85.9 s within 120 (before: 133-194 s), with SI OK on 14 of 14 and the same labels; W12-S1 is REMEDIATED and closed. The 120 s margin is thin on dell2's network (62-86 s); the rest of hop 3 (build_context ~25-30 s, returns load ~14-22 s) is the analysis's if scheduling needs more.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigation rows IRPT_CUSTDY-W14-S1, IRPT_CUSTDY-W14-S2, IRPT_CUSTDY-W14-S3, IRPT_CUSTDY-S12",
    "org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/2.0.0_SA_COO~K2/IRPT_CUSTDY_ROUND_6_DRAIN_END_20261007.md @7f88b5be96",
    "pytest -q data/assets/scripts/gold/irpt_custody/tests: 147 passed, 0 failed, 1 xfailed (this compile's read, dell2 CLOUD, 2026-10-07 ~15:0xZ)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A test-setup note, a retired test, a measured premise correction with its fix, and the round's grade record."
 }
]
```

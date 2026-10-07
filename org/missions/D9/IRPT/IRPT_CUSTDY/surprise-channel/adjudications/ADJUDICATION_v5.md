# IRPT_CUSTDY: CVO adjudication, round 5

<sweep_watermark>2026-10-07T13:1xZ</sweep_watermark>

Round 5 L8 compile and L9 by `3.0.0_SA_CVO` (seated on dell2), 2026-10-07 ~13:2xZ. L8 input: `org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/2.0.0_SA_COO~K2/IRPT_CUSTDY_ROUND_5_DRAIN_END_20261007.md @2e68ccd2d2` (msg 587). 2 of 2 orders complete and
VALID: CU-e-1 @5b85219599, CU-e-2 @8029bc6635 (portal 99addd80, not on DEV). L9: CU15-AC3 MET; grade file `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_CUSTDY_ROUND_5_L9_GRADE_20261007.md`. 6 rows: 3 dismissed
below, 3 graduated OPEN in `remediations/REMEDIATION_v5.md`. Clock advanced in place: W10-S1 (REMEDIATION_v4) REMEDIATED and closed. ARMED: 0.
FWD-1 NOT LIVE: hops 1-4 run on real data for all 18 granted accounts; the served render (hop 5) waits on IRPT_BCKEND's print kind and on
the template's DEV landing (Andrew's word). Still OPEN: W1-S1, W4-S1, W9-S5.

```json
[
 {
  "id": "IRPT_CUSTDY-C-S5",
  "project": "IRPT_CUSTDY",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-07T13:20Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "ROUND 5 L9: CU15-AC3 (C-SHAPE) MET, with a finding on the instrument (its BD deny list is not BD's real vocabulary). W13-S1 (the 4 unkeyed accounts: 0 found, 4 not held), W12-S2 (name_sources typed at file level) and S11 (the round's real-run grade) are dismissed; W10-S1 is closed in place.",
  "adjudicates": [
   "IRPT_CUSTDY-W13-S1",
   "IRPT_CUSTDY-W12-S2",
   "IRPT_CUSTDY-S11"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
  "world_is": "W13-S1 answers W10-S1: 39 Schwab silver tables, 8 identifiers per account, 0 matches, with a positive control classed FOUND through the same code; the 4 are NOT_HELD and carried as not_covered with that reason, so all 18 granted accounts are in the report data (14 SI OK). W12-S2 types an optional field to the real documents' shape. S11 records the close. W10-S1 (REMEDIATION_v4) REMEDIATED and closed: the question it put is measured. C-SHAPE: the contract's 45 keys share 6 generic words with a real BD record's 75 keys (accounts, fees, market_value, name, symbol, value) and none of BD's distinctive fields; the producer reads the custodian (grade file).",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigation rows IRPT_CUSTDY-W13-S1, IRPT_CUSTDY-W12-S2, IRPT_CUSTDY-S11",
    "org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/2.0.0_SA_COO~K2/IRPT_CUSTDY_ROUND_5_DRAIN_END_20261007.md @2e68ccd2d2",
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_CUSTDY_ROUND_5_L9_GRADE_20261007.md"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A measured answer to an open question, a typing note, and the round's grade record."
 }
]
```

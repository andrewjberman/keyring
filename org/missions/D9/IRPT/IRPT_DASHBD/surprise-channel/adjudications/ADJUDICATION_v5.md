# IRPT_DASHBD -- rounds 15 to 17 (workstream B) L8/L9 adjudication

<sweep_watermark>2026-10-07T07:36Z</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2), 2026-10-07 ~08:2xZ. L8 inputs: the drain-end packet `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUNDS_15_17_B_DRAIN_END_20261007.md` (@13ed122c56, by the dell2 successor `2.0.0_SA_COO~D2`; `2.0.0_SA_COO~P2`'s packet @9f647705c9 covers the same four orders and agrees, msg 54); and this seat's reads on dell2 (the _contracts and census suites re-run, routes.json and the api root's filter, git ls-files of the E3 records). 4 of 4 orders are terminal, merged and VALID: DB-b-23 @487429cb60,
DB-b-24 @28efce5b4d, DB-b-25 @98d439936a, DB-b-26 @0685c40ec0. 6 rows surfaced after the previous watermark 2026-10-04T23:59Z (W9-S1,
W9-S2, W9-S3, W10-S1, W12-S1, S26); 2 are dismissed by the row below; 4 graduate in remediations/REMEDIATION_v6.md: 3 REMEDIATED and
closed, 1 OPEN. ARMED before: 3 (W9-S1 BLOCKING, W9-S2, W9-S3); ARMED after: 0.

```json
[
 {
  "id": "IRPT_DASHBD-C-S16",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-07T08:25:00Z",
  "one_line": "S26 (2.0.0_SA_COO~D2's disarm record for W9-S1..S3) and W10-S1 (the E3 ruling's bearer line already named batch 248).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-S26",
   "IRPT_DASHBD-W10-S1"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
  "world_is": "S26's effect is carried on W9-S1, W9-S2 and W9-S3, which graduate REMEDIATED and closed in REMEDIATION_v6; this compile re-ran S26's two suites and read its two source facts. W10-S1 is a reading note: the order's text described an older bearer line, the worker rewrote only the bearer value to name batches 248 and 249, and the record is committed (DB-b-24 drained @28efce5b4d).",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigation row(s) IRPT_DASHBD-S26, IRPT_DASHBD-W10-S1",
    "pytest -q _contracts in infra/aws/lambda/investor-reporting: 190 passed; pytest -q _authz/tests/test_unguarded_census.py: 9 passed (this compile's read, dell2 CLOUD df7865f720, 2026-10-07 ~08:1xZ-08:2xZ)",
    "docs/contracts/investor-reporting/v1/routes.json: 21 routes, 19 DECLARED, 2 ROUTED_ELSEWHERE (the two reporting routes) (this compile's read, dell2 CLOUD df7865f720, 2026-10-07 ~08:1xZ-08:2xZ)",
    "infra/aws/terraform/investor-reporting/api/routes.tf:40-43 builds irpt_routes only from rows with status DECLARED (this compile's read, dell2 CLOUD df7865f720, 2026-10-07 ~08:1xZ-08:2xZ)",
    "git ls-files: deliverables/0.9.0_WK_IRPT_DASHBD~6/E3_SHAPE_RULING.json and BD_POPULATION_PULL_E3.json are tracked (this compile's read, dell2 CLOUD df7865f720, 2026-10-07 ~08:1xZ-08:2xZ)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A disarm record whose effect is carried on the rows it names, and a note on an order's wording with no hazard."
 }
]
```

# IRPT_DASHBD: remediations, round 70 (workstream B)

<sweep_watermark>2026-10-11T16:50Z</sweep_watermark>

Slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T16:50:24Z. Input: msg 5385 (round 70 fully drained @d7b1f1f4e2; records under deliverables/0.9.0_WK_IRPT_DASHBD~105 to ~108).
Graduated, round label v71: 2 rows, OPEN, INERT. Closed in place in REMEDIATION_v28, each on the issuer's re-run of its cell and not
re-run by this seat: D2-W103-S1 (row 3 with no valuation source is refused), D2-W103-S2 and D2-W102-S1 (contract prose and the build
manifest's text corrected).

**For the CTO's analysis:**
1. **The thresholds fix is built and not released** (row D2-W100-S3 stays open). The served manifests still carry the 24-key object;
   one daily returns manifest is confirmed, and how many carry it is not counted. A release, and a decision on the manifests already
   served, are yours.
2. **The tie-out:** 8 of the 90 remain unclassed, the classing is by rule, and two of its results sit against an earlier refutation
   (row D2-W108-S2).
3. FWD-11 and FWD-12 stay parked.

```json
[
 {
  "id": "IRPT_DASHBD-D2-W108-S1",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "DB-b-135: the reader ~35 reaches the custodian tables through the plan BD_POPULATION_PLAN_E3.json (the account-to-Black-Diamond-id map), and that file is no longer in the tree.",
  "evidence": [
   "investigation row IRPT_DASHBD-D2-W108-S1",
   "msg 5385 (round 70 fully drained @d7b1f1f4e2; records under deliverables/0.9.0_WK_IRPT_DASHBD~105 to ~108)"
  ],
  "remedy": "The account-to-custodian id plan is restored to the tree or its reader is given another route; without it the custodian tables cannot be reached for the tie-out.",
  "owner": "2.0.0_SA_COO~D2",
  "round": "v71",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~D2",
   "round": "v71"
  },
  "closed": false
 },
 {
  "id": "IRPT_DASHBD-D2-W108-S2",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "DB-b-135: of the 90, 51 hold the same dollars on both sides end to end and close under START or MID flow timing, which sits beside the DB-b-106 refutation of FLOW_TIMING on event-date sets; 31 more carry Black Diamond accrued income in their values and gains.",
  "evidence": [
   "investigation row IRPT_DASHBD-D2-W108-S2",
   "msg 5385 (round 70 fully drained @d7b1f1f4e2; records under deliverables/0.9.0_WK_IRPT_DASHBD~105 to ~108)"
  ],
  "remedy": "The 51 segments that close under START or MID flow timing are reconciled with the earlier refutation of flow timing, and the 31 carrying accrued income are read on the ledger sums the cell did not examine.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v71",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v71"
  },
  "closed": false
 }
]
```

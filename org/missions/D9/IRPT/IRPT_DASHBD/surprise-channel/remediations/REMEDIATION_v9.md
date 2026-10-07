# IRPT_DASHBD -- round 23 (workstream B) remediations

<sweep_watermark>2026-10-07T14:5xZ</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2), 2026-10-07 ~15:0xZ. L8 input: `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND23_B_DRAIN_END_20261007.md @980c56b3a6` (msg 734). 1 of 1 order (DB-b-35) terminal, merged and VALID
@a8df9a5880; 0 judgment criteria; LOCAL. 3 rows, all graduated OPEN here; none dismissed, so no ADJUDICATION file is written for this round.
ARMED: 0. FWD-4 is not shown by this round: 39 of 91 sampled windows miss the activity identity (W20-S2), and the passing window does not
move the realized term.

```json
[
 {
  "id": "IRPT_DASHBD-W20-S2",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Across 91 graded account-windows (100 accounts x 24 trading days, 2026-09-01..10-05), the activity identity (start value + contributions - withdrawals + realized + unrealized change + income = end value) ties within one cent on 52 and fails on 39: most by cents, a few by more, one account by about 1.1 million. The gaps are labelled GAP_ABOVE_ALLOWANCE and carried, never plugged; the cause is not diagnosed. AC1 passed on one named window whose realized gain, contributions and withdrawals are all 0, so it does not exercise the realized term.",
  "evidence": [
   "investigation row IRPT_DASHBD-W20-S2",
   "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND23_B_DRAIN_END_20261007.md @980c56b3a6",
   "pytest -q data/assets/scripts/gold/irpt_reporting/tests: 70 passed (this compile's read, dell2 CLOUD, 2026-10-07 ~15:0xZ)"
  ],
  "remedy": "Before these tables are released: read the ~1.1M account's window term by term against its transactions and lots, then classify the other 38 gaps (rounding over 24 days vs a missing term). Grade FWD-4 on a window that moves the realized term. A transaction type the activity rule does not sign is a cause to test first (the ADVI_COTBKF rebuild missed Cash in Lieu, row ADVI_COTBKF-D2-S24, on another firm's data).",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v24",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v24"
  },
  "closed": false
 },
 {
  "id": "IRPT_DASHBD-W20-S1",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The lot tables' source names and columns are typed in account_activity_lots.py because sources.json was outside the grant.",
  "evidence": [
   "investigation row IRPT_DASHBD-W20-S1",
   "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND23_B_DRAIN_END_20261007.md @980c56b3a6",
   "pytest -q data/assets/scripts/gold/irpt_reporting/tests: 70 passed (this compile's read, dell2 CLOUD, 2026-10-07 ~15:0xZ)"
  ],
  "remedy": "The release cell moves them into sources.json, as W18-S1's tokens were moved.",
  "owner": "2.0.0_SA_COO~D2",
  "round": "v24",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~D2",
   "round": "v24"
  },
  "closed": false
 },
 {
  "id": "IRPT_DASHBD-W20-S3",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The custodian's lot event ids repeat (131 distinct close_event_id over 726 realized lots), so both lot tables key on composites.",
  "evidence": [
   "investigation row IRPT_DASHBD-W20-S3",
   "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND23_B_DRAIN_END_20261007.md @980c56b3a6",
   "pytest -q data/assets/scripts/gold/irpt_reporting/tests: 70 passed (this compile's read, dell2 CLOUD, 2026-10-07 ~15:0xZ)"
  ],
  "remedy": "The contracts state the composite keys; a consumer joining on close_event_id alone would multiply rows. Closes when the contracts and one consumer read agree.",
  "owner": "2.0.0_SA_COO~D2",
  "round": "v24",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~D2",
   "round": "v24"
  },
  "closed": false
 }
]
```

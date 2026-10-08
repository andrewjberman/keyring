# IRPT_DASHBD -- round 25 (workstream B) remediations

<sweep_watermark>2026-10-07T19:4xZ</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2), 2026-10-07 ~20:3xZ. Graduated at this compile (ADJUDICATION_v10.md): 2 rows, both OPEN, round label v26.

```json
[
 {
  "id": "IRPT_DASHBD-W22-S3",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The lot tables gain basis_source member WASH_SALE_EXCLUDED_BASIS (METHOD_VERSION 3, SCHEMA_VERSION 1.2), and the lot contracts under org/standards/ do not list basis_source at all.",
  "evidence": [
   "investigation row IRPT_DASHBD-W22-S3",
   "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND25_B_DRAIN_END_20261007.md @7cadad7a87"
  ],
  "remedy": "The release cell adds basis_source and its members to the lot contracts before the tables are served.",
  "owner": "2.0.0_SA_COO~D2",
  "round": "v26",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~D2",
   "round": "v26"
  },
  "closed": false
 },
 {
  "id": "IRPT_DASHBD-W22-S5",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "classify_and_sum in the served account_return_daily.py raises on a repeated index label, before and after this round's None hardening.",
  "evidence": [
   "investigation row IRPT_DASHBD-W22-S5",
   "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND25_B_DRAIN_END_20261007.md @7cadad7a87"
  ],
  "remedy": "Read whether a served input can carry a repeated index label; if it can, the next reporting-gold release de-duplicates or refuses with a named reason, tested on the served layer's pandas.",
  "owner": "2.0.0_SA_COO~D2",
  "round": "v26",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~D2",
   "round": "v26"
  },
  "closed": true
 }
]
```

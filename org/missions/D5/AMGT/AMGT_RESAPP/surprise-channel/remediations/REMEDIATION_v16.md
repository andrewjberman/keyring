# AMGT_RESAPP -- surprise channel, REMEDIATION v16 -- Z-S11 disarm clock (citing row) and Z-S348

Author: 3.0.0_SA_CVO~Z. Round: v83. Fabric: site-z. Recorded: 2026-10-05T03:5xZ. **Reader:** `1.0.0_SA_CTO~Z`.

```json
[
 {
  "id": "AMGT_RESAPP-Z-C-S458",
  "project": "AMGT_RESAPP",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "Z-S11: the CRO harvester build and the round-5 rd-3/rd-4 orders collided on one write surface (one box and one lambda vs four harvesters on a box); its first remediation row was written INERT with no disarm block, so it could never be disarmed in place.",
  "evidence": [
   "adjudications/ADJUDICATION_v83.md#AMGT_RESAPP-Z-C-S458",
   "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S11",
   "task-orders AMGT_RESAPP.TO-AMGT-rd-3 and TO-AMGT-rd-4: last status superseded",
   "dc868af89c (2026-09-11T20:16Z, ancestor of HEAD) retires infra/aws/terraform/amgt-resapp/dynamodb.tf and security-metrics-table.tf; ea6cd450fa removes its main.tf; no such tree at HEAD"
  ],
  "remedy": "The competing orders were superseded with a named successor and the orphaned module retired; this row carries the disarm clock Z-S11's own row could not.",
  "owner": "2.0.0_SA_COO~Z",
  "round": "v83",
  "disarms": [
   "AMGT_RESAPP-Z-S11"
  ],
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~Z",
   "at": "2026-09-11T20:16Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~Z",
   "round": "v83"
  },
  "closed": true
 },
 {
  "id": "AMGT_RESAPP-Z-S348",
  "project": "AMGT_RESAPP",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "to-decomp-ref-lint's seating limb counted withdrawn orders as open and read the first status tag, refusing seats on projects whose orders were terminal.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S348",
   "3e537ca81b (merged @9fa882c45a, ancestor of HEAD): the lint reads the last line-anchored status and treats withdrawn as terminal; open orders 525 -> 59 per the CTO"
  ],
  "remedy": "The seating lint reads the last status tag and counts withdrawn as terminal.",
  "owner": "1.0.0_SA_CTO~Z",
  "round": "v83",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO~Z",
   "round": "v83"
  },
  "closed": true
 }
]
```

-- 3.0.0_SA_CVO~Z

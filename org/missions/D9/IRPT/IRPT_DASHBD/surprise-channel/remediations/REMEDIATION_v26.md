# IRPT_DASHBD -- rounds 52 and 54 remediations

<sweep_watermark>2026-10-09T16:58Z</sweep_watermark>

Graduated at ADJUDICATION_v33.md, round label v55: D2-W81-S1, OPEN.

```json
[
  {
    "id": "IRPT_DASHBD-D2-W81-S1",
    "project": "IRPT_DASHBD",
    "fabric": "dell2",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "BD's landed transaction dates exist only in blackdiamond/49financial/silver_legacy/transactions (legacy plane, last return_date 2026-08-20, whole weeks absent); of 475 FLOW_TIMING/INCOME_DATE segments 156 confirmed, 319 UNEXPLAINED (BD_RECORD_ABSENT_DAY 76, BD_RECORD_ENDS_BEFORE_OPAL_EVENTS 80, DATE_SETS_DIFFER 275, NO_BD_TXN_FOR_ACCOUNT 3; codes overlap).",
    "evidence": [
      "investigation row IRPT_DASHBD-D2-W81-S1",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUNDS_52_54_B_DRAIN_END_20261009.md @bb07230e44 (msg 3738)"
    ],
    "remedy": "Rule what 'confirmed' means for a FLOW_TIMING or INCOME_DATE segment: equal dates show the two books record the same event on the same day, which argues AGAINST timing as the cause of the gap unless the convention differs (W75-S1). Then either re-code the 156 or keep them with the ruling cited; the 319 UNEXPLAINED need a BD record past 2026-08-20 (a fresh BD transaction pull) before they can be read.",
    "owner": "1.0.0_SA_CTO~DELL2",
    "round": "v55",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL2",
      "round": "v55"
    },
    "closed": false
  }
]
```

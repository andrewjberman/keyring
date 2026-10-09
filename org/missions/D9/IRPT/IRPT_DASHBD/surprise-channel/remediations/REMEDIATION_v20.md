# IRPT_DASHBD -- rounds 42 and 44 remediations

<sweep_watermark>2026-10-09T13:26Z</sweep_watermark>

Graduated at the rounds-42/44 L8 (ADJUDICATION_v26.md), round label v45: S43, OPEN (a ruling).

```json
[
  {
    "id": "IRPT_DASHBD-S43",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "TO-DB-b-86 cannot run as amended: the runner requires account_set_id as sel_<64 hex> from an Opal operator's selection-create answer, but AMENDMENT 1's two served reads cannot produce it -- the served custody directory has no selection field in any of its 269 entries, and svc-custody-statement is admitted on three operations that do not include selection-create. Filling it would be a fabricated reference.",
    "evidence": [
      "investigation row IRPT_DASHBD-S43",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUNDS_42_44_B_DRAIN_END_20261009.md @d4661c3360 (msg 3358)"
    ],
    "remedy": "Rule how DB-b-86 obtains a selection (account_set_id sel_<64 hex>): an operator's selection-create answer, a served selection read for svc-custody-statement, or a re-cut that does not need one.",
    "owner": "1.0.0_SA_CTO~DELL2",
    "round": "v45",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL2",
      "round": "v45"
    },
    "closed": false
  }
]
```

# IRPT_DASHBD -- round 45 remediations

<sweep_watermark>2026-10-09T13:50Z</sweep_watermark>

Graduated at round 45's L8 (ADJUDICATION_v27.md), round label v46: D2-W68-S1, OPEN.

```json
[
  {
    "id": "IRPT_DASHBD-D2-W68-S1",
    "project": "IRPT_DASHBD",
    "fabric": "dell2",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "sel_<64 hex> is not derivable from the seat-authored file (it hashes the firm directory revision) and the POST /analysis owner-resolution loads a stored selection record: a file-only submission will be refused by the route unless a stored record exists.",
    "evidence": [
      "investigation row IRPT_DASHBD-D2-W68-S1",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND45_B_DRAIN_END_20261009.md @748b3cd3dc (msg 3396)"
    ],
    "remedy": "DB-b-86's first real run proves whether live POST /analysis admits a submission with no account_set_id; if it refuses (no stored SELECTION record), the runner needs an operator's selection-create answer.",
    "owner": "2.0.0_SA_COO~D2",
    "round": "v46",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~D2",
      "round": "v46"
    },
    "closed": false
  }
]
```

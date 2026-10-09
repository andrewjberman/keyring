# IRPT_DASHBD -- round 48 remediations

<sweep_watermark>2026-10-09T14:40Z</sweep_watermark>

Graduated at round 48's L8 (ADJUDICATION_v29.md), round label v49: 2 rows, OPEN.

```json
[
  {
    "id": "IRPT_DASHBD-D2-W73-S1",
    "project": "IRPT_DASHBD",
    "fabric": "dell2",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "74 OUTSIDE segments carry a DEFECT: BD and the served series disagree on dollars and the gain gap does not reconcile the return gap",
    "evidence": [
      "investigation row IRPT_DASHBD-D2-W73-S1",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND48_B_DRAIN_END_20261009.md @63b594d8d0 (msg 3482)"
    ],
    "remedy": "Trace the 74 segments where Black Diamond's dollars and the served series disagree and the gain gap does not explain the return gap (value, flow or gain source per segment), and print the NEAR_ZERO_BASE count at 0.5% and 2% of peak beside the 1% one.",
    "owner": "2.0.0_SA_COO~D2",
    "round": "v49",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~D2",
      "round": "v49"
    },
    "closed": false
  },
  {
    "id": "IRPT_DASHBD-D2-W73-S2",
    "project": "IRPT_DASHBD",
    "fabric": "dell2",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "123 OUTSIDE segments carry a DEFECT: dollars tie yet the returns differ and no convention, window or base test explains it",
    "evidence": [
      "investigation row IRPT_DASHBD-D2-W73-S2",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND48_B_DRAIN_END_20261009.md @63b594d8d0 (msg 3482)"
    ],
    "remedy": "Trace the 123 segments where the dollars tie but the returns differ (a vendor TWR convention, a window or sub-period linking difference), each to a named reason or named untraced; FWD-8 is not met while these stand.",
    "owner": "2.0.0_SA_COO~D2",
    "round": "v49",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~D2",
      "round": "v49"
    },
    "closed": false
  }
]
```

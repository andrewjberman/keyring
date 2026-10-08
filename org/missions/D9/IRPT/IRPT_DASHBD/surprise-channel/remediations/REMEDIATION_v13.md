# IRPT_DASHBD -- round 29 remediations

<sweep_watermark>2026-10-08T21:02Z</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2), 2026-10-08. Graduated at round 29's L9 (ADJUDICATION_v15.md), round label v30: W30-S1, W31-S2, both OPEN.

```json
[
  {
    "id": "IRPT_DASHBD-W30-S1",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Opal's fee_amount is 0 on every window-day over all 1,528 right halves, while Opal sits above BD on 94.7% of them (median +0.567 pp). The likely cause, unmeasured, is an advisory fee BD deducts that Opal's daily never carries.",
    "evidence": [
      "investigation row IRPT_DASHBD-W30-S1 (RIGHT_GAP_E2.json drivers_undefined)",
      "drive log @047176ff76 (E2 statistics)"
    ],
    "remedy": "Compare each right half's gap to BD's own gross-minus-net over the same half (the round-18 pull carries both). A tie routes the fix to Opal's fee feed (fee_amount is never populated); no tie leaves the gap unexplained and keeps branch B's repair open.",
    "owner": "1.0.0_SA_CTO~DELL2",
    "round": "v30",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL2",
      "round": "v30"
    },
    "closed": false
  },
  {
    "id": "IRPT_DASHBD-W31-S2",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "At batch 2,000 the lots-stage total read 757.55, 692.81 and 666.98 s on this box (a 90 s spread with two other workers running), so the 750 s bar sits inside run-to-run noise; W27-S2's served-runtime measurement (pandas 2.2.3) is still owed.",
    "evidence": [
      "investigation row IRPT_DASHBD-W31-S2 (LOTS_750_E3.json)",
      "remediation row IRPT_DASHBD-W27-S2 (REMEDIATION_v12)"
    ],
    "remedy": "Measure batch 2,000 once on the served runtime before the release, and state the bar against that runtime's spread (or pick 1,500, 627 s, for headroom).",
    "owner": "2.0.0_SA_COO~D2",
    "round": "v30",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~D2",
      "round": "v30"
    },
    "closed": false
  }
]
```

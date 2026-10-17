# AMGT_RESAPP -- round 108 AC9 grade restated by full id (dell1)

<sweep_watermark>2026-10-17T11:43:03Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-17T11:43:03Z. One row; nothing swept since ADJUDICATION_v145.

```json
[
  {
    "id": "AMGT_RESAPP-D1-C-S171",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-17T11:43:03Z",
    "one_line": "AMGT_RESAPP.TO-AMGT-bo-3.withheld-reasons-walk-on-a-local-build-of-prod AC9 MET. This row restates C-S169's grade (ADJUDICATION_v145) by the order's full to_id, so round-close-check reads it; no grade changed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "round-close-check credits a judgment grade only on a row naming the order by its full to_id or the full short id after 'TO-'.",
    "world_is": "C-S169 named the order 'AMGT_RESAPP.TO-AMGT-bo-3', which the check does not match to the to_id AMGT_RESAPP.TO-AMGT-bo-3.withheld-reasons-walk-on-a-local-build-of-prod (round-close-check --round 108 read AC9 UNGRADED after v145). The grade and its bounds are C-S169's: MET on the named scope, and FWD-40 (d) not realized because of the RIO LN Model crash (W477-S1, REMEDIATION_v48).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ADJUDICATION_v145.md row AMGT_RESAPP-D1-C-S169",
        "python .tools/round-close-check.py --project AMGT_RESAPP --round 108 (UNGRADED before this row)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade restated by full id; no grade changed."
  }
]
```

-- 3.0.0_SA_CVO

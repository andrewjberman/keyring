# AMGT_RESAPP -- round 106, bm-5 AC5 grade restated by order id (dell1)

<sweep_watermark>2026-10-15T16:43Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-15T19:06:37Z. Asked by 2.0.0_SA_COO~R1 msg 6148: round-close-check credits a grade only when the row names
the order by its to_id. One row; no rows swept, so the watermark does not move. The grade and its evidence are unchanged from C-S151 (ADJUDICATION_v131 @fb734342ab).

```json
[
  {
    "id": "AMGT_RESAPP-D1-C-S153",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-15T19:06:37Z",
    "one_line": "AMGT_RESAPP.TO-AMGT-bm-5.the-fresh-draw-ten-name-browser-walk-on-a-local-build-of-prod-with-the-pe-basis-and-reasons-feature AC5 NOT MET -- the same grade as C-S151, restated with the order's to_id.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "AMGT_RESAPP.TO-AMGT-bm-5.the-fresh-draw-ten-name-browser-walk-on-a-local-build-of-prod-with-the-pe-basis-and-reasons-feature AC5 (judgment): the walk's screenshot read over the three round-106 changes.",
    "world_is": "AMGT_RESAPP.TO-AMGT-bm-5.the-fresh-draw-ten-name-browser-walk-on-a-local-build-of-prod-with-the-pe-basis-and-reasons-feature AC5 NOT MET. Change 1 shows on BNP FP; change 3 does not show on SHOP CN (the team's own P/E line fills the forward cells, so the withhold reason never prints); change 2 was not exercised, because no shot opens the All-figures grid. The full record and evidence are in AMGT_RESAPP-D1-C-S151, ADJUDICATION_v131.md @fb734342ab.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "adjudications/ADJUDICATION_v131.md AMGT_RESAPP-D1-C-S151 @fb734342ab",
        ".tools/round-close-check.py:525-560 (the order-name match this row satisfies)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade record restating C-S151 by the order's to_id; not a new hazard."
  }
]
```

-- 3.0.0_SA_CVO

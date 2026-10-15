# DSGN_RBNDV2 -- remediations, v3

<sweep_watermark>2026-10-15T12:10Z</sweep_watermark>

Author: `3.0.0_SA_CVO~L`, 2026-10-15 ~12:1xZ, at the round-3 close. Graduated in ADJUDICATION_v4.md C-S14. One row, ARMED. REMEDIATION_v1 and v2 stand as filed.

```json
[
 {
  "id": "DSGN_RBNDV2-W10-S2",
  "project": "DSGN_RBNDV2",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "RSIModal.tsx's chart grid, axis and tick were literal white (lines 229, 334, 351, 370, 375, 376). RV-c-2 mapped them to the rb tokens, and the served file holds 0 white literals, but the modal opens from a chart bar that no walk has pressed, so its render is unread.",
  "evidence": [
   "org/missions/D13/DSGN/DSGN_RBNDV2/surprise-channel/investigations/INVESTIGATION_v1.md row W10-S2",
   "adjudication row DSGN_RBNDV2-C-S14"
  ],
  "remedy": "P3. A walk opens RSIModal from its chart bar (a walker --hover or coordinate press on the Global RSI panel) and reads its axes. Done when the RSI chart axes read navy-grey in that walk.",
  "owner": "2.0.0_SA_COO~RB",
  "round": "v3",
  "remediation": {"state": "OPEN", "owner": "2.0.0_SA_COO~RB", "round": "v3"},
  "disarm": {"state": "ARMED", "owner": "2.0.0_SA_COO~RB", "at": null},
  "closed": false
 }
]
```

-- 3.0.0_SA_CVO~L

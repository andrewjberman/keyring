# IRPT_DASHBD: CVO correction of v148's mechanical tally (round 149 packet 5)

<sweep_watermark>2026-10-17T00:40Z</sweep_watermark>

Correction by `3.0.0_SA_CVO~IRPT` of its own row IRPT_DASHBD-D2-C-S85 (ADJUDICATION_v148 @1050831467). Its one_line says "Mechanical: 25 PASS, 6 FAIL". The body's own per-criterion lines sum to 27 PASS and 6 FAIL of 33:
- **reader:** 8 PASS, 4 FAIL;
- **applier:** 9 PASS;
- **portal:** 10 PASS, 2 FAIL.

Nothing else in v148 changes.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S86",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-17T00:40:00Z",
  "one_line": "Corrects C-S85's mechanical tally: 27 PASS and 6 FAIL of 33 (reader 8/4, applier 9/0, portal 10/2), not 25 PASS. Nothing else changes.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": ["IRPT_DASHBD-D2-C-S85"],
  "spec_asserts": "C-S85 one_line: 'Mechanical: 25 PASS, 6 FAIL'.",
  "world_is": "C-S85's body lists PASS on DB170-1-AC3, DB173-1-AC2/AC3, DB174-1-AC1/AC3, DB178-1-AC1/AC2/AC3 (8), DBC176/179/182 x3 (9), DBP175 x3, DBP177 x3, DBP180-1-AC1/AC3, DBP181-1-AC1/AC3 (10): 27; FAIL on DB170-1-AC1/AC2, DB173-1-AC1, DB174-1-AC2, DBP180-1-AC2, DBP181-1-AC2: 6.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/adjudications/ADJUDICATION_v148.md @1050831467, section 'Mechanical criteria, re-run (33)'"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A counting error in the CVO's own one_line; the per-criterion record in v148 stands."
 }
]
```

# ADVI_COTBKF: CVO adjudication, round 30

<sweep_watermark>2026-10-09T09:04Z</sweep_watermark>

Round 30 L8 compile and L9 grade by `3.0.0_SA_CVO` (seated on dell2), 2026-10-09 ~09:0xZ. L8 input: `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_30_DRAIN_END_20261009.md @6a163e8b24` (msg 2956).
**L9: CB30ad1-AC2 MET** (row D2-S46; `org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_30_L9_GRADE_20261009.md`). 2 rows dismissed below; no new remediation row; D2-S45 stays OPEN. ARMED: 0.

**For the analysis:** one outside number settles D2-S45: the as-traded close of 808524102 and 808524839 on one pre-split day (expect
~39.99 / ~39.44 on 2022-10-12 if r28 is right; ~13.33 / ~19.72 if r28 double-scales). Yahoo egress is open.

```json
[
  {
    "id": "ADVI_COTBKF-C-S31",
    "project": "ADVI_COTBKF",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T09:04:24Z",
    "one_line": "Round 30 rows dismissed: D2-W57-S1 (the r28-is-right reading, labelled an inference from method_r28's own continuity test -- carried, unproven, by D2-S45) and this seat's grade row D2-S46. D2-S45 stays OPEN: the factor is located (808524102 x3, 808524839 x2, both 2024-10-11) but the right level is unmeasured.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_COTBKF-D2-W57-S1",
      "ADVI_COTBKF-D2-S46"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "CB-ad-1 complete, drained @abe8a94a17; SCALE-TRACE accounts=2 untraced=2 (issuer's run equals the worker's).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows ADVI_COTBKF-D2-W57-S1, D2-S46",
        "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_30_DRAIN_END_20261009.md @6a163e8b24",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_30_L9_GRADE_20261009.md"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An inference carried by an open row, and a grade row."
  }
]
```

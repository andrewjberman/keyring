# ADVI_COTBKF: CVO adjudication, round 40

<sweep_watermark>2026-10-09T14:16Z</sweep_watermark>

Round 40 L8 compile and L9 grade by `3.0.0_SA_CVO` (seated on dell2), 2026-10-09 ~14:2xZ. L8 input: `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_40_DRAIN_END_20261009.md @5006e7df0d (msg 3433)`.
**L9: CB40an1-AC2 MET** (row D2-S65; `org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_40_L9_GRADE_20261009.md`). W68-S1 and W68-S2 graduate OPEN in `remediations/REMEDIATION_v28.md`. ARMED: 0.

**For the analysis:** the writer is safe but NOT-CLEAN in production as built: the gold run syncs only code/gold/, so without the registry
shipped beside it every row reads absent (W68-S2). The deploy cell must carry lib/opal_naming and the registry.

```json
[
  {
    "id": "ADVI_COTBKF-C-S38",
    "project": "ADVI_COTBKF",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T14:16:38Z",
    "one_line": "Round 40: this seat's grade row D2-S65 dismissed (MET). D2-W68-S1 (a dead share-class check) and D2-W68-S2 (the writer's run-time registry dependency, deploy-blocking as is) graduate. D2-S62 stays OPEN: it closes when the next silver-prep's census reads cottonwood with BREACH=0.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_COTBKF-D2-S65"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "CB-an-1 complete, drained @ba35c04d1c; cot gold tests 36 passed; SOURCE-FIRM-CENSUS keys=38 absent=11671939 BREACH=0 (the column does not exist yet; NOT deployed).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_COTBKF-D2-S65",
        "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_40_DRAIN_END_20261009.md @5006e7df0d (msg 3433)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A MET grade row."
  }
]
```

# ADVI_COTBKF: CVO adjudication, round 35

<sweep_watermark>2026-10-09T12:17Z</sweep_watermark>

Round 35 L8 compile and L9 grade by `3.0.0_SA_CVO` (seated on dell2), 2026-10-09 ~12:2xZ. L8 input: `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_35_DRAIN_END_20261009.md @cd42e26d8a (msg 3252)`.
**L9: CB35ai1-AC2 MET** (row D2-S51, detector note; `org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_35_L9_GRADE_20261009.md`). W60-S1 closed; D2-S52 graduates OPEN in `remediations/REMEDIATION_v25.md`.
ARMED: 0.

**For the analysis (two acts, one Andrew's):**
1. **The 38 keys:** a rewrite without the 49F rows under a never-widen pair, not a delete (each key is a full Cottonwood price file).
   Which one is Andrew's call; S3 deletes need his word.
2. **The three bonds:** Yahoo carries no bond series, so they stay HELD (HELD_SOURCE_UNDER_REVIEW) until a source of record is ruled.

```json
[
  {
    "id": "ADVI_COTBKF-C-S34",
    "project": "ADVI_COTBKF",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T12:17:11Z",
    "one_line": "Round 35 rows dismissed: D2-W63-S1 (the worker's disclosure: run 1's detector over-matched docstrings and a 1 s prior-carrier window; corrected in the detector, not the rule; the read set narrowed after a timeout, stated) and this seat's grade row D2-S51. W60-S1 closed in place (its question is answered: the rows came from a shared-builder chain that ran 49F's inject step inside cot's run, removed @319a716cb4 -- a defect, now closed in code). D2-S52 graduates: the rows still in the 38 keys.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_COTBKF-D2-W63-S1",
      "ADVI_COTBKF-D2-S51"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "CB-ai-1 complete, drained @381f92da9e; BD-TXN-PROVENANCE class=shared_builder_run, 38 keys (the issuer's run equal except keys_scanned, the bucket being live). Round 34 (CB-ah-3 held on its pair) is not compiled here.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows ADVI_COTBKF-D2-W63-S1, D2-S51",
        "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_35_DRAIN_END_20261009.md @cd42e26d8a (msg 3252)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A disclosure and a grade row."
  }
]
```

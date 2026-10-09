# ADVI_COTBKF: CVO adjudication, round 27

<sweep_watermark>2026-10-09T04:44Z</sweep_watermark>

Round 27 L8 compile and L9 grade by `3.0.0_SA_CVO` (seated on dell2), 2026-10-09 ~04:5xZ. L8 input: `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_27_DRAIN_END_20261009.md @8f766d479f` (msg 2428).
**L9: CB27aa1-AC3 NOT MET; CB27aa2-AC3 MET; CB27aa3-AC3 MET** (row D2-S40; `org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_27_L9_GRADE_20261009.md`). 4 rows dismissed below; 5 graduate OPEN in
`remediations/REMEDIATION_v19.md` (W50-S1..S3, W51-S1, D2-S40). ARMED: 0.

**For the analysis:** the split, distribution and in-kind repairs (W50-S1..S3) un-hold CB-aa-4. The trace's reach cap must be fixed
before the months it grades are seen (D2-S40).

```json
[
  {
    "id": "ADVI_COTBKF-C-S28",
    "project": "ADVI_COTBKF",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T04:44:16Z",
    "one_line": "Round 27 rows dismissed: D2-W52-S1 (the builder re-derives holdings and daily returns and refuses unless they check against the run -- the right design), D2-W52-S2 (most cells are blank with a reason; a statement of coverage, carried by the price work), D2-W52-S3 (35 of 3,098 MATCH months on open accounts; the one-account read and Year join state their rules), D2-S39 (the issuer's disarm of W50-S1..S3: CB-aa-4 withdrawn, nothing served).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_COTBKF-D2-W52-S1",
      "ADVI_COTBKF-D2-W52-S2",
      "ADVI_COTBKF-D2-W52-S3",
      "ADVI_COTBKF-D2-S39"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Four orders terminal (3 complete, CB-aa-4 withdrawn @19f2e89ca8, never spawned). Nothing was written to S3. W50-S1..S3 stay OPEN as defects, disarmed by D2-S39 because their only path to a reader is CB-aa-4.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows ADVI_COTBKF-D2-W52-S1, W52-S2, W52-S3, D2-S39",
        "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_27_DRAIN_END_20261009.md @8f766d479f"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A sound design, coverage statements, and the issuer's disarm."
  }
]
```

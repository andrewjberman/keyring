# ADVI_COTBKF: CVO adjudication, round 70

<sweep_watermark>2026-10-11T17:14Z</sweep_watermark>

L8 compile and L9 grade by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T17:14:12Z. L8 input: `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_70_DRAIN_END_20261011.md @28d71b3241 (msg 5417)`.
**L9: CB70br2-AC2, CB70br3-AC2, CB70br4-AC2 and CB70br5-AC3 all MET** (row D2-S121; `org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_70_L9_GRADE_20261011.md`).
2 rows dismissed below. 1 row graduates OPEN in `remediations/REMEDIATION_v41.md`.

```json
[
  {
    "id": "ADVI_COTBKF-C-S54",
    "project": "ADVI_COTBKF",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T17:14:12Z",
    "one_line": "Round 70: dismissed, D2-W114-S1 (a correction of this seat's row D2-S120: the flow differs on 47 account-days over 46 dates when compared exactly, not 44; accepted, and reconciled by this seat -- 44 carry a real change and 3 are floating-point residue on a value of zero) and this seat's grade row D2-S121. Graduates: D2-W113-S1.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_COTBKF-D2-W114-S1",
      "ADVI_COTBKF-D2-S121"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence.",
    "world_is": "Round 70's five orders are terminal and no ADVI_COTBKF order is open (to-check).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows D2-W114-S1, D2-S121",
        "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_70_DRAIN_END_20261011.md @28d71b3241 (msg 5417)",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_70_L9_GRADE_20261011.md",
        "this seat's exact comparison of the flow column on the two at-pin tables: 47 account-days over 46 dates differ exactly; 44 differ by more than 1e-9; the other 3 differ by less than 1e-12 on a value of 0.0, floating-point residue"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An accepted correction, reconciled, and a grade row."
  }
]
```

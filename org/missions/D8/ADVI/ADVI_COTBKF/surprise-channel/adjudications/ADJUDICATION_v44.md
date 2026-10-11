# ADVI_COTBKF: CVO adjudication, round 67

<sweep_watermark>2026-10-11T13:18Z</sweep_watermark>

L8 compile and L9 grade by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T13:18:17Z. L8 input: `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_67_DRAIN_END_20261011.md @2326dc3955 (msg 4966)`.
**L9: CB67bo2-AC2 MET** (row D2-S116; `org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_67_L9_GRADE_20261011.md`). 2 rows dismissed below.
4 rows graduate OPEN in `remediations/REMEDIATION_v38.md`, the slug for rounds 65 to 67.

```json
[
  {
    "id": "ADVI_COTBKF-C-S51",
    "project": "ADVI_COTBKF",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T13:18:17Z",
    "one_line": "Round 67: dismissed, D2-W97-S1 (the served table could not be rebuilt: the build now reads the split store at a named instant and refuses an unpinned read -- the issuer's own refusal run and its equal re-run an hour apart; Proof A, 0 of 1,691,729 rows differing at the served instant, is the worker's run and was re-run by nobody) and this seat's grade row D2-S116. Graduate: D2-S115, D2-W100-S1, D2-W99-S1, D2-W99-S2.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_COTBKF-D2-W97-S1",
      "ADVI_COTBKF-D2-S116"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Rounds 65, 66 and 67 are terminal and no ADVI_COTBKF order is open (to-check).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows D2-W97-S1, D2-S116",
        "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_67_DRAIN_END_20261011.md @2326dc3955 (msg 4966)",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_67_L9_GRADE_20261011.md"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A defect answered by a pin, on the issuer's two runs and the worker's proof, and a grade row."
  }
]
```

# ADVI_COTBKF: CVO adjudication, round 12

<sweep_watermark>2026-10-07T14:5xZ</sweep_watermark>

Round 12 L8 compile and L9 by `3.0.0_SA_CVO` (seated on dell2), 2026-10-07 ~15:0xZ. L8 input: `deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_12_DRAIN_END_20261007.md @c4f975368c` (msg 733). 1 of 1 order (CB-l-1) complete
and VALID @c324cf4f27. 1 row (D2-W28-S1), dismissed below. L9: CB12l1-AC3 NOT MET; grade file `org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_12_L9_GRADE_20261007.md`; this compile files row D2-S24
(the defect) and does not compile it. ARMED: 0.

```json
[
 {
  "id": "ADVI_COTBKF-C-S17",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-07T15:05Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "ROUND 12 L9: CB12l1-AC3 NOT MET (cash-in-lieu sales are never subtracted; row D2-S24). D2-W28-S1 (three choices the order left open) is dismissed.",
  "adjudicates": [
   "ADVI_COTBKF-D2-W28-S1"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
  "world_is": "D2-W28-S1's choices are each reasonable and stated: a repeated pair counts on both sides (394 pairs), a trade dated on a non-trading day takes effect the next trading day (220 of 3,537 trade dates), and a quantity within 1e-6 of zero is not stored. None of them causes the 13 differences; all 13 are unsubtracted cash-in-lieu fractions (grade file).",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigation row ADVI_COTBKF-D2-W28-S1",
    "deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_12_DRAIN_END_20261007.md @c4f975368c",
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_12_L9_GRADE_20261007.md"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Stated method choices, none of which is the cause of the round's differences."
 }
]
```

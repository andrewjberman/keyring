# ADVI_COTBKF: CVO adjudication, round 75

<sweep_watermark>2026-10-11T22:35Z</sweep_watermark>

L9 grade, L8 compile and L10 slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T22:35:08Z. Input: `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_75_DRAIN_END_20261011.md @056535ed50 (msg 5976)`.
**CB75bw1-AC2, CB75bw2-AC2, CB75bw4-AC2: all MET** (row D2-S128; `org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_75_L9_GRADE_20261011.md`). 1 row dismissed below. Nothing graduates.

**For the CTO's analysis:**
1. **The served table marks a purchase at about three quarters of the cash paid, on the 12 purchases read.** Confirmed by the worker
   under a rule written first and by this seat on the custodian's amount and quantity: the unadjusted close 12 of 12, the served
   close 0 of 12.
2. **A quarter of all purchase rows do not fit the unadjusted close** (26 percent of 936; unexamined). That is the next thing to
   read: it decides whether "value a purchase at the unadjusted close" is the whole rule or part of it.
3. **`weight_effect` names 63 of the 74 and is not a cause.** It does not say which build is wrong on those days.
4. 10 of 377 holders of the moved funds are measured; the size beyond them is not known. Row D2-S127 stays OPEN on that.
5. The one fund at 0.18 is not named and nothing served rests on it. The correction list carries a trade-day entry marked a lead;
   on this round's evidence it is more than a lead for the 12 and still a lead for the rest.

```json
[
  {
    "id": "ADVI_COTBKF-C-S59",
    "project": "ADVI_COTBKF",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T22:35:08Z",
    "one_line": "Round 75: this seat's grade row D2-S128 (three criteria MET) is dismissed as a grade record. No worker or issuer row was filed in the round. Rows D2-S126, D2-S127 and D2-W120-S1 stay OPEN.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_COTBKF-D2-S128"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): a judgment criterion is graded by the CVO and never self-graded.",
    "world_is": "No ADVI_COTBKF order is open (this seat's count of the order files: 150 complete, 3 withdrawn, 1 superseded).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row D2-S128",
        "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_75_DRAIN_END_20261011.md @056535ed50 (msg 5976)",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_75_L9_GRADE_20261011.md"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade row."
  }
]
```

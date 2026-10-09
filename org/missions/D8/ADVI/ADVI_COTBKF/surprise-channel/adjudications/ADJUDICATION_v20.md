# ADVI_COTBKF: CVO adjudication, round 26

<sweep_watermark>2026-10-09T03:03Z</sweep_watermark>

Round 26 L8 compile and L9 grade by `3.0.0_SA_CVO` (seated on dell2), 2026-10-09 ~03:0xZ. L8 input: `deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_26_DRAIN_END_20261009.md` (msg 2221). 3 of 3 orders
terminal. **L9: CB26z1-AC3, CB26z2-AC3, CB26z3-AC2 all MET** (row D2-S38; `org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_26_L9_GRADE_20261009.md`). 4 rows dismissed below; D2-W48-S2 (the 512
unexplained) graduates OPEN in `remediations/REMEDIATION_v18.md`. ARMED: 0.

For the analysis: 94.2% of all non-MATCH months are UNPRICED (74,846 of 79,495). Price coverage, not method, bounds FWD-3 now. The
endpoint is 4 of 9 by instruments run tonight; the '6 of 9' figure carried since round 15 is retired.

```json
[
  {
    "id": "ADVI_COTBKF-C-S27",
    "project": "ADVI_COTBKF",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T03:03:20Z",
    "one_line": "Round 26 rows dismissed: D2-W48-S1 (ARMED: the default flip turned one test red outside CB-z-2's grant; grant widened @4a4088de98 and fixed @1d4ceec9d0, suite 659 passed), D2-W48-S3 (the record of that fix), D2-W49-S1 (the only local daily-returns file is a stale round-18 output grading 1,685; nothing is served, which is FWD-3's NOT), and this seat's grade row D2-S38 (all three MET).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_COTBKF-D2-W48-S1",
      "ADVI_COTBKF-D2-W48-S3",
      "ADVI_COTBKF-D2-W49-S1",
      "ADVI_COTBKF-D2-S38"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Drains a9aca322b9 and 718291c2c7 are ancestors of box/dell2 HEAD. CB26z2-AC2 (mechanical) FAILED (unexplained=512) and is closed graded NOT MET by CTO msg 2213, not amended; the 512 carry forward as D2-W48-S2. The endpoint stands at 4 of 9 REALIZED, correcting the '6 of 9' carried since round 15.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows ADVI_COTBKF-D2-W48-S1, D2-W48-S3, D2-W49-S1, D2-S38",
        "deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_26_DRAIN_END_20261009.md",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_26_L9_GRADE_20261009.md"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An armed red disarmed by an in-round fix, its record, a stale local file with nothing served, and a MET grade."
  }
]
```

# ADVI_COTBKF: CVO adjudication, round 25

<sweep_watermark>2026-10-09T01:43Z</sweep_watermark>

Round 25 L8 compile and L9 grade by `3.0.0_SA_CVO` (seated on dell2), 2026-10-09 ~01:5xZ. L8 input: `deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_25_DRAIN_END_20261009.md` (msg 2105). CB-y-1 and
CB-y-2 complete and VALID. **L9: CB25y1-AC3 MET, CB25y2-AC3 MET** (row D2-S37; `org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_25_L9_GRADE_20261009.md`). 3 rows dismissed below; 3 rows of round 24
closed in place (D2-S36, D2-W46-S2, D2-W46-S3). No new remediation row. ARMED: 0.

For the analysis: `method_r25` is graded at 0 regressions and +39 MATCH. Adopting it as the default is the CTO's call. The next
yield is a fresh cause census of the 886 DIFF months on that baseline.

```json
[
  {
    "id": "ADVI_COTBKF-C-S26",
    "project": "ADVI_COTBKF",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T01:43:44Z",
    "one_line": "Round 25 rows dismissed: D2-W47-S1 (the carried-level premise did not hold: the method's ledger closes to 0.00 on 13 of 13 closed accounts; the old baseline departs, so no fix was owed), D2-W47-S2 (dividends graded both ways: 20 of 22 do not move, ex-dating nets +2/-6, pay date stays), and this seat's grade row D2-S37 (both AC3s MET, nothing owed).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_COTBKF-D2-W47-S1",
      "ADVI_COTBKF-D2-W47-S2",
      "ADVI_COTBKF-D2-S37"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Chain drained @052a80dd0f (ancestor of box/dell2 HEAD). method_r25: MATCH 3,059 -> 3,098, 0 regressions; dividend both-ways run (ex-dates served by dell1 MDPF_DEMQUE @5a392db104): 22 of 22 graded, MATCH 3,098 -> 3,094 under ex. Closed in place, clocks only: D2-S36 (round 24's unmeasurable dividend clause, now measured), D2-W46-S2 (ex-date source, delivered), D2-W46-S3 (unlisted types, each sourced, 35 of 35 MATCH) in REMEDIATION_v17.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows ADVI_COTBKF-D2-W47-S1, D2-W47-S2, D2-S37",
        "deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_25_DRAIN_END_20261009.md",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_25_L9_GRADE_20261009.md"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A falsified premise needing no fix, a measured convention question decided by its own numbers, and a MET grade."
  }
]
```

# ADVI_COTBKF: CVO adjudication, round 34

<sweep_watermark>2026-10-09T12:55Z</sweep_watermark>

Round 34 L8 compile and L9 grade by `3.0.0_SA_CVO` (seated on dell2), 2026-10-09 ~13:0xZ. L8 input: `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_34_DRAIN_END_20261009.md @9498283193 (msg 3295)`.
**L9: CB34ah1-AC2 MET, CB34ah2-AC3 MET** (row D2-S58; `org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_34_L9_GRADE_20261009.md`). The CTO's reader gate may open on this grade. Rows dismissed below;
D2-S50, W59-S1 and W53-S3 closed in place; 6 graduate OPEN in `remediations/REMEDIATION_v26.md`. ARMED: 0.

**For the analysis:**
1. **The re-grade line reads control_same=False, uninvestigated.** The control accounts moved because the price basis changed for every
   account, which is expected, but no row says so; a reader gate opened on this round should know the control is not a no-change arm.
2. **5 new regressions are ABSENT** (D2-S53..S57), two on D49151054 near 0.6 pp; causes untraced.
3. **3,962 interpolated days dropped** (W62-S2); 36 priced holding-days lost.

```json
[
  {
    "id": "ADVI_COTBKF-C-S35",
    "project": "ADVI_COTBKF",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T12:55:59Z",
    "one_line": "Round 34 rows dismissed: D2-W61-S1 (BLOCKING, cross_firm: answered by rounds 35/36 and carried by D2-S52, the 38-key rewrite), D2-W62-S1 (AC2's invocation read the grades from a copied path, recorded) and this seat's grade row D2-S58. Closed in place, clocks only: D2-S50 (FWD-3 re-minted on the as-traded basis: served verify match=True on all three tables, new versions at 12:41Z), D2-W59-S1 (the price-basis ruling applied store-wide), D2-W53-S3 (the four round-28 regressions now MATCH).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_COTBKF-D2-W61-S1",
      "ADVI_COTBKF-D2-W62-S1",
      "ADVI_COTBKF-D2-S58"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "CB-ah-1, -2, -3 complete; the CB-ah-3 ledger closed (5 legs); MATCH 3,133 -> 3,678, DIFF 838 -> 293; 5 new regressions ABSENT; three 49F bonds HELD (988 account-days).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows ADVI_COTBKF-D2-W61-S1, D2-W62-S1, D2-S58",
        "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_34_DRAIN_END_20261009.md @9498283193 (msg 3295)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Carried by an open row, a recorded path note, and a grade row."
  }
]
```

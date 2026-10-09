# ADVI_COTBKF: CVO adjudication, round 33

<sweep_watermark>2026-10-09T10:50Z</sweep_watermark>

Round 33 L8 compile and L9 grade by `3.0.0_SA_CVO` (seated on dell2), 2026-10-09 ~10:5xZ. L8 input: `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_33_DRAIN_END_20261009.md @2fc7789480` (msg 3170).
**L9: CB33ag1-AC2 MET** (row D2-S49; `org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_33_L9_GRADE_20261009.md`). Rows dismissed below; D2-S50 (BLOCKING) and W60-S1 graduate OPEN in
`remediations/REMEDIATION_v24.md`. ARMED: 0.

**For the analysis:**
1. **The served FWD-3 tables are on the wrong basis for 38.3% of account-days, and unmarked** (D2-S50). ADDENDUM 8 item 2's marking
   should land before the rebuild, so no reader takes those rows as measured meanwhile.
2. **bd_txn_price in the cottonwood store** (W60-S1): its only writer in the repo is under data/black_diamond/. Whether that is the
   shared Black Diamond platform (Cottonwood's master is BD z09) or another firm's pipeline decides whether the cross-firm NEVER applies.
   It is yours to rule; the read of the writer's history is the evidence.

```json
[
  {
    "id": "ADVI_COTBKF-C-S33",
    "project": "ADVI_COTBKF",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T10:50:45Z",
    "one_line": "Round 33 rows dismissed: D2-S48 (folded into W60-S1), D2-W60-S2 (one debug Yahoo call beyond the 72 paced ones, disclosed) and this seat's grade row D2-S49. W59-S1's measurement is done (store-wide census); its ruling half stays with ADDENDUM 8. D2-S50 (served tables on the wrong basis, unmarked) and W60-S1 (bd_txn_price provenance) graduate.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_COTBKF-D2-S48",
      "ADVI_COTBKF-D2-W60-S2",
      "ADVI_COTBKF-D2-S49"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "CB-ag-1 complete, drained @aa376eb868; PRICE-BASIS tickers=3580 dividend_adjusted=2079 (58.1%), adv_days_on_adjusted=638948/1669040 (the issuer's run equals the worker's).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows D2-S48, D2-W60-S2, D2-S49",
        "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_33_DRAIN_END_20261009.md @2fc7789480"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A folded row, a disclosed extra call, and a grade row."
  }
]
```

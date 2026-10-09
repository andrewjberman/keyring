# ADVI_COTBKF: CVO adjudication, rounds 36 and 39

<sweep_watermark>2026-10-09T14:04Z</sweep_watermark>

Rounds 36 and 39 L8 compile and L9 grade by `3.0.0_SA_CVO` (seated on dell2), 2026-10-09 ~14:0xZ. L8 input: `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUNDS_36_39_DRAIN_END_20261009.md @3d68a5ab23 (msg 3412)`.
**L9: CB36aj1-AC2 MET, CB39am1-AC2 MET** (row D2-S64; `org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUNDS_36_39_L9_GRADE_20261009.md`). D2-S52 closed in place. ARMED: 0.

**For the analysis:**
1. **49 Financial's rows are out of Cottonwood's price store**; the prior versions are kept, and their deletion is Andrew's act. Condition 4
   (no 49F input at the next manual silver-prep) is the issuer's watch item; a re-injection reopens D2-S52.
2. **The carry-forward now carries its claim** (price_basis, price_source_date, source_firm) but is NOT deployed; the SERVED cell follows.
3. D2-S62 (the bd token) stays OPEN: round 40's source_firm field is its answer when it lands.

```json
[
  {
    "id": "ADVI_COTBKF-C-S37",
    "project": "ADVI_COTBKF",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T14:04:25Z",
    "one_line": "Rounds 36 and 39 rows dismissed: D2-W64-S1 (BLOCKING: the three bonds' source -- ruled by the CTO and measured in round 37 as UNPRICED; they now read UNPRICED in the store), D2-W64-S2, and this seat's grade row D2-S64. Closed in place, clocks only: D2-S52 (49 Financial's rows removed from the 38 Cottonwood price keys as new versions under the pair: 1,734 rows out, every other row byte-identical, verify 38/38; prior versions kept, their deletion Andrew's act).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_COTBKF-D2-W64-S1",
      "ADVI_COTBKF-D2-W64-S2",
      "ADVI_COTBKF-D2-S64"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "COT-PRICE-REWRITE-VERIFY keys=38 match=38/38 (the issuer's read of the served keys); the ff_worker claim stamp passes 31 cot gold tests, NOT deployed (a later SERVED cell). Round 38 stays open (CB-al-2 held on W66-S1).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows ADVI_COTBKF-D2-W64-S1, D2-W64-S2, D2-S64",
        "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUNDS_36_39_DRAIN_END_20261009.md @3d68a5ab23 (msg 3412)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Ruled and measured, and a grade row."
  }
]
```

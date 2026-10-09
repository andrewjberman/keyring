# ADVI_COTBKF: CVO adjudication, round 37

<sweep_watermark>2026-10-09T13:36Z</sweep_watermark>

Round 37 L8 compile and L9 grade by `3.0.0_SA_CVO` (seated on dell2), 2026-10-09 ~13:4xZ. L8 input: `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_37_DRAIN_END_20261009.md @7bc7b1fc1e (msg 3373)`.
**L9: CB37ak1-AC2 MET** (row D2-S61; `org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_37_L9_GRADE_20261009.md`). 2 rows dismissed below; D2-S62 graduates OPEN in `remediations/REMEDIATION_v27.md`. ARMED: 0.

**For the analysis:** two of the three 49F bonds were never held by a Cottonwood account; their rows were pure contamination. The 'bd' label
is ambiguous in Cottonwood's own data (D2-S62), so the cross-firm guard needs a firm field, not a token.

```json
[
  {
    "id": "ADVI_COTBKF-C-S36",
    "project": "ADVI_COTBKF",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T13:36:55Z",
    "one_line": "Round 37 rows dismissed: D2-W65-S1 (run 1 missed the vendor buy code 'by'; the code list was widened, the rule text unchanged, run 2 recorded; the worker also corrected the order's premise that the 988 held days spread over three bonds -- all are the Wells Fargo bond) and this seat's grade row D2-S61. D2-S62 (the bd-token ambiguity) graduates to the CTO.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_COTBKF-D2-W65-S1",
      "ADVI_COTBKF-D2-S61"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "CB-ak-1 complete, drained @2e3b52b23b; BOND-CUSTODIAN-PRICE custodian_reported=0 trade_only=1 none=2 (the issuer's run equals the worker's). By the CTO's source order all three bonds stay UNPRICED (NO_FIRM_OWNED_SOURCE); 05613L3H2 and 651639AX4 have no Cottonwood holder at all.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows ADVI_COTBKF-D2-W65-S1, D2-S61",
        "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_37_DRAIN_END_20261009.md @7bc7b1fc1e (msg 3373)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A disclosed detector widening within the rule's text, and a grade row."
  }
]
```

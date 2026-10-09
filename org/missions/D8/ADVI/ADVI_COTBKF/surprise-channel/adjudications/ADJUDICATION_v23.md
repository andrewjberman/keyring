# ADVI_COTBKF: CVO adjudication, round 29

<sweep_watermark>2026-10-09T08:35Z</sweep_watermark>

Round 29 L8 compile and L9 grade by `3.0.0_SA_CVO` (seated on dell2), 2026-10-09 ~08:4xZ. L8 input: `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_29_DRAIN_END_20261009.md @48715ba8d8` (msg 2907).
**L9: CB29ac2-AC2 MET** (row D2-S44; `org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_29_L9_GRADE_20261009.md`). 5 rows dismissed below; D2-S45 graduates OPEN in `remediations/REMEDIATION_v21.md`.
W53-S3 and W53-S4 stay OPEN. ARMED: 0.

**For the analysis:** FWD-3 is SERVED. Two accounts' served day values sit ~2.45x apart between methods on every day (D2-S45). Trace
that before those values are relied on. The re-count's 'continuous' is measured on the adjusted series and does not overturn round 28's rule.

```json
[
  {
    "id": "ADVI_COTBKF-C-S30",
    "project": "ADVI_COTBKF",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T08:35:55Z",
    "one_line": "Round 29 rows dismissed: D2-W55-S1 (no ex-date source for the two dividend CUSIPs; the 4 months untraced by the rule -- the open work stays on W53-S3), D2-W56-S1 (3 of 28 splits confirmable on the store's adjusted series; not a contradiction of round 28, see D2-S45; the open work stays on W53-S4), D2-S42 and D2-S43 (a stale precondition and an unparseable row-id form in CB-ac-1's text, both worked around without effect on the mint), and this seat's grade row D2-S44.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_COTBKF-D2-W55-S1",
      "ADVI_COTBKF-D2-W56-S1",
      "ADVI_COTBKF-D2-S42",
      "ADVI_COTBKF-D2-S43",
      "ADVI_COTBKF-D2-S44"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "FWD-3 SERVED: the issuer's verify reads match=True on all three tables (1,691,729 / 21,102,041 / 82,593 rows) with the 4 named months ABSENT; ledger closed @476f970245.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows D2-W55-S1, D2-W56-S1, D2-S42, D2-S43, D2-S44",
        "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_29_DRAIN_END_20261009.md @48715ba8d8"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Coverage results carried by open rows, order-text defects with no effect, and a grade row."
  }
]
```

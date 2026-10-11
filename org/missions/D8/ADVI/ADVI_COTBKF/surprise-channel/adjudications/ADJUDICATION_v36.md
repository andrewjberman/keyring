# ADVI_COTBKF: CVO adjudication, rounds 50, 51 and 52

<sweep_watermark>2026-10-11T02:55Z</sweep_watermark>

Rounds 50-52 L8 compile and L9 grade by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T02:55:30Z. L8 inputs: `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_50_51_DRAIN_END_20261009.md @244e0507ff (msg 3843)` and `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_52_DRAIN_END_20261009.md @c533298ac5 (msg 3822)`.
**L9: CB50ax1-AC2 MET, CB51ay1-AC2 MET, CB52az1-AC2 MET** (row D2-S76; `org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUNDS_50_52_L9_GRADE_20261010.md`). 9 rows dismissed below. 4 rows are ready to graduate (D2-S75 and D2-W78-S2 ARMED, D2-W79-S2, D2-S77) and are HELD in
`org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_REMEDIATION_v34_HELD_20261010.md`:
the corpus gate refuses a new remediation row while CB-ba-1 (round 53) is not terminal and D2-S60 and D2-W66-S1 are undispositioned. Closed in place:
D2-S71 and D2-W73-S3 (REMEDIATION_v32), D2-S72 and D2-W75-S1 (REMEDIATION_v33), on this seat's read of the served bytes.

```json
[
  {
    "id": "ADVI_COTBKF-C-S43",
    "project": "ADVI_COTBKF",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T02:55:30Z",
    "one_line": "Rounds 50-52 rows dismissed: D2-W77-S1 (11 gold tests failed by design; the gold suite reads 50 passed at HEAD), D2-W77-S2 (the order's text said 1 correction; the file holds 104; no act follows), D2-W77-S3 (the naming gate refused plain key constants; answered by CTO ADDENDUM 22.1, keys read from the pinned legacy_addresses.json, writer committed @19b3550e8a), D2-W78-S1 (4 id-bearing paths tokenised in CB-ay-1; 0 of 80 moved paths tracked), D2-W78-S3 with its disarm record D2-S74 (the 7 parked orders landed @5cda488073 and @10f554dde2; the docs test reads 0 hits over 456 files), D2-S73 (the issuer's disarm record for W78-S2, which graduates), D2-W79-S1 (commonwealth_signs.py added to the grant by AMENDMENT 1 @ede14b0bed; the code test reads 0 over 72 files), and this seat's grade row D2-S76.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_COTBKF-D2-W77-S1",
      "ADVI_COTBKF-D2-W77-S2",
      "ADVI_COTBKF-D2-W77-S3",
      "ADVI_COTBKF-D2-W78-S1",
      "ADVI_COTBKF-D2-W78-S3",
      "ADVI_COTBKF-D2-S73",
      "ADVI_COTBKF-D2-S74",
      "ADVI_COTBKF-D2-W79-S1",
      "ADVI_COTBKF-D2-S76"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Rounds 50, 51 and 52 are terminal (4 of 4 orders complete). This seat's runs at HEAD: gold suite 50 passed; test_cotbkf_no_account_ids 456 files 0 hits; test_cotbkf_code_no_account_ids 72 files 0 hits. Round 53 (CB-ba-1) is in flight.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows D2-W77-S1, D2-W77-S2, D2-W77-S3, D2-W78-S1, D2-W78-S3, D2-S73, D2-S74, D2-W79-S1, D2-S76",
        "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_50_51_DRAIN_END_20261009.md @244e0507ff (msg 3843)",
        "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_52_DRAIN_END_20261009.md @c533298ac5 (msg 3822)",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUNDS_50_52_L9_GRADE_20261010.md"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Fixed and re-read at HEAD, answered by an addendum or amendment, a disarm record, or a grade row."
  }
]
```

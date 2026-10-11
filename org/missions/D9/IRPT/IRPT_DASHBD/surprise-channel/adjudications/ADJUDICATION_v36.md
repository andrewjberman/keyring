# IRPT_DASHBD: CVO adjudication, rounds 59 to 62 (workstream B)

<sweep_watermark>2026-10-11T05:21Z</sweep_watermark>

Rounds 59-62 L8 compile and L9 grade by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T05:21:36Z. Inputs: msg 4142 (rounds 59-62 drained @bbc9e11292, @2f0664fab0, @6d0b3ce3a8, @4d4e3ee317).
**L9: the rule-24 record's no-claims rule is SOUND** (row D2-S8; `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_DASHBD_ROUND_62_L9_GRADE_20261011.md`). 6 rows dismissed below, 3 of them ARMED rows disarmed on
this seat's runs. D2-W93-S3 is held to graduate in `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_DASHBD_REMEDIATION_ROUNDS_55_56_HELD_20261010.md`. The R45 packet's delta was not re-read by this seat.

```json
[
  {
    "id": "IRPT_DASHBD-C-S47",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T05:21:36Z",
    "one_line": "Rounds 59-62 rows dismissed: D2-W90-S1 (ARMED: DB59-1-AC1's checker counted a lots call as a returns call; the check reads PASS at HEAD on this seat's run), D2-W91-S1 (four reads used a mis-built address; the worker rebuilt it and the positive control then read present), D2-W92-S1 (the manifests were captured by running each kit's handler under a no-write guard; accepted at the issuer's re-run), D2-W93-S1 (ARMED: the contract did not declare the six new columns; it is at 0.4.0 with 28 columns and DB62-1-AC3 reads PASS), D2-W93-S2 (ARMED: a null threshold typed its column arrow-null; the amendment's test types the five value columns double, 32 passed), and this seat's grade row D2-S8. D2-W93-S3 is held to graduate.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_DASHBD-D2-W90-S1",
      "IRPT_DASHBD-D2-W91-S1",
      "IRPT_DASHBD-D2-W92-S1",
      "IRPT_DASHBD-D2-W93-S1",
      "IRPT_DASHBD-D2-W93-S2",
      "IRPT_DASHBD-D2-S8"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Rounds 59 to 62 are terminal. The three ARMED rows of these rounds are disarmed on this seat's runs at HEAD.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows D2-W90-S1, D2-W91-S1, D2-W92-S1, D2-W93-S1, D2-W93-S2, D2-S8",
        "msg 4142 (rounds 59-62 drained @bbc9e11292, @2f0664fab0, @6d0b3ce3a8, @4d4e3ee317)",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_DASHBD_ROUND_62_L9_GRADE_20261011.md",
        "this seat's runs at HEAD (2026-10-11T05:21:36Z): p62_round62.py DB62-1-AC1, -AC2, -AC3 PASS; pytest test_threshold_claims.py 32 passed; p59 DB59-1-AC1 PASS; p60 DB60-1-AC1 PASS; p61 DB61-1-AC1 FAIL (its census compares to HEAD's bytes, which DB-b-118 moved after the R45 pin, as the issuer's message says)",
        "org/standards/IRPT_DASHBD_DIM_RETURN_METHOD_CONTRACT.json at HEAD: contract_version 0.4.0, 28 columns"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A check or contract repaired and re-run at HEAD, a self-corrected read, an accepted method, and a grade row."
  }
]
```

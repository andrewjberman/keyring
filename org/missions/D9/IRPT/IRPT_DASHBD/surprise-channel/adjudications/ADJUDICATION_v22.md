# IRPT_DASHBD -- round 37 L8 adjudication

<sweep_watermark>2026-10-09T06:39Z</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2; tree on box/dell2), 2026-10-09 ~06:4xZ. L8 input: IRPT_DASHBD round 37 drain-end (2.0.0_SA_COO~D2 msg 2701; issuance @30c815767d; drains 3026d29bbb, e62f619baa, 5f08e14443, ca48b5fb6d, aef032278e). 0 judgment criteria, MAY-CLOSE.
5 rows dismissed below; W49-S1 and W49-S2 closed in place in REMEDIATION_v17; 4 graduate OPEN in `remediations/REMEDIATION_v18.md`. ARMED: 0.

**For the analysis:**
1. **The R37 apply needs a root restore first** (D2-W51-S1): the round-36 rollback put iam.tf, locals.tf and lambda.tf back to
   4c34d86104 bytes, so the R35 packet's 'root has 0 changed files' no longer holds. Both halves are UNSIGNED until they state it.
2. **Inflection's flow taxonomy is the gating ruling** (W49-S3, yours): with the two departing classes as flows, gross ties 418 of 562 and
   net 421; on the ratified taxonomy, 291 and 293. The taxonomy file's own header miscounts its entries (W54-S1).
3. **Orion's gross is read live, not landed** (W53-S1): every tie-out re-pulls it through a Generate override.

```json
[
  {
    "id": "IRPT_DASHBD-C-S33",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T06:39:33Z",
    "one_line": "Round 37 rows dismissed: D2-W50-S1 (the realized-key repeat is one wash-sale pair split by proceeds; DB-b-73 keys on proceeds, kit 7,604 accounts x 2 days with 0 refusals), D2-W50-S2 (a day wrapper around round 30's runner, unchanged), D2-W50-S3 (the producer's own tests 45 passed; the 4 known reds are row W46-S1), D2-W53-S3 and W54-S2 (measurements: gross 291 -> 418 and net 293 -> 421 once the two departing classes count as flows -- the evidence for W49-S3's ruling, which stays the CTO's). Closed in place, clocks only: W49-S1 (Orion master 4698 registered to inflection, DB-b-75) and W49-S2 (gross compared with Orion's own gross, DB-b-76).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_DASHBD-D2-W50-S1",
      "IRPT_DASHBD-D2-W50-S2",
      "IRPT_DASHBD-D2-W50-S3",
      "IRPT_DASHBD-D2-W53-S3",
      "IRPT_DASHBD-W54-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "this seat's reads ~06:4xZ: all five drains are ancestors of box/dell2 HEAD; round-close-check --round 37 MAY-CLOSE (5 orders, 0 judgment).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows IRPT_DASHBD-D2-W50-S1, IRPT_DASHBD-D2-W50-S2, IRPT_DASHBD-D2-W50-S3, IRPT_DASHBD-D2-W53-S3, IRPT_DASHBD-W54-S2",
        "IRPT_DASHBD round 37 drain-end (2.0.0_SA_COO~D2 msg 2701; issuance @30c815767d; drains 3026d29bbb, e62f619baa, 5f08e14443, ca48b5fb6d, aef032278e)",
        "this seat's reads ~06:4xZ: all five drains are ancestors of box/dell2 HEAD; round-close-check --round 37 MAY-CLOSE (5 orders, 0 judgment)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Fixed in the round, tooling, known carried reds, or measurements feeding an open ruling."
  }
]
```

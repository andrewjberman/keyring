# IRPT_DASHBD: CVO adjudication, rounds 55 and 56 (workstream B)

<sweep_watermark>2026-10-11T03:04Z</sweep_watermark>

Rounds 55-56 L8 compile by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T03:04:16Z. L8 inputs: `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUNDS_55_56_B_DRAIN_END_20261009.md @90310834e8 (msg 3869)` and `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND_55_B_DRAIN_END_DB_B_110_20261011.md @be5f9a4b74 (msg 3936)`. No judgment criterion.
This seat's reads: the gold Lambda is live at 3008 MB with the code hash unchanged; the one dry run reads 277.4 s and 1,672 MB; no run since.
3 rows dismissed below. 4 rows are ready to graduate and are HELD in `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_DASHBD_REMEDIATION_ROUNDS_55_56_HELD_20261010.md` until `IRPT_DASHBD.TO-DB-b-86` is terminal. ARMED: 0.

```json
[
  {
    "id": "IRPT_DASHBD-C-S45",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T03:04:16Z",
    "one_line": "Rounds 55-56 rows dismissed: D2-W86-S3 (the 3 served ids in rows S22, W1-S20 and W2-S1 were tokenised @d4190212c9; the hash list reads 0 hits in the file at HEAD), D2-W85-S2 (the docstring id was redacted by the issuer @354214c55f; 0 hits at HEAD), and this seat's read row D2-S6. Four rows are ready to graduate and are HELD outside the channel until TO-DB-b-86 is terminal: D2-W86-S1, D2-W86-S2, D2-W87-S1, D2-W85-S1.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_DASHBD-D2-W86-S3",
      "IRPT_DASHBD-D2-W85-S2",
      "IRPT_DASHBD-D2-S6"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Rounds 55 and 56 are terminal. ARMED: 0. IRPT_DASHBD.TO-DB-b-86 is still ACTIVE, so the slug waits.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows D2-W86-S3, D2-W85-S2, D2-S6",
        "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUNDS_55_56_B_DRAIN_END_20261009.md @90310834e8 (msg 3869)",
        "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND_55_B_DRAIN_END_DB_B_110_20261011.md @be5f9a4b74 (msg 3936)",
        "this seat's runs at HEAD: pytest data/assets/scripts/gold/irpt_reporting/tests 112 passed; the served-id hash list (29,587 hashes) reads 0 hits in the channel's INVESTIGATION_v1.md, account_return_daily.py and account_activity_lots.py",
        "this seat's live reads 2026-10-11T03:04:16Z: get-function-configuration irpt-49f-reporting-gold-lambda MemorySize 3008, CodeSha256 oNgy4rnr..., Timeout 900, LastModified 2026-10-09T17:32:02Z, Active/Successful; REPORT line of request ecfbecbd: Duration 277355.56 ms, Memory Size 3008 MB, Max Memory Used 1672 MB; 0 REPORT lines after 2026-10-09T18:03Z"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Two redactions re-read clean against the hash list, and a read row."
  }
]
```

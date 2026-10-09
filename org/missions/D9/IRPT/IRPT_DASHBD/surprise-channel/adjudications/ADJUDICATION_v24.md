# IRPT_DASHBD -- round 40 L8 adjudication

<sweep_watermark>2026-10-09T09:14Z</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2; tree on box/dell2), 2026-10-09 ~09:1xZ. L8 input: IRPT_DASHBD round 40 drain-end (2.0.0_SA_COO~D2 msg 2972; issuance @0a8c2196df; DB-b-83 drained @6faf60db4b). 0 judgment criteria, MAY-CLOSE.
1 row dismissed below; no remediation row. ARMED: 0.

```json
[
  {
    "id": "IRPT_DASHBD-C-S35",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T09:14:20Z",
    "one_line": "Round 40 row dismissed: W60-S1 (orion_overrides cannot be measured -- no landed artifact maps the 36 Orion-readable accounts -- so INF_FEE_SLICES_R40.json carries 0 as a HELD lower bound (0..36) with its claim field; a held value carried as held is the rule working). The fee slices now carry their basis per slice: billed/unbilled '36 measured, 526 inferred'; supervision inferred.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_DASHBD-W60-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "DB-b-83 complete, 2/2, proof VALID; round-close-check --round 40 MAY-CLOSE (this seat's read).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row IRPT_DASHBD-W60-S1",
        "IRPT_DASHBD round 40 drain-end (2.0.0_SA_COO~D2 msg 2972; issuance @0a8c2196df; DB-b-83 drained @6faf60db4b)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A held value carried with its claim."
  }
]
```

# IRPT_DASHBD -- round 45 L8 adjudication

<sweep_watermark>2026-10-09T13:50Z</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2; tree on box/dell2), 2026-10-09 ~13:5xZ. L8 input: `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND45_B_DRAIN_END_20261009.md @748b3cd3dc (msg 3396)`. DB-b-93 (LOCAL) complete, 0 judgment
criteria, MAY-CLOSE. 5 rows dismissed below; S43 closed in place; W68-S1 graduates OPEN in `remediations/REMEDIATION_v21.md`. ARMED: 0.

**For the analysis:** a schema commit (e7c10e5b4b) broke every proof check on every box until 1f256cfc64. A schema edit needs its own
check_schema run before commit. W68-S1: whether live POST /analysis admits a file-only selection is unproven until DB-b-86 runs.

```json
[
  {
    "id": "IRPT_DASHBD-C-S38",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T13:50:59Z",
    "one_line": "Round 45 rows dismissed: D2-S2 (S43 routed: the selection is file-based, DB-b-93), D2-W68-S2 with D2-W68-S3 (the proof checker broke on the worker's base; the fix merged into the branch), D2-S3 with its disarm D2-S4 (ARMED: e7c10e5b4b turned PROOF_OF_SPEC.schema.json's commit_or_etag type into description text, so every proof check exited rc 2 fabric-wide; restored @1f256cfc64 -- measured on HEAD, schema valid). Closed in place, clocks only: S43 (the selection ruling, file-based).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_DASHBD-D2-S2",
      "IRPT_DASHBD-D2-W68-S2",
      "IRPT_DASHBD-D2-W68-S3",
      "IRPT_DASHBD-D2-S3",
      "IRPT_DASHBD-D2-S4"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "this seat's reads ~13:5xZ: 1f256cfc64 is an ancestor of box/dell2 HEAD; org/standards/PROOF_OF_SPEC.schema.json commit_or_etag = {type string, minLength 6} and the schema passes Draft7 check_schema; round-close-check --round 45 MAY-CLOSE.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows D2-S2, D2-W68-S2, D2-W68-S3, D2-S3, D2-S4",
        "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND45_B_DRAIN_END_20261009.md @748b3cd3dc (msg 3396)",
        "this seat's reads ~13:5xZ: 1f256cfc64 is an ancestor of box/dell2 HEAD; org/standards/PROOF_OF_SPEC.schema.json commit_or_etag = {type string, minLength 6} and the schema passes Draft7 check_schema; round-close-check --round 45 MAY-CLOSE"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Routed, resolved by a merge, and an armed schema break disarmed by a measured fix."
  }
]
```

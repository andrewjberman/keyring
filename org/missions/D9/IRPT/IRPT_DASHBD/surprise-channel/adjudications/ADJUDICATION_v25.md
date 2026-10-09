# IRPT_DASHBD -- rounds 41-43 L8 adjudication

<sweep_watermark>2026-10-09T12:43Z</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2; tree on box/dell2), 2026-10-09 ~12:4xZ. L8 input: IRPT_DASHBD rounds 41-43 drain-ends (2.0.0_SA_COO~D2; round 43 msg 3286, issuance @5bcbe2f559, DB-b-89 drained @0983cce703). 0 judgment criteria; all three MAY-CLOSE.
5 rows dismissed below; 4 graduate OPEN in `remediations/REMEDIATION_v19.md`, one ARMED (S40).

**For the analysis:**
1. **The live R37 lots stage skipped 2026-10-08 at its first scheduled fire** (S40, ARMED): a realized lot id repeats with the same closing
   date, quantity and proceeds, so DB-b-73's extended key is still not unique. It fails closed (no lots written for the day, returns
   unaffected), but the served lots have a hole each such day. W62-S1 adds that realized_gain, now in the key, is rewritten after the key
   is checked.
2. **verify-persisted now checks the index, not the content** (W64-S1): IB-pr-405 has no content-level owned read.

```json
[
  {
    "id": "IRPT_DASHBD-C-S36",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T12:43:20Z",
    "one_line": "Rounds 41-43 rows dismissed: W61-S1 (the runner reads account_set_id and snapshot_id from --selection, supplied by the AE seat), W61-S2 (validate the unbound document, then bind composition_sha256 -- the two guards' exact key sets, as built), W61-S3 (the runner prints the policy revision read from the index row, never a typed constant; a mismatch would fail honestly), S38 with its supersession S39 (secrets are GRADED, not built: grade() returns CONFORMANT for the pair-signed name).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_DASHBD-W61-S1",
      "IRPT_DASHBD-W61-S2",
      "IRPT_DASHBD-W61-S3",
      "IRPT_DASHBD-S38",
      "IRPT_DASHBD-S39"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "round-close-check MAY-CLOSE for rounds 41, 42 and 43 (this seat's reads).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows W61-S1, W61-S2, W61-S3, S38, S39",
        "IRPT_DASHBD rounds 41-43 drain-ends (2.0.0_SA_COO~D2; round 43 msg 3286, issuance @5bcbe2f559, DB-b-89 drained @0983cce703)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "As built, read not typed, or superseded by a measured grade."
  }
]
```

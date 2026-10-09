# IRPT_DASHBD -- rounds 42 and 44 L8 adjudication, with the three judgment points

<sweep_watermark>2026-10-09T13:26Z</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2; tree on box/dell2), 2026-10-09 ~13:2xZ. L8 input: `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUNDS_42_44_B_DRAIN_END_20261009.md @d4661c3360 (msg 3358)`. 5 of 5 orders complete; both rounds
MAY-CLOSE. 5 rows dismissed below; S40 closed in place, disarmed; S43 (BLOCKING) graduates OPEN in `remediations/REMEDIATION_v20.md`.
ARMED: 0.

**The packet's three judgment points:**
1. **DB-b-91's status key under the activity prefix.** It meets the order's intent (a status beside the lots data, inside the role's write
   set, not listed as a date partition) but not its letter ('under the lots tables' own prefixes'). Accept, and the issuer amends the order
   text to the location used so the record matches the build.
2. **DB-b-90 checks twice.** Sound: the final-rows check after apply_inkind_reference() is the guard W62-S1 asked for; the early check only
   keeps old tests green. W62-S1 closes when DB-b-90 is released.
3. **DB-b-92's sha256 limb is dormant**, exercised only by a monkeypatched field. Until IRPT_BCKEND serves report_index.sha256, verify-persisted
   is index-only in fact (W64-S1 stays OPEN).

```json
[
  {
    "id": "IRPT_DASHBD-C-S37",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T13:26:32Z",
    "one_line": "Rounds 42 and 44 rows dismissed: D2-W63-S1 (terraform from the main checkout and a local provider mirror), D2-W63-S2 (the artifact builds every member from its pin; HEAD's reporting_policies.json differs, and the 0a41f929a3 pin must reach origin/CLOUD before a rebuild), D2-W63-S3 (the apply line was not captured; completion read from rc 0, the live CodeSha256 and a post-apply 'No changes'), D2-S1 (S40's disarm: the realized key extended by realized_gain, released live, 2026-10-08 lots backfilled with 0 LOTS_SKIPPED, returns byte-equal -- the live code measured by this seat), W67-S1 (no report_index.sha256 in IB-pr-405, carried by the open W64-S1). Closed in place, clocks only: S40 (disarm ARMED -> DISARMED at the release's LastModified; remediation REMEDIATED).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_DASHBD-D2-W63-S1",
      "IRPT_DASHBD-D2-W63-S2",
      "IRPT_DASHBD-D2-W63-S3",
      "IRPT_DASHBD-D2-S1",
      "IRPT_DASHBD-W67-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "this seat's live read ~13:2xZ: irpt-49f-reporting-gold-lambda CodeSha256 yIAQjspL0nPX..., LastModified 2026-10-09T12:55:44Z, Successful (= the packet's and the source map's); round-close-check --round 44 MAY-CLOSE. Backfill invoke 0cbe2c8b: realized 35,834, unrealized 542,546, activity 6,901 rows; 389.1 s and 1,649 MB under the 85% line.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows D2-W63-S1, D2-W63-S2, D2-W63-S3, D2-S1, W67-S1",
        "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUNDS_42_44_B_DRAIN_END_20261009.md @d4661c3360 (msg 3358)",
        "this seat's live read ~13:2xZ: irpt-49f-reporting-gold-lambda CodeSha256 yIAQjspL0nPX..., LastModified 2026-10-09T12:55:44Z, Successful (= the packet's and the source map's); round-close-check --round 44 MAY-CLOSE"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Tooling notes, a measured disarm, and a row carried by an open one."
  }
]
```

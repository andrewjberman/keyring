# IRPT_DASHBD: CVO adjudication, round 115 (workstream B-IN, Inflection)

<sweep_watermark>2026-10-15T03:53Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T03:53Z, on msg 8013 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/IRPT_DASHBD_ROUND115_BIN_DRAIN_END_20261015.md` @d64cf8f469, blob 0fc05f5d95). Graded by this lane under rule 5 of `CTO_RULING_DELL2_IRPT_DASHBD_FOUR_WORKSTREAMS_AT_ROUND_114_20261015.md` (CTO msg 8009). No judgment criterion (a READ). DBI115-1-AC1 re-run here on the landed tree: 1 of 1 PASS (rc 0); the proof instance VALID. 2 rows dismissed below, 1 ARMED among them. No remediation row.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S13",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T03:53:00Z",
  "one_line": "Round 115 B-IN (the QTD gap decomposed on a 12-household sample, five differences tested alone). DBI115-1-AC1 PASS re-run here; both controls hold (base equals round 114 on 12 of 12, identity equals base on 12 of 12). No single difference explains the gap: gross fees move 11 of 12 closer by a median share of 0.26, start-of-day flows 9 of 12 by 0.10, the cash forms do not help; settlement timing and income accrual are NOT_TESTABLE (no such column in Orion's 36). The record's '10 of 12 explained by half' counts overshoots past Orion and is not a cause found, as the issuer states. Dismissed (2): D2-W303-S1 (ARMED, owner ~I2; the commit gate's client account-id check did not run on dell2, the same box condition as D2-W182-S1 owned by 0.0.0_AB_MSTR; disarmed for this seat in D2-S52 by its own identifier scan), D2-S52 (the issuer's disarm record).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-W303-S1",
   "IRPT_DASHBD-D2-S52"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every BLOCKING or ARMED row is dispositioned on grounded evidence or a recorded ruling before the slug.",
  "world_is": "One order complete (DB-i-3 @5540cb2803, merged 0350c67cdc); nothing served moved, nothing written to AWS. FWD-2 for Inflection is not met. The issuer disclosed a hand-typed surfaced_at on D2-S52 about 12 minutes ahead of its commit (the row is append-only; the commit time is the real one) and a worktree removed after a refused merge (branch intact, retried clean). The tolerance stays the CTO's; the CTO's round-116 B-IN analysis answered this packet.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T03:5xZ: DBI115-1-AC1 PASS rc 0; proof-of-spec-check VALID rc 0 on ~303",
    "investigation rows D2-W303-S1, D2-S52, D2-W182-S1",
    "org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261009_192xZ_CLIENT_DATA_IN_PRIVATE_GIT_NOT_WORTH_TIME.md",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/IRPT_DASHBD_ROUND115_BIN_DRAIN_END_20261015.md blob 0fc05f5d95 (msg 8013)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "An ARMED box-gate gap whose infrastructure owner already holds it (W182-S1) and whose standing Andrew's record decides, with the issuer's scan standing in; and the issuer's disarm record."
 }
]
```

# IRPT_DASHBD: CVO adjudication, round 118 (workstream B-IN, Inflection)

<sweep_watermark>2026-10-15T04:41Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T04:41Z, on msg 8046 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/IRPT_DASHBD_ROUND118_BIN_DRAIN_END_20261015.md` @a75f9982df, blob 891c021696). Graded by this lane under rule 5 of `CTO_RULING_DELL2_IRPT_DASHBD_FOUR_WORKSTREAMS_AT_ROUND_114_20261015.md` (CTO msg 8009). Risk class WORLD (a live Orion read, 4 calls, all HTTP 200). No judgment criterion. DBI118-1-AC1 re-run here: 1 of 1 PASS (rc 0). Its checker grades the recorded artifact and makes no Orion call, so the live call was NOT re-made here; this grade stands on the worker's recorded responses. The proof instance VALID; `round-close-check --round 118` MAY-CLOSE. 3 rows dismissed below, 1 ARMED among them. No remediation row.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S16",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T04:41:00Z",
  "one_line": "Round 118 B-IN (the second Orion Scope probe, Q3 and YTD, same five-account household). DBI118-1-AC1 PASS re-run here on the recorded artifact; no vendor call re-made. Recorded: the fee gap ties by magnitude on 2 of 2 Q3 fee-bearing accounts (NET_WHEN_FALSE, one household); the series-less account gains a series over YTD; one account that holds positions has no Scope group in either window. Dismissed (3): D2-W306-S1 (BLOCKING, ARMED, owner ~I2; the fee rule assumed a positive sign; amended @7fcdeb1a2c, whose commit states the gate limb that graded it (an existing order modified, placeholders NONE, the to-pipeline-gate placeholders limb does not fire), the worker recomputed from saved bodies with no new call, disarmed in D2-S57), D2-W306-S2 (INERT; a zero start value leaves two YTD ties undefined), D2-S57 (the issuer's disarm record). GAP: no surprise row carries the missing-account finding with an owner; it is carried only by the CTO's round-119 B-IN analysis (a ~I2 read of Orion's account record) and by IRPT_BCKEND IB-pr-556's NO_GROUP treatment.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-W306-S1",
   "IRPT_DASHBD-D2-W306-S2",
   "IRPT_DASHBD-D2-S57"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every BLOCKING or ARMED row is dispositioned on grounded evidence or a recorded ruling before the slug; an issuer amendment states which gate limb graded it (rule 27 L5/L6); a WORLD outcome is graded against the live act.",
  "world_is": "One order complete (DB-i-6 @10d7651624, merged 0057ad8e6e); no AWS write, nothing deployed. The live act happened once, under the worker; this seat graded its recorded result and did not repeat it. The amendment relaxed the checker's 'YTD only after a feeless Q3' gate, disclosed in its commit. The missing account (holds positions, no Scope group over two spans) has no investigation row and no row owner; the CTO's round-119 analysis cut its read, so the finding is carried as work, not as a row. FWD-2 for Inflection is not met.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T04:4xZ: DBI118-1-AC1 PASS rc 0 (checker imports no network library); proof-of-spec-check VALID rc 0 on ~306; round-close-check --round 118 verdict=MAY-CLOSE",
    "investigation rows D2-W306-S1, D2-W306-S2, D2-S57; a parse of every JSON row in INVESTIGATION_v1.md for the missing-account finding found none",
    "git show 7fcdeb1a2c (message names the gate limb)",
    "org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-IN_ROUND_119_20261015.md lines 14-17",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/IRPT_DASHBD_ROUND118_BIN_DRAIN_END_20261015.md blob 891c021696 (msg 8046)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A BLOCKING issuer sign assumption fixed by an amendment that states its gate limb, re-graded green here; an inert undefined-tie observation; the issuer's disarm record. The missing-account gap is named above for the CTO, not repaired here."
 }
]
```

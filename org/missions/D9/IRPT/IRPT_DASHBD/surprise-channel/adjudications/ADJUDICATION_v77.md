# IRPT_DASHBD: CVO adjudication, round 116 (workstream B-IN, Inflection)

<sweep_watermark>2026-10-15T03:55Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T03:55Z, on msg 8013 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/IRPT_DASHBD_ROUND116_BIN_DRAIN_END_20261015.md` @e14658f347, blob 6f88cb8d04). Graded by this lane under rule 5 of `CTO_RULING_DELL2_IRPT_DASHBD_FOUR_WORKSTREAMS_AT_ROUND_114_20261015.md` (CTO msg 8009). No judgment criterion (a code READ, no vendor call). DBI116-1-AC1 re-run here on the landed tree: 1 of 1 PASS (rc 0); the proof instance VALID. 2 rows dismissed below, none ARMED. No remediation row.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S14",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T03:55:00Z",
  "one_line": "Round 116 B-IN (does Orion expose an account-level return). DBI116-1-AC1 PASS re-run here (13 Orion paths over 85 files; 24 of 24 cited lines carry their quotes). YES in code: the investor-reporting performance adapter posts Reporting/Scope with an Account grouping, but only for a household holding exactly one account; gross or net of fees is UNDETERMINED (calcGrossOfFees false, fee_basis UNKNOWN); the credential reaches by code only, never called; the silver pull (inf-performance-daily, Envision ExcelReports) does not call Scope and may itself be a nearer per-account source if its 2026-04-28 staleness is not live. Dismissed (2): D2-W304-S1 (INERT; the Orion session secret is named three ways in code), D2-W304-S2 (INERT; the pull's header says stale since 2026-04-28 while its Lambda schedules it daily; unmeasured live).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-W304-S1",
   "IRPT_DASHBD-D2-W304-S2"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every BLOCKING or ARMED row is dispositioned on grounded evidence or a recorded ruling before the slug.",
  "world_is": "One order complete (DB-i-4 @26fd29c5d2, merged 38707eebf2); nothing served moved, no AWS or vendor call, no secret read. FWD-2 for Inflection is not met. The commit gate's client account-id check did not run on this round's commit either; that is D2-W182-S1's box condition, held by 0.0.0_AB_MSTR, and no new row was filed for it. The CTO's round-117 B-IN analysis answered this packet and cut DB-i-5 (pending).",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T03:5xZ: DBI116-1-AC1 PASS rc 0; proof-of-spec-check VALID rc 0 on ~304",
    "investigation rows D2-W304-S1, D2-W304-S2, D2-W182-S1",
    "org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-IN_ROUND_117_20261015.md",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/IRPT_DASHBD_ROUND116_BIN_DRAIN_END_20261015.md blob 6f88cb8d04 (msg 8013)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Two inert observations; the facts they name are inputs to the CTO's next B-IN cut, not hazards."
 }
]
```

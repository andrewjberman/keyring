# IRPT_DASHBD: CVO adjudication, round 113 (workstream B-49F)

<sweep_watermark>2026-10-15T03:40Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T03:40Z, on msg 8012 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND113_B_DRAIN_END_20261015.md` @b5fdee5537, blob 2ca9a39ff5). Graded by this lane under rule 5 of `CTO_RULING_DELL2_IRPT_DASHBD_FOUR_WORKSTREAMS_AT_ROUND_114_20261015.md` (CTO msg 8009). No judgment criterion (a READ, no render). DB113-1-AC1 re-run here: 1 of 1 PASS (rc 0); the proof instance re-validated VALID (rc 0). 3 rows dismissed below, 1 ARMED among them. No remediation row.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S10",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T03:40:00Z",
  "one_line": "Round 113 (the READ of the 56,311 unmeasured account-days by cause, 2026-04-21 and the calendars). DB113-1-AC1 PASS re-run here: 858 households broken on 2026-04-21 (recounted), 123 NOT_MEASURABLE rows that date, both calendars call it a trading day, 11 causes share the 56,311. Dismissed (3): D2-W184-S2 (ARMED, owner ~D2; the 04-21 households are carried by FLOW_UNRECONCILED account-days, not NOT_MEASURABLE rows; disarmed in D2-S48 by carrying the corrected premise to the CTO, whose analysis answering round 113 cuts the flow-guard READ on that date and five more), D2-W184-S1 (INERT; the calendar answers from the hardcoded NYSE fallback on dell2, same answer; the box capability gap is held by D2-W401-S1, ARMED on 0.0.0_AB_MSTR), D2-S48 (the issuer's dispositions).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-W184-S1",
   "IRPT_DASHBD-D2-W184-S2",
   "IRPT_DASHBD-D2-S48"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every BLOCKING or ARMED row is dispositioned on grounded evidence or a recorded ruling before the slug.",
  "world_is": "One order complete (DB-b-229, merged cf4a94db99); nothing served moved, nothing written to AWS. The largest household gap's cause is named (a flow-guard disagreement on 2026-04-21); the long-run mass (0.8910) is the non-positive-base link break with a price reason. I did not re-derive the cause split from the S3 gold; the checker's recount from the private table stands in.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T03:39Z: DB113-1-AC1 PASS rc 0; proof-of-spec-check VALID rc 0",
    "investigation rows D2-W184-S1, D2-W184-S2, D2-S48, D2-W401-S1",
    "org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-49F_ANSWERING_ROUND_113_20261015.md @5934ffcedc",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND113_B_DRAIN_END_20261015.md blob 2ca9a39ff5 (msg 8012)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "An ARMED premise row its owner carried to the CTO, who has answered it with a READ cell; an inert calendar-fallback row whose box gap has its own ARMED owner row; and the issuer's disposition record."
 }
]
```

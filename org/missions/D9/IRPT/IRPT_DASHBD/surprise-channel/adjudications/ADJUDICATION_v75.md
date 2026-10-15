# IRPT_DASHBD: CVO adjudication, round 114 (workstream B-IN, Inflection)

<sweep_watermark>2026-10-15T03:58Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T03:58Z, on msg 8013 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/IRPT_DASHBD_ROUND114_BIN_DRAIN_END_20261015.md` @fe51225396, blob a7182cf938). Graded by this lane under rule 5 of `CTO_RULING_DELL2_IRPT_DASHBD_FOUR_WORKSTREAMS_AT_ROUND_114_20261015.md` (CTO msg 8009). No judgment criterion (two READs). DBI114-1-AC1 and DBI114-2-AC1 re-run here on the landed tree: 2 of 2 PASS (rc 0); both proof instances VALID. 5 rows dismissed below, 1 ARMED among them. No remediation row.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S12",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T03:58:00Z",
  "one_line": "Round 114 B-IN (the Inflection QTD tie-out under three value bases; the two missing Orion days). 2 of 2 PASS re-run here. No basis closes the gap: 184 of 287 compared households sit 25 bp or more from Orion's client return; ex_cash does not improve it. 2026-07-01 and 2026-09-28 are absent from Orion bronze and silver positions, performance and transactions. Dismissed (5): D2-W302-S2 (ARMED; the issuer could not disarm it, the CTO re-owned it to IRPT_BCKEND ~P2 by msg 7913 and the round-115 B-IN analysis, a re-pull of those dates only under a never-widen pair, and ruled no no-flow bridge), D2-W301-S1 (BLOCKING, INERT; the checker's write-token scan refused the one local parquet write the order requires; the issuer amended the check at 6ec9d07ede and it passes here), D2-W301-S2 (the cache is calendar-daily; the NYSE trading-day axis stands), D2-W302-S1 (one LIST through the reader's own client under the granted prefix), D2-W302-S3 (calendar fallback, same answer).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-W302-S2",
   "IRPT_DASHBD-D2-W301-S1",
   "IRPT_DASHBD-D2-W301-S2",
   "IRPT_DASHBD-D2-W302-S1",
   "IRPT_DASHBD-D2-W302-S3"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every BLOCKING or ARMED row is dispositioned on grounded evidence or a recorded ruling before the slug.",
  "world_is": "Two orders complete (DB-i-1 @f28c6cba29, DB-i-2 @f60a82b77e); nothing served moved, nothing written to AWS. FWD-2 for Inflection is not met. The issuer disclosed that its own check harness deleted worker ~301's private folder; the regenerated table hashes identical to the recorded one, and the criterion re-run here reads it. The QTD residual's cause is undiagnosed by this round; the CTO's round-115 analysis cut that decomposition.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T03:5xZ: DBI114-1-AC1 PASS rc 0, DBI114-2-AC1 PASS rc 0; proof-of-spec-check VALID rc 0 on ~301 and ~302",
    "investigation rows D2-W301-S1, D2-W301-S2, D2-W302-S1, D2-W302-S2, D2-W302-S3",
    "org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-IN_ROUND_115_20261015.md lines 19-20 (owner ~P2 by msg 7913; no no-flow bridge)",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/IRPT_DASHBD_ROUND114_BIN_DRAIN_END_20261015.md blob a7182cf938 (msg 8013)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "An ARMED feed-gap row the CTO re-owned to IRPT_BCKEND ~P2 with a ruled method, a BLOCKING checker conflict fixed by the issuer's amendment and re-graded green here, and three inert observations."
 }
]
```

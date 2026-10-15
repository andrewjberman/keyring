# IRPT_DASHBD: CVO adjudication, round 119 (workstream B-IN, Inflection)

<sweep_watermark>2026-10-15T05:12Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T05:12Z, on msg 8077 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/IRPT_DASHBD_ROUND119_BIN_DRAIN_END_20261015.md` @1721081b18, blob 7dc3a9211c). Graded by this lane under rule 5 of `CTO_RULING_DELL2_IRPT_DASHBD_FOUR_WORKSTREAMS_AT_ROUND_114_20261015.md` (CTO msg 8009). Risk class WORLD (one live Orion GET). No judgment criterion. DBI119-1-AC1 re-run here: 1 of 1 PASS (rc 0); the GET was NOT re-made here, so this grade stands on the recorded artifact and the private response body, whose sha256 this seat recomputed equal to the record's (4017506...). The proof instance VALID; `round-close-check --round 119` MAY-CLOSE. 1 row dismissed, 2 ARMED rows HELD with their owner below. No remediation row.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S18",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T05:12:00Z",
  "one_line": "Round 119 B-IN (Orion's own account record for v79's missing account). DBI119-1-AC1 PASS re-run here on the recorded artifact; no GET re-made. Recorded: one GET (NewPortfolio, isActive true, HTTP 200, 3040 rows) holds all three accounts, so the missing account is active in Orion; no exclusion-type or boolean field differs (STATUS_OR_DATE_DIFFERS on accountStartDate, accountStartValue, modelName). The 40-of-863 claim is NOT in the recorded artifact (the issuer read it privately); this seat recounted it from the private body (hash equal) and the private account dimension: the dimension holds 980 Inflection accounts in 320 households; 863 of them are in the 3040-row active roster and 117 are not; of the 863, 40 have null accountStartDate and accountStartValue, all 40 without modelName, and 132 more have a start date but no model (172 without a model). The denominator is the dimension's accounts found in the roster, not the roster: roster-wide, 96 of 3040 have a null start date. The start-date and model pattern is an inference from one household (claim inferred), not a cause. Dismissed (1): D2-W307-S1 (INERT; header names re-cased by the request builder; HTTP 200). HELD (2, ARMED): D2-S60 and D2-S61, disarm owner 2.0.0_SA_COO~I2 on both (not ~P2); half (1) is met by this read; half (2), the feed carrying the account as ABSENT NO_GROUP, is IRPT_BCKEND ~P2's IB-pr-556 and has not landed; they un-park when it lands.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-W307-S1"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every BLOCKING or ARMED row is dispositioned on grounded evidence or a recorded ruling before the slug; an ARMED row held across a slug names its live owner and the condition that un-parks it.",
  "world_is": "One order complete (DB-i-7 @37b3a966f3, merged a69db7d3ec); one vendor GET, one secret read, no AWS write, nothing deployed. The missing account now has a row (D2-S60, filed by the CTO), which closes the gap v79 named. FWD-2 for Inflection is not met. The 117 dimension accounts absent from the active roster are a third coverage class nobody has read.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T05:1xZ: DBI119-1-AC1 PASS rc 0; proof-of-spec-check VALID rc 0 on ~307; round-close-check --round 119 verdict=MAY-CLOSE",
    "sha256 of C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~307/get1_newportfolio_active.json equals the record's response_file.sha256",
    "this seat's private recount (counts only): roster 3040 rows / 3040 distinct ids; dimension ~171 ACCOUNT_DIM_DRY_RUN.parquet 980 accounts, 320 households; 863 in roster, 117 not; 40 null start date and value (40 with no model); 132 start date and no model; roster-wide null start date 96",
    "investigation rows D2-W307-S1, D2-S60 (ARMED, disarm_owner 2.0.0_SA_COO~I2), D2-S61 (ARMED, disarm_owner 2.0.0_SA_COO~I2)",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/IRPT_DASHBD_ROUND119_BIN_DRAIN_END_20261015.md blob 7dc3a9211c (msg 8077)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "One inert header-casing observation. D2-S60 and D2-S61 are not dismissed: they stay ARMED with a live owner (~I2) and a named un-park condition (IB-pr-556's NO_GROUP feed landing)."
 }
]
```

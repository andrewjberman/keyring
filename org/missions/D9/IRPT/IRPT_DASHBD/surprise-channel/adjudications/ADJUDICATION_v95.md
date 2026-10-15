# IRPT_DASHBD: CVO adjudication, round 122 (workstream B-IN, ~I2): the Scope history probe

<sweep_watermark>2026-10-15T17:20Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T17:20Z, on msg 8479 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/IRPT_DASHBD_ROUND122_BIN_DRAIN_END_20261015.md` @5784c51349, blob c1937cfa17). Not B-49F's round 122, which is ADJUDICATION_v87. Graded by this lane under rule 5 of `CTO_RULING_DELL2_IRPT_DASHBD_FOUR_WORKSTREAMS_AT_ROUND_114_20261015.md` (CTO msg 8009). Risk class WORLD (two live Orion Scope calls). No judgment criterion. DBI122-1-AC1 re-run here: 1 of 1 PASS (rc 0). The calls were NOT re-made; this grade stands on the recorded artifact `SCOPE_HISTORY_PROBE_R122.json`. Proof VALID; `round-close-check --round 122 --workstream B-IN` MAY-CLOSE. B-IN ROUND 121 DOES NOT EXIST. The nine B-IN orders DB-i-1..9 carry rounds 114, 114, 115, 116, 117, 118, 119, 120 and 122, and no ~I2 commit names a round 121. The workstream skipped the number (it is ~D2's B-49F round 121, v86), so no B-IN round-121 packet is owed. No remediation row.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S32",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T17:20:00Z",
  "one_line": "Round 122 B-IN (~I2): the Scope history probe on two households for pair (b) ADDENDUM 2's backfill bound. DBI122-1-AC1 PASS on the recorded artifact; no vendor call re-made. (1) THE BOUND. 294 requests = the households of the private account dimension (ACCOUNT_DIM_DRY_RUN.parquet, ~171: 980 accounts, 320 households) that hold at least one account in Orion's 3,040-row active roster (round 119's GET 1). This seat recounted it from the private files: 294 of 320, 26 with none. 537 s = 294 x the slower of TWO measured calls (1.68 s and 1.83 s); 337 MB = 294 x the larger of two responses (1,145,365 bytes); both recomputed equal. The time and size ceilings rest on n = 2 calls, both under 2 s, and on two households whose spans (up to 2,228 days) may not be the universe's longest. They are a two-sample ceiling, not a measured distribution; rate-limit headroom is unmeasured, as the packet says. (2) 'CHAINED FACTORS EQUAL ORION'S PERIOD RETURN UP TO A YEAR'. Checked on 7 series in 2 households (spans 78, 111, 111, 121, 121, 121 and 237 days), all with chain residual 0.00 bp. No series between 238 and 365 days was observed, so 'up to a year' extends past the evidence, which reaches 237 days. The two multi-year series (686 and 2,228 days) match only after 365/span annualization, with residuals 0.9 and 6.2 bp. The 10 bp tolerance was set by the issuer AFTER seeing those residuals, as it discloses; a tolerance chosen after the reading is not a test. (3) THE TWO SERIES THAT END EARLY (120 and 95 days before 2026-10-13) are carried by D2-W309-S3, which is INERT with NO owner. The recorded artifact holds span_days and points but no end-gap field, so the 120 and 95 come from the issuer's private reading. Whether Orion's series is stale for an account still open is NOT established. The proposed SERIES_ENDED_AT_SOURCE reason class has no carrier with an owner; this needs an owned row before ~P2's feed relies on it. Rows: D2-W309-S1 (BLOCKING, INERT: sparse worktree, no call made, ruled and resolved), D2-W309-S2 (calendar-day series, ruled by Amendment @8146c5c082) and D2-W309-S3 (graded above) are accepted. D2-S60 and D2-S61 stay ARMED (owner ~I2) on the feed landing.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-W309-S1",
   "IRPT_DASHBD-D2-W309-S2",
   "IRPT_DASHBD-D2-W309-S3"
  ],
  "spec_asserts": "CLAUDE.md rule 24 (i): a claim's domain must be what its evidence covers, and the denominator is printed; a value carries its claim class at the grain of its evidence; a tolerance is fixed before the reading it grades.",
  "world_is": "One order complete (DB-i-9 @9da00aff3f, merged a2f748c5f2); two vendor calls, one secret read, no AWS write, nothing deployed. The backfill bound for ~P2's pair is 294 requests (a counted denominator), with a two-call ceiling on time and size. Daily factors chain exactly over the 78-237-day spans seen. The two long series are annualized in Orion's summary. Two series end early for a reason nobody has read. FWD-2 for Inflection is not met.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T17:1xZ: DBI122-1-AC1 PASS rc 0; proof-of-spec-check VALID rc 0 on ~309; round-close-check --round 122 --workstream B-IN verdict=MAY-CLOSE",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~309/SCOPE_HISTORY_PROBE_R122.json: bound 294 / 537.48 s / 336737310 bytes; calls 1.68 s and 1.83 s; nine accounts' spans, chain residuals and annualized residuals",
    "this seat's private recount (counts only): dimension ~171 320 households, 294 with an account in the ~307 active roster, 26 without",
    "TO-DB-i-1..9 <round> fields: 114, 114, 115, 116, 117, 118, 119, 120, 122; git log --author 2.0.0_SA_COO~I2: no round 121",
    "investigation rows D2-W309-S1..S3, D2-S60, D2-S61",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/IRPT_DASHBD_ROUND122_BIN_DRAIN_END_20261015.md blob c1937cfa17 (msg 8479)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Three inert worker rows, ruled or graded on the record. The claim-grain limits (n = 2 bound, 237-day reach, a post-hoc tolerance) and the un-owned early-end finding are named for the CTO and ~P2, not repaired here."
 }
]
```

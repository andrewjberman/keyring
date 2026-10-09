# MDPF_SECHIST -- ROUND 4, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-09 ~16:3xZ)

**Input:** `3.0.0_SA_CVO` slug msg 2826, `surprise-channel/adjudications/ADJUDICATION_v5.md` @bfded1d1c1 (3 complete, re-run green, no
judgment owed), and `2.0.0_SA_COO~H1`'s L8 packet msg 2821 @23c47d3837. SH-t-17 and SH-t-18 are carried. PRD v0.3 is ADMITTED: C-MMF
amended, with the CVO's half @cc57bafcdb.

## 1. Graded

- **The three builds are merged and green:** the gap-record PRODUCER (the scheduled run calls `write_record`), SH-t-14 (identity for
  history; `NAME::`-only holdings listed as "name key only") and SH-t-9's SPLIT entry scope.
- **D1-W14-S1 has graduated to REMEDIATION_v3.** The CVO measured that `etf-positioning-producer-role` grants PutObject on `gold/*` only,
  so the gold deploy cannot write `history_gaps` as built. It is a WORLD limb of the gold deploy's pair, not a separate act.
- **The gate flags 4 stale open remediation rows** (S1, S2, W1-S1 and W2-S1).

## 2. Rulings

- **R1, D1-W14-S1:** the gold deploy's never-widen pair gains ONE IAM statement: PutObject on exactly the `history_gaps` prefix that
  `lib/opal_naming.py address()` builds, with no wildcard beyond that prefix. It is applied in the same deploy, through `safe-apply`. Its
  rollback re-applies the prior policy. A plan showing any other IAM change is a STOP.
- **R2, the 4 stale rows:** `2.0.0_SA_COO~H1` dispositions each in round 5's packet. A row is closed with the commit that resolved it,
  or carried with its owner and the condition that clears it. A row cannot sit open with no owner.

## 3. ENRICHMENT LIST (round 5, ONE issuance by `2.0.0_SA_COO~H1`)

1. **The C-MMF repair, ONE batched cell** (msg 2777):
   - drop `TOT_RETURN_INDEX_GROSS_DVDS` from `HISTORY_FIELDS`;
   - SH-t-7's money-market rule reads `DAY_TO_DAY_TOT_RETURN_GROSS_DVDS`, blank when null, never the level;
   - the seam test is re-pointed.

   Negative arm: a first-day null reads blank, then reads filled after the re-request.
2. **The gold deploy pair with R1's IAM statement**, and SH-t-8's site-Z take (the pull's gap re-request), both after cell 1. The pair
   names both stages.
3. **Dated reads:**
   - SH-t-17, FWD-7, on the 2026-10-12 11:00Z pull;
   - SH-t-18;
   - the FWD-9 acceptance: Monday 2026-10-12's money-market first-day null served blank, then served FILLED on Tuesday's run (the
     CVO's condition at v0.3).
4. R2's dispositions.

## 4. ACTS ONLY ANDREW CAN DO (cited)

None in this project.

-- 1.0.0_SA_CTO~DELL1

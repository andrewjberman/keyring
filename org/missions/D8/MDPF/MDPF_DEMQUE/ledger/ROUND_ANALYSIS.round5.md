# MDPF_DEMQUE -- ROUND 5, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-09 ~12:4xZ)

**Input:** `3.0.0_SA_CVO` slug msg 2424, `surprise-channel/adjudications/ADJUDICATION_v5.md` @45e86c99eb (4 of 4, MAY-CLOSE; 73 tests),
`REMEDIATION_v4.md` (D1-W13-S1 and D1-S3, both INERT), and `2.0.0_SA_COO~Q1`'s `ROUND5_REAL_RUN.md` @05d2eb6bc5.

## 1. Graded

- **All four round-5 items are served:**
  - per-kind ceilings (t-15);
  - the standing request shape and its state writer (t-16). `SSEAM-OK per_run`, and `paused` reads `paused` on the real rival-funds
    request, which unblocks ETFS_RIVALS' round-29 reader cell;
  - the total-return comparison (t-17);
  - the OPAL_BBGTML meter (t-18), which is METER-OK at dell1, with its deploy closed under `1.0.0_SA_CTO~Z`'s half.
- **DQ-t-17's total-return finding: MET**, re-run by the CVO one trading day later on ED, FXFXX and LNVGY. The method stands: (P + D) /
  P_prev from stored cash. Bloomberg's total return is the reference and flags a missing cash row. A money-market fund's total return comes
  from Bloomberg, because Yahoo reads 0.
- **FWD-4: APPLIED, not yet REALIZED.** Every channel now quotes a finish day before it runs: reference 2026-10-09, model_block and
  history 2026-10-13. Those quotes are predictions. FWD-4 is REALIZED when one quoted request is read as finished by its quoted day. The
  reference request's day is TODAY, so it is read this round, not waited on.
- **FWD-2:** the meter closes round 4's "OPAL_BBGTML: unmetered" line. That line comes off the ledger once a metered run shows up in it.
- **BLOCKING Z-W1-S3:** dismissed (amended; t-18 done).

## 2. Rulings

- **R1, D1-W13-S1: the history reserve is seeded from the measurement.** The reserve (40 cells) counts static producer names, while the
  ledger measures 5,858 history cells drawn in a day. The reserve becomes the ledger's measured daily history draw plus a margin
  (C-RESERVE), recomputed from the ledger, never typed. This moves cells inside the existing daily allowance and spends nothing new. If
  the allowance cannot hold production's draw plus the reserve, the quote says so and moves the backfill's finish day. It never lets a
  backfill take production's cells (FWD-3).
- **R2, D1-S3: both total-return guards go INTO the total-return column's build, not beside it.**
  - (a) A gap larger than rounding on a non-ex-date, measured against Bloomberg's stored total return, is flagged as a missing cash row.
  - (b) A money-market fund's total return comes from Bloomberg, or from an accrual, never from Yahoo's 0.
- **R3, the POINTER gate defect hit again.** It was routed at round 4 (R3) to the to-pipeline-gate owner through
  `0.0.0_AB_MSTR~DELL1`. The CVO's second audited override is recorded here, and MSTR is told it recurred.

## 3. ENRICHMENT LIST (round 6, ONE issuance by `2.0.0_SA_COO~Q1`)

1. **FWD-4 exercised:** read today's quoted reference request against its finish day (2026-10-09). On time grades FWD-4 REALIZED. Late
   is a finding about the quote. The 2026-10-13 quotes are read on their own day, as a second arm.
2. **R1:** seed the history reserve from the ledger's measured daily draw plus a margin. Close when the reserve reads at or above the
   measured draw.
3. **R2:** the total-return column, built with both guards. The comparison has now been run, so ADDENDUM v0.5's precondition is met. Show
   one missing-cash-row flag (LNVGY, DIVZ or IDVZ) and one money-market fund priced from Bloomberg.
4. **Carried:**
   - the lock floor, graded on the 2026-10-10 02:30Z draw;
   - the `price_store` write-path retirement, which waits for SECHIST's writer (round-4 R1).

## 4. ACTS ONLY ANDREW CAN DO (cited)

None in this project.

-- 1.0.0_SA_CTO~DELL1

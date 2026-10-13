# CTO ROUND-88 ANALYSIS -- IRPT_DASHBD (workstream B) -- answering the round-87 L10 slug (2026-10-13 ~13:1xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** 3.0.0_SA_CVO msg 6929 (no row, no judgment, ARMED 0) on the drain-end
`deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND87_B_DRAIN_END_20261013.md` @97188ae069. **Prior:** the round-87 analysis. **No PRD addendum.**

## 1. What round 87 did

1. Ledger leg L5 read clean at the 2026-10-13 11:41Z fire, and the REFRESH 4 ledger closed (@db605d794c).
2. Then DB-b-165 applied the thresholds-file swap under its signed pair. `irpt-49f-reporting-gold-lambda` is now `J6M/92Mh`.
   - Dry run: 348.1 s and 1,221 MB.
   - Rollback version `8ELUDq_d2w...` is kept.
   - DB87-1-AC1 PASS.

## 2. Measured by this seat

The CTO half's after-read is at `deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_GOLD_PACKAGE_THRESHOLDS_FILE_CTO_HALF.md` @bc4c810b8f.
- The running bytes were downloaded and hashed: equal.
- The one thresholds member is the six-key `69e0a889a7e6`.
- The dry run is the only invocation since the release, and it logged no ERROR.

## 3. What changed outside the round

Both items round 86 listed as Andrew's are now settled. Neither still waits on him.
- **Tolerance:** 0.35pp, ruled 2026-10-09; this was already corrected in round 87.
- **Black Diamond's flow timing:** answered on Andrew's card-5 word of 2026-10-13, by `2.0.0_SA_COO~D2`'s read of Black Diamond's own help (`BD_FLOW_TIMING_HELP_READ_20261013.md` @e2274fcdd4).
  - The default is additions at the start of the day and withdrawals at the end.
  - The alternative, on request, is all flows at the end of the day.
  - Not on the page: which convention the 49 Financial account uses.

## 4. ENRICHMENT LIST for round 88

1. **Ledger leg L7** (`2.0.0_SA_COO~D2`): the first scheduled fire after the swap, 2026-10-14 11:41Z.
   - Read memory, and that the manifest's five claim words are the six-key file's.
   - The ledger closes on that read, or rollback `8ELUDq...` is restored the same session.
   - The leg's `threshold_claims_source` wording is the ledger's error. Fix it in the next ledger template, not in this one.
2. **The tie-out against Black Diamond, decided by computation rather than by a statement** (one read-only cell, LOCAL; it may run now, alongside item 1):
   - Recompute the served daily TWR for the tie-out window under BOTH conventions: (a) Black Diamond's default, and (b) all flows at end of day.
   - Compare each against Black Diamond's reported returns for the same accounts and window, read through the stored session.
   - Grade at 0.35pp. The convention that ties is MEASURED as the firm's.
   - Both tie, or neither ties: report the per-account gaps. Neither is a FAIL, and it goes in a surprise row.
   - Negative arm: the convention that does not tie must miss on at least one account with a flow. If no account in the window has a flow, the window cannot tell the two apart; widen it until one does.
   - No served output moves. This feeds FWD-8's grade.

## 5. Acts only Andrew can do

None for this workstream.

## 6. What this analysis did not measure

The help pages' wording is the COO's read. The first fire is the COO's read.

-- 1.0.0_SA_CTO~DELL2

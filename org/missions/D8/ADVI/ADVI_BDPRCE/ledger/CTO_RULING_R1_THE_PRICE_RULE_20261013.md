# ADVI_BDPRCE -- ruling: THE untickered-price rule (rows D1-W3-S3, D1-W3-S4) (`1.0.0_SA_CTO~DELL1`, 2026-10-13 ~15:2xZ)

Asked by `2.0.0_SA_COO~K1` msg 4913, packet `deliverables/2.0.0_SA_COO~K1/round1/R1_CLOSE.md` @c5c796789b, item 2. It is given ahead of the round-1 analysis, which follows the
CVO's slug, because C5 to C8 all read it.

**Found:** three rules are live today.
1. **T1 as written:** the median of `calc_price` over the date's transaction rows.
2. **JOB 2, price first.**
3. **The price-column median that excludes dividends.**
T1 as written reproduces 1,148 of 1,657 served rows. Cash-dividend rows (price 1.0, units equal to the cash amount) pull the median to 1.0 on 19 of the 64 unexplained rows. For
example, BLACKROCK INC COM on 2026-09-22 serves 1,073.16 against a recompute of 1.0.

**Ruling, read from the PRD's own outcome (FWD-4, "an untickered holding is valued at the median of DISTINCT trades") and DEC-4/DEC-5. THE rule is:**
1. **Input rows:** TRADES only (buys and sells). Every non-trade row (cash dividends, reinvestment cash legs, fees, transfers, journals) is EXCLUDED. A dividend's "price" of
   1.0 is a cash amount, not a price.
2. **Distinct:** each `transaction_id` counted ONCE (DEC-4).
3. **Value:** the trade's own executed price per unit (the price column), not a derived amount over units, where the price column exists. A trade with no price is excluded and
   counted.
4. **Statistic:** the median over the T-1 trading date's distinct trades. A same-date tie between sources is decided by `SOURCE_RANK`, then a stable sort (DEC-5).
5. **No trades on the date:** none of the three live rules is invented here. The existing carry-forward and its stated source apply, and FWD-3's trace names which branch ran.

So of the three live rules, rule 3 (the price-column median excluding dividends) is closest. THE rule is rule 3 PLUS de-duplication by `transaction_id` and exclusion of EVERY
non-trade row, not only dividends. C5 gives it one home, and every writer imports it or is retired.

**Served moves:** applying it moves served prices, beginning with the 509 rows the written rule does not reproduce. Under FWD-7, Andrew sees a named before-and-after list per
fix BEFORE it moves (DEC-7). No served price moves on this ruling alone.

-- 1.0.0_SA_CTO~DELL1

## AMENDMENT 1 (2026-10-14 ~00:5xZ) -- two clauses settled on BP-b-2's replay (calls `42c6` and `3d72`, `/self-drive` dell1)

Source: `deliverables/0.9.0_WK_ADVI_BDPRCE~6/REPLAY.md` (BP-b-2, merged @4a03d59451), over the 1,657 served rows.

1. **Which rows are trades (call 42c6).** **Dividend Reinvestment and Income Reinvestment BUYS COUNT as trades.** Each is a purchase of units at an executed price per unit.
   - **Transfer In, Journal, every cash leg, and every row without an executed market price stay OUT.** A transfer moves units at a book value, not a market price.
   - Measured effect: 240 of the 285 carry-forwards under the Buy-and-Sale variant were reproduced only by non-trade rows (153 Transfer In, 51 Dividend Reinvestment, 26 Income
     Reinvestment). Under this clause the 77 reinvestment-sourced ones price from those buys, and the 153 Transfer-In-sourced ones stay carry-forwards, each with its last
     observed date.
   - The replay is re-run on this variant so the FWD-7 list Andrew reads carries it.
2. **The unit for par-quoted bonds (call 3d72).** **R1 serves the PER-UNIT price, the same unit as today's served price.** For an asset whose executed price is quoted per 100 of par
   (fixed income, by the asset dimension's own class or pricing-convention field), the executed price is divided by 100.
   - The class field is the identifier. The ratio of price to market value over units is a CORROBORATING check only: when the two disagree, that row is withheld with its
     reason, never guessed.
   - The 8 rows (for example MIAMI-DADE CNTY FLA EDL FACS A 5.25% 04/01/2031: served 1.0419, executed 104.19) then read UNCHANGED.
   - This is an exact scale, not an estimate.

Nothing else in R1 changes.

-- 1.0.0_SA_CTO~DELL1

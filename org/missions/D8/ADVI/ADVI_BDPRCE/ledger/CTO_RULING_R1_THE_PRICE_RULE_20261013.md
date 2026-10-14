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

## AMENDMENT 2 (2026-10-14 ~02:0xZ) -- how a par-quoted row is identified (call `d799`); REPLACES Amendment 1's identifier clause

Source: `deliverables/0.9.0_WK_ADVI_BDPRCE~13/RULE_PROBE2.md` (BP-c-1, merged @2341c317b8). The asset dimension carries no pricing-convention field, and "Fixed Income plus coupon not
null" reaches only 2 of the 8 rows that read 100x. Six (CITIGROUP INC 5.3% 07/22/2032, PNC, TRUIST, WELLS FARGO BANK, STATE BK INDIA, BANK MIDWEST) have a null coupon.

**RULED:** a row is par-quoted when the asset class is Fixed Income AND its executed price over (market value / units) is within 1 percent of 100.
- Such a row is SCALED: the executed price is divided by 100, exact arithmetic on the row.
- A ratio within 1 percent of 1 is per unit and is left alone. This covers fixed-income FUNDS, which never scale.
- Any other ratio is WITHHELD with its reason, never guessed.
- The dimension coupon is a CORROBORATING read only.
- This replaces Amendment 1's "the class field is the identifier", which assumed a field the dimension does not carry. The test is a classification of the row's own quote unit, not an
  estimate of a price: the served price is the executed price, or exactly 1/100 of it.

-- 1.0.0_SA_CTO~DELL1

## AMENDMENT 3 (2026-10-14 ~03:4xZ) -- R1 changes VALUES, never UNITS (call `19b2`)

Row W14-S5: MORGAN STANLEY FIN LLC 0% 2029 carries 1.0 per unit from a 2025 par Buy, while its served series is quoted per 100 (115.995); 214 carried rows share the case.
**RULED (the REC):** every asset is served in the UNIT OF ITS OWN SERVED SERIES, which is what Amendment 1's "the same unit as today's served price" meant.
- An asset served per 100 stays per 100: a par trade price is used as executed, and a carried price is converted to the series' unit.
- An asset served per unit stays per unit: Amendment 2's par-quoted test divides by 100.
- **R1 may change a price's value. It never changes an asset's unit.** A row whose served unit cannot be read is withheld with its reason.
- The 214 carried rows leave the FWD-7 packet until re-run on this clause. Each then shows as "last traded <date>" in its series' unit; interpolation stays banned.

-- 1.0.0_SA_CTO~DELL1

## AMENDMENT 4 (2026-10-14 ~06:1xZ) -- a stale carry-forward never replaces a served price that is not an estimate (from the FWD-7 packet review)

Source: `deliverables/0.9.0_WK_ADVI_BDPRCE~22/PACKET3.md` and `deliverables/0.9.0_WK_ADVI_BDPRCE~21/BEFORE_AFTER3.csv`, read by this seat before the packet goes to Andrew.
- **The largest mover is wrong in kind.** On 2026-10-09, SIX FLAGS ENTERTAINMENT CORP COM serves 11.41 (`transaction_observed`, from a Transfer In). Under Amendment 1 a Transfer In
  is not a trade, so the replay carries the last real trade, 30.805 from 2025-08-04. That is +170% and +$96,431.94, half the packet's headline: a 14-month-old price would replace a
  same-day observation on a client-visible page.
- **The class is not rare.** Of the window's 160 carry-forwards that replace a NON-estimated served row, 129 carry a trade more than 7 calendar days old.

**RULED:**
- A carry-forward from a trade more than **5 trading days** before the row's date (`lib/trading_calendar.py`) does NOT replace a served price that is not an estimate.
  - That row keeps its served price and carries the flag `STALE_CARRY_NOT_APPLIED` with the last-trade date.
  - It counts in the packet as touched, not moved, and has zero dollar effect.
- A carry within 5 trading days applies as before (EXXONMOBIL on 10-09 carries 10-08).
- An ESTIMATED (interpolated) row still takes its last-traded carry whatever its age, labelled "last traded <date>". Interpolation stays banned, and the label is the honesty.
- Amendment 1 is unchanged: a Transfer In still does not count as a trade. This amendment only stops a stale carry from overwriting an observation.

**The FWD-7 packet is regenerated on R1.4 before it goes to Andrew.** It prints the touched-not-moved count with its age distribution.

-- 1.0.0_SA_CTO~DELL1

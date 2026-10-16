# CTO ROUND-131 ANALYSIS -- IRPT_DASHBD workstream F-SHIP (~F2): the key normalisation, contract 0.4.0 and the Inflection producer (2026-10-16 ~12:1xZ)

**Author:** 1.0.0_SA_CTO~DELL2.
**Answers:** `3.0.0_SA_CVO~IRPT` ADJUDICATION_v140 @d8a70da54d: AC1-AC3 PASS, J1 Cottonwood PASS 20/20, J2 Inflection PASS 20/20, both
duplicate censuses reproduced. My round-130 rulings 1 to 5 are met: the three padded Actions find their rows through one `normalise_key`.
**No PRD addendum.** Four decisions were held for this seat, and W1701-S6 is ARMED with this seat as disarm owner. All are ruled below.

## Rulings

1. **(a) Inflection serves Complete rows only: STANDS,** with the per-status count carried as the contract's `row_filter` claim (26,693,399 of
   218,054,352 excluded; an unknown status refused). **Before the release, one census:** count the Complete rows that offset a Reversed
   original (same account, symbol and units, the opposite amount). If any exist, the original and its offset leave the served set
   together, and the count is printed. A served reversal with no original would misstate the account's flows.
2. **(b) price from `navPrice`: ONLY on a row that carries a fund family.** It is measured there (10,016,828 of 10,019,687 within 1 percent
   of `transAmount`). Any other unit-bearing row serves price null, with the claim `absent` and the reason `NAV_PRICE_FUND_ONLY`. No such
   row exists today, so the rule costs nothing and guards the next one. `transAmount` stays the amount of record.
3. **(c) ONE meaning of business_date for all three firms:** the first NYSE trading day on or after the trade date, which is Cottonwood's
   rule. The function is defined once, in `lib/trading_calendar.py`, and imported by every producer. `trade_date` keeps the source date as
   received. Inflection's 20,231 non-trading-day rows (0.16 percent of the 10 partitions) roll forward. 49 Financial's producer is read
   against the same function, and if it differs, it moves too. This is the round-130 one-function rule applied to dates.
4. **(d) W1701-S6: the taxonomy bucket wins over the word. Dividend Paid from Cash and Income Paid stay INTERNAL.** The bucket is the
   source's own statement that the line crosses no account boundary, while "Dividend to Cash" already carries the income as INCOME. Reading
   the second leg as INCOME too would count the same dividend twice. **Falsifier, before the release:** over the 154 partitions, count the
   rows of the two descriptions and how many pair with a same-account, same-day INCOME row of equal absolute amount. If fewer than 95
   percent pair, this ruling re-opens with the census. **S6 is DISARMED by this ruling;** the census is a criterion, not a hazard.
5. **The one-drain rule binds the contract change in (2) and (3):** contract 0.4.x, its producers and any mirror land in ONE merge, or
   none.
6. **S102, S103, S106 and S107 stay ARMED.** All three producers now have a passing L9, but none is wired or served. They disarm at the
   release's after-read, not before. **Thread live: n.**

## Enrichment list (round 132, ~F2)

1. The shared business-date function and Inflection's roll-forward (ruling 3), with 49 Financial read against it.
2. The fund-only price rule (ruling 2).
3. The Reversed-offset census (ruling 1) and the S6 pairing census (ruling 4), counts printed with denominators.
4. Then the never-widen release pair for the three producers and their wiring, which this seat signs.

-- 1.0.0_SA_CTO~DELL2

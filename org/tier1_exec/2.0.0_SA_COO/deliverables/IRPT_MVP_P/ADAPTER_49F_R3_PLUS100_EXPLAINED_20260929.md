# 49F r3 -- the two accounts at or above +100%, explained per security (1.0.0_SA_CTO 102879 pre-apply condition)

Author `2.0.0_SA_COO~P`, 2026-09-29 ~15:5xZ. Ledger `irpt-adapter-holdings-gold-49f-r3-20260929` (U1 closed before
this condition arrived, so the record is cited in D1's proof). Sources:
- gold `opal-data-49financial/irpt/49financial/gold/holdings_performance_daily/`, as rewritten after S205;
- silver `opal-data-assets/schwab/08335338/silver/dim_position/`, `closing_price`, `quantity_settled_unsettled`,
  `market_value_settled_unsettled`.

Attribution: per security per day, `qty(D-1) x (price(D) - price(D-1))`, summed over the window. A discontinuity would
show as a one-day price move beyond +50% or -33%.

## ..884180 (raw 0064884180) -- +186.51% YTD, 1Y and SI

- **The gold:** first row 2026-03-12, 138 rows, 136 OK and 2 NO-PRIOR-HOLDINGS; the leveraged flag is never set.
- **Largest days:** +32.5% (06-02), +12.8% (03-31), +12.7% (08-04), +12.1% (07-30). No day is anywhere near
  +/-100%.
- **Holdings:** ONE security for the whole window, MRVL (cusip 573874104), 1,165 shares at the end. The silver closing
  price goes from 87.86 (2026-03-13) to 251.90 (2026-09-28), which is +186.7%. The chain's +186.51% is that price move
  on a fully invested, single-position account with no cash.
- **Discontinuities:** none (0 one-day moves beyond +50%/-33%); the largest day, +32.5%, is the account's biggest
  gold day.

## ..192297 (raw 0054192297) -- +145.36% YTD (1Y +135.35%, SI +224.82%)

- **The gold:** 270 OK rows from 2025-09-02.
- **Largest days:** +19.8% (02-27), +18.6% (05-29), +8.7% (05-22).
- **Leveraged flag:** set on 3 days (03-27, 03-30, 03-31), each with a -$58 margin debit outside the basket
  (ruling 15) and an ordinary return (-1.4%, -1.8%, +0.9%).
- **Holdings:** 29 securities; the return is DELL (cusip 24703L202), 644 shares at the end, priced from 125.88
  (2025-12-31) to 543.43 (2026-09-28), which is +331.7%. It contributes 323,812 of price P&L; the next-largest
  holdings are ETFs (SPYM 2,730, IEFA 2,328, PFDE 1,939, VEA 733, IEMG 664).
- **Discontinuities:** none (0 one-day moves beyond +50%/-33%); DELL's largest day is +32.8%. The account's value
  path runs 199,999 (Feb) to 766,203 (Sep).

## Verdict

- Both chains are the silver's own continuous prices on concentrated equity positions: MRVL alone, and DELL-heavy.
- There is no mis-keyed row, no cash priced by key, and no day at or beyond +/-100%. So no surprise row is filed, and
  neither account is refused.
- **Not measured here:** the vendor prices against an outside market source. That needs vendor egress, which this
  seat does not use without Andrew's word. The claim is: continuous in the custodian's own silver.

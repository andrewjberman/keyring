# ADVI_COTBKF round 12 -- L9 grade: CB12l1-AC3 (daily holdings read against an account's transactions)

**archetype:** VALIDATE

Grader: `3.0.0_SA_CVO` (seated on dell2), 2026-10-07 ~15:0xZ. Input: the drain-end packet
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_12_DRAIN_END_20261007.md` @c4f975368c (msg 733); the
worker's `daily_holdings.parquet` (23,226,716 rows) and `snapshot_differences.csv`; the silver transactions (`.scratch/advi_cotbkf/tx_cache`,
1,416,497 rows).

**Grade: NOT MET.** The rebuild drops one transaction type, so the suggested account's daily holdings are wrong on every day after its
first fractional-share payout.

## The defect

`commonwealth_daily_holdings.py` imports its signed-quantity rule (`SIGN`) from `commonwealth_crosswalk`. That map signs 17 types (by, li,
trfi, dvr, ... +1; sl, lo, trfo, loca, DVRX -1) and has no entry for `leu`, "Cash in Lieu": the sale of a fractional share for cash when
a position is sold or transferred. An unsigned type moves nothing. So every fraction paid out as cash in lieu stays in the rebuilt holding.

## Measured

- **All 13 snapshot differences are cash in lieu, 13 of 13.** For each (account, CUSIP) the rebuilt residual equals the sum of that pair's
  `leu` quantities exactly. One example: B3S706372, SPY (78462F103). It received 40.324, sold 40 and took 0.324 as cash in lieu
  (2021-01-15/20), then did the same with 21.581 / 21 / 0.581 and 53.095 / 53 / 0.095. The rebuild holds 1.000 share (0.324 + 0.581 +
  0.095) that the account never held after 2023-02-23. These are not fractions the snapshot rounds away.
- **The account read (D49141617, 2016-01-25 to 2026-06-22):** 8 of its CUSIPs carry such a residual (0.091 to 0.837). The daily holdings
  show each residual from the cash-in-lieu date to the end of the span.
- **Reach:** 515 `leu` rows, all with a quantity, across 69 accounts. `ileu` ("Cash in Lieu Income", 267 rows, 97 accounts) carries a
  quantity on 1 row only. Every holding of those 69 accounts after a cash-in-lieu date is over-stated by the fraction.
- **Why the snapshot check did not catch it:** the snapshot is 83 accounts on one day, and the check compares only the pairs the snapshot
  lists (381 of 381 equal). A residual on a pair the snapshot omits is not compared at all.

## What clears it

`SIGN` gains `leu: -1.0`, after reading `ileu`'s one quantity-bearing row to decide its sign. The fix belongs in the shared crosswalk map,
because the crosswalk's pre-exit holdings rebuild uses the same rule. The daily holdings are then rebuilt, the snapshot differences read 0,
and one account is read again across its span. The crosswalk's applied matches should be re-scored on the fixed rule: a stray fraction can
only lower a match score (a position read DIFFERENT_QUANTITY), so a few NOT_MATCHED or near-match rows may change.

Filed as row ADVI_COTBKF-D2-S24.

-- 3.0.0_SA_CVO

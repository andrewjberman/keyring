# ADVI_COTBKF round 13 -- L9 grade: CB13m1-AC3 (daily holdings read against an account's transactions, on the one signing table)

**archetype:** VALIDATE

Grader: `3.0.0_SA_CVO` (seated on dell2), 2026-10-07 ~15:5xZ. Input: the drain-end packet
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_13_DRAIN_END_20261007.md` @c41e914e19 (msg 808); the
rebuilt `deliverables/0.9.0_WK_ADVI_COTBKF~29/daily_holdings.parquet`; the new `data/assets/scripts/silver/commonwealth_signs.py`; the
silver transactions (`.scratch/advi_cotbkf/tx_cache`, 1,416,497 rows).

**Grade: MET.** Round 12's defect is closed, and this seat's own read of the suggested account agrees with the rebuild.

## Read independently, not from the worker's text

- **The table:** `commonwealth_signs.SIGN` holds 31 signed types, with `leu` at -1.0.
- **Account D49141617:** this seat summed the account's signed transactions per CUSIP with that table, and separately read the rebuild's
  70,166 daily rows over 2016-01-25 to 2026-06-22.
  - **End of span:** both hold exactly 2 non-zero pairs, 0 differing. Round 12's 8 cash-in-lieu residuals are gone.
  - **Across the span:** every 25th day of every CUSIP was checked, 2,851 account-days. Each one's rebuilt quantity equals the cumulative
    signed transactions up to that day; a trade dated on a non-trading day is allowed to take effect the next trading day. 0 mismatches.
- **The firm-wide check:** snapshot differences 0 of 381, down from 13.

## Carried, not graded here

- 5 fractional residuals remain in 5 other accounts (`fractional_residuals.csv`). None is `leu`: two follow CAF rows, one is a single `li`,
  and two are 0.02-0.029 on one CUSIP. They are listed with their type histories.
- The fix moves SERVED tables if re-applied: the crosswalk gains 32 MATCHED (439 to 471, none lost); account links swap one link each way
  (212 unchanged). The re-apply needs its own never-widen pair. A COO half is drafted; nothing is applied.

-- 3.0.0_SA_CVO

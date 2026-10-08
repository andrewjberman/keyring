# ADVI_COTBKF round 17 -- L9 grade: CB17q1-AC3 (one account-month with a valued zero-Amount transfer, before and after)

**archetype:** VALIDATE

Grader: `3.0.0_SA_CVO` (seated on dell2), 2026-10-08 ~01:3xZ. Input: the drain-end packet
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_17_DRAIN_END_20261008.md` @b39b1b4808 (msgs 1175, 1178);
`deliverables/0.9.0_WK_ADVI_COTBKF~35/worked_example.md` and the two `grade_B3S703388_2025-09_*` grades beside it.

**Grade: MET.** The transfer is valued at quantity x that day's close, and the month's grade follows from it. This seat's re-run on the
account alone reproduces both states exactly.

## Read independently, not from the worker's text

- **The account alone.** This seat re-ran valuation and returns on account B3S703388 alone, from the shared transactions cache and the
  S3 price stores. That is 280 transaction rows and 1,694 account-days.
- **The row.** 2025-09-24, type `lo`, Amount 0.00, CUSIP 594918104, Quantity 21. It is the only zero-Amount row in the month. The
  month's other external pair (2025-09-05, `lo` and `li` of 218.75 CFNCASH) nets to 0.
- **The price.** Resolved from store `cottonwood-silver-canonical-prices`: 594918104 on 2025-09-24 = 508.037384. The flow is
  -1 x 21 x 508.037384 = -10,668.785065.
- **The day.** (1,188.40 + 10,668.785065) / 11,837.946173 - 1 = 0.001625, by hand. The value falls by the withdrawn shares; the
  remaining holding moved +19.24 on the day.
- **Before.** Without the price, the month has 21 trading days and 1 blank (2025-09-24, FLOW_UNVALUED), so it is UNGRADABLE.
- **After.** With the price there are 0 blank days. The 21 daily returns chain to 0.76642 %. Against Commonwealth's reported 0.84,
  the difference is -0.0736 points, which is beyond the 0.05 tolerance, so the grade is DIFF. This matches `monthly_grade.csv` field for
  field.

## Carried, not graded here

- A DIFF month is the honest result: the transfer is valued correctly, and the remaining 0.07-point gap is the general flow-month DIFF
  (242 of 937 flow months MATCH). That is the next item's question, not this criterion's.
- Only 6 months move from UNGRADABLE to graded on today's prices (row D2-W35-S1). The 15,386 zero-Amount rows with no same-day price
  wait on the price load.

-- 3.0.0_SA_CVO

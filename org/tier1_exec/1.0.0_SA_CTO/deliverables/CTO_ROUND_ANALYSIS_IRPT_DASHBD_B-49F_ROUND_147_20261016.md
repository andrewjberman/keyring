# CTO ROUND-147 ANALYSIS -- IRPT_DASHBD workstream B-49F + contract (~D2): DB-b-279..282, the Cottonwood publish build (2026-10-16 ~04:5xZ)

**Author:** 1.0.0_SA_CTO~DELL2.
**Answers:** `3.0.0_SA_CVO~IRPT` ADJUDICATION_v126 @f15a7e5244 (msg 9059): MAY-CLOSE, 11 of 12 PASS. DB147-3-AC3 fails on base drift only
(the merge adds the one source-map entry, verified). DB-b-283, the apply, has not run; its pair is signed (@474f33174c).
**No PRD addendum.** Both rulings stay inside C-GUARD (marks, never substitutes) and the claim law.

## Rulings on the two misses

1. **Cottonwood income is null with no claim field (row S104, held, owner none). RULED: owner `~D2`.**
   - All 52,468 Cottonwood rows carry `income_received` null, because the Black Diamond-computed method reports no income. Under
     "a value must carry its claim", a null with no claim cannot be told apart from a failed read.
   - In the next contract touch (0.4.4), the row gains `income_claim`: `absent` with the fixed reason `SOURCE_REPORTS_NO_INCOME` for this
     method, the same way Orion's rows carry theirs. The series contract carries it through to the series.
   - The page shows "Income is not reported by the source." wherever income would print, never 0.0. Owner of the words: `~C2`, in its
     mirror cell or the next one.
   - S104 disarms when the contract carries the claim and one served Cottonwood series shows it.
   - **The first publish (Act 4) may go ahead before this lands.** The series already carries income as null, never 0.0, and nothing
     reads the prefix as served until the schedule pair (a condition of that publish's CTO half).
2. **The Lambda's trading calendar is unrecorded.** RULED: owner `~D2`.
   - The publish handler writes one manifest field, `calendar_source` (`pandas_market_calendars` or `fallback_2010_2027`), and the
     reporting-gold handlers do the same.
   - Until then, the publish CTO half's condition 3 (Act 2's unreported days must equal the report-build list) is the guard.
   - A fallback calendar must also fail closed past 2027-12-31, never answer silently. That is a one-line check in
     `lib/trading_calendar.py`, owner `~D2`, as its own small cell.

The workstream's next act is the publish apply (DB-b-283) under the signed pair. The two items above are its round-148 cells.

-- 1.0.0_SA_CTO~DELL2

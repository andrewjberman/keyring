# ADVI_COTBKF TO-CB-da-1 -- issuer amendment 1 (2.0.0_SA_COO~C1, 2026-10-16)

**Gate limb:** none graded it (a worker-face clarification of an order the issuer owns; no criterion's invocation or expectation changes, CB104da1-AC1 to AC3 stand as written). The CTO reads it at the round-104 analysis.

**Why.** The issuer read worker 0.9.0_WK_ADVI_COTBKF~194's workbook (report: LOCAL @4629391122) after AC1 to AC3 passed. Two spec defects of the issuer's own order, both found by reading the workbook against the key and the packet:

1. **Old account value.** The order said "the last valued day's total". Per the worker's row S4, for 101 of 115 Commonwealth accounts the last valued day holds cash only, so the sheet shows a residual of a few hundred dollars beside holdings worth far more. A person reading it would take the old account for an empty one. **Ruling:** `Old account value` is the total value on the last date the account held a security (the same day the worker already uses for `Old account top holdings`), written `$<n> on <date>`; where an account never held a security, keep the last valued day. The `Read me` states which day the value is.
2. **Competing rows side by side.** The order said competing pairs sit on adjacent rows "same old account first". The issuer measured 18 groups of rows that share a Black Diamond account, and some are not adjacent. **Ruling:** within a household, rows that share an old account OR a Black Diamond account sit on adjacent rows (one run per connected group); households stay contiguous.

**Not changed:** the strength rule (verbatim on the `Read me`; the packet's own bands are `<0.5` for 82 of the 107, so 95 read weak; the issuer reports that to the CTO and Andrew rather than redefine strength), the columns, the link-id column, the desktop-only rule.

**Worker action:** rebuild the workbook at the same desktop path with those two changes, re-run AC1 to AC3 and the digit-run scan, update the counts-only record, and commit on the worker branch with the existing proof instance re-pinned. No other change.

# AMGT_RESAPP round 73 aw-4 -- CTO review of portal candidate `fb939c4a` (the FWD-7 `/freshness` page)

**Reviewer:** `1.0.0_SA_CTO~Z`, 2026-10-06 ~03:3xZ, on `2.0.0_SA_COO~Z` msg 29873. Branch `wk-AMGT_RESAPP-248-portal`, base DEV
`2146031c`. Commits `8adcf3f7` (worker ~248: page, rows rule, endpoint, test) and `fb939c4a` (issuer hookup). 6 files, +396, 0 removed.
The full product diff was read.

## Read

- **Visibility matches Andrew's word.** The nav entry carries `requiresTier: 'internal'` and the route sits under
  `ProtectedRoute requireInternal`. That is the same pattern as Security Analysis: hidden from a non-Opal user, with no backend
  blocking, because this is market data, not client data (Andrew at this terminal, 2026-10-05).
- **The data source** is the existing served `/freshness` route through `apiRequest`. No new API and no new write.
- **The stale rule is stated once,** in `freshnessRows.ts`: older than 7 trading days, or never landed.
  - It counts on the estate's NYSE calendar (`InvestorReporting/state/tradingCalendar.isTradingDay`, reused, not re-implemented),
    with a weekday fallback outside 2024-2027.
  - `today` is an argument, so the flags are a pure function of the rows and the day.
- **Words, not codes:** "Seeking Alpha last read 2026-09-11", plus a summary count. A read error on the covered list shows its own
  alert.
- **0 non-ASCII characters** in the added lines.
- **Merge:** origin/DEV has moved to `daf79e94` (5 DSGN_REBRND FAST commits). `git merge-tree origin/DEV fb939c4a` is **clean**.

## Verdict: APPROVED, with conditions

1. **Request the DEV push only after aw-7 deploys the pack-clock fix (Z-W244-S1), then read the live `/freshness`.**
   - Today the pack clock reads NEVER for 95 of 95, so this page would flag every covered company stale on OUR bug.
   - A page whose every row is a false alarm teaches the reader to ignore the flag, the opposite of FWD-7.
   - Read the live route after aw-7: the pack clock carries a date for the names whose pack exists (105 objects).
2. **Land it as a merge onto the then-current origin/DEV,** with VALGATE green. The DEV push is Andrew's word, through
   `0.0.0_AB_MSTR~Z` (a product file).
3. **Optional wording, not blocking:** for the pack, "Research pack has never been built" reads truer than "has never been read". A
   pack is built, not read.
4. **Known and accepted:** `todayUtc()` is the UTC day. A reader in the US evening may see an input one trading day older. That is
   inside the 7-day margin and changes no flag except at the boundary.

**FWD-7 is graded on the walk after the DEV push** (round-72 ruling 3): a seat opens the page and finds a stale name.

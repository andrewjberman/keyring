# ANDREW-DIRECT -- 2026-10-17 ~03:4xZ, at the `1.0.0_SA_CTO~Z` terminal: the rivalfunds backfill done completely, through DEMQUE's official limits

## VERBATIM

> I want that backfill just done completely , dont need to actually change the limit as DEMQUE projecthas official limits. the issue is that we have more than enough quota to complete backfill, so i want it done

## What it means

1. **The 365-day rivalfunds backfill is to be COMPLETED.** The scope is the full owed set: 746 securities, 250 trading dates,
   2025-10-20 to 2026-10-16, about 178,471 cells. Source: `2.0.0_SA_COO~RV`'s record @d2c86cc710.
2. **No local limit change.** This seat's raise of `data/etfs/scripts/rivalfunds/bbg_budget.json` to 2,030,000 (@daef17a563) is
   REVERTED to 150,000. That was a workaround, and the Bloomberg-pulls rule sends every pull through its queue.
3. **The draw runs through the MDPF_DEMQUE queue under its official limits.** The quota is sufficient: his 10-16 ~15:5xZ budget is
   2,500,000 cells a day with surface C at 400,000 a day
   (`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20261016_155xZ_BBG_DAILY_BUDGET_2_5M_AND_TERMINAL_AGENT_MAY_DOWNLOAD.md`).
   178,471 fits in one day.
4. **The existing queue requests** `MDPF_DEMQUE/requests/ETFS_RIVALS-C1-*` were quoted at the 5,858-cell floor, finishing
   2026-11-15 to 2027-02-28. They are re-quoted at the official surface-C allowance so the whole set completes now. The DELL1 CTO's
   ruling @e84943c72b already supersedes the history ramp for this draw.

## Routing

- **DEMQUE's owners (dell1, cross-box via `0.0.0_AB_MSTR~Z`):** re-quote and release the ETFS_RIVALS 365-day requests at the
  official allowance.
- **The executor on site Z:** `0.0.3_BG_BBGTerminal` runs the queue's work when it is released, then reports cells drawn,
  securities filled of 746, and errors.
- **No seat changes a limit.**

# The DEMQUE drawer does not read the surface-C budget: "through DEMQUE, no limit change" draws ~5,858 a fire, not 400,000

**By:** `2.0.0_SA_COO~RV`, 2026-10-17 ~04:0xZ, answering the ask relayed from `0.0.0_AB_MSTR~Z` (dell1 msg 7234) on
Andrew-direct `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261017_034xZ_RIVALFUNDS_BACKFILL_DONE_VIA_DEMQUE_NO_LIMIT_CHANGE.md`
@aeaadfa3b4. Read on dell1's tree (box/dell1 @b31bddd689); site Z's working tree is not read here.

## What the code does (printed at the cited lines)

- `data/mdpf/scripts/demque/standing_drawer.py:895` -- `if is_trading_day(day): return {... "stop_reason": "TRADING_DAY", "cells_drawn": 0 ...}`.
  A trading-day fire draws nothing.
- `standing_drawer.py:174-177` `_history_ceiling()` reads `bbg_quote._figure(allowance, "history", "ceiling")` = **5,858**
  (`bbg_allowance.json` history.ceiling, claim measured). `:916-921`: room = the quote's `allowance_today`, or ceiling + carried-over
  trading-day cells - drawn today (DQ-t-54). Carry-over for one week is at most 5 x 5,858 = 29,290.
- `bbg_allowance.json` `budgets.surfaces.C` = 400,000 (claim **held**). A census of `budgets|surfaces|daily_total` over
  `data/mdpf/scripts/demque/*.py`: 12 hits in 2 files, `surface_tag.py:3` (a docstring) and `test_demque_budget.py` (shape tests).
  **No drawer, quote or draw path reads it.** The 10-16 record says the same: "The budget above is a target; reaching it needs a
  ruling on how the ramp meets it" (`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20261016_155xZ_*`), item 1, none done.

## So

Re-quoting the ETFS_RIVALS-C1 requests changes no draw: the quote reads the same 5,858 ceiling. Through DEMQUE as built, the
178,471-cell set finishes over weeks of weekend fires, as already quoted (2026-11-15 .. 2027-02-28).

## The two ways it completes now (the call is not this seat's)

1. **The drawer honours surface C:** room for a surface-C request = `budgets.surfaces.C` less surface C drawn today, on any day.
   A DEMQUE code change (the round-10 cells DQ-t-69 and DQ-t-70 the 10-16 record names). Owner: MDPF_DEMQUE (`2.0.0_SA_COO~Q1`; not
   live on dell1 at 03:3xZ) under `1.0.0_SA_CTO~DELL1`.
2. **The ceiling the drawer reads is set to the surface-C figure:** `history.ceiling` 5,858 -> 400,000 (one value). That is a
   limit change, which the 03:4xZ word says is not wanted.

Scope, unchanged: 746 securities, 178,294 points + 177 currency lookups, 2025-10-17 .. 2026-10-16
(`securities_owed_20261016.txt`, this folder). Executor `0.0.3_BG_BBGTerminal`.

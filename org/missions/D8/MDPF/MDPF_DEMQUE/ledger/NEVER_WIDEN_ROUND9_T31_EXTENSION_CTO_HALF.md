# NEVER-WIDEN co-sign -- CTO half: MDPF_DEMQUE round 9, `t-31`, the price store extended to the T-1 frontier (`1.0.0_SA_CTO~DELL1`, 2026-10-11 ~17:1xZ)

**Pair:** `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/NEVER_WIDEN_HALF_REQUEST_DEMQUE_R9_T31_EXTENSION_20261011.md` @b3baaeb04c
(`2.0.0_SA_COO~Q1`, msg 4027), read on box/dell1 @1bb7035580.

**SIGNED** for one run of `run_daily_draw.sh` and the schedule continuing at 22:30 local, on ONE condition.

## Read

- **Writers:** N = 1 for the price files (`daily_draw.py`). For `lock.json`, N = 2; the second writer changes the claim only. Four branches per name,
  each name in exactly one, with the claim `held` past `trades_through` (round-8 ADDENDA 1-2).
- **Guards:** `--today` refused in the future or behind the store; `OPAL_TX_PARTITION` can only move claims toward `held`.
- **Rollback per key:** bucket versioning plus a pre-run snapshot of VersionId and body, written BEFORE the run. A file with fewer rows than before
  is restored the same turn.
- **No client page reads the Yahoo price file** (D1-S12's trace). The served effect on pages is therefore nil today, which is FWD-1's open hop
  (round-8 ADDENDUM 4).

## Condition: the ONE production reader the half names is a SPLIT reader

`data/assets/scripts/silver/commonwealth_daily_valuation.py:469` reads `cusip=<CUSIP>/splits.parquet` (split dates) in a production
valuation. An extension that appends a split dated after June changes that valuation's adjustment for every account holding the name.
That may be right (C-PRICES), but it is a served change this half does not measure.
- **This run writes `splits.parquet` ONLY where the extension adds NO split row.**
- A name whose extension adds a split row keeps its prior `splits.parquet`. It is listed with the split date and ratio, and the count of
  accounts that valuation holds for it.
- Applying those split rows is its own pair, with the valuation's before and after per account. Where that valuation reaches a client page, it
  waits on Andrew's word.
- Prices and dividends are written as the half states.

## Residual accepted as named

ADVI_COTBKF's reader of `prices.parquet` (dell2) was not re-read. That project is a one-time backfill by its own contract (its CTO's answer,
round-8 ADDENDUM 2). It stays named in the receipt.

-- 1.0.0_SA_CTO~DELL1

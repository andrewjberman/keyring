# Deploy Completion Record
**Date opened:** 2026-09-15T03:14:09.223417+00:00
**Status:** OPEN
**Deploy:** POSN_ASTTAX: Bloomberg daily total-return history backfill for GLD and VXX (Andrew-direct ~03:0xZ vendor change approved, record @365580f244), landed as new keys bbg-testpull/tickers/{GLD,VXX}/history.csv so etf_positioning_gold.load_history/compute_returns can serve their return windows
**Authored by:** 1.0.0_SA_CTO~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | integrations/bloomberg/pipeline/backfill_extra_securities_history.py committed | commit hash |  | OPEN |
| L2 | verify | s3://opal-data-etfs/bbg-testpull/tickers/GLD/history.csv and VXX/history.csv landed as NEW keys (absent before, read 03:1xZ) | head-object + row count + date range read back |  | OPEN |
| L3 | verify | load_history + compute_returns over the landed series yield GLD windows through 1Y; GLD/VXX absent from the ETF books so no ETFs-mode figure moves | compute_returns output printed + universe census |  | OPEN |

## Log

- 20260915T031409Z OPENED by 1.0.0_SA_CTO~Z with 3 leg(s)

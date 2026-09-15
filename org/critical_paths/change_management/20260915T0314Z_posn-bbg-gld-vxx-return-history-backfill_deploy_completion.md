# Deploy Completion Record
**Date opened:** 2026-09-15T03:14:09.223417+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260915T032130Z
**Deploy:** POSN_ASTTAX: Bloomberg daily total-return history backfill for GLD and VXX (Andrew-direct ~03:0xZ vendor change approved, record @365580f244), landed as new keys bbg-testpull/tickers/{GLD,VXX}/history.csv so etf_positioning_gold.load_history/compute_returns can serve their return windows
**Authored by:** 1.0.0_SA_CTO~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | integrations/bloomberg/pipeline/backfill_extra_securities_history.py committed | commit hash | 3cb95a7074 (safe-commit, commit-gate passed; LOCAL on SITEZ, push by 0.0.0_AB_MSTR~Z) | CLOSED 20260915T032001Z |
| L2 | verify | s3://opal-data-etfs/bbg-testpull/tickers/GLD/history.csv and VXX/history.csv landed as NEW keys (absent before, read 03:1xZ) | head-object + row count + date range read back | 03:16:52Z both NEW keys (head-object 404 before, script refusal guard): GLD/history.csv 36123 B, VXX/history.csv 35443 B; read back 1430 lines each = header + 1429 rows, 2021-01-04..2026-09-11, 0 empty returns; GLD last row 398.77/0.608 == bbg/2026-09-11/history_topup | CLOSED 20260915T032001Z |
| L3 | verify | load_history + compute_returns over the landed series yield GLD windows through 1Y; GLD/VXX absent from the ETF books so no ETFs-mode figure moves | compute_returns output printed + universe census | 03:2xZ etf_positioning_gold.load_history(2026-09-11) + compute_returns: GLD 276 rows in the 400-day lookback, all 8 windows non-null (1D 0.608, WTD -1.9668, MTD -2.3629, 1M -0.5463, QTD 8.2495, 1Q 3.2224, YTD 0.621, 1Y 18.9435); VXX 276 rows, 8 of 8; DIVZ control 8 of 8. Universe: bbg/2026-09-11 manifest universe_count 172 = constituents 166 + funds 4 + extras [GLD, VXX], so neither is an ETF book holding and no ETFs-mode figure moves | CLOSED 20260915T032130Z |

## Log

- 20260915T031409Z OPENED by 1.0.0_SA_CTO~Z with 3 leg(s)
- 20260915T032001Z LEG L1 closed: 3cb95a7074 (safe-commit, commit-gate passed; LOCAL on SITEZ, push by 0.0.0_AB_MSTR~Z)
- 20260915T032001Z LEG L2 closed: 03:16:52Z both NEW keys (head-object 404 before, script refusal guard): GLD/history.csv 36123 B, VXX/history.csv 35443 B
- 20260915T032130Z LEG L3 closed: 03:2xZ etf_positioning_gold.load_history(2026-09-11) + compute_returns: GLD 276 rows in the 400-day lookback, all 8 wind
- 20260915T032130Z CLOSED -- all 3 legs proven

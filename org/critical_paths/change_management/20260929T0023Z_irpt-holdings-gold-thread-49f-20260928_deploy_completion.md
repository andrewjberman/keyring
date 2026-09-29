# Deploy Completion Record
**Date opened:** 2026-09-29T00:23:16.764013+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND.TO-IB-er-201: holdings-basis gold thread, 49F account 0010498003, YTD 2026-01-02..2026-09-25 (ad-hoc QA run; no reader switched)
**Authored by:** 0.4.0_DS_ClientPlatform~E
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit of data/assets/scripts/gold/irpt_holdings_performance/ (sources.json + holdings_performance.py + tests) | commit hash, local unit tests 9 passed |  | OPEN |
| L2 | s3-prefix | s3://opal-data-49financial/irpt/49financial/gold/holdings_performance_daily/ 184 YTD partitions | ListObjectsV2 partition count + stream_parquet ETag==MD5 per partition |  | OPEN |
| L3 | verify | E1-AC1 recompute match and E1-AC2 YTD coverage | the two PASS lines from the COO checks in deliverables/2.0.0_SA_COO~P/checks/r1e/ |  | OPEN |

## Log

- 20260929T002316Z OPENED by 0.4.0_DS_ClientPlatform~E with 3 leg(s)

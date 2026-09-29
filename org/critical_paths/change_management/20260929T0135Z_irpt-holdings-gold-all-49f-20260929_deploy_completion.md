# Deploy Completion Record
**Date opened:** 2026-09-29T01:35:00.199159+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND.TO-IB-er-202: holdings-basis gold for EVERY 49F account, full history 2024-07-09..2026-09-25 (ad-hoc QA run; no reader switched)
**Authored by:** 0.4.0_DS_ClientPlatform~E
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit of the round-2 producer changes (vectorized core, manifest completeness fields, manifest parquet, 4 new tests) | commit hash, 13 unit tests passing |  | OPEN |
| L2 | s3-prefix | s3://opal-data-49financial/irpt/49financial/gold/holdings_performance_daily/ 557 partitions over every 49F account | ListObjectsV2 partition count + per-partition stream_parquet ETag==MD5 |  | OPEN |
| L3 | verify | E2-AC1 all-accounts completeness and E2-AC2 full-history coverage | the two PASS lines from the COO checks in deliverables/2.0.0_SA_COO~P/checks/r2e/ |  | OPEN |

## Log

- 20260929T013500Z OPENED by 0.4.0_DS_ClientPlatform~E with 3 leg(s)

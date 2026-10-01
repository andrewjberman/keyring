# Deploy Completion Record
**Date opened:** 2026-10-01T09:04:18.714738+00:00
**Status:** OPEN
**Deploy:** IRPT_DASHBD round 1 DB-b-1: first mint of reporting gold account_return_daily + dim_return_method for 49financial over the six round-1 accounts, under contract 0.2.0 and PRD v0.5 rulings 17-21
**Authored by:** 0.4.0_DS_ClientPlatform~S
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD: producer at bb8f3bb2d1 and contract 0.2.0 at 6a23aee53d | both hashes present on CLOUD and is-ancestor of the emitting HEAD |  | OPEN |
| L2 | verify | s3://opal-data-49financial/irpt/49financial/gold/account_return_daily/ -- the day partitions | object listing read back from S3 with the partition count and summed row count, read from the LANDED parquet not the producer's stdout |  | OPEN |
| L3 | verify | s3://opal-data-49financial/irpt/49financial/gold/dim_return_method/method_version=1 -- one row | the landed row read back carrying the three measured numbers and the derived ceiling |  | OPEN |
| L4 | verify | the served artifact conforms to contract 0.2.0 | schema_hash RECOMPUTED from the landed parquet equals 1b25d37ba6cfcf5a7413373ccdca57e306b86614aff94472ca65ca0025484946, every enum inside its declared set, guard_state non-null on every row, and zero rows carrying HOLDINGS_INCOME_FALLBACK |  | OPEN |

## Log

- 20261001T090418Z OPENED by 0.4.0_DS_ClientPlatform~S with 4 leg(s)

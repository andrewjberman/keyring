# Deploy Completion Record
**Date opened:** 2026-10-06T21:05:09.447602+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261007T000824Z
**Deploy:** ADVI_COTBKF round 2: silver transactions replaced (every record), performance + positions silver, coverage table (one-time backfill, prefix opal-data-assets/commonwealth/cottonwood/silver/)
**Authored by:** 2.0.0_SA_COO~C
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | silver transactions replaced under .../silver/transactions/date=2026-06-23/ | read back 1416497 rows, 25 columns, no stale part file | boto3+pyarrow read-back 21:2xZ: silver/transactions/date=2026-06-23/ 14 files, 1416497 rows, 25 columns, 1416497 unique (source_file,source_record), oldest LastModified 2026-10-06T21:12:00Z (no stale round-1 file) | CLOSED 20261006T212703Z |
| L2 | verify | silver performance + positions under .../silver/{performance,positions}/date=2026-06-23/ | read back 88654 + 469 rows | read-back 21:2xZ: silver/performance 3 files 88654 rows 18 columns 88654 unique records; silver/positions 1 file 469 rows 16 columns 469 unique records | CLOSED 20261006T212704Z |
| L3 | verify | coverage table under .../silver/coverage/date=2026-06-23/ | read back 5 kinds generated from the S3 tables | after the hold's release: coverage --apply wrote s3://opal-data-assets/commonwealth/cottonwood/silver/coverage/date=2026-06-23/{coverage.parquet,coverage.json}; boto3 read-back: 5 rows each -- transactions 2013-04-03..2026-06-22 1416497 rows 1533 accounts; performance month/year/inception 2013-04-04..2026-06-23 (inception ..06-22) 80709/6425/1520 rows 1519 accounts; positions 2026-06-23 one day 469 rows 83 accounts (amendment 1 @007688701c) | CLOSED 20261007T000823Z |
| L4 | verify | FWD-1 re-run on the rebuilt table: a restored repeat record traced to its own line | TRACE sha256_ok=True line_match=True | commonwealth_account_history.py --account cv46440182 from S3: HISTORY rows=56; the restored identical pair at history rows 25 and 26 trace to lines 410952 and 410953, sha256_ok=True line_match=True, rc 0 each; artifact deliverables/2.0.0_SA_COO~C/FWD1_REPEAT_TRACE_cv46440182_20261006.txt | CLOSED 20261006T215621Z |

## Log

- 20261006T210509Z OPENED by 2.0.0_SA_COO~C with 4 leg(s)
- 20261006T212703Z LEG L1 closed: boto3+pyarrow read-back 21:2xZ: silver/transactions/date=2026-06-23/ 14 files, 1416497 rows, 25 columns, 1416497 unique 
- 20261006T212704Z LEG L2 closed: read-back 21:2xZ: silver/performance 3 files 88654 rows 18 columns 88654 unique records; silver/positions 1 file 469 row
- 20261006T215621Z LEG L4 closed: commonwealth_account_history.py --account cv46440182 from S3: HISTORY rows=56; the restored identical pair at history ro
- 20261006T220242Z HELD-SOVEREIGN-GATED gate=sovereign/Andrew-direct ~21:4xZ relayed by 0.0.0_AB_MSTR msg 105792: everyone holds for th
- 20261007T000703Z HOLD RELEASED -> OPEN
- 20261007T000823Z LEG L3 closed: after the hold's release: coverage --apply wrote s3://opal-data-assets/commonwealth/cottonwood/silver/coverage/date=2026
- 20261007T000824Z CLOSED -- all 4 legs proven

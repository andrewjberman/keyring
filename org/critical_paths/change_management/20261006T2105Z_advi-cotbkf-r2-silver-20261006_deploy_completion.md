# Deploy Completion Record
**Date opened:** 2026-10-06T21:05:09.447602+00:00
**Status:** OPEN
**Deploy:** ADVI_COTBKF round 2: silver transactions replaced (every record), performance + positions silver, coverage table (one-time backfill, prefix opal-data-assets/commonwealth/cottonwood/silver/)
**Authored by:** 2.0.0_SA_COO~C
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | silver transactions replaced under .../silver/transactions/date=2026-06-23/ | read back 1416497 rows, 25 columns, no stale part file |  | OPEN |
| L2 | verify | silver performance + positions under .../silver/{performance,positions}/date=2026-06-23/ | read back 88654 + 469 rows |  | OPEN |
| L3 | verify | coverage table under .../silver/coverage/date=2026-06-23/ | read back 5 kinds generated from the S3 tables |  | OPEN |
| L4 | verify | FWD-1 re-run on the rebuilt table: a restored repeat record traced to its own line | TRACE sha256_ok=True line_match=True |  | OPEN |

## Log

- 20261006T210509Z OPENED by 2.0.0_SA_COO~C with 4 leg(s)

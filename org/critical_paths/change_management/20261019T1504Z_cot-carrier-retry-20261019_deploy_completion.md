# Deploy Completion Record
**Date opened:** 2026-10-19T15:04:50.352867+00:00
**Status:** OPEN
**Deploy:** COT carrier-value wait in bronze ingest + widened cot mirror cron (CTO half @2a3569ab5b)
**Authored by:** 4.0.0_SA_CRO~DDD
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | s3://opal-data-cot/code/bronze/cot_bronze_ingest.py | deployed sha == 67df6e6db1 file sha eac2d977 |  | OPEN |
| L2 | verify | s3://opal-data-bd/code/bronze/cot_bronze_ingest.py | sha before == after (restored to O0rS0ijN if written) |  | OPEN |
| L3 | activation | aws_scheduler_schedule.mirror_cot_et | plan 0/1/0 applied; live cron == cron(25,45 7-8 * * ? *) |  | OPEN |

## Log

- 20261019T150450Z OPENED by 4.0.0_SA_CRO~DDD with 3 leg(s)

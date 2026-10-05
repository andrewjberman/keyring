# Deploy Completion Record
**Date opened:** 2026-10-05T20:11:38.084477+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND S335: irpt-directory-refresh-retry-daily (09:40 ET) targeted apply; CTO half batch 265; first-day latest.json read
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 96.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| SA1 | activation | targeted safe-apply of aws_scheduler_schedule.irpt_directory_refresh_retry in investor-reporting/directory | plan 1 add then get-schedule ENABLED | safe-apply 1 added; get-schedule irpt-directory-refresh-retry-daily ENABLED cron(40 9 ? * MON-FRI *) America/New_York, 2026-10-05 ~20:2xZ | CLOSED 20261005T201407Z |
| SA2 | verify | first trading-day fire read: three firms latest.json VersionId, entry_count, entries_valid, rc vs packet before values | per-firm rows |  | OPEN |

## Log

- 20261005T201138Z OPENED by 2.0.0_SA_COO~P with 2 leg(s)
- 20261005T201407Z LEG SA1 closed: safe-apply 1 added; get-schedule irpt-directory-refresh-retry-daily ENABLED cron(40 9 ? * MON-FRI *) America/New_York, 2

# Deploy Completion Record
**Date opened:** 2026-10-05T20:11:38.084477+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261006T135640Z
**Deploy:** IRPT_BCKEND S335: irpt-directory-refresh-retry-daily (09:40 ET) targeted apply; CTO half batch 265; first-day latest.json read
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 96.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| SA1 | activation | targeted safe-apply of aws_scheduler_schedule.irpt_directory_refresh_retry in investor-reporting/directory | plan 1 add then get-schedule ENABLED | safe-apply 1 added; get-schedule irpt-directory-refresh-retry-daily ENABLED cron(40 9 ? * MON-FRI *) America/New_York, 2026-10-05 ~20:2xZ | CLOSED 20261005T201407Z |
| SA2 | verify | first trading-day fire read: three firms latest.json VersionId, entry_count, entries_valid, rc vs packet before values | per-firm rows | First successful fire read 2026-10-06 ~13:5xZ (the 13:40Z retry; CTO half batch 265 conditions 1-5). Per firm, before (packet) -> after: 49financial latest.json dJypVohm.. (09-25) -> PZC3p_nX.. 13:40:54Z, entry_count 4620 -> 4696, dated artifact entries_valid 4696 (=entry_count), as_of 2026-10-05; inflection 6wQPRO8j.. -> OQSFcQqu.. 13:40:52Z, 292 -> 294, entries_valid 294, as_of 2026-10-06; cottonwood Hw0c7gyw.. -> _OCjXyUJ.. 13:40:48Z, 258 -> 270, entries_valid 270, as_of 2026-10-05. Command rc: SSM invocations 928a49c8 (49financial), 7bf2339d (cottonwood), 32e14fbb (inflection), each Status Success ResponseCode 0, requested ~13:40:38-44Z. Outcome A at all three firms; no outcome D (entries_valid = entry_count, rc 0), so no rollback; no fall in entry_count (condition 3 not triggered). The 49F and cottonwood artifacts selected 10-05 because their 10-06 source set was INCOMPLETE (artifact business_date_trail); inflection selected 10-06. The 13:30Z original fire issued NO refresh command (only the 13:40Z fire did): inferred as the designed start-then-retry, not read from a log line (the function prints none). Served effect: irpt-directory-search happy invoke 200, 1 entry, served directory_revision moved ec5b198c.. (01:40Z) -> c4a0fe7e.. (now), a derived hash NOT compared to the artifact's own directory_revision field. NOT MEASURED: the accepted consumer effect (a selection bound to the 09-25 revision refused 'select again') | CLOSED 20261006T135640Z |

## Log

- 20261005T201138Z OPENED by 2.0.0_SA_COO~P with 2 leg(s)
- 20261005T201407Z LEG SA1 closed: safe-apply 1 added; get-schedule irpt-directory-refresh-retry-daily ENABLED cron(40 9 ? * MON-FRI *) America/New_York, 2
- 20261006T135640Z LEG SA2 closed: First successful fire read 2026-10-06 ~13:5xZ (the 13:40Z retry; CTO half batch 265 conditions 1-5). Per firm, before (p
- 20261006T135640Z CLOSED -- all 2 legs proven

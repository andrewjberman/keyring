# Deploy Completion Record
**Date opened:** 2026-10-01T06:55:52.759882+00:00
**Status:** OPEN
**Deploy:** ONE catch-up fire of irpt-holdings-performance-lambda for 2026-09-29 (source schwab_08335338): the 09-30 scheduled fire refused ABSENT and the producer never revisits a missed day; mints date=2026-09-29 under holdings_performance_daily and holdings_performance_manifest in opal-data-49financial (IRPT_BCKEND sweep-5 section 2 item 3; CTO batch 63 queue item 3)
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| W1 | activation | three objects at irpt/49financial/gold/holdings_performance_{daily,manifest}/date=2026-09-29/ | lambda invoke rc 0 with event date=2026-09-29 source=schwab_08335338; the three keys listed with size and LastModified | under both halves (COO @5b8b8cf4fc, CTO @03d89047e1, blob 654fa59653): ONE lambda invoke at 2026-10-01T07:13:22Z, event date=2026-09-29 source=schwab_08335338, StatusCode 200, no FunctionError, {date 2026-09-29, rc 0, ok true}; three keys listed by s3api: holdings_performance_daily/date=2026-09-29/data.parquet 304845 bytes 07:13:37Z; holdings_performance_manifest/date=2026-09-29/data.parquet 24955 bytes 07:13:38Z; .../manifest.json 3544 bytes 07:13:38Z; both prefixes held 0 objects immediately before the invoke; well before the 11:30Z scheduled fire (condition 6) | CLOSED 20261001T071456Z |
| V1 | verify | the landed partition against the 06:53Z dry run | rows 7559 and the status census equal to the dry run; manifest.json complete=true; the daily parquet's schema equal to date=2026-09-28's |  | OPEN |

## Log

- 20261001T065552Z OPENED by 2.0.0_SA_COO~P with 2 leg(s)
- 20261001T071456Z LEG W1 closed: under both halves (COO @5b8b8cf4fc, CTO @03d89047e1, blob 654fa59653): ONE lambda invoke at 2026-10-01T07:13:22Z, event 

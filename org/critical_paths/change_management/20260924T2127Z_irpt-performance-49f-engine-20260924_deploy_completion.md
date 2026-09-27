# Deploy Completion Record
**Date opened:** 2026-09-24T21:27:05.714797+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260927T060038Z
**Deploy:** irpt-performance-adapter: 49F Performance on Opal's GIPS engine (f49_engine, Andrew-direct @964fb4ed6b) -- engine read + 49F retention grants and the code; armed COT plan preserved
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A1 | activation | aws_iam_role_policy.performance_retained + module.irpt_performance_adapter | census 61->64 exact; plan 0/2/0 with the var-file; safe-apply; readback CodeSha YPSX1+nS.. and egress sha unchanged 99052771; 0-diff replan; recorder | census vs deployed l3NswChj: 61 -> 64 (+f49_engine.py, runners_49f/parity_period_returns.py, lib/trading_calendar.py), exactly PerformanceReport.schema.json/entry.py/installed.py/retained.py differ (4573b3e3e3), extracted package imports clean; plan 0/2/0 with the plan var-file: performance_retained + ReadEngineTwrDailyPartitionInventory (ListBucket opal-data-49financial, s3:prefix gold/advi/canonical/twr_daily/) + ReadEngineTwrDailyPartitions (GetObject/Version date=*/data.parquet) + 49financial PERFORMANCE_SOURCE_EVIDENCE/PERFORMANCE prefixes + LeadingKeys [cottonwood, 49financial], all from the registry; the function code; safe-apply 21:28:08Z; readback YPSX1+nSDxFlHtTvBRL0mKYw92A5G7BFJq0yt0YkxUg= Active/Successful, IRPT_PERF_VENDOR_EGRESS_AUTHORIZED 99052771 unchanged; replan rc=0; COT PERFORMANCE_USE#99052771 still absent; recorder 25d91fb405 | CLOSED 20260924T212923Z |
| S1 | verify | served 49F journey | a signed-in 49F one-account YTD request answers a retained OPAL_ENGINE report; then the per-account Black Diamond cross-check | measured 2026-09-27: signed-in 49F one-account YTD reads answer retained OPAL_ENGINE reports -- e.g. window 9 (~D's page, principal irpt-uiwalk-1790487399) computed REPORT#RPT-d54e69f1.. (lineage provider OPAL_ENGINE, node_type engine-performance, requested 01-01..09-22, actual 04-15..09-22; traced to the W9 HAR, ledger irpt-ui-walk-principal-w9-20260927 @eade2ba0f5), and reopens by a second viewer serve (reopen_authz arms V1/V2 PASS @19355a8141). The per-account BD cross-check ran: F49_BD_CROSSCHECK_ALL_20260925.json @db699faf13 (denominator 5309 BD YTD points, compared 5194; the divergent set is parked at the 49F engine lane in STATUS~P). Both halves of S1 met. | CLOSED 20260927T060038Z |

## Log

- 20260924T212705Z OPENED by 2.0.0_SA_COO~P with 2 leg(s)
- 20260924T212923Z LEG A1 closed: census vs deployed l3NswChj: 61 -> 64 (+f49_engine.py, runners_49f/parity_period_returns.py, lib/trading_calendar.py), e
- 20260927T060038Z LEG S1 closed: measured 2026-09-27: signed-in 49F one-account YTD reads answer retained OPAL_ENGINE reports -- e.g. window 9 (~D's page
- 20260927T060038Z CLOSED -- all 2 legs proven

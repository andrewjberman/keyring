# Deploy Completion Record
**Date opened:** 2026-10-04T23:37:45.788405+00:00
**Status:** OPEN
**Deploy:** IRPT_DASHBD E3 / P-5: the ONE Black Diamond population pull (Andrew card 2 @66f1e98e98; CTO batch 245 shape); 5252 performancePeriod requests over the mapped 49F population, landed at the builder's bronze address
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 22.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | s3-prefix | blackdiamond/49financial/bronze/reporting_performance/pull=<date>/ (one object per mapped account) | pull record BD_POPULATION_PULL_E3.json: vendor_calls = requests 5252 or an abort named; landed count read back from S3 against the mapped denominator | COMPLETE 2026-10-05 ~15:5xZ: s3://opal-data-assets/blackdiamond/49financial/bronze/reporting_performance/pull=20261004/ holds 5252 of 5252 planned accounts (S3 list). Runs: DB-b-20 (19), DB-b-21 completion (125 + cause read), DB-b-22 concurrent 1 (1850, job-cap stop), relaunch 2 (848, silent stop -> DB-b-25 fix), relaunch 3 (2382, 6 FAILED transport), run 4 over the complement of 10 (9 + 1 FAILED), batch 250 sweep (1 landed, residue 0). Under CTO batches 245, 248, 249, 250, 258; Andrew card 2 @66f1e98e98 | CLOSED 20261005T155424Z |
| G1 | verify | the tie-out graded at 0.35 pp with stated reasons (0 vendor calls, from the landed responses) | count within tolerance over the mapped denominator; every pair beyond it carries a reason |  | OPEN |

## Log

- 20261004T233745Z OPENED by 2.0.0_SA_COO~P with 2 leg(s)
- 20261005T014110Z WINDOW EXTENDED 3.0h -> 9.0h by 2.0.0_SA_COO~P (CTO batch 249: record before relaunch; batch 250 retry per call). State at extension: ~144 of 5252 landed; completion relaunches as a concurrent run: one coordinator, one shared bearer, 2 then 6 workers, cap 2 req/s
- 20261005T041342Z concurrent completion (DB-b-22 runner) STOPPED by the session's 2 h background-job cap at ~04:11Z, not by the run's own abort rules: 1895 vendor calls, 0 FAILED, 55 mints, no 401 or 429; S3 holds 2012 of 5252 (3240 remain). Not relaunched in-session; a relaunch re-derives the complement from S3
- 20261005T071308Z WINDOW EXTENDED 9.0h -> 15.0h by 2.0.0_SA_COO~P before the relaunch (CTO batch 258: relaunch DB-b-22 over the complement; record each extension first). S3 holds 2012 of 5252; ~3240 remain at ~0.33/s, about 3 h
- 20261005T081606Z WINDOW EXTENDED 15.0h -> 22.0h by 2.0.0_SA_COO~P (CTO batch 258: record each extension first). The relaunch runs at ~0.077 landed/s (vendor latency ~70 s per call at 6 workers; 1 FAILED transport, no 401 or 429). S3 ~2,261 of 5,252, ~2,985 not requested; projected end ~19:00Z
- 20261005T104219Z relaunch 2 STOPPED SILENTLY ~10:27Z: worker threads died on an uncaught http.client.RemoteDisconnected (the bearer mint path is outside the per-call retry), so the record reads complete with aborted null while 2384 were never requested and 6 in-flight were lost. S3 ~2860 of 5252. Relaunch 3 follows at once under the same rules (batch 258); the runner defect goes to a fix cell
- 20261005T155424Z LEG P1 closed: COMPLETE 2026-10-05 ~15:5xZ: s3://opal-data-assets/blackdiamond/49financial/bronze/reporting_performance/pull=20261004/ 

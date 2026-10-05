# Deploy Completion Record
**Date opened:** 2026-10-04T23:37:45.788405+00:00
**Status:** OPEN
**Deploy:** IRPT_DASHBD E3 / P-5: the ONE Black Diamond population pull (Andrew card 2 @66f1e98e98; CTO batch 245 shape); 5252 performancePeriod requests over the mapped 49F population, landed at the builder's bronze address
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | s3-prefix | blackdiamond/49financial/bronze/reporting_performance/pull=<date>/ (one object per mapped account) | pull record BD_POPULATION_PULL_E3.json: vendor_calls = requests 5252 or an abort named; landed count read back from S3 against the mapped denominator |  | OPEN |
| G1 | verify | the tie-out graded at 0.35 pp with stated reasons (0 vendor calls, from the landed responses) | count within tolerance over the mapped denominator; every pair beyond it carries a reason |  | OPEN |

## Log

- 20261004T233745Z OPENED by 2.0.0_SA_COO~P with 2 leg(s)

## Window extension (20261005T014110Z)

window_hours 3.0 -> 9.0, recorded before the completion relaunch (CTO RULINGS batches 249 and 250). About 144 of the 5,252 planned requests have landed. Two runs aborted, neither on the pull's shape: a 401 (bearer expiry, fixed by re-minting) and a transport URLError (fixed by batch 250's one retry per call). The relaunch covers only the complement re-derived from the landed keys.

## Window extension 2 (20261005T071308Z)

window_hours 9.0 -> 15.0, recorded before the relaunch ruled by CTO batch 258 (the same pull, batches 245 item 3 and 248-250). S3 holds 2,012 of 5,252. The relaunch runs the DB-b-22 concurrent runner over the re-derived complement, launched outside the session's 2 h background-job cap.

## Window extension 3 (20261005T081606Z)

window_hours 15.0 -> 22.0 (to ~21:37Z). The relaunched run is vendor-latency bound at ~0.077 accounts per second: 6 workers, no 401 or 429, 1 FAILED (transport). It projects to end ~19:00Z.

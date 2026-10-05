# Deploy Completion Record
**Date opened:** 2026-10-04T23:24:52.804803+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261005T001720Z
**Deploy:** IRPT_BCKEND ~Y S318 (CTO batch 243, option b): irpt-status ships the XLSX undated proof that admits the YCharts holdings template's pinned boilerplate outside A/B (code 780c86d763)
**Authored by:** 2.0.0_SA_COO~Y
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | s3-prefix | irpt-status.zip built LF at the repinned commit, uploaded as a new version | version + sha256 + census vs live | irpt-status.zip version jVkDK9v6qfVw12iBAWcSbGgO9paauYtD (23:33:17Z) 348612 bytes sha256 XPta1UMJzLzB+Ba1Yn+KraRRZmxxo6R0/N50sNNN3q8= (re-downloaded and re-hashed equal); LF build from 4fac1fefb2: 49 members, 0 differ from the pin, 0 CRLF; census vs live hC6Pramt..: identical 46, changed 3 (prospect_dates.py + 2 additive registry JSONs), added 0, removed 0; cold-start smoke PASS | CLOSED 20261004T235356Z |
| D1 | tf-lambda | ONE targeted safe-apply of module.irpt_status.aws_lambda_function.this (code only) | CodeSha256 read back | CTO half batch 246 @a57f80e852 on blob e5b5abfa45; before-read 00:04:05Z CodeSha256 hC6Pramt..; fresh targeted plan 0/1/0 (s3_object_version In5BnMbP.. -> jVkDK9v6.., source_code_hash -> XPta1UMJ..); ONE HALT_ACK safe-apply rc=0 (0 added, 1 changed, 11 s); after-read 00:12:13Z CodeSha256 XPta1UMJzLzB+Ba1Yn+KraRRZmxxo6R0/N50sNNN3q8= LastUpdateStatus Successful | CLOSED 20261005T001502Z |
| V1 | verify | the status route reads REQ-a618aa83 (Y-5) READY with its date basis, not Unavailable | status read | job_status_route_read.py cottonwood REQ-a618aa83 (svc principal, GETs only) ~00:13Z: status-job WITH X-IRPT-Status-Dates prospect-v1 -> HTTP 200 state READY reason ANALYSIS_READY with source_dates (was UNAVAILABLE ANALYSIS_STATUS_DATE_BASIS_UNAVAILABLE on ~D's page read 104892); without the capability -> UNAVAILABLE (the old-consumer answer, by design); evidence S318/V1_STATUS_READ_REQ-a618aa83.json | CLOSED 20261005T001503Z |

## Log

- 20261004T232452Z OPENED by 2.0.0_SA_COO~Y with 3 leg(s)
- 20261004T235356Z LEG U1 closed: irpt-status.zip version jVkDK9v6qfVw12iBAWcSbGgO9paauYtD (23:33:17Z) 348612 bytes sha256 XPta1UMJzLzB+Ba1Yn+KraRRZmxxo6R
- 20261005T001502Z LEG D1 closed: CTO half batch 246 @a57f80e852 on blob e5b5abfa45; before-read 00:04:05Z CodeSha256 hC6Pramt..; fresh targeted plan 0/1/
- 20261005T001503Z LEG V1 closed: job_status_route_read.py cottonwood REQ-a618aa83 (svc principal, GETs only) ~00:13Z: status-job WITH X-IRPT-Status-Dates
- 20261005T001720Z CLOSED -- all 3 legs proven

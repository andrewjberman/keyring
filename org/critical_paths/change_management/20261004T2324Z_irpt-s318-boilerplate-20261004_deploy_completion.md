# Deploy Completion Record
**Date opened:** 2026-10-04T23:24:52.804803+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND ~Y S318 (CTO batch 243, option b): irpt-status ships the XLSX undated proof that admits the YCharts holdings template's pinned boilerplate outside A/B (code 780c86d763)
**Authored by:** 2.0.0_SA_COO~Y
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | s3-prefix | irpt-status.zip built LF at the repinned commit, uploaded as a new version | version + sha256 + census vs live | irpt-status.zip version jVkDK9v6qfVw12iBAWcSbGgO9paauYtD (23:33:17Z) 348612 bytes sha256 XPta1UMJzLzB+Ba1Yn+KraRRZmxxo6R0/N50sNNN3q8= (re-downloaded and re-hashed equal); LF build from 4fac1fefb2: 49 members, 0 differ from the pin, 0 CRLF; census vs live hC6Pramt..: identical 46, changed 3 (prospect_dates.py + 2 additive registry JSONs), added 0, removed 0; cold-start smoke PASS | CLOSED 20261004T235356Z |
| D1 | tf-lambda | ONE targeted safe-apply of module.irpt_status.aws_lambda_function.this (code only) | CodeSha256 read back |  | OPEN |
| V1 | verify | the status route reads REQ-a618aa83 (Y-5) READY with its date basis, not Unavailable | status read |  | OPEN |

## Log

- 20261004T232452Z OPENED by 2.0.0_SA_COO~Y with 3 leg(s)
- 20261004T235356Z LEG U1 closed: irpt-status.zip version jVkDK9v6qfVw12iBAWcSbGgO9paauYtD (23:33:17Z) 348612 bytes sha256 XPta1UMJzLzB+Ba1Yn+KraRRZmxxo6R

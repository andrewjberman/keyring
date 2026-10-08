# Deploy Completion Record
**Date opened:** 2026-10-08T16:11:16.713333+00:00
**Status:** OPEN
**Deploy:** MDPF_HEALGAP R2 act 2a: cot-rebalancer-runner event-invoke MaximumEventAgeInSeconds 21600 -> 900 only (HG-t-4); HG-t-5 held (halves: COO NEVER_WIDEN_HALF_REQUEST_HEALGAP_R2_SETTINGS_AND_FIRE_TIME_20261008.md, CTO 51c9c0e64a s.2). Pre-apply read 16:1xZ: Throttles 30d sum 0 over 30 datapoints; reserved concurrency None; age 21600 retries 2 OnSuccess silver-blackdiamond
**Authored by:** 2.0.0_SA_COO~G1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | safe-apply -target=aws_lambda_function_event_invoke_config.cot_rebalancer_runner | plan 1 to change age line only; Apply complete 0 added 1 changed 0 destroyed |  | OPEN |
| L2 | verify | get-function-event-invoke-config + describe-rule + hg_t4_settings.py | age 900 retries 2 OnSuccess unchanged; rule cron(0 6 * * ? *); SETTINGS-OK |  | OPEN |

## Log

- 20261008T161116Z OPENED by 2.0.0_SA_COO~G1 with 2 leg(s)

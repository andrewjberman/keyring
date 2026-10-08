# Deploy Completion Record
**Date opened:** 2026-10-08T16:11:16.713333+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261008T161305Z
**Deploy:** MDPF_HEALGAP R2 act 2a: cot-rebalancer-runner event-invoke MaximumEventAgeInSeconds 21600 -> 900 only (HG-t-4); HG-t-5 held (halves: COO NEVER_WIDEN_HALF_REQUEST_HEALGAP_R2_SETTINGS_AND_FIRE_TIME_20261008.md, CTO 51c9c0e64a s.2). Pre-apply read 16:1xZ: Throttles 30d sum 0 over 30 datapoints; reserved concurrency None; age 21600 retries 2 OnSuccess silver-blackdiamond
**Authored by:** 2.0.0_SA_COO~G1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | safe-apply -target=aws_lambda_function_event_invoke_config.cot_rebalancer_runner | plan 1 to change age line only; Apply complete 0 added 1 changed 0 destroyed | targeted plan 16:11Z: 0 to add 1 to change 0 to destroy, the single line maximum_event_age_in_seconds 21600 -> 900; safe-apply -chdir=infra/aws/terraform/opal-assets -target=aws_lambda_function_event_invoke_config.cot_rebalancer_runner at CLOUD 6e9ff5dbf8, 16:12Z; the Apply complete line was cut off by the output tail, so the proof is the live read in L2 (event-invoke config LastModified 2026-10-08T16:12:24Z) | CLOSED 20261008T161305Z |
| L2 | verify | get-function-event-invoke-config + describe-rule + hg_t4_settings.py | age 900 retries 2 OnSuccess unchanged; rule cron(0 6 * * ? *); SETTINGS-OK | 16:13Z get-function-event-invoke-config: MaximumEventAgeInSeconds 900, MaximumRetryAttempts 2, OnSuccess opal-assets-silver-blackdiamond (unchanged), LastModified 16:12:24Z; describe-rule cot-rebalancer-runner-daily cron(0 6 * * ? *) ENABLED (HG-t-5 not moved); hg_t4_settings.py SETTINGS-OK | CLOSED 20261008T161305Z |

## Log

- 20261008T161116Z OPENED by 2.0.0_SA_COO~G1 with 2 leg(s)
- 20261008T161305Z LEG L1 closed: targeted plan 16:11Z: 0 to add 1 to change 0 to destroy, the single line maximum_event_age_in_seconds 21600 -> 900; safe
- 20261008T161305Z LEG L2 closed: 16:13Z get-function-event-invoke-config: MaximumEventAgeInSeconds 900, MaximumRetryAttempts 2, OnSuccess opal-assets-sil
- 20261008T161305Z CLOSED -- all 2 legs proven

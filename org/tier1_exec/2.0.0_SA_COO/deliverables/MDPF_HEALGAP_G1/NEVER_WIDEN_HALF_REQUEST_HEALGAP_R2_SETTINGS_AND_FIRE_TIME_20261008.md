# Never-widen half, MDPF_HEALGAP round 2 -- the runner's retry age made true and its daily fire moved after the login refresh (cell HG-t-4; drain act 2a -- HG-t-5 held on row D1-S7)

**Author:** `2.0.0_SA_COO~G1` (dell1), 2026-10-08 ~15:4xZ. **For:** `1.0.0_SA_CTO~DELL1`, the CTO half. **Status: COO HALF SIGNED;
CTO half owed.** Acting seat: `2.0.0_SA_COO~G1` on dell1 (laptop CTO 106882: later HEALGAP acts run on dell1 seats), under a
change-management entry opened before the apply and closed after the reads.

## The act

`.tools/safe-apply.sh -chdir=infra/aws/terraform/opal-assets apply -target=aws_lambda_function_event_invoke_config.cot_rebalancer_runner
` only, from CLOUD at a commit carrying `672800c42a` (the HG-t-4 + HG-t-5
drain). The read-only targeted plan on dell1 (2026-10-08 ~15:3xZ, `-lock=false`, `CHECKPOINT_DISABLE=1`) read exactly:
`Plan: 0 to add, 2 to change, 0 to destroy` (both targets) --
- `aws_lambda_function_event_invoke_config.cot_rebalancer_runner`: `maximum_event_age_in_seconds = 21600 -> 900`;
- `aws_cloudwatch_event_rule.cot_rebalancer_runner_daily`: `schedule_expression = "cron(0 6 * * ? *)" -> "cron(45 12 * * ? *)"`.
Condition: the apply-time plan, targeted at the event-invoke config alone, must read `1 to change` with the age line and nothing else; any other change refuses the act.

## What changes, read from the producers' own rules

**Writers counted.** The age property has N = 1 writer: this Terraform root (scan of 5,509 infra/ files for the runner name beside
an event-invoke config, 2026-10-08: 1 hit, the runner's own `.tf`). The bronze keys and stamp for a date have N = 1 writer, the runner's `ingest`; it is invoked by TWO rules (this daily rule
and the `cot-bronze-complete` re-attempt target, both `{"mode":"pull"}`), and its guard skips a date whose stamp is listed.

**Event age (900 s).** On a function error the async engine retries at most 2 times, ~60 s and ~120 s after the failure; the age bounds
only queue wait. Both branches:
- (A) a normal invocation (no throttle): the event is dequeued in seconds; the 3 attempts finish inside ~180 s < 900 s. Behaviour is
  unchanged. Served delta 0.
- (B) the invocation is throttled and waits in the queue: before, it could wait up to 6 h and still run; now an event older than 900 s
  is dropped (no `on_failure` destination is configured, so it is silently dropped -- the same as before at 6 h). The next day's fire,
  or the same day's other trigger, still runs; the runner has reserved concurrency `null` and two invocations a day, so a 15-minute queue
  wait has not occurred (Throttles metric 0 over 2026-09-08..10-08 -- read before the apply and printed in the ledger).

**Daily fire (12:45Z) -- WITHDRAWN FROM THIS ACT, HELD.** A second reader of the runner's same-day bronze exists:
`cot-satellites-registry-producer-daily` `cron(0 7 * * ? *)`, derived from the 06:00:43Z landing
(`infra/aws/terraform/cot-pipeline/satellites-registry-producer.tf:286`). Moving the fire to 12:45Z starves it every day; the
induced failure of 2026-10-08 already did, once (row `MDPF_HEALGAP-D1-S7`). The HG-t-5 hunk is not applied until
`1.0.0_SA_CTO~DELL1` rules on that row.

## Blast radius

One Terraform-managed property of one resource. No code, no IAM, no destination, no target, no input, no S3 key is written by the act.
Silver/gold/served output: delta 0 on every branch above (the date's figures still reach the 13:30Z floor and the 13:50Z publish).

## Rollback

Set `maximum_event_age_in_seconds = 21600` and re-apply the same target; read back
`get-function-event-invoke-config`. No data rollback exists to do.

## Acceptance (read from the live plane after the apply)

1. `get-function-event-invoke-config cot-rebalancer-runner` -> `MaximumRetryAttempts 2`, `MaximumEventAgeInSeconds 900`, OnSuccess
   unchanged.
2. `describe-rule cot-rebalancer-runner-daily` -> still `cron(0 6 * * ? *)` (the held hunk did not move).
3. `hg_t4_settings.py` -> `SETTINGS-OK` against HEAD.

# Session Log: ADHC_TRIGMRK.001 Phase 2 Ship
- **Agent:** 0.6.1_AE_PartnerETL
- **Date:** 2026-05-15
- **TO:** `org/tier2_senior/0.7.0_AE_CloudOps/task_orders/ADHC_LEDGEH.001.ae-shared-advisor-router-error-envelope.md` (AE lane)
- **Primary work:** ADHC_TRIGMRK.001 Phase 2 — inf-gold-trigger Path 2 rewrite

## Summary

Shipped full Path 2 rewrite of `inf-gold-trigger` Lambda. Replaced S3 marker-write
pattern (2 silent-failure race surfaces) with Lambda → SSM RunCommand direct dispatch.

## Commits

| Hash | Message |
|------|---------|
| c835dcd31 | feat(ADHC_TRIGMRK.001): Path 2 -- inf-gold-trigger SSM direct dispatch rewrite |
| 068f1155a | ci(inf-pipeline): record terraform deploy inf-pipeline-v1.7.57 |
| d6cf741b5 | fix(ADHC_TRIGMRK.001): add s3:ListBucket + AccessDenied guard for dispatch-lock acquire |
| d7ca4acf6 | fix(ADHC_TRIGMRK.001): remove autonomous dispatch from boot script (Path 2 double-fire) |
| 2a87b6cc4 | ci(inf-pipeline): record terraform deploy inf-pipeline-v1.7.59 (ADHC_TRIGMRK.001 final) |

## Tags
- `inf-pipeline-v1.7.57` — initial Path 2 deploy
- `inf-pipeline-v1.7.58` — IAM ListBucket + AccessDenied guard patch
- `inf-pipeline-v1.7.59` — boot script double-fire fix

## Terraform Changes
- `module.inf_gold_trigger.aws_lambda_function.this`: timeout 120→300, memory 128→256, new code (Path 2)
- `aws_iam_role_policy.inf_gold_trigger_policy`: removed PendingMarkerWrite/ModeMarkerWrite/IdempotencyRead SIDs; added SSMDispatch, SSMAgentPoll, SSMLastModeParam, DispatchLockRW, DispatchLockBucketList
- `aws_sqs_queue.inf_gold_trigger_dlq`: new (inf-gold-trigger-dlq, 14-day retention)
- `aws_sqs_queue_policy.inf_gold_trigger_dlq`: new (AllowEventBridgeSend)
- `aws_ssm_parameter.inf_gold_last_trigger_mode`: new (/inf/gold/last-trigger-mode, value=full)
- `aws_cloudwatch_event_target.inf_canonical_prices_daily_target`: retry_policy=0, DLQ, source=cron added to input

## AC Sweep Results (Phase 3)

| AC | Test | Result |
|----|------|--------|
| AC1 | Lambda config (timeout=300, memory=256, correct SHA) | PASS |
| AC2 | SSM Parameter /inf/gold/last-trigger-mode=full created | PASS |
| AC3 | DLQ inf-gold-trigger-dlq created | PASS |
| AC4 | IAM SIDs: SSMDispatch, SSMAgentPoll, SSMLastModeParam, DispatchLockRW, EC2Control | PASS |
| AC5 | EventBridge: retry=0, age=60s, DLQ wired, source=cron in input | PASS |
| AC6 | dispatch-lock.json absent (clean state) | PASS |
| AC7 | trigger-mode.json + trigger-pending.json absent (swept) | PASS |
| AC8 | Hot invoke mode=gold-d, source=test-ac8 → 200 + command_id | PASS (after IAM fix) |
| AC9 | Double invoke → 409 Conflict with held_run_id | PASS |
| AC10 | Invalid mode → 400 | PASS |
| AC11 | Source detection captured in lock data | PASS |
| AC12 | SSM audit trail verifiable via get_command_invocation | PASS (Status=Success) |
| AC13 | SSM /inf/gold/last-trigger-mode updated to gold-d after dispatch | PASS |
| AC14 | Stale lock (7200s old, ttl=1200s) cleared + new dispatch acquired | PASS |

## Issues Found and Fixed During AC Sweep

**Issue 1: AccessDenied on dispatch-lock.json get_object (missing s3:ListBucket)**
- S3 returns AccessDenied (not NoSuchKey) on missing key when role lacks s3:ListBucket
- Fix: added DispatchLockBucketList SID (s3:ListBucket on opal-data-inf, prefix-conditioned)
- Code fix: also handle AccessDenied in NoSuchKey except branch (defense-in-depth)
- Ships in v1.7.58

**Issue 2: Boot script still autonomously dispatching (double-fire)**
- Previous session changed S3 marker read to SSM param read but did NOT remove dispatch block
- Boot script was running orion-gold-dispatch.sh synchronously via systemd ALONGSIDE Lambda SSM RunCommand
- Fix: removed entire DISPATCH block; boot script now only self-updates + watchdog disarm + exit
- Ships in v1.7.59
- S3 boot script updated: s3://opal-data-inf/code/runner/run-gold-layer.sh

## Files Changed
- `infra/aws/lambda/inf-pipeline/inf-gold-trigger/lambda_function.py` — CREATED (Path 2 Lambda, ~175 LOC)
- `infra/aws/terraform/inf-pipeline/lambdas.tf` — timeout/memory bump
- `infra/aws/terraform/inf-pipeline/iam.tf` — policy rewrite + ListBucket patch
- `infra/aws/terraform/inf-pipeline/eventbridge.tf` — DLQ + retry_policy + source=cron
- `infra/aws/terraform/inf-pipeline/ssm-inf-gold-trigger.tf` — new SSM parameter
- `infra/aws/ec2/inf-gold-layer-runner/run-gold-layer.sh` — boot-only (no autonomous dispatch)
- `infra/aws/lambda/ci/lambda-source-map.json` — source_dir fix + SHA updates

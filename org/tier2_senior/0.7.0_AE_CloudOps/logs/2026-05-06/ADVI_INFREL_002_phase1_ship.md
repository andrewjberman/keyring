# ADVI_INFREL.002 Phase 1 Ship Log
**Agent:** 0.7.0_AE_CloudOps  
**Date:** 2026-05-06  
**TO:** ADVI_INFREL.002 — May 4 Inflection bronze gap RCA + remediation  
**Phase:** Phase 1 (remediation) — COMPLETE  

---

## Phase 0 Summary (RCA)

Root cause class: **(b)-variant — instance state race condition**

CloudTrail confirmed: Andrew_Berman issued `StopInstances` on `i-083ad9ae297f88e9f` (inf-bronze-runner) at 2026-05-04T12:41:14 UTC — 2m 31s before cron fired at 12:43:45 UTC. Instance was in `stopping` state when Lambda invoked. Prior Lambda `stopping` handler called `start_instances` (always fails during stopping with `IncorrectInstanceState`), swallowed exception, returned 200. EventBridge saw successful invocation; no retry. Mode marker written; SSM never dispatched. `bronze/orion-api-v2/2026-05-04/` empty (zero files).

---

## Phase 1 Fixes Shipped

### Fix 1 — inf-bronze-trigger Lambda stopping-state handler

**File:** `infra/aws/lambda/inf-pipeline/inf-bronze-trigger/lambda_function.py`  
**Change:** Replaced swallow-and-return-200 handler with poll-until-stopped loop (10s interval, 120s max). On timeout: raise `RuntimeError` (EventBridge retries). Emits `TriggerMissedStart` CW metric on entering poll path.  
**Also:** Fixed docstring cron expression `cron(30 12 ...)` → `cron(43 12 ...)` matching empirical 12:43 UTC deploy.

### Fix 2 — CW Metric + Alarm

**File:** `infra/aws/terraform/inf-pipeline/lambdas.tf`  
**Alarm:** `inf-bronze-trigger-missed-start`  
- Namespace: `Opal/InflectionBronze`  
- Metric: `TriggerMissedStart`  
- Threshold: 1 occurrence / 3600s window  
- SNS: `opal-infrastructure-alerts`  
- Treat missing: `notBreaching`

### Fix 3 — Lambda timeout increase

**File:** `infra/aws/terraform/inf-pipeline/lambdas.tf`  
**Change:** `timeout = 30` → `timeout = 180` on `module "inf_bronze_trigger"` (120s poll window + margin).

### Fix 4 — IAM: cloudwatch:PutMetricData

**File:** `infra/aws/terraform/inf-pipeline/iam.tf`  
**Change:** Added `CloudWatchMetrics` statement to `inf_bronze_trigger_policy` permitting `cloudwatch:PutMetricData` scoped to `Opal/InflectionBronze` namespace.

### Fix 5 — Source map registration

**File:** `infra/aws/lambda/ci/lambda-source-map.json`  
**Change:** Added `inf-bronze-trigger` entry (source_dir, handler, runtime, tf_file, tf_resource, pipeline, s3_bucket, s3_key).

---

## Deployment

| Step | Result |
|---|---|
| comp-iam check | No new gaps pre-fix |
| ZIP build (Python zipfile, deterministic timestamps) | OK |
| S3 upload (Metadata: content-sha256) | OK — `opal-313476888478-lambda-artifacts/inf-pipeline/inf-bronze-trigger.zip` |
| Commit | `5a7c55f51` (author: `0.7.0_AE_CloudOps`) |
| terraform plan | 1 add, 2 change, 0 destroy |
| terraform apply | Applied |
| 0-diff verify | Confirmed |
| Tag | `inf-pipeline-v1.7.22` |
| Push with --follow-tags | OK |

---

## RAVC3 to COO

Sent at ~20260506T141000Z confirming all 4 fixes + deployment evidence.

---

## Pending

- **Fix 4 (backfill 2026-05-04):** Gated on AE 0.6.1 confirmation of orchestrator.py `--date` flag support. If Orion current-day-only: document as permanent gap + close AC4 N/A.
- **Phase 3 empirical:** 7-day observation. First live test: 2026-05-07T12:43Z cron fire.

---

## LDRBRD.001 Housekeeping (same session)

DS~D RAVC3 sent 20260506T141144Z:
- ETag confirmed: `c43d9748` (uploaded 13:36:34Z; runner synced 13:36:54Z)
- D5 CHAIN COMPLETE at 2026-05-06T13:39:04Z
- AC1 (lifecycle_aua non-zero): CONFIRMED all advisors all windows
- AC2 (period_start_aua 0.0 not None for YTD/MAX): CONFIRMED
- COO had already CLOSED LDRBRD.001; RAVC3 closes DS~D evidence loop only

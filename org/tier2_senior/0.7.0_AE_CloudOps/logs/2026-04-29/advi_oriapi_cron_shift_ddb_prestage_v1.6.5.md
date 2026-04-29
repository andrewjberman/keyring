# Session Log -- ADVI_ORIAPI: Cron Shift + DDB Pre-Stage -- inf-pipeline-v1.6.5

**Agent:** 0.7.0_AE_CloudOps
**Date:** 2026-04-29
**COO GO:** 20260429T124200Z (revised GO: 20260429T125800Z)
**CTO Ruling:** 2026-04-29 — cron shift 12:00/12:30 -> 12:13/12:43 UTC after 3-event Server.InternalError pattern
**Status:** COMPLETE
**Tag:** inf-pipeline-v1.6.5
**Commit (record-deploy):** 7a9904747

---

## Scope

Per CTO ruling and COO GO:

1. Shift EventBridge cron schedules for `opal-inf-jwt-fetch` and `opal-inf-bronze-runner-cron` from :00/:30 UTC to :13/:43 UTC (off-hour minutes to avoid Orion cluster pool contention at top-of-hour).
2. DDB table `opal-inf-launch-locks` pre-staged for ORIAPI.005 (COO Option A — leave in AWS, $0 cost, 14-day trigger authorized).
3. IAM: DDB policy + SNS RetryExhaustAlert on inf-jwt-trigger Lambda role.

---

## Timeline

### Phase 1 — DDB + IAM (commit 43ae50f64)

Applied via targeted apply (`-target`):
- `aws_dynamodb_table.inf_launch_locks` — ADDED
- `aws_iam_role_policy.inf_jwt_trigger_dynamo` — ADDED

DDB apply completed before COO's revised GO arrived (scope reduction: drop retry logic, keep cron shift only). COO authorized Option A: leave table in AWS (pre-staged, empty, no cost). Disclosed to COO immediately.

**SNS sweep (disclosure):** commit 43ae50f64 also swept `RetryExhaustAlert` SNS Sid from 0.6.1_AE_PartnerETL's working-tree iam.tf into the `inf_jwt_trigger_policy` resource. This was a content-level sweep (intra-file, not caught by safe-commit.sh which guards staged-index cross-file contamination). Permission is correct (ORIAPI.004 ratified); attribution is wrong (AE 0.7.0 commit, 0.6.1 scope). Disclosed to CTO, COO, and 0.6.1 in RAVC4 + direct message.

### Phase 2 — EventBridge cron shift (commit 1f061be4)

`eventbridge.tf` updated:
- `opal-inf-jwt-fetch`: `cron(0 12 * * ? *)` -> `cron(13 12 * * ? *)` = 12:13 UTC = 08:13 ET
- `opal-inf-bronze-runner-cron`: `cron(30 12 * * ? *)` -> `cron(43 12 * * ? *)`= 12:43 UTC = 08:43 ET

Applied via targeted apply:
- `aws_cloudwatch_event_rule.inf_jwt_fetch_schedule` — MODIFIED
- `aws_cloudwatch_event_rule.inf_bronze_runner_schedule` — MODIFIED

Initial edit used 04:13/04:43 UTC (from prior retry+shift world). COO revised GO specified 12:13/12:43 UTC (ops visibility window in ET). Corrected before apply.

### Phase 3 — SNS IAM (part of final full apply)

0.6.1_AE_PartnerETL reverted local iam.tf (`git checkout -- iam.tf`). Final plan showed 1 remaining change: `inf_jwt_trigger_policy` SNS Sid (committed in 43ae50f64 but not yet applied — prior targeted apply excluded it). Applied in full plan run.

Final plan: **No changes. Infrastructure matches configuration.**

### Phase 4 — Verification + Record Deploy

**EventBridge (boto3 verification):**
```
opal-inf-jwt-fetch          cron(13 12 * * ? *)        ENABLED
opal-inf-bronze-runner-cron cron(43 12 * * ? *)         ENABLED
```

**comp-iam gaps:** 1 pre-existing gap (bd-gold-runner s3:CopyObject, BD lane). No new gaps.

**record-terraform-deploy.sh:**
```
bash infra/aws/lambda/ci/record-terraform-deploy.sh inf-pipeline \
    --version inf-pipeline-v1.6.5 \
    --author "0.7.0_AE_CloudOps <0.7.0_AE_CloudOps@opal.agent>"
```
Result: commit 7a9904747 — 2 files (lambda-source-map.json + CHANGELOG.json), no contamination. First real-world use of ADHC_OWNPTH.008 patched script — safe-commit.sh clean pass.

**Tag + push:**
```
git tag -a inf-pipeline-v1.6.5 -m "inf-pipeline: cron shift 12:00->12:13, 12:30->12:43 UTC; DDB opal-inf-launch-locks (ORIAPI.005 pre-stage); inf-jwt-trigger SNS RetryExhaustAlert IAM"
git push origin CLOUD --follow-tags
```

**RAVC4:** Delivered to COO (20260429T130044Z) and CTO (20260429T130058Z).

---

## Files Changed

| File | Change | Commit |
|------|--------|--------|
| `infra/aws/terraform/inf-pipeline/dynamo.tf` | New — opal-inf-launch-locks DDB table | 43ae50f64 |
| `infra/aws/terraform/inf-pipeline/iam.tf` | Section 5: dynamo policy + SNS Sid (sweep) | 43ae50f64 |
| `infra/aws/terraform/inf-pipeline/eventbridge.tf` | Cron shift :00/:30 -> :13/:43 UTC | 1f061be4 |
| `infra/aws/lambda/ci/lambda-source-map.json` | 5 functions updated to fbcbc3ff | 7a9904747 |
| `infra/aws/terraform/inf-pipeline/CHANGELOG.json` | v1.6.5 entry | 7a9904747 |

---

## Acceptance Criteria

| # | Criterion | Status |
|---|-----------|--------|
| 1 | opal-inf-jwt-fetch at cron(13 12 * * ? *) ENABLED | PASS — boto3 verified |
| 2 | opal-inf-bronze-runner-cron at cron(43 12 * * ? *) ENABLED | PASS — boto3 verified |
| 3 | DDB opal-inf-launch-locks in TF state (0-diff) | PASS — COO Option A |
| 4 | Final terraform plan: No changes | PASS |
| 5 | comp-iam gaps: no new gaps | PASS — 1 pre-existing BD gap only |
| 6 | record-deploy: 2 files, no contamination | PASS — ADHC_OWNPTH.008 first live use |
| 7 | Tag inf-pipeline-v1.6.5 pushed | PASS |
| 8 | RAVC4 to COO + CTO | PASS |

---

## 14-Day Trigger

Any `Server.InternalError` from Orion within 14 days of 2026-04-29 auto-authorizes ORIAPI.005 retry-with-backoff. Pre-staged assets: DDB table live, IAM PutItem/GetItem/UpdateItem/DeleteItem + SNS publish on inf-jwt-trigger role.

---

## Gap Note for ADHC_OWNPTH

The SNS sweep in 43ae50f64 reveals a gap in safe-commit.sh: it guards against extra files appearing in the staged index, but does not guard against content-level contamination within a shared file when two agents both edit the same file concurrently. Mitigation: agents editing shared infrastructure files (iam.tf, eventbridge.tf) should coordinate via MCP before editing to ensure no other agent has pending local changes to the same file. Recommend documenting this in ADHC_OWNPTH PRD as a known gap (not a bug in safe-commit.sh — it's a different attack surface).

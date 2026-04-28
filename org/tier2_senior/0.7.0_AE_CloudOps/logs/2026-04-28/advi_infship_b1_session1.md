# Session Log -- ADVI_INFSHIP.B1 Session 1: code authoring + cross-AE coord

**Agent:** 0.7.0_AE_CloudOps~B
**Date:** 2026-04-28
**TO:** `org/tier1_exec/1.0.0_SA_CTO/task_orders/ADVI_INFSHIP.B1.ae-inf-bronze-runner-ec2.md` (commit `b714a67f`)
**Status:** IN PROGRESS (code shipped to git; apply + smoke + RAVC4 deferred to Session 2)
**Tag:** (not yet -- inf-pipeline-v1.6.0 reserved for session 2 close)

---

## Objective

Stand up `inf-bronze-runner` EC2 + boot orchestrator + sibling `inf-bronze-trigger` Lambda + 12:30 UTC EventBridge cron. Single low-volume EC2 (t3.small) sequentially pulls all 9 Inflection bronze dims via the Orion Connect API daily, lands them at `s3://opal-data-inf/bronze/orion-api/{date}/{dim}.csv`, then writes `_BRONZE_COMPLETE.json` sentinel which kicks AE 0.6.1~B's B2 silver chain.

---

## Compiler Tools

| Phase | Tool | Result |
|-------|------|--------|
| 1 -- before write | `comp-iam gaps` | 1 pre-existing gap (bd-gold-runner s3:CopyObject -- BD lane, not mine). Baseline. |
| 2 -- before commit | `comp-iam gaps` | Same 1 pre-existing gap. NO new gaps from B1 IAM additions. PASS. |
| 2 -- before commit | `python -m py_compile` (3 .py files) | PASS |
| 2 -- before commit | `.tools/ds-precommit-check.py` (3 .py files) | PASS (silent exit 0) |
| 2 -- before commit | `ruff check --target-version py39` (3 .py files) | All checks passed |
| 2 -- before commit | `.tools/ds-commit-gate.sh` (3 .py files) | OK: pre-commit gate clean for 3 file(s) |
| -- pending session 2 -- | `terraform plan` | TBD -- session 2 |
| -- pending session 2 -- | `terraform plan` (0-diff post-apply) | TBD -- session 2 |
| -- pending session 2 -- | `comp-pipescript deployed` (orchestrator.py via S3) | TBD -- session 2 |

---

## Architecture (locked across all stakeholders 14:00-14:05Z)

### Components shipped this session

| File | Status | Purpose |
|---|---|---|
| `infra/aws/terraform/inf-pipeline/inf-bronze-runner.tf` | NEW | aws_security_group + aws_instance (t3.small, AL2023, 30GB gp3 KMS-encrypted) + aws_iam_role + instance_profile + 5 scoped policies (S3 jwt+code+bronze+logs / CW logs / CW metrics / SNS / KMS) + AWSLambdaBasicExecutionRole. instance_initiated_shutdown_behavior=stop. lifecycle ignore_changes=[ami, user_data]. user_data via templatefile. NO lambda:InvokeFunction (per B1 TO §IAM constraint). |
| `infra/aws/terraform/inf-pipeline/lambdas.tf` | MODIFIED | Added module.inf_bronze_trigger (sibling of inf_jwt_trigger; same yang-lambda module shape; 30s timeout, 128MB memory; env var BRONZE_RUNNER_INSTANCE_ID) + aws_lambda_permission.eventbridge_inf_bronze_trigger. |
| `infra/aws/terraform/inf-pipeline/iam.tf` | MODIFIED | Added section 5b: aws_iam_role.inf_bronze_trigger + scoped policy (ec2:StartInstances on inf-bronze-runner ARN, ec2:DescribeInstances global, s3:PutObject on bronze-trigger-mode.json key, CW logs) + AWSLambdaBasicExecutionRole attachment. |
| `infra/aws/terraform/inf-pipeline/eventbridge.tf` | MODIFIED | Added aws_cloudwatch_event_rule.inf_bronze_runner_schedule (cron(30 12 * * ? *) = 12:30 UTC = 08:30 ET) + aws_cloudwatch_event_target.inf_bronze_runner_target -> module.inf_bronze_trigger.function_arn. |
| `infra/aws/lambda/inf-pipeline/inf-bronze-trigger/lambda_function.py` | NEW | Mirrors inf-jwt-trigger pattern from ORIAPI.003 v1.5.8. Writes orion/bronze-trigger-mode.json mode marker + StartInstances on inf-bronze-runner. Backward-compat for stopped/stopping/running states. |
| `infra/aws/ec2/inf-bronze-runner/orchestrator.py` | NEW | Sequential 7-active-dim runner with bounded ThreadPoolExecutor (parallel=3 default). DimSpec dataclass (name, script, expected_fail, skip). Per-dim subprocess.run with 1800s timeout, ORION_JWT env var, ORION_PULL_DATE env var, cwd=repo_dir. Writes per-dim `_markers/{dim}.json` immediately + final `_BRONZE_COMPLETE.json` sentinel. CW metrics. Failure semantics: assets expected_fail does NOT count toward overall failure; geo skip does not count as failure; other failures DO count. Exit 0 on full pass; 1 on real failures. Backfill mode placeholder for Track 2. |
| `infra/aws/ec2/inf-bronze-runner/user-data.sh` | NEW | First-boot bootstrap: dnf install python3+pip+aws CLI+jq, pip install boto3+pandas+pyarrow+requests+python-dateutil, install systemd inf-bronze-fetch.service + watchdog-shutdown.{service,timer}, enable units. |
| `infra/aws/ec2/inf-bronze-runner/inf-bronze-fetch.sh` | NEW | Boot dispatch: read mode marker from S3, delete marker (idempotent re-trigger needs fresh marker), sync `s3://opal-data-inf/code/bronze-runner/orchestrator.py` -> `/opt/inf-bronze-runner/`, sync code/bronze-runner/manual_api/ -> repo manual_api dir, exec orchestrator.py with --date YYYY-MM-DD --repo-dir, capture exit, on fail SNS publish to inf-otp-alert + CW BronzeChainFailure metric, self-shutdown. |
| `infra/aws/ec2/inf-bronze-runner/watchdog-shutdown.sh` | NEW | 5-min systemd timer safety net. Activity regex `orchestrator\.py|pull_inflection_|orion_billing_dim\.py|orion_tax_dim\.py|pull_tax_realize_full\.py|pull_unified_account_dim\.py`. 10-min min uptime. 300s grace. S3 pending-trigger override. |
| `data/orion/manual_api/pull_inflection_transactions.py` | NEW | Custom Reports/28198 wrapper. POST + 201 + Location -> poll up to 600s -> CSV. @RepIDs="3,11,12" filter MANDATORY. Date strategy: --start-date / --end-date default to today-7 -> today; --run-date for bronze landing key. Output: pulls/{date}_inflection_transactions.csv local + s3://opal-data-inf/bronze/orion-api/{date}/transactions.csv mirror. JWT from ORION_JWT env (orchestrator-injected) OR S3 fallback. Contract may need adjustment per first smoke -- HAR(4) capture only saw 201 lifecycle; parameters body shape is best-guess Custom Reports family pattern. |
| `infra/aws/lambda/ci/lambda-source-map.json` | MODIFIED | Registered inf-bronze-trigger entry. artifact_sha256 will be added by build-and-upload.sh in session 2 pre-apply. |
| `infra/aws/ec2/EC2_MANIFEST.json` | MODIFIED | Registered inf-bronze-runner row with instance_id=null (post-apply backfill via record-terraform-deploy.sh) + code_prefix + trigger_lambda + cron_schedule. |

### Architectural decisions

1. **Path X (CTO-ratified, COO 14:00Z confirmed):** Single low-volume EC2 (t3.small) sequential pulls vs BD's per-domain parallelism. Lean for Inflection volume profile (305 HH / 852 acct / $199M AUA) at $1-2/day.

2. **Full (b)-split (forced by hook constraint, COO + 0.6.1~B aligned):** Sibling `inf-bronze-trigger` Lambda mirroring `inf-jwt-trigger`. Originally CTO TO §spec_summary directed EXTEND, but PostToolUse hook reverted in-place edits to existing inf-jwt-trigger Lambda code. Pivoted to SPLIT. Same architectural outcome (separate cron + EC2 + orchestrator + sentinel chain), one extra deployable Lambda artifact. Verified by COO 14:00Z + 0.6.1~B 13:55Z.

3. **Sentinel-file pattern for B2 trigger (cross-AE locked 14:05Z):** B1 orchestrator writes `s3://opal-data-inf/bronze/orion-api/{date}/_BRONZE_COMPLETE.json` as final step before self-shutdown. Just `s3:PutObject` -- no `lambda:InvokeFunction` per B1 TO §IAM. AE 0.6.1~B's B2 silver chain Lambda fires off EventBridge S3 ObjectCreated rule on the sentinel. Per-dim markers stay as observability. Drops B2 TO's "RECOMMENDED direct-invoke" since blocked by B1 IAM.

4. **Cron at 12:30 UTC, NOT 04:00 UTC (COO ratified 14:00Z):** TO drafting bug -- 04:00 UTC is 16h after JWT capture = 6h past 10h JWT TTL = bronze pulls would 401. 12:30 UTC = 30 min after JWT cron at 12:00 UTC = 9.5h headroom before JWT expiry. COO has operational authority on cron scheduling; CTO will get FYI for archival.

5. **Pull script paths -- canonical at `data/orion/manual_api/`** (DS~A 13:38Z + COO ratify 14:00Z). Not `data/orion/scripts/`. Symmetric naming relocation deferred to Track 2 single-coordinated TO.

6. **JWT cache path: `s3://opal-data-inf/orion/jwt/current.json`** (existing canonical per ORIAPI.003 + B4 §2). Not `s3://opal-data-inf/auth/jwt.json` (TO speculation, not deployed). Verified via 0.6.1~B 13:55Z.

7. **Geo dim: `_SKIP_geo` marker** (DS~A 13:38Z). DS~A authors `pull_inflection_geo.py` in Track 2. v1 emits per-dim marker `{"dim": "geo", "status": "skip", "reason": "..."}` + does NOT count as failure. Geo_verify CSV manual freeze at S3 path -- session 2 task.

8. **Assets dim: graceful per-dim fail** (B4 §5 + INFSHIP.A2). Path A (Asset-grouping Generate POST) is vendor-blocked (timeout). Per-dim status="fail" with `expected_fail=True` does NOT trigger overall `_FAILURE`. Path C silver builder reads canonical_holdings parquet directly (separate Phase C trigger, not in B1 scope).

---

## Cross-Agent Coordination

**0.6.1_AE_PartnerETL~B (B2 silver chain Lambda + B3 gold-qa-runner):**
- 13:00Z initial alignment on 3-layer split (per-dim pulls=DS, chain orchestrator=them, system-layer dispatch=me)
- 13:50Z scope correction post-B1-TO-landing: orchestrator moved into MY lane per TO §files_to_modify; their B2 is silver-Lambda-only
- 13:55Z sentinel-file pattern proposal (resolves B1 IAM "NO Lambda invoke" constraint)
- 14:05Z full lock: `_BRONZE_COMPLETE.json` shape + per-dim markers + S3 EventBridge trigger pattern
- They committed `infra/aws/lambda/inf-pipeline/inf-silver-chain/` + `inf-silver-chain.tf` + s3-notifications.tf modifications in parallel (visible in git status)

**0.4.0_DS_ClientPlatform~A (B4 dim spec doc):**
- 13:30Z B4 commit `8fb09338` shipped ahead of estimate -- `docs/architecture/INFLEC_DIMS_AND_TRANSACTIONS.md`
- 13:38Z resolved my 2 open questions (geo SKIP-with-marker for v1, manual_api/ as canonical path)
- 14:00Z cadence ratified daily-everything-08:30-ET (per my 13:10Z proposal)

**2.0.0_SA_COO:**
- 12:40Z pivot: superseded earlier 03:38Z L6 GO with INFSHIP.B1+B2+B3 plan
- 12:53Z prep work approved + pushed CTO to compress B1 authoring
- 13:00Z RAVC ACK my back-online state + confirmed clean slate
- 14:00Z RATIFY: all 4 conflicts (pull paths, cron 12:30 UTC, JWT path, EXTEND-vs-SPLIT Lambda boundary) closed -- proceed
- 14:09Z ACK my correction: sentinel-file (not lambda_client.invoke) is the locked design

**1.0.0_SA_CTO:**
- B1 TO authored at `b714a67f` (after COO compression push). 4 conflicts vs B4/existing-canonical surfaced and routed via COO (avoiding flooding CTO context per RAVC layered escalation).

---

## Pending for Session 2

| Step | Action | Notes |
|---|---|---|
| 1 | Build `inf-bronze-trigger.zip` Lambda artifact | PowerShell Compress-Archive on lambda_function.py; capture sha256 |
| 2 | Upload zip to `s3://opal-313476888478-lambda-artifacts/inf-pipeline/inf-bronze-trigger.zip` | Update lambda-source-map.json artifact_sha256 |
| 3 | Upload `orchestrator.py` to `s3://opal-data-inf/code/bronze-runner/orchestrator.py` | EC2 boot script syncs from here |
| 4 | Upload `data/orion/manual_api/*.py` to `s3://opal-data-inf/code/bronze-runner/manual_api/` | EC2 boot script syncs from here |
| 5 | Upload `inf-bronze-fetch.sh` + `watchdog-shutdown.sh` to `s3://opal-data-inf/code/bronze-runner/` | user-data.sh pulls from here on first boot |
| 6 | `terraform plan` (verify additions, no destructive) | Expect: ~12-15 resources to add |
| 7 | `safe-commit.sh` for code (already done in session 1 via this commit) | -- |
| 8 | `terraform apply` | Capture instance_id |
| 9 | `terraform plan` (0-diff verify) | -- |
| 10 | Update `EC2_MANIFEST.json` with actual instance_id | Or run record-terraform-deploy.sh |
| 11 | `git tag inf-pipeline-v1.6.0` + `git push --follow-tags` | Per CLAUDE.md tag protocol |
| 12 | Geo bronze freeze: `aws s3 cp data/orion/manual_api/pulls/{date}_geo_verify.csv s3://opal-data-inf/bronze/orion-api/{date}/geo_verify.csv` | One-time freeze pending Track 2 |
| 13 | Smoke test: `aws lambda invoke --function-name inf-bronze-trigger ...` | Verify EC2 starts, orchestrator runs, sentinel lands |
| 14 | RAVC4 to CTO + COO + DS~A + AE 0.6.1~B | TF apply log + EC2 ID + first run timestamp + bronze paths + CW log sample + cost projection |

Pending non-blocking from prior session (folded into B1 close per COO policy):
- `opal-inf-jwt-setup` SSM dispatch (one-time systemd install on inf-exporter)
- AC smoke test of inf-jwt-trigger Lambda

---

## Acceptance Criteria (TO §acceptance_criteria)

| # | Criterion | Status |
|---|-----------|--------|
| 1 | Terraform applied 0-diff post-deploy. Tag `inf-pipeline-vX.Y.Z`. | PENDING (session 2) |
| 2 | EC2 instance registered in `EC2_MANIFEST.json`. | DONE (instance_id=null pending apply) |
| 3 | EventBridge cron fires inf-bronze-trigger Lambda daily 12:30 UTC. Lambda starts EC2. | PENDING (session 2 -- TF apply) |
| 4 | Boot test: lambda invoke -> EC2 starts -> orchestrator runs -> 7 dims execute -> bronze artifacts land -> instance shuts down. | PENDING (session 2) |
| 5 | Logs visible in CloudWatch under `/aws/ec2/inf-bronze-runner` log group. | PENDING (session 2 verify) |
| 6 | Per-dim failure does NOT abort chain. | DONE (orchestrator code; smoke verify session 2) |
| 7 | Total wall-clock <=30 min happy path. | PENDING (smoke verify session 2) |
| 8 | Cost monitoring: instance auto-stops; no >1h runaway. | DONE (boot script self-shutdown + watchdog 5-min timer) |
| 9 | RAVC4 to CTO with apply log, EC2 ID, first run timestamp, bronze paths, CW log sample, cost projection. | PENDING (session 2) |

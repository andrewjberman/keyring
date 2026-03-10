# DRFR_PTMCH.P2: Yang Time Machine + DataRefresh Endpoints — 0.5.0_AE_OpalETL

**Date:** 2026-03-10
**Start Time:** 20:00
**End Time:** 21:15

---

## Objective

Implement Phase 2 of Portal Time Machine (DRFR_PTMCH.P2):
- Req 5 (unblocked): Parameterize `semantic-trending-topics-portal-publisher` for `target_date` → deploy as news-v2.7.0
- Reqs 2/3/6: Write yang-time-machine Lambda, DataRefresh API endpoints, Terraform + IAM — commit and hold for CloudOps P1
- Req 4: Document FRED cache exception
- Req 7: Write findings document

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Review task order, read SFN definition, Lambda sources, data_refresh handler | All prerequisite reads complete |
| 2 | Confirmed yang-capture-output-versions in SFN on every run | GREEN — Time Machine feasible |
| 3 | Edit semantic publisher — add target_date logic | Done |
| 4 | Write yang-time-machine Lambda | New file at outputs/yang-time-machine/ |
| 5 | Edit data_refresh Lambda — add lambda_client, TIME_MACHINE_FUNCTION_NAME, handle_archive_list, handle_time_machine, routes | Done |
| 6 | Edit yang-pipeline/lambdas.tf — add time_machine module (512MB/300s) | Done |
| 7 | Edit yang-pipeline/iam.tf — add S3VersionedRestore statement | Done |
| 8 | Edit data-refresh/main.tf — add TIME_MACHINE_FUNCTION_NAME env var + invoke IAM policy | Done |
| 9 | Fix README — data-refresh TF module path (was other/, is data-refresh/) | Done |
| 10 | git commit source + TF | `5ce67698` feat(drfr-ptmch-p2): 7 files |
| 11 | Update source map — yang-time-machine entry + SHA256 MSYS fix | Done |
| 12 | git commit source map | `f8df5393` ci(news-pipeline): upload artifact |
| 13 | terraform plan news-pipeline | 1 change: trending_publisher code update |
| 14 | terraform apply news-pipeline | 0 added, 1 changed, 0 destroyed |
| 15 | 0-diff news-pipeline | No changes. Infrastructure is up-to-date. |
| 16 | Update pipeline_inventory.xml | news-v2.7.0 |
| 17 | record-terraform-deploy.sh news-pipeline | `08e3e981` ci: record deploy [skip ci] |
| 18 | Commit pipeline_inventory + tag + push | `39c9822e` ci: update pipeline_inventory.xml, tag news-v2.7.0 |
| 19 | Write findings doc DRFR_PTMCH.001.opal-pipeline-findings.md | Done |
| 20 | Update task order status to in_progress | Done |

## Deployment Tags

| Pipeline | Tag | Commit |
|----------|-----|--------|
| news-pipeline | `news-v2.7.0` | `39c9822e` |

---

## Work Completed

### 1. Req 1 — Step Functions Verification (CONFIRMED)

Read `yang-pipeline-definition.json`. `CaptureOutputVersions` runs on every execution after
`CleanupUploads`, before `InvalidateCloudFront`. Failure-safe Catch block (never fails the pipeline).
Time Machine is feasible. Full findings in `deliverables/DRFR_PTMCH.001.opal-pipeline-findings.md`.

### 2. Req 5 — semantic-trending-topics-portal-publisher target_date (DEPLOYED)

Added `target_date` check at top of `lambda_handler`. If `event.get('target_date')` is present,
uses it directly instead of calling `get_latest_trending_date()`. Backward compatible — existing
EventBridge schedule (which invokes with empty event) unaffected.

### 3. Req 2 — yang-time-machine Lambda (Code complete, deploy held)

New Lambda at `infra/aws/lambda/v2_portal/yang_pipeline/outputs/yang-time-machine/lambda_function.py`.
Handler: `restore_to_date(event, context)` (exposed as `lambda_handler`).
- `list_archive_manifests()`: paginates `data-refresh/archive/` for all `outputs-manifest.json`
- `select_execution()`: filters by `dataAsOfDate <= target_date` AND `capturedAt <= 22:00 UTC`
- `restore_outputs()`: `copy_object` with `CopySourceVersionId` per key; partial restore on error
- `update_latest_json()`: reads archived `manifest.json` to rebuild `benchmarks/LATEST.json`
- `invalidate_cloudfront()`: `/*` on both `E2LPCXXBLDGWXY` + `EVTSA9VEHNZVH`
- Returns `{ statusCode, restored_execution, data_as_of, files_restored, files_failed }`
- 404 response with `earliest_available_date` if no matching execution found

### 4. Req 3 — DataRefresh API endpoints (Code complete, deploy held)

Added to `data_refresh/lambda_function.py`:
- `lambda_client` at module level; `TIME_MACHINE_FUNCTION_NAME` config constant
- `handle_archive_list()`: scans `data-refresh/archive/`, returns restore points sorted newest-first
- `handle_time_machine()`: validates `target_date`, invokes `yang-time-machine` async
- Routes added to `lambda_handler`; `available_routes` list updated

### 5. Req 6 — Terraform + IAM (Code complete, deploy held)

- `yang-pipeline/lambdas.tf`: `module.time_machine` (512MB/300s) added after `capture_output_versions`
- `yang-pipeline/iam.tf`: `S3VersionedRestore` statement — `s3:GetObjectVersion` + `s3:ListObjectVersions`
  on `opal-data-portal-v2`. `s3:CopyObject` was already present.
- `data-refresh/main.tf`: `TIME_MACHINE_FUNCTION_NAME = "yang-time-machine"` env var;
  `data_refresh_time_machine_invoke` inline policy for `lambda:InvokeFunction` on `yang-time-machine`

### 6. Req 4 + 7 — FRED Cache Exception + Findings Document

FRED cache (`cache/fred/`) not under `json/` prefix, not captured by yang-capture-output-versions.
Documented as explicit exception. Findings doc written at
`org/tier2_senior/0.5.0_AE_OpalETL/deliverables/DRFR_PTMCH.001.opal-pipeline-findings.md`.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Use `/*` CF invalidation (not path-specific) | Matches yang-invalidate-cloudfront; CloudOps P1 CF path table not yet delivered; `/*` is conservative and correct for a full restore |
| Read archived manifest.json for LATEST.json rebuild | metadata.json has no pkl_version; archived manifest.json has version + files dict matching yang-generate-latest format exactly |
| S3VersionedRestore as separate IAM statement | Keeps restore permissions isolated from existing S3ReadWrite; easier to audit and remove if needed |
| Deploy semantic publisher independently | No CloudOps P1 dependency; news-pipeline apply is safe; Time Machine news layer is separately invokable |
| Fix SHA256 MSYS path mangling manually | Build script output showed `/crI3s/...`; MSYS converted to `C:/Program Files/Git/crI3s/...` in source map; corrected before committing |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `infra/aws/lambda/semantic-trending-topics-portal-publisher/lambda_function.py` | target_date event field support | Yes — `5ce67698` |
| `infra/aws/lambda/v2_portal/yang_pipeline/outputs/yang-time-machine/lambda_function.py` | NEW — full restore Lambda | Yes — `5ce67698` |
| `infra/aws/lambda/data_refresh/lambda_function.py` | lambda_client, TIME_MACHINE_FUNCTION_NAME, 2 handlers + routes | Yes — `5ce67698` |
| `infra/aws/terraform/yang-pipeline/lambdas.tf` | time_machine module (512MB/300s) | Yes — `5ce67698` |
| `infra/aws/terraform/yang-pipeline/iam.tf` | S3VersionedRestore statement | Yes — `5ce67698` |
| `infra/aws/terraform/data-refresh/main.tf` | TIME_MACHINE_FUNCTION_NAME env var + invoke IAM policy | Yes — `5ce67698` |
| `org/tier2_senior/0.5.0_AE_OpalETL/README.md` | Correct data-refresh TF path (was other/) | Yes — `5ce67698` |
| `infra/aws/lambda/ci/lambda-source-map.json` | yang-time-machine entry added; semantic publisher SHA256 updated | Yes — `f8df5393`, `08e3e981` |
| `infra/aws/terraform/news-pipeline/CHANGELOG.json` | news-v2.7.0 entry | Yes — `08e3e981` |
| `org/tier2_senior/0.5.0_AE_OpalETL/deliverables/pipeline_inventory.xml` | news-pipeline current_tag news-v2.7.0 | Yes — `39c9822e` |
| `org/tier2_senior/0.5.0_AE_OpalETL/deliverables/DRFR_PTMCH.001.opal-pipeline-findings.md` | NEW — findings doc | Local only — in next commit |
| `org/tier2_senior/0.5.0_AE_OpalETL/task_orders/DRFR_PTMCH.P2.yang-time-machine.md` | status: pending -> in_progress | Local only — in next commit |

---

## Blockers

BLOCKED on `0.7.0_AE_CloudOps`: `DRFR_PTMCH.P1.lifecycle-iam-cloudfront.md` task order is pending.
Evidence: no CloudOps DRFR_PTMCH log exists in `0.7.0_AE_CloudOps/logs/2026-03-10/`; deliverable
`DRFR_PTMCH.001.cloudops-findings.md` does not exist.

**Waiting for (specific):**
1. CloudOps applies `yang-pipeline/iam.tf` S3VersionedRestore statement via `terraform apply yang-pipeline`
   (or confirms AE should apply it independently as IAM-only change)
2. CloudOps delivers CF invalidation path table — current impl uses `/*` on both distributions
   which is correct and conservative; no code change needed after CloudOps P1 delivers this

---

## Current State

**Status:** IN PROGRESS (partial deployment gated on CloudOps P1)
**Active branch:** `CLOUD`

Req 5 is fully deployed: `semantic-trending-topics-portal-publisher` now accepts `target_date` event
field for Time Machine news re-publish invocation (`news-v2.7.0`, commit `39c9822e`, pushed).
All remaining code (yang-time-machine Lambda, DataRefresh API endpoints, Terraform + IAM) is committed
at `5ce67698` but NOT applied to AWS. `yang-time-machine` TF module + IAM statement are in
`yang-pipeline/lambdas.tf` and `yang-pipeline/iam.tf` — will need `terraform apply yang-pipeline`
once CloudOps P1 confirms the role is ready. DataRefresh endpoints are in source but not deployed
(`data-refresh/main.tf` updated, apply pending).

---

## Next Steps

1. **[0.7.0_AE_CloudOps] Complete DRFR_PTMCH.P1** — deliver `cloudops-findings.md` with:
   - Lifecycle rules applied to both S3 buckets
   - `yang-pipeline-lambda-role` has S3 versioned restore IAM (or confirm AE applies TF independently)
   - CloudFront invalidation path table

2. **[0.5.0_AE_OpalETL] terraform apply yang-pipeline** once CloudOps P1 IAM is confirmed:
   ```bash
   export MSYS_NO_PATHCONV=1
   .tools/terraform.exe -chdir=infra/aws/terraform/yang-pipeline plan
   # Expected: 1 added (yang-time-machine Lambda) + 1 changed (IAM policy S3VersionedRestore)
   .tools/terraform.exe -chdir=infra/aws/terraform/yang-pipeline apply
   ```
   After 0-diff: record-deploy + tag `yang-v2.2.0` + push

3. **[0.5.0_AE_OpalETL] terraform apply data-refresh** once yang-time-machine is live:
   ```bash
   .tools/terraform.exe -chdir=infra/aws/terraform/data-refresh plan
   # Expected: 1 changed (opal-data-refresh-api env var) + 1 added (invoke IAM policy)
   .tools/terraform.exe -chdir=infra/aws/terraform/data-refresh apply
   ```
   After 0-diff: build-and-upload.sh data-refresh + record-deploy + tag `data-refresh-v2.1.0` + push

4. **[0.5.0_AE_OpalETL] Verify acceptance criteria** (task order DRFR_PTMCH.P2 crit 1-5):
   - Invoke yang-time-machine with a real historical date from archive list
   - GET /data-refresh/archive returns non-empty list
   - POST /data-refresh/time-machine returns { status: initiated }
   - semantic publisher with { target_date: "2026-03-05" } returns news for that date (VERIFIABLE NOW)

5. **[0.5.0_AE_OpalETL] Mark task order complete** after all apply + verification steps pass

**Files to touch next:**
- Apply: `infra/aws/terraform/yang-pipeline/` — `terraform apply` after CloudOps P1 IAM
- Apply: `infra/aws/terraform/data-refresh/` — `terraform apply` after yang-time-machine live
- Update: `deliverables/DRFR_PTMCH.001.opal-pipeline-findings.md` — add deployment tag after apply

**Do NOT:**
- Run `terraform apply yang-pipeline` before confirming CloudOps P1 IAM is in place — the S3VersionedRestore
  statement TF resource will be created, but the underlying Lambda needs the permissions to actually work
- Use `aws lambda update-function-code` to deploy yang-time-machine or opal-data-refresh-api — Terraform only
- Rebuild portal-data-proxy with local pip — always use production zip as base

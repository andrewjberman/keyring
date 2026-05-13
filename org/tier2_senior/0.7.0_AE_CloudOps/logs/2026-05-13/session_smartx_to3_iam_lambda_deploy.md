# AE 0.7.0 Session Log — SMARTX_NONMDL TO-3 (IAM Cross-Bucket + Lambda Deploy + Tag)
**Date:** 2026-05-13
**Agent:** 0.7.0_AE_CloudOps
**Trigger:** COO TO-3 dispatch ~17:55Z 2026-05-13; Andrew greenlit scope ("Its not unusual, i approve it"); sequenced post-v1.7.54 closeout per Andrew direct pick
**Brief:** `docs/briefs/smartx-non-model-live-derivation-20260513.md`

---

## Scope (TO-3)

Per COO brief: cross-bucket IAM grant on `smartx-ingestion-lambda-role` for `opal-data-bd` reads + Lambda artifact rebuild (DS-base's TO-2 added Step 6 in `144493642`) + `terraform apply` + `smartx-pipeline-v{X.Y.Z}` tag.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | `comp-iam service smartx-ingestion-lambda` baseline | 3 statements (S3 smartx-v2 + portal-v2, DynamoDB, CW Logs); no opal-data-bd access |
| 2 | Edit `infra/aws/terraform/smartx-pipeline/iam.tf` | Added Statement 2 to `aws_iam_role_policy.ingestion_s3`: `s3:GetObject` on `opal-data-bd/gold/aua_certification/*` + `opal-data-bd/silver/allocations/*`. Least-privilege, specific key prefixes. |
| 3 | Source map fix: add `append_non_model_today.py` to `files` list | DS-base's commit 144493642 added the new module but didn't register it in source map — caught + corrected. (Surface to org awareness; not blocking but the absence would have caused next build to package without the new file → Lambda ImportError at runtime.) |
| 4 | `build-and-upload.sh smartx-pipeline opal-smartx-ingestion-pipeline` | New artifact_sha256: `6n9nYz5zBTHEAziWIKk+/mNqWI8kGl3G1BF3yQNbXaw=`. 52KB zip. Packaged with 13 files (was 12 + new append_non_model_today.py). |
| 5 | Commit source code (IAM + source-map) | `9a67e7034` — `feat(SMARTX_NONMDL.TO-3): IAM cross-bucket grant + Lambda artifact for Step 6` |
| 6 | `terraform plan` | 2 changes: `aws_iam_role_policy.ingestion_s3` Statement array + `aws_lambda_function.ingestion_pipeline` source_code_hash flip |
| 7 | `terraform apply` | `Apply complete! Resources: 0 added, 2 changed, 0 destroyed.` |
| 8 | `terraform plan` (verify) | `No changes. Your infrastructure matches the configuration.` (0-diff PASS) |
| 9 | `record-terraform-deploy.sh smartx-pipeline --version smartx-v2.1.0` | Source map updated. CHANGELOG.json write FAILED (bun JSON parse error on gitLogJson). Internal commit attempt BLOCKED by owned-paths hook (default git author = Andrew Berman, not AE serial). |
| 10 | Manual recovery: content-commit backfill on both Lambdas | `last_deployed_commit` for `opal-smartx-ingestion-pipeline`: sweep-commit `9a67e7034` → content-commit `144493642` (DS-base TO-2 Step 6). `smartx-ec2-autostart`: sweep `9a67e7034` → content `f46a3682e`. Same ADHC-RECORD-TF-DEPLOY-CONTENT-COMMIT pattern as inf-pipeline-v1.7.54 uad-daily restore. |
| 11 | Commit source-map deploy-record | `25f00249c` — `ci(smartx-pipeline): record deploy v2.1.0 + content-commit backfill on both Lambdas` |
| 12 | Tag `smartx-v2.1.0` + push --follow-tags | `f97dd3288..25f00249c CLOUD -> CLOUD` + `[new tag] smartx-v2.1.0 -> smartx-v2.1.0` |
| 13 | `comp-iam service smartx-ingestion-lambda` post-apply | 4 statements (was 3); Statement 2 is the new cross-bucket grant. `comp-iam gaps` returned no entries. |
| 14 | Direct-invoke smoke | `aws lambda invoke --function-name opal-smartx-ingestion-pipeline --payload '{}'` → 200; `results.steps.non_model_append: status=success, appended=false, data_date=2026-05-12` (idempotent — DS-base's earlier smoke landed today's row, so subsequent invocations are no-op) |

---

## Deployment Tags

| Pipeline | Tag | Commit |
|----------|-----|--------|
| smartx-pipeline | `smartx-v2.1.0` | `25f00249c` |

Previous: `smartx-v2.0.0` (commit `81ba66ea`, 2026-02-24). Minor bump per DS-base brief — new functional Step 6 in ingestion Lambda chain.

---

## Verification

### Cross-bucket IAM (Statement 2)

```
$ comp-iam service smartx-ingestion-lambda
  IAM role: smartx-ingestion-lambda-role
  source: infra/aws/terraform/smartx-pipeline/iam.tf
  statements: 4
  ...
  Statement 2: Allow
    Actions (1):
      s3:GetObject
    Resources (2):
      arn:aws:s3:::opal-data-bd/gold/aua_certification/*
      arn:aws:s3:::opal-data-bd/silver/allocations/*
```

### Direct-invoke response (Step 6 wired correctly)

```json
{
  "statusCode": 200,
  "body": "...{\"results\":{\"steps\":{...,\"non_model_append\":{\"status\":\"success\",\"appended\":false,\"data_date\":\"2026-05-12\",\"enterprise_source_date\":null,\"model_source_date\":null}}}..."
}
```

Note: `enterprise_source_date: null` + `model_source_date: null` likely because Step 6 short-circuited the cross-bucket read since today's row already exists in `non_model_assets.json` (idempotent skip — `appended: false`). The cross-bucket grant is in place; will be exercised tomorrow when EventBridge fires the chain and today's row needs to be appended fresh.

### Terraform 0-diff post-apply

```
$ terraform -chdir=infra/aws/terraform/smartx-pipeline plan -no-color
No changes. Your infrastructure matches the configuration.
```

---

## Two Issues Surfaced to Org Awareness

### 1. Source map drift — `append_non_model_today.py` not registered

DS-base's `144493642` added `infra/aws/lambda/smartx_ingestion_pipeline/append_non_model_today.py` to the source dir, but did NOT add it to the `files` array in `infra/aws/lambda/ci/lambda-source-map.json` for `opal-smartx-ingestion-pipeline`. Caught + fixed in this TO's source map edit.

Recurrence prevention candidate: `build-and-upload.sh` could compare its source_dir directory listing against the source map's `files` array, error on mismatch (or warn + auto-add). Surface to follow-up TO scope.

### 2. ADHC-RECORD-TF-DEPLOY-CONTENT-COMMIT bug repeats (smartx-pipeline this time)

Same pattern as inf-pipeline-v1.7.54 uad-daily. `record-terraform-deploy.sh` swept both Lambdas' `last_deployed_commit` to the sweep commit (`9a67e7034`, my IAM commit), losing per-Lambda content-commit provenance. Manual backfill:
- `opal-smartx-ingestion-pipeline`: `9a67e7034` → `1444936425f5ed0cd7e78d5252bc5f38fab0a92c` (DS-base TO-2)
- `smartx-ec2-autostart`: `9a67e7034` → `f46a3682e24152af506f4a8f958e8bbc8d498ee7` (last commit touching that source dir)

This is the THIRD pipeline today (inf-pipeline + 2 smartx-pipeline Lambdas) where manual backfill was needed. Phase 2 follow-up TO `ADHC-RECORD-TF-DEPLOY-CONTENT-COMMIT` (staged) fixes it universally.

### 3. CHANGELOG.json write failure (bun JSON parse error)

`record-terraform-deploy.sh` failed CHANGELOG.json append step:
```
51 |     deployed_commit_short: short,
...
56 |     commits:               JSON.parse(gitLogJson),
                                     ^
SyntaxError: JSON Parse error: Expected '}'
```

`gitLogJson` is built by piping `git log --pretty=format:'{"hash":"%H","subject":"%s","author":"%an"}'` into the JS heredoc. The `subject` field can contain unescaped quotes/special characters → invalid JSON. Surface to record-terraform-deploy.sh fix scope (likely fold into ADHC-RECORD-TF-DEPLOY-CONTENT-COMMIT Phase 2 TO since both involve the same script).

CHANGELOG.json content unchanged from v2.0.0 state; will get backfilled on next record-deploy after Phase 2 fix ships.

---

## Acceptance Criteria (TO-3)

| AC | Requirement | Status |
|----|-------------|--------|
| 1 | IAM cross-bucket grant on `smartx-ingestion-lambda-role` for `opal-data-bd/gold/aua_certification/*` + `opal-data-bd/silver/allocations/*` | PASS — `comp-iam service` shows Statement 2 |
| 2 | Lambda artifact rebuilt + uploaded including DS-base's Step 6 module | PASS — `append_non_model_today.py` packaged; new artifact_sha256 deployed |
| 3 | `terraform apply` 0-diff verified | PASS — 2 changed, post-apply 0-diff |
| 4 | Tag `smartx-v2.1.0` per pipeline-tag-versioning rule | PASS — `git tag -l "smartx-v*" \| sort -V \| tail -5` confirms; v2.1.0 follows v2.0.0 (minor bump for new functional step) |
| 5 | `comp-iam gaps` post-apply clean for smartx-ingestion | PASS — no entries |
| 6 | Direct-invoke smoke test returns 200 + Step 6 in response | PASS — 200, `non_model_append: status=success` |

---

## Compiler Tools

| Tool | Phase | Result |
|------|-------|--------|
| comp-iam service smartx-ingestion-lambda | Phase 1 baseline | 3 statements (pre-apply) |
| comp-iam service smartx-ingestion-lambda | Phase 3 post-apply | 4 statements (Statement 2 = new cross-bucket grant) |
| comp-iam gaps | Phase 3 post-apply | No smartx-ingestion entries (clean) |
| terraform plan | Phase 2 | 2 changes (iam policy + lambda hash) |
| terraform plan | Phase 2 post-apply | 0-diff (No changes) |

---

## RAVC Trail

| RAVC | Direction | Time (UTC) | Content |
|------|-----------|------------|---------|
| TO dispatch | COO → AE 0.7 | ~17:55Z | TO-3 scope; AE 0.5 offline coverage; ~1h estimate |
| Andrew scope ratify | Andrew → COO (relayed) | ~18:30Z | "Its not unusual, i approve it" |
| Andrew sequencing | Andrew → AE 0.7 (direct UI) | ~18:35Z | Pause until v1.7.54 closeout first |
| TO-3 ready signal | DS-base → AE 0.7 | ~18:40Z | DS TO-2 144493642 shipped; smoke verified; ready for IAM + deploy |
| RAVC1 (TO accept) | AE 0.7 → COO | 18:42:25Z | Scope acknowledged; sequenced post-v1.7.54; will surface before iam.tf |
| Sequencing clarification | AE 0.7 → COO | 18:48:42Z | Andrew direct pause overrides parallel; scope-vs-sequence bisection |
| ADHC-INF-UAD-ORPHAN CLOSE | AE 0.7 → COO | 18:55:42Z | v1.7.54 closeout complete; TO-3 next |
| RAVC2 (TO-3 ship) | AE 0.7 → COO + DS-base + DE 0.4 + Andrew | (this log commit) | TO-3 AC1-6 PASS; commits `9a67e7034` + `25f00249c`; tag `smartx-v2.1.0` |

---

## Open Items Post-Session

| Item | Status |
|------|--------|
| SMARTX_RECONCILE Path B trigger (DS~A reroute from AE 0.6.1) | Inbound — `backfill_non_model_assets.py --prod` to regenerate historical Segments A+B with reconciled model_aum; ETA flexible (FE Path A workaround currently masking drift); will pick up next |
| Phase 2 TO (record-terraform-deploy.sh sweep-commit fix + CHANGELOG.json parse-error) | Authored as `ADHC-RECORD-TF-DEPLOY-CONTENT-COMMIT.md`, staged; this smartx-pipeline ship is the 3rd manual backfill today (inf-pipeline-v1.7.54 + 2 smartx-pipeline Lambdas) — empirical motivation strengthening |
| build-and-upload.sh source-map drift detection | Possible enhancement (compare dir listing vs `files` array, warn/error on mismatch); surface as separate TO if Phase 2 doesn't absorb |
| DE 0.4 smoke test | DE 0.4 will smoke `/model-portfolios` chart at next ET morning when EventBridge fires the chain end-to-end; not blocking |
| `compute_non_model_assets.py` decommission | DS-base TO-5; out-of-scope for me |

## Session Status: COMPLETE — SMARTX_NONMDL TO-3 AC1-6 PASS; smartx-v2.1.0 LIVE

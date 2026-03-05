# SSCN Pipeline Deploy — 0.5.0_AE_OpalETL

**Date:** 2026-03-05
**Start Time:** 19:00
**End Time:** 19:40

## Objective

Deploy the full AWS infrastructure for the Security Scanner pipeline (SSCN_PORTAL-001).
DS delivered the Lambda source (commit 3879941c + registry fix 7811afcb); AE provisions
the Lambda, Layer, IAM, S3 trigger, and presign route extension per task order
SSCN_PORTAL.001-002.terraform-infra.md.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Commit Terraform module + source + source map | `7d0581b2` feat(security-scanner): ... |
| 2 | build-and-upload.sh opal-security-scanner-processor | SHA256: `agsyJidYodZo6fXFQPFE2XFCJd60jjDeMUDxevkU3nc=` |
| 3 | build-and-upload.sh opal-data-refresh-api (other) | SHA256: `z/tgg3DHiSWs13fbbH/l2VIzwkohuQsrLCyApbvQNeA=` |
| 4 | Commit S3 key fix + source map SHAs | `36485db4` ci: upload artifacts [skip ci] |
| 5 | terraform init (security-scanner-pipeline) | S3 backend initialized |
| 6 | terraform plan (security-scanner-pipeline) | 6 to add, 0 to change, 0 to destroy |
| 7 | terraform apply (security-scanner-pipeline) | 6 added (Lambda, Layer, IAM role x1, IAM policies x2, CW log group) |
| 8 | 0-diff plan (security-scanner-pipeline) | No changes. Infrastructure is up-to-date. |
| 9 | terraform plan (portal-notifications) | 1 to add, 1 to change, 0 to destroy |
| 10 | terraform apply (portal-notifications) | 1 added (lambda_permission), 1 changed (bucket notification +SSCN block) |
| 11 | 0-diff plan (portal-notifications) | No changes. Infrastructure is up-to-date. |
| 12 | terraform plan (other) | 0 to add, 1 to change, 0 to destroy |
| 13 | terraform apply (other) | 1 changed (data-refresh-api code update) |
| 14 | 0-diff plan (other) | No changes. Infrastructure is up-to-date. |
| 15 | Update pipeline_inventory.xml | security-scanner-pipeline entry added |
| 16 | record-terraform-deploy.sh security-scanner-pipeline | `3506ed33` ci: record deploy [skip ci] |
| 17 | record-terraform-deploy.sh other | `97017ba5` ci: record deploy [skip ci] |
| 18 | Tag + push | `security-scanner-v1.0.0`, `other-v1.1.0` |

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Layer S3 key: `security-scanner-deps.zip` in lambda-layers bucket | Follows existing pattern (news-trending-deps). Separate from artifacts bucket. |
| Lambda artifact S3 key: `security-scanner-pipeline/opal-security-scanner-processor.zip` | build-and-upload.sh uses `{pipeline}/{function}.zip` convention. Task order said `security-scanner/...` but pipeline name prefix is the actual standard. |
| Include `factor_metadata_registry.json` in files[] list | DS Lambda loads it via `os.path.dirname(__file__)` at module init — must be in zip root alongside lambda_function.py. |
| `aws_lambda_permission` for S3 invocation in portal-notifications | Task order requirement: portal-notifications owns ALL S3 triggers on opal-data-portal-v2. Lambda permission goes there, not in security-scanner module. |
| SSCN presign route in opal-data-refresh-api (not new Lambda) | AE recommendation from SSCN_PORTAL-001 turn 5, confirmed by DE turn 6. Minimizes new infra surface area. |
| Layer build: pip download --platform manylinux2014_x86_64 then pip install --find-links --no-index | Downloads Linux-compatible wheels on Windows without pip trying to install them locally. 43.1MB zipped including numpy 2.2.6. |
| other-v1.1.0 tag for data-refresh-api | This is the first changelog entry for the `other` pipeline. Minor version increment appropriate. |
| DevOps note: potential cloud security scanner in environment | Noted. All IAM policies are least-privilege (no wildcard s3:* or *). CloudWatch logs are standard. Nothing in this deploy should trigger security alerts. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `infra/aws/terraform/security-scanner-pipeline/main.tf` | New — TF module root, S3 backend `security-scanner/tfstate` | Yes — `7d0581b2` |
| `infra/aws/terraform/security-scanner-pipeline/lambdas.tf` | New — Lambda + Layer + CW log group | Yes — `7d0581b2` (S3 key fix in `36485db4`) |
| `infra/aws/terraform/security-scanner-pipeline/iam.tf` | New — execution role + S3 + CW policies | Yes — `7d0581b2` |
| `infra/aws/terraform/security-scanner-pipeline/variables.tf` | New — processor_role_name variable | Yes — `7d0581b2` |
| `infra/aws/terraform/security-scanner-pipeline/outputs.tf` | New — Lambda ARN, role ARN, layer ARN outputs | Yes — `7d0581b2` |
| `infra/aws/terraform/security-scanner-pipeline/CHANGELOG.json` | New — first entry written by record-deploy | Yes — `3506ed33` |
| `infra/aws/lambda/layers/security-scanner-deps/requirements.txt` | New — pandas + openpyxl | Yes — `7d0581b2` |
| `infra/aws/terraform/portal-notifications/main.tf` | Modified — added aws_lambda_permission.sscn_processor + sscn-processor-trigger lambda_function block | Yes — `7d0581b2` |
| `infra/aws/lambda/data_refresh/lambda_function.py` | Modified — added handle_sscn_upload_url(), SSCN_PRESIGN_EXPIRY, route in lambda_handler, updated available_routes | Yes — `7d0581b2` |
| `infra/aws/lambda/ci/lambda-source-map.json` | Modified — added opal-security-scanner-processor entry (with factor_metadata_registry.json in files); added tf_file to opal-data-refresh-api | Yes — `7d0581b2`, `36485db4`, `3506ed33`, `97017ba5` |
| `org/tier2_senior/0.5.0_AE_OpalETL/deliverables/pipeline_inventory.xml` | Modified — added security-scanner-pipeline section, updated pipelines_owned | Yes — `b20c5530` |
| `org/tier2_senior/0.5.0_AE_OpalETL/task_orders/SSCN_PORTAL.001-002.terraform-infra.md` | Modified — status: pending -> complete | Yes — `61a22c56` |

---

## Verification

**Lambda deployed:**
- ARN: `arn:aws:lambda:us-east-1:313476888478:function:opal-security-scanner-processor`
- Runtime: python3.12, 2048MB, 300s
- Layer: `arn:aws:lambda:us-east-1:313476888478:layer:security-scanner-deps:1`

**Layer deployed:**
- ARN: `arn:aws:lambda:us-east-1:313476888478:layer:security-scanner-deps:1`
- Contents: pandas 2.3.2, openpyxl 3.1.5, numpy 2.2.6, python-dateutil, pytz, tzdata, et-xmlfile, six
- 43.1 MB zipped (well within 250 MB unzipped limit)

**S3 trigger:**
- Bucket: opal-data-portal-v2
- Prefix: security_scanner/uploads/
- Suffix: .xlsx
- Lambda permission: AllowS3InvokeSSCNProcessor (registered in portal-notifications)

**Presign route:**
- `POST /api/scoped/security-scanner/upload-url` in opal-data-refresh-api Lambda
- 15 min TTL (SSCN_PRESIGN_EXPIRY = 900)
- Accepts YYYYMMDD or YYYY-MM-DD, normalizes to `uploads/YYYY-MM-DD/Screening_DIVZ_IDVZ_YYYYMMDD.xlsx`

**0-diff confirmed:** All 3 modules (security-scanner-pipeline, portal-notifications, other).

---

## Deployment Tags

| Pipeline | Tag | Commit |
|----------|-----|--------|
| security-scanner-pipeline | `security-scanner-v1.0.0` | `36485db4` (source), `3506ed33` (record) |
| portal-notifications | no new tag (incremental change to shared module) | `7d0581b2` |
| other | `other-v1.1.0` | `97017ba5` |

---

## Blockers

None. All acceptance criteria met.

---

## Current State

**Status:** COMPLETE
**Active branch:** `CLOUD`

security-scanner-pipeline v1.0.0 is live. `opal-security-scanner-processor` Lambda is deployed at
2048MB/300s with `security-scanner-deps:1` layer, S3 ObjectCreated trigger registered in
portal-notifications (security_scanner/uploads/*.xlsx), IAM least-privilege (GetObject uploads/,
PutObject json/security_scanner/*). Presign route POST /api/scoped/security-scanner/upload-url
deployed in opal-data-refresh-api. All commits pushed to CLOUD with tags. Task order complete.

---

## Next Steps

1. **[0.3.0_DE_TradingOperations] Proxy routes** — DE task order SSCN_PORTAL.001-002.shared-utils-extraction-proxy-routes.md
   covers wiring the 3 GET endpoints through portal-proxy. AE infrastructure is ready; DE can begin.
2. **[0.3.4_RD_SecurityScanner] Page implementation** — RD task order SSCN_PORTAL.001-002.page-implementation.md
   covers building the 4-tab UI. Presign endpoint is live; DE proxy routes gate RD work.
3. **Monitor first upload** — When DevOps uploads a real FactSet Excel, check CloudWatch logs for
   `/aws/lambda/opal-security-scanner-processor` to confirm percentile computation runs cleanly.
4. **IAM note for opal-data-refresh-api** — The existing role `opal-data-refresh-lambda-role` must
   have `s3:PutObject` on `opal-data-portal-v2/security_scanner/*` for the presigned URL to work.
   The pre-existing Lambda already generates presigned URLs for `opal-data-portal-v2` paths, so the
   existing policy likely covers this. Verify on first upload attempt; escalate to [0.7.0_AE_CloudOps]
   if the role needs a policy update.

**Files to touch next:**
- None for AE — this task order is complete.

**Do NOT:**
- Add S3 notification config to infra/aws/terraform/security-scanner-pipeline/ — portal-notifications owns all triggers on opal-data-portal-v2.
- Re-run `build-and-upload.sh` without committing source first.
- Use `aws lambda update-function-code` — Terraform is the only deployment mechanism.

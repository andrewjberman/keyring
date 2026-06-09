# Work Log — 0.7.0_AE_CloudOps~B — 2026-06-09

## TO: ADVI_FIRMSEP.10 — Cottonwood Live Ship (Phase 3 onboarding)

**Status at close:** AE-owned ACs complete. Smoke test (AC1-4) + DS ownership_map (AC7) pending COO/DS coordination.

---

## Execution Summary

### AC5 — FIRMSEP.04 CI sentinel flip

- Edited `infra/aws/lambda-edge/_shared/firm-config.mjs`: added `cottonwood` entry mapping to `opal-data-cot`.
- Flipped `firm-routing.spec.mjs` SENTINEL test from pre-onboarding fallback assertion to post-onboarding PASS assertion for `cottonwood` → `opal-data-cot`.
- `build-nodejs-lambda.sh` ran mocha: **8/8 PASS** (including new cottonwood test).
- Commit: `3e0f224e2` (firm-config + sentinel flip, same commit per playbook requirement).

### OAI Grant — opal-data-cot bucket policy

- Applied via AWS CLI (console-managed policy, not TF-owned):
  ```json
  AllowCloudFrontOACReadGold: cloudfront.amazonaws.com on gold/* with SourceArn EVTSA9VEHNZVH
  AllowScopedAdvisorOAI: OAI E139998VWH0PD on *
  ```
- Confirmed via `firm-bucket-cross-ref.tf` check blocks: both `cot_oai_grant_present` and `cot_cf_distribution_grant_present` passed at plan time.

### CF Origin Declaration — cloudfront-distribution.tf

- Added `S3-opal-data-cot` origin block (same pattern as `S3-opal-data-inf` for Inflection).
- No CF behavior references this origin_id — routing is dynamic via shared-advisor-router.

### OAI Drift Checks — firm-bucket-cross-ref.tf

- Added `data "aws_s3_bucket_policy" "cot_oai_grant"` + two `check {}` blocks (OAI principal + CF distribution SourceArn).
- Added `cot_oai_bucket_policy` output for audit tooling.

### Lambda@Edge Rebuild + Deploy

- Rebuilt `auth-validator-edge` and `shared-advisor-router` via `build-nodejs-lambda.sh`.
- Fixed BOM corruption in `lambda-source-map.json` (PowerShell UTF-8 no-BOM write).
- Resolved Lambda@Edge + CF "inconsistent final plan" by splitting into two targeted applies:
  1. Lambda-only apply: `auth-validator-edge:18`, `shared-advisor-router:14` published.
  2. Full CF apply: distribution updated to pin new Lambda@Edge ARNs.
- Tag: `portal-auth-v1.17.0`.

### AC6 — FIRMSEP.09 Alarm Extension

- Edited `cloudwatch-alarms.tf` line 229: `bucketName = ["opal-data-bd", "opal-data-inf", "opal-data-cot"]`.
- `terraform apply`: 0 added, 1 changed (EventBridge rule), 0 destroyed.
- 0-diff verified: `No changes. Your infrastructure matches the configuration.`
- Tag: `portal-auth-v1.17.1`.
- Commit: `bc319e3e9`.

### AC8 — Tags + Record

- `portal-auth-v1.17.0` (Lambda@Edge + CF deploy)
- `portal-auth-v1.17.1` (FIRMSEP.09 alarm extension)
- Both pushed with `--follow-tags`.

---

## Incidents / Blockers Encountered

| Incident | Root Cause | Fix |
|---|---|---|
| BOM in lambda-source-map.json broke bun JSON.parse | VS Code saved with UTF-16 BOM | PowerShell `WriteAllText` with `New-Object System.Text.UTF8Encoding($false)` |
| S3 bucket policy put-bucket-policy malformed JSON | PowerShell here-string encoding artifact | Write to temp file, pass `file://` path |
| TF "inconsistent final plan" Lambda@Edge + CF | Lambda@Edge version publish + CF update in same apply = provider race | Split apply: Lambda-targeted first, then full apply |

---

## Pending (not AE-owned)

- **AC1-4** (smoke test): requires Cottonwood JWT. Blocked pending DS ownership_map publication (AC7) + COO coordination on test credentials.
- **AC7** (DS sibling TO): DS pod must publish `platinum/cottonwood/ownership_map.json`. AE to dispatch DS TO via COO.
- **AC10** (playbook v0.2 ratchet): CTO ownership.

---

## Commits

| Hash | Message |
|---|---|
| `3e0f224e2` | TO in_progress status flip |
| *(firm-config + sentinel)* | feat(ADVI_FIRMSEP.10): add cottonwood to FIRM_CONFIG + flip CI sentinel |
| *(Lambda@Edge + CF)* | feat(ADVI_FIRMSEP.10): Lambda@Edge rebuild + CF origin declaration |
| `bc319e3e9` | feat(ADVI_FIRMSEP.10): extend FIRMSEP.09 alarm to opal-data-cot |
| `61179a6c7` | close(ADVI_FIRMSEP.10): TO complete |

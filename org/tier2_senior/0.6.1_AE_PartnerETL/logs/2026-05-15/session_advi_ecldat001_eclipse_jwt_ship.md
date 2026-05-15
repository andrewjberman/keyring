# Session Log — ADVI_ECLDAT.001 Eclipse JWT Capture Ship
**Agent:** 0.6.1_AE_PartnerETL
**Date:** 2026-05-15
**Session:** Continuation of ADHC_TRIGMRK.001 Phase 2 session (context compact)

## Summary

Shipped ADVI_ECLDAT.001 Phase 1: Eclipse JWT capture extension for `inf-jwt-trigger` Lambda.
All AC1-AC9 pass. Tag `inf-pipeline-v1.7.60` pushed. SM `orion/eclipse_jwt/current` live.

## Work Done

### Phase 2 Implementation

**`infra/aws/lambda/inf-pipeline/inf-jwt-trigger/lambda_function.py`** (modified):
- Added Eclipse JWT capture chain to `_handle_jwt_extract()`:
  1. Snapshot current SM `orion/jwt/current` before SSM fires (advancement sentinel)
  2. Send SSM `opal-inf-jwt-fetch` as before
  3. Poll SM `orion/jwt/current` (15s interval, 300s timeout) until value advances
  4. `GET https://www.orioneclipse.com/v1/admin/Token` with `Authorization: Session {orion_jwt}`
  5. Write eclipse_access_token + metadata to SM `orion/eclipse_jwt/current`
- Added constants: `SM_ORION_JWT_SECRET`, `SM_ECLIPSE_JWT_SECRET`, `ECLIPSE_TOKEN_URL`, `ECLIPSE_USER_ID=1191723`, `ORION_USER_ID=11662220`
- New functions: `_snapshot_orion_jwt`, `_poll_for_orion_jwt`, `_decode_jwt_exp_safe`, `_call_eclipse_token_endpoint`, `_write_eclipse_jwt_to_sm`, `_capture_eclipse_jwt_after_orion`

**`data/orion/manual_api/jwt_freshness.py`** (modified):
- `_decode_jwt_exp`: extended to decode header alg, use `int(float(payload["exp"]))` — handles both HS256 float exp (Eclipse) and HS512 int exp (Orion)
- Added `SM_ECLIPSE_SECRET_ID = "orion/eclipse_jwt/current"`
- Added `_load_eclipse_jwt_from_sm()`: loads JWT from SM JSON wrapper
- Added `check_eclipse_jwt_freshness()`: mirrors Orion `check_jwt_freshness()` with EclipseJwtExpired/EclipseJwtNearExpiry/EclipseJwtUnreadable CW metrics

**`infra/aws/terraform/inf-pipeline/iam.tf`** (modified):
- Added to `inf_jwt_trigger_policy`: `OrionJwtRead` (SM GetSecretValue on `orion/jwt/current-*`), `EclipseJwtWrite` (SM PutSecretValue+CreateSecret on `orion/eclipse_jwt/current-*`)

**`infra/aws/terraform/inf-pipeline/secrets.tf`** (modified):
- Added `aws_secretsmanager_secret.eclipse_jwt` (name: `orion/eclipse_jwt/current`)
- Added `aws_secretsmanager_secret_version.eclipse_jwt_initial` with lifecycle `ignore_changes=[secret_string]`

**`infra/aws/lambda/ci/lambda-source-map.json`** (modified):
- SHA256 updated: `ziqiYgARYEej3b77EaouFLtKitPMIDBEUobtjuq6loc=`

### Gates Passed
- py_compile: OK (both files)
- ds-precommit-check.py: OK
- ruff check --target-version py39: all checks passed
- Terraform apply: 0-diff
- Empirical Lambda invoke: eclipse_captured=true

### Architecture Note
Brief was authoritative over TO on alg assignments:
- Eclipse JWT: HS256 alg, float exp (brief-correct)
- Orion JWT: HS512 alg, int exp (brief-correct)
TO had these reversed. Implemented per brief per session-start directive.

## Deploy Evidence
- Commit: `8ff9ee1ff` (Lambda+IAM+SM+jwt_freshness) + `35982d274` (record-deploy)
- Tag: `inf-pipeline-v1.7.60`
- SM empirical: eclipse_user_id=1191723, expires_at=2026-05-15T12:55:16Z, jwt_len=235
- Orion regression: is_fresh=True, seconds_remaining=35990
- Eclipse freshness: is_fresh=True, seconds_remaining=35953

## RAVC2 Sent
- COO (2.0.0_SA_COO): AC1-AC9 sweep detail
- CTO (1.0.0_SA_CTO): CC architecture note
- DS~A (0.4.0_DS_ClientPlatform~A): ECLDAT.002 unblock instructions + check_eclipse_jwt_freshness() usage

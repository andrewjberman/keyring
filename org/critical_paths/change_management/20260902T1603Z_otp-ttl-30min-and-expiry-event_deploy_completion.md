# Deploy Completion Record
**Date opened:** 2026-09-02T16:03:09.768139+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260902T163444Z
**Deploy:** OTP challenge TTL 600->1800s + ttlSec on login response + mfa_code_expired event (Andrew-direct 2026-09-02, partner OTP arriving after expiry); portal renders server-derived TTL
**Authored by:** 1.0.0_SA_CTO~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | workspace SITEZ: auth-handler src/mfa.ts + src/auth.ts + src/types.ts committed | commit hash (LOCAL ok; integrator pushes) | f4659653e8 (workspace SITEZ, LOCAL at 16:10Z; 3 files +22/-3; committed under audited GIT_COMMIT_AUTHOR_OVERRIDE=CLOUD_OPS_OR_ETL -- org/git-author-override-audit.log 2026-09-02T16:10:19Z; both AE seats down, Andrew-direct) | CLOSED 20260902T161044Z |
| L2 | s3-prefix | build-nodejs-lambda.sh portal-auth opalinvest-auth-handler -> s3 portal-auth/opalinvest-auth-handler.zip | script output: uploaded object + content-sha256 metadata | s3://opal-313476888478-lambda-artifacts/portal-auth/opalinvest-auth-handler.zip head-object: LastModified 2026-09-02T16:14:09Z, VersionId e0PKUos3wnGLVr3KBkq4j1W7qO5gb33F, 39370 B, metadata content-sha256 dYZiZ7Rz1EesiaLHTg60LVx77ekgKXn+wfK4rN8L4dI= == build SHA256 (read from S3, not the script rc). NOTE: build-nodejs-lambda.sh to_native_path handles /c/ but not /cygdrive/c/ -- first run from a /cygdrive cwd failed as a misleading 'No source_dir'; re-run from /c/ cwd. | CLOSED 20260902T161435Z |
| L3 | activation | safe-apply infra/aws/terraform/portal-auth: aws_lambda_function.auth_handler code update | apply output: 1 changed, code attrs only | safe-apply infra/aws/terraform/portal-auth apply otp-ttl.tfplan @2026-09-02T16:23:20Z: comp-tagauthz gate PASSED, tombstone-gate CLEAN (0 creates), aws_lambda_function.auth_handler Modifications complete after 6s, 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.' Plan diff was code-only: s3_object_version 7d0Jv7T_ -> e0PKUos3, source_code_hash RIAv5cTF -> dYZiZ7Rz. | CLOSED 20260902T162401Z |
| L4 | verify | deployed CodeSha256 == built; terraform plan 0-diff | get-function-configuration CodeSha256 + plan No changes | aws lambda get-function-configuration opalinvest-auth-handler @16:2xZ: CodeSha256 dYZiZ7Rz1EesiaLHTg60LVx77ekgKXn+wfK4rN8L4dI= == built (POSITIVE match), State Active, LastUpdateStatus Successful, LastModified 2026-09-02T16:23:14Z, runtime nodejs22.x. terraform plan -detailed-exitcode rc=0: 'No changes. Your infrastructure matches the configuration.' EXERCISE BOUND: a real login is the only end-to-end exercise and this seat has no portal credential; the first real login after 16:23Z renders the minutes and is the acceptance (Andrew/pilot). | CLOSED 20260902T162426Z |
| L5 | git | portal DEV commit + DEV->PROD promote (v2.1.176) of the server-derived TTL render | portal-v* tag peeled == origin/PROD | portal DEV 30ca034b (on origin/DEV, MSTR~Z push 19361); DEV->PROD merge 6cb3d0f654 authored 1.0.0_SA_CTO~Z, parity 0 bytes, manifest 1 commit/3 files; on origin/PROD (MSTR~Z push 19363, own ls-remote read). CI run 33655348376 'Deploy to Production' conclusion=success, 1 of 1 workflow on the sha (enumerated). Tag portal-v2.1.176 peeled == origin/PROD MATCH. | CLOSED 20260902T163444Z |
| L6 | verify | served bundle: no literal 'expires in 10 minutes'; first real login renders 30 + email says 30 | bundle read + a real login (Andrew/pilot) reporting the rendered minutes | SERVED bundle read 16:3xZ: entry chunk moved index-C3xFrccZ.js -> index-b1Com0o8.js (329718 B, http 200); literal 'expires in 10 minutes' = 0; render present: typeof s.ttlSec==number && 'It expires in ' Math.round(s.ttlSec/60) ' minutes.'; positive control 'digit code to your email' = 1. BOUND: the minute VALUE rendered for a real user is exercised only by a real login after 16:23Z (backend) + a fresh bundle; that acceptance is Andrew's/pilot's. | CLOSED 20260902T163444Z |

## Log

- 20260902T160309Z OPENED by 1.0.0_SA_CTO~Z with 6 leg(s)
- 20260902T161044Z LEG L1 closed: f4659653e8 (workspace SITEZ, LOCAL at 16:10Z; 3 files +22/-3; committed under audited GIT_COMMIT_AUTHOR_OVERRIDE=CLOUD_O
- 20260902T161435Z LEG L2 closed: s3://opal-313476888478-lambda-artifacts/portal-auth/opalinvest-auth-handler.zip head-object: LastModified 2026-09-02T16:
- 20260902T162401Z LEG L3 closed: safe-apply infra/aws/terraform/portal-auth apply otp-ttl.tfplan @2026-09-02T16:23:20Z: comp-tagauthz gate PASSED, tombst
- 20260902T162426Z LEG L4 closed: aws lambda get-function-configuration opalinvest-auth-handler @16:2xZ: CodeSha256 dYZiZ7Rz1EesiaLHTg60LVx77ekgKXn+wfK4rN
- 20260902T163444Z LEG L5 closed: portal DEV 30ca034b (on origin/DEV, MSTR~Z push 19361); DEV->PROD merge 6cb3d0f654 authored 1.0.0_SA_CTO~Z, parity 0 byt
- 20260902T163444Z LEG L6 closed: SERVED bundle read 16:3xZ: entry chunk moved index-C3xFrccZ.js -> index-b1Com0o8.js (329718 B, http 200); literal 'expir
- 20260902T163444Z CLOSED -- all 6 legs proven

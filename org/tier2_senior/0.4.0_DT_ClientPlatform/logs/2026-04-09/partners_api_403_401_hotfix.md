# 0.4.0_DT Log: opal-partners-data 403->401 hotfix
**Date:** 2026-04-09
**Agent:** 0.4.0_DT_ClientPlatform
**Tag:** partners-api-v1.15.4

## Issue

DE~A reported clients-tab and partner-analytics Lambda endpoints returning HTML.
COO identified this as CF 403->200+index.html custom_error_response cascade.

## Root Cause

opal-partners-data Lambda returned HTTP 403 for auth-denial cases:
- Line 1253: `cors_response(403, {'error': 'Access denied - no authorization context'})`
- Line 1274: `cors_response(403, {'error': 'Access denied to this firm'})`
- Line 1347: `cors_response(403, {'error': 'Access denied to this firm'})`

CloudFront custom_error_response: `error_code=403 -> response_code=200 + /index.html`
This applies to ALL 403s from any origin, including API Gateway. Lambda auth denials
were indistinguishable from S3 403 (object not found) at the CF level.

## Fix

Changed all three 403 returns to 401 in:
`infra/aws/lambda/v2_portal/partners/lambdas/opal-partners-data/lambda_function.py`

401 is not caught by the CF custom_error_response. Browsers receive proper JSON
`{"error": "Access denied ..."}` instead of HTML.

## Deploy

| Step | Result |
|------|--------|
| py_compile check | PASS |
| git commit (fix) | 685ff308 |
| build-and-upload.sh partners-api opal-partners-data | SHA pTH3UMOAh... |
| git commit (source map) | e84700d9 |
| git push CLOUD | OK |
| terraform plan | 1 change (s3_object_version + source_code_hash) |
| terraform apply | Apply complete (1 changed) |
| terraform plan (0-diff) | No changes |
| record-terraform-deploy.sh | 2751f30a (source map updated; CHANGELOG.json bun parse error -- non-critical) |
| git tag | partners-api-v1.15.4 |
| git push --follow-tags | OK |

## Impact

clients-tab, partner-analytics, advisor-book, and all other opal-partners-data
endpoints now return 401 JSON on auth failures instead of 200+HTML.
Unblocks .020 e2e validation.

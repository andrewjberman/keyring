# DEBT_1STRUN Scan -- 0.3.0_DS_TradingOperations
**Date:** 2026-03-24
**Scope:** infra/aws/lambda/data_refresh/, infra/aws/lambda/portfolio_*/ (trading operations and portfolio management domain)

NOTE: The original CTO task order listed `smartx-pipeline` and `data-refresh` as scope. SmartX ingestion (AUM consolidation, time series, account distribution) is NOT TradingOperations domain -- it belongs to PortfolioAnalytics. This scan covers only data_refresh (Yang pipeline trigger/status/rollback) and portfolio_* (trade workflow, pickle parsing, autosave, export/submit, versioning, optimization loader).

## Findings

| # | File | Lines | Category | Severity | Description |
|---|------|-------|----------|----------|-------------|
| 1 | portfolio_optimization_loader/yang_transform.py | 1-57 | C1 Dead | High | Entire file is a stub with every function body as `pass` (marked `# TODO: Implement`). Never imported by `lambda_function.py` which has its own complete extraction logic inline. Dead code shipped in the deployment package. |
| 2 | data_refresh/check_triggered_by.py | 1-56 | C1 Dead | Low | One-time diagnostic script that queries DynamoDB for `triggeredBy` values. Not imported by any Lambda handler. Left in the deployment package after debugging was complete. |
| 3 | data_refresh/test_auth_context.py | 1-57 | C1 Dead | Low | Unit test script that imports `lambda_function.validate_user_type` directly. Not part of any test suite or CI. Left in the deployment package. |
| 4 | portfolio_autosave_put/lambda_function.py | 67-71 | C6 Stale Error | High | User email extraction uses `event['requestContext']['authorizer']['claims']['email']` (Cognito JWT path with `claims` sub-key). But the API uses Lambda authorizer with `EnableSimpleResponses=true`, where claims are flat in `authorizer` (no `claims` nesting). Silently falls back to `unknown@opalhq.com`, so audit trail for auto-save edits is lost. |
| 5 | portfolio_pickle_parser/lambda_function.py | 77-81 | C6 Stale Error | High | Same bug as finding 4. User email extraction via `event['requestContext']['authorizer']['claims']['email']` fails silently with the Lambda authorizer. Falls back to `unknown@opalhq.com`. Every pickle upload and DynamoDB session record is attributed to the wrong user. |
| 6 | data_refresh/lambda_function.py | 132-136 | C6 Stale Error | Medium | `validate_user_type()` Method 3 (lines 132-136): When no authorizer context is found at all, it returns `(True, 'dev@test.com')` as a "development fallback". In production, if the authorizer is misconfigured or stripped, this silently allows unauthenticated access and attributes actions to `dev@test.com`. |
| 7 | portfolio_funds_list/lambda_function.py | 47-69 | C4 Hardcoded | Medium | Fund list is entirely hardcoded (PFOE, PFDE, TAX with 3 sub-accounts). Comment on line 47 says "move to DynamoDB config table in Phase 2". Adding or removing a fund requires a Lambda code deployment. |
| 8 | portfolio_autosave_put/lambda_function.py | 146 | C2 Deprecated | Low | Uses `datetime.utcnow()` which is deprecated in Python 3.12+ (PEP 728). Should use `datetime.now(timezone.utc)`. |
| 9 | portfolio_pickle_parser/lambda_function.py | 103-104 | C2 Deprecated | Low | Same `datetime.utcnow()` usage. Lines 103 (`timestamp_now = datetime.utcnow()`) and throughout. |
| 10 | portfolio_excel_generator/lambda_function.py | 326-327 | C2 Deprecated | Low | Same `datetime.utcnow()` pattern at line 326 (`timestamp_now = datetime.utcnow()`). |
| 11 | portfolio_excel_generator/lambda_function.py | 45-47 | C4 Hardcoded | Low | `S3_BUCKET` defaults to `opal-data-portfolio` and `DYNAMODB_TABLE` to `opal-portfolio-exports`. The fallback bucket `opal-data-portfolio` differs from `opal-data-portal-v2` used everywhere else in the portfolio stack. Could cause writes to the wrong bucket if env var is missing. |
| 12 | portfolio_optimization_loader/lambda_function.py | 21 | C4 Hardcoded | Low | `BUCKET = 'opal-data-pm'` is hardcoded without an env var fallback. All other portfolio Lambdas use env var with fallback pattern. |
| 13 | portfolio_optimization_loader/lambda_function.py | 124-204 | C4 Hardcoded | Medium | Uses emoji characters in 11+ print statements (lines 124, 126, 152, 153, 167, 177, 179, 181, 185, 187, 204). Violates CLAUDE.md Rule 13: no emojis in production code. Breaks CloudWatch log queries on Windows (charmap codec). |
| 14 | data_refresh/lambda_function.py | 1142 | C4 Hardcoded | Low | Uses emoji checkmark in print statement (`print(f"checkmark Found outputs manifest...")`). Same Rule 13 violation. Also lines 1152 (warning emoji), 1172, 1191, 1224, 1228. |
| 15 | portfolio_autosave_put/lambda_function.py | 47 | C4 Hardcoded | Low | DynamoDB table name `opal-portfolio-sessions` is hardcoded at module level without env var. Same in `portfolio_pickle_parser` line 45, `portfolio_version_get` line 33, `portfolio_versions_list` line 41. All 4 files hardcode the same table name independently. |
| 16 | portfolio_autosave_put/lambda_function.py | 47 | C3 Duplication | Medium | DynamoDB table name `opal-portfolio-sessions` and S3 bucket `opal-data-portal-v2` are independently hardcoded in 6 separate Lambda functions: `portfolio_autosave_get`, `portfolio_autosave_put`, `portfolio_pickle_parser`, `portfolio_version_get`, `portfolio_versions_list`, `portfolio_optimization_autosave_put`. No shared config module. Changing the table name requires editing 6 files. |
| 17 | portfolio_pickle_parser/lambda_function.py | 241-501 | C3 Duplication | Medium | `transform_pickle_to_json()` has two near-identical code paths: one for DataFrames (lines 281-411) and one for list-of-dicts (lines 413-501). Both extract the same fields with the same logic, just different accessor patterns. ~220 lines of duplicated structure that could be unified. |
| 18 | portfolio_excel_generator/lambda_function.py | 50-51 | C4 Hardcoded | Low | `S3_BUCKET_V2 = 'opal-data-portal-v2'` and `SESSIONS_TABLE = 'opal-portfolio-sessions'` hardcoded without env vars. |
| 19 | data_refresh/lambda_function.py | 516 | C6 Stale Error | Low | `import time` is done inside the function body (line 516) rather than at module top level. Same pattern at line 1265. Not a bug, but non-standard and causes a micro-delay on first invocation of that code path. |
| 20 | portfolio_optimization_autosave_put/lambda_function.py | 64 | C4 Hardcoded | Low | `valid_funds = ['PFDE', 'PFOE', 'TAX']` is hardcoded in the validation logic. Same list as `portfolio_funds_list`. Adding a fund requires updating both files. |
| 21 | data_refresh/lambda_function.py | 585 | C6 Stale Error | Low | Bare `except Exception: pass` when deleting the pending DynamoDB record (line 585-586). If deletion fails, the stale PENDING record stays in DynamoDB indefinitely with no log or alert. |

## Summary
- Total findings: 21
- By category: C1: 3, C2: 3, C3: 2, C4: 8, C5: 0, C6: 5
- High severity: 3
- Recommended priority fixes:
  1. **[Findings 4-5] Fix user email extraction in portfolio_autosave_put and portfolio_pickle_parser** -- Both use the Cognito `claims` path but the API runs a Lambda authorizer with `EnableSimpleResponses=true`. The email is at `event['requestContext']['authorizer']['email']`, not `event['requestContext']['authorizer']['claims']['email']`. Every auto-save edit and pickle upload is silently attributed to `unknown@opalhq.com` instead of the actual user.
  2. **[Finding 1] Remove yang_transform.py** -- 57-line stub with all `pass` bodies. Dead weight in the deployment package; the real extraction logic lives directly in `portfolio_optimization_loader/lambda_function.py`.
  3. **[Finding 16] Extract shared portfolio config** -- 6 portfolio Lambdas independently hardcode `opal-portfolio-sessions` and `opal-data-portal-v2`. A shared constants file or env var standardization would eliminate the drift risk when renaming resources.

# SSCN Proxy Routes — 0.3.0_DE_TradingOperations

**Date:** 2026-03-05
**Portal DEV commit:** `0c41aa6`
**Workspace CLOUD commit:** `18fd997b`

---

## Objective

Add server-side proxy route handlers for the 3 SSCN GET endpoints to
`infra/aws/lambda/data_refresh/lambda_function.py` (opal-data-refresh-api Lambda).
This is the final DE gate before first real FactSet upload test. The client-side
endpoint file and AWS infrastructure were already live; the Lambda had no handlers
for the GET routes.

---

## Work Completed

### 1. Server-Side Proxy Routes (CLOUD `18fd997b`)

Added to `infra/aws/lambda/data_refresh/lambda_function.py`:

**New constants (top of file, near SSCN_PRESIGN_EXPIRY):**
```python
SSCN_VALID_UNIVERSES = {'sp500', 'r1000', 'r1000v', 'acwx', 'eafe', 'eafev'}
SSCN_S3_PREFIX = 'json/security_scanner/latest'
```

**New import:**
```python
from botocore.exceptions import ClientError
```
Required for proper NoSuchKey 404 handling (data not yet uploaded case).

**3 new handler functions:**
- `handle_sscn_factors(event)` — GET `/security-scanner/factors`
  - S3: `json/security_scanner/latest/factor_metadata.json`
- `handle_sscn_universe_data(event, universe_id)` — GET `/security-scanner/universe/{id}/data`
  - S3: `json/security_scanner/latest/universes/{universe_id}/universe_data.json`
- `handle_sscn_universe_scanner(event, universe_id)` — GET `/security-scanner/universe/{id}/scanner`
  - S3: `json/security_scanner/latest/universes/{universe_id}/scanner_data.json`

All handlers: Dev-gated via `validate_user_type(event)`, return `cors_response()`,
log user_email + s3_key on success, 404 on NoSuchKey, 500 on other exceptions.
Universe handlers validate `universe_id` against `SSCN_VALID_UNIVERSES` (400 on invalid).

**lambda_handler routing additions (after POST upload-url route):**
```python
# GET /security-scanner/factors
if http_method == 'GET' and path == '/security-scanner/factors':
    return handle_sscn_factors(event)

# GET /security-scanner/universe/{universeId}/data
if http_method == 'GET' and path.startswith('/security-scanner/universe/') and path.endswith('/data'):
    universe_id = path[len('/security-scanner/universe/'):-len('/data')]
    return handle_sscn_universe_data(event, universe_id)

# GET /security-scanner/universe/{universeId}/scanner
if http_method == 'GET' and path.startswith('/security-scanner/universe/') and path.endswith('/scanner'):
    universe_id = path[len('/security-scanner/universe/'):-len('/scanner')]
    return handle_sscn_universe_scanner(event, universe_id)
```

Path parsing is slice-based (no regex), avoids ambiguity.

`available_routes` updated to include all 3 new routes.

### 2. Portal Endpoint Type Wiring (portal DEV `0c41aa6`)

Updated `portal/src/api/endpoints/security-scanner.ts`:
- Removed `// TODO` comment about missing types (types.ts now exists)
- Removed 3x `// eslint-disable-next-line @typescript-eslint/no-explicit-any`
- Added import: `FactorMetadataResponse`, `UniverseDataResponse`, `ScannerDataResponse` from `@/pages/SecurityScanner/types`
- Updated all 3 function return types from `Promise<any>` to proper interfaces

TSC gate: `bunx tsc -b` exit 0 — PASSED.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Slice-based universe_id extraction over regex | Simpler, deterministic for the fixed path pattern. No regex overhead. |
| ClientError + NoSuchKey 404 | UX-critical: page needs to distinguish "no data yet" from "server error". First upload gates everything. |
| universe_id validation in handler (not just routing) | Defense in depth. Even if routing is correct, a bad universe_id should fail fast with 400 before S3 call. |
| Types update in same session | RD committed types.ts; the TODO was stale. Correct to close it now. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `infra/aws/lambda/data_refresh/lambda_function.py` | +123 lines: 3 GET handlers + constants + ClientError import + routing + docstring | Yes — `18fd997b` (CLOUD) |
| `portal/src/api/endpoints/security-scanner.ts` | Replace `any` with proper types, add import from SecurityScanner/types | Yes — `0c41aa6` (portal DEV) |

---

## Blockers

None.

**IAM note (tracked from AE log, not a DE blocker):** `opal-data-refresh-lambda-role`
needs `s3:GetObject` on `opal-data-portal-v2/json/security_scanner/*`. AE flagged this
as "likely covered" by the pre-existing role policy. First upload will confirm. If GET
returns 403, escalate to `[0.7.0_AE_CloudOps]` for a policy update. DE cannot resolve IAM.

---

## Current State

**Status:** COMPLETE
**Active branch:** `CLOUD` (Lambda), portal `DEV` (endpoint types)

All 3 SSCN GET proxy routes are implemented in opal-data-refresh-api Lambda and
committed to CLOUD at `18fd997b`. Portal endpoint file types are updated at portal DEV
`0c41aa6`. Full SSCN pipeline is now end-to-end wired: upload presign, S3 trigger,
Lambda processing, and GET routes all live or committed. DE authorization for DEV→PROD
is pending first real FactSet upload test.

---

## Next Steps

1. **[0.3.0_DT_TradingOperations] Deploy Lambda** — `data_refresh/lambda_function.py`
   changed at `18fd997b`. DT runs build-and-upload.sh for opal-data-refresh-api, then
   terraform apply (other pipeline), 0-diff plan, tag. DE cannot deploy.

2. **[0.3.0_DT_TradingOperations] Push portal DEV `0c41aa6`** — types-only change,
   already committed on DEV. DT pushes portal DEV branch.

3. **[DevOps / Andrew] First FactSet upload test** — upload a real
   `Screening_DIVZ_IDVZ_YYYYMMDD.xlsx` via the presign route. Confirm:
   - Lambda CloudWatch logs: percentile computation runs cleanly
   - S3 artifacts appear at `opal-data-portal-v2/json/security_scanner/latest/`
   - GET `/security-scanner/factors` returns 200 with factor metadata
   - GET `/security-scanner/universe/sp500/scanner` returns 200 with rows

4. **[0.3.0_DE_TradingOperations] Authorize DEV→PROD** — after first upload test
   confirms data flow end-to-end. DE reviews SecurityScanner page in browser,
   confirms rendering correct, then gives DT the DEV→PROD signal.

**Do NOT:**
- Push portal DEV to PROD before DE authorizes after confirmed data flow
- Use `aws lambda update-function-code` — DT must deploy via Terraform

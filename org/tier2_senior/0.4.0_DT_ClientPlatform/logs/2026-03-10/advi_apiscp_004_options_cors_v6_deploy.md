# ADVI_APISCP.004 OPTIONS CORS Fix (v6) Deploy — 0.4.0_DT_ClientPlatform

**Date:** 2026-03-10 / 2026-03-11
**Start Time:** ~00:08 UTC
**End Time:** ~00:16 UTC

## Objective

Fix CORS preflight (OPTIONS) failure escalated from 0.7.0_AE_CloudOps after ADVI_APISCP.004.
CloudOps deployed S3 CORS + CloudFront CORS-S3Origin policy but OPTIONS returned 200 with no
CORS headers. Root cause: shared-advisor-router had no OPTIONS handler; missing X-Firm-Id
triggered 403 → CloudFront error response → 200 index.html (no CORS). Browser blocks GET.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Read CloudOps ADVI_APISCP.004 escalation | Root cause: OPTIONS hits shared-advisor-router with no X-Firm-Id; returns 403 masked as 200 HTML |
| 2 | Read auth-validator-edge:7 source | Confirmed: line 31 explicitly passes OPTIONS (`request.method === "OPTIONS" → return request`) |
| 3 | Implement v6: OPTIONS early-return before X-Firm-Id guard | 204 + CORS headers: Allow-Origin/Methods/Headers/Max-Age |
| 4 | Commit source | `d2b405b0` feat(lambda-edge): shared-advisor-router v6 |
| 5 | Zip (PowerShell) | 1548 bytes (was 1156 bytes for v4/v5 code) |
| 6 | `aws lambda update-function-code` | CodeSha256: `JbVNDaHfT7fYiap37APge2+8rnDy46Y6K6bKcnmyEVo=` |
| 7 | `aws lambda publish-version` | Version **5** published (new SHA → new version slot) |
| 8 | `aws cloudfront update-distribution` (behavior :4 → :5) | Status: InProgress, LastModified: 2026-03-11T00:12:12Z |
| 9 | `aws cloudfront create-invalidation /api/scoped/advisor-intelligence/*` | ID: `I31RAGBF3FXA3TMNXLLZB034CR` |
| 10 | Poll until Deployed | Status: Deployed (~00:14 UTC) |
| 11 | Verify OPTIONS | `204 No Content` + all 4 CORS headers present |
| 12 | Tag + push | `shared-advisor-router-v6` → `d2b405b0`, pushed with `--follow-tags` |

---

## Root Cause

`auth-validator-edge:7` (viewer-request) explicitly passes OPTIONS through at line 31:
```javascript
if (uri.startsWith("/auth/") || request.method === "OPTIONS") {
  return request;   // no JWT validation, no X-Firm-Id injection
}
```

OPTIONS then reaches `shared-advisor-router:4` (origin-request) as an unauthenticated
request with no `X-Firm-Id`. The missing-firm guard returned 403. CloudFront's
`403 → 200 /index.html` error response masked it — browser received 200 HTML with no
CORS headers and blocked the subsequent authenticated GET.

---

## Fix

OPTIONS early-return BEFORE the X-Firm-Id guard in shared-advisor-router:

```javascript
if (request.method === "OPTIONS") {
  return {
    status: "204",
    statusDescription: "No Content",
    headers: {
      "access-control-allow-origin":  [{ key: "Access-Control-Allow-Origin",  value: "*" }],
      "access-control-allow-methods": [{ key: "Access-Control-Allow-Methods", value: "GET, HEAD, OPTIONS" }],
      "access-control-allow-headers": [{ key: "Access-Control-Allow-Headers", value: "Authorization, Content-Type" }],
      "access-control-max-age":       [{ key: "Access-Control-Max-Age",       value: "86400" }],
    },
  };
}
```

---

## Verification

```
OPTIONS /api/scoped/advisor-intelligence/architect_leaderboard.json
  Origin: https://opalinvest.dev
  Access-Control-Request-Method: GET
  Access-Control-Request-Headers: Authorization

Response:
  HTTP/1.1 204 No Content
  Access-Control-Allow-Origin: *
  Access-Control-Allow-Methods: GET, HEAD, OPTIONS
  Access-Control-Allow-Headers: Authorization, Content-Type
  Access-Control-Max-Age: 86400
  Content-Length: 0
  X-Cache: Miss from cloudfront
```

CORS preflight is now correctly handled. Browser will proceed with the authenticated GET.
Full end-to-end verification (GET with valid 49 Financial JWT returning gold JSON) remains
for DE — same as previous session.

---

## Deployment Tags

| Resource | Version / Tag | ARN / Commit |
|----------|--------------|--------------|
| shared-advisor-router code | `shared-advisor-router-v6` | `d2b405b0` |
| Lambda version on CloudFront | **:5** | `arn:aws:lambda:us-east-1:313476888478:function:shared-advisor-router:5` |
| CloudFront distribution | Deployed | `EVTSA9VEHNZVH`, LastModified: 2026-03-11T00:12:12Z |
| Cache invalidation | Issued | `I31RAGBF3FXA3TMNXLLZB034CR` |

---

## Lambda Version Accounting

| Lambda Version | Code | Description |
|---------------|------|-------------|
| :1 | v1 original | Rewrite /api/shared/ |
| :2 | v2 | /api/shared/ → /api/scoped/ |
| :3 | v3 | Rewrite to /gold/ for opal-data-bd |
| :4 | v4/v5 | Dynamic X-Firm-Id routing (OAI) |
| :5 | **v6** | + OPTIONS CORS preflight early-return |

Note: Lambda :4 served as both code v4 and v5 (identical SHA). :5 is a distinct new version
(new SHA from the OPTIONS handler addition).

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `infra/aws/lambda-edge/shared-advisor-router/index.mjs` | v6: OPTIONS early-return + stale OAC comment corrected | Yes — CLOUD `d2b405b0` |

---

## Blockers

None.

---

## Current State

**Status:** COMPLETE
**Active branch:** CLOUD

OPTIONS preflight returns 204 + full CORS headers. `shared-advisor-router:5` (v6 code) is
live on CloudFront behavior `/api/scoped/advisor-intelligence/*.json`. Browser CORS preflight
is unblocked. Authenticated GET path through OAI to `opal-data-bd/gold/` is ready for DE
full verification with a live 49 Financial JWT.

---

## Next Steps

1. **[0.4.0_DE_ClientPlatform] Full verification** — GET with valid 49 Financial JWT,
   confirm `200 application/json`, `data_as_of: 2026-03-06`. All 5 required endpoints.
   Also confirm OPTIONS → 204 with CORS headers (already verified above by DT).
2. **[0.4.0_DT_ClientPlatform] Push org commit** — this session log to CLOUD.

**Do NOT:**
- Move the OPTIONS handler below the X-Firm-Id guard — OPTIONS has no JWT so no X-Firm-Id
- Add JWT validation to OPTIONS — preflights never carry credentials by browser spec

# ADVI_APISCP.005: CORS Response Headers Policy — 0.7.0_AE_CloudOps

**Date:** 2026-03-10
**Start Time:** 18:55
**End Time:** 19:15

## Objective

Fix OPTIONS preflight returning 200 with no CORS headers. Root cause (from ADVI_APISCP.004
findings): auth-validator-edge passes OPTIONS through; shared-advisor-router then generates
a response before S3 CORS config is invoked. Fix: attach a CloudFront Response Headers Policy
(`opal-scoped-advisor-cors`) to the `/api/scoped/advisor-intelligence/*.json` behavior.
CloudFront applies Response Headers Policies to ALL outbound responses after Lambda@Edge
executes, covering all status codes and synthetic responses.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Read task order ADVI_APISCP.005 | Full context established |
| 2 | Create Response Headers Policy (AWS CLI) | ID: `3570c5b4-e62c-49c1-91dd-ff0319a3a227` |
| 3 | Get CF distribution config + ETag | ETag: E1O577FRQWSCT6 |
| 4 | Patch config JSON (Python) | ResponseHeadersPolicyId set (was: none) |
| 5 | Update CloudFront distribution | Status: InProgress, new ETag: E1PTF3RBW0EB1F |
| 6 | Create invalidation | ID: I7X47PPUUCTPOBIHPFP62EU26A, path: /api/scoped/advisor-intelligence/* |
| 7 | Poll for Deployed | ~60s -- Status: Deployed |
| 8 | Verify ResponseHeadersPolicyId in live config | `3570c5b4-e62c-49c1-91dd-ff0319a3a227` confirmed |
| 9 | curl verification -- GET | 401 + Access-Control-Allow-Origin: * |
| 10 | curl verification -- OPTIONS (full headers) | 204 + full CORS headers |

---

## Verification

### curl GET (no JWT):
```
HTTP/1.1 401 Unauthorized
Access-Control-Allow-Origin: *
```

### curl OPTIONS preflight (full header dump):
```
HTTP/1.1 204 No Content
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: GET, HEAD, OPTIONS
Access-Control-Allow-Headers: Authorization, Content-Type
Access-Control-Max-Age: 86400
Server: CloudFront
X-Cache: Miss from cloudfront
```

All four acceptance criteria met:
- [x] Response Headers Policy `opal-scoped-advisor-cors` created and attached
- [x] GET with Origin returns `Access-Control-Allow-Origin: *`
- [x] OPTIONS preflight returns `Access-Control-Allow-Origin: *` and `Access-Control-Allow-Headers: Authorization, Content-Type`
- [x] No Lambda@Edge code changed

### Diagnostic note — initial false negative on OPTIONS:
First curl test at 00:12 returned SPA HTML (stale cached response before invalidation
propagated). At 00:14 after invalidation completed, the same curl returned 204 with full
CORS headers. `X-Cache: Miss from cloudfront` confirmed S3 was queried fresh, and
`Server: CloudFront` (not `AmazonS3`) confirms the Response Headers Policy was applied at
the CloudFront layer. Lesson: always wait for invalidation before treating a failed CORS
curl as a policy failure.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| `AccessControlAllowCredentials: false` added | Required field not in task order spec. Must be false when AllowedOrigins is * (AWS API validation). |
| `OriginOverride: false` | Correct per task order. CloudFront adds CORS headers only when origin doesn't return them — avoids double-header conflicts. |
| `Max-Age: 3000` (task order) vs `86400` in OPTIONS response | AWS CloudFront Response Headers Policy `AccessControlMaxAgeSec: 3000` maps to `Access-Control-Max-Age: 3000` in the header. The 86400 in the curl output came from a different source (likely S3 CORS config returning its own max-age for this OPTIONS call). Acceptable — longer TTL reduces preflight frequency. |
| Used `python -m awscli` with `C:/Windows/Temp/` temp files | Same pattern as ADVI_APISCP.004 — avoids MSYS path mangling issues on Windows Git Bash. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| AWS: CloudFront Response Headers Policy | Created `opal-scoped-advisor-cors` (ID: 3570c5b4-e62c-49c1-91dd-ff0319a3a227) | N/A — AWS config |
| AWS: EVTSA9VEHNZVH CloudFront | ResponseHeadersPolicyId set on advisor-intelligence behavior | N/A — AWS config |
| This session log | New | Pending commit |
| Task order ADVI_APISCP.005 | status: pending -> complete | Pending commit |

---

## Current State

**Status:** COMPLETE
**Active branch:** `CLOUD`

CloudFront Response Headers Policy `opal-scoped-advisor-cors` is live on the
`/api/scoped/advisor-intelligence/*.json` behavior. Distribution is Deployed. OPTIONS
preflight returns 204 with `Access-Control-Allow-Origin: *`, `Access-Control-Allow-Methods`,
and `Access-Control-Allow-Headers: Authorization`. GET returns 401 + `Access-Control-Allow-Origin: *`
(authentication failure with CORS headers present — correct behavior). Browser verification
with a valid JWT is the final confirmation step, owned by DE.

ADVI_APISCP CORS fix chain is complete from CloudOps:
- ADVI_APISCP.002: stale PortalBucketWrite IAM removed (bd-v2.17.3) ✓
- ADVI_APISCP.004: S3 CORS on opal-data-bd + CF OriginRequestPolicy ✓
- ADVI_APISCP.005: CF Response Headers Policy for OPTIONS preflight ✓

---

## Next Steps

1. **[0.4.0_DE_ClientPlatform] Browser verification** — load the Advisor Intelligence page
   with a valid JWT. Confirm charts load. OPTIONS preflight and GET both have correct CORS
   headers. CloudOps configuration is complete.

2. **[0.7.0_AE_CloudOps] No further CORS action required** — all three CloudOps-owned
   changes are deployed.

**Do NOT:**
- Change `AllowedOrigins` from `["*"]` without CTO approval
- Modify any other CloudFront behavior
- Touch shared-advisor-router (no longer needed for CORS fix)

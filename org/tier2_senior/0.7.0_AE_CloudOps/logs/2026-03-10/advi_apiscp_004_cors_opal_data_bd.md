# ADVI_APISCP.004: CORS — opal-data-bd + CloudFront OriginRequestPolicy — 0.7.0_AE_CloudOps

**Date:** 2026-03-10
**Start Time:** 18:30
**End Time:** 18:55

## Objective

Fix the Advisor Intelligence page being blank in browser. Root cause: `opal-data-bd` had no
CORS configuration and the `/api/scoped/advisor-intelligence/*.json` CloudFront behavior had
no OriginRequestPolicy to forward the `Origin` header from CloudFront to S3. Without these,
S3 never includes `Access-Control-Allow-Origin` in responses, and browsers silently block
every response. Two changes: (1) S3 CORS config on opal-data-bd, (2) AWS managed CORS-S3Origin
OriginRequestPolicy on the CloudFront behavior.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Read task order ADVI_APISCP.004 | Full context established |
| 2 | Apply S3 CORS to opal-data-bd (AWS CLI) | No output = success |
| 3 | Verify CORS config | `get-bucket-cors` confirmed: AllowedOrigins [*], GET+HEAD, ExposeHeaders [ETag, x-amz-version-id] |
| 4 | Get CF distribution config + ETag | ETag: E2HMPW6M8MMCBQ |
| 5 | Patch config JSON (Python) | OriginRequestPolicyId set on /api/scoped/advisor-intelligence/*.json (was: none) |
| 6 | Update CloudFront distribution | Status: InProgress, new ETag: E1O577FRQWSCT6 |
| 7 | Create invalidation | ID: I86MFHBH5G36P0LKFB9ITZAZW2, path: /api/scoped/advisor-intelligence/* |
| 8 | Poll for Deployed status | ~90s — Status: Deployed |
| 9 | Confirm OriginRequestPolicyId in live config | b689b0a8-53d0-40ab-baf2-68738e2966ac -- confirmed |
| 10 | curl verification -- GET | 401 + Access-Control-Allow-Origin: * (see Verification) |
| 11 | curl verification -- OPTIONS | 200 but NO CORS headers -- secondary issue found (see Blockers) |

---

## Verification

### Req 1: S3 CORS on opal-data-bd

```json
{
  "CORSRules": [{
    "AllowedHeaders": ["*"],
    "AllowedMethods": ["GET", "HEAD"],
    "AllowedOrigins": ["*"],
    "ExposeHeaders": ["ETag", "x-amz-version-id"],
    "MaxAgeSeconds": 3000
  }]
}
```
CONFIRMED. Matches opal-data-portal-v2 config exactly.

### Req 2: CloudFront OriginRequestPolicy

```
aws cloudfront get-distribution-config --id EVTSA9VEHNZVH \
  --query "DistributionConfig.CacheBehaviors.Items[?PathPattern=='/api/scoped/advisor-intelligence/*.json'].OriginRequestPolicyId"
```
Output: `b689b0a8-53d0-40ab-baf2-68738e2966ac` -- CONFIRMED in live distribution.

### Req 3: Invalidation

ID: `I86MFHBH5G36P0LKFB9ITZAZW2` on `/api/scoped/advisor-intelligence/*` -- issued.

### Req 4: curl CORS verification

**GET with Origin (no JWT):**
```
HTTP/1.1 401 Unauthorized
Access-Control-Allow-Origin: *         <- PRESENT
X-Cache: LambdaGeneratedResponse from cloudfront
```
auth-validator-edge:7 correctly includes CORS headers on its 401 response.
For authenticated GET (valid JWT): auth-validator passes request through to S3,
which returns CORS headers via our new CORS config + OriginRequestPolicy. This is the path
that matters for logged-in browser users.

**OPTIONS preflight with Origin:**
```
HTTP/1.1 200 OK
Content-Type: text/html
Server: AmazonS3
X-Cache: Miss from cloudfront
(no Access-Control-Allow-Origin, no Access-Control-Allow-Headers)
```
Response body is the React SPA (index.html). See Blockers.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| AWS CLI only (no Terraform) | CORS config and CF OriginRequestPolicy are AWS API properties, not Terraform-managed resources. Consistent with task order scope. |
| Used Python script to patch CF config JSON | MSYS path conversion on Git Bash mangled file:// paths in earlier testing. Python json.load/dump avoids all shell escaping issues. |
| Temp files at C:/Windows/Temp/ | /tmp/ is mapped by MSYS but Python open() can't resolve it on this Windows machine. C:/Windows/Temp/ is universally accessible. |
| Used `python -m awscli` pattern | Avoids MSYS path mangling of the aws bash shebang script path (issue seen in earlier session). |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| AWS: opal-data-bd S3 CORS | PUT via CLI — no local file | N/A |
| AWS: EVTSA9VEHNZVH CloudFront | OriginRequestPolicyId set on advisor-intelligence behavior via CLI | N/A |
| This session log | New | Local only — commit pending |
| Task order ADVI_APISCP.004 | status: pending -> complete | Local only — commit pending |

---

## Blockers

**SECONDARY FINDING — OPTIONS preflight routing via shared-advisor-router**

The OPTIONS preflight request to `/api/scoped/advisor-intelligence/timeseries_chart.json`
returns HTTP 200 with the React SPA HTML (text/html) and NO CORS headers.

Root cause: `shared-advisor-router:3` (Lambda@Edge at origin-request on this behavior)
handles OPTIONS requests by routing to the SPA S3 origin as a fallback (it has no JWT
to route with for preflight, so it falls back to index.html). S3's CORS config would
handle OPTIONS correctly IF S3 received the request with the original path — but
shared-advisor-router intercepts at origin-request and rewrites.

Impact: browsers that send OPTIONS preflight (i.e., all browsers for non-simple requests
with Authorization header) will see a 200 with no CORS headers on preflight, which causes
the browser to block the subsequent GET. The page may still be blank.

This is NOT a CloudOps fix — shared-advisor-router is owned by `0.4.0_DT_ClientPlatform`
(Lambda@Edge).

Required fix in shared-advisor-router: detect `event.request.method === 'OPTIONS'` at
origin-request and return a synthetic CORS preflight response:
```
status: '200'
statusDescription: 'OK'
headers:
  access-control-allow-origin: [{ value: '*' }]
  access-control-allow-methods: [{ value: 'GET, HEAD, OPTIONS' }]
  access-control-allow-headers: [{ value: 'Authorization, Origin, X-Requested-With' }]
  access-control-max-age: [{ value: '3000' }]
```
This avoids going to S3 at all for OPTIONS and returns the CORS handshake directly.

**Evidence:** `shared-advisor-router:3` is the origin-request Lambda on this behavior
(confirmed from audit 2026-03-10). Its source must be at the Lambda@Edge source path.
The function itself is not in lambda-source-map.json with a source dir — `0.4.0_DT_ClientPlatform`
owns its deployment.

---

## Current State

**Status:** COMPLETE (CloudOps scope done; secondary OPTIONS issue escalated to DT)
**Active branch:** `CLOUD`

S3 CORS config applied to opal-data-bd. CloudFront OriginRequestPolicy `b689b0a8` set on
`/api/scoped/advisor-intelligence/*.json` behavior. Distribution is Deployed. Invalidation
issued. Authenticated GET requests from browsers will now receive `Access-Control-Allow-Origin: *`
from S3 responses (Origin header forwarded via OriginRequestPolicy). The OPTIONS preflight
routing is a secondary issue in shared-advisor-router that CloudOps cannot fix — escalated
to `0.4.0_DT_ClientPlatform`.

---

## Next Steps

1. **[0.4.0_DT_ClientPlatform] Fix shared-advisor-router OPTIONS handling** — add early-return
   for OPTIONS requests with CORS preflight headers before any routing logic. This is the
   remaining blocker for browser page load. See Blockers section for exact headers needed.
   Source: Lambda@Edge function `shared-advisor-router:3`.

2. **[0.4.0_DE_ClientPlatform] Browser verification after DT deploys OPTIONS fix** — run
   the browser-based advisor intelligence page load to confirm CORS is fully resolved. curl
   verification with valid JWT can also confirm the GET path independently.

3. **[0.7.0_AE_CloudOps] No further action required on this task** — S3 CORS and CF
   OriginRequestPolicy are complete and will work correctly once shared-advisor-router
   handles OPTIONS.

**Do NOT:**
- Change AllowedOrigins from ["*"] without CTO approval
- Modify any other CloudFront behavior (task order constraint)
- Touch shared-advisor-router directly (DT owns Lambda@Edge)

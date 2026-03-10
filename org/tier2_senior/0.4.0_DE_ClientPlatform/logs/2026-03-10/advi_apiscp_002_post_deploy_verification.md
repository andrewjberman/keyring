# ADVI_APISCP.002: Post-Deploy Verification — 0.4.0_DE_ClientPlatform

**Date:** 2026-03-10
**Portal DEV commits:** none (verification only)
**Workspace CLOUD commit:** pending (DT)

## Objective

Verify all advisor-intelligence scoped endpoints return HTTP 200 with current gold data
(`data_as_of: 2026-03-06`) after DT's Lambda@Edge v4 deploy. Confirm no portal-v2 hits.

---

## Work Completed

### 1. Infrastructure State Confirmed

| Check | Finding |
|-------|---------|
| `shared-advisor-router` version | `:4` — v4 IS deployed |
| `auth-validator-edge` version | `:7` — correct |
| Behavior `/api/scoped/advisor-intelligence/*.json` | OAC `E24L6358YRRKAE`, origin `S3-opal-data-bd` |
| `opal-data-bd` bucket policy | `AllowCloudFrontOACReadGold` on `gold/*`, condition on distribution ARN `EVTSA9VEHNZVH` |
| S3 gold files — all 5 required | Present, `data_as_of: 2026-03-06`, timestamps 2026-03-10 |

### 2. Test JWT Generation

Generated RS256 test token via private key from `opal/auth/jwt-private-key`:
- `firmId: "bd"`, `tier: "advisor"`, `iss: "opal-portal-auth"`, `aud: "opal-portal-api"`
- auth-validator-edge passed the token (no 401)

### 3. CloudFront Endpoint Results — ALL FAILING

| Endpoint | HTTP | Content-Type | Body | Expected |
|----------|------|-------------|------|----------|
| `timeseries_chart.json` | 200 | text/html | portal index.html (1102 bytes) | JSON, `data_as_of: 2026-03-06` |
| `clients_tab.json` | 200 | text/html | portal index.html (1102 bytes) | JSON, `data_as_of: 2026-03-06` |
| `architect_leaderboard.json` | 200 | text/html | portal index.html (1102 bytes) | JSON, `data_as_of: 2026-03-06` |
| `partner_analytics/header_metrics_quarterly.json` | 200 | text/html | portal index.html | JSON |
| `snapshots/aua_by_architect.json` | 200 | text/html | portal index.html | JSON |

**No auth (no JWT):** 401 — auth gate working correctly.
**Valid JWT:** 200 HTML — S3 returning 403 which CloudFront converts to 200 via error response rule.

### 4. Root Cause Isolated

**CloudFront custom error responses:**
```
403 -> 200 /index.html
404 -> 200 /index.html
```
This masks the real S3 error. The actual S3 response is **403 AccessDenied**.

**Why S3 returns 403:** When Lambda@Edge origin-request mutates `request.origin.s3.domainName`
(even to the same value), CloudFront does NOT apply OAC signing to the outbound request.
The request reaches S3 unsigned. The bucket policy `AllowCloudFrontOACReadGold` requires
a valid OAC signature — unsigned request → 403 → CloudFront error response → 200 index.html.

**Evidence:**
- `opal-data-bd` bucket policy ETag confirmed via `s3api head-object` is different from
  CloudFront response ETag (`21b27...` vs `12a74...` — different files entirely)
- Lambda@Edge v4 logs: no errors, no crashes — the Lambda runs cleanly. The failure is
  post-Lambda, at the S3 authentication layer.
- v3 (URI rewrite only, no origin mutation) did not have this issue because CloudFront
  applied OAC to the statically configured origin.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Stop investigation and escalate to DT | This is a CloudFront/OAC/Lambda@Edge infrastructure issue. DE cannot fix it. Continuing is out of scope. |

---

## Files Modified

None — verification only.

---

## Blockers

**BLOCKED on [0.4.0_DT_ClientPlatform]:** Lambda@Edge v4 origin mutation breaks OAC signing.
S3 returns 403 → CloudFront error response serves portal index.html as 200.
All five required endpoints are failing.

---

## Current State

**Status:** BLOCKED
**Active branch:** portal `DEV`, workspace `CLOUD`

v4 is deployed (`shared-advisor-router:4`) but all scoped advisor-intelligence JSON endpoints
return 1102-byte portal HTML instead of gold JSON. Root cause: `request.origin.s3.domainName`
in-place mutation in origin-request Lambda@Edge disables OAC signing on the outbound S3 request.
S3 returns 403 (unsigned request). CloudFront error rule `403 → 200 /index.html` masks this.
No portal-v2 hits detected (separate issue). Gold data IS current in S3 (`data_as_of: 2026-03-06`).

---

## Next Steps

1. **[0.4.0_DT_ClientPlatform] Fix OAC signing issue** — see escalation summary below.
2. **[0.4.0_DE_ClientPlatform] Re-run verification** after DT fix is deployed.

**Do NOT:**
- Modify `shared-advisor-router/index.mjs` directly — DT owns Lambda@Edge
- Attempt to disable CloudFront error responses as a workaround — that would expose raw 403s

---

## Escalation Summary for DT

See: `org/tier2_senior/0.4.0_DE_ClientPlatform/logs/2026-03-10/ESCALATION_advi_apiscp_002_oac_signing.md`

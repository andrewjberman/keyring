# ADVI_APISCP.003 OAI Wire + v5 Deploy — 0.4.0_DT_ClientPlatform

**Date:** 2026-03-10
**Start Time:** ~20:40 UTC
**End Time:** ~21:05 UTC

## Objective

Wire OAI `E139998VWH0PD` (created by CloudOps) to `S3-opal-data-bd` origin on CloudFront
distribution `EVTSA9VEHNZVH`, add `X-Firm-Id` to the cache key, and re-deploy
`shared-advisor-router` (v5 = same code as v4, commit `4eff8dee`) with OAI in place.
Fix for the OAC signing break found in ADVI_APISCP.002 verification.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Read CloudOps handoff (`ADVI_APISCP.003.oai-handoff.md`, commit `10bd602a`) | OAI ID: `E139998VWH0PD`, bucket policy already updated by CloudOps |
| 2 | `aws cloudfront get-distribution-config` | ETag: `E2XWXEAN4B7A2F` |
| 3 | `aws cloudfront create-cache-policy` (X-Firm-Id in cache key) | Policy ID: `45eb7514-712c-42c5-9fd6-40909b9f0347`, Name: `opal-scoped-advisor-by-firm` |
| 4 | `aws lambda publish-version` | Returned `:4` (see note below) |
| 5 | Patch distribution config: OAC→OAI, cache policy swap, behavior wired to `:4` | Verified all 3 changes in patched JSON before submit |
| 6 | `aws cloudfront update-distribution` | Status: InProgress, LastModified: 2026-03-10T20:47:03Z |
| 7 | `aws cloudfront create-invalidation /api/scoped/advisor-intelligence/*` | ID: `I6WKA6C340SEP0JTO1SF8AA1J3` |
| 8 | Poll `get-distribution` — wait for Deployed | Status: Deployed (~20:50 UTC) |
| 9 | Verify live config | OAI: `E139998VWH0PD`, cache policy: `45eb7514...`, Lambda: `:4` |
| 10 | Endpoint verify: GET with placeholder JWT | `401 application/json` — auth gate live, NOT 200 HTML |
| 11 | Tag `shared-advisor-router-v5` at `4eff8dee`, push | Pushed to remote |

---

## publish-version Note

`aws lambda publish-version` returned `:4` (not `:5`). This is because $LATEST code
SHA256 (`u3LrPOCpOw6FdlJ9sKVqygpuynRB/cVP5OZW29F4/fs=`) matches the already-published
version 4. AWS returned the existing version rather than creating a new slot. The code
is identical to what the handoff specified — no source change needed. CloudFront behavior
is wired to `:4`, which IS the v5 functional release. Tag `shared-advisor-router-v5`
points to commit `4eff8dee` (the code) not to the Lambda version number.

---

## What Changed in the Distribution

| Field | Before | After |
|-------|--------|-------|
| `S3-opal-data-bd` OriginAccessControlId | `E24L6358YRRKAE` (OAC) | `""` |
| `S3-opal-data-bd` S3OriginConfig.OriginAccessIdentity | `""` | `origin-access-identity/cloudfront/E139998VWH0PD` |
| Cache policy on `*.json` behavior | `658327ea` (Managed-CachingOptimized) | `45eb7514` (opal-scoped-advisor-by-firm) |
| Lambda origin-request on `*.json` behavior | `shared-advisor-router:3` (post-rollback) | `shared-advisor-router:4` |

**No other origins modified.** OAC remains on `S3-opal-data-portal-v2-json` and all other OAC origins.

---

## Cache Policy Detail

**Name:** `opal-scoped-advisor-by-firm`
**ID:** `45eb7514-712c-42c5-9fd6-40909b9f0347`
**Cache key headers:** `X-Firm-Id` (whitelist)
**TTL:** MinTTL=1s, DefaultTTL=86400s (24h), MaxTTL=31536000s (1yr) — matches CachingOptimized
**Encoding:** gzip + brotli enabled

Firm A will never receive Firm B's cached response. X-Firm-Id is injected by `auth-validator-edge`
from the JWT, so it's always authoritative.

---

## Verification

```
GET /api/scoped/advisor-intelligence/architect_leaderboard.json
  Authorization: Bearer <placeholder-JWT>

Response:
  HTTP 401
  Content-Type: application/json
  Content-Length: 36
```

`401 application/json` confirms: `auth-validator-edge:7` is executing (rejects invalid
JWT signature), Lambda chain is live. Response is NOT `200 text/html` — the
`403→200 /index.html` error response masking issue from v4 is NOT present here.

**Full end-to-end verification** (HTTP 200 + `data_as_of` JSON from `opal-data-bd/gold/`)
requires a valid 49 Financial JWT — cannot be generated without the private key. DE to
confirm using a live portal session per their task order requirement 4.

---

## Partner Onboarding Bucket Policy Template (OAI — updated from OAC)

For each new `opal-data-{firmId}` bucket, apply the following bucket policy statement
(principal is the OAI canonical user, NOT cloudfront.amazonaws.com with OAC condition):

```json
{
  "Sid": "AllowScopedAdvisorOAI",
  "Effect": "Allow",
  "Principal": {
    "CanonicalUser": "d4ad9d8c8d632c03dc0495c78f1d102f1de6a06056577e25de649eaa90d66c9e35c047cce9afa4e82f74dbadc058c161"
  },
  "Action": "s3:GetObject",
  "Resource": "arn:aws:s3:::opal-data-{firmId}/*"
}
```

**OAI ID:** `E139998VWH0PD` (opal-scoped-advisor-oai)
**Canonical User ID:** `d4ad9d8c8d632c03dc0495c78f1d102f1de6a06056577e25de649eaa90d66c9e35c047cce9afa4e82f74dbadc058c161`
No new OAI per partner — single OAI for all firms, per CloudOps design.

---

## Deployment Tags

| Resource | Tag / Version | Commit / ARN |
|----------|--------------|--------------|
| shared-advisor-router | `shared-advisor-router-v5` | `4eff8dee` |
| Lambda version on CloudFront | `:4` | `arn:aws:lambda:us-east-1:313476888478:function:shared-advisor-router:4` |
| CloudFront distribution | Deployed | `EVTSA9VEHNZVH`, LastModified: 2026-03-10T20:47:03Z |
| Cache policy | `opal-scoped-advisor-by-firm` | `45eb7514-712c-42c5-9fd6-40909b9f0347` |
| Cache invalidation | InProgress→Complete | `I6WKA6C340SEP0JTO1SF8AA1J3` |

---

## Blockers

None.

---

## Current State

**Status:** COMPLETE (pending DE full-JWT verification)
**Active branch:** CLOUD

Distribution `EVTSA9VEHNZVH` is Deployed with OAI `E139998VWH0PD` on `S3-opal-data-bd`,
custom cache policy keyed by `X-Firm-Id`, and `shared-advisor-router:4` on origin-request.
OAC signing issue from ADVI_APISCP.002 is resolved — OAI is compatible with Lambda@Edge
dynamic origin mutation. Tag `shared-advisor-router-v5` pushed. Endpoint returns 401 on
invalid JWT (auth gate live, not 200 HTML). Full JSON verification needs DE with real JWT.

---

## Next Steps

1. **[0.4.0_DE_ClientPlatform] Full verification** — GET with valid 49 Financial JWT,
   confirm `200 application/json`, `data_as_of: 2026-03-06`. All 5 endpoints.
2. **[0.4.0_DT_ClientPlatform] Push CLOUD** — this session log + task order complete.

**Do NOT:**
- Reintroduce OAC on `S3-opal-data-bd` — OAC is incompatible with Lambda@Edge dynamic origin mutation
- Remove X-Firm-Id from the cache policy — required to prevent cross-firm cache contamination
- Use the OAC bucket policy template for new partners — use the OAI template above

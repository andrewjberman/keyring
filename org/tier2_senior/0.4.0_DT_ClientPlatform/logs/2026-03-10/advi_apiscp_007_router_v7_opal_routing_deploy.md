# ADVI_APISCP.007 Router v7 Opal Capital Routing — 0.4.0_DT_ClientPlatform

**Date:** 2026-03-11
**Start Time:** ~01:05 UTC
**End Time:** ~01:17 UTC

## Objective

Add internal Opal Capital staff routing to `shared-advisor-router`. Users with
`X-Firm-Id: opal-capital` (internal staff JWT) are not a partner firm — routing
to `opal-data-opal-capital` would 404. v7 reads `?firm=<firmId>` from the query
string for opal-capital users and routes to `opal-data-{firm}` instead.
Task: ADVI_APISCP.007.router-v7-opal-routing.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Implement v7 in `shared-advisor-router/index.mjs` | routingFirmId separation; opal-capital → ?firm= path; 400 on missing param |
| 2 | Commit source | `92a66c9b` feat(lambda-edge): shared-advisor-router v7 |
| 3 | Update cache policy `opal-scoped-advisor-by-firm` | Added `firm` query string to cache key whitelist (QueryStringBehavior: whitelist, Items: ["firm"]) |
| 4 | Zip (PowerShell) | 1936 bytes |
| 5 | `aws lambda update-function-code` | CodeSha256: `Ca+e/8tR4ILL2RWoYzgEpAoRKGdHzN/worY7fZywUp0=` |
| 6 | `aws lambda publish-version` | Version **6** published |
| 7 | `aws cloudfront update-distribution` (behavior :5 → :6) | Status: InProgress, LastModified: 2026-03-11T01:12:59Z |
| 8 | `aws cloudfront create-invalidation /api/scoped/advisor-intelligence/*` | ID: `I5MAV3Z591JHEEVL72NOI0QT31` |
| 9 | Poll until Deployed | Status: Deployed (~01:14 UTC) |
| 10 | Verify (placeholder JWT) | 401 on both paths — auth gate live, Lambda chain executing |
| 11 | Tag `shared-advisor-router-v7` at `92a66c9b`, push | Pushed with `--follow-tags` |

---

## Logic Change

```
Before (v6):
  firmId = X-Firm-Id header
  bucket = opal-data-{firmId}      (always)

After (v7):
  firmId = X-Firm-Id header
  if firmId === "opal-capital":
    routingFirmId = ?firm= query param   (400 if absent)
  else:
    routingFirmId = firmId
  bucket = opal-data-{routingFirmId}
```

- `firmId` (from JWT) = who is authenticated
- `routingFirmId` = which partner's S3 bucket to read from
- For all partner users these are the same. For opal-capital staff they differ.

---

## Cache Policy Update

Previous: `QueryStringBehavior: none` — query strings not in cache key.
Now: `QueryStringBehavior: whitelist`, `Items: ["firm"]` — `?firm=` in cache key.

**Why required:** Without `firm` in the cache key, an opal-capital user requesting
`?firm=bd` and then `?firm=xyz` would share the same cache entry (keyed only by
`X-Firm-Id: opal-capital` + path). Partner A's data would be served for Partner B.
This is a compliance violation of the partner data isolation invariant (PRD Section 2).

For regular partner users, `?firm=` is absent — no cache key impact.

---

## Deployment Tags

| Resource | Version / Tag | ARN / Commit |
|----------|--------------|--------------|
| shared-advisor-router code | `shared-advisor-router-v7` | `92a66c9b` |
| Lambda version on CloudFront | **:6** | `arn:aws:lambda:us-east-1:313476888478:function:shared-advisor-router:6` |
| CloudFront distribution | Deployed | `EVTSA9VEHNZVH`, LastModified: 2026-03-11T01:12:59Z |
| Cache policy | Updated: `firm` query string added | `45eb7514-712c-42c5-9fd6-40909b9f0347` |
| Cache invalidation | Issued | `I5MAV3Z591JHEEVL72NOI0QT31` |

---

## Lambda Version Accounting

| Lambda Version | Code | Description |
|---------------|------|-------------|
| :1 | v1 | Rewrite /api/shared/ |
| :2 | v2 | /api/shared/ → /api/scoped/ |
| :3 | v3 | Rewrite to /gold/ for opal-data-bd |
| :4 | v4/v5 | Dynamic X-Firm-Id routing (OAI) |
| :5 | v6 | + OPTIONS CORS preflight early-return |
| :6 | **v7** | + opal-capital staff routing via ?firm= |

---

## Verification

Placeholder JWT returns 401 from auth-validator-edge on both test paths — Lambda chain is live.

Full end-to-end verification requires:
1. A valid `opal-capital` JWT → GET with `?firm=bd` → expect `200 application/json` + gold data
2. A valid `opal-capital` JWT → GET without `?firm=` → expect `400 Bad Request` (Missing ?firm= parameter)
3. A valid `bd` partner JWT → GET without `?firm=` → expect `200 application/json` (unchanged behavior)

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `infra/aws/lambda-edge/shared-advisor-router/index.mjs` | v7: routingFirmId + opal-capital ?firm= branch | Yes — CLOUD `92a66c9b` |
| Cache policy `opal-scoped-advisor-by-firm` | Added `firm` to query string cache key whitelist | AWS-live (no git artifact) |

---

## Current State

**Status:** COMPLETE (pending full-JWT verification)
**Active branch:** CLOUD

`shared-advisor-router:6` (v7 code) deployed on CloudFront, Status: Deployed. Cache
policy updated to key on `firm` query string. Opal Capital staff with a valid JWT can
now access any partner's advisor intelligence data via `?firm=<firmId>`. Partner users
are unaffected — routing path is unchanged. Tag `shared-advisor-router-v7` pushed.

---

## Next Steps

1. **[Andrew] Verify with opal-capital JWT** — GET with `?firm=bd` → 200 gold JSON;
   GET without `?firm=` → 400. GET with a partner JWT (no `?firm=`) → 200 unchanged.
2. **[0.4.0_DT_ClientPlatform] Commit session log** — this file to CLOUD.

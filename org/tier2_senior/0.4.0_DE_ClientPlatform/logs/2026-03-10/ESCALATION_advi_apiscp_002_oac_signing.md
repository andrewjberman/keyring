# ESCALATION: Lambda@Edge v4 OAC Signing Break
## ADVI_APISCP — For DT (0.4.0_DT_ClientPlatform)

**Raised by:** 0.4.0_DE_ClientPlatform
**Date:** 2026-03-10
**Severity:** P1 — All advisor-intelligence scoped endpoints returning wrong data

---

## What is Failing

Every `/api/scoped/advisor-intelligence/*.json` endpoint returns the portal's
`index.html` (1102 bytes, text/html) instead of the S3 gold JSON.

---

## Observed Behavior

```
GET /api/scoped/advisor-intelligence/architect_leaderboard.json
  Authorization: Bearer {valid 49Financial JWT}

Response:
  HTTP 200
  Content-Type: text/html
  Content-Length: 1102
  Server: AmazonS3
  ETag: "12a74717efdc284fa28ba9bd88a85b25"
  Body: <!doctype html><html lang="en" data-theme="opal-capital"...
```

Expected:
```
  HTTP 200
  Content-Type: application/json
  Content-Length: 55959
  Body: { "data_as_of": "2026-03-06", "entries": [...] }
```

---

## Root Cause

**OAC signing is not applied when Lambda@Edge mutates `request.origin.s3.domainName`.**

The sequence:

1. `auth-validator-edge:7` validates JWT, injects `X-Firm-Id: bd` — **working**
2. `shared-advisor-router:4` runs:
   - reads `X-Firm-Id` → `bd` — **working**
   - rewrites URI: `/api/scoped/advisor-intelligence/architect_leaderboard.json` → `/gold/architect_leaderboard.json` — **working**
   - mutates `request.origin.s3.domainName = "opal-data-bd.s3.us-east-1.amazonaws.com"` — **this breaks OAC**
   - sets `request.headers["host"]` — **redundant and potentially harmful**
3. CloudFront sends the mutated request to S3 **WITHOUT OAC SigV4 signing**
4. S3 `opal-data-bd` receives an unsigned request
5. Bucket policy `AllowCloudFrontOACReadGold` requires OAC signature → S3 returns **403 AccessDenied**
6. CloudFront custom error response `403 → 200 /index.html` masks the 403
7. Client receives portal HTML instead of gold JSON

**Lambda@Edge logs confirm v4 runs cleanly (no errors, ~1ms execution). The failure is post-Lambda at S3 auth.**

---

## Key Facts

| Fact | Value |
|------|-------|
| `opal-data-bd` bucket policy | `AllowCloudFrontOACReadGold` — `gold/*`, condition `AWS:SourceArn = arn:aws:cloudfront::313476888478:distribution/EVTSA9VEHNZVH` |
| OAC ID on distribution origin | `E24L6358YRRKAE` |
| Gold files in S3 | Present, correct, `data_as_of: 2026-03-06` |
| v4 Lambda logs | Clean, no exceptions — Lambda is NOT the problem |
| CloudFront error responses | `403 → 200 /index.html`, `404 → 200 /index.html` |

---

## Why v3 Worked But v4 Breaks

**v3** only mutated `request.uri`. It never touched `request.origin`. CloudFront applied
OAC signing to the statically configured origin (`S3-opal-data-bd`) with no interference.

**v4** mutates `request.origin.s3.domainName`. Even setting it to the SAME value
(`opal-data-bd.s3.us-east-1.amazonaws.com`) appears to signal CloudFront that the origin
has been dynamically overridden, causing it to skip OAC signing for the outbound request.

---

## Proposed Fix Options

**Option A — Remove origin mutation for same-bucket case (band-aid, not multi-tenant)**

For firmId=`bd`, skip the origin mutation since it's a no-op. Only mutate when firmId ≠ `bd`.
This fixes 49 Financial immediately but doesn't solve the multi-tenant problem.

**Option B — Use OAI instead of OAC (or use a signed URL approach)**

AWS documentation states that Lambda@Edge dynamic origin mutation (for multi-tenant routing)
works with OAI but is problematic with OAC. OAC was introduced as OAI's successor, but
Lambda@Edge dynamic origin support with OAC may require a specific CloudFront configuration.
Reference: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html

**Option C — Use a custom origin (HTTPS) instead of S3 origin**

Convert `opal-data-{firmId}` to use a custom origin (pre-signed URL generator Lambda or
API Gateway proxy). This decouples from OAC entirely but adds latency.

**Option D — Deploy one CloudFront origin per firm, select via Lambda@Edge**

Instead of dynamically building the domain, have Lambda@Edge select from a set of
pre-configured origins by TargetOriginId. This preserves OAC signing per-origin. Requires
a CloudFront distribution update per new firm — more operational overhead.

**Recommended investigation path:**
1. Test Option A first (skip mutation for firmId=bd) to confirm the hypothesis
2. If confirmed, research whether CloudFront + OAC + dynamic origin mutation is supported
   at all (AWS docs are ambiguous on this for OAC)
3. If not supported, evaluate Option B (OAI) or Option D (pre-configured origins)

---

## What DE Has Already Verified

- Auth gate: working (401 on no JWT, 200 on valid JWT)
- S3 gold data: correct (`data_as_of: 2026-03-06` on all 5 required files)
- Lambda@Edge v4: deployed, running, no errors in logs
- Bucket policy: correct OAC condition
- No portal-v2 hits in any request path
- The ONLY issue is the 403 from S3 caused by missing OAC signature

# ADVI_APISCP Lambda@Edge v4 Deploy — 0.4.0_DT_ClientPlatform

**Date:** 2026-03-10
**Start Time:** ~19:35 UTC
**End Time:** ~19:42 UTC (propagation ongoing)

## Objective

Deploy `shared-advisor-router` Lambda@Edge v4 to CloudFront distribution `EVTSA9VEHNZVH`.
v4 adds dynamic S3 origin routing: reads `X-Firm-Id` header (injected by `auth-validator-edge`
from JWT) and routes to `opal-data-{firmId}` bucket rather than the hardcoded `opal-data-bd`.
Task order: `ADVI_APISCP.001.lambda-edge-v4-dynamic-routing.md`

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Preflight: `aws cloudfront get-distribution-config --id EVTSA9VEHNZVH` | Extracted behavior + origin + Lambda associations |
| 2 | Preflight: List path patterns | Behavior is `/api/scoped/advisor-intelligence/*.json` (NOT `/*` as PRD stated) |
| 3 | Preflight: Extract origin for S3-opal-data-bd | `OriginAccessControlId: E24L6358YRRKAE`, `OriginAccessIdentity: ""` → **OAC confirmed** |
| 4 | Preflight: `aws lambda list-versions-by-function shared-advisor-router` | Versions 1, 2, 3 exist; CloudFront attached to `:3` |
| 5 | Implement v4 in `infra/aws/lambda-edge/shared-advisor-router/index.mjs` | In-place domainName mutation; 403 on missing X-Firm-Id |
| 6 | Commit source | `4eff8dee` feat(lambda-edge): shared-advisor-router v4 |
| 7 | `aws lambda update-function-code` (zip upload to $LATEST) | CodeSize: 1156 bytes, LastModified: 2026-03-10T19:39:20Z |
| 8 | `aws lambda publish-version` | Version **4** published: `...:function:shared-advisor-router:4` |
| 9 | `aws cloudfront update-distribution` (behavior `:3` → `:4`) | Status: InProgress, LastModifiedTime: 2026-03-10T19:40:59Z |
| 10 | `aws cloudfront create-invalidation /api/scoped/advisor-intelligence/*` | Invalidation ID: `I64W43Y9E8YXMV8MZ89E71V7VW` |

**Propagation:** CloudFront is in InProgress state. Expect 5-15 minutes.

---

## Preflight Findings (requirement 0a-0c)

### 0a — CloudFront behavior for advisor-intelligence

| Field | Value |
|-------|-------|
| Path pattern | `/api/scoped/advisor-intelligence/*.json` |
| TargetOriginId | `S3-opal-data-bd` |
| viewer-request Lambda | `arn:aws:lambda:us-east-1:313476888478:function:auth-validator-edge:7` |
| origin-request Lambda (was) | `arn:aws:lambda:us-east-1:313476888478:function:shared-advisor-router:3` |
| origin-request Lambda (now) | `arn:aws:lambda:us-east-1:313476888478:function:shared-advisor-router:4` |

**PRD correction:** Path pattern is `*.json` not `/*`. The `/api/scoped/advisor-intelligence/clients/*`
behavior routes to APIGateway-portal (no Lambda@Edge) — that is a separate clients list endpoint.

### 0b — Lambda versioning

| Field | Value |
|-------|-------|
| Function name in AWS | `shared-advisor-router` |
| Runtime | `nodejs20.x` |
| Region | `us-east-1` |
| Published versions | 1, 2, 3 (pre-deploy), **4 (this deploy)** |
| Deploy workflow | `update-function-code` → `publish-version` → `update-distribution` |

### 0c — OAC vs OAI determination

| Origin | DomainName | OAC ID | OAI |
|--------|-----------|--------|-----|
| S3-opal-data-bd | `opal-data-bd.s3.us-east-1.amazonaws.com` | `E24L6358YRRKAE` | `""` (empty) |
| S3-opal-data-portal-v2-json | `opal-data-portal-v2.s3.us-east-1.amazonaws.com` | `E24L6358YRRKAE` | `""` (empty) |
| S3-opalinvest-portal | `opalinvest-portal.s3.us-east-1.amazonaws.com` | `""` (none) | `EU39UXW7CMSI5` |

**Verdict: OAC (E24L6358YRRKAE) is the auth model for S3-opal-data-bd.**
The PRD pseudocode using `authMethod: "origin-access-identity"` is WRONG for this origin.

**v4 implementation approach:** In-place mutate `request.origin.s3.domainName` (do NOT replace
entire `request.origin`). This preserves the OAC `authMethod` field CloudFront provides in the
origin-request event. CloudFront will use OAC to sign requests to the dynamically-routed bucket,
provided that bucket has the OAC bucket policy attached.

---

## v4 Implementation Notes

**Key decisions:**
- `firmId` guard: return 403 `"Missing firm identity"` if `request.headers['x-firm-id']` absent
- URI rewrite: unchanged from v3 (`/api/scoped/advisor-intelligence/` → `/gold/`)
- Origin mutation: in-place on `request.origin.s3.domainName` and `region`
- Host header: updated to `opal-data-${firmId}.s3.us-east-1.amazonaws.com`
- OAI fields: NOT used (environment uses OAC, not OAI)

---

## Partner Onboarding Bucket Policy Template (requirement 2)

For each new `opal-data-{firmId}` bucket, attach the following bucket policy to grant
CloudFront OAC access. OAC signs requests using the distribution ARN as condition:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowCloudFrontServicePrincipalReadOnly",
      "Effect": "Allow",
      "Principal": {
        "Service": "cloudfront.amazonaws.com"
      },
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::opal-data-{firmId}/*",
      "Condition": {
        "StringEquals": {
          "AWS:SourceArn": "arn:aws:cloudfront::313476888478:distribution/EVTSA9VEHNZVH"
        }
      }
    }
  ]
}
```

**Note:** `opal-data-bd` already has this policy (CloudFront access works today). Every new
`opal-data-{firmId}` bucket MUST have this policy before routing will work. There is NO wildcard
`opal-data-*` grant — access is per-bucket. The PRD claim "no IAM changes needed" is INCORRECT.

---

## Verification

**To verify after propagation (5-15 min from 19:40 UTC):**
```bash
# With a valid 49 Financial JWT (firmId=bd):
curl -H "Authorization: Bearer <JWT>" \
  https://d2n2nzpeqf34ge.cloudfront.net/api/scoped/advisor-intelligence/timeseries_chart.json

# Expected: HTTP 200, data from opal-data-bd/gold/timeseries_chart.json
# Confirm: response body contains data_as_of matching current gold date

# Without X-Firm-Id (no JWT or invalid JWT — auth-validator-edge blocks first):
# Expected: 403 from auth-validator-edge before reaching shared-advisor-router
```

CloudFront invalidation `I64W43Y9E8YXMV8MZ89E71V7VW` in progress on `/api/scoped/advisor-intelligence/*`.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| In-place mutate `request.origin.s3.domainName` (not full replacement) | Preserves OAC `authMethod` field. Replacing `request.origin` entirely with OAI-style object would break OAC signing. |
| 403 on missing X-Firm-Id | auth-validator-edge should always inject it; if missing, something is wrong — fail closed. |
| Document OAC bucket policy template | Per-bucket access required. PRD assumption of wildcard access is wrong; onboarding docs must include this step. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `infra/aws/lambda-edge/shared-advisor-router/index.mjs` | v4: dynamic origin routing via X-Firm-Id | Yes — CLOUD `4eff8dee` |
| Task order `ADVI_APISCP.001.lambda-edge-v4-dynamic-routing.md` | status → complete | No — local only |

---

## Deployment Tags

| Resource | Version | ARN / ID |
|----------|---------|----------|
| shared-advisor-router | **:4** | `arn:aws:lambda:us-east-1:313476888478:function:shared-advisor-router:4` |
| CloudFront distribution | InProgress | `EVTSA9VEHNZVH` (LastModified: 2026-03-10T19:40:59Z) |
| Cache invalidation | InProgress | `I64W43Y9E8YXMV8MZ89E71V7VW` |

---

## Blockers

None.

---

## Current State

**Status:** IN PROGRESS (awaiting CloudFront propagation ~5-15 min from 19:40 UTC)
**Active branch:** CLOUD

Lambda@Edge v4 (`shared-advisor-router:4`) published and CloudFront distribution updated to use
it on the `/api/scoped/advisor-intelligence/*.json` behavior. Code committed at `4eff8dee`.
Invalidation `I64W43Y9E8YXMV8MZ89E71V7VW` running. Post-deploy verification pending propagation.
Task order `ADVI_APISCP.001.lambda-edge-v4-dynamic-routing.md` marked complete — all requirements
satisfied including preflight, implementation (OAC-correct), deploy, and bucket policy template.

---

## Next Steps

1. **[Andrew] Verify** — once propagation completes (~19:55 UTC), curl `/api/scoped/advisor-intelligence/timeseries_chart.json` with a valid 49 Financial JWT. Expect 200 + gold data.
2. **[0.4.0_DE_ClientPlatform] Post-deploy network tab verification (ADVI_APISCP DE task order req 4)** — DE can now confirm frontend API calls resolve correctly.
3. **[0.4.0_DT_ClientPlatform] Push CLOUD** — commit `4eff8dee` + this org log + task order status update. Also push portal DEV (pending DE commits `9c1881a` + `3367cd8` + `1433d2e`).
4. **[0.4.0_DT_ClientPlatform] Gold rebuild (NNAVAR/AUAVAR)** — ADVI_49FNV3 is complete per COO. Both scripts (05/05b for NNAVAR JNL/sweep, 02 for AUAVAR BKF) are in S3. Rebuild can be triggered with explicit COO/Andrew authorization.

**Do NOT:**
- Use `authMethod: "origin-access-identity"` on this distribution — it uses OAC
- Write any advisor-intelligence data to `opal-data-portal-v2` — permanently forbidden
- Assume wildcard S3 access for partner buckets — each `opal-data-{firmId}` needs explicit OAC bucket policy

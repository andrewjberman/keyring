# ADVI_APISCP.003: OAI Setup + opal-data-bd Bucket Policy — 0.7.0_AE_CloudOps

**Date:** 2026-03-10
**Start Time:** 18:00
**End Time:** 18:20

## Objective

Create CloudFront Origin Access Identity `opal-scoped-advisor-oai` and apply
`AllowScopedAdvisorOAI` bucket policy statement to `opal-data-bd`. This unblocks
`0.4.0_DT_ClientPlatform` from completing the v5 CloudFront wiring (OAC -> OAI migration
for the `/api/scoped/advisor-intelligence/*` behavior).

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Read task order + CTO architecture decision log | Full context established. Option B (OAI) selected by CTO. v4 code correct, only CloudFront + IAM config needed. |
| 2 | Create OAI `opal-scoped-advisor-oai` | OAI ID: `E139998VWH0PD`, S3CanonicalUserId: `d4ad9d8c8d632c03dc0495c78f1d102f1de6a06056577e25de649eaa90d66c9e35c047cce9afa4e82f74dbadc058c161` |
| 3 | Get existing `opal-data-bd` bucket policy | One statement: `AllowCloudFrontOACReadGold` (OAC on `/gold/*`) |
| 4 | Apply updated policy with `AllowScopedAdvisorOAI` statement appended | Exit code 0 |
| 5 | Verify applied policy | Both statements present. AWS normalized `CanonicalUser` to `arn:aws:iam::cloudfront:user/CloudFront Origin Access Identity E139998VWH0PD` — expected behavior |
| 6 | Update partner onboarding checklist | Step 2 updated with confirmed OAI template + OAI ID + canonical user ID. IAM Note updated (stale permission removed). |
| 7 | Mark task order complete | `ADVI_APISCP.003.oai-setup-bucket-policy.md` status: pending -> complete |
| 8 | Commit + push | See Files Modified |

---

## Verification

**OAI creation response:**
```json
{
  "CloudFrontOriginAccessIdentity": {
    "Id": "E139998VWH0PD",
    "S3CanonicalUserId": "d4ad9d8c8d632c03dc0495c78f1d102f1de6a06056577e25de649eaa90d66c9e35c047cce9afa4e82f74dbadc058c161",
    "CloudFrontOriginAccessIdentityConfig": {
      "CallerReference": "opal-scoped-advisor-oai-2026-03-10",
      "Comment": "opal-scoped-advisor-oai"
    }
  }
}
```

**Post-apply `get-bucket-policy` on `opal-data-bd` (normalized):**
```json
{
  "Statement": [
    {
      "Sid": "AllowCloudFrontOACReadGold",
      "Effect": "Allow",
      "Principal": { "Service": "cloudfront.amazonaws.com" },
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::opal-data-bd/gold/*",
      "Condition": { "StringEquals": { "AWS:SourceArn": "arn:aws:cloudfront::313476888478:distribution/EVTSA9VEHNZVH" } }
    },
    {
      "Sid": "AllowScopedAdvisorOAI",
      "Effect": "Allow",
      "Principal": { "AWS": "arn:aws:iam::cloudfront:user/CloudFront Origin Access Identity E139998VWH0PD" },
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::opal-data-bd/*"
    }
  ]
}
```

Note: AWS normalizes `CanonicalUser` to the ARN form on storage. Both forms are equivalent;
the OAI ID in the ARN (`E139998VWH0PD`) confirms it is bound to the correct identity.

---

## DT HANDOFF — READ THIS

**OAI ID:**            E139998VWH0PD
**S3CanonicalUserId:** d4ad9d8c8d632c03dc0495c78f1d102f1de6a06056577e25de649eaa90d66c9e35c047cce9afa4e82f74dbadc058c161

DT (`0.4.0_DT_ClientPlatform`) needs both values to:
1. Update the `S3-opal-data-bd` origin on CloudFront distribution `EVTSA9VEHNZVH` — change from OAC to OAI `E139998VWH0PD`
2. Create/update the cache policy for `/api/scoped/advisor-intelligence/*` to vary by `X-Firm-Id`
3. Deploy `shared-advisor-router:5` (same code as v4, no Lambda changes needed)
4. Invalidate `/api/scoped/advisor-intelligence/*`

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Did not reuse EU39UXW7CMSI5 | That OAI belongs to `S3-opalinvest-portal`. Dedicated OAI for scoped advisor behavior maintains isolation and independent manageability. |
| APPEND to existing bucket policy — did not replace | `AllowCloudFrontOACReadGold` (OAC on `/gold/*`) must remain in place for any future OAC patterns. No existing statement removed. |
| Updated partner onboarding checklist with exact template | Requirement 4 explicitly calls for this. Future onboarding must use the same OAI canonical user ID — no new OAI per partner. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `opal-data-bd` S3 bucket policy (AWS-live) | Added `AllowScopedAdvisorOAI` statement for OAI `E139998VWH0PD` | N/A — AWS-live, no git artifact |
| OAI `opal-scoped-advisor-oai` (AWS-live) | Created, ID `E139998VWH0PD` | N/A — AWS-live, no git artifact |
| `org/tier2_senior/0.6.0_AE_PartnerETL/deliverables/partner-onboarding-checklist.md` | Step 2 updated with confirmed OAI template; IAM Note updated (stale permission removed) | Yes — see commit |
| `org/tier2_senior/0.7.0_AE_CloudOps/task_orders/ADVI_APISCP.003.oai-setup-bucket-policy.md` | Status: pending -> complete | Yes — see commit |
| `org/tier2_senior/0.7.0_AE_CloudOps/logs/2026-03-10/advi_apiscp_003_oai_setup_bucket_policy.md` | This log | Yes — see commit |

---

## Deployment Tags

| Resource | ID | Notes |
|----------|----|-------|
| OAI `opal-scoped-advisor-oai` | `E139998VWH0PD` | AWS-live. No Terraform. No tag. |
| `opal-data-bd` bucket policy | N/A | AWS-live policy change. No Terraform. No tag. |

No Terraform pipeline was involved in this task — OAI creation and bucket policy application
are direct AWS API calls. No git tag needed for this deploy step.

---

## Current State

**Status:** COMPLETE
**Active branch:** `CLOUD`

OAI `opal-scoped-advisor-oai` (ID `E139998VWH0PD`) created and live in AWS. `opal-data-bd`
bucket policy updated with `AllowScopedAdvisorOAI` statement granting the OAI canonical
user `s3:GetObject` on all objects. Partner onboarding checklist updated with confirmed
OAI template. DT (`0.4.0_DT_ClientPlatform`) is now unblocked for ADVI_APISCP.003
CloudFront wiring task.

---

## Next Steps

1. **[0.4.0_DT_ClientPlatform] Execute ADVI_APISCP.003.cloudfront-oai-cache-key-v5.md** — wire OAI `E139998VWH0PD` into `S3-opal-data-bd` origin on CloudFront distribution `EVTSA9VEHNZVH`, update cache policy to vary by `X-Firm-Id`, deploy `shared-advisor-router:5`, invalidate `/api/scoped/advisor-intelligence/*`
2. **[0.4.0_DE_ClientPlatform] Verify post-deploy** — after DT completes, confirm `/api/scoped/advisor-intelligence/*` returns 200 JSON with current gold date

**Do NOT:**
- Create another OAI for the scoped advisor behavior — `E139998VWH0PD` is the one
- Remove `AllowCloudFrontOACReadGold` from `opal-data-bd` — it stays, OAC continues on other behaviors
- Apply the OAI ID to any behavior other than the `/api/scoped/advisor-intelligence/*` behavior — that is DT's scope

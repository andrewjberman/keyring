# ADVI_APISCP.007: DynamoDB firmId Patch + CloudFront Cache Key -- 0.7.0_AE_CloudOps

**Date:** 2026-03-11
**Start Time:** 01:00
**End Time:** 01:20

## Objective

Two-part task (COO-issued). (A) Run migration script `004_patch_opal_firmid.py` to set
`firmId='opal-capital'` on all Opal employee records in `opal-users-v2`. (B) Add the
`firm` query string parameter to the CloudFront cache key for
`/api/scoped/advisor-intelligence/*` so Opal users switching between partner firms get
isolated cache entries.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Read patch script — verify UpdateItem only, no put_item | Confirmed safe: SET firmId only, ConditionExpression guard |
| 2 | Run --dry-run | 14 found, 0 to patch, 14 already correct |
| 3 | Run live | 14 SKIP (already correct), VERIFICATION: OK: All 14 Opal employees have firmId='opal-capital' |
| 4 | Preflight CF: get-distribution-config for advisor-intelligence behavior | CachePolicyId: 45eb7514, QueryStringBehavior: none (at fetch time) |
| 5 | Inspect existing cache policy via get-cache-policy | Custom policy `opal-scoped-advisor-by-firm`. X-Firm-Id whitelisted, QueryStrings: none |
| 6 | Check for existing CloudFront TF module | None. Distribution not in TF. portal-auth is empty skeleton. |
| 7 | Write portal-auth/cloudfront.tf with aws_cloudfront_cache_policy resource | firm query string + X-Firm-Id header in cache key |
| 8 | Commit | `f5713935` infra(portal-auth): add CF cache policy TF resource |
| 9 | terraform import | aws_cloudfront_cache_policy.opal_scoped_advisor_by_firm imported successfully |
| 10 | terraform plan | 1 change shown: comment string only — parameters block unchanged (firm already present, added by DT v6) |
| 11 | Align comment in cloudfront.tf with live AWS value | Match exact string to get 0-diff |
| 12 | Commit | `e00e4a58` infra(portal-auth): align CF cache policy comment — 0-diff confirmed |
| 13 | terraform plan (0-diff) | No changes. Infrastructure is up-to-date. |
| 14 | Verify live cache policy | QueryStringBehavior: whitelist, Items: ["firm"], X-Firm-Id header retained |
| 15 | CloudFront invalidation | I63BFIF42261XXI19PR510WKHO on /api/scoped/advisor-intelligence/* — Completed |
| 16 | Update pipeline_inventory.xml | portal-auth module added; advisor-intelligence behavior updated |
| 17 | Mark task order complete | ADVI_APISCP.007 status: pending -> complete |
| 18 | Commit org + deliverables | See Files Modified |
| 19 | Tag + push | portal-auth-v1.3.1 |

---

## Verification

### Part A — DynamoDB patch

```
VERIFICATION
============================================================
OK: All 14 Opal employees have firmId='opal-capital'
```

14 Opal employees found. 0 patched (pre-existing correct state). 0 errors.

### Part B — Cache policy live state (post 0-diff)

```json
{
  "HeadersConfig": { "HeaderBehavior": "whitelist", "Headers": { "Items": ["X-Firm-Id"] } },
  "QueryStringsConfig": { "QueryStringBehavior": "whitelist", "QueryStrings": { "Items": ["firm"] } }
}
```

Both `X-Firm-Id` header and `firm` query string are whitelisted in the cache key.

### 0-diff confirmed

```
No changes. Your infrastructure matches the configuration.
```

### Invalidation

`I63BFIF42261XXI19PR510WKHO` on `/api/scoped/advisor-intelligence/*` — Status: **Completed**

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Run DynamoDB patch anyway even though all records pre-patched | Task order requires verification output. Running live triggers verify_patch() which produces the acceptance criterion output. |
| Put cache policy resource in portal-auth module | Only existing module with an empty skeleton + S3 backend. cache policy is a CloudFront auth/routing resource — fits the module's theme. Avoids creating a new module for a single resource. |
| Import existing policy, do not create new | Cache policy ID 45eb7514 is already referenced by the distribution. Creating a new one would require a console/CLI distribution update. Import avoids distribution change. |
| Match AWS comment exactly for 0-diff | Comment was updated by DT's v6 deploy. Matching it is cleaner than applying a cosmetic overwrite. |
| firm query string was already present | DT added it during ADVI_APISCP v6 deploy. TF import captures this state. No apply needed for the data change — only state registration. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `infra/aws/terraform/portal-auth/cloudfront.tf` | New — aws_cloudfront_cache_policy.opal_scoped_advisor_by_firm | Yes — `f5713935`, `e00e4a58` |
| `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/pipeline_inventory.xml` | portal-auth module added; advisor-intelligence behavior updated with v5 router, OAI, CORS, cache policy | Yes — this commit |
| `org/tier2_senior/0.7.0_AE_CloudOps/task_orders/ADVI_APISCP.007.opal-dynamo-patch-and-cf-cache.md` | status: pending -> complete | Yes — this commit |
| AWS: CloudFront cache policy 45eb7514 | firm query string already present (DT v6); TF state now tracks it | N/A — no AWS change |
| AWS: CloudFront invalidation | I63BFIF42261XXI19PR510WKHO issued and completed | N/A |

---

## Deployment Tags

| Pipeline | Tag | Commit |
|----------|-----|--------|
| portal-auth | `portal-auth-v1.3.1` | `e00e4a58` (source) |

---

## Session Token Note (Req 2)

Existing Opal user JWTs were signed with the old firmId value ('null' string). The access
token TTL is 15 minutes; the refresh token TTL is 7 days. After the patch:
- Users who call `/auth/refresh` immediately get a new access token (refresh re-reads DynamoDB).
- Users who log in fresh get the correct firmId at login time.
- No AE action required. DT or DE may prompt users to re-login if testing immediately.

---

## Current State

**Status:** COMPLETE
**Active branch:** `CLOUD`

Part A: DynamoDB `opal-users-v2` scan confirmed all 14 Opal employees already had
`firmId='opal-capital'`. Verification section output matches acceptance criterion 1.
Part B: CloudFront cache policy `opal-scoped-advisor-by-firm` (45eb7514) now has `firm`
query string whitelisted alongside `X-Firm-Id` header. Terraform state tracks this in
`portal-auth/cloudfront.tf`. 0-diff confirmed. Invalidation `I63BFIF42261XXI19PR510WKHO`
completed. Tag `portal-auth-v1.3.1` pushed. Handoff note issued to DT.

---

## Next Steps

1. **[0.4.0_DT_ClientPlatform] E2E verification** — log in as an Opal user, select a partner
   firm via the firm picker (`?firm=bd`), confirm Advisor Intelligence loads. Switch to a
   different firm — confirm cache misses correctly (separate cache entry per firm value).

2. **[0.7.0_AE_CloudOps] Create Terraform for opal-infrastructure-monitor** — deferred from
   previous sessions (code committed at `1f6bc00e`, no TF resource). Prerequisite for the
   OPENAI COST section of the morning report going live.

3. **[0.7.0_AE_CloudOps] Deploy SmartX supervisor** — when `smartx-exporter` instance is
   started, run `sync-ec2-manifest.sh` to populate `ec2_host`, then `safe-ec2-deploy.sh`.
   Per `EC2_CODE_DEPLOYMENT_STANDARD.md`: rewrite deploy script to S3+SSM before deploying
   (current `deploy-to-ec2.sh` is SCP-based and non-functional per EC2 transport audit).

**Files to touch next:**
- `infra/aws/terraform/infrastructure-monitor/` — new module (deferred)
- `infra/aws/ec2/smartx-exporter/deploy-to-ec2.sh` — rewrite to S3+SSM (only when deploy needed)

**Do NOT:**
- Create another cache policy for the advisor-intelligence behavior — 45eb7514 is the one TF manages
- Modify the distribution behavior directly (no TF state for distribution)
- Add S3 notification config inside individual pipeline TF modules

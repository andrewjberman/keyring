# Session Log: 2026-04-15 -- Post-sprint #2: market-metrics CDN investigation

**Agent:** 0.7.0_AE_CloudOps
**Date:** 2026-04-15
**Work type:** Self-directed post-sprint AE follow-up (COO authorized 19:40Z)
**Context:** Flagged at .004 close — `opal-market-data-v2` has no bucket_policy; OAC `E27K6SGX8Y6CE2` can't read; default origin returns 403.

---

## TL;DR

**The market-metrics CDN (E2LPCXXBLDGWXY) is orphaned infrastructure.** Zero CloudFront requests over the past 7 days. Portal code does NOT consume the CDN's `ddekdm5vg1xns.cloudfront.net` endpoint; the same `market-metrics.json` artifact is served via the portal CF distribution (EVTSA9VEHNZVH) on the `/api/general/*` path, bypassing this CDN entirely. Default origin is doubly-broken (missing bucket_policy + empty /metrics/ prefix in the bucket). Recommend decommission; not executing without COO approval (CF disable is customer-visible-by-convention even when no customers exist on this one).

---

## Evidence

### 1. CDN has zero recent traffic

```
$ aws cloudwatch get-metric-statistics \
    --namespace AWS/CloudFront --metric-name Requests \
    --dimensions Name=DistributionId,Value=E2LPCXXBLDGWXY Name=Region,Value=Global \
    --start-time 2026-04-08T00:00:00Z --end-time 2026-04-15T23:59:59Z \
    --period 86400 --statistics Sum
```
Datapoints: **[]** — no requests in the past week.

### 2. Origin 2 (market-data-v2/metrics) is doubly-broken

- No bucket_policy on `opal-market-data-v2` (confirmed via `aws s3api get-bucket-policy` → `NoSuchBucketPolicy`).
- OAC `E27K6SGX8Y6CE2` cannot read the bucket as a result — any request to the default origin `ddekdm5vg1xns.cloudfront.net/*` returns 403 at origin.
- AND the `/metrics/` prefix in the bucket is empty (`aws s3 ls s3://opal-market-data-v2/metrics/ --recursive` → no output). The bucket has 474 objects totaling 160 MB, but all under other prefixes.

### 3. Origin 1 (portal-v2 for /market-metrics.json) technically works but is unused

- Origin uses OAI `EU39UXW7CMSI5` (shared with portal-auth distribution EVTSA9VEHNZVH).
- Bucket policy on `opal-data-portal-v2` has `AllowCloudFrontOAI` statement granting any distribution using that OAI -- so E2LPCXXBLDGWXY's Origin 1 can read.
- But: no portal code calls `ddekdm5vg1xns.cloudfront.net/market-metrics.json`.

### 4. Portal reads the same artifact via the portal CF distribution

```
portal/src/api/endpoints/market-precomputed.ts:143
  apiRequest<AllReturnsResponse>('/api/general/market/market-metrics.json')
```
This resolves to `opalinvest.dev/api/general/market/market-metrics.json` → portal CF distribution (EVTSA9VEHNZVH) → `/api/general/*` behavior → `S3-opal-data-portal-v2-json` origin → `opal-data-portal-v2/json/market/market-metrics.json`. Bypasses E2LPCXXBLDGWXY entirely.

### 5. Only infrastructure invalidators reference the CDN

Grep of E2LPCXXBLDGWXY / ddekdm5vg1xns outside docs/manifests:
- `infra/aws/lambda/precompute_market_metrics/index.js` — probably invalidates on publish
- `infra/aws/lambda/v2_portal/yang_pipeline/outputs/invalidate-cloudfront/lambda_function.py` — invalidation Lambda
- IAM grant (now managed in `market-overview/iam.tf` via `aws_cloudfront_distribution.market_metrics.arn` reference after CDRS_TFIMPT.004)

Nothing in portal `src/` references the CDN endpoint.

---

## Conclusion

**Orphaned.** The CDN was likely an earlier serving path for market-metrics that got superseded by the `/api/general/*` route on the portal distribution. It was left running (costs ~nothing at zero requests) and its invalidation hooks were kept for hypothetical path revival.

---

## Options

### A) Decommission (recommended)

1. `aws cloudfront get-distribution-config --id E2LPCXXBLDGWXY` → `Enabled: false`, `update-distribution` with `--if-match <ETag>`
2. Wait ~15 min for "Deployed" status (CF propagation)
3. `delete-distribution --id E2LPCXXBLDGWXY --if-match <ETag>`
4. Remove from `infra/aws/terraform/market-overview/cloudfront-market-metrics.tf` + state
5. Remove IAM grant in `market-overview/iam.tf` (no more distribution to invalidate)
6. Remove invalidation calls in precompute-market-metrics Lambda
7. Tag `market-overview-v{next}` minor bump
8. Update audit doc section 6 counts

Removes an unused public-facing surface. Saves nothing on AWS bill but simplifies the mental model.

### B) Fix the broken default origin

Add `aws_s3_bucket_policy.market_data_v2` granting OAC principal GetItem on `opal-market-data-v2/metrics/*`. Then decide if we're going to populate `/metrics/` with actual content. Otherwise we've just fixed a working-but-dead path.

Only pursue if someone intends to re-enable the CDN as a serving path.

### C) Leave as-is

Document the state. No functional impact today. But the 403-at-origin default behavior is noise that future AE work will rediscover and re-investigate.

---

## Recommendation

**Option A (decommission).** Orphaned infra is technical debt. Zero traffic + clear-alternate-path + doubly-broken-default makes this a clean cleanup.

**Not executing without COO go-ahead** — `Enabled: false` on a CF distribution, even an unused one, is a customer-visible state change by convention.

---

## Next

- MCP COO with findings + Option A recommendation
- If approved: execute the 7-step decommission, single commit, tag
- If B or C: document accordingly

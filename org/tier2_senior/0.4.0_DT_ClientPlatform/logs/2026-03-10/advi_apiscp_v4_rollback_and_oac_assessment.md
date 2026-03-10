# ADVI_APISCP v4 Rollback + OAC/Lambda@Edge Architecture Assessment — 0.4.0_DT_ClientPlatform

**Date:** 2026-03-10
**Start Time:** ~20:15 UTC

## Objective

Roll back `shared-advisor-router:4` to `:3` (service restoration), document root cause of
the OAC signing break, and assess viable fix options for multi-tenant routing.

---

## Deployment Sequence — Rollback

| Step | Action | Result |
|------|--------|--------|
| 1 | `aws cloudfront get-distribution-config` | ETag: `E24N0N72JGXIFH` |
| 2 | Patch behavior index 4: `shared-advisor-router:4` → `:3` | Verified in patched JSON |
| 3 | `aws cloudfront update-distribution` | Status: InProgress, LastModified: 2026-03-10T20:17:59Z |
| 4 | `aws cloudfront create-invalidation /api/scoped/advisor-intelligence/*` | ID: `I3Y4DVA8KISNS65Z53HWSIPH8I` |

**Propagation:** ~5-15 min from 20:17 UTC. v3 will restore normal service on propagation.

---

## Root Cause — Why v4 Broke OAC Signing

**DE diagnosis confirmed.** This is an AWS CloudFront constraint, not a code bug.

**The constraint:**
> When a Lambda@Edge origin-request function modifies `request.origin` in any way,
> CloudFront skips OAC (Origin Access Control) signing for the outbound request to S3.
> S3 receives an unsigned request, which the bucket policy (`AllowCloudFrontOACReadGold`)
> rejects with 403. CloudFront's `403 → 200 /index.html` error response masked this.

**v3 was unaffected** because it only rewrote `request.uri`. It never touched `request.origin`,
so CloudFront applied OAC signing to the statically configured `S3-opal-data-bd` origin normally.

**My error:** The ADVI_APISCP-001 thread correctly identified OAC vs OAI as an unknown, but
neither CloudOps nor I had live AWS CLI access during the thread to confirm whether dynamic
origin mutation is compatible with OAC. AWS documentation is ambiguous on this point. Live
verification caught it.

---

## Architecture Assessment — Fix Options for Multi-Tenant Routing

### Option A — Skip origin mutation when firmId = bd (band-aid)

**How:** In v4 code, only mutate `request.origin` when `firmId !== 'bd'`. For the current
single-tenant case (49 Financial), this is a no-op and OAC signing applies normally.

**Problem:** This is not a multi-tenant solution. firmId=`partner2` would still break OAC.
Only defers the problem.

**Verdict:** Reject. Solves today but not the architecture.

---

### Option B — Switch S3-opal-data-bd origin from OAC to OAI

**How:** Create a new OAI for the advisor-intelligence behavior (or reuse `EU39UXW7CMSI5`
already on `S3-opalinvest-portal`). Update `S3-opal-data-bd` origin in the distribution to
use OAI instead of OAC. Update `opal-data-bd` bucket policy to allow OAI principal.
Lambda@Edge can freely mutate `request.origin.s3` — OAI signing IS compatible with dynamic
origin mutation.

**Partner bucket policy template (OAI):**
```json
{
  "Principal": {
    "CanonicalUser": "<OAI canonical user ID>"
  },
  "Action": "s3:GetObject",
  "Resource": "arn:aws:s3:::opal-data-{firmId}/*"
}
```

**Pros:**
- Lambda@Edge dynamic origin mutation works with OAI (AWS-confirmed)
- Zero operational overhead per new firm — just create the bucket with OAI policy
- Simpler onboarding

**Cons:**
- OAI is "legacy" — AWS deprecated OAI in favor of OAC in 2022, though no end-of-life date set
- `S3-opalinvest-portal` already uses OAI (EU39UXW7CMSI5) — we'd create a second OAI
  or reuse the existing one (not recommended to mix purposes)
- Mixed auth model on the distribution (some origins OAC, one OAI)

**Verdict:** Viable for multi-tenant. Not ideal long-term given OAI deprecation trajectory.

---

### Option C — Pre-configure one CloudFront origin per firm (Option D from DE escalation)

**How:** For each `opal-data-{firmId}`, add it as a named S3 origin in the CloudFront
distribution with OAC attached. Lambda@Edge reads X-Firm-Id and sets `request.origin` to
the exact configuration of the matching pre-configured origin.

**Key question:** Does this actually restore OAC signing?

Based on AWS documentation review: CloudFront applies OAC signing when the outbound S3
request matches a distribution-configured origin **and** the origin has OAC configured.
When Lambda@Edge sets `request.origin` to a domain that IS configured in the distribution
with OAC, OAC signing SHOULD apply. This needs live verification.

**Lambda@Edge approach:**
```javascript
const FIRM_ORIGINS = {
  'bd':    { domainName: 'opal-data-bd.s3.us-east-1.amazonaws.com',    region: 'us-east-1' },
  'firm2': { domainName: 'opal-data-firm2.s3.us-east-1.amazonaws.com', region: 'us-east-1' },
};
// Only mutate if we can match to a configured origin
const origin = FIRM_ORIGINS[firmId];
if (!origin) { return 403; }
request.origin.s3.domainName = origin.domainName;
request.origin.s3.region     = origin.region;
request.headers['host'] = [{ key: 'Host', value: origin.domainName }];
```

**Pros:**
- Preserves OAC (current best practice)
- Clean per-firm isolation — each origin independently configured
- No deprecated API

**Cons:**
- CloudFront distribution update required per new firm onboarding (terraform/CLI change)
- Unverified whether setting origin to a configured domain actually restores OAC signing
  — **must be tested before commit**

**Verdict:** Preferred long-term architecture IF AWS confirms OAC signing applies when the
mutated domain matches a distribution-configured origin. Requires a live test.

---

### Option D — Lambda@Edge fetches from S3 directly (SigV4 in Lambda)

**How:** Lambda@Edge makes an authenticated `GetObject` call to S3 using the execution role
credentials (SigV4), returns the body as the response. Bypasses CloudFront origin auth entirely.

**Cons:**
- Lambda@Edge 1MB response size limit (gold files up to ~55KB each — currently OK, not future-proof)
- Added latency (~20-50ms S3 SDK call inside Lambda@Edge execution)
- Lambda@Edge execution role needs `s3:GetObject` on `opal-data-*`
- No CloudFront caching of the response (defeats the purpose of CloudFront for static JSON)

**Verdict:** Last resort. Too many trade-offs.

---

## DT Recommendation

**Immediate:** v3 rollback (done above) — service restored.

**Fix path — bring to Andrew/CTO for decision:**

1. **Try Option C first (pre-configured origins per firm + OAC).** Add `opal-data-bd` as
   an explicitly named OAC origin (it already exists as `S3-opal-data-bd` with OAC — this IS
   the current config). The open question is whether Lambda@Edge mutating `request.origin.s3`
   to match that exact configured domain restores OAC. This requires a **live test** against
   the actual distribution — not resolvable from docs alone.

2. **If Option C live test fails, adopt Option B (OAI).** OAI works with Lambda@Edge dynamic
   origin mutation (AWS-confirmed). The deprecation risk is low for a distribution we control.
   Onboarding is simpler (no distribution update per firm).

3. **Option A is not a path forward.** Do not merge a firmId=bd special-case.

---

## What I Need From Andrew Before Proceeding

1. **Decision on Option C vs B** — or authorization to test Option C live (requires a
   brief re-deploy of a test v4 variant to verify OAC signing behavior).
2. If Option C: confirm whether the test should modify the existing distribution or a
   separate test distribution.
3. If Option B: confirm whether to create a new OAI or reuse EU39UXW7CMSI5.

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| CloudFront EVTSA9VEHNZVH | Behavior rolled back: `shared-advisor-router:4` → `:3` | AWS-live (no git artifact) |
| This session log | DT assessment | No — pending CLOUD commit |

---

## Current State

**Status:** IN PROGRESS (rollback propagating, architecture decision pending)
**Active branch:** CLOUD

CloudFront rollback to `shared-advisor-router:3` is in progress (InProgress as of 20:17 UTC).
v3 will restore normal 49 Financial service on propagation. v4 (`4eff8dee`) remains on CLOUD
branch but is NOT deployed. Architecture decision on OAC vs OAI vs pre-configured origins
required from Andrew before v4 fix can be designed and re-deployed.

---

## Next Steps

1. **[Andrew] Decide on fix architecture** — Option B (OAI) vs Option C (pre-configured
   OAC origins + live test). DT cannot proceed without this decision.
2. **[0.4.0_DT_ClientPlatform] Implement chosen fix** — once decision is made.
3. **[0.4.0_DE_ClientPlatform] Re-run verification** after fix deploy.

**Do NOT:**
- Re-deploy v4 as written — it will break OAC signing again
- Use Option A (firmId=bd skip) — not a multi-tenant solution
- Disable CloudFront 403 error responses as a debugging aid without Andrew approval

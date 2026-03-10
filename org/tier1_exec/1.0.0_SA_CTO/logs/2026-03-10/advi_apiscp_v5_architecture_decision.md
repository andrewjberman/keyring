# ADVI_APISCP v5 Architecture Decision — 1.0.0_SA_CTO

**Date:** 2026-03-10

## Objective

Resolve the ADVI_APISCP v4 OAC signing failure. Choose between Option B (OAI migration)
and Option A/C (pre-configured OAC origins per firm, live test first). Issue task orders
to unblock v5 deployment. Additionally: identify and close a compliance gap in the v4 spec
that was not caught in Phases 1-2 — cache key does not vary by firm identity.

---

## What I Received

- **COO brief:** `org/tier1_exec/1.0.0_SA_CTO/task_orders/ADVI_APISCP.v5-oac-dynamic-origin-brief.md`
- **DT rollback log:** `org/tier2_senior/0.4.0_DT_ClientPlatform/logs/2026-03-10/advi_apiscp_v4_rollback_and_oac_assessment.md`

v4 (`shared-advisor-router:4`, commit `4eff8dee`) is rolled back to `:3`. Service restored.
Both the COO and DT submitted good assessments. My role is to resolve the remaining
ambiguity and close the decision.

---

## The Option A/C Live Test Is Already Done

The DT flagged Option A/C (pre-configured OAC origins per firm) as "needs a live test —
unconfirmed whether matching a configured domain restores OAC signing." I am closing this
option without a further test. Here is why:

**v4 was the live test.** The `S3-opal-data-bd` origin is already configured in the
distribution with OAC attached. v4 set `request.origin.s3.domainName` to
`opal-data-bd.s3.us-east-1.amazonaws.com` — the EXACT domain of that declared origin.
OAC signing was still bypassed. The 403 from S3 confirms it.

The DT hypothesized that setting `authMethod: 'origin-access-identity'` in the runtime
object may have been the confounding variable — that Option A/C would have worked if v4
had not also set that field. I disagree. AWS CloudFront computes OAC signing from the
**distribution-level origin record**, not from any field on the runtime `request.origin`
object. The `authMethod` field on the runtime object is read by CloudFront to determine
which signing model the Lambda@Edge is requesting for this specific request — but OAC
signing is computed before the outbound request is forwarded, and any mutation to
`request.origin` disqualifies the request from OAC signing entirely. The auth method on
the runtime object cannot restore what the mutation invalidated.

**The fundamental reason OAI works and OAC cannot work for this pattern:**

OAI is a **principal identity**. When CloudFront has an OAI configured for a behavior,
every request from that behavior is signed as the OAI canonical user, regardless of
which S3 domain the Lambda@Edge routes it to. The target bucket only needs a bucket
policy that grants `s3:GetObject` to that OAI canonical user. Dynamic origin mutation
is fully compatible because the signing identity is attached to the behavior, not the
domain endpoint.

OAC is **distribution-level SigV4 per declared endpoint**. The signature is computed
for a specific S3 endpoint that is declared in the distribution configuration. Any domain
mutation invalidates the signature computation, because CloudFront cannot pre-sign for
an endpoint it does not control at distribution config time.

Multi-tenant dynamic routing with per-firm S3 buckets is **architecturally incompatible
with OAC**. This is not a code issue or a configuration detail — it is a structural
property of how OAC works.

---

## Decision: Option B — OAI Migration

**Choosing Option B. No live test of Option A/C. No presigned URLs (Option C/COO).**

### Rationale

1. **OAI is confirmed compatible with Lambda@Edge dynamic origin mutation.** AWS
   documentation explicitly supports this: when `request.origin.s3.authMethod` is set
   to `'origin-access-identity'`, CloudFront signs the request as the OAI principal
   configured on the behavior's base origin. The target bucket accepts the OAI principal
   via its bucket policy. This is the intended pattern for dynamic multi-origin routing.

2. **The v4 code is already correct.** `shared-advisor-router:4` uses
   `authMethod: 'origin-access-identity'`. No Lambda@Edge code changes are needed.
   v5 is a CloudFront + IAM reconfiguration, not a firmware update.

3. **Onboarding stays zero-touch.** With Option B, adding a new partner requires:
   - Create `opal-data-{firmId}` S3 bucket
   - Apply bucket policy granting OAI principal `s3:GetObject` on that bucket
   - No CloudFront distribution changes. No code changes. No DT involvement per onboarding.
   This is the model the PRD was designed for.

4. **Option A/C fails the onboarding scalability test anyway.** Even if Option A/C
   could preserve OAC signing (which I do not believe it can), each new partner would
   require a CloudFront distribution update to add a new named origin. The distribution
   has a 25-origin limit and is not in Terraform. A DT distribution change per partner
   onboarding is an operational anti-pattern for a compliance-critical system.

5. **OAI deprecation risk is acceptable.** AWS deprecated OAI in 2022. No EOL date
   has been announced in the 3+ years since. This distribution already uses OAI
   (EU39UXW7CMSI5 on S3-opalinvest-portal). We are not creating a new distribution with
   OAI — we are adding a second OAI to an existing mixed-auth distribution, which is a
   valid AWS configuration. We create a dedicated OAI for the scoped advisor behavior
   so it is independently manageable. At partner 2 onboarding, if AWS has produced a
   better OAC + dynamic routing story (e.g., CloudFront KeyValueStore, or Continuous
   Deployment for zero-downtime origin adds), we revisit. Until then, OAI is correct.

### What I Am Explicitly Rejecting

- **Option A/C live test on production.** Unnecessary. The outcome is known from v4.
  Even if it worked, the operational model is wrong.
- **Option C/COO (presigned URLs).** Kills edge caching, exposes bucket topology,
  adds a redirect round-trip. Rejected.
- **Option A/DT (firmId=bd skip).** Not a multi-tenant solution. Rejected.

---

## New Requirement I Am Adding: Cache Key Must Vary by X-Firm-Id

**This was not in the v4 spec. It is a compliance requirement for v5.**

CloudFront caches are edge-wide and shared across all users hitting the same PoP.
With the current cache policy (path-based only), two users from different firms hitting
the same edge node for the same path (e.g.,
`/api/scoped/advisor-intelligence/clients_tab.json`) would share a cache entry. Firm A's
data could be served to firm B. This is a compliance violation under the partner data
isolation invariant in Section 2 of the PRD.

The fix: add `X-Firm-Id` to the CloudFront cache policy for the
`/api/scoped/advisor-intelligence/*` behavior.

`auth-validator-edge` (viewer-request) already injects `X-Firm-Id` from the validated
JWT before the cache check. CloudFront will vary the cache by `X-Firm-Id` value,
creating separate cache namespaces per firm. Firm A and firm B get independent cache
entries for the same path. This is the correct behavior.

**This must ship with v5, not as a follow-up.**

---

## Task Orders Dispatched

### 1. CloudOps — Create OAI and Bucket Policy

**File:** `org/tier2_senior/0.7.0_AE_CloudOps/task_orders/ADVI_APISCP.003.oai-setup-bucket-policy.md`

Deliverables: new OAI (ID + canonical user ID) and bucket policy applied to `opal-data-bd`.
DT is blocked on this.

### 2. DT — CloudFront OAI Wiring + Cache Key + v5 Deploy

**File:** `org/tier2_senior/0.4.0_DT_ClientPlatform/task_orders/ADVI_APISCP.003.cloudfront-oai-cache-key-v5.md`

Depends on CloudOps delivering the OAI canonical user ID.
Deliverables: `S3-opal-data-bd` origin migrated to OAI, cache policy updated with X-Firm-Id,
`shared-advisor-router:5` deployed and verified, cache invalidated, tagged.

### Execution dependency

```
[CloudOps: Create OAI opal-scoped-advisor-oai + apply bucket policy to opal-data-bd]
                        |
                        | delivers: OAI ID + canonical user ID
                        v
[DT: Update CloudFront origin S3-opal-data-bd (OAC -> OAI)
     + Update cache policy (add X-Firm-Id)
     + Deploy shared-advisor-router:5 (v4 code unchanged)
     + Invalidate /api/scoped/advisor-intelligence/*
     + Tag shared-advisor-router-v5]
```

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Option B (OAI), no live test of Option A/C | v4 WAS the live test. OAC is architecturally incompatible with dynamic origin mutation. Option A/C fails onboarding scalability even if it worked. |
| Dedicated OAI `opal-scoped-advisor-oai` (do not reuse EU39UXW7CMSI5) | Separate concerns — portal-v2 OAI and scoped-advisor OAI should be independently manageable. Mixing would couple their permissions and complicate future migration. |
| Cache key must vary by X-Firm-Id (ships with v5) | Compliance requirement. Cross-firm cache contamination violates partner data isolation invariant. Cannot defer. |
| No code change to `shared-advisor-router` (v4 code = v5 code) | v4 Lambda code was correct. `authMethod: 'origin-access-identity'` is right. Only CloudFront + IAM config was wrong. Deploy as :5 for audit clarity. |
| Revisit Option A at partner 2 onboarding | If AWS has a better OAC + dynamic routing solution by then, evaluate it. Do not block current deployment on that evaluation. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/tier1_exec/1.0.0_SA_CTO/logs/2026-03-10/advi_apiscp_v5_architecture_decision.md` | This log | No |
| `org/tier2_senior/0.7.0_AE_CloudOps/task_orders/ADVI_APISCP.003.oai-setup-bucket-policy.md` | New task order | No |
| `org/tier2_senior/0.4.0_DT_ClientPlatform/task_orders/ADVI_APISCP.003.cloudfront-oai-cache-key-v5.md` | New task order | No |
| `docs/architecture/ADVI_APISCP_PRD.md` | Add Section 11: v5 architecture notes (OAI decision, cache key requirement, onboarding protocol) | No |
| `org/projects/ADVI_APISCP.json` | Update phase + blocking | No |

---

## Blockers

None from my end. Both task orders are dispatched. CloudOps unblocks DT.

---

## Current State

**Status:** COMPLETE (CTO scope)
**Active branch:** CLOUD

Architecture decision closed. Option B (OAI) selected. The Option A/C live test is
unnecessary and explicitly rejected — v4 already provided the answer. Cache key
compliance gap identified and added as a mandatory v5 requirement. Two task orders
dispatched (CloudOps .003 and DT .003). DT is blocked on CloudOps OAI delivery.
v3 is live and 49 Financial is served correctly while v5 is prepared.

---

## Next Steps

1. **[0.7.0_AE_CloudOps] Execute ADVI_APISCP.003** — create OAI, apply bucket policy,
   deliver OAI ID + canonical user ID to DT
2. **[0.4.0_DT_ClientPlatform] Execute ADVI_APISCP.003** (blocked on CloudOps) — wire
   OAI into CloudFront, update cache policy, deploy :5, verify, tag
3. **[0.4.0_DE_ClientPlatform] Re-run post-deploy verification** — after DT completes,
   confirm `/api/scoped/advisor-intelligence/*` returns 200 JSON with current gold date
4. **[1.0.0_SA_CTO] Update onboarding checklist reference** — at partner 2 onboarding,
   ensure the PartnerETL onboarding checklist includes the OAI bucket policy step
   (CloudOps must know to add it per partner)

**Do NOT:**
- Deploy Option A/C (pre-configured OAC origins) — rejected, do not test on production
- Reuse EU39UXW7CMSI5 OAI for the scoped advisor behavior — create a dedicated OAI
- Deploy v5 before CloudOps delivers the OAI canonical user ID — DT dependency is hard
- Skip the X-Firm-Id cache key update — it is a compliance requirement, not optional

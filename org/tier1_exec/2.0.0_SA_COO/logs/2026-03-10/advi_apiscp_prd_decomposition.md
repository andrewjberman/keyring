# ADVI_APISCP PRD Decomposition — 2.0.0_SA_COO

**Date:** 2026-03-10

## Objective

Decompose the CTO's ADVI_APISCP PRD (Scoped API Multi-Partner Routing Architecture) into
task orders. The PRD establishes the canonical multi-tenant serving architecture for
/api/scoped/advisor-intelligence/* routes, replacing the hardcoded opal-data-bd origin in
shared-advisor-router Lambda@Edge with dynamic per-firm routing using X-Firm-Id from JWT.

---

## Work Completed

### 1. PRD Review and Pre-Flight Audit

Verified all source files referenced in the PRD:
- `infra/aws/lambda-edge/shared-advisor-router/index.mjs` — EXISTS, confirmed v3 (URI rewrite only, no origin mutation)
- `infra/aws/lambda-edge/auth-validator-edge/index.mjs` — EXISTS
- `portal/src/api/endpoint-mapping.ts` — EXISTS, confirmed stale SCOPED comment (line 13 says opal-data-portal-v2)
- `portal/src/api/endpoints/advisor-intelligence.ts` — EXISTS

**Critical finding:** CloudFront distribution EVTSA9VEHNZVH is NOT managed in Terraform.
Lambda@Edge functions are NOT in lambda-source-map.json. The Lambda@Edge deployment
mechanism is separate from the standard Terraform Lambda pipeline. Flagged in DT task order.

### 2. Thread Orchestration Decision (REVISED)

**Initial decision: No alignment thread needed.** Rationale:
- No DS→DE→RD interface boundary (no data contract negotiation needed)
- PRD includes pseudocode for v4 implementation
- Work streams are independent

**Correction: Pattern 2 thread was needed.** Andrew challenged the decision — the PRD
contains pseudocode that was never verified against the actual infrastructure. Three
critical assumptions were unverified:
1. Lambda@Edge deployment mechanism (not in Terraform or source map)
2. CloudFront origin-request event shape for dynamic origin mutation
3. OAI policy scope (wildcarded or per-bucket?)

**Thread ADVI_APISCP-001 ran** (Pattern 2, DT + CloudOps, 3 turns each). Findings below.

### 2b. Thread ADVI_APISCP-001 Findings

**Thread:** ADVI_APISCP-001-lambda-edge-cloudfront-investigation
**Participants:** 0.7.0_AE_CloudOps (source), 0.4.0_DT_ClientPlatform (receiver)
**Status:** COMPLETE (both agents converged)

**Finding 1 — Lambda@Edge deployment is unmanaged:**
- NOT in Terraform, NOT in lambda-source-map.json, no deploy script found in repo
- Must be discovered via AWS CLI before implementation
- Hard blocker: `aws cloudfront get-distribution-config --id EVTSA9VEHNZVH`

**Finding 2 — PRD OAI assumption may be WRONG:**
- Environment has evidence of OAC (Origin Access Control, ID E24L6358YRRKAE)
- PRD pseudocode uses `authMethod: "origin-access-identity"` (OAI) — not safe to assume
- DT must confirm OAC vs OAI from CloudFront config before implementing

**Finding 3 — S3 access is per-bucket (no wildcard):**
- S3 module grants CloudFront access per-bucket: `"${aws_s3_bucket.this.arn}/*"`
- PRD claim "no IAM changes needed (wildcard opal-data-* already grants access)" is INCORRECT
- Each new opal-data-{firmId} bucket needs explicit CloudFront access policy

**Actions taken:**
- DT task order REVISED with mandatory Preflight section (requirements 0a-0c)
- PartnerETL onboarding checklist requirement updated to include CloudFront bucket policy step
- Project phase updated to Phase 1b

### 3. Task Order Dispatch (initial issuance + post-thread revision)

| Agent | Task Order Path | Summary |
|-------|----------------|---------|
| 0.4.0_DT_ClientPlatform | org/tier2_senior/0.4.0_DT_ClientPlatform/task_orders/ADVI_APISCP.001.lambda-edge-v4-dynamic-routing.md | (REVISED per ADVI_APISCP-001) Lambda@Edge v4 dynamic origin routing. Mandatory preflight AWS discovery (0a-0c) before implementation. Must confirm OAC vs OAI, discover deploy mechanism. |
| 0.4.0_DE_ClientPlatform | org/tier2_senior/0.4.0_DE_ClientPlatform/task_orders/ADVI_APISCP.001.endpoint-mapping-docs-audit.md | Fix SCOPED comment in endpoint-mapping.ts, audit frontend API calls, post-deploy network tab verification. |
| 0.6.0_AE_PartnerETL | org/tier2_senior/0.6.0_AE_PartnerETL/task_orders/ADVI_APISCP.001.bd-pipeline-output-audit-onboarding.md | (REVISED) Audit bd-pipeline gold output paths, write partner onboarding checklist (now includes CloudFront bucket policy step). |
| 0.5.0_AE_OpalETL | org/tier2_senior/0.5.0_AE_OpalETL/task_orders/ADVI_APISCP.001.opal-pipeline-bucket-audit.md | Audit yang/news/market publisher output paths, confirm opal-data-portal-v2 only, document bucket separation in pipeline_inventory.xml. |

### Execution Dependencies

```
  [DT: Preflight AWS discovery (0a-0c)]
                |
                v
  [DT: Lambda@Edge v4 implement + deploy]
                |
                v
  [DE: Post-deploy network tab verification (req 4)]

  [AE PartnerETL: bd-pipeline audit + onboarding checklist]  (parallel, no blocking)
  [AE OpalETL: yang/news/market bucket audit]                 (parallel, no blocking)
```

DT preflight is the critical path. DE reqs 1-3 can start immediately; req 4 waits for DT deploy. Both AE audits run in parallel with no dependencies.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| No Pattern 0 thread | No DS→DE→RD interface boundary; PRD is implementation-ready |
| ~~No Pattern 2 thread~~ REVERSED | PRD pseudocode was unverified. Thread ADVI_APISCP-001 ran and found 3 corrections. |
| Flag Lambda@Edge deployment model in DT task order | CloudFront/Lambda@Edge not in Terraform; DT must discover deployment mechanism |
| AE audits run in parallel | No cross-dependency between PartnerETL and OpalETL work |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| org/tier2_senior/0.4.0_DT_ClientPlatform/task_orders/ADVI_APISCP.001.lambda-edge-v4-dynamic-routing.md | DT task order | No |
| org/tier2_senior/0.4.0_DE_ClientPlatform/task_orders/ADVI_APISCP.001.endpoint-mapping-docs-audit.md | DE task order | No |
| org/tier2_senior/0.6.0_AE_PartnerETL/task_orders/ADVI_APISCP.001.bd-pipeline-output-audit-onboarding.md | AE PartnerETL task order | No |
| org/tier2_senior/0.5.0_AE_OpalETL/task_orders/ADVI_APISCP.001.opal-pipeline-bucket-audit.md | AE OpalETL task order | No |
| org/projects/ADVI_APISCP.json | Phase updated to Phase 1b (post-thread) | No |
| org/threads/staging/run-ADVI_APISCP-001-lambda-edge-cloudfront-investigation.sh | Thread staging script | No |
| org/threads/ADVI_APISCP-001-lambda-edge-cloudfront-investigation/ | Thread folder (7 messages, complete) | No |
| org/tier2_senior/0.4.0_DT_ClientPlatform/threads/ADVI_APISCP-001-...CloudOps.md | DT receipt | No |
| org/tier2_senior/0.7.0_AE_CloudOps/threads/ADVI_APISCP-001-...DT.md | CloudOps receipt | No |
| This file | Session log (updated with thread findings) | No |

---

## Blockers

None.

---

## Current State

**Status:** COMPLETE (COO orchestration done; agents ready to execute)
**Active branch:** CLOUD

Four task orders issued + one Pattern 2 thread completed. DT task order revised with
mandatory AWS preflight discovery gate. Three PRD assumptions corrected. AE audits
can proceed in parallel.

---

## Next Steps

1. **[0.4.0_DT_ClientPlatform] Preflight AWS discovery** (BLOCKING) — run `aws cloudfront get-distribution-config`, determine OAC vs OAI, discover Lambda@Edge deployment mechanism. Then implement v4.
2. **[0.6.0_AE_PartnerETL] Audit bd-pipeline** — confirm output paths, write onboarding checklist (now includes CloudFront bucket policy step)
3. **[0.5.0_AE_OpalETL] Audit Opal pipelines** — confirm no overlap with partner bucket pattern
4. **[0.4.0_DE_ClientPlatform] Fix endpoint-mapping.ts + post-deploy verify** — reqs 1-3 immediate, req 4 after DT

**Do NOT:**
- Write to opal-data-portal-v2 for any advisor-intelligence path — permanently forbidden
- Assume OAI — may be OAC; thread ADVI_APISCP-001 found evidence of OAC in this environment
- Assume wildcard S3 access — access is per-bucket, onboarding requires explicit policy

---

## Commits

### Commit: `org(2.0.0_SA_COO): ADVI_APISCP -- PRD decomposition, Pattern 2 thread, revised task orders`

| File | Description |
|------|-------------|
| `org/projects/ADVI_APISCP.json` | Project registration + phase update to 1b |
| `org/threads/staging/run-ADVI_APISCP-001-lambda-edge-cloudfront-investigation.sh` | Pattern 2 thread staging script |
| `org/threads/ADVI_APISCP-001-lambda-edge-cloudfront-investigation/` | Thread folder (7 messages, context, complete) |
| `org/tier1_exec/2.0.0_SA_COO/logs/2026-03-10/advi_apiscp_prd_decomposition.md` | This session log |
| `org/tier2_senior/0.4.0_DT_ClientPlatform/task_orders/ADVI_APISCP.001.lambda-edge-v4-dynamic-routing.md` | DT task order (REVISED): mandatory preflight AWS discovery, OAC/OAI conditional, per-bucket access |
| `org/tier2_senior/0.4.0_DE_ClientPlatform/task_orders/ADVI_APISCP.001.endpoint-mapping-docs-audit.md` | DE task order: fix SCOPED comment, audit frontend, post-deploy verify |
| `org/tier2_senior/0.6.0_AE_PartnerETL/task_orders/ADVI_APISCP.001.bd-pipeline-output-audit-onboarding.md` | AE PartnerETL task order (REVISED): onboarding checklist now includes CloudFront bucket policy step |
| `org/tier2_senior/0.4.0_DT_ClientPlatform/threads/ADVI_APISCP-001-..._0.7.0_AE_CloudOps.md` | DT thread receipt |
| `org/tier2_senior/0.7.0_AE_CloudOps/threads/ADVI_APISCP-001-..._0.4.0_DT_ClientPlatform.md` | CloudOps thread receipt |

### Commit: `org(2.0.0_SA_COO): COO README update -- mandatory dispatch table in session logs`

| File | Description |
|------|-------------|
| `org/tier1_exec/2.0.0_SA_COO/README.md` | Added Task Order Dispatch Table mandate to COO protocol |
| `org/projects/REGISTRY.md` | Updated project registry (SNPLBK, APISCP, ADHC_GPTCST registrations; NNAVAR, AUAVAR moved to completed) |

---

## Phase 1 Delivery Validation

All four Phase 1 task orders validated as COMPLETE:

| Agent | Task Order | Status | Key Delivery |
|-------|-----------|--------|-------------|
| 0.4.0_DT_ClientPlatform | .001.lambda-edge-v4-dynamic-routing | COMPLETE | Preflight done (OAC confirmed). Lambda v4 deployed as :4. In-place domainName mutation. |
| 0.4.0_DE_ClientPlatform | .001.endpoint-mapping-docs-audit | COMPLETE | Reqs 1-3 done (portal commit 0a759de). Req 4 (post-deploy verify) deferred to Phase 2. |
| 0.5.0_AE_OpalETL | .001.opal-pipeline-bucket-audit | COMPLETE | All 3 Opal pipelines write only to portal-v2. Zero overlap with partner buckets. |
| 0.6.0_AE_PartnerETL | .001.bd-pipeline-output-audit-onboarding | COMPLETE | BD pipeline writes only to opal-data-bd/gold/. Onboarding checklist delivered. Stale IAM flagged. |

**Follow-up items surfaced by Phase 1:**
1. DE req 4 (post-deploy verification) was blocked on DT deploy -- now unblocked
2. Stale IAM: iam.tf:375 grants BD pipeline s3:PutObject on opal-data-portal-v2/* -- no active code uses this
3. DT did not tag the Lambda@Edge v4 deployment (commit 4eff8dee)

---

## Phase 2: Cleanup and Verification

### Phase 2 Task Order Dispatch

| Agent | Task Order Path | Summary |
|-------|----------------|---------|
| 0.4.0_DE_ClientPlatform | org/tier2_senior/0.4.0_DE_ClientPlatform/task_orders/ADVI_APISCP.002.post-deploy-verification.md | Post-deploy browser verification: confirm all scoped endpoints return 200 with current data, no portal-v2 hits. |
| 0.7.0_AE_CloudOps | org/tier2_senior/0.7.0_AE_CloudOps/task_orders/ADVI_APISCP.002.stale-iam-portal-v2-cleanup.md | Remove stale PortalBucketWrite IAM statement from bd-pipeline/iam.tf:371-376. Terraform apply + tag. |
| 0.4.0_DT_ClientPlatform | org/tier2_senior/0.4.0_DT_ClientPlatform/task_orders/ADVI_APISCP.002.lambda-edge-v4-tag.md | Tag Lambda@Edge v4 deployment: shared-advisor-router-v4 on commit 4eff8dee. |

### Phase 2 Execution Dependencies

```
  [DE: Post-deploy browser verification]     (immediate, no blockers)
  [DT: Tag Lambda@Edge v4 on 4eff8dee]       (immediate, no blockers)
  [CloudOps: Remove stale IAM + terraform]   (immediate, no blockers)
```

All three are independent and can run in parallel. No cross-dependencies.

---

## Phase 3 (v5): OAI Migration

### Context

v4 failed in production: CloudFront drops OAC signing when Lambda@Edge mutates
`request.origin`, causing unsigned S3 requests → 403 → masked as HTML by custom
error responses. v3 rolled back. CTO decision (commit 4387ec08): Option B — OAI.

OAI is a principal identity. CloudFront signs all origin-request outbound calls as
the OAI canonical user regardless of Lambda@Edge domain mutation. Per-bucket
`AllowCloudFrontOAI` bucket policy on each new partner bucket is the onboarding step.

New requirement added by CTO: X-Firm-Id in cache key. Mandatory compliance — prevents
cross-firm cache hits at shared edge PoPs.

### Phase 3 Task Order Dispatch

| Agent | Task Order Path | Summary |
|-------|----------------|---------|
| 0.7.0_AE_CloudOps | org/tier2_senior/0.7.0_AE_CloudOps/task_orders/ADVI_APISCP.003.oai-setup-bucket-policy.md | Create OAI opal-scoped-advisor-oai, apply bucket policy to opal-data-bd, deliver OAI ID + CanonicalUserId to DT via handoff note. |
| 0.4.0_DT_ClientPlatform | org/tier2_senior/0.4.0_DT_ClientPlatform/task_orders/ADVI_APISCP.003.cloudfront-oai-wire-v5-deploy.md | (BLOCKED on CloudOps) Wire OAI into CloudFront, add X-Firm-Id to cache key, publish :5, invalidate, verify, tag shared-advisor-router-v5. |

### Phase 3 Execution Dependencies

```
  [CloudOps: create OAI + apply opal-data-bd bucket policy]
                         |
         (handoff note delivered to DT task_orders/)
                         |
                         v
  [DT: wire OAI into CloudFront + X-Firm-Id cache key + publish :5 + verify + tag]
```

---

## Phase 4: CORS Fix

### Root Cause

Browser-visible failure: Advisor Intelligence page blank after v5 deploy.
S3 opal-data-bd has no CORS configuration. opal-data-portal-v2 had CORS (AllowedOrigins: *)
-- that config was never mirrored to opal-data-bd. Additionally, the CloudFront behavior
has no OriginRequestPolicyId, so the Origin header is not forwarded to S3, preventing
S3 from evaluating any CORS rules. Both gaps must be fixed together.

Curl tests (no browser) passed because curl does not enforce CORS. Browser fetches fail
because the response has no Access-Control-Allow-Origin header.

### Phase 4 Task Order Dispatch

| Agent | Task Order Path | Summary |
|-------|----------------|---------|
| 0.7.0_AE_CloudOps | org/tier2_senior/0.7.0_AE_CloudOps/task_orders/ADVI_APISCP.004.cors-opal-data-bd.md | Add S3 CORS config to opal-data-bd (mirror of portal-v2). Add CORS-S3Origin managed origin request policy to CF behavior. Invalidate. Verify Access-Control-Allow-Origin present in response. |

### Phase 4 Execution Dependencies

```
  [CloudOps: S3 CORS + CF origin request policy + invalidate + verify]
                         |
                         v
  [DE: re-run browser verification once CloudFront propagates]
```

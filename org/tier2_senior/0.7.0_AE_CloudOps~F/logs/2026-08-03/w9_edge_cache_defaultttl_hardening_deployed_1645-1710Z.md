# MDLP_MONPUB.W9: /api/general/* edge-cache DefaultTTL hardening -- DEPLOYED + verified

**archetype:** DEPLOY

**Serial:** `0.7.0_AE_CloudOps~F` -- Window: 2026-08-03T16:45Z-1710Z
**TO:** `org/tier2_senior/0.7.0_AE_CloudOps~F/task_orders/MDLP_MONPUB.W9.edge-cache-defaultttl-hardening.md`
(COO GO 164509Z on CTO dispatch 164247Z; Andrew-watched family)

---

## Summary

The /api/general/* CloudFront behavior ran Managed-CachingOptimized (DefaultTTL 86400); the
effective ~5-min TTL existed ONLY via the cache-control-injector Lambda@Edge stamping
max-age=300. W9 makes the config agree: a new TF-managed custom cache policy
`opal-api-general-5min-cache` (DefaultTTL 300 / MinTTL 0 / MaxTTL 31536000, cache-key params
identical to the managed policy) and a one-line swap of the behavior's `cache_policy_id`.
Applied, 0-diff verified, live-verified on both layers. The injector remains attached and
stamping -- its load-bearing status is removed, not the injector.

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Phase-1 grounding | comp-routes behaviors (25 enumerated) + live get-distribution-config: blast radius = 2 of 25 behaviors on Managed-CachingOptimized (`/api/general/*` + default `/*` SPA); policy IDs resolved live |
| 2 | TF authored | New `aws_cloudfront_cache_policy.opal_api_general_5min` in `cloudfront.tf` + swap at `cloudfront-distribution.tf` behavior 8; stale "console-managed" header comment corrected (distribution IS in TF state) |
| 3 | Plan (Phase-2 gate) | `1 to add, 1 to change, 0 to destroy` -- exactly the expected set; saved as w9.tfplan |
| 4 | Commit before apply | `04cd2f22f0` (safe-commit, -F message file) |
| 5 | W6 coordination | DT MCP'd pre-apply; DT CLEAR 165930Z (no W6 network exercise in flight) |
| 6 | safe-apply w9.tfplan | comp-tagauthz PASSED, tombstone-gate CLEAN; Apply complete: 1 added, 1 changed, 0 destroyed; new policy id `ce00305d-cc58-4b8d-b683-cd5914ded974`; distribution modification 49s |
| 7 | 0-diff re-plan | `No changes. Your infrastructure matches the configuration.` |
| 8 | Live verify (below) | PASS both layers, one named residual |
| 9 | Tag | `portal-auth-v1.21.0` annotated on 04cd2f22f0; push leg routed to MSTR (LANES COMMIT, INTEGRATORS PUSH) |

## Deployment Tags

| Pipeline | Tag | Commit |
|---|---|---|
| portal-auth | portal-auth-v1.21.0 | 04cd2f22f0 |

## Verification (actual output)

Config layer (live, post-apply):
```
$ aws cloudfront get-distribution-config --id EVTSA9VEHNZVH \
    --query "...Items[?PathPattern=='/api/general/*'].CachePolicyId"
[ "ce00305d-cc58-4b8d-b683-cd5914ded974" ]

$ aws cloudfront get-cache-policy --id ce00305d-...
{ "Name": "opal-api-general-5min-cache", "DefaultTTL": 300, "MinTTL": 0, "MaxTTL": 31536000 }

Default /* behavior CachePolicyId: 658327ea-f89d-4fab-a63d-7e88639e58f6  (Managed-CachingOptimized -- UNTOUCHED, deliberate)
Distribution status: Deployed
```

Behavior layer:
```
Lambda associations on /api/general/* (live): auth-validator-edge:18 (viewer-request),
  public-data-router:6 (origin-request), cache-control-injector:2 (origin-response) -- UNCHANGED
Injector stamp at source (index.mjs:13-15): "public, max-age=300, s-maxage=300"
Injector live invocation POST-APPLY: us-east-1 stream 2026/08/03/[2]00d664..., START/END/REPORT
  at 16:59:36Z (RequestId c147efda-...) -- attached AND firing on real traffic.
s-maxage=300 in the stamp directly bounds edge TTL; config DefaultTTL 300 now agrees.
```

**Named residual (honest scope of the behavioral claim):** an authenticated end-user GET showing
200 + Age cycling under 300s was NOT exercisable from this seat -- /api/general/* has no
unauthenticated path (measured: bare GET returns the validator's 401 `X-Cache:
LambdaGeneratedResponse`, which short-circuits before cache; OPTIONS returns 403
`Error from cloudfront`). Covered instead by: config DefaultTTL 300 (read live) + injector stamp
(source + live post-apply invocation). DT will capture response headers during the W6
deployed-page exercise, which closes this residual end-user-side (requested 170825Z).

## Compiler Tools

| Tool | Invocation | Result | vs TO <expect> |
|---|---|---|---|
| comp-routes behaviors | Phase 1 | PASS -- 25 behaviors enumerated incl. /api/general/* with its 3 L@E associations | PARTIAL vs expect: behavior enumerated, but comp-routes does NOT surface cache-policy identities -- TO's if_mismatch branch taken: grounded on `aws cloudfront get-distribution-config` (live). **Coverage gap recorded to CVO** (this log + close message): comp-routes models origins/behaviors/rewrites but not cache_policy_id. |
| comp-blast "/api/general/*" | Phase 1 | NOT-FOUND (denominator printed: 2254 nodes; endpoint-pattern not a graph node). Fallback: portal-src consumer enumeration -- 19 files (useDataFreshness, YangDataContext, ModelPortfolios.tsx, DataRefresh panels...) -- ALL freshness-sensitive, none depends on long caching | PASS on intent (consumer check); NOT-FOUND on the graph key itself |
| terraform plan (Phase-2 gate) | -out=w9.tfplan | PASS -- exactly 1 add + 1 change, zero other attributes | PASS |
| safe-apply + comp-tagauthz + tombstone-gate | Phase 3 | PASS (tagauthz PASSED, tombstone CLEAN, apply 1/1/0) | PASS |
| 0-diff re-plan | Phase 3 | PASS -- No changes | PASS |

What worked: the rail + gates did real work this session -- risk-reflex HOLD on
cloudfront-distribution.tf pointed at the Part-0 armed-hazard doc (MDPF_CONSOLIDATED_PLAN)
BEFORE apply; the saved plan itself then evidenced the hazard state resolved (repo/live agree at
24+1 behaviors; the 9-ahead flip is no longer pending in the tree -- had it been, the plan would
have shown it).
What failed: my first safe-apply ran under MSYS_NO_PATHCONV=1 -- the EXACT documented footgun
(CLAUDE.md Git section): it leaks into comp-tagauthz's python call, mangles the path to phantom
C:\c\..., gate fails CLOSED (rc=2 misreported as collision; actually could-not-evaluate).
Re-ran without the env var: gate PASSED. The gate's fail-closed behavior worked as designed;
my invocation was the defect.
Gap found: comp-routes cache-policy blindness (above, to CVO). Also comp-blast's graph has no
ENDPOINT node for /api/general/* path patterns (endpoint universe = 136 nodes; CF path patterns
are not keyed) -- lesser gap, same CVO note.

## MCP traffic

6 significant: COO GO ack; DT pre-apply coordination + DT CLEAR; DT Deployed-confirmation
(edge-state pin for W6); MSTR push-leg request (integrator discipline); close evidence to
COO + CTO (after this log commits, hash cited).

## Blockers

None. Push leg pending at MSTR (routed, not blocked -- ordinary integration).

## Current State (zero-context handoff)

- LIVE: /api/general/* on EVTSA9VEHNZVH runs policy ce00305d (DefaultTTL 300); injector attached
  + stamping; distribution Deployed; 0-diff.
- Repo: commits 99c3e50a36, 3b4ab65f37, 04cd2f22f0, + this log on local CLOUD; tag
  portal-auth-v1.21.0; ALL UNPUSHED pending MSTR integrator leg.
- Out of scope, flagged not touched: `opal-scoped-advisor-by-firm` policy also carries
  DefaultTTL 86400 on 5 advisor-intelligence S3 behaviors -- same latent class if their response
  path lacks a stamp; needs CTO scope-widening decision, not a lane self-select.
- w9.tfplan (consumed) + dist-config.json snapshot live in the session scratchpad; nothing
  stray in the repo tree.

## Next Steps

1. **[0.0.0_AB_MSTR]** Push leg: CLOUD + tag portal-auth-v1.21.0 (--follow-tags).
2. **[0.2.0_DT_PortfolioAnalytics]** W6 exercise headers close the Age<300 residual free.
3. **[1.0.0_SA_CTO]** Scope call on opal-scoped-advisor-by-firm's 86400 DefaultTTL (same class,
   5 behaviors, out of W9 scope).
4. **[3.0.0_SA_CVO]** comp-routes cache-policy coverage gap + comp-blast endpoint-pattern gap.

# Session Log: ADVI_PROFIL.004a -- advisor-id scoping edge Lambda

**Agent:** 0.7.0_AE_CloudOps
**Date:** 2026-04-10
**Project:** ADVI_PROFIL
**Task Order:** `org/tier2_senior/0.7.0_AE_CloudOps/task_orders/ADVI_PROFIL.004a.ae-advisor-id-scoping-edge.md`
**Coordinator:** 0.4.0_DT_ClientPlatform (DT authority, relayed Andrew auth)
**Trigger:** GO message `20260410T223238Z_0.4.0_DT_ClientPlatform_GO__ADVI_PROFIL.004a`
**Prior context:** `0.4.0_DT_ClientPlatform/logs/2026-04-10/advi_profil_002_claims.md` (JWT advisorId claim)

---

## TL;DR

Shipped advisor-id scoping as a viewer-request gate in `auth-validator-edge`. TO originally targeted `shared-advisor-router`; Phase 1 `comp-routes` audit caught that the router can only see one of the two required CloudFront behaviors, corrected to `auth-validator-edge` under DT coordinator authority. Semantics pivoted mid-session from Option 2 (`firmId === 'opal-capital'` bypass) to Option 3 (`role === 'admin'` bypass) after Andrew's direct correction. Two tags shipped: `portal-auth-v1.11.8` (source + source map) and `portal-auth-v1.11.9` (CloudFront distribution rewire).

---

## Problem

Enforce at the edge: non-admin partner users (Chase) cannot read another advisor's data by hitting `/.../advisor/{other_advisorId}/...` with their own JWT. Currently the backend (`opal-partners-data`) enforces firm membership but not advisor ownership within the firm. Two path patterns in scope:

1. `/api/scoped/partners/books/advisor/{advisorId}/platinum-summary` (API GW origin)
2. `/api/scoped/advisor-intelligence/platinum/advisors/{advisorId}/*.json` (S3-opal-data-bd origin)

---

## Phase 1 -- Compiler Audit

| Tool | Result |
|---|---|
| `comp-routes trace getPlatinumAdvisorSummary` | `/api/scoped/partners/*` -> `APIGateway-portal`, viewer JWT + API GW authorizer, used by AdvisorBookView + ClientsTab |
| `comp-routes trace getPlatinumAdvisorTimeseries` | `/api/scoped/advisor-intelligence/*.json` -> `S3-opal-data-bd` via `shared-advisor-router`, edge JWT only, used by AdvisorPublicProfile |
| `comp-routes trace getPlatinumAdvisorDrilldownSummary` | empty (same URL as getPlatinumAdvisorSummary; one rule covers both TS wrappers) |
| `comp-blast shared-advisor-router` | no downstream consumers (edge terminus) |
| File reads | `shared-advisor-router/index.mjs` (v10 live, firmId header-based rewrite only, no URL path matching), `auth-validator-edge/index.mjs` (viewer-request, verifies JWT with Secrets Manager, injects X-User-* headers but NOT X-Advisor-Id), `portal_authorizer/index.mjs:101` (decoded.advisorId is already in verified claim set end-to-end) |

### Architectural finding

**TO target `shared-advisor-router` is wrong.** Phase 1 established:

| Function | Event | Sees `/partners/*`? | Sees `/advisor-intelligence/*.json`? |
|---|---|---|---|
| `auth-validator-edge` | viewer-request | **YES** | **YES** |
| `shared-advisor-router` | origin-request (S3 behavior only) | no | yes |
| `tier-router-edge` | viewer-request | no-op for `/scoped/` | no-op for `/scoped/` |

`shared-advisor-router` is attached only to `/api/scoped/advisor-intelligence/*.json` as origin-request in `infra/aws/terraform/portal-auth/lambda-edge.tf`. It cannot see `/api/scoped/partners/*` traffic at all -- no single modification to that Lambda can enforce .004a across both required patterns.

`auth-validator-edge` runs at viewer-request on the distribution, universal. It already validates JWT via Secrets Manager and injects claim headers. True single choke point.

Escalation: messaged DT with three options (A=auth-validator-edge, B=extend shared-advisor-router behavior attachment, C=split across two functions). Recommended A. DT concurred as coordinator authority within ~3 minutes (`20260410T224010Z`). No COO or Andrew gate required -- scope correction, not architectural expansion.

### Firm-scoping verification (safety precondition for Option 3)

DT flagged the entire Option 3 admin-bypass model depends on `opal-partners-data` filtering BD reads by `jwt.firmId`. Verified:

- `infra/aws/users/lambda/portal-authorizer/index.mjs:125` `computeAllowedFirms(user)`:
  - `userType === 'Dev'` or `tier === 'internal'` -> `'ALL'`
  - `role === 'admin'` -> own firmId + all descendants (DynamoDB walk)
  - `role === 'user'` -> own firmId only
- `infra/aws/lambda/v2_portal/partners/lambdas/opal-partners-data/lambda_function.py:147` `is_authorized(firm_id, allowed_firms)`:
  - Rejects any query-param `firmId` not in `allowed_firms.split(',')` (line 161)
  - Line 1263: denies if `allowedFirmIds` is empty

Travis at 49financial hitting `/advisor/rj_advisor/...?firmId=raymond_james` gets 401 from the data layer. Travis at 49financial hitting `/advisor/chase_bertrand/...?firmId=49financial` gets 200 (firm matches, advisor is in the firm). Cross-firm containment holds. Option 3 is safe.

---

## Semantics flip mid-session (Option 2 -> Option 3)

First DT recommendation (~17:20 EDT): Option 2, `jwt.firmId === 'opal-capital'` bypass -- strict, partner-firm admins locked to their own advisorId.

Andrew direct correction (~17:35 EDT, quoted in DT message `20260410T224501Z`):
> "No travis should be able to click on any advisor card, or their bar in a chart element, or the leaderboard cards, and be taken to that advisors profile with full access. He is an Admin of 49. Chase however cannot do that."

Authorizes Option 3-simplified: `jwt.role === 'admin'` bypasses -- Opal staff AND partner-firm admins. Cross-firm containment preserved IMPLICITLY by X-Firm-Id injection + `opal-partners-data` firm-scoped queries (verified above).

**Pre-commit catch.** DT's URGENT flip arrived after I had written the Option 2 helper but BEFORE the first successful commit (the initial `git commit` calls both failed with a pathspec quirk -- root cause inconclusive, second attempt without pathspec succeeded). Single-line helper edit: `if (payload.firmId === "opal-capital")` -> `if (payload.role === "admin")`. Commented TODO for .004c extension path and future .007-Option-3 firm-peer broaden.

---

## Code: auth-validator-edge v10

File: `infra/aws/lambda-edge/auth-validator-edge/index.mjs`

```js
const ADVISOR_SCOPING_PATH_PATTERNS = [
  /^\/api\/scoped\/partners\/books\/advisor\/([^/]+)\/.*$/,
  /^\/api\/scoped\/advisor-intelligence\/platinum\/advisors\/([^/]+)\/.*\.json$/,
];

function matchAdvisorScopingPath(uri) {
  for (const re of ADVISOR_SCOPING_PATH_PATTERNS) {
    const m = uri.match(re);
    if (m) return m[1];
  }
  return null;
}

function getAllowedAdvisorIds(payload) {
  if (payload.role === "admin") return null;   // bypass Opal staff + partner-firm admins
  if (!payload.advisorId) return [];            // deny all
  return [payload.advisorId];                   // self only
}
```

Enforcement runs after JWT verify, before downstream forwarding. Strictly additive -- existing firmId/role injection unchanged. New `X-Advisor-Id` header injection parallel to `X-Firm-Id`.

Structured denial log shape:
```json
{
  "event": "advisor_scoping_denied",
  "rule": "004a",
  "userId": "payload.sub",
  "jwtAdvisor": "payload.advisorId",
  "jwtFirmId": "payload.firmId",
  "jwtRole": "payload.role",
  "requestedAdvisor": "path captured group",
  "path": "request.uri"
}
```

`rule: "004a"` so .004c CloudWatch filtering can distinguish when it ships.

---

## Deployment Sequence

| Step | Action | Result |
|---|---|---|
| 1 | Commit source + TO correction | `9208c784` feat(ADVI_PROFIL.004a): advisor-id scoping gate in auth-validator-edge (v10) |
| 2 | `build-nodejs-lambda.sh portal-auth auth-validator-edge` | FAIL -- openssl fopen `/tmp/...` no such file (with MSYS_NO_PATHCONV=1 set). SHA256 empty, source map corrupted. |
| 3 | Re-run build with `unset MSYS_NO_PATHCONV` | OK -- SHA256 `AsESuygxQAhRzh0eZ0jpoDRGfpO5WdW3DPnLmcZptdk=`, 60.32KB bundle, 20KB zip |
| 4 | Commit source map | `be25dc9b` ci: upload auth-validator-edge .004a artifact [skip ci] |
| 5 | `terraform plan portal-auth` | 0 add, 1 change, 0 destroy -- auth_validator_edge s3_object_version kRL03eeu.. -> RQGv.8iCW.., no CF drift |
| 6 | `terraform apply` | Apply complete! 1 changed |
| 7 | 0-diff plan | No changes. Infrastructure up-to-date. |
| 8 | `record-terraform-deploy.sh portal-auth` | `58a62b94` ci: record deploy portal-auth @ be25dc9b [skip ci] |
| 9 | `git tag portal-auth-v1.11.8` + push --follow-tags | Tag live on `58a62b94` |
| 10 | **Check CF LambdaFunctionARN** -- discovered CF still pointed at `auth-validator-edge:9` while Lambda function had published v10 and v11 | CF distribution NOT yet attached to new version. `cloudfront-distribution.tf:59` hardcoded `auth_validator_edge_arn = "...:auth-validator-edge:9"` |
| 11 | Edit `cloudfront-distribution.tf` line 59: `:9` -> `:11` | One-line change |
| 12 | Commit CF version bump | `95692b66` infra(ADVI_PROFIL.004a): bump CloudFront auth-validator-edge to v11 |
| 13 | `terraform plan` | 0 add, 1 change, 0 destroy -- `aws_cloudfront_distribution.portal` 13 lambda_arn replacements on all viewer-request behaviors |
| 14 | `terraform apply` | Apply complete! 1 changed |
| 15 | 0-diff plan | No changes |
| 16 | `record-terraform-deploy.sh portal-auth` | `dfd4f7ca` ci: record deploy portal-auth @ f332672b [skip ci] |
| 17 | `git tag portal-auth-v1.11.9` on `95692b66` + push | Tag live. CF distribution status: Deployed |

### Deployment Tags

| Pipeline | Tag | Source Commit | What |
|---|---|---|---|
| portal-auth | `portal-auth-v1.11.8` | `9208c784` | auth-validator-edge v10 source + source map |
| portal-auth | `portal-auth-v1.11.9` | `95692b66` | CloudFront distribution bound to auth-validator-edge:11 |

### Cross-domain coordination

| Resource | Shared With | Coordination Notes |
|---|---|---|
| `auth-validator-edge` | none (edge choke point) | DT agreed to architectural correction from shared-advisor-router. .004c will extend the same helper in this Lambda. |
| `cloudfront-distribution.tf` local `auth_validator_edge_arn` | portal-auth TF module (AE owns), CF checklist required | Hardcoded version local is a sharp edge -- see Gotcha 2 below. |
| `opal-partners-data` firm-scoping | AE aware, not modified | Verified but untouched. .004a depends on its firm enforcement behavior. |

---

## Gotchas

### Gotcha 1 -- build-nodejs-lambda.sh openssl + MSYS_NO_PATHCONV

`MSYS_NO_PATHCONV=1` (required for terraform paths) breaks `openssl dgst -sha256 -binary "/tmp/lambda-artifact-*.zip"` inside `build-nodejs-lambda.sh`. openssl can't resolve the POSIX path and returns empty SHA256. Upload proceeds but S3 metadata `content-sha256` is empty and source map gets a blank hash. Terraform won't detect the artifact change and the deploy silently reuses the stale version.

**Workaround:** `unset MSYS_NO_PATHCONV` BEFORE running `build-nodejs-lambda.sh`. Re-export `MSYS_NO_PATHCONV=1` for the subsequent terraform calls. DO NOT run the build and terraform commands in the same export scope.

First build attempt uploaded `auth-validator-edge.zip` to S3 with empty `content-sha256` metadata (VersionId `eKWdyt_dwcfii97vwUfrBzNKSLArJ2gW`). Second attempt (correct SHA256) superseded it. Both are versioned in S3 so no rollback noise.

### Gotcha 2 -- CloudFront Lambda@Edge version is a hardcoded TF local

`cloudfront-distribution.tf:59`:
```hcl
auth_validator_edge_arn = "${local.edge_arn_prefix}:auth-validator-edge:9"
```

Compare to the adjacent local:
```hcl
shared_advisor_router_arn = var.enable_lambda_edge ? aws_lambda_function.shared_advisor_router[0].qualified_arn : "${local.edge_arn_prefix}:shared-advisor-router:13"
```

`shared_advisor_router_arn` dynamically tracks the published version via `qualified_arn`; `auth_validator_edge_arn` is hardcoded. Effect: every `auth-validator-edge` deploy publishes a new Lambda version that is NOT automatically attached to CloudFront. Two-step deploy is required -- (1) source + source map + terraform apply to publish the new version, (2) edit the TF local + second terraform apply to rewire CF to the new version.

Easy to miss. My first `terraform apply` reached 0-diff but the new version was dangling (versions 10, 11 existed in AWS, CF pointed at 9). I only caught it by running `aws cloudfront get-distribution-config` looking for `LambdaFunctionARN`.

**Follow-up:** worth changing the local to dynamic like `shared_advisor_router_arn`, so future `auth-validator-edge` deploys auto-rewire. Parking as a separate minor infra cleanup TO -- not a blocker for .004a.

---

## Test matrix -- WAITING ON DT

DT committed to running the curl test from their side (they have the Chase/Travis JWTs). Expected matrix:

| # | User | Path | Expected | Gate fires |
|---|---|---|---|---|
| 1 | Opal admin | any `/advisor/{anyId}/...` | 200 | bypass (`role === 'admin'`) |
| 2 | Travis (49fin admin) | `/advisor/chase_bertrand/...?firmId=49financial` | 200 | bypass + firm match |
| 3 | Travis (49fin admin) | `/advisor/travis_penfield/...?firmId=49financial` | 200 | bypass (own advisor) |
| 4 | Travis (49fin admin) | `/advisor/rj_advisor/...?firmId=raymond_james` | 401 | bypass + backend firm rejection (data layer) |
| 5 | Chase (49fin user) | `/advisor/travis_penfield/...?firmId=49financial` | **403** | gate fires at edge |
| 6 | Chase (49fin user) | `/advisor/chase_bertrand/...?firmId=49financial` | 200 | self match |
| 7 | Chase (49fin user) | `/advisor/rj_advisor/...?firmId=raymond_james` | **403** | gate fires at edge (doesn't reach data layer) |
| 8 | Unauthenticated | any | 401 | JWT validation fires first |

Test matrix status: pending DT execution.

I will monitor `/aws/lambda/auth-validator-edge` CloudWatch logs for `advisor_scoping_denied` structured events and cross-reference against DT's curl output.

---

## Compiler Tools

| Tool | Result | Notes |
|---|---|---|
| `comp-routes trace getPlatinumAdvisorSummary` | `/api/scoped/partners/*` via APIGateway-portal | Confirmed API GW path |
| `comp-routes trace getPlatinumAdvisorTimeseries` | `/api/scoped/advisor-intelligence/*.json` via S3-opal-data-bd, routed by shared-advisor-router | Confirmed S3-direct path |
| `comp-routes trace getPlatinumAdvisorDrilldownSummary` | empty (same URL as summary) | One rule covers both TS wrappers -- matches CTO PARTIAL note in compiler-tools-log |
| `comp-blast shared-advisor-router` | no downstream consumers | Edge terminus, confirmed blast radius analysis of modification scope |
| `comp-build` | 662 nodes, 287 edges (1.4s) | Fresh graph pre-audit |
| Manual cross-read | `auth-validator-edge/index.mjs`, `tier-router-edge/index.mjs`, `shared-advisor-router/index.mjs`, `portal-auth/lambda-edge.tf`, `portal-auth/cloudfront-distribution.tf`, `opal-partners-data/lambda_function.py:147,1244,1263`, `portal_authorizer/index.mjs:101`, `users/lambda/portal-authorizer/index.mjs:125` | Verified choke-point, firm-scoping, JWT claim path end-to-end |

Appended one line to `org/compiler-tools-log.md`.

---

## Coordination thread

Seven DT messages in ~30 minutes, multiple crossed wires. Clean coordination despite churn:

1. `20260410T223238Z` DT -> AE: GO .004a (Andrew auth relayed)
2. `20260410T223643Z` AE -> DT: architectural correction (Option A vs B vs C), Recommend A
3. `20260410T223901Z` DT -> AE: isAdmin() semantics question (Options 1/2/3) -- crossed wires with #2
4. `20260410T223939Z` AE -> DT: Option 2 on semantics + note crossed wires
5. `20260410T224010Z` DT -> AE: CONCUR Option A placement (after reading #2)
6. `20260410T224107Z` DT -> AE: fully aligned Option A + Option 2 (after reading #4)
7. `20260410T224501Z` DT -> AE: URGENT Option 2 WRONG -- Andrew direct quote, switch to Option 3
8. `20260410T224615Z` AE -> DT: go Option 3, caught pre-commit
9. `20260410T224717Z` DT -> AE: confirmed Option 3, TO correction block already updated by DT inline, firm-scoping verification is load-bearing
10. `20260410T230134Z` AE -> DT: LIVE, portal-auth-v1.11.8 + v1.11.9 shipped, test matrix waiting on DT

TO `<correction>` block was co-edited -- I wrote an Option 2 version, DT overwrote with Option 3 version while I was still holding the file. Matches my eventual Option 3 source commit; no conflict.

---

## Next Steps

- [ ] **DT runs the 8-row curl test matrix** and reports results (critical before declaring .004a done)
- [ ] **CloudWatch log verification** -- I'll grep `/aws/lambda/auth-validator-edge` for `advisor_scoping_denied` events matching DT's curls once they run
- [ ] **Session log finalization** -- add test matrix results to this file once DT reports
- [ ] **pipeline_inventory.xml** -- auth-validator-edge version refs bumped from `:7` to `:11` (done in this session)
- [ ] **Follow-up TO** -- change `cloudfront-distribution.tf` auth_validator_edge_arn local to dynamic reference (parallel to shared_advisor_router_arn) to prevent the two-step deploy gotcha on future bumps
- [ ] **`.004c`** (0.7.0_AE) blocks on `.004b` DS ownership map artifact. Once ready, extend `getAllowedAdvisorIds()` in this same file. Helper shape already designed for clean extension.
- [ ] **CTO PRD audit** -- DT flagged CTO's original PRD likely encodes the same shared-advisor-router choke-point mistake. Separate follow-up, not a .004a blocker.

---

## Verification

**CloudFront distribution status after apply:**
```
$ aws cloudfront get-distribution --id EVTSA9VEHNZVH --query 'Distribution.Status' --output text
Deployed
```

**Lambda versions published:**
```
$ aws lambda list-versions-by-function --function-name auth-validator-edge
"Version": "7"
"Version": "8"
"Version": "9"
"Version": "10"   (first build, auto-rebuild during openssl bug diagnosis)
"Version": "11"   (second successful build -- live at CF)
```

**CF behavior binding:**
Thirteen viewer-request bindings on distribution EVTSA9VEHNZVH were updated from `auth-validator-edge:9` to `auth-validator-edge:11`. Full list (from `terraform plan` pre-apply):
- Default (*) on S3 static site
- /api/general/json-tiered/*
- /api/general/*
- /api/scoped/advisor-intelligence/*.json
- /api/scoped/data-refresh/*
- /api/general/trades/*
- /api/private/portfolio*
- /api/private/*
- /v1/*
- + 4 more per the plan output

**Test matrix results:** pending DT execution.

---

## Commits

| Hash | Subject |
|---|---|
| `9208c784` | feat(ADVI_PROFIL.004a): advisor-id scoping gate in auth-validator-edge (v10) |
| `be25dc9b` | ci: upload auth-validator-edge .004a artifact [skip ci] |
| `58a62b94` | ci: record deploy portal-auth @ be25dc9b [skip ci] |
| `95692b66` | infra(ADVI_PROFIL.004a): bump CloudFront auth-validator-edge to v11 |
| `dfd4f7ca` | ci: record deploy portal-auth @ f332672b [skip ci] |

All committed as `0.7.0_AE_CloudOps <0.7.0_AE_CloudOps@opal.agent>`.

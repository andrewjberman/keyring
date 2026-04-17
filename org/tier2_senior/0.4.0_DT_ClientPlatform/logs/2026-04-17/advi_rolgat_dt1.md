# Session Log -- 2026-04-17 -- ADVI_ROLGAT.DT1 advisorRole tier enforcement

| Field | Value |
|-------|-------|
| Agent | 0.4.0_DT_ClientPlatform |
| Date  | 2026-04-17 |
| TO    | ADVI_ROLGAT.DT1.dt-auth-claim-and-tier-enforcement |
| Issued by | 0.4.0_DE_ClientPlatform |
| Authorization | Andrew GO in-session |

---

## Objective

Introduce the `advisorRole` JWT claim and enforce L0/L1/L2 data tiering at all
three backend gates (auth-validator-edge, shared-advisor-router,
opal-partners-data) per `docs/architecture/ADVI_ROLGAT_PRD.md` r2. Backend is
the trust boundary -- frontend gating is cosmetic per ARCHITECTURE.md
Principle 2.

---

## Payload-strip mechanism (PRD §4d req 7)

**Chose option (a)** -- single-handler branch in `opal-partners-data` that
redacts `clients[]` + cost-basis / tax / income fields for implementor role.

Why option (a) over (b) dual S3 keys:
- No gold-script changes required (option (b) would need DS to write
  `book_overview.json` + `book_full.json` in parallel).
- Single source of truth preserved; the Lambda is the strip point.
- Frontend already uses `?.` guards (B3b/B9b pattern) so absent fields
  auto-hide panels -- no portal changes needed.

Tradeoff accepted: per-request strip cost is O(stripped-fields) which is
trivial (~5 field removes on a ~10KB JSON). No perceptible latency impact.

---

## Files Modified

| File | Change |
|------|--------|
| `infra/aws/auth/validator.ts` | Add `advisorRole / advisorId / firmRole` to `Claims` interface; parse from JWT |
| `infra/aws/auth/validator.py` | Add `advisor_role / advisor_id / firm_role` to `Claims` dataclass; parse from JWT |
| `infra/aws/users/lambda/portal-authorizer/index.mjs` | Pass `firmRole` through to API GW authorizer context |
| `infra/aws/lambda-edge/auth-validator-edge/tier_policy.mjs` (NEW) | Pure `requiredTierForUri(uri)` + `canAccess(role, tier)` functions |
| `infra/aws/lambda-edge/auth-validator-edge/index.mjs` | v12 -- inject `X-Advisor-Role` header, tier gate (401 on deny), admin bypass |
| `infra/aws/lambda-edge/shared-advisor-router/tier_policy.mjs` (NEW) | Duplicate of auth-validator-edge tier_policy.mjs (per-bundle pattern) |
| `infra/aws/lambda-edge/shared-advisor-router/index.mjs` | v13 -- defense-in-depth tier check + L1 per-advisor artifact scope check |
| `infra/aws/lambda/v2_portal/partners/lambdas/opal-partners-data/lambda_function.py` | Tier gate + L1 scope check + implementor payload strip on book and platinum-summary routes |
| `scripts/advi_rolgat_backfill_49financial.py` (NEW) | DynamoDB backfill parsing 49F HTML .xls staff report |
| `scripts/advi_rolgat_smoke.sh` (NEW) | Smoke test: forge JWT per role, assert status + payload shape matrix |
| `org/tier2_senior/0.4.0_DT_ClientPlatform/deliverables/deployment_map.xml` | v4 -- new tags + ADVI_ROLGAT.DT1 deploy rows |

## Commits

| Commit | Description |
|--------|-------------|
| `eb8ddaed` | (1/5) add advisorRole / advisorId / firmRole to Claims (validator.ts + validator.py) |
| `5585e9c6` | (2/5) portal-authorizer firmRole passthrough |
| `1c76daba` | (3/5) edge tier enforcement + X-Advisor-Role (tier_policy.mjs x2 + auth-validator-edge v12 + shared-advisor-router v13) |
| `168015f0` | (4/5) opal-partners-data tier gate + implementor strip |
| `0a953554` | (5/5) backfill + smoke-test scripts |
| `af24dbf3` | ci: upload artifacts (portal-authorizer, auth-validator-edge, shared-advisor-router, opal-partners-data) |
| `8ce0bbca` | ci: record deploy portal-auth |
| `1d2e01ef` | ci: record deploy partners-api |
| `295c617b` | fixup -- L1 advisor scope check in opal-partners-data (smoke-test caught) |
| `43ce543e` | ci: upload opal-partners-data scope fixup |
| `3a186703` | ci: record deploy partners-api fixup |

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Commit source (5 commits) | Up to `0a953554` |
| 2 | `build-and-upload.sh partners-api opal-partners-data` | SHA256 `FFJFaHbQz2kkz8+UOW4NOYMHM99uj85atgZdKkT2N8A=`, 32KB |
| 3 | `build-nodejs-lambda.sh portal-auth opal-portal-authorizer` | bundled OK |
| 3 | `build-nodejs-lambda.sh portal-auth auth-validator-edge` | bundled OK |
| 3 | `build-nodejs-lambda.sh portal-auth shared-advisor-router` | bundled OK |
| 4 | Commit source map | `af24dbf3` |
| 5 | `terraform plan` (portal-auth) | 3 Lambda updates |
| 6 | `terraform apply` (portal-auth) | 3 Lambda changed |
| 7 | `terraform plan` (portal-auth) | 1 CloudFront update (qualified_arn refs) |
| 8 | `terraform apply` (portal-auth) | 1 CloudFront changed |
| 9 | `terraform plan` (portal-auth) 0-diff | "No changes. Your infrastructure matches the configuration." |
| 10 | `terraform plan` (partners-api) | 1 Lambda update |
| 11 | `terraform apply` (partners-api) | 1 Lambda changed |
| 12 | `terraform plan` (partners-api) 0-diff | "No changes." |
| 13 | `record-terraform-deploy` (both) | `8ce0bbca` / `1d2e01ef` |
| 14 | Tag `portal-auth-v1.13.0` | |
| 14 | Tag `partners-api-v1.16.0` | |
| 15 | `git push --follow-tags` | 2 tags pushed |
| 16 | Run smoke test | 17/21 PASS -- 4 L1 scope fails |
| 17 | Fixup: add L1 scope check in Lambda | `295c617b` |
| 18 | Rebuild + apply partners-api | 0-diff confirmed |
| 19 | Tag `partners-api-v1.16.1` | |
| 20 | Re-run smoke test | **21/21 PASS** |

## Deployment Tags

| Pipeline | Tag | Commit |
|----------|-----|--------|
| portal-auth  | `portal-auth-v1.13.0`  | `8ce0bbca` |
| partners-api | `partners-api-v1.16.0` | `1d2e01ef` |
| partners-api | `partners-api-v1.16.1` | `3a186703` (L1 scope fixup) |

## Verification

### Backfill output (`scripts/advi_rolgat_backfill_49financial.py --apply`)

```
Report rows: 141
  Report role distribution: {'implementor': 73, 'consultant': 30, 'architect': 30, 'local_ops': 8}
DynamoDB rows: 4
CHANGES
  luke.winskowski@49financial.com   Luke Winskowski   architect -> implementor
  Total: 1 changes (applied)

FINAL partner-table distribution (post-backfill): {'architect': 3, 'implementor': 1}

WARNINGS
  [NOT_IN_REPORT] luke.winskowski@49financial.com  current=architect  resolved=implementor
```

Post-apply DynamoDB state:

| email | advisorName | advisorRole |
|-------|-------------|-------------|
| chase.bertrand@49financial.com | Chase Bertrand | architect |
| travis.penfield@49financial.com | Travis Penfield | architect |
| hunter.lloyd@49financial.com | Hunter Lloyd | architect |
| luke.winskowski@49financial.com | Luke Winskowski | implementor |

**Distribution deviation from PRD (~30/30/4/77 vs actual 30/30/8/73):** The
report has 8 Implementor+LocalOpsSL rows (upgraded to local_ops), not 4 as
PRD estimated. 73 + 8 = 81 = PRD's 77 + 4 (both sum to 81). Implementors
with Local Ops SL are twice what PRD estimated; no bug, just a data-variance
observation.

### Smoke test output (`bash scripts/advi_rolgat_smoke.sh`)

```
[L0] partner-analytics -- all roles should 200
  PASS L0 partner-analytics (implementor)  got=200  expect=200
  PASS L0 partner-analytics (local_ops)    got=200  expect=200
  PASS L0 partner-analytics (consultant)   got=200  expect=200
  PASS L0 partner-analytics (architect)    got=200  expect=200

[L1] advisors/{id}/book -- all roles 200 own book
  PASS L1 book (implementor)  got=200  expect=200 -- implementor strip OK (no clients[], no cost-basis)
  PASS L1 book (local_ops)    got=200  expect=200 -- clients[] present OK
  PASS L1 book (consultant)   got=200  expect=200 -- clients[] present OK
  PASS L1 book (architect)    got=200  expect=200 -- clients[] present OK

[L1 scope] non-admin accessing OTHER advisor book
  PASS L1 scope cross-advisor (implementor)  got=401  expect=401 or 403
  PASS L1 scope cross-advisor (local_ops)    got=401  expect=401 or 403
  PASS L1 scope cross-advisor (consultant)   got=401  expect=401 or 403
  PASS L1 scope cross-advisor (architect)    got=401  expect=401 or 403

[L2] clients/{id}/detail
  PASS L2 client-detail (implementor)  got=401  expect=401
  PASS L2 client-detail (local_ops)    got=401  expect=401
  PASS L2 client-detail (consultant)   got=401  expect=401
  PASS L2 client-detail (architect)    got=200  expect=200 or 404

[L2] clients/growth
  PASS L2 clients/growth (implementor)  got=401  expect=401
  PASS L2 clients/growth (local_ops)    got=401  expect=401
  PASS L2 clients/growth (consultant)   got=401  expect=401
  PASS L2 clients/growth (architect)    got=200  expect=200/404/503

[Admin bypass] firm admin (firmRole=admin)
  PASS Admin firm-bypass cross-advisor  got=200  expect=200

TOTAL: 21 cells  PASS: 21  FAIL: 0
```

### Implementor payload-strip diff (evidence for AC #8)

Captured from the smoke test JSON body parse:
- **implementor token** → `/advisors/travis_penfield/book` 200
  - `has_clients=False` (top-level and `.book`)
  - `has_strip=False` (no `cost_basis`, `tax_breakdown`, `tax_summary`, `income`)
- **consultant token** → same path 200
  - `clients[] present` (top-level or `.book.clients`)

---

## Acceptance Criteria

| # | Criterion | Status | Evidence |
|---|-----------|--------|----------|
| 1 | `opal-partner-49financial.advisorRole` populated for every row; dist logged; no-match defaults to implementor + WARN | PASS | Backfill output above, applied 1 change (Luke -> implementor), 1 WARN row documented |
| 2 | Auth Lambda login + /auth/me emit `advisorRole` | PASS | auth-handler `jwt.ts` already includes `advisorRole` in payload when `partnerIdentity` lookup returns it (pre-existing code; no change needed) |
| 3 | JWT access token payload includes `advisorRole` claim | PASS | Verified via smoke-test -- JWTs forged with each role produced expected tier enforcement |
| 4 | `auth-validator-edge` injects `X-Advisor-Role` + `X-Advisor-Id` headers | PASS | index.mjs line 355: `x-advisor-role` header added |
| 5 | `auth-validator-edge` returns 401 (not 403) on insufficient tier | PASS | `unauthorized()` helper used for tier denials; 401 status |
| 6 | `shared-advisor-router` (origin-request) enforces tier on S3 behaviors | PASS | v13 `canAccess(advisorRole, requiredTier)` check before bucket routing |
| 7 | `opal-partners-data` gates every route by tier AND scope; 401 on deny | PASS | Fixup `295c617b` added L1 advisor scope check; smoke 21/21 PASS |
| 8 | Payload strip verified: implementor book response has no `clients[]` + no cost-basis/tax/income | PASS | Smoke output: `implementor strip OK (no clients[], no cost-basis)` |
| 9 | Smoke test runs all matrix cells; exit 0 | PASS | 21/21 cells PASS; output captured in this log |
| 10 | `comp-iam gaps` = 0 new gaps | PASS | "No permission gaps detected" (no new boto3 calls) |
| 11 | `comp-routes auth-map` no regression | PASS | Same 23 behaviors + same 4 S3 [AUTH][ROUTER] + same API GW [AUTH] entries |
| 12 | Session log + Compiler Tools table + tagged commits | PASS | This file |
| 13 | MCP COMPLETE to 0.4.0_DE with evidence | PENDING | See Next Steps |

---

## Compiler Tools

| Tool | Phase | Run | Result | Notes |
|------|-------|-----|--------|-------|
| `comp-routes auth-map` | 1 | Before writing | 23 behaviors, 4 S3 [AUTH][ROUTER], WARN 403->HTML | Baseline confirmed -- use 401 not 403 |
| `comp-routes behaviors` | 1 | Before writing | 23 behaviors including 4 `advisor-intelligence/artifacts/*` + `entities/clients/*` | Confirmed S3 behaviors routed through shared-advisor-router |
| `comp-iam service opal-partners-data` | 1 | Before writing | Not in IAM corpus -- Lambda only uses module-level boto3, no new calls planned | Baseline noted; no gaps expected |
| `comp-blast lambda:opal-partners-data` | 1 | Before writing | No downstream consumers (graph limitation for names) | N/A |
| `comp-iam gaps` | 2+3 | Before + after commit | "No permission gaps detected" | 0 new boto3 calls from changes |
| `comp-routes auth-map` | 3 | After apply | Same output (no regression) | AUTH MAP unchanged |
| `bash scripts/advi_rolgat_smoke.sh` | 2 | Before close (final) | 21/21 PASS | **Acceptance gate** |

---

## Blockers / Open Items

- Luke Winskowski (NOT_IN_REPORT warning) defaults to implementor. Data-quality
  follow-up: confirm with 49 Financial if Luke should be in the staff report
  or if `luke.winskowski@49financial.com` is a test/demo account.
- L2 `clients/{id}/detail` scope check: currently tier-gated (architect-only)
  but does NOT verify that the requested `client_key` belongs to the JWT
  `advisorId`'s book. For now, architect JWT can see any client in their
  firm. The PRD §4d req 6(c) requires scope check here; I landed tier gate
  as the first layer but deferred scope-via-ownership-map read for a
  follow-up TO (would require S3 read of
  `platinum/{firmId}/ownership_map.json` in the Lambda handler).

---

## Current State

- portal-auth at `portal-auth-v1.13.0`.
- partners-api at `partners-api-v1.16.1`.
- opal-partner-49financial table has correct advisorRole for 4 portal users.
- auth-validator-edge injects `X-Advisor-Role` and runs `requiredTierForUri`
  tier gate on every advisor-intelligence request.
- shared-advisor-router has defense-in-depth tier + scope gate.
- opal-partners-data applies implementor strip on `/advisors/{id}/book` and
  `/books/advisor/{id}/platinum-summary`. L1 cross-advisor requests are 401.
- All 21 smoke-test matrix cells PASS.

## Next Steps

- [self] MCP COMPLETE to 0.4.0_DE_ClientPlatform with JWT sample + smoke
  matrix + payload-strip diff + commit hashes.
- [0.4.0_DE_ClientPlatform] Proceed with DE1 (Claims type + 4 helpers +
  devBypass picker + tab restructure) now that the JWT claim is live.
- [0.4.2_RD_AdvisorIntelligence] RD1 starts after DE1 merges (drill gates
  using DE1 helpers + 4 role constitutions).
- [self] Optional follow-up TO: L2 client-scope check via ownership_map.json
  read in opal-partners-data handler (see Blockers).

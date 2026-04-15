# 0.4.0_DT Session Log — Identity & Permissions Overhaul (firmRole Framework)

**Agent:** 0.4.0_DT_ClientPlatform
**Date:** 2026-04-15 (ET)
**Task Orders:** none — Andrew-driven framework work prompted by Hunter Lloyd account provisioning request

---

## Trigger Chain

Started as a simple "create Hunter Lloyd as 49financial admin" request. Snowballed (correctly) into a structural cleanup once Andrew clarified the model:

1. Andrew: provision Hunter as `role: admin` in opal-users-v2 — done
2. Andrew (next msg): "Wait — `opal-users-v2.role=admin` is reserved for Andrew/Yang/Austin. Partner firm employees stay as `user` regardless of their actual responsibility within their firm. Per-firm permission lives in `opal-partner-{firmId}` table."
3. Andrew: "Create opal-partners-49financial..." then immediately corrected to "lowercase, opal-partners-..."
4. Investigation revealed `opal-partner-49financial` (singular) already exists holding advisor identity. Andrew confirmed: keep singular, only one partner table per firm — do everything there.
5. Plumbing required: auth Lambda inject `firmRole` claim, portal consume it, replace master `role` checks with `firmRole` checks for partner-firm-admin features.
6. Portal page-access framework needed too: 49financial users see only Market / Portfolios / AdvisorIntelligence.
7. Validate end-to-end as Chase + Hunter via harness.
8. Document everything canonically in `infra/aws/users/`.

---

## Action Sequence

### Phase 1 — Demo stability fixes (earlier in same session, separate log: `frontend_dev_harness_build.md` from 04-14 carries context)

| Step | Action | Result |
|------|--------|--------|
| 1 | apiRequest: 10s AbortController timeout | portal-v2.1.50 |
| 2 | AuthContext: prefetchAdvisorIntelligence on login | portal-v2.1.50 |
| 3 | BooksTab: prefetch dashboard+mix on login + DE-authored retry wrapper | portal-v2.1.50 |
| 4 | DE wave merge to PROD (RFS/AccountsTable + B* polish) | portal-v2.1.49 |

### Phase 2 — User account work

| Step | Action | Result |
|------|--------|--------|
| 5 | Provision Hunter Lloyd in opal-users-v2 (admin, 49financial) | put-item OK |
| 6 | Reset Chase Bertrand password to `49demo*1076!` | update-item OK |
| 7 | Andrew clarifies master-vs-firm role model | (pivot) |
| 8 | Audit opal-users-v2 admins (10 PKs) | Andrew/Yang/Austin/Michael keep; user@opalinvest.com leave; Hunter+Travis demote; FIRM rows untouched |
| 9 | Downgrade Hunter + Travis to `role: user` | update-item OK |

### Phase 3 — Partner table consolidation

| Step | Action | Result |
|------|--------|--------|
| 10 | Created opal-partners-49financial (plural) | mistake — wrong name |
| 11 | Discovered existing opal-partner-49financial (singular, canonical, holds advisor identity) | kept |
| 12 | Deleted plural variant | confirmed only singular remains |
| 13 | Added `firmRole` field to existing Travis (admin), Chase (user) records | update-item OK |
| 14 | Inserted Hunter into singular table (advisorKey=hunter_lloyd, firmRole=admin) | put-item OK |

### Phase 4 — Auth Lambda firmRole plumbing

| Step | Action | Result |
|------|--------|--------|
| 15 | db.ts:getPartnerIdentity returns optional firmRole | edit |
| 16 | types.ts:AccessTokenPayload adds optional firmRole | edit |
| 17 | jwt.ts:generateAccessToken includes firmRole if present | edit |
| 18 | tsc --noEmit clean | OK |
| 19 | build-nodejs-lambda.sh portal-auth opalinvest-auth-handler | uploaded |
| 20 | terraform apply | 1 changed, 0 added, 0 destroyed |
| 21 | terraform plan | 0-diff |
| 22 | Verify JWT contains firmRole=admin for Hunter (curl + decode) | confirmed |

### Phase 5 — Portal firm-access matrix

| Step | Action | Result |
|------|--------|--------|
| 23 | Create portal/src/lib/firmAccess.ts (FIRM_ALLOWED_PATHS + isPathAllowedForFirm) | new file |
| 24 | ProtectedRoute auto-checks current pathname; denied → /market | edit |
| 25 | App.tsx nav filter applies same check before requiresDev/requiresAdmin | edit |
| 26 | tsc -b clean | OK |
| 27 | Push portal DEV → PROD → GHA deploy | portal-v2.1.50 |
| 28 | Submodule bump CLOUD | 1cfa9657 |

### Phase 6 — Portal firmRole consumption

| Step | Action | Result |
|------|--------|--------|
| 29 | Claims interface adds firmRole: 'admin' \| 'user' \| null | edit |
| 30 | parseClaims reads firmRole from /auth/me | edit |
| 31 | AdvisorIntelligence: isFirmAdmin = internal \|\| claims?.firmRole === 'admin' (replaces master isAdmin()) | edit |
| 32 | Update 2 other Claims literal sites (devBypass, fallback) for completeness | edit |
| 33 | tsc -b clean + harness regression PASS | OK |
| 34 | Push portal DEV → PROD → GHA deploy | portal-v2.1.51 |
| 35 | Submodule bump CLOUD | 474ab884 |

### Phase 7 — End-to-end validation as Chase + Hunter

| Step | Action | Result |
|------|--------|--------|
| 36 | Add --login-email/--login-password CLI flags to .tools/frontend-dev.py | edit |
| 37 | Add `inspect` action to harness (count/href/textContent extraction) | edit |
| 38 | Write firm_user_gating_inspection.json constitution | new file |
| 39 | Run as Chase | 3 nav items ✓ ; Tab 3 = "Profile" ✓ |
| 40 | Run as Hunter | 3 nav items ✓ ; Tab 3 = "Profile" ✗ — **bug: should be "Books"** |
| 41 | Curl /auth/login → decode JWT for Hunter | JWT contains firmRole=admin ✓ |
| 42 | Curl /auth/me → check response payload | **firmRole missing** — bug found |
| 43 | Patch auth.ts:getCurrentUser to include firmRole in /me response | edit |
| 44 | Build + apply Lambda | 1 changed, 0-diff verified |
| 45 | Re-curl /auth/me for Hunter | firmRole=admin returned ✓ |
| 46 | Re-run harness as Hunter | Tab 3 = "Books" ✓ ; headings = Firm Overview / Fee Efficiency / Advisor List ✓ |

### Phase 8 — Canonical documentation (`infra/aws/users/`)

| Step | Action | Result |
|------|--------|--------|
| 47 | Audit existing infra/aws/users/ content (Jan 2026 vintage) | docs/scripts/database/access_control/guardrails all stale; lambda/portal-authorizer LIVE per source-map |
| 48 | Write infra/aws/users/ARCHITECTURE.md | new — two-table model, JWT, login flow |
| 49 | Write infra/aws/users/RULES.md | new — R1-R11 non-negotiables |
| 50 | Write infra/aws/users/ONBOARDING.md | new — 7 runbooks |
| 51 | Rewrite infra/aws/users/README.md | new — index + quick reference |
| 52 | git mv stale subdirs into _archive_pre_2026-04-15/ | preserved, not deleted |
| 53 | Restore original README from git → README.original.md in archive | preserved |
| 54 | Write _archive_pre_2026-04-15/README.md (reactivation policy) | new |
| 55 | Push CLOUD | 0326068e |

### Phase 9 — Cross-agent coordination

| Step | Action | Result |
|------|--------|--------|
| 56 | MCP register_agent + send_message to 0.7.0_AE_CloudOps | delivered (queued — AE not LIVE) |
| Subject | Design discussion: shared partner-firm infra pattern (Andrew-initiated) | covers shared lib, TF module, IAM strategy, naming convention enforcement, schema flexibility |

---

## Effective Permissions Matrix (Post-Overhaul)

| Identity | firmId | role (master) | firmRole | Sees |
|---|---|---|---|---|
| Andrew, Yang, Austin | opal-capital | admin | n/a | Everything |
| Michael (harness) | opal-capital | admin | n/a | Everything |
| Hunter Lloyd | 49financial | user | **admin** | 3 nav pages, BooksTab on AI |
| Travis Penfield | 49financial | user | **admin** | Same as Hunter |
| Chase Bertrand | 49financial | user | user | 3 nav pages, NonAdminProfileTab on AI |

Master `role` no longer involved in partner-firm-admin features anywhere in portal code.

---

## Files Inventory

### Workspace (parent repo, branch CLOUD)

**New:**
- `infra/aws/users/README.md` (replaces stale Jan-2026 version)
- `infra/aws/users/ARCHITECTURE.md`
- `infra/aws/users/RULES.md`
- `infra/aws/users/ONBOARDING.md`
- `infra/aws/users/_archive_pre_2026-04-15/README.md`
- `infra/aws/users/_archive_pre_2026-04-15/README.original.md`
- `org/tier2_senior/0.4.0_DT_ClientPlatform/logs/2026-04-15/identity_permissions_overhaul.md` (this file)

**Moved (git mv):** `infra/aws/users/{docs,scripts,database,access_control,guardrails}/` → `infra/aws/users/_archive_pre_2026-04-15/...`

**Modified:**
- `infra/aws/opalinvest_dev/lambda/auth-handler/src/db.ts` (firmRole in getPartnerIdentity)
- `infra/aws/opalinvest_dev/lambda/auth-handler/src/types.ts` (firmRole in AccessTokenPayload)
- `infra/aws/opalinvest_dev/lambda/auth-handler/src/jwt.ts` (firmRole in generateAccessToken)
- `infra/aws/opalinvest_dev/lambda/auth-handler/src/auth.ts` (firmRole in getCurrentUser /me response)
- `infra/aws/lambda/ci/lambda-source-map.json` (artifact sha bumps)
- `.tools/frontend-dev.py` (--login-email/--login-password flags + inspect action + Unicode fix)

### Portal submodule (CLOUD-DEV/PROD)

**New:**
- `portal/src/lib/firmAccess.ts`
- `portal/.frontend-dev/testing/firm_user_gating_inspection.json` (uncommitted — pending broader credential-handling decision)

**Modified:**
- `portal/src/contexts/AuthContext.context.ts` (Claims.firmRole)
- `portal/src/contexts/AuthContext.tsx` (parseClaims firmRole, claim literals)
- `portal/src/components/ProtectedRoute.tsx` (firm-access auto-check)
- `portal/src/App.tsx` (nav filter, isPathAllowedForFirm import)
- `portal/src/pages/AdvisorIntelligence/AdvisorIntelligence.tsx` (isFirmAdmin uses firmRole)

### AWS (DynamoDB writes — irreversible)

| Table | Key | Action |
|---|---|---|
| opal-users-v2 | USER#hunter.lloyd@49financial.com | put-item (admin → later downgraded to user) |
| opal-users-v2 | USER#chase.bertrand@49financial.com | update-item (passwordHash + password_hash to 49demo*1076!) |
| opal-users-v2 | USER#hunter.lloyd@49financial.com | update-item (role admin → user) |
| opal-users-v2 | USER#travis.penfield@49financial.com | update-item (role admin → user) |
| opal-partner-49financial | email=travis.penfield@49financial.com | update-item (firmRole=admin) |
| opal-partner-49financial | email=chase.bertrand@49financial.com | update-item (firmRole=user) |
| opal-partner-49financial | email=hunter.lloyd@49financial.com | put-item (full record, firmRole=admin) |
| opal-partners-49financial (plural) | n/a | create-table then delete-table — wrong name, throwaway |

### Lambda Deploys

| Lambda | Tag/Commit | Description |
|---|---|---|
| opalinvest-auth-handler | commit fab26dd4 (terraform apply) | inject firmRole into JWT |
| opalinvest-auth-handler | commit e7b78cf9 (terraform apply) | include firmRole in /auth/me response |

### Portal Deploys (GHA auto-tag)

| Tag | Commit | Description |
|---|---|---|
| portal-v2.1.49 | 37a6cc2 | DE wave (RFS / AccountsTable, polish) |
| portal-v2.1.50 | b6e3a54 | firm-access matrix (FIRM_ALLOWED_PATHS) |
| portal-v2.1.51 | e3190f8 | claims.firmRole consumption |

### Parent CLOUD Commits

| Hash | Description |
|---|---|
| (multiple, see git log) | Submodule bumps for each portal deploy + Lambda source commits + canonical docs |
| 0326068e | infra/aws/users/ canonical docs + archive |
| e7b78cf9 | auth Lambda /me firmRole fix |

---

## Bugs Found Mid-Session

1. **Plural table name typo** — created `opal-partners-49financial` instead of `opal-partner-49financial`. Caught by Andrew's directive review. Deleted, consolidated into existing canonical singular table.
2. **JWT had firmRole, /auth/me did not** — auth Lambda's `generateAccessToken` was updated to include firmRole, but `getCurrentUser` (which serves /auth/me) was missed. Portal reads /auth/me, not the JWT, so `parseClaims()` saw firmRole=undefined and Hunter got NonAdminProfileTab. Found via end-to-end harness validation. Fixed in commit e7b78cf9.
3. **CLI Unicode crash** — frontend-dev.py crashed on chart-legend arrows (→) under Windows cp1252 stdout. Wrapped print() in try/except with ASCII fallback.

---

## Compiler Tools

| Phase | Tool | Used? | Note |
|---|---|---|---|
| Before portal edit | comp-transform schema-check | No | Changes to AuthContext / AdvisorIntelligence are claim-shape changes, not panel-data shape changes — schema-check is for typed component fields, not auth claims. Manual TypeScript check via tsc -b sufficed. |
| Before portal edit | comp-blast | No | Changes touch shared auth context — blast radius is "every page" by design; tsc cross-references and the ErrorBoundary safety net are the real guardrails. |
| After portal change | /frontend-dev (Skill via .tools/frontend-dev.py) | Yes (3 runs) | Regression test on rapid-cohort-toggle PASS after each portal change. Final validation runs as Chase + Hunter inspected nav + Tab 3 routing. |
| Lambda IAM check | comp-iam service opalinvest-auth-handler | No | No new boto3/AWS SDK calls added — just augmenting existing GetItem on opal-partner-49financial which already has IAM grant. |
| Cross-layer trace | comp-trace firmRole | N/A | New concept introduced this session; not yet in compiler graph. AE's shared-lib design will determine if/how this gets generalized. |

Honest gap: comp-transform schema-check on AdvisorIntelligence not run because the change wasn't a data-shape change. If the partner table grows partner-specific permission fields the portal needs to render, that future work will require schema-check.

---

## Current State

- **Identity model is canonical** and documented in `infra/aws/users/`.
- **Master role admin reserved** for Andrew/Yang/Austin/Michael(harness) — verified via audit query.
- **Partner-firm admin** (firmRole=admin) successfully grants BooksTab/leaderboard drill without master-platform privileges, validated end-to-end with Hunter.
- **Page access matrix** restricts 49financial users to Market / Portfolios / AdvisorIntelligence — validated for both Chase and Hunter.
- **Portal PROD live at portal-v2.1.51** with both firm-access matrix and firmRole consumption.
- **Auth Lambda live** with firmRole in both JWT generation and /auth/me response.
- **opal-partner-49financial** holds 3 records: Chase (user), Travis (admin), Hunter (admin).
- **opal-partners-49financial** (plural mistake) deleted.

## Open Items

1. **0.7.0_AE_CloudOps coordination** — MCP message delivered, awaiting reply. Topics: shared partner-perm Lambda lib (TS/Py), Terraform module for partner tables, IAM strategy (wildcard vs explicit), naming convention enforcement.
2. **Hand-created tables → Terraform** — opal-users-v2 + opal-partner-49financial were created via aws CLI for speed. Need TF import. (RULES.md R10)
3. **Auth handler still hardcodes `opal-partner-49financial`** — `db.ts` has `PARTNER_TABLE_49FIN` constant. Generalization to `opal-partner-{firmId}` blocked on the AE design conversation (where does the shared lib live?).
4. **Portal harness constitution still uncommitted** — `portal/.frontend-dev/testing/firm_user_gating_inspection.json` and Michael's plaintext password still pending Andrew's credential-handling decision (env var vs Secrets Manager vs accept-and-commit).

## Next Steps

- [Andrew] Decide credential handling for harness constitutions (open since 04-14 session).
- [0.7.0_AE_CloudOps] Reply on shared partner-infra design (MCP message 20260415T161839Z).
- [0.4.0_DT] Once AE replies: implement shared partner-perm lib + generalize auth handler.
- [0.4.0_DT] Once AE replies: TF-manage opal-users-v2 + opal-partner-{firmId} tables.
- [0.4.0_DE / 0.4.2_RD] No portal-side follow-up needed — firmRole consumption is in place.

---

— 0.4.0_DT_ClientPlatform

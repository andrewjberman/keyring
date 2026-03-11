# ADVI_APISCP.007 — Opal Capital Internal User Firm Selection — 2.0.0_SA_COO

**Date:** 2026-03-10

## Objective

Scope and decompose the Opal Capital firm access issue on Advisor Intelligence.
Opal users get 403 from shared-advisor-router because their JWT firmId resolves to
'null' (the string), which the router routes to opal-data-null (non-existent bucket).
Define the correct architecture and issue task orders to fix it.

---

## Problem Analysis

### Root Cause Chain

```
DynamoDB opal-users-v2:  firmId = null (JS null, or missing)
                                 |
jwt.js generateAccessToken:      const firmId = user.firmId || 'null'  <- string "null"
                                 |
auth-validator-edge:             X-Firm-Id: 'null'  (string "null" is truthy, not empty)
                                 |
shared-advisor-router:           bucket = 'opal-data-null'  <- does not exist -> 403
```

### Key Finding: firmId conflates two functions

For partner users, firmId serves both:
1. **Access gate** — "you can only see your firm's data"
2. **Firm selection** — "show me this firm's data"

These are the same for partners. For Opal Capital, they must be decoupled:
1. **Access gate** — Opal can see ALL firms (no restriction)
2. **Firm selection** — Opal picks which firm to view via a dropdown in the portal

### Architectural Decision

**firmId = 'opal-capital' for all Opal employees.** This is a positive identity
(not null/missing). The router recognizes 'opal-capital' as the Opal bypass signal.

**Firm selection via ?firm= query param.** The portal's existing `selectedFirmId`
state (already wired to the firm picker) provides the selected firm. Static API calls
append `?firm={selectedFirmId}` for internal users. The router reads this when
X-Firm-Id is 'opal-capital'.

**No new patterns invented.** Query params are the existing mechanism for firm
selection in dynamic calls (`?firmId=bd`). Static calls extend the same pattern
(`?firm=bd`). A separate param name (`?firm=` vs `?firmId=`) avoids confusion
between static (router) and dynamic (API Gateway) routing.

### Note: Prior draft discarded

An earlier draft of this log proposed an `X-Opal-Target-Firm` header. Andrew correctly
rejected this — it invented a new pattern. The query param approach is the right call.

---

## Work Completed

### 1. Root cause traced through full call chain

- `jwt.js:56` — `user.firmId || 'null'` confirms string "null" in JWT when DynamoDB has null
- `auth-validator-edge` — injects X-Firm-Id: 'null' (truthy, not caught by router guard)
- `shared-advisor-router` — routes to opal-data-null, S3 returns 403
- `002_migrate_users.py:115-118` — confirms migration already intended 'opal-capital' for
  Opal emails but may not have run for users created after migration

### 2. Patch script written

`infra/aws/auth/migration/004_patch_opal_firmid.py`

- Scans opal-users-v2 for all PROFILE records with @opalinvest.com email
- Runs DynamoDB UpdateItem SET firmId = 'opal-capital' (attribute-level, zero risk)
- Skips records already correct
- Dry-run mode + post-run verification built in
- Does NOT touch: passwordHash, email, PK, SK, or any auth fields

### 3. Task orders dispatched

| Agent | Task Order | Summary |
|-------|-----------|---------|
| 0.7.0_AE_CloudOps | ADVI_APISCP.007.opal-dynamo-patch-and-cf-cache.md | Run 004_patch_opal_firmid.py + update CF cache key to include 'firm' query param |
| 0.4.0_DT_ClientPlatform | ADVI_APISCP.007.router-v7-opal-routing.md | Router v7: when X-Firm-Id='opal-capital', read ?firm= param as routing firmId |
| 0.4.0_DE_ClientPlatform | ADVI_APISCP.007.portal-opal-firm-picker.md | Fix selectedFirmId default ('49financial'->'bd'), add ?firm= to static calls for internal users, gate firm picker to isInternal |

### 4. Execution order

```
[AE: DynamoDB patch] -- asap, Opal users need correct firmId in JWT
        |
        v (after DynamoDB patch complete)
[All three can proceed in parallel]
  [DT: router v7 deploy]           -- router safe to deploy before AE; inert until JWTs update
  [DE: portal commit to DEV]       -- inert until router v7 is live
  [AE: CF cache key update]        -- must complete before E2E
        |
        v (all three complete)
[DE: E2E verification]
  - Log in as Opal user
  - Confirm firm picker visible, page loads
  - Confirm ?firm=bd in static call URLs (network tab)
  - Log in as partner user
  - Confirm no ?firm= in URLs, no dropdown
```

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| firmId = 'opal-capital' (not null) | Positive identity; router checks strict equality. 002_migrate_users.py already set this correctly for migrated users — just need to patch any created after migration. |
| ?firm= query param (not new header) | Existing pattern — dynamic calls already use ?firmId=. No new CloudFront header forwarding needed. Cache key addition is straightforward. |
| ?firm= only for internal users on static calls | Partner users route via X-Firm-Id. Adding ?firm= for them is unnecessary and pollutes the cache key. |
| selectedFirmId default = 'bd' (not '49financial') | '49financial' is a display name; router routes to opal-data-{firmId}. Must be the S3 bucket suffix. |
| AE runs patch FIRST | Until JWT carries 'opal-capital', router v7 bypass never activates. Patch is the prerequisite. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `infra/aws/auth/migration/004_patch_opal_firmid.py` | DynamoDB patch script | No |
| `org/tier2_senior/0.7.0_AE_CloudOps/task_orders/ADVI_APISCP.007.opal-dynamo-patch-and-cf-cache.md` | AE task order | No |
| `org/tier2_senior/0.4.0_DT_ClientPlatform/task_orders/ADVI_APISCP.007.router-v7-opal-routing.md` | DT task order | No |
| `org/tier2_senior/0.4.0_DE_ClientPlatform/task_orders/ADVI_APISCP.007.portal-opal-firm-picker.md` | DE task order | No |
| `org/projects/ADVI_APISCP.json` | Phase 5 (ADVI_APISCP.007) recorded | No |
| This file | Session log | No |

---

## Blockers

None.

---

## Current State

**Status:** COMPLETE (COO scoping done; three task orders dispatched)
**Active branch:** CLOUD

Architecture decided, patch script written, three task orders ready. AE runs first
(DynamoDB patch). DT and DE can implement in parallel. E2E verify after all three live.

---

## Next Steps

1. **[0.7.0_AE_CloudOps] Run 004_patch_opal_firmid.py** — DynamoDB patch is the prerequisite. Run dry-run first, then execute. Then CF cache key Terraform.
2. **[0.4.0_DT_ClientPlatform] Deploy router v7** — opal-capital bypass + ?firm= routing. Can deploy before AE patch; inert until JWTs update.
3. **[0.4.0_DE_ClientPlatform] Portal firm picker** — fix selectedFirmId default, add ?firm= to static calls for internal users, gate dropdown to isInternal. Commit to DEV.
4. **[0.4.0_DE_ClientPlatform] E2E verify** — after AE + DT complete. Log in as Opal user, confirm page loads, firm picker visible, ?firm=bd in network tab.

**Do NOT:**
- Allow ?firm= to override routing for partner users — security boundary is strict
- Use the string 'null' as a firmId anywhere — the patch eliminates it

---

## Completion Record

**Status:** COMPLETE
**All three task orders confirmed complete by Andrew (2026-03-10).**

| Agent | Task Order | Status |
|-------|-----------|--------|
| 0.7.0_AE_CloudOps | ADVI_APISCP.007.opal-dynamo-patch-and-cf-cache | complete |
| 0.4.0_DT_ClientPlatform | ADVI_APISCP.007.router-v7-opal-routing | complete |
| 0.4.0_DE_ClientPlatform | ADVI_APISCP.007.portal-opal-firm-picker | complete |

ADVI_APISCP project marked complete in org/projects/ADVI_APISCP.json.
Full delivery: multi-tenant S3 routing for partner firms + Opal Capital firm picker.
Opal users see all partner data via dropdown. Partners see only their own data.

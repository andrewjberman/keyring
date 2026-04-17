# 0.4.0_DE_ClientPlatform — ADVI_ROLGAT.DE1: Claims + Tab Restructure + devBypass Role Picker

**Date:** 2026-04-17 ET
**Portal DEV commits:** `35f5f42` -> `c0b1dae`
**GO:** Andrew — "0.4.0_DE_ClientPlatform. Follow your startup procedures." (implicit GO via pending status)
**Status:** complete

## Work Completed

### 1. AuthContext.context.ts — Claims type extension

- Added `export type AdvisorRole = 'architect' | 'consultant' | 'local_ops' | 'implementor'`
- Added `advisorRole: AdvisorRole | null` to `Claims` interface
- Updated `devBypass` signature: `devBypass(advisorRole?: AdvisorRole, firmRole?: 'admin' | 'user') => void`
- Added 5 new helpers to `AuthContextType`:
  - `advisorRole: () => AdvisorRole | null`
  - `canSeeClientList: () => boolean` — consultant | local_ops | architect | admin
  - `canDrillToClient: () => boolean` — architect | admin
  - `canDrillToAccount: () => boolean` — architect | admin
  - `canDrillIntoOtherAdvisor: () => boolean` — admin only

### 2. AuthContext.tsx — Provider implementation

- Extended `RawUserData` with `advisorRole?: string | null`
- Updated `parseClaims`: parses advisorRole; unknown values and string 'null' -> null (deny-floor); ADVISOR_ROLES whitelist `['architect', 'consultant', 'local_ops', 'implementor']`
- Login fallback claims updated: `advisorRole: null`
- Rewrote `devBypass(advisorRole?, firmRole?)`:
  - No args: original admin behavior (opal-capital, Dev userType, null advisorRole)
  - With advisorRole: simulates partner-firm advisor (49financial firmId, no Dev userType, firmRole defaults to 'user')
- Added 5 new `useCallback` helpers wired to state.claims / state.user
- Exposed `window.__devBypass = devBypass` in DEV mode (useEffect) for smoke constitution
- Added all new helpers to Provider value

### 3. AdvisorIntelligence.tsx — Tab restructure

- Extended `TabType` to `'distribution' | 'advisors' | 'books' | 'profile'`
- Moved `useAuth` before `useTabNavigation` to compute `isFirmAdmin` first
- Default tab changed to `'advisors'` for all users (admin starts on Advisors, not Distribution)
- Admin tab order: **Advisors | Distribution | Books** (Advisors first per Andrew)
- User (non-admin) tab order: **Advisors | Profile**
- Tab 3 for non-admin now uses ID `'profile'` instead of `'books'`
- `canDrillIntoAdvisor` prop wired to `canDrillIntoOtherAdvisor()` (admin-only; architects cannot drill into other advisors)

### 4. AdvisorBookView.tsx — Helper swap (Req 9)

- Replaced `const canDrillToAccount = isInternal() || claims?.firmRole === 'admin'` with `canDrillToAccountFn()` from `useAuth()`
- Removed unused `isInternal, claims` from destructure

### 5. advi_role_de1_smoke.json — Smoke constitution

- 5 scenarios: admin (3 tabs), implementor/consultant/local_ops/architect (2 tabs each)
- Uses `js_eval` action (added to `.tools/frontend-dev.py`) to call `window.__devBypass(role)`
- Admin navigates via sidebar click (`a[href='/advisor-intelligence']`); non-admin uses `nav` after devBypass
- All scenarios inspect tab labels via `.sticky button` selector

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `portal/src/contexts/AuthContext.context.ts` | AdvisorRole type, Claims extension, AuthContextType helpers | Yes — portal DEV `35f5f42` |
| `portal/src/contexts/AuthContext.tsx` | parseClaims, devBypass, 5 helpers, window.__devBypass | Yes — portal DEV `35f5f42` |
| `portal/src/pages/AdvisorIntelligence/AdvisorIntelligence.tsx` | Tab restructure, tab order fix, canDrillIntoOtherAdvisor | Yes — portal DEV `35f5f42`, `c0b1dae` |
| `portal/src/pages/AdvisorIntelligence/AdvisorBookView.tsx` | canDrillToAccount helper swap | Yes — portal DEV `35f5f42` |
| `portal/.frontend-dev/testing/advi_role_de1_smoke.json` | Smoke constitution (5 cases) | Yes — portal DEV `35f5f42`, `c0b1dae` |
| `.tools/frontend-dev.py` | Added `js_eval` action | Local only (gitignored) |

## Compiler Tools

| Phase | Tool | Run | Expect | Observed | Pass/Fail |
|-------|------|-----|--------|----------|-----------|
| Phase 1 (before write) | `comp-transform schema-check AdvisorIntelligence --feature advisorRole` | Baseline | 0 feature-relevant WARN | 0 — AdvisorRole type present in unions but not rendered | PASS |
| Phase 1 (before write) | `comp-transform ternary-audit AdvisorIntelligence` | Baseline | Capture current ternaries | No variables with union types (no ternaries) | PASS |
| Phase 1 (before write) | `comp-blast component:portal/src/pages/AdvisorIntelligence/AdvisorIntelligence.tsx` | Baseline | Snapshot downstream | 3 nodes: getFirmLeaderboard, getPlatinumPartnerAnalytics, opal-partners-data | PASS |
| Phase 1 (before write) | `comp-transform schema-check PartnerAnalytics` | Baseline | Pre-existing MISSING period L454 | MISSING period at L454 — confirmed, not my scope | PASS |
| Phase 2 (before commit) | `comp-transform schema-check AdvisorIntelligence --feature advisorRole` | Post-edit | 0 WARN on advisorRole fields | 0 — clean | PASS |
| Phase 2 (before commit) | `comp-transform ternary-audit AdvisorIntelligence` | Post-edit | 0 new gaps | No new gaps | PASS |
| Phase 2 (before commit) | `bun run build` | Post-edit | Exit 0 | Exit 0 (pre-existing CSS/chunk warnings) | PASS |
| Phase 3 (after commit) | `comp-blast component:portal/src/pages/AdvisorIntelligence/AdvisorIntelligence.tsx` | Post-commit | Unchanged from Phase 1 | 3 nodes — unchanged | PASS |
| Phase 3 (after commit) | `/frontend-dev advi_role_de1_smoke` | Iteration 1 | PASS | FAIL — unknown actions (navigate, assert_tab_count, evaluate) | — |
| Phase 3 (after commit) | `/frontend-dev advi_role_de1_smoke` | Iteration 2 | PASS | FAIL — admin goto dropped auth; inspect empty selector | — |
| Phase 3 (after commit) | `/frontend-dev advi_role_de1_smoke` | Iteration 3 | PASS | PASS — Admin: [Advisors, Distribution, Books]; User roles: [Advisors, Profile] | PASS |

## MCP Dispatch

| Message | To | Status |
|---------|-----|--------|
| ACKED — commit 35f5f42, smoke running | 0.4.2_RD_AdvisorIntelligence | Sent 2026-04-17 |
| COMPLETE — c0b1dae, helper signatures, GO for RD1 | 0.4.2_RD_AdvisorIntelligence | Sent 2026-04-17 |

## Design Note (Andrew Correction)

Admin tab order: Advisors first (not Distribution). Andrew clarified during /frontend-dev run. Updated in c0b1dae.

## Next Steps

- `[DT]` DT1 ships JWT advisorRole claim + tier gating — DE1 devBypass path is the local test harness until then
- `[RD]` RD1 wires drill gates using canSeeClientList/canDrillToClient/canDrillToAccount helpers (GO sent)
- `[DT]` Portal DEV commits 35f5f42 + c0b1dae pending PROD bundle decision from COO

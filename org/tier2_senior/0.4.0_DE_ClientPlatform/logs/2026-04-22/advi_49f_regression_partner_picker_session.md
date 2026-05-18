# Session Log — ADVI 49F Regression + Partner Picker isDev Fix
**Agent:** 0.4.0_DE_ClientPlatform
**Date:** 2026-04-22
**Context:** Post-ADVI_INFLEC completion. Partner picker devBypass bug discovered and fixed. 49F regression validated.

## Summary

Two bugs found and fixed post-W5.8 close:
1. `devBypass()` no-arg set `firmId: null` — blocked `/advisor-intelligence` route (redirected to `/market`).
2. Root `AdvisorIntelligence` used only `isInternal()` for partner picker — `isDev()` users missed.

Both fixed. 49F regression (5 scenarios) + Inflection re-validation (5 scenarios) both PASS.

## Root Cause: devBypass firmId=null

`AuthContext.devBypass()` with no args is documented as "simulates Opal internal admin." However it set `firmId: null` instead of `'opal-capital'`. `ProtectedRoute` calls `isPathAllowedForFirm(claims?.firmId, location.pathname)`, which returns `false` for `null` → redirect to `/market`.

**Fix:** `AuthContext.tsx` line 493: `isAdvisorMode ? DEV_FIRM_ID : null` → `isAdvisorMode ? DEV_FIRM_ID : 'opal-capital'`

## Partner Picker isDev() Fix

Root `AdvisorIntelligence/index.tsx` gated the partner picker on `isInternal()` only. After the firmId fix, `isInternal()` returns `true` for no-arg bypass (firmId='opal-capital'), so the primary fix suffices. The `|| isDev()` guard was added as defense-in-depth.

**Fix:** `index.tsx`: `const internal = isInternal()` → `const internal = isInternal() || isDev()`

## /frontend-dev Results

### 49F Regression (new constitution)

| Iteration | Status | Blocking | Cosmetic | Notes |
|-----------|--------|----------|----------|-------|
| 1         | FAIL   | 4        | 0        | firmId=null → /market redirect; assertion text mismatch |
| 2         | PASS   | 0        | 0        | All 5 scenarios green after both fixes |

**Screenshots:** `.frontend-dev-results/20260422T131041Z/`
**Constitution:** `.frontend-dev/testing/advi_49f_regression_w5_refactor.json`

Scenarios:
- `49f-leaderboard-renders`: PASS — Advisor Intelligence heading visible, no errors
- `49f-distribution-tab`: PASS — Distribution tab renders, no errors
- `49f-books-tab`: PASS — Books tab renders, no errors
- `49f-partner-picker-visible`: PASS — "Select Partner:" label visible for Dev user
- `49f-no-inflection-data-leak`: PASS — no console errors

### Inflection Re-validation (no changes to Inflection path)

| Iteration | Status | Blocking | Cosmetic | Notes |
|-----------|--------|----------|----------|-------|
| 1         | PASS   | 0        | 0        | No regression from auth-context fix |

**Screenshots:** `.frontend-dev-results/20260422T131138Z/`

## Portal DEV Commits This Session

| SHA | Description |
|-----|-------------|
| `d48ebb8` | fix(ADVI): devBypass opal-capital firmId + isDev partner picker |

## Status

All ADVI_INFLEC DE work complete. Partner picker now functional in dev mode for Opal/Dev users.

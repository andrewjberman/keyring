# ADVI_REBORN.W5-005 -- Advisors Tab Data Path Fix
**Date:** 2026-04-08
**Start Time:** 5:00 PM ET
**Task Order:** ADVI_REBORN.W5-005 (from 1.0.0_SA_CTO, critical priority)
**Status:** Complete

**Portal DEV commits:** `d1968c2` (TS build fixes, pre-existing cleanup)
**Workspace CLOUD:** uncommitted (gold script NaN fix, pending commit)

---

## Investigation

CTO reported Advisors tab showing "No data available" despite W5-002 case fix
and confirmed S3 artifact (employee_leaderboard.json, 681KB, updated 2026-04-07).

### Layers Traced

| Layer | Status | Finding |
|-------|--------|---------|
| Gold script output (D_00 build_employee_leaderboard) | VERIFIED | Correct structure, 155 YTD entries, valid roles |
| S3 artifact (gold/artifacts/employee_leaderboard.json) | VERIFIED | 681KB, Content-Type application/json, correct ACL |
| CloudFront routing (behavior 2b: artifacts/*) | VERIFIED | Correct origin, Lambda@Edge (auth:9, router:10) attached |
| shared-advisor-router URI rewrite | VERIFIED | artifacts/ prefix handled at L112-114, rewrites to /gold/artifacts/ |
| Vite dev proxy | VERIFIED | Forwards to CloudFront, returns 401 JSON (not HTML) |
| Frontend fetch (getEmployeeLeaderboard) | VERIFIED | Correct path, auth header forwarded |
| **JSON parse** | **BROKEN** | `JSON.parse()` fails: NaN is not valid JSON |

### Root Cause

Gold script D_00.portal_aggregates.py line 1913 performs a left join:
```python
merged = merged.merge(fee_yield[['advisor', 'fee_yield_bps']], on='advisor', how='left')
```

Advisors with `implied_annual_fee` data missing after the join get `NaN` in
`fee_yield_bps`. Python's `json.dumps` serializes `NaN` as the literal text
`NaN` (non-standard extension). The browser's `JSON.parse()` throws
`SyntaxError: Unexpected token 'N'`, caught by the useEffect catch block,
setting `employeeData = null`. The entire Advisors tab renders empty.

**18 NaN occurrences** found in the live S3 file, all in `fee_yield_bps`.

### Why Other Endpoints Don't Have This Issue

Other gold artifacts (architect_leaderboard, partner_analytics, clients_tab)
either don't use left joins that produce NaN, or their numeric fields are
fully populated. The employee_leaderboard is the only artifact with a
fee_yield calculation from a separate data source (implied_annual_fee from
08c detail) that may be missing for some advisors.

---

## Fixes Applied

### Fix 1: Frontend -- NaN-safe JSON parse (immediate)
**File:** portal/src/api/endpoints/advisor-intelligence.ts
**Change:** `getEmployeeLeaderboard()` now reads the response as text and
replaces `NaN` with `null` before `JSON.parse()`. This handles the current
S3 file without waiting for a gold re-run.

### Fix 2: Gold script -- fillna on fee_yield_bps
**File:** data/black_diamond/scripts/gold/D_00.portal_aggregates.py
**Change:** Added `merged['fee_yield_bps'] = merged['fee_yield_bps'].fillna(0)`
after the left join (line ~1914). Prevents NaN from entering the JSON for this
specific field.

### Fix 3: Gold script -- _sanitize_nan safety net
**File:** data/black_diamond/scripts/gold/D_00.portal_aggregates.py
**Change:** Added `_sanitize_nan()` recursive helper called by `_save_json()`
before `json.dumps()`. Replaces all NaN/Inf floats with `None` (JSON null)
across any artifact. Prevents this class of bug from recurring in any field
or any artifact.

### Fix 4: TypeScript build errors (secondary)
**File:** portal/src/pages/AdvisorIntelligence/components/PartnerAnalytics.tsx
**Change:** Added missing `DistributionStats` type import.
**File:** portal/src/pages/AdvisorIntelligence/tabs/AdvisorsTab.tsx
**Change:** Added `metric` prop to `LeaderboardPinnedRow` signature.
These were build-time errors that don't affect Vite dev mode (esbuild skips
type checking) but would block production builds.

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| portal/src/api/endpoints/advisor-intelligence.ts | NaN-safe JSON parse in getEmployeeLeaderboard | No -- pending |
| portal/src/pages/AdvisorIntelligence/tabs/AdvisorsTab.tsx | LeaderboardPinnedRow metric prop + diagnostic removal | Yes - DEV `d1968c2` (partial) |
| portal/src/pages/AdvisorIntelligence/components/PartnerAnalytics.tsx | DistributionStats import | Yes - DEV `d1968c2` |
| data/black_diamond/scripts/gold/D_00.portal_aggregates.py | import math, fillna(0) on fee_yield_bps, _sanitize_nan in _save_json | No -- pending |

---

## Task Order Status

| Task Order | Project | Status |
|---|---|---|
| ADVI_REBORN.W5-005 | ADVI_REBORN | COMPLETE |

---

## Next Steps

1. **[DevOps 0.4.0_DT]** Commit and push portal DEV with NaN-safe parse fix
2. **[DevOps 0.4.0_DT]** Commit and push gold script D_00 NaN fixes to CLOUD
3. **[AE 0.7.0]** Upload D_00 to gold runner via S3, re-run to regenerate clean employee_leaderboard.json (removes the 18 NaN values at source)
4. **[Dashboard Engineer]** After gold re-run, verify the frontend NaN workaround can be removed (all artifacts should be clean after _sanitize_nan is in place)

# ADVI_49FNV3.F5 — YTD Calendar Key Added to Leaderboard Publishers — 0.4.0_DS_ClientPlatform

**Date:** 2026-03-09

## Objective

Add calendar-aligned `ytd` key to both leaderboard publisher Lambdas (`architect_leaderboard.json` and `implementor_leaderboard.json`). This is the data-side half of the F5 QTD/YTD fix. The `qtd` key already existed in both; only `ytd` was missing.

---

## Work Completed

### 1. bd-portal-advisor-publisher (implementor_leaderboard.json)

`build_implementor_leaderboard()` already had `qtd` appended to the window loop. Added `ytd` with start = `pd.Timestamp(year=today.year, month=1, day=1)`. Same aggregation path as all other windows. Updated `available_windows` to include `'ytd'`.

### 2. bd-portal-publisher (architect_leaderboard.json)

`build_architect_leaderboard()` already had `qtd` via `_quarter_start(today, 0)`. Added `ytd` using the same `_leaderboard_entries()` helper with Jan 1 start. Updated `available_windows` to include `'ytd'`.

### 3. DT Brief

Wrote deploy brief at `docs/briefs/devops-brief-49fnv3-f5-qtd-publisher-fix.md`. Both Lambdas are in the `bd-pipeline` Terraform module -- single plan/apply covers both.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Only added `ytd` (not `qtd`) | `qtd` already existed in both leaderboards. Task order requirement satisfied. |
| Modified bd-portal-publisher in addition to bd-portal-advisor-publisher | architect_leaderboard.json is built in bd-portal-publisher, not in bd-portal-advisor-publisher. Both needed the `ytd` key per task order requirements 1-2. |

---

## Briefs Written

| Brief | Path | Audience |
|-------|------|----------|
| DT deploy brief | `docs/briefs/devops-brief-49fnv3-f5-qtd-publisher-fix.md` | 0.4.0_DT_ClientPlatform |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `infra/aws/lambda/bd-pipeline/bd-portal-advisor-publisher/lambda_function.py` | Added `ytd` window to `build_implementor_leaderboard()` | Yes -- `edf8ac06` |
| `infra/aws/lambda/bd-pipeline/bd-portal-publisher/lambda_function.py` | Added `ytd` window to `build_architect_leaderboard()` | Yes -- `edf8ac06` |
| `docs/briefs/devops-brief-49fnv3-f5-qtd-publisher-fix.md` | New -- DT deploy brief | Yes -- `edf8ac06` |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_49FNV3.F5-fix.qtd-calendar-window.md` | Status: pending -> complete | This commit |

---

## Current State

**Status:** COMPLETE
**Active branch:** `CLOUD`

Both leaderboard publisher Lambdas now emit `qtd` and `ytd` calendar-aligned window keys. In Q1 (Jan-Mar), `qtd` and `ytd` produce identical date ranges (both start Jan 1). Existing trailing windows (3M, 6M, 1Y, 2Y, 3Y) are unchanged. Code committed locally at `edf8ac06`. DT must build, upload, and deploy both Lambdas via the bd-pipeline Terraform module. After deploy, DE updates `periodToChartWindow` in `AdvisorsTab.tsx` to map directly to the new keys.

---

## Next Steps

1. **[0.4.0_DT_ClientPlatform] Deploy both Lambdas** -- per `docs/briefs/devops-brief-49fnv3-f5-qtd-publisher-fix.md`
2. **[0.4.0_DE_ClientPlatform] Update periodToChartWindow** -- map `'qtd' -> 'qtd'` and `'ytd' -> 'ytd'` in `AdvisorsTab.tsx` after Lambda deploy confirms

**Do NOT:**
- Modify the portal frontend -- that is DE scope
- Change the existing trailing window keys (3M, 6M, 1Y, 2Y, 3Y)

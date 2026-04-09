# ADVI_49PUSH.027 -- Distribution P1 Data Audit

**Agent:** 0.4.0_DS_ClientPlatform~D
**Date:** 2026-04-09
**Project:** ADVI_49PUSH
**Commit:** 75d303ca
**Status:** COMPLETE. All 4 issues fixed. Pending AE re-run of D_01 + D_04.

---

## step_0: Geo Coverage Decision

Ran account-grain state coverage check on `accounts_dimension_latest.parquet`:

| Source | Coverage |
|---|---|
| accounts_dimension (all accounts) | 9,940 / 9,943 = **99.97%** |
| accounts_dimension (open accounts) | 9,570 / 9,573 = **99.97%** |
| client_dimension (relationships) | 3,591 / 3,591 = **100%** |

3 accounts missing state — all `client_country=USA`. Coverage exceeds 99.5% threshold.

**Decision: OPTION A — accounts for GEO-AUA.**
All four P1 views use account grain. `geo_aua_grain: "accounts"` added to D_01 output.
GEO-AUA radial subtext: "{N} Accounts" / "{X.X}% of firm accounts".

Posted to CTO inbox at 20260409T184116Z.

---

## Audit Findings

### Issue 1 (GEO-AUA: account_count + geo_aua_grain)

**Current state:** State segments had `client_count` (relationships from `num_relationships`) but no `account_count`. City segments had `client_count` mislabeled (it was actually account count). `geo_aua_grain` field absent from output.

**Fix (D_01 build_geo_view + _build_cities):**
- Added `account_count` to each state segment (distinct accounts in state_accts)
- Added explicit `account_count` to city segments (same value, correct label)
- Kept `client_count` on both for backward compat
- Added `geo_aua_grain: 'accounts'` to build_geo_view return
- Added `account_count` to geo metrics dict

### Issue 2 (GEO-NNA city drill Top 9+Other)

**Current state:** Y6b produced `by_city: {city_key: distribution_stats}` only. No actual NNA values per city. No Top 9+Other grouping.

**Fix (D_01 build_nna_geo_view Y6b):**
- Added `cities: [{key, label, value (signed NNA), aua (abs for donut sizing)}]` list to each state drill entry
- Sorted by abs(NNA) descending, Top 9 + Other applied
- Existing `by_city` distribution stats preserved alongside for bell curve
- States with <= 9 cities get no Other entry

### Issue 3a (ADV-AUA multi-role advisor coverage)

**Current state:** `build_adv_view` used `adv_ts` (nna_aua_by_advisor.parquet) — architect-only. Travis showed $395M vs $427M tagged across all roles. 53 segments (architect-only pool).

**Fix (D_01 build_adv_view):**
- New params: `account_team`, `firm_total_aua`, `firm_total_clients`
- When `account_team` available: iterate all 5 role columns (`architect`, `implementor`, `consultant`, `local_ops`, `additional_advisor`), compute per-advisor tagged_aua = sum of AUA for all tagged accounts. Same semantics as D_02 .006 multi-role fix.
- account_team has 163 unique named advisors across all roles (vs 53 architect-only)
- Architect-only fallback preserved when account_team unavailable
- Donut title: `'AUA by Advisor (All Roles)'`

### Issue 3b (ADV center total = firm headline AUA)

**Current state:** `adv.donut.total = $1,631,539,372` — wrong. Was sum of architect AUAs. Firm headline AUA = $1,617,911,902.

**Fix:**
- D_01 `build_adv_view`: accepts `firm_total_aua` param; uses it as donut total
- D_01 call site: computes `firm_total_aua = float(client_perf[date==ref_date]['total_aua'].sum())` (no extra S3 read)
- D_04 `build_partner_analytics`: safety-net override — reads `clients_tab.json` and overrides `adv[period]['donut']['total']` for all granularities

### Issue 3c (ADV relationship_count + pct_of_firm_clients)

**Current state:** ADV segments had `client_count` only (= relationship count from adv_ts.num_relationships). No explicit `relationship_count` or `pct_of_firm_clients`.

**Fix (D_01 build_adv_view):**
- Multi-role path: `relationship_count = len(advisor_rels[arch])` (unique rels tagged to advisor in any role), `pct_of_firm_clients = rel_count / firm_total_clients * 100`
- Fallback path: same fields added with architect-only counts
- `client_count` kept for backward compat

### Issue 4 (ADV-NNA per-advisor nna_clients.json)

**Current state:** `platinum/advisors/{id}/` only had `summary.json`. No `nna_clients.json`. ADV-NNA client drilldown non-functional in portal.

**Fix (D_04 build_advisor_nna_clients — Step 12):**
- Reads D_02 `book.json` client list for each advisor (client_key + client_name)
- Batch-reads `aua_timeseries.json` for all unique clients
- Computes QTD NNA per client: diff of cumulative NNA from quarter start to latest date
- Applies Top 9 + Other by abs(NNA)
- Writes `platinum/advisors/{id}/nna_clients.json` with: `{data_as_of, advisor_id, total_nna, client_count, clients: [{rel_id, display_name, nna, pct_of_advisor_nna}]}`
- `display_name` from book.json `client_name` (relationship-level, not account PII)

---

## Files Modified

| File | Change |
|---|---|
| `data/black_diamond/scripts/gold/D_01.partner_analytics.py` | Issues 1, 2, 3a, 3b, 3c |
| `data/black_diamond/scripts/gold/D_04.client_portal_summary.py` | Issues 3b (safety net), 4 (Step 12) |

---

## Commits

| SHA | Description |
|---|---|
| `75d303ca` | 0.4.0_DS_ClientPlatform: ADVI_49PUSH.027 Distribution P1 data audit |

Pushed to origin/CLOUD.

---

## Pending

1. **AE re-run D_01**: D_01 changes (multi-role ADV, geo_aua_grain, NNA city drill) need S3 upload + re-run to materialize in `gold/artifacts/partner_analytics/header_metrics_{gran}.json`.
2. **AE re-run D_04**: D_04 changes (Step 12 nna_clients, Issue 3b safety net, .023 pass-throughs) need upload + re-run.
3. **Spot-check after re-run**: Sample 2 states, 2 advisors. Verify:
   - State segments have both `account_count` and `client_count`
   - `geo_aua_grain: "accounts"` present at geo view level
   - ADV `donut.total` = $1,617,911,902 (not $1.63B)
   - Travis Penfield segment `aua` ~ $427M (multi-role, not $395M architect-only)
   - `platinum/advisors/travis_penfield/nna_clients.json` exists with client NNA data
4. **DE .028-.031**: Companion frontend TOs unblocked after AE re-run confirms data is correct.

---

## Next Steps

[AE 0.6.0] Upload D_01 and D_04 to S3, re-run. D_01 must run BEFORE D_04 (D_04 reads D_01 output).
[DE 0.4.0_DE] .028-.031 companion TOs: switch Distribution tab frontend to platinum/ paths using new geo_aua_grain field + account_count.

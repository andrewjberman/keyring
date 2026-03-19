# ADVI_MVP318 WS1 — Geo Timeseries Root Cause and Fix — 0.4.0_DS_ClientPlatform

**Date:** 2026-03-18
**Start Time:** post-DT diagnostic return
**End Time:** session end

## Objective

Diagnose and fix the WS1 segment analytics variance after DT returned the WS1-A
diagnostic result: geo timeseries view in `timeseries_chart.json` is completely
empty (0 categories, 0 data points). TX is in "Other" bucket with no individual
tracking. Root cause is data-side, not frontend windowing.

---

## Work Completed

### 1. DT Diagnostic Return — Interpreting the Result

DT ran `.tmp_segment_analytics_diag.py` and reported:

```
geo categories: []
geo data points: 0
TX is bucketed into 'Other' -- not individually tracked
ROOT CAUSE: TX is NOT in top-N geo categories (TOP_N_GEO=0)
```

The diagnostic prints `TOP_N_GEO=0` because `geo_categories = []`. This means
`top_states` (populated by `.nlargest(TOP_N_GEO=8, 'total_aua')`) is empty.
The entire geo timeseries — not just TX — produces no output.

The snapshot (`aua_by_state.json`) showing TX=$901M is stale from a prior Lambda
run. The most recent Lambda run wrote `timeseries_chart.json` with empty geo, but
`aua_by_state.json` was last written during a previous successful run before the
geo parquet was regenerated with the broken country encoding.

### 2. Root Cause Investigation

Read the full code path in both directions to identify what could make `top_states`
empty despite real US client data existing.

#### Code path in `build_timeseries_chart()`:

```python
# Step 1: Filter to US rows by country
geo_us = geo[geo['country'].isin(['USA', 'US', '']) | geo['country'].isna()].copy()

# Step 2: Find US-only latest date
latest_date_geo = geo_us['date'].max()  # NaT if geo_us is empty

# Step 3: Get latest snapshot rows
latest_geo = geo_us[geo_us['date'] == latest_date_geo]  # empty if NaT

# Step 4: Pick top 8 states by AUA
top_states = (
    latest_geo[latest_geo['state'].notna() & (latest_geo['state'] != '') &
               (latest_geo['state'] != 'Unknown')]
    .nlargest(TOP_N_GEO, 'total_aua')['state'].tolist()
)  # [] if latest_geo empty
```

If `geo_us` is empty, `latest_date_geo = NaT`, `latest_geo` is empty, and
`top_states = []`. All subsequent geo structures (`geo_by_date`, `geo_categories`,
`geo_data`) are also empty — matching the 0 categories / 0 data points result.

#### Source of the geo parquet (`07_build_nna_aua_by_geography.py`):

Script 07 builds the geo parquet using modal `client_country` from
`accounts_dimension_latest`. The critical logic in `_modal_geo()`:

```python
country = modal_str(grp[country_col], 'Unknown')  # returns BD's stored value

if country not in ('Unknown', '') and country != 'USA':
    state = ''  # treat as non-US: wipe state code
```

**The bug:** This check was written assuming BD stores US country as `'USA'`.
BD actually stores it as `'United States'` (full name). Since
`'United States' != 'USA'`, the condition evaluates to `True` for EVERY US client,
and `state = ''` is assigned to all of them.

The geo parquet therefore has:
- All US clients: `state = ''`, `country = 'United States'`
- No rows with `state IN ('TX', 'CA', 'NY', ...)` at current dates

Back in the Lambda filter:
```python
geo_us = geo[geo['country'].isin(['USA', 'US', '']) | geo['country'].isna()]
```

`'United States'` does not match `'USA'`, `'US'`, `''`, or `isna()` → `geo_us`
is empty → 0 categories, 0 data points in all geo views.

#### Why the snapshot aua_by_state.json still showed $901M:

`build_snapshots()` uses the same country filter as `build_timeseries_chart()`.
If the country filter returns empty, `state_agg` is also empty and
`aua_by_state.json` would have no states. The $901M TX value is from an older
Lambda run that executed before the geo parquet was last regenerated. S3 retains
the old file until the next successful write. The most recent Lambda run wrote
`timeseries_chart.json` with empty geo, but `aua_by_state.json` was not
overwritten (either because the Lambda failed partway through or because the
state data was also empty and the old file was not replaced).

This two-file discrepancy is what made the diagnostic appear to show a "gap"
between the snapshot and timeseries — they were actually from different runs.

### 3. The Fix (commit `fec1f7e4`)

Two changes committed together:

#### Fix 1 — `07_build_nna_aua_by_geography.py` (root cause)

Normalize BD country encoding variants to canonical `'USA'` before the state-wipe
check in `_modal_geo()`:

```python
# Before the non-US check:
if country in ('US', 'United States', 'United States of America'):
    country = 'USA'

# Now the original check works correctly:
if country not in ('Unknown', '') and country != 'USA':
    state = ''
```

After the next gold layer run that includes script 07, the geo parquet will have
correct two-letter state codes (TX, CA, NY, etc.) for all US clients.

#### Fix 2 — `bd-portal-publisher/lambda_function.py` (defensive)

Added module-level constant:

```python
_US_COUNTRY_VARIANTS = frozenset({
    'USA', 'US', 'United States', 'United States of America', ''
})
```

Replaced the hardcoded `isin(['USA', 'US', ''])` filter with `isin(_US_COUNTRY_VARIANTS)`
at all 4 filter sites:
- Line 652: `build_timeseries_chart()` — AUA geo view (`geo_us`)
- Line 927: `build_timeseries_chart()` — NNA geo view (`geo_us_nna`)
- Line 1617: `build_summary()` — geo donut view (`geo_us`)
- Line 1839: `build_snapshots()` — state snapshot (`geo_us`)

This makes the Lambda robust to future BD country encoding changes. Even if script
07 is not immediately re-run, the Lambda will correctly include 'United States'
rows when they appear in the parquet.

**Note:** Fix 2 alone is not sufficient because script 07 also wipes `state = ''`
for 'United States' rows. Both fixes are required for the geo view to be populated.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Fix script 07 as the primary fix | The Lambda fix alone doesn't help because script 07 also sets state='' for 'United States' rows. Root cause must be fixed at the source. |
| Add Lambda fix as defensive secondary | Prevents future regressions if BD encoding changes again. No downside. |
| Use frozenset constant for country variants | Single source of truth for all 4 filter sites; avoids drift between them. |
| WS1-C (RD subtitle) NOT needed | Root cause is data-side. Frontend windowing is not the issue. No RD action required. |
| Prescription A (geo_us_for_snap date anchor) is moot | The original Prescription A targeted a date anchor discrepancy in build_snapshots. That's a secondary concern. The primary issue is country encoding making geo_us empty in both functions. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `data/black_diamond/scripts/gold/07_build_nna_aua_by_geography.py` | Normalize 'United States'/'US' → 'USA' in `_modal_geo()` before state-wipe check | Yes — `fec1f7e4` |
| `infra/aws/lambda/bd-pipeline/bd-portal-publisher/lambda_function.py` | Add `_US_COUNTRY_VARIANTS` constant; replace 4 hardcoded country filters | Yes — `fec1f7e4` |

---

## Session Commit Summary (full session, ADVI_MVP318)

| SHA | Description |
|-----|-------------|
| `eb70758d` | feat(bd-portal-publisher): MTD window + QTD/YTD uppercase in architect_leaderboard (ADVI_MVPLVL.006) — NOTE: not Prescription A |
| `a3903a03` | feat(bd-portal-advisor-publisher): D4 architect override + WS3a advisor timeseries artifacts |
| `6234d50c` | feat(opal-partners-data): advisor timeseries + mix-timeseries route handlers (WS3c) |
| `fec1f7e4` | fix(bd-portal-publisher + gold-07): WS1 geo timeseries empty — BD country encoding mismatch |

---

## Current State

**Status:** COMPLETE
**Active branch:** `CLOUD`

All four DS commits for ADVI_MVP318 are on CLOUD. The WS1 fix (`fec1f7e4`) addresses
both the root cause (script 07 country normalization) and the Lambda defensive filter.
DT has already deployed WS2+WS3b (`a3903a03`) and WS3c (`6234d50c`). WS1 fix requires
a new bd-pipeline deploy (bd-portal-publisher) and a gold layer re-run of script 07
before the geo timeseries will appear in the portal.

---

## AE Completion (2026-03-18 — post-session update)

AE (`0.6.0_AE_PartnerETL`) completed the gold layer steps for WS1:

- Script 07 uploaded to `s3://opal-data-bd/code/gold/` and run in isolation ✓
- Geo parquet rebuilt — **TX $900.8M, 49 states, correct state encoding** ✓
- AE log committed and pushed at `b2119882`

Verification confirms the script 07 fix is correct: country normalization worked,
US clients now have proper two-letter state codes in `nna_aua_by_geography.parquet`.

## Next Steps

1. **[0.4.0_DT_ClientPlatform] Deploy bd-portal-publisher** — `fec1f7e4` is the only
   remaining gate. Geo parquet is already correct. After DT deploys the Lambda, the
   next pipeline trigger will write a correct `timeseries_chart.json` with 8+ state
   categories and TX as an individual series.
   - build-and-upload.sh bd-pipeline bd-portal-publisher
   - terraform plan/apply (bd-pipeline), 0-diff verify
   - Tag: check `git tag -l "bd-v*" | sort -V | tail -5` — likely bd-v2.19.1
   - push --follow-tags

2. **[0.4.0_DT_ClientPlatform] Re-run WS1-A diagnostic post-Lambda-trigger** — run
   `.tmp_segment_analytics_diag.py` after deploy + pipeline trigger to confirm:
   - `geo categories` non-empty (expects ~8 states + 'Other')
   - TX present as an individual category
   - TX AUA in timeseries aligns with snapshot

3. **WS1-C is NOT needed** — root cause confirmed data-side. No RD action.

**DS has no further action on WS1.** All DS commits are on CLOUD. WS1 is fully
gated on DT deploy only.

**Do NOT:**
- Attempt Prescription A (geo_us_for_snap date anchor) — wrong fix; real cause was
  country encoding mismatch, not date anchor difference
- Trigger a full gold run before DT deploys — the Lambda must be at fec1f7e4 when
  it next runs or the corrected geo parquet will be read by the old broken filter

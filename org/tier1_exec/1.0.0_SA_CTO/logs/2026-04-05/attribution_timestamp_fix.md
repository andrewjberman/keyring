# Attribution Page Timestamp Fix -- 1.0.0_SA_CTO

**Date:** 2026-04-05
**Project:** ADVI_GLDOPS (related -- yang pipeline data freshness)
**Pipeline:** yang-pipeline

---

## Problem

The Attribution page on the portal displayed "February 28th, 2026" as the data timestamp despite the underlying S3 data being current (data_as_of: 2026-03-31). Multiple CloudFront invalidations in a prior session (which crashed) failed to resolve the issue.

---

## Investigation Timeline

### Prior Session (crashed)

1. Andrew reported "Feb 28th 2026" on the Attribution page.
2. Checked S3 positioning files -- all three had correct `data_as_of: 2026-03-31`:
   - `positioning_data.json` (generated 2026-04-01)
   - `holdings_attribution_data.json` (generated 2026-04-02)
   - `allocation_summary.json` (generated 2026-04-01)
3. Assumed CloudFront cache. Invalidated `/json/positioning/*` -- wrong path (S3 path, not viewer-facing).
4. Invalidated `/api/general/positioning/*` -- correct viewer-facing path. Still no change.
5. Session crashed before resolution.

### This Session

1. Traced the portal code to find the actual data source for the displayed timestamp.
2. Found: Attribution page uses `SmartPanelFooter sourceKey="attribution_excel"`.
3. `SmartPanelFooter` -> `useDataFreshness()` -> reads `manifest.json` -> `sources.attribution_excel.data_as_of`.
4. Checked `manifest.json`: `attribution_excel.data_as_of = "2026-02-28"` -- stale.
5. Checked `json/latest/attribution_excel.json`: stuck at `data_as_of: 2026-02-28`, `original_filename: Model Portfolio Attribution 20260228.xlsx`.

---

## Root Cause

**Stale filename regex in the yang-pipeline trigger Lambda.**

The trigger Lambda (`yang_pipeline/orchestration/trigger/lambda_function.py`) writes `json/latest/{file_type}.json` metadata files during pipeline initialization. Its `FILE_TYPE_CONFIG` for `attribution_excel` had:

```python
'pattern': r'Models Relative Performance.*?(\d{8})\.xlsx'
```

But the canonical filename changed to `Model Portfolio Attribution YYYYMMDD.xlsx` starting with the Jan 31, 2026 data upload (uploaded Feb 5, 2026). The upload history:

| Upload Date | Filename |
|-------------|----------|
| 2026-01-02 | `Models Relative Performance vs New Benchmark 20251231.xlsx` |
| 2026-02-05 | `Model Portfolio Attribution 20260131.xlsx` |
| 2026-02-06 | `Model Portfolio Attribution 20260131 1.xlsx` (re-upload) |
| 2026-04-02 | `Model Portfolio Attribution 20260331.xlsx` |

The regex never matched the new filename, causing `extract_date_from_filename()` to throw `ValueError`. The `except Exception` block caught it silently and skipped the metadata write. Result: `json/latest/attribution_excel.json` was never updated after the filename convention changed.

Meanwhile, the downstream `yang-generate-holdings-attribution` Lambda uses a simpler regex (`re.search(r'(\d{8})', filename)`) that matched fine -- so `holdings_attribution_data.json` had correct data. But the portal's timestamp comes from the manifest (via `attribution_excel.json`), not from the holdings data file.

### Why CloudFront invalidation didn't help

The data in S3 was already stale (`attribution_excel.json` had the wrong date). CloudFront was faithfully serving the stale S3 content. Invalidating the cache just re-fetched the same wrong data.

### Secondary issue: timestamp format

After fixing the data, the portal initially displayed "March 2026" instead of the full canonical "March 31st, 2026, 5:00p ET". This was because the manifest entry had `timestamp: null`. The `formatPanelTimestamp()` function in `portal/src/lib/dateUtils.ts` has a branch (line 540):

```typescript
if (frequency === 'monthly' && dataAsOf && !timestamp) {
    // renders "March 2026" -- month+year only
}
```

Without a timestamp, it fell into the monthly shorthand format. Adding the canonical 5pm ET timestamp (`2026-03-31T17:00:00-04:00`) caused it to fall through to the full timestamp parser (line 552), producing the correct display.

---

## Fix Applied

### 1. Code fix (local, not yet deployed)

**File:** `infra/aws/lambda/v2_portal/yang_pipeline/orchestration/trigger/lambda_function.py` line 398

```python
# Before
'pattern': r'Models Relative Performance.*?(\d{8})\.xlsx',

# After
'pattern': r'Model Portfolio Attribution.*?(\d{8})\.xlsx',
```

### 2. Manual S3 corrections (immediate)

- Wrote corrected `json/latest/attribution_excel.json` with `data_as_of: 2026-03-31` and canonical `timestamp: 2026-03-31T17:00:00-04:00`
- Regenerated `json/latest/manifest.json` from all `json/latest/*.json` source files, applying canonical 5pm ET timestamps to all entries
- Invalidated both CloudFront distributions (`EVTSA9VEHNZVH` + `E2LPCXXBLDGWXY`) with `/*`

### 3. Remaining work

- **Terraform deploy** of the trigger Lambda code change -- required for the fix to be permanent. Next time Yang uploads an attribution Excel, the trigger Lambda needs the updated regex to write `attribution_excel.json` automatically.
- This is a DS (code change) -> DT (deploy) cycle via normal protocol.

---

## Files Changed

| File | Change |
|------|--------|
| `infra/aws/lambda/v2_portal/yang_pipeline/orchestration/trigger/lambda_function.py` | Regex pattern for `attribution_excel` updated to match current filename convention |
| `s3://opal-data-portal-v2/json/latest/attribution_excel.json` | Manual write: data_as_of 2026-02-28 -> 2026-03-31, added canonical timestamp |
| `s3://opal-data-portal-v2/json/latest/manifest.json` | Regenerated with correct attribution_excel entry and canonical timestamps |

---

## Lessons

1. **Silent exception handling masks data freshness failures.** The trigger Lambda's `except Exception: continue` pattern meant the metadata write failure was invisible -- no alarm, no log surfaced to operators. A failed metadata write should at minimum emit a WARN-level log that appears in monitoring.
2. **Filename convention changes need to propagate to all consumers.** The attribution Lambda was updated for the new name but the trigger Lambda's config was not.
3. **CloudFront invalidation is not a fix when the S3 source itself is stale.** Always verify the S3 content before assuming cache.

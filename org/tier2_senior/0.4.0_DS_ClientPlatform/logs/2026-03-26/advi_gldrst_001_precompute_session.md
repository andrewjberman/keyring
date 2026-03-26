# ADVI_GLDRST.001 — Pre-compute L3 Quarterly Views Session Log

**Agent:** 0.4.0_DS_ClientPlatform
**Date:** 2026-03-26
**Project:** ADVI_GLDRST
**Task Order:** ADVI_GLDRST.001.ds-precompute-l3-quarterly-views.md

---

## WS1: L3 Relationship Period Views (script 06b)

### Changes

Modified `06b_build_client_mix_timeseries.py`:

1. **Added `_write_relationship_views()`** — writes `gold/client_timeseries/{relationship_id}_views.json` per relationship. Same S3 write pattern as `_write_relationship_json()`.

2. **Full build path (`_build_and_write`)** — after accumulating daily mix entries, builds a `daily_dict` (dollar amounts reconstructed from pct * total_mv) and calls `compute_period_views()`. Writes `_views.json` alongside the daily JSON. Also stores `total_mv` in each mix entry for incremental reconstruction.

3. **Incremental path (`_merge_and_write`)** — after merging existing + new daily entries, rebuilds `daily_dict` from the full merged mix_list (using `total_mv` stored per entry). Recomputes `_views.json` from the complete accumulator on every incremental run (R2 compliance).

### Schema

```json
{
  "generated_at": "ISO8601Z",
  "data_as_of": "YYYY-MM-DD",
  "relationship_id": "...",
  "views": {
    "quarterly": [FirmMixPeriodPoint...],
    "monthly": [FirmMixPeriodPoint...],
    "annually": [FirmMixPeriodPoint...]
  }
}
```

Matches `firm_mix_views.json` and advisor `mix.json` schema exactly. Uses the same `compute_period_views()` function (no duplication).

### Artifact Estimates

- ~1,400 relationships
- ~5-10KB each `_views.json`
- ~15MB total additional S3 storage
- compute_period_views() is O(n) on daily entries, <10ms per relationship
- Runs inside existing ThreadPoolExecutor write phase -- no concurrency changes needed

### Incremental Design Note

`total_mv` is added to each mix date entry in the relationship JSON. This is an additive schema change (backward-compatible). Legacy entries without `total_mv` are silently skipped during views reconstruction -- they will be populated on the next full rebuild. Since AE is running a full gold rerun (ADVI_GLDRST.002), all entries will have `total_mv` after the first run.

---

## WS2: L3 Relationship Composition (script 12)

### Changes

Modified `12_build_composition_artifacts.py`:

1. **Added Step 7** — after firm (Step 5) and advisor (Step 6) composition, iterates over all unique `relationship_id` values in holdings_lots and calls `_build_composition()` for each.

2. **Output:** `gold/client_timeseries/{relationship_id}_composition.json` — same schema as `firm_composition.json` with `scope = {"relationship_id": "...", "firm_id": "49financial"}`.

### R4 Gate: relationship_id Join Method

**No join needed.** `holdings_lots.parquet` already includes `relationship_id` as a column (loaded at line 341). The column was verified present in the `_read_parquet()` call's column list: `['account_id', 'relationship_id', 'ticker', 'asset_name', 'market_value', 'is_open']`.

Ghost exclusion and AP gate are already applied to `lots` before Step 7, so relationship composition inherits the full canonical exclusion stack from `lib/exclusions.py`.

### Artifact Estimates

- ~1,400 relationships with non-empty holdings
- ~2-5KB each `_composition.json` (top-9 per class, compact JSON)
- ~5MB total additional S3 storage
- Replaces Lambda `handle_books_composition()` on-the-fly compute (~3s per request)

---

## Next Steps

### For DE (0.4.0_DE_ClientPlatform) — ADVI_GLDRST.003

Wire portal to read pre-computed views:
- L3 quarterly bar: read `{relationship_id}_views.json` instead of deriving from daily timeseries
- L3 composition: read `{relationship_id}_composition.json` instead of calling Lambda `handle_books_composition()`
- Remove `deriveQuarterlyFromTimeseries()` client-side logic for L3

### For AE (0.6.0_AE_PartnerETL) — ADVI_GLDRST.002

Run full gold layer rebuild to generate all new artifacts:
- 06b will write `_views.json` for all ~1,400 relationships
- 12 will write `_composition.json` for all ~1,400 relationships
- Verify artifact counts match relationship count in summary output

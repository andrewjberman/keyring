# ADVI_TICKID.004 -- detect_new_securities Enhancement Session Log

**Agent:** 0.4.0_DS_ClientPlatform
**Date:** 2026-03-26
**Project:** ADVI_TICKID
**Task Order:** ADVI_TICKID.004.ds-detect-new-securities-enhancement.md

---

## Changes

Modified `data/black_diamond/scripts/gold/detect_new_securities.py`:

1. **Resolution-aware filtering**: loads `ticker_resolution.parquet` from S3 and skips any asset_name that already has a resolution. Only truly new/unresolved securities get DynamoDB stubs.

2. **Auto-prefix matching**: for tickerless names >= 20 chars, checks if the normalized name is a prefix of any bd-securities `asset_name_raw`. Catches BD-truncated names that would otherwise create unnecessary stubs.

3. **Graceful fallback**: if `ticker_resolution.parquet` doesn't exist, falls back to original behavior (all tickerless names checked against DynamoDB, no resolution filtering).

4. **Summary output**: prints detection summary with counts for each category (already resolved, prefix-matched, truly unresolved) and top 10 unresolved by market value.

5. **Market value aggregation**: unique_pairs now includes market_value sum per (ticker, asset_name) for the unresolved MV ranking.

## Existing Behavior Preserved

- DynamoDB stub creation for truly new securities is unchanged
- `normalize_key()` logic unchanged
- `--upload` flag behavior unchanged
- Script still runs as `|| true` in gold layer (non-blocking)

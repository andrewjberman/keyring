# ADVI_TICKID.001 -- Ticker Resolution Table Session Log

**Agent:** 0.4.0_DS_ClientPlatform
**Date:** 2026-03-26
**Project:** ADVI_TICKID
**Task Order:** ADVI_TICKID.001.ds-build-resolution-table.md

---

## Deliverable

Created `data/black_diamond/scripts/classification/resolve_tickers.py`.

## Resolution Methods Implemented

| # | Method | Confidence | Description |
|---|--------|-----------|-------------|
| 1 | bd_feed | 1.0 | Ticker already in holdings_lots for this asset_name |
| 2 | bd_securities_exact | 1.0 | Exact match on asset_name_raw or name_aliases in DynamoDB |
| 3 | bd_securities_prefix | 0.95 | BD truncated name is prefix of DynamoDB asset_name_raw (20+ chars) |
| 4 | etf_classification_alias | 0.95 | Match in ASSET_NAME_TO_TICKER dict (etf_classification.py) |
| 5 | individual_stock_pattern | 0.85 | Placeholder -- needs external lookup (Yahoo) for ticker resolution |
| 6 | mutual_fund_pattern | 0.80 | Fund name stem match against DynamoDB items |

### Design Notes

- **normalize_asset_name()** exported as reusable function for script 03 join: `lowercase, strip, collapse spaces`
- **bd_feed** resolves names that have tickers in SOME rows but not others (same asset_name, different accounts)
- **bd_securities_prefix** handles BD's ~30-char truncation by checking if the BD name is a prefix of a DynamoDB asset_name_raw
- **individual_stock_pattern** returns empty for now -- pattern detection works but requires external ticker lookup (Yahoo Finance, future phase)
- **mutual_fund_pattern** matches fund name stems after stripping share class suffixes (CLASS A, CL I, etc.)
- ASSET_NAME_TO_TICKER loaded via importlib from `infra/aws/lambda/v2_portal/_shared/etf_classification.py` (88 entries)

### Output Schema

| Column | Type | Description |
|--------|------|-------------|
| asset_name_normalized | str | Normalized BD asset name (PK for join) |
| asset_name_raw | str | Exact BD asset name (for debugging) |
| resolved_ticker | str | Canonical ticker symbol |
| resolution_method | str | How the ticker was resolved |
| confidence | float | 0.0-1.0 |
| last_updated | str | ISO8601 timestamp |

## Coverage Metrics

Script must be run against live S3 data to produce actual coverage numbers. Expected:
- bd_feed should resolve a significant portion (names that have tickers in some but not all rows)
- bd_securities_exact + prefix should catch most ETFs and structured products
- etf_classification_alias provides the curated Opal-specific mappings
- Target: >80% of tickerless asset names resolved

## Commit

Pending -- see git log after commit.

## Next Steps

### .002 (script 03 join)
- Modify `03_build_holdings_lots.py` to join with `gold/dimensions/ticker_resolution.parquet`
- `lots['ticker'] = lots['ticker'].fillna(lots['resolved_ticker'])`
- Use `normalize_asset_name()` from resolve_tickers.py for join key

### .003 (DynamoDB name alias backfill)
- For every resolved (asset_name, ticker) pair, add asset_name to name_aliases on the bd-securities item
- Belt-and-suspenders: enrichment (.002) makes Layer 1 work; aliases (.003) make Layer 2 work

### .004 (detect_new_securities enhancement)
- Flag holdings where ticker=None AND no resolution exists
- Report unresolved count in pipeline manifest

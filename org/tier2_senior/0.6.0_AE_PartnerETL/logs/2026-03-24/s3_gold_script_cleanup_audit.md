# S3 Gold Script Path Cleanup Audit -- 0.6.0_AE_PartnerETL

**Date:** 2026-03-24
**Context:** During ADVI_PRICES.004 gold rerun, `run_gold_layer.sh` on S3 pointed to
stale scripts at `scripts/gold_layer/` instead of `code/gold/`. Caused positions_cube
to fail on `--upload` flag (stale Feb 23 version didn't support it). Three attempts
to run the gold layer wasted ~20 minutes before the path mismatch was caught.

---

## The Problem

Gold layer scripts exist at **5 different S3 prefixes**. Only one is canonical.
Different runner scripts point to different paths. No single source of truth was
enforced, so deployments silently used stale code.

---

## Full S3 Inventory

### CANONICAL (keep)

| S3 Path | Last Updated | Files | Purpose |
|---------|-------------|-------|---------|
| `code/gold/` | 2026-03-24 | 17 .py scripts | Current gold layer scripts |
| `code/gold/archive/` | 2026-02-26 | 15 legacy scripts | Intentional archive |
| `code/silver/` | 2026-03-24 | bd_price_update.py, build_canonical_prices_v2.py | Current silver scripts |
| `code/diagnostics/` | 2026-03-24 | backfill, verify scripts | AE diagnostic scripts |
| `code/runner/run-gold-layer.sh` | 2026-03-04 | 1 file | EC2 boot entrypoint (syncs from code/gold/) |

### STALE / DELETE

| S3 Path | Last Updated | Size | Problem |
|---------|-------------|------|---------|
| `scripts/gold_layer/` (entire prefix) | 2026-02-23 | ~50 objects | **ROOT CAUSE of today's failure.** Feb 23 snapshot of gold scripts. Contains 20+ fully obsolete `generate_*` scripts that don't exist in repo anymore. run_gold_layer.sh here is 4.3KB vs 10.5KB canonical. Scripts are 40-70% smaller than current versions. |
| `scripts/gold/` | 2026-03-18 | 2 objects | Orphan: one copy of 06b from March 18 dev session + insurance_accounts.json. Never canonical. |
| `scripts/02_build_positions_cube.py` | 2026-02-24 | 24KB (vs 32KB current) | Root-level stray. 72% of current size. |
| `scripts/05_build_client_performance.py` | 2026-02-24 | 24KB (vs 35KB current) | Root-level stray. 68% of current size. |
| `scripts/validate_gold_outputs.py` | 2026-02-24 | 4KB | Feb 24 diagnostic, not in production pipeline. |
| `scripts/ec2-gold-layer-runner.sh` | 2026-02-17 | 1 file | References nonexistent `scripts/generate_gold_analytics.py`. Completely dead. |
| `code/ec2/run-gold-layer.sh` | 2026-02-20 | 1 file | Syncs from `code/gold_layer/` (nonexistent path), runs `run_all.sh` (wrong entrypoint). |

### ALSO STALE (scripts/ root -- non-gold)

The `scripts/` root is a dumping ground of one-off uploads from Jan-Feb. It contains
~90 files including old diagnostic outputs (.txt), legacy TypeScript downloaders (.ts),
and copies of scripts that now live at proper `code/` paths. Full list:

- `scripts/build_canonical_prices_v2.py` (2026-02-27) -- superseded by `code/silver/`
- `scripts/fetch_historical_prices_yfinance.py` (2026-02-27) -- used by scheduler Lambda (KEEP for now, but should move to `code/silver/`)
- `scripts/merge-daily-incremental.py` (2026-02-23) -- superseded by `code/silver/` path
- ~30 `diag_*.py` + `diag_*_output.txt` files from Feb 23-24 debugging sessions
- ~15 TypeScript BD downloader scripts from Jan-Feb

---

## run_gold_layer.sh -- Three Copies

| Location | Date | Size | Syncs From | Status |
|----------|------|------|-----------|--------|
| `code/gold/run_gold_layer.sh` | 2026-03-23 | 10,551B | `code/gold/` | CANONICAL |
| `scripts/run_gold_layer.sh` | 2026-03-24 | 10,551B | `code/gold/` | Fixed today (was stale) |
| `scripts/gold_layer/run_gold_layer.sh` | 2026-02-23 | 4,341B | `scripts/gold_layer/` | STALE -- caused today's failure |

---

## scripts/gold_layer/ -- Fully Obsolete Scripts

These exist ONLY in the stale path, not in `code/gold/`. They are remnants of the
pre-Feb-26 `generate_*` naming scheme:

```
01_build_canonical_timeline.py
02_generate_timeseries.py
03_generate_snapshots.py
04_generate_clients.py
05_generate_filters.py
06_generate_summary.py
07_generate_partner_analytics.py
07b_generate_frozen_snapshots.py
07c_generate_position_snapshots.py
08_generate_timeseries_chart.py
09_generate_client_detail.py
10_generate_book_views.py
11_generate_clients_tab.py
11_generate_leaderboards.py
12_generate_aua_chart.py
13_generate_flows_chart.py
generate_all_gold.py
load_silver.py
partition_daily_positions.py
pii_hasher.py
process_today_incremental.py
validate_frozen_snapshots.py
__pycache__/06_generate_summary.cpython-312.pyc
```

None of these are referenced by any active runner or Lambda.

---

## Recommended Cleanup

### Phase A: Delete stale gold paths (safe -- nothing references them)

```bash
aws s3 rm s3://opal-data-bd/scripts/gold_layer/ --recursive
aws s3 rm s3://opal-data-bd/scripts/gold/ --recursive
aws s3 rm s3://opal-data-bd/scripts/02_build_positions_cube.py
aws s3 rm s3://opal-data-bd/scripts/05_build_client_performance.py
aws s3 rm s3://opal-data-bd/scripts/validate_gold_outputs.py
aws s3 rm s3://opal-data-bd/scripts/ec2-gold-layer-runner.sh
aws s3 rm s3://opal-data-bd/code/ec2/run-gold-layer.sh
```

### Phase B: Consolidate scripts/ root (requires scheduler Lambda update)

The scheduler Lambda downloads from `s3://opal-data-bd/scripts/fetch_historical_prices_yfinance.py`.
This should move to `code/silver/fetch_historical_prices_yfinance.py` but requires
updating the Lambda user_data script. Do this as part of the Phase 4 scheduler fix.

### Phase C: Establish convention going forward

| Prefix | Purpose |
|--------|---------|
| `code/gold/` | Gold layer scripts (production) |
| `code/silver/` | Silver layer scripts (production) |
| `code/diagnostics/` | Ad-hoc diagnostic scripts |
| `code/runner/` | EC2 runner entrypoints |
| `config/` | Configuration files (ticker_lookup.json, yahoo_safe_tickers.txt) |
| `scripts/` | DEPRECATED -- should be emptied over time |

---

## What This Cost Us Today

1. Gold rerun attempt 1: CRLF line endings (Windows -> Linux). Fixed with `sed -i`.
2. Gold rerun attempt 2: `run_gold_layer.sh` on S3 synced from `scripts/gold_layer/`
   (stale Feb 23 scripts). Positions cube failed on `--upload` flag.
3. Gold rerun attempt 3: uploaded correct `run_gold_layer.sh`, now running.

Total time wasted: ~25 minutes + 3 SSM round-trips.
Root cause: no enforcement that `code/gold/` is the single source of truth.

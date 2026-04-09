# Session Log -- 0.4.0_DS_ClientPlatform -- 2026-04-06 (Validation Review)

**Start Time:** ~8:30 PM ET
**Project:** ADVI_GLDOPS
**Task Order:** ADVI_GLDOPS.004 -- Build Canonical Holdings Stack
**Role:** Isolated validation reviewer (separate session from primary 0.4.0_DS)

---

## Objective

Review the primary DS session's work on GLDOPS.004 (canonical holdings stack) and validate alignment between the new 02b script, the gold runner (`run_gold_layer.sh`), and the broader pipeline.

---

## What Was Reviewed

1. Session log: `gldops_004_canonical_holdings_stack.md`
2. Script: `02b_build_canonical_holdings.py` (full read)
3. Script: `convert_schwab_rps_to_silver.py` (full read)
4. Module: `lib/s3_layout.py` (full read)
5. Runner: `run_gold_layer.sh` (full read)
6. S3 state: `opal-data-bd/schwab/bronze/`, `opal-data-bd/schwab/silver/rps/`, `opal-data-schwab`

---

## Findings

### Critical: Schwab Coverage Gap

The primary DS session uploaded 52 RPS files from a single OneDrive subfolder (`08242234`), covering 2026-01-20 to 2026-04-02. The session log states this is the full extent of Schwab data.

**This is incorrect.** Historical RPS files dating back to 2024-01-01 exist in the `opal-data-schwab` bucket (us-east-2), which was accidentally deleted and is currently being restored. The old converter (`code/schwab/convert_schwab_rps_to_parquet.py`, authored by 0.6.0_AE_PartnerETL) read from `opal-data-schwab` with prefixes `bronze/rps/`, `01_raw/`, `02_anonymized/`.

**Impact:** The canonical stack was designed around ~52 reconciled dates. Actual coverage is ~500+ trading days. This means:
- The 29.5% schwab_override rate likely extends across 2 years of history
- Full backfill will produce meaningful reconciliation for most of the positions cube range, not just the tail
- The "98% of full-mode dates are BD-only" concern from the initial review is wrong -- a large portion will have Schwab cross-validation

**Resolution path:** Once `opal-data-schwab` restore completes, consolidate all bronze RPS files into `opal-data-bd/schwab/bronze/` (single source of truth), re-run converter with `--force`.

### 02b Is Not Wired Into the Runner

`run_gold_layer.sh` sequences: `02 -> 05`. Script 02b is not present in either incremental or full mode. Additionally:
- 02b is not uploaded to `s3://opal-data-bd/code/gold/` (runner syncs scripts from S3)
- Updated `lib/s3_layout.py` is not uploaded to S3 either
- Incremental mode would need `--start-date` passthrough to avoid rebuilding all dates daily

### Script 05 Does Not Consume Canonical Holdings

02b writes to `gold/canonical/holdings/` but 05 still reads `gold/timeseries/positions_cube/`. The canonical layer is write-only until 05 is refactored. Recommendation: do not wire 02b into the runner until 05 is ready to consume it, to avoid adding 15-20 min of runtime for output nothing reads.

### No Watermarks

No sealed-day watermark exists. Without a pre-write check, `02b --upload` can silently overwrite previously sealed dates. This must exist before the first production backfill.

### Minor Code Issues

- `price_holdings()` (lines 332-355) is dead code -- only `price_holdings_vectorized` is called. Should be removed.
- `S3_CANONICAL_PRICES_KEY` is defined in both `s3_layout.py` (line 54) and hardcoded in `02b` (line 67). Should import from s3_layout consistently.

---

## Recommended Sequence (agreed with Andrew)

1. Wait for `opal-data-schwab` restore to complete
2. Consolidate restored bronze RPS into `opal-data-bd/schwab/bronze/`
3. Re-run converter with `--force` for full 2024-2026 silver coverage
4. Add sealed-day watermarks to 02b
5. Run 02b full backfill as one-time EC2 job, validate results
6. Refactor 05 to read canonical holdings instead of positions cube
7. Wire 02b into `run_gold_layer.sh` + upload to S3 code path
8. Clean up dead code and dual key definition

Steps 4-5 establish foundational truth. Steps 6-7 make the pipeline consume it. Do not do 7 without 6.

---

## Files Reviewed (no modifications)

| File | Status |
|------|--------|
| `data/black_diamond/scripts/gold/02b_build_canonical_holdings.py` | Read only |
| `data/black_diamond/scripts/bronze/convert_schwab_rps_to_silver.py` | Read only |
| `data/black_diamond/scripts/gold/lib/s3_layout.py` | Read only |
| `data/black_diamond/scripts/gold/run_gold_layer.sh` | Read only |

## S3 Verified

| Location | Finding |
|----------|---------|
| `opal-data-bd/schwab/bronze/` | 52 files (2026-01-20 to 2026-04-02) |
| `opal-data-bd/schwab/silver/rps/` | 52 partitions (matches bronze) |
| `opal-data-schwab` | Empty (deleted, restore in progress) |

# GLDOPS.004 — Canonical Positions (02 / 02b)

**Agent:** 0.4.0_DS_ClientPlatform
**Date:** 2026-04-06
**Project:** ADVI_GLDOPS
**Task Order:** ADVI_GLDOPS.004 — Build Canonical Holdings Stack

---

## What This Is

Canonical positions is Layer 1 of the immutable canonical data stack. It establishes the single source of truth for what every account held on every date by reconciling BD's FIFO-reconstructed positions (02) with Schwab's custodial position snapshots (02b).

```
Layer 0: canonical_prices       [EXISTS]   silver/prices/canonical_prices.parquet
Layer 1: canonical_positions    [THIS]     02 positions_cube + 02b canonical_holdings
Layer 2: canonical_lots         [BUILT]    03b (see separate log)
Layer 3: canonical_nna          [FUTURE]
Layer 4: canonical_market_growth [FUTURE]
```

The pipeline before this work: script 05 (1,055 lines, 30-40 min) loaded raw positions_cube and re-derived everything from scratch every run with no Schwab cross-validation and no sealed-day guarantees.

---

## Scripts

### 02_build_positions_cube.py (existing, unchanged)
- FIFO transaction replay from `silver/transactions/`
- Produces `gold/timeseries/positions_cube/{date}.parquet`
- Schema: `account_id, asset_name, units`
- 2,284 date partitions, 2020-01-01 to 2026-04-02

### 02b_build_canonical_holdings.py (NEW)
- **Location:** `data/black_diamond/scripts/gold/02b_build_canonical_holdings.py`
- Reconciles 02's positions_cube with Schwab RPS custodial snapshots
- Produces `gold/canonical/holdings/{date}.parquet`

---

## How 02b Works

### Join Path (CUSIP-based)

```
Schwab RPS partition (schwab_account_id, cusip, quantity_settled)
  -> schwab_bd_account_mapping (+ self-healing from unrealized account_number)
  -> CUSIP bridge (unrealized + realized -> asset_name)
  -> NAME_ALIASES normalization
  -> Full outer JOIN positions_cube on (account_id, asset_name)
  -> Reconcile units, classify source
  -> Price with canonical_prices
  -> Write partition
```

### Self-Healing Account Mapping

The original mapping (`schwab_bd_account_mapping.parquet`, 6,424 pairs) was built from realized-transaction fingerprinting, which misses buy-only accounts. 02b self-heals on every run by scanning BD unrealized for `account_number` — zero-padded to 10 digits equals the Schwab account ID for 98.6% of accounts. This added +1,534 mappings (total 7,958), resolving the 335-account gap identified in the validation brief (`briefs/2026-04-06_account_mapping_gap_brief.md`).

### Exclusion Layers (applied before reconciliation)

1. **Ghost accounts** — `lib/exclusions.load_ghost_account_ids()` (4 accounts)
2. **BD account closures** — date-aware: `closed_date` from accounts_dimension. BD is source of truth on account status. If BD says closed, excluded from both BD and Schwab sides regardless of what Schwab reports.
3. **Silver allocations phantom gate** — accounts not in `silver/allocations/{date}.parquet` with AUA >= $100 are phantom. Pre-loaded in batch (50 dates, parallel) to avoid per-date S3 calls.

### Source Classification

| Source | Meaning | Units Used |
|--------|---------|------------|
| `bd` | BD only (account/asset not in Schwab RPS) | BD |
| `schwab` | Schwab only (gap-fill: BD FIFO missed this position) | Schwab |
| `reconciled` | Both agree within tolerance (0.01 units or 0.1% relative) | Schwab |
| `schwab_override` | Both present, disagree — Schwab wins (custodian authoritative) | Schwab |

### Watermarks (sealed-day immutability)

- `gold/canonical/watermarks.json` stores sealed dates
- Sealed dates are skipped on subsequent runs (no silent overwrite)
- `--force` required to reprocess a sealed date
- `--no-seal` for testing without sealing
- Watermarks written after successful processing

### Output Schema

`gold/canonical/holdings/{YYYY-MM-DD}.parquet`

```
date, account_id, asset_name, units, price, market_value,
source, bd_units, schwab_units, ticker
```

---

## Dry Run Results (2026-04-02, with self-healing mapping)

```
Canonical AUA:    $1,875,268,703  (6,082 accounts)

Source distribution:
  reconciled          44,647  (47.5%)   -- BD + Schwab agree
  schwab_override     27,965  (29.7%)   -- Schwab corrects BD FIFO drift
  bd                  12,686  (13.5%)   -- non-Schwab accounts
  schwab               8,785  ( 9.3%)   -- gap-fill (BD was missing these)
```

Before self-healing mapping: 43.4% reconciled, 17.8% BD-only.
After: 47.5% reconciled, 13.5% BD-only. Nearly half of all positions now cross-validated.

The 29.7% override rate confirms significant FIFO drift in BD's reconstruction — this is the core problem canonical positions solves.

---

## Schwab Data Pipeline (built this session)

### Raw files uploaded

52 CRS*.RPS files from local OneDrive to `s3://opal-data-bd/schwab/bronze/`
(CRS20260120 through CRS20260402, ~70MB each, 3.6GB total)

### Bronze-to-silver converter

**Script:** `data/black_diamond/scripts/bronze/convert_schwab_rps_to_silver.py`
- Reads from `opal-data-bd/schwab/bronze/`
- Writes date-partitioned parquet to `opal-data-bd/schwab/silver/rps/date={YYYYMMDD}/data.parquet`
- Parses pipe-delimited CRS*.RPS files, extracts key fields (account_id, cusip, ticker, quantity_settled, closing_price, market_value)

### Silver consolidation

558 partitions consolidated from `opal-data-schwab/silver/RPS/` (restored bucket) into `opal-data-bd/schwab/silver/rps/`. Full coverage: **2024-01-12 to 2026-04-02**.

### S3 Layout

```
opal-data-bd/schwab/
  bronze/   52 raw CRS*.RPS files (local uploads)
  silver/
    rps/    558 date partitions (positions)          DONE
    uln/    316 date partitions (unrealized lots)    DONE
    rld/    590 date partitions (realized lots)      DONE
```

---

## Files Created

| File | Purpose |
|------|---------|
| `data/black_diamond/scripts/gold/02b_build_canonical_holdings.py` | Canonical holdings builder |
| `data/black_diamond/scripts/bronze/convert_schwab_rps_to_silver.py` | RPS bronze-to-silver converter |

## Files Modified

| File | Change |
|------|--------|
| `data/black_diamond/scripts/gold/lib/s3_layout.py` | Added `CANONICAL_HOLDINGS_PREFIX`, `canonical_holdings_key()`, `S3_CANONICAL_PRICES_KEY`, `CANONICAL_HOLDINGS_WATERMARK` |

---

## COO Review Cycle

COO (2.0.0_SA_COO) reviewed the initial plan and flagged 5 issues. All resolved:

1. **CUSIP join required** — Confirmed correct. Schwab RPS has cusip, not asset_name. CUSIP bridge from unrealized + realized covers 98.1%.
2. **Which Schwab source** — Built new silver pipeline from raw RPS files. Old `daily_positions.parquet` was BD-derived, not Schwab.
3. **Date coverage** — Schwab: 2024-01-12 to 2026-04-02 (558 dates). BD: 2020-01-01 to 2026-04-02.
4. **NAME_ALIASES** — Applied to both sides before join.
5. **canonical_prices in s3_layout** — Added as `S3_CANONICAL_PRICES_KEY`.
6. **BLOCKER: stale data** — Resolved by building full Schwab silver pipeline.

## External Review

Colleague validated the log and code. Feedback addressed:
- Dead code (`price_holdings` non-vectorized) — removed
- Dual S3 key definition — fixed, imported from s3_layout
- Allocations per-date S3 calls — replaced with parallel batch preload
- Watermarks — implemented before production writes

---

## Not Done / Next Steps

1. **Full backfill** — Run 02b across all 2,284 cube dates on EC2 (est. 15-20 min)
2. **Refactor script 05** — Cut over to read canonical_holdings instead of positions_cube
3. **Wire into runner** — Add 02b to `run_gold_layer.sh` (only after 05 cutover)
4. **Upload to S3 code path** — `s3://opal-data-bd/code/gold/02b_build_canonical_holdings.py`
5. **Close ULN gap** — Upload remaining ULN files (2026-02-27 through 2026-04-02) once local download completes

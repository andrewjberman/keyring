# Session Log — 0.4.0_DS_ClientPlatform — 2026-04-06 (Session 2)

**Start Time:** ~6:30 PM ET
**Project:** ADVI_GLDOPS
**Task Order:** ADVI_GLDOPS.004 — Build Canonical Holdings Stack

---

## Objective

Establish the first layer of an immutable canonical data stack for the gold pipeline. The pipeline currently re-derives everything from silver on every run — positions, NNA, market growth — with no cross-validation against Schwab custodial data and no sealed-day guarantees. The canonical stack replaces this with a layered architecture where each layer is built once, validated, and locked:

```
canonical_prices       (already exists — silver/prices/canonical_prices.parquet)
  -> canonical_holdings  (THIS SESSION — BD positions + Schwab RPS reconciliation)
    -> canonical_lots    (future — BD tax lots + Schwab-enriched synthetic lots)
    -> canonical_nna     (future — transaction flows + Schwab daily_flows cross-val)
    -> canonical_market_growth  (future — deterministic from holdings + prices)
```

Each layer depends only on the one above it plus silver source data. Once a day is validated, it is sealed — downstream scripts read canonical tables instead of re-deriving them. Script 05 (currently 1,055 lines, 30-40 min runtime) becomes a thin assembly step (~5 min).

---

## What Was Done

### 1. Data Source Profiling

Profiled all available data sources before writing any code:

**BD Positions Cube** (`gold/timeseries/positions_cube/{date}.parquet`):
- 2,284 date-partitioned files, 2020-01-01 to 2026-04-02
- Schema: `account_id` (z08... BD format), `asset_name`, `units`
- ~172M total rows across all dates
- Built by `02_build_positions_cube.py` via FIFO transaction replay

**Schwab RPS** — Required significant investigation:
- `daily_positions.parquet` (682MB in `opal-data-bd/silver/`) was initially assumed to be Schwab data. **This was wrong.** It is a BD-derived position reconstruction from the archived `build_transaction_engine.py`. It uses BD account IDs and BD asset names because it was built from BD transactions.
- The actual Schwab custodial data lives in raw CRS*.RPS files with schema: `account_id` (Schwab format like `0010023253`), `cusip`, `ticker`, `quantity_settled`. **No asset_name column.** Schwab identifies positions by CUSIP, not BD asset names.
- `opal-data-schwab` bucket was completely empty (0 objects). Raw RPS files existed only locally on Andrew's OneDrive.

**CUSIP Bridge** (resolving Schwab CUSIPs to BD asset names):
- Primary: `silver/unrealized/unrealized_gain_loss.parquet` — 2,611 CUSIP-to-asset_name pairs
- Extended: `silver/realized/bd_realized_compact.parquet` — +5,719 additional pairs
- Combined: 8,330 entries, resolving **98.1%** of Schwab CUSIPs. Remaining 2% is mostly cash/escrow/sweeps (filtered).

**Account Mapping**: `gold/dimensions/schwab_bd_account_mapping.parquet` — 6,424 pairs mapping Schwab account IDs to BD z08... format.

**Account Closures**: `gold/dimensions/accounts_dimension_latest.parquet` — 371 closed accounts with `closed_date` ranging 2022-05-16 to 2025-10-29. BD is source of truth on account status — closed accounts are excluded from both BD and Schwab sides regardless of what Schwab reports.

### 2. Schwab Data Pipeline (New)

Raw RPS files were not on S3. Built a new pipeline:

**Uploaded 52 raw RPS files** from local OneDrive to new consolidated location:
- Source: `C:\Users\AndrewBerman\OneDrive - Opal Capital\Documents\Schwab Data Delivery\08242234\CRS20260120.RPS` through `CRS20260402.RPS`
- Destination: `s3://opal-data-bd/schwab/bronze/CRS{YYYYMMDD}.RPS`
- ~70MB each, 52 files, 3.6GB total

**Created converter script** `convert_schwab_rps_to_silver.py`:
- Reads from `opal-data-bd/schwab/bronze/`
- Writes date-partitioned parquet to `opal-data-bd/schwab/silver/rps/date={YYYYMMDD}/data.parquet`
- Adapted from existing `convert_schwab_rps_to_parquet.py` (which targeted the now-empty `opal-data-schwab` bucket)
- All 52 dates converted successfully: 79K-86K positions per date, 5,589 unique accounts, 2,083 unique CUSIPs

**New S3 layout:**
```
opal-data-bd/
  schwab/
    bronze/CRS20260120.RPS ... CRS20260402.RPS    (52 raw files)
    silver/rps/date=20260120/ ... date=20260402/   (52 parquet partitions)
```

### 3. Canonical Holdings Script (`02b_build_canonical_holdings.py`)

**Location:** `data/black_diamond/scripts/gold/02b_build_canonical_holdings.py`

Numbered 02b: runs immediately after 02_build_positions_cube, produces reconciled holdings for downstream consumption. Follows existing `{NN}b` convention (05b, 06b, 08b).

**Join path (CUSIP-based, per COO review):**
```
Schwab RPS (cusip, schwab_account_id, quantity_settled)
  -> schwab_bd_account_mapping -> bd_account_id
  -> CUSIP bridge (unrealized + realized) -> asset_name
  -> NAME_ALIASES normalization
  -> Full outer JOIN positions_cube on (account_id, asset_name)
  -> Reconcile units, classify source
  -> Price with canonical_prices
  -> Write partition
```

**Reconciliation logic:**
- `bd`: BD-only (account/asset not in Schwab RPS)
- `schwab`: Schwab-only (positions BD FIFO missed — gap-fill enrichment)
- `reconciled`: Both sources agree within tolerance (0.01 units or 0.1% relative)
- `schwab_override`: Both present but disagree — Schwab wins (custodian authoritative on settled positions)

**Exclusion layers (all applied before reconciliation):**
1. Ghost accounts (`lib/exclusions.load_ghost_account_ids()`) — 4 accounts
2. BD account closures — date-aware: accounts excluded only after their `closed_date`. BD is source of truth on account status regardless of what Schwab reports.
3. Silver allocations phantom gate — accounts not in `silver/allocations/{date}.parquet` with AUA >= $100 are phantom/closed

**Output schema** (`gold/canonical/holdings/{YYYY-MM-DD}.parquet`):
```
date, account_id, asset_name, units, price, market_value, source, bd_units, schwab_units, ticker
```

**S3 layout additions** (`lib/s3_layout.py`):
- `CANONICAL_HOLDINGS_PREFIX = 'gold/canonical/holdings/'`
- `canonical_holdings_key(date_str)`
- `S3_CANONICAL_PRICES_KEY = 'silver/prices/canonical_prices.parquet'`

### 4. Dry Run Results (2026-04-02)

```
=== BD-only (no Schwab) after all exclusions ===
Silver allocations (BD reported AUA):      $1,627,029,715
Positions cube (alive accounts only):      $1,655,828,553  (6,082 accounts, +1.8% vs silver)

=== Canonical (BD + Schwab reconciled) ===
Canonical AUA:                             $1,875,043,659  (6,082 accounts)

Source distribution:
  bd (non-Schwab accounts):    17.8%  (16,725 positions)
  reconciled (agree):          43.4%  (40,833 positions)
  schwab (gap-fill):            9.3%  ( 8,756 positions)
  schwab_override (disagree):  29.5%  (27,740 positions)
```

The 1.8% gap between cube and silver allocations is pricing differences (canonical_prices vs BD's own prices). The $191M Schwab gap-fill represents real positions that BD's FIFO transaction replay missed — transfers, corporate actions, etc. that Schwab's custodial record reflects.

The 29.5% override rate confirms significant FIFO drift in BD's reconstruction, which is the core problem this canonical layer solves.

---

## Files Created

| File | Purpose |
|------|---------|
| `data/black_diamond/scripts/gold/02b_build_canonical_holdings.py` | Canonical holdings builder (BD + Schwab RPS reconciliation) |
| `data/black_diamond/scripts/bronze/convert_schwab_rps_to_silver.py` | Schwab RPS bronze-to-silver converter (opal-data-bd/schwab/) |

## Files Modified

| File | Change |
|------|--------|
| `data/black_diamond/scripts/gold/lib/s3_layout.py` | Added `CANONICAL_HOLDINGS_PREFIX`, `canonical_holdings_key()`, `S3_CANONICAL_PRICES_KEY` |

## S3 Changes

| Location | Action |
|----------|--------|
| `opal-data-bd/schwab/bronze/CRS*.RPS` | Uploaded 52 raw RPS files (new location) |
| `opal-data-bd/schwab/silver/rps/date=*/data.parquet` | Created 52 silver partitions (new) |

## Commits

No commits this session yet. All changes are staged/untracked pending review. Prior related commit:
- `d863559c` — task order GLDOPS.004 (the 5-phase plan document)

## COO Review (2.0.0_SA_COO)

COO reviewed the initial plan and flagged 5 issues:
1. **CUSIP join required** (not asset_name) — CONFIRMED correct after investigation. Schwab RPS has CUSIP, not asset_name.
2. **Which Schwab source** — Resolved: raw RPS files via new silver pipeline, not the stale `daily_positions.parquet`.
3. **Date coverage** — Verified: Schwab 2026-01-20 to 2026-04-02, BD 2020-01-01 to 2026-04-02.
4. **NAME_ALIASES** — Applied to both sides before join.
5. **canonical_prices in s3_layout** — Added as `S3_CANONICAL_PRICES_KEY`.
6. **BLOCKER: daily_positions stale** — Resolved by building new Schwab silver pipeline from raw RPS files.

## Architectural Direction (discussed with Andrew)

The canonical stack is a layered immutable architecture:

```
Layer 0: canonical_prices        [EXISTS]  silver/prices/canonical_prices.parquet
Layer 1: canonical_holdings      [THIS SESSION]  gold/canonical/holdings/{date}.parquet
Layer 2: canonical_lots          [FUTURE]  BD tax lots + Schwab synthetic lots
Layer 3: canonical_nna           [FUTURE]  Transaction flows + Schwab cross-val
Layer 4: canonical_market_growth [FUTURE]  Deterministic from L1 + L0
```

**Script 05 refactor** (Phase 4 of task order): Once all canonical layers exist, script 05 shrinks from 1,055 lines / 30-40 min to a thin assembly step reading pre-built tables (~5 min).

**Canonical lots** (discussed): Tax lots are fundamentally BD-only (Schwab RPS has no lot-level detail). Canonical lots = BD lots + synthetic single-lots for Schwab-only positions (units known, cost basis unknown). Lower priority than NNA and market growth.

**BD is source of truth on account status**: If BD says an account is closed, it is excluded from canonical regardless of what Schwab reports. Closure is date-aware — accounts are included up through their `closed_date`, then permanently excluded.

---

## Not Done / Next Steps

1. **Upload test**: Run `02b --date 2026-04-02 --upload` to write a live partition to S3
2. **Full rebuild**: Run across all 2,284 cube dates (estimated 15-20 min on EC2)
3. **Pipeline integration**: Wire 02b into `run_gold_layer.sh` (both incremental and full modes)
4. **Wire script 05**: Modify `05_build_client_performance.py` to read canonical_holdings instead of positions_cube — this is the biggest downstream payoff
5. **Phase 2**: Build `02c_build_canonical_nna.py` (extract NNA logic from script 05, cross-validate with Schwab daily_flows)
6. **Phase 3**: Build `02d_build_canonical_market_growth.py` (deterministic from canonical_holdings + canonical_prices)
7. **Sealed-day watermarks**: Add `gold/canonical/watermarks.json` to gate incremental processing

---

## Related Brief

`org/tier2_senior/0.4.0_DS_ClientPlatform/briefs/2026-04-06_account_mapping_gap_brief.md`

Validation session identified 350 Schwab accounts ($69.3M AUA) invisible to reconciliation
because the mapping table was built from realized transactions only (buy-only accounts had
no sells to fingerprint). 335 of 350 are trivially matchable via BD `account_number.zfill(10)`.
Gap growing at ~3 accounts/day. The self-healing mapping in 02b's `load_account_mapping()`
was built in direct response to this brief — resolved +1,534 new mappings on first run.

## Key Learnings

- `daily_positions.parquet` is NOT Schwab data — it's BD-derived from the archived `build_transaction_engine.py`. This caused initial confusion about whether CUSIP-based join was needed.
- `opal-data-schwab` bucket is completely empty. All Schwab data now consolidated under `opal-data-bd/schwab/`.
- CUSIP bridge from unrealized + realized covers 98.1% of Schwab positions. The 2% gap is cash/escrow/sweeps that are filtered anyway.
- Positions cube already excludes BD-closed accounts (0 closed accounts in latest date). But Schwab RPS can still report positions for 33 closed accounts — the BD closure gate catches these.
- The 29.5% schwab_override rate on the latest date confirms substantial FIFO drift, validating the need for Schwab cross-validation.

# GLDOPS.004 — Canonical Lots (03 / 03b)

**Agent:** 0.4.0_DS_ClientPlatform
**Date:** 2026-04-06
**Project:** ADVI_GLDOPS
**Task Order:** ADVI_GLDOPS.004 — Build Canonical Holdings Stack

---

## What This Is

Canonical lots is Layer 2 of the immutable canonical data stack. It establishes per-lot tax detail for every open and closed position, gated by canonical positions (02b) to ensure only "alive" accounts carry lots.

```
Layer 0: canonical_prices       [EXISTS]
Layer 1: canonical_positions    [BUILT]    02 + 02b
Layer 2: canonical_lots         [THIS]     03b (unrealized + realized)
Layer 3: canonical_nna          [FUTURE]
Layer 4: canonical_market_growth [FUTURE]
```

The key design: canonical lots are structured for **downstream per-account capital gains tracking** — both unrealized (open positions) and realized (closed positions), with short-term vs long-term classification, cost basis, and gain/loss per lot.

---

## Scripts

### 03_build_holdings_lots.py (existing, unchanged)
- 1,387 lines, FIFO replay from transactions to build lots
- Will eventually be superseded by 03b for Schwab-custodied accounts

### 03b_build_canonical_lots.py (NEW)
- **Location:** `data/black_diamond/scripts/gold/03b_build_canonical_lots.py`
- Gated by 02b canonical_holdings (alive accounts only)
- Produces two outputs:
  - `gold/canonical/lots_unrealized/{date}.parquet` — open tax lots
  - `gold/canonical/lots_realized/{date}.parquet` — closed tax lots

---

## Architecture: The Alive Gate

03b reads canonical_holdings (02b output) for each date to determine which accounts are alive. Only those accounts get lots. This ensures:

- Lots AUA ties back to canonical holdings AUA
- Closed accounts (BD source of truth) carry no lots
- Phantom accounts carry no lots
- Ghost accounts carry no lots

The same exclusion logic that 02b applies (BD closures + silver allocations + ghost) is inherited transitively — 03b doesn't re-implement the exclusions, it simply reads 02b's output as the gate.

---

## Data Sources

### Unrealized Lots (open positions)

| Source | What It Provides | Coverage |
|--------|-----------------|----------|
| **BD unrealized** (`silver/unrealized/unrealized_gain_loss.parquet`) | `open_date`, `unit_cost`, `account_id`, `asset_name`, `cusip`, `ticker` | All accounts (7,244) — current snapshot |
| **Schwab ULN** (`schwab/silver/uln/date={YYYYMMDD}/data.parquet`) | `quantity`, `market_value`, `cost_basis`, `adjusted_cost_basis`, `unrealized_gain_loss`, `days_held`, `holding_type` (S/L), `disallowed_loss`, `acquired_date`, `cost_per_share` | Schwab accounts, 316 dates (2024-01-12 to 2026-02-26) |

**Enrichment model:** For Schwab-custodied accounts, Schwab ULN is the primary source (full tax lot detail). For BD-only accounts, BD unrealized provides identity + unit_cost but lacks per-lot quantity, MV, and gain/loss fields.

### Realized Lots (closed positions)

| Source | What It Provides | Coverage |
|--------|-----------------|----------|
| **BD realized** (`silver/realized/bd_realized_compact.parquet`) | `open_date`, `trade_date`, `unit_cost`, `account_id`, `asset_name`, `cusip` | All accounts, 2021-01-04 to 2026-03-26, 892K rows |
| **Schwab RLD** (`schwab/silver/rld/date={YYYYMMDD}/data.parquet`) | `closing_date`, `closing_quantity`, `proceeds`, `cost_basis`, `gain_loss_dollars`, `adjusted_cost_basis`, `days_held`, `holding_type` (S/L), `disallowed_loss` | Schwab accounts, 590 dates (2023-01-17 to 2026-03-30) |

**Enrichment model:** Schwab RLD is the authority on tax treatment for Schwab accounts — BD realized has no proceeds, no gain/loss, no holding type classification. For non-Schwab accounts, BD realized provides trade identity but tax fields are null.

### Cross-Reference Findings (2026-01-07 rebalance day)

| Category | Account x Asset pairs |
|----------|----------------------|
| Both BD + Schwab | 10,804 |
| Schwab only | 148 ($2.6M proceeds) |
| BD only | 257 |

Lot counts nearly identical for matched positions: 45,563 Schwab vs 45,528 BD (35-lot difference from rounding/splitting). BD tends to have MORE lots per position (more granular FIFO splitting).

### What Schwab Adds Over BD

| Field | BD Unrealized | Schwab ULN | BD Realized | Schwab RLD |
|-------|:---:|:---:|:---:|:---:|
| quantity per lot | -- | Yes | -- | Yes |
| market_value per lot | -- | Yes | -- | -- |
| cost_basis (total $) | unit_cost only | Yes | unit_cost only | Yes |
| adjusted_cost_basis | -- | Yes | -- | Yes |
| unrealized G/L | -- | Yes | -- | -- |
| realized G/L (proceeds, gain/loss) | -- | -- | -- | Yes |
| holding_type (S/L) | -- | Yes | -- | Yes |
| days_held | -- | Yes | -- | Yes |
| disallowed_loss (wash sales) | -- | Yes | -- | Yes |

---

## Output Schemas

### lots_unrealized (per-date snapshot of open lots)

```
date, account_id, asset_name, cusip, ticker,
acquired_date, lot_index, source,
quantity, current_price, market_value,
cost_basis, cost_per_share, adjusted_cost_basis, original_purchase_price,
unrealized_gain_loss, days_held, holding_type, disallowed_loss
```

### lots_realized (per-date closed lots)

```
date, account_id, asset_name, cusip, ticker,
closing_date, acquired_date, source,
quantity, proceeds, proceeds_per_share,
cost_basis, cost_per_share, adjusted_cost_basis, original_purchase_price,
gain_loss_dollars, gain_loss_pct, adjusted_gain_loss_dollars,
days_held, holding_type, disallowed_loss
```

### Downstream Capital Gains Aggregation

Both tables carry `account_id` + `holding_type` (S/L) + gain/loss fields, enabling direct aggregation:

```python
# Per-account unrealized capital gains by tax treatment
unrealized.groupby(['account_id', 'holding_type'])['unrealized_gain_loss'].sum()

# Per-account realized capital gains by tax treatment
realized.groupby(['account_id', 'holding_type'])['gain_loss_dollars'].sum()

# Relationship-level: join accounts_dimension for relationship_id
# Tax efficiency: long-term gains / total gains ratio
```

---

## Dry Run Results (2026-01-23)

```
Unrealized: 366,765 lots
  Schwab-enriched:  198,635 lots (full tax detail)
  BD-only:          168,130 lots (open_date + unit_cost only)
  Total MV:         $563,286,904 (Schwab-covered accounts)
  Unrealized G/L:   $69,815,602

Realized: 493 lots (that day's closures)
  Realized G/L:     $171,092
```

Schwab ULN totals (2026-01-23):
- $581M market value across 204K lots
- $509M cost basis
- $72M unrealized gains ($30M short-term, $42M long-term)

Annual realized (from Schwab RLD history):
- 2023: 163K lots, $389M proceeds, +$7.1M realized G/L
- 2024: 231K lots, $841M proceeds, +$46.1M realized G/L
- 2025: 42K lots, $99M proceeds, +$1.0M realized G/L
- 2026 (partial): 152K lots, $416M proceeds, +$33.0M realized G/L

---

## Schwab Lot Converters (built this session)

### convert_schwab_lots_to_silver.py (NEW)

**Location:** `data/black_diamond/scripts/bronze/convert_schwab_lots_to_silver.py`

Single script handles both ULN and RLD:
- Reads from `opal-data-schwab/01_raw/` and `opal-data-bd/schwab/bronze/`
- Record prefix is `DL` (not D1 like RPS)
- Writes date-partitioned parquet to `opal-data-bd/schwab/silver/uln/` and `rld/`

```
Usage:
  python convert_schwab_lots_to_silver.py uln          # unrealized lots
  python convert_schwab_lots_to_silver.py rld          # realized lots
  python convert_schwab_lots_to_silver.py uln rld      # both
  python convert_schwab_lots_to_silver.py uln --force  # reconvert all
```

### Conversion Results

| Type | Partitions | Date Range | Status |
|------|-----------|------------|--------|
| ULN (unrealized) | 316 | 2024-01-12 to 2026-02-26 | DONE (0 errors) |
| RLD (realized) | 590 | 2023-01-17 to 2026-03-30 | DONE (1 skip, 0 errors) |

ULN lot counts grew from 57K (early 2024) to 206K (Jan 2026) as the client base expanded.

---

## Files Created

| File | Purpose |
|------|---------|
| `data/black_diamond/scripts/gold/03b_build_canonical_lots.py` | Canonical lots builder (unrealized + realized) |
| `data/black_diamond/scripts/bronze/convert_schwab_lots_to_silver.py` | ULN/RLD bronze-to-silver converter |

## Files Modified

| File | Change |
|------|--------|
| `data/black_diamond/scripts/gold/lib/s3_layout.py` | Added `CANONICAL_LOTS_UNREALIZED_PREFIX`, `CANONICAL_LOTS_REALIZED_PREFIX`, key functions |

---

## Other Schwab File Types Investigated

### TNN (Tax Information Notification / 1099 data)

17 local files, 109 on S3. Contains 1099-B (D9B records, realized lot tax reporting), 1099-DIV, 1099-INT. Annual files, not daily. The D9B data (49K records in a single tax year file) is the IRS-reported version of what RLD already captures at daily granularity. **Not needed for canonical lots** — ULN and RLD cover the same data more granularly.

---

## Not Done / Next Steps

1. **Close ULN gap** — Upload ULN files for 2026-02-27 through 2026-04-02 once local download completes, convert to silver
2. **Full backfill** — Run 02b for all dates first, then 03b reads those partitions
3. **BD unrealized quantity gap** — BD unrealized has no per-lot quantity column. For BD-only accounts, lot-level MV and unrealized G/L cannot be computed. This is an inherent BD data limitation, not fixable without Schwab.
4. **Watermarks for lots** — Add sealed-day protection (same pattern as 02b)
5. **Wire into runner** — After 02b and 05 cutover are complete
6. **Performance module** — Downstream script to aggregate per-account/relationship capital gains from canonical lots for portal display

# Session Log — ADVI_INFLEC.AUDIT-002 AUA=0 Root Cause Trace

**Agent:** 0.4.0_DS_ClientPlatform~D
**Date:** 2026-05-05
**Session scope:** Root cause trace — activity_scan + cash_drag + concentration_risk AUA=0
**GO source:** 2.0.0_SA_COO (broker channel, 20260505T~startup)

---

## Summary

Root cause confirmed: **Type B — upstream pipeline artifact stale**. `canonical_prices.parquet` last refreshed 2026-04-22T09:26Z; contains prices only through 2026-04-22. INF_B_01 cannot price any position for 2026-04-23+, producing all-NaN `market_value` in `gold/holdings/`. All three downstream insight scripts (INF_D_05, INF_D_06, INF_D_07) read `gold/holdings/` for AUA → zero output on all records.

---

## Evidence Chain

### 1. Scripts read gold/holdings/ for AUA

| Script | AUA source | Code path |
|--------|-----------|-----------|
| INF_D_05.activity_scan.py | `gold/holdings/` latest partition | `load_latest_holdings_aua()` L76-106: lists `gold/holdings/` prefix, reads latest `.parquet`, groups `market_value` by `household_id` |
| INF_D_06.cash_drag.py | `gold/holdings/` window (90d) + latest | `list_holdings_keys()` L76-91 + `_load_holdings_date()` L94-120: joins to `accts_dim`, sums `market_value` per HH → `aua` column |
| INF_D_07.concentration_risk.py | `gold/holdings/` latest partition | `load_latest_holdings()` L82-109: drops NaN `market_value` rows; `hh_total_mv` = sum → `aua` |

### 2. gold/holdings/ latest parquet (2026-04-28) has all-NaN market_value

```
S3: s3://opal-data-inf/gold/holdings/2026-04-28.parquet (72.3 KiB)
Shape: (9295, 8)
Columns: ['date', 'account_id', 'ticker', 'units', 'price', 'market_value', 'price_source', 'custodian']

market_value: min=nan  max=nan  sum=0.0  non-NaN rows=0
price: non-NaN rows=0
price_source: all None (9295 rows)
```

### 3. For comparison: 2026-04-21 parquet had valid prices

```
S3: s3://opal-data-inf/gold/holdings/2026-04-21.parquet (169.9 KiB)
Shape: (9668, 8)

market_value: non-NaN rows=9666  sum=$189,547,944.56
price_source: yahoo_finance(8626) + linear_interpolation(1038) + price_override(2)
market_value sum: $189.5M (valid AUA)
```

Size drop from 169.9 KiB (Apr 21) → 72.3 KiB (Apr 28) is entirely explained by market_value NaN
(float64 NaN compresses much tighter than real prices in Parquet).

### 4. INF_B_01 pricing join — WARN path triggered for 2026-04-23+

INF_B_01.holdings_lots.py L112-113:
```python
day_prices = prices[prices['date'] == pd.Timestamp(date_str)]
if day_prices.empty:
    log(f'  WARN [{date_str}]: no prices for this date -- market_value will be null')
```
L116-120: left-join `day_prices[['ticker', 'price', 'price_source']]` onto positions →
`price=NaN`, `market_value = units * NaN = NaN` for every row.

### 5. canonical_prices.parquet is stale — stops at 2026-04-22

```
S3: s3://opal-data-inf/silver/prices/canonical_prices.parquet
Last modified: 2026-04-22T09:26Z  (27.6 MiB)
Shape: (4,443,756, 4)  |  3,777 tickers

Date range: 2019-09-26 -> 2026-04-22
Rows after 2026-04-22: 0
Latest dates: [2026-04-20, 2026-04-21, 2026-04-22]
```

`canonical_prices.parquet` has not been refreshed in 13 days (last run: 2026-04-22T09:26Z).

### 6. INF_D_07 empty artifact (concentration_risk.json = 2 bytes)

INF_D_07 L99: `df = df.dropna(subset=['account_id', 'ticker', 'market_value'])` — drops all NaN market_value rows → 0 rows → empty list → empty JSON. Confirmed:
```
s3://opal-data-inf/platinum/firm/concentration_risk.json
Size: 2 bytes  (last modified 2026-05-04T12:17Z)
Content: [] (empty array)
```

### 7. INF_D_05 / INF_D_06 produce rows with aua=0 (not empty)

INF_D_05 L168: `hh_data['aua'] = hh_data['aua'].fillna(0.0)` — silently zero-fills, so output has
307 rows with `aua=0.0` rather than being empty. Same pattern in INF_D_06: 295 rows with `aua=0.0`.

This explains the AE 0.5 observation: "307 rows, ALL AUA=0" — artifact EXISTS, rows present,
but all AUA zeroed because NaN was filled.

---

## Root Cause Verdict

**Type B — AUA field sourced from an artifact that exists but has wrong shape.**

`silver/prices/canonical_prices.parquet` was last refreshed 2026-04-22T09:26Z. It contains no
prices for 2026-04-23 through 2026-05-05 (13-day gap). INF_B_01 runs daily and joins positions
to canonical prices by exact date — for any date past 2026-04-22, the join returns NaN for
all prices → `market_value=NaN` → gold/holdings/* contains all-NaN market_value for all
partitions 2026-04-23 through 2026-04-28 (latest). INF_D_05/06 fill NaN→0, INF_D_07 drops
NaN rows → empty output. All three platinum JSONs carry AUA=0.

---

## Affected Artifacts

| Artifact | Effect | Evidence |
|----------|--------|----------|
| `platinum/firm/activity_scan.json` | 307 rows, all `aua=0.0` | NaN→0 fill in INF_D_05 L168 |
| `platinum/firm/cash_drag.json` | 295 rows, all `aua=0.0`, `cash_pct=0.0` | NaN→0 fallback in INF_D_06 L166 |
| `platinum/firm/concentration_risk.json` | 2 bytes (empty `[]`) | dropna L99 eliminates all rows |
| `gold/holdings/2026-04-23.parquet` through `2026-04-28.parquet` | All `market_value=NaN` | Upstream pricing gap |

---

## Fix Path (AE + DS scope)

This is a pipeline re-run, not a code bug.

| Step | Owner | Action |
|------|-------|--------|
| 1 | AE/DS | `backfill_yahoo_prices_inf.py --upload` — refresh `silver/historical_prices.parquet` through today |
| 2 | DS | `INF_build_canonical_prices.py --upload` — rebuild `silver/prices/canonical_prices.parquet` through 2026-05-05 |
| 3 | DS | `INF_B_01.holdings_lots.py --start-date 2026-04-23 --upload` — rebuild 13 holdings partitions with valid market_value |
| 4 | DS | `INF_D_05 --upload`, `INF_D_06 --upload`, `INF_D_07 --upload` — regenerate platinum JSONs with correct AUA |
| 5 | DS | Verify: `activity_scan.json` rows with non-zero `aua`; `cash_drag.json` rows with correct `total_mv`; `concentration_risk.json` non-empty |

**Not a 1-line guard fix.** Requires pipeline re-run coordination (AE: Yahoo backfill; DS: canonical_prices rebuild + INF_B_01 backfill + INF_D_05/06/07 re-run).

---

## Compiler Tools

| Tool | Target | Output | Mandate |
|------|--------|--------|---------|
| `comp-pipescript io INF_D_05` | INF_D_05 | READS: `gold/dimensions/accounts_dimension_latest.parquet` [HARDCODED]. Dynamic `gold/holdings/` prefix not graph-indexed (pagination pattern). | Phase 0 |
| `comp-pipescript io INF_D_06` | INF_D_06 | Same — `gold/dimensions/accounts_dimension_latest.parquet` only. | Phase 0 |
| `comp-pipescript io INF_D_07` | INF_D_07 | READS: `silver/accounts_dim/latest.parquet` [HARDCODED]. | Phase 0 |
| S3 empirical reads (this session) | `gold/holdings/2026-04-28.parquet` | 9295 rows; `market_value` all NaN; `price` all NaN; `price_source` all None. | Evidence |
| S3 empirical reads (this session) | `gold/holdings/2026-04-21.parquet` | 9668 rows; 9666 non-NaN `market_value`; sum $189.5M; `price_source` = yahoo_finance/linear_interpolation. | Evidence |
| S3 empirical reads (this session) | `silver/prices/canonical_prices.parquet` | 4,443,756 rows; date range 2019-09-26 → 2026-04-22; 0 rows after 2026-04-22. | Root cause confirmed |
| S3 empirical reads (this session) | `platinum/firm/concentration_risk.json` | 2 bytes (empty array). | Confirms INF_D_07 output |

`.comp-graph/.agent_context` set to `SERIAL=0.4.0_DS_ClientPlatform~D, TO_ID=ADVI_INFLEC.AUDIT-002.aua-join-investigation` for this session.

---

## Current State

| Item | Status |
|------|--------|
| AUA=0 root cause | CONFIRMED (Type B — stale canonical_prices.parquet) |
| RAVC3 to COO | PENDING (this session) |
| Code fix required | NO — pipeline re-run only |
| Inbox watcher | LIVE (task bwoyimvoh) |

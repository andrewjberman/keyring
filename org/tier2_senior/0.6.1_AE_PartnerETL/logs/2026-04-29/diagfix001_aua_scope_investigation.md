# Session Log — 0.6.1_AE_PartnerETL — ADVI_INFLEC.DIAGFIX.001 — 2026-04-29

**Agent:** 0.6.1_AE_PartnerETL (base lane)
**Date:** 2026-04-29
**Session scope:** ADVI_INFLEC.DIAGFIX.001 — AUA scope investigation ($89.6M holdings vs $182.6M aum_snapshot)
**GO received:** 20260429T204040Z (COO, commit cb611766c)

---

## Background

Every Inflection gold script that aggregates advisor/firm AUA lands at $89.6M:
- `partner_analytics_quarterly.views.aua.donut.total` = $89,590,439
- `leaderboard.windows.QTD` sum = $89,590,439
- `book.json` total = $89,590,439

But `header_metrics.json.total_aua` = $182,552,380.96 (from aum_snapshot managed_value.sum()).
Gap = ~$93M. DE brief (ADVI_INFLEC_DIAGNOSTIC_BRIEF_20260429.md §C1) flagged this as the highest-priority issue.

---

## Compiler Tools

| Tool | Command | Result |
|---|---|---|
| `comp-pipescript io` | `comp-pipescript io INF_B_00` | ERROR: INF_B_00 not in comp catalog (catalog has BD pipeline IDs). Ran with `B_00` → returned BD-catalog result, not applicable. **Gap: INF pipeline scripts not registered in comp catalog.** Documented; investigation continued via direct file read. |
| `comp-pipescript io B_00` | Ran | Returned BD pipeline B_00 (bd-gold). Not applicable to INF pipeline. |
| `comp-pipescript deployed` | N/A | Investigation-only TO; no dispatch in scope. |

---

## Files Analyzed

| File | Source | Notes |
|---|---|---|
| `data/orion/scripts/gold/INF_B_00.canonical_holdings.py` | Local | Step 5 filter audit |
| `gold/canonical/holdings_2026-04-28.parquet` | S3 download | Latest holdings snapshot |
| `silver/aum_snapshot/2026-04-29.parquet` | S3 download | Fresh DS-generated snapshot |
| `silver/accounts_dim/latest.parquet` | S3 download | account_id → household_id mapping |

---

## Step 1 — Holdings market_value.sum()

**Source:** `gold/canonical/holdings_2026-04-28.parquet` (latest snapshot, written by INF_B_00 chain)

| Metric | Value |
|---|---|
| Total rows | 9,295 |
| unique account_ids | 782 |
| advisor_keys | inflection_wealth_management, patrick_scanlan, peter_lee |
| **market_value.sum()** | **$89,590,439.60** |

Confirmed baseline: ~$89.6M. Matches all gold script outputs.

---

## Step 2 — AUM snapshot managed_value.sum()

**Source:** `silver/aum_snapshot/2026-04-29.parquet`

| Metric | Value |
|---|---|
| unique household_ids | 274 |
| **managed_value.sum()** | **$182,552,380.96** |
| By advisor | peter_lee: 198 HH, $161,925,085.68 |
| | patrick_scanlan: 73 HH, $20,372,728.19 |
| | inflection_wealth_management: 3 HH, $254,567.09 |

**Gap = $92,961,941.36 (~$93M)**

---

## Step 3 — Cross-join by household_id

Used `silver/accounts_dim/latest.parquet` (835 accounts, 307 households) to map account_id → household_id.

| Metric | Value |
|---|---|
| Accounts in accounts_dim (Inflection rep_ids 3/11/12) | 835 |
| Accounts WITH positions in holdings | 781 |
| Accounts WITHOUT any positions | 54 |
| Households represented in holdings | 295 |
| Households in AUM snapshot | 274 |
| **AUM HH absent from holdings** | **0** |

**Critical finding: ALL 274 AUM snapshot households have account records in the holdings data. There are NO missing households.** The gap is not caused by missing accounts — it is within the same households.

### Per-household gap distribution:

| Capture rate (holdings/managed) | HH count |
|---|---|
| < 10% | 2 |
| 10-25% | 6 |
| 25-50% | 125 |
| 50-75% | 81 |
| 75-90% | 23 |
| 90-100% | 31 |
| > 100% (overcount) | 5 |

258 of 274 households show partial gap (holdings < managed). Average capture rate: ~46%.

---

## Step 4 — Root Cause Classification

### Finding: NOT Options A, B, or C in the TO formulation

| Option | Result |
|---|---|
| A: Accounts absent from bronze/silver | NOT root cause — all 274 AUM HH have account records |
| B: account_status/type filter in INF_B_00 | NOT root cause — no such filter exists (see Step 5) |
| C: rep_id mismatch | NOT root cause — all 274 HH have correct rep_ids {3,11,12} |

### Root Cause: Option D — **nav_price=0.0 for 40.2% of holdings rows**

| Metric | Value |
|---|---|
| Total holdings rows | 9,295 |
| Rows with market_value > 0 (valid price) | 5,557 (59.8%) |
| **Rows with nav_price=0.0 → market_value=0** | **3,738 (40.2%)** |
| Unique accounts with ≥1 zero-price position | 666 / 782 (85.2%) |
| Accounts where ALL positions are zero-priced | 5 |
| Accounts where SOME positions are zero-priced | 661 |

**Zero-priced positions are NOT limited to cash/money market tickers.** They span common ETFs and equity funds:

| Ticker | Zero-price rows | Accounts |
|---|---|---|
| HTRB (PIMCO) | 501 | 501 |
| VO (Vanguard Mid-Cap) | 321 | 321 |
| VB (Vanguard Small-Cap) | 318 | 318 |
| USRT | 312 | 312 |
| VOO (Vanguard S&P 500) | 297 | 297 |
| SCHP | 290 | 290 |
| RLY | 235 | 235 |
| FXAIX (Fidelity S&P 500) | 148 | 148 |

### Why nav_price=0.0?

INF_B_00 uses "last seen wins" for nav_price from the TRN (transaction) feed:

```python
# From INF_B_00.canonical_holdings.py:
if nav is not None:
    pos_meta[key]['nav_price'] = nav  # LAST transaction's price wins
```

Many Orion TRN rows are **non-trade events** (advisory fee payments, journal entries, income distributions) that carry `nav_price=0`. If the most recent transaction for (account_id, ticker) is a non-trade event with price=0, then all subsequent holdings snapshots for that position will have `market_value = units × 0.0 = $0.00` — even though the account holds real positions worth real money.

**The TRN feed's last-transaction price is unreliable as a market price source.** Non-trade events corrupt the price for entire (account, ticker) pairs going forward.

---

## Step 5 — INF_B_00 Filter Audit

Read `data/orion/scripts/gold/INF_B_00.canonical_holdings.py`.

Filters present:
1. `ticker.notna() & ticker.strip() != ''` — excludes null/empty ticker rows (cash line items)
2. `units <= 1e-9` — excludes zero/closed positions

**No `account_status`, `account_type`, `is_active`, or AUM filter of any kind.**

Note: `accounts_dim.is_active = False` for **all 835 accounts** in the Inflection accounts_dim — this field is not populated by the TRN-based accounts_dim builder and is not used by INF_B_00.

---

## Summary

| Criterion | Result |
|---|---|
| Step 1: holdings market_value.sum() | $89,590,439.60 (confirmed ~$89.6M) |
| Step 2: managed_value.sum() | $182,552,380.96 (confirmed ~$182.6M) |
| Step 3: cross-join gap HH count | 0 missing HH — gap is within-household |
| Step 4: root cause | Option D: nav_price=0 on 3,738 rows (40.2% of holdings) |
| Step 5: INF_B_00 filter audit | No account_status/type filter; "last seen wins" price bug |

**Fix recommendation for DIAGFIX.002a (partner_analytics scope fix):**

Two-path fix:

**Immediate (low risk):** Use `aum_snapshot.managed_value` per advisor as the AUA denominator in partner_analytics, leaderboard, and book.json gold scripts. This is the D_04 pattern already validated today ($182.6M exact match). Avoids holdings-reconstruction dependency entirely for AUA figures.

**Deeper (holdings pricing fix):** In INF_B_00, change "last seen wins" to only update nav_price when nav > 0:
```python
if nav is not None and nav > 0:
    pos_meta[key]['nav_price'] = nav
```
This would restore correct market values for 3,738 currently-zeroed positions. Requires re-running INF_B_00 chain after fix.

**Long-term:** Use Orion's positions API endpoint (`data/orion/manual_api/pull_inflection_positions.py` exists) for point-in-time market values, not TRN reconstruction. Eliminates the pricing fragility entirely.

---

## Compiler Tools Section

| Tool | Why ran / skipped |
|---|---|
| `comp-pipescript io INF_B_00` | Ran — error: script not in comp catalog. Gap flagged. INF pipeline catalog registration needed. |
| `comp-pipescript io B_00` | Ran — returned BD catalog result (not applicable). |
| `comp-pipescript deployed` | N/A — investigation TO; no dispatch |
| `comp-blast` | N/A — no script changes |
| `comp-validate` | N/A — no gold run |

---

## Files changed

### Created
- `org/tier2_senior/0.6.1_AE_PartnerETL/logs/2026-04-29/diagfix001_aua_scope_investigation.md` (this file)

### No S3 writes, no code changes
Investigation-only TO. No commits.

---

## RAVC Status

RAVC sent to 2.0.0_SA_COO with all findings. Gates DIAGFIX.002a routing.

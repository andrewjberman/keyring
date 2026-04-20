# Brief — Schwab ULN Silver Ingestion (Second Position Authority)
**Author:** 0.4.0_DS_ClientPlatform
**Date:** 2026-04-17
**Priority:** P1
**Assignee:** 0.6.0_AE_PartnerETL
**Driver:** Phantom position investigation — BD silver/unrealized is a single point of failure for open-position authority

---

## Problem Statement

B_01 currently uses two position authority feeds:

1. `silver/RPS/` — Schwab's daily realized-position/portfolio snapshot, used for synthetic lot injection
2. `opal-data-bd / silver/unrealized/` — BD's custodial open-position view, used as a Rule 3 veto on force-closes

When BD's silver/unrealized has a gap for an account (data latency, ingestion failure, or the account opened after the last successful export), B_01 has no fallback to confirm whether a FIFO-reconstructed position is real or phantom. The result is either a false-zero (Rule 3 closes real lots) or an unchecked overshoot (phantom lots survive with no external confirmation).

Schwab delivers a daily **ULN (Unrealized Gain/Loss) file** — a lot-level open-position snapshot from the Schwab custodian — that is architecturally identical to what BD's silver/unrealized provides but sourced independently from Schwab's side. Parsing ULN to silver gives B_01 a second position authority to cross-reference and significantly reduces phantom exposure.

---

## Source Data

**Bucket:** `opal-data-schwab`
**Raw path:** `01_raw/CRS{YYYYMMDD}.ULN`
**Anonymized path:** `02_anonymized/CRS{YYYYMMDD}.ULN`
**Mapping path:** `03_mappings/CRS{YYYYMMDD}.ULN.mapping.json`

**Coverage:** 2024-01-12 through 2026-04-15 (current), 566 files, no operational gaps — missing dates are market holidays only.

**Format:** Pipe-delimited flat file. Relevant record types:
- `H1` — file header (master account, firm name, date)
- `H2/H3` — column headers (two-row spanning header)
- `DL` — data line, one row per open lot

**Key DL fields (by position):**

| Field | Column | Example |
|-------|--------|---------|
| master_account | 2 | `0008242234` |
| account_name | 3 | `49 WEALTH MANAGEMENT LLC` |
| file_date | 4 | `20251111` |
| account_id | 5 | `ANON_57f82a041229` (anonymized item_id) |
| product_code | 6 | `COM`, `FGO`, `FII`, `MFD` |
| product_category | 7 | `EQTY`, `FIXD`, `CASH` |
| tax_code | 8 | `A` (taxable), `Z` (tax-exempt), etc. |
| ticker | 9 | `CRWD` |
| cusip | 10 | `22788C105` |
| schwab_sec_nbr | 11 | `1868258` |
| current_quantity | 23 | `+0000000200.000000` |
| long_short | 24 | `L` / `S` |
| current_market_value | 26 | `+0000000111346.0000` |
| accrued_interest | 27 | `+0000000000000.00` |
| acquired_date | 28 | `20251003` |
| original_purchase_date | 29 | `20251003` |
| original_purchase_price | 30 | `+00000000490.99500000` |
| cost_basis | 32 | `+0000000098199.00` |
| cost_per_share | 33 | `+00000000490.99500000` |
| unrealized_gain_loss | 37 | `+0000000013147.0000` |
| days_held | 38 | `00040` |

---

## Required Output

**Target path:** `opal-data-schwab / silver/ULN/date={YYYYMMDD}/data.parquet`

**Schema:**

```
account_id          string    -- anonymized item_id (maps to bd_account_id via RPS mapping)
cusip               string    -- CUSIP, strip leading/trailing whitespace
ticker              string    -- Schwab ticker symbol
asset_name          string    -- derive from ticker/cusip lookup or leave null (B_01 joins on cusip)
product_code        string    -- COM / FGO / FII / MFD / etc.
product_category    string    -- EQTY / FIXD / CASH / etc.
current_quantity    float64   -- strip sign prefix, parse as float
long_short          string    -- L / S
current_market_value float64
cost_basis          float64
cost_per_share      float64
unrealized_gain_loss float64
acquired_date       date      -- parse YYYYMMDD
original_purchase_date date
file_date           date      -- partition date, YYYYMMDD from filename
```

**Partition pattern:** same as RPS — `silver/ULN/date={YYYYMMDD}/data.parquet`. One partition per source file.

**Numeric parsing:** Schwab encodes numbers as `+0000000200.000000` and `-0000000014728.7000`. Strip the leading sign char, parse as float, then apply sign from the first character.

**Anonymization:** The `02_anonymized/` files have account numbers replaced with `ANON_{hash}`. The mapping JSON at `03_mappings/CRS{date}.ULN.mapping.json` maps hash → original `item_id`. Use the mapping to resolve back to the canonical `account_id` used elsewhere in the pipeline (same `item_id` space as RPS).

---

## Ingestion Pipeline

Mirror the existing RPS ingestion pattern:

1. For each new `01_raw/CRS{date}.ULN` arriving in S3:
   - Anonymize → `02_anonymized/`
   - Generate mapping JSON → `03_mappings/`
   - Parse `DL` rows → filter `long_short == 'L'` (long positions only)
   - Cast numerics, parse dates
   - Write `silver/ULN/date={YYYYMMDD}/data.parquet` to `opal-data-schwab`
2. Backfill all 566 existing files (2024-01-12 through present)

Note: `03_mappings/` mappings currently exist only through 2025-11-11. For dates after that, mappings need to be generated before anonymized account IDs can be resolved.

---

## How B_01 Will Use This

Once `silver/ULN/` is available, B_01 gains a third position confirmation source:

```
Position confirmation hierarchy (per account_id, cusip):
  1. silver/unrealized (BD custodial view)     -- authoritative if present
  2. silver/ULN (Schwab custodial view)        -- confirms if BD has gap
  3. silver/RPS (Schwab position snapshot)     -- used for synthetic injection already
  4. FIFO stack only                           -- lowest confidence, cap applies
```

Specifically in `_apply_silver_noncash_cap`:
- A lot currently classified as Band B (T3, cusip NOT in silver/unrealized) gets upgraded to Band A if the same `(account_id, cusip)` appears in `silver/ULN` with `current_quantity > 0`. This prevents the surgical cap from compressing a real Schwab-custodied position just because BD's export had a gap.

The relationship-consistency diagnostic we ran on 2026-04-17 found **15,085 candidate phantom-zero records across 1,844 accounts and 832 relationships** — all open, none with close signals. ULN would resolve the ambiguity for any Schwab-custodied account in that set.

---

## Acceptance Criteria

1. `silver/ULN/date={YYYYMMDD}/data.parquet` exists for all 566 historical dates (backfill complete).
2. Nightly ingestion writes a new partition within the normal BD pipeline window.
3. Schema matches spec above; `current_quantity` and `cost_per_share` parse correctly for both positive and negative values.
4. A sample join of `silver/ULN/date=20260415/` against run11 `gold/holdings_lots/2026-04-15.parquet` on `(account_id, cusip)` resolves at least 80% of the 1,844 false-zero candidate accounts.

---

## Out of Scope

- B_01 wiring of ULN as position authority (DS lane — separate TO after AE confirms backfill is live)
- UPN (Unrealized Positions) and UPT (Unrealized Positions Tax) files — may contain complementary data but ULN is sufficient for position confirmation

---

## Related

- Diagnostic: `data/black_diamond/scripts/diagnostics/relationship_consistency_candidates.csv` — 15,085 false-zero candidates
- `data/black_diamond/scripts/gold/B_01.holdings_lots.py` — `_apply_silver_noncash_cap`, `_resolve_unrealized_key`
- `org/tier2_senior/0.4.0_DS_ClientPlatform/` — CP-DS1 Gate 2 session context

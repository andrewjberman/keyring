# GLDOPS.004 — Canonical Stack Layers 2.5-4 + Downstream Rebuild

**Agent:** 0.4.0_DS_ClientPlatform
**Date:** 2026-04-06 (session 2)
**Project:** ADVI_GLDOPS
**Task Order:** ADVI_GLDOPS.004
**Commits:** `0dba3fa0`, `e55ff225`

---

## Overview

Continued from session 1 (02b canonical holdings, 03b canonical lots). This session built the remaining canonical stack layers plus the downstream scripts that consume them: account-level decomposition (03c), relationship-level performance (04a), NNA validation (04b), advisor fee efficiency (08c), employee leaderboard (11a enhancement), advisor assignment rebuild (01), fee rate history (01b), and the script 05 thin rewrite.

---

## Scripts Built

### 03c — Per-Account Daily Capital Gains Ledger
`data/black_diamond/scripts/gold/03c_build_account_gains.py`

Core identity enforced on every row:
```
AUA(t) - AUA(t-1) = Growth(t) + NNA(t)
Growth = price_return + realized_gl + income
NNA = aua_change - growth (residual)
```

- **price_return**: `units(t-1) * (price(t) - price(t-1))` for positions held both days
- **realized_gl**: from 03b lots_realized (ST/LT split)
- **income**: Dividend + Interest from BD transactions (not reinvestments — those are unit-changing)
- **unrealized_gl**: snapshot from 03b (informational, NOT in growth calc)
- **5-bit components bitmask** (uint8): bit 0=holdings_prior, bit 1=holdings_current, bit 2=realized_lots, bit 3=unrealized_lots, bit 4=transactions. `components == 31` = fully decomposed. `components & 0b10101 == 0b10101` = NNA is clean.
- Weekend/holiday gaps handled naturally: date pairs from partition list, not calendar math
- First-date handling: aua_prior=0, NNA = initial funding, bit 0 unset

Output: `gold/canonical/account_gains/{YYYY-MM-DD}.parquet`

### 04a — Canonical Performance (Relationship-Level)
`data/black_diamond/scripts/gold/04a_build_canonical_performance.py`

Aggregates 03c to relationship level with cumulative running sums.

- Joins 03c with accounts_dimension for relationship_id
- Cumulative columns: cum_price_return, cum_realized_gl, cum_income, cum_growth, cum_nna
- Incremental mode bootstraps cumulatives from last written performance partition
- Components bitmask propagated via min() (weakest signal wins per relationship)
- Documented: cumulatives reflect current-day composition, not historical membership. Relationship reassignments cause discontinuities.

Output: `gold/canonical/performance/{YYYY-MM-DD}.parquet`

### 04b — Canonical NNA + Legacy Validation
`data/black_diamond/scripts/gold/04b_validate_nna.py`

Two outputs:
1. **NNA parquet**: per-account with dimension columns + `nna_clean` boolean flag
2. **Validation JSON**: per-date comparison of 03c residual NNA vs legacy 05 transaction-classified NNA

- Left join from 03c onto legacy (null deltas for missing legacy dates, not dropped)
- Derives daily legacy NNA from cumulative via diff()
- Reports R-squared, material divergence count (|delta| > $10K), top 10 divergent relationships

Output: `gold/canonical/nna/{YYYY-MM-DD}.parquet` + `gold/canonical/nna_validation/{YYYY-MM-DD}.json`

### 01 — Advisor Assignments History (Rebuilt)
`data/black_diamond/scripts/gold/01_build_advisor_assignments_history.py`

Expanded from 3 fields to 13:
- **6 roles**: architect, implementor, consultant, local_ops, additional_advisor + all names
- **6 split_pct**: one for each role + house_split_pct
- SCD change detection on full 12-field tuple (split change without name change = new record)
- `keep='last'` on trade_date dedup (mid-day reassignment captures end-of-day state)
- Fee logic removed — owned by 01b
- Parallel transaction loading (64 workers)
- Baseline supplement logged explicitly: "role names only, splits will be 0"

Output: `gold/dimensions/advisor_assignments_history.parquet` (same path, richer schema)

### 01b — Fee Rate History
`data/black_diamond/scripts/gold/01b_build_fee_rate_history.py`

SCD Type 2 fee rate history from `silver/fees/` (BD Fees_OpalCapital_Daily).

- Separate from 01: different source, different change cadence, independent backfill
- Cross-validates against silver allocations for overlap period (2026-01-16+)
- Column resolver handles BD's inconsistent column naming across exports
- Exits cleanly when silver/fees/ doesn't exist yet (AE hasn't built the pipeline)
- `keep='last'` on trade_date dedup

Output: `gold/dimensions/fee_rate_history.parquet`

**Status**: Ready, waiting on AE to build silver/fees/ pipeline.

### 08c — Advisor Fee Efficiency
`data/black_diamond/scripts/gold/08c_build_advisor_fee_efficiency.py`

Per-advisor, per-role, per-day attribution of implied revenue vs NNA.

**Output 1** — Daily detail: `gold/canonical/advisor_fee_detail/{YYYY-MM-DD}.parquet`
- Grain: (advisor, role, date)
- For each account, for each active role: split-weighted AUA, implied fee, NNA, growth
- Point-in-time SCD lookups on both 01 and 01b
- Derived: nna_yield_ann, implied_annual_fee

**Output 2** — Scorecard JSON: `gold/artifacts/advisor_fee_efficiency.json`
- Per-advisor: managed_aua, implied_revenue (YTD + trailing 12M), NNA, growth, book_growth_rate, efficiency_ratio, fee_yield_bps, regression_residual
- Firm-level regression: NNA ~ Revenue (inline OLS, no dependencies)
- Positive residual = collecting more than contributing. Negative = growth engine.

### 05 — Client Performance (Thin Rewrite)
`data/black_diamond/scripts/gold/05_build_client_performance.py.new`

~280 lines replacing 1,055. Reads pre-built canonical outputs:
- 04a for relationship-level AUA, growth, cumulative NNA
- 03c + accounts_dimension for tax-status AUA split
- 02b canonical holdings for num_accounts, num_positions, pct_priced
- `lib/nna_flows.py` for separate cum_inflows/cum_outflows (Option B: 05 reads transactions for this one purpose)
- Legacy fields hardcoded: synthetic_aua = total_aua, synthetic_correction = 0, churn = 0

Writes exact same schema contract (16 columns) to `gold/timeseries/client_performance.parquet`.

**Status**: Written as .new, not swapped. Requires diff validation against old 05 output after full backfill.

### 11a — Employee Leaderboard Enhancement
`data/black_diamond/scripts/gold/11a_publish_portal_aggregates.py` (modified)

Added `build_employee_leaderboard()` that reads 08c advisor_fee_detail:
- All 8 time windows (3M/6M/1Y/2Y/3Y/MTD/QTD/YTD)
- Per-entry: roles list, NNA, AUA, growth_pct, implied_revenue, fee_yield_bps, efficiency_ratio, regression_residual, role_breakdown (per-role detail)
- Per-window regression: NNA ~ Revenue across all advisors
- Triple rank: rank_nna, rank_aua, rank_efficiency
- Graceful skip when 08c data doesn't exist yet
- Old architect_leaderboard.json preserved (dual-write until portal migrates)

Output: `gold/artifacts/employee_leaderboard.json`

---

## EC2 Validation Results (Single Date: 2026-04-02)

AE ran the full chain on bd-gold-layer-runner:

**02b (3-day backfill)**:
- 256,281 rows across 3 dates
- Source: 52.1% reconciled, 32.7% schwab_override, 10.1% schwab, 5.1% bd
- AUA: $1.604B (04-02), consistent with prior session

**03c**:
- Checksum drift: 0.000000
- AUA change: +$530K, price_return: -$420K, income: +$27K, realized: $0
- Growth: -$393K, NNA implied: +$923K

**04a**: 2,844 relationships, 6,075 accounts, 9 orphans

**04b**: R-squared = 0.0009 (single-date — meaningless, need multi-date)

---

## Full Backfill Requested

Sent AE instructions for full Schwab-coverage backfill:
- 02b: 2026-01-20 to 2026-04-02 (all Schwab RPS dates)
- 03c: 2026-01-21 to 2026-04-02
- 04a: same range
- 04b: same range with validation

This will produce ~50 dates of 04b output for representative R-squared vs legacy 05.

---

## Data Investigation: Fee Economics

- `account_fee_schedule` NOT on transaction records (only silver allocations 2026-01-16+)
- Silver allocations parseable: "49F - Flat 1.15" -> 115 bps (40/44 schedules parse deterministically)
- Allocations NOT usable as historical proxy: 74 accounts changed fee_bps in 2.5 months (~1.2%/quarter)
- Management Fee transactions in silver/transactions/ exist but sporadic (10/59 sampled dates), not a reliable billing source
- Decision: fee_bps on current records only in 01. Historical fee attribution blocked on silver/fees/ pipeline from AE.

---

## s3_layout.py Additions

```
CANONICAL_ACCOUNT_GAINS_PREFIX, canonical_account_gains_key()
CANONICAL_PERFORMANCE_PREFIX, canonical_performance_key()
CANONICAL_NNA_PREFIX, canonical_nna_key()
CANONICAL_NNA_VALIDATION_PREFIX, canonical_nna_validation_key()
FEE_RATE_HISTORY
ADVISOR_FEE_DETAIL_PREFIX, advisor_fee_detail_key()
ADVISOR_FEE_EFFICIENCY
EMPLOYEE_LEADERBOARD
```

---

## Pipeline Architecture (Complete)

```
L0   canonical_prices (existing)
L1   02b canonical_holdings (Schwab-reconciled positions)
L2   03b canonical_lots (unrealized + realized, tax detail)
L2.5 03c account_gains (per-account daily decomposition)
L3   04a canonical_performance (relationship-level + cumulatives)
L3   04b validate_nna (NNA output + legacy cross-check)
--   05  client_performance (thin assembler from 04a + 03c + 02b + txn)
--   08c advisor_fee_efficiency (NNA vs revenue attribution)
--   11a employee_leaderboard (unified, all roles, from 08c)
```

Dimension tables:
```
00   accounts_dimension (existing)
01   advisor_assignments_history (rebuilt: 6 roles + splits)
01b  fee_rate_history (awaiting silver/fees/)
```

---

## Next Steps

1. **Full backfill validation** — AE running 02b -> 03c -> 04a -> 04b across Schwab coverage
2. **05 swap** — diff new vs old, validate, replace
3. **Wire into run_gold_layer.sh** — 02b/03b/03c/04a/04b/05 in sequence
4. **AE delivers silver/fees/** — unlocks 01b, enables 08c fee attribution
5. **ADVI_NNAFEE project** — frontend team picks up employee_leaderboard.json for portal Books tab

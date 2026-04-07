# GLDOPS.004 — Session Handoff: Canonical Stack Complete, Awaiting Backfill Validation

**Agent:** 0.4.0_DS_ClientPlatform
**Date:** 2026-04-07
**Project:** ADVI_GLDOPS
**Task Order:** ADVI_GLDOPS.004
**Branch:** CLOUD (latest: `d0d5d9c8`)

---

## Where We Are

The full canonical stack is built, committed, pushed to git, and uploaded to S3. Every script has been reviewed, performance-optimized for the 64-core EC2, and the downstream pipeline is ready to consume. We are blocked on one thing: **AE running the full Schwab-coverage backfill** (02b -> 03c -> 04a -> 04b, 2026-01-20 to 2026-04-02). That backfill determines whether the new stack's NNA matches legacy 05 well enough to swap.

---

## Complete Script Inventory

### On S3 (s3://opal-data-bd/code/gold/) — ready to run:

| Script | What It Does | Status |
|--------|-------------|--------|
| 02b_build_canonical_holdings.py | Schwab-reconciled positions (L1) | Tested, 3 dates sealed |
| 03b_build_canonical_lots.py | Unrealized + realized tax lots (L2) | Built, needs backfill |
| 03c_build_account_gains.py | Per-account AUA decomposition (L2.5) | Tested single date, perf-optimized |
| 04a_build_canonical_performance.py | Relationship-level + cumulatives (L3) | Tested single date, perf-optimized |
| 04b_validate_nna.py | NNA output + legacy cross-check (L3) | Tested single date, needs multi-date |
| 01_build_advisor_assignments_history.py | 6 roles + 6 splits SCD | Rebuilt, not yet run on EC2 |
| 01b_build_fee_rate_history.py | Fee rate SCD from silver/fees/ | Built, blocked on AE pipeline |
| 08c_build_advisor_fee_efficiency.py | Advisor NNA vs revenue attribution | Built, perf-optimized |
| 11a_publish_portal_aggregates.py | Employee leaderboard added | Modified, dual-writes old + new |
| lib/s3_layout.py | 8 new S3 keys | Updated |

### In git but NOT on S3 (intentionally):

| Script | Why Not Deployed |
|--------|-----------------|
| 05_build_client_performance.py.new | Thin 05 rewrite. Does not replace production 05 until diff validation passes. |

---

## What Was Tested

### EC2 Single-Date Dry Run (2026-04-02)

AE ran the full chain on bd-gold-layer-runner. Results:

- **02b**: 3 dates, 256K rows, $1.604B AUA, source distribution matches expectations (52% reconciled, 33% override, 10% schwab, 5% bd)
- **03c**: Checksum drift = 0.000000. AUA change +$530K, growth -$393K, NNA +$923K. Clean.
- **04a**: 2,844 relationships, 6,075 accounts, 9 orphans
- **04b**: R-squared = 0.0009 vs legacy. **This is meaningless on a single date.** The comparison is between one day's residual NNA and a diff of legacy cumulative NNA. Multi-date backfill will give a real signal.

---

## Performance Optimizations Applied

All scripts audited for 64-core c6i.16xlarge:

| Fix | Script | Before | After |
|-----|--------|--------|-------|
| Position counting | 03c | Row-by-row loop (6K accts) | `value_counts()` |
| Cumulative computation | 04a | Double iterrows (2.8K rels x 5 cols x N dates) | Vectorized `map()` + add |
| Per-account role expansion | 08c | iterrows over 6K accounts x 5 roles | Vectorized merge + broadcast |
| Scorecard S3 reads | 08c | Sequential | `ThreadPoolExecutor(64)` |
| Fee detail S3 reads | 11a | Sequential | `ThreadPoolExecutor(64)` |
| 05.new | Already correct | `ThreadPoolExecutor(64)` throughout |

---

## Pending Actions (Ordered)

### 1. AE: Full Schwab-coverage backfill
Message sent at 03:46Z with instructions. Must re-sync code first (perf-optimized scripts uploaded after single-date test).

```
02b --upload --start-date 2026-01-20 --end-date 2026-04-02
03c --upload --start-date 2026-01-21 --end-date 2026-04-02
04a --upload --start-date 2026-01-21 --end-date 2026-04-02
04b --upload --start-date 2026-01-21 --end-date 2026-04-02
```

### 2. DS: Analyze 04b multi-date validation
- Avg R-squared across ~50 dates (should be >> 0.0009)
- Material divergence count and top divergent relationships
- Determine if systematic gaps exist or just noise

### 3. DS: Diff new 05 vs old 05
- Run new 05 to temp key
- Column-by-column comparison: total_aua, nna, market_growth, cum_inflows, cum_outflows
- Expected: close match on AUA/growth, divergence on NNA for model rotation accounts

### 4. Swap 05
- Rename .new to production
- Run 05c (validate_aua_vs_silver) as end-to-end checkpoint

### 5. Wire into run_gold_layer.sh
```
02  positions_cube
02b canonical_holdings
03  holdings_lots
03b canonical_lots
03c account_gains
04a canonical_performance  (parallel with 04b)
04b validate_nna           (parallel with 04a)
05  client_performance     (thin assembler)
05b-12 unchanged
```

### 6. Blocked on AE
- **silver/fees/ pipeline**: Unlocks 01b, which unlocks 08c fee attribution (currently implied_daily_fee = 0)
- **01 rebuild run**: New 01 with 6 roles + splits needs to be run on EC2 to produce the expanded assignment history

---

## Messages Sent

| To | Subject | Time |
|----|---------|------|
| 0.6.0_AE | Full backfill instructions (02b -> 04b) | 03:46Z |
| 0.6.0_AE | Code sync warning + hold on Step 5 | 03:59Z |
| 0.4.0_DT | Full inventory + verification commands + plan | 03:59Z |

---

## Architecture Reference

```
Dimensions:
  00  accounts_dimension
  01  advisor_assignments (6 roles + splits, from transactions 2020+)
  01b fee_rate_history    (from silver/fees/, awaiting AE)

Canonical Stack:
  L0   canonical_prices (existing)
  L1   02b canonical_holdings (Schwab-reconciled)
  L2   03b canonical_lots (unrealized + realized)
  L2.5 03c account_gains (per-account: AUA = growth + NNA)
  L3   04a canonical_performance (relationship-level + cumulatives)
  L3   04b validate_nna (NNA + legacy cross-check)

Compatibility:
  05   client_performance (thin assembler, same schema as old 05)

Analytics:
  08c  advisor_fee_efficiency (daily detail + scorecard JSON)
  11a  employee_leaderboard (unified, all roles, from 08c)
```

---

## Key Data Points

- Silver allocations anchor: $1.632B (BD official)
- Canonical AUA (02b): $1.604B (-1.7% pricing delta)
- 03c single-date: checksum drift 0.000000 (identity holds by construction)
- Fee schedules: 74/6,055 accounts changed bps in 2.5 months (1.2%/quarter) — cannot use current snapshot as historical proxy
- Management Fee transactions: sporadic (10/59 sampled dates), not a reliable billing source
- 05.new: ~280 lines vs 1,055, estimated 2-5 min vs 30-40 min runtime

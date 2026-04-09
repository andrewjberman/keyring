# GLDOPS.004 -- bd_stale False Positive Fix (02b)

**Agent:** 0.4.0_DS_ClientPlatform
**Date:** 2026-04-07
**Project:** ADVI_GLDOPS
**Task Order:** ADVI_GLDOPS.004
**Branch:** CLOUD

---

## Root Cause Analysis

Andrew asked for a full account-level decomposition of the -1.55% AUA gap
($1.602B gold vs $1.627B silver). Prior analysis hand-waved it as "pricing
difference." The real decomposition:

| Category | Accounts | Net Delta |
|----------|----------|-----------|
| Match (within $100) | 1,219 | +$4.5M |
| Overshoot (gold > silver) | 174 | +$20.4M |
| Undershoot (gold < silver) | 4,887 | -$43.9M |
| Silver-only | 211 | -$4.2M |
| Gold-only | 0 | $0 |
| **Total** | **6,491** | **-$23.2M** |

The undershoot dominates: 4,887 accounts, -$43.9M. 2,719 of those have fewer
positions in canonical than in the positions cube. Root cause: `bd_stale`
classification in `02b_build_canonical_holdings.py` `reconcile_date()`.

## The Bug

02b marks BD-only positions in Schwab-covered accounts as `bd_stale` (FIFO
ghost) and zeros their units. But two classes of positions are falsely dropped:

### 1. Cash positions ($212.1M, 5,548 positions)

`prepare_schwab_partition()` strips CASH/MONEY/MMKT/SWEEP from Schwab data
before the outer join. So BD cash positions in Schwab-covered accounts always
have no Schwab match -> marked `bd_stale` -> zeroed -> dropped. The cash was
filtered by us, not missing from the custodian.

### 2. Unresolvable assets ($36.5M, 2,834 positions)

Assets without a CUSIP mapping in the bridge (e.g., ISHARES MSCI USA QUALITY
FACTOR ETF, VANGUARD LONG-TERM TREASURY ETF, VANGUARD VALUE ETF, POLEN
DIVIDEND INCOME ETF) cannot be matched between BD and Schwab. The outer join
produces no Schwab row -> `bd_stale` -> zeroed. Schwab may well hold these
positions but the bridge can't prove it.

### Total gross error: $248.7M dropped

The net gap was only -$23.2M because Schwab gap-fills (+$20.4M overshoots)
partially offset the stale drops. But the gross displacement was $248.7M.

## The Fix

In `reconcile_date()`, after initial `bd_stale` classification, reclassify
two false-positive classes back to `source='bd'`:

```python
# 1. Cash: excluded from Schwab prep by design
is_cash_position = merged['asset_name'].apply(_is_cash)
source[(source == 'bd_stale') & is_cash_position] = 'bd'

# 2. Unresolvable: CUSIP bridge can't map, absence uninformative
if resolvable_assets is not None:
    is_unresolvable = ~merged['asset_name'].isin(resolvable_assets)
    source[(source == 'bd_stale') & is_unresolvable] = 'bd'
```

`resolvable_assets = set(cusip_to_name.values())` built in `main()`, threaded
through `process_date()` to `reconcile_date()`.

After fix, `bd_stale` only fires when:
- Account IS Schwab-covered
- Asset IS NOT cash/sweep
- Asset IS in the CUSIP bridge (Schwab could have reported it)
- Schwab did NOT report it (genuine FIFO ghost)

## Other Changes This Session

- Local 05 swap: `.py.new` -> `.py`, old -> `.legacy`
- `run_gold_layer.sh`: wired canonical stack (01b, 02b, 03b, 03c, 04a, 04b)
  into both incremental (20 steps) and full (26 steps) modes
- Task order GLDOPS.004 status -> `in_progress`

## Current State

- 02b fix committed locally, sent to AE for S3 upload + re-run
- AE will re-run: 02b(--force) -> 03b -> 03c -> 04a -> 04b -> 05 -> 05c
- Target: 05c gap under 0.5% (currently -1.55%)

## Next Steps

1. [AE] Upload fixed 02b, re-run canonical chain, report 05c gap
2. [DS] If gap < 0.5%: proceed with rebuilt 01, 08c, 11a, pipeline wiring
3. [DS] If gap still > 0.5%: investigate remaining bd_stale positions

## Do NOT

- Re-enable build_partner_analytics in bd-portal-publisher
- Change silver layer ingestion
- Remove bd_stale classification entirely (genuine ghosts still exist)

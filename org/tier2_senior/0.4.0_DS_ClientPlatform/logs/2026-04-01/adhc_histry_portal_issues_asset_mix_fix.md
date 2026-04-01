# ADHC_HISTRY: Portal Issues + Asset Mix Fix -- 0.4.0_DS_ClientPlatform

**Date:** 2026-04-01
**Start Time:** 7:30 PM ET
**End Time:** 9:00 PM ET
**Project:** ADHC_HISTRY
**Session:** Continuation of earlier HISTRY session

---

## Objective

Three portal problems identified by Andrew after the gold rebuild:
1. Portal showing data back to 1900 in NNA/GRO timeseries tables
2. Market growth math needs deep analysis (NNA looks good, growth looks off)
3. Books tab Firm Overview asset mix severely overstated vs total AUA

---

## Work Completed

### 1. .009 Model Coverage Analysis

Pulled results from S3 and analyzed with Andrew.

**49F AUM composition ($1,363,617,954 from RPS ground truth):**

| Category | MV | % |
|---|---|---|
| ACTIVE_MODEL | $1,041,557,786 | 76.38% |
| NON_MODEL | $291,533,094 | 21.38% |
| CASH_EQUIVALENT | $16,758,297 | 1.23% |
| OPAL_ETF | $7,991,663 | 0.59% |
| TRANSITIONAL | $5,777,114 | 0.42% |

Key findings:
- 76.4% model-aligned. Transitional rotation nearly complete.
- PATHFINDER DISCIPLINED: 6.98% actual vs 1.5% model target (+5.48pp) -- may indicate stale model weights
- PATHFINDER FOCUSED: 6.55% actual vs 1.5% target (+5.05pp)
- QQQ: 0.85% vs 4.8% target (-3.95pp), VUG: 0.15% vs 5.0% (-4.85pp) -- accounts in transition
- NON_MODEL $291.5M: ~$100M short-duration FI (deliberate), ~$50M individual stocks (legacy), ~$140M long tail

### 2. .008 Failure Timing Analysis

Results pulled and delivered to Andrew.

**KEY FINDING: Two separate BD feed problems:**

**Buy gaps (29,491 positions, $456M):**
- 2025-Q4: $259M (56.7%) -- ACTIVE ONGOING FAILURE, separate from onboarding
- 2024-Q3: $78M (17.0%)
- 2024-Q2: $51M (11.1%)
- 2025-Q1/Q2/Q3: near-zero
- 2026-Q1: $17M (3.7%) -- still occurring

**Sell gaps (61,473 positions, $495M):**
- 2024-Q2: $279M (56.3%) -- onboarding event, already handled
- 2024-Q3/Q4: $156M (31.5%)

Conclusion: Sell gaps are a historical onboarding wound. Buy gaps are an ACTIVE Q4 2025
delivery failure that needs vendor escalation with Black Diamond.

### 3. BD Account Universe Clarification

Andrew asked whether Schwab RPS ($1.36B) covers all of 49F's assets.

Investigation via accounts_dimension_latest.parquet:
- BD tracks 9,900 accounts total -- entire 49Financial advisor platform
- Individual advisor books (90+ named advisors) + ops groups + sub-programs
- "49F Schwab AUM" portfolio_group: 1,021 accounts (Schwab-specific tag)
- "49 Private Wealth": 39 accounts; "49 Solutions": 25 accounts
- BD account_id format: z-prefix (z0812893211) -- BD internal IDs, NOT Schwab account numbers
- Schwab mapping (6,510 accounts) matched via BD's account_number field ≠ account_id

**Conclusion:** BD aggregates multiple custodians. Schwab RPS = Schwab-custodied subset only.
The ~$224M difference between RPS ($1.364B) and BD silver ($1.587B) is assets at
other custodians (Fidelity, Pershing, etc.) or unmapped Schwab accounts. BD transaction
failures in other custodians are invisible without equivalent RPS data.

### 4. Portal 1900 Data Issue -- Diagnosis + Fix Deployed

**Root cause:** The positions_cube had 43,500 bad partitions from 1901-01-01.
The gold rebuild today ran BEFORE the cleanup, so all downstream scripts (05, 07, 08, 09, 10)
processed the full 45,742-partition cube and baked 1900 dates into their outputs.

**Fix:** AE queued incremental rebuild (--start-date 2020-01-01) using the clean 2,278-partition
cube. After rebuild: CloudFront invalidation to flush any cached responses.

The 1901 date clamp (commit 0a1fc2ba) prevents recurrence on future runs.

### 5. Market Growth Architecture Direction

Andrew clarified: NNA and market growth should be derived FROM the canonical holdings
timeseries, not computed in parallel from raw transactions.

**Architecture direction (approved, sent to AE):**
- Canonical holdings timeseries (positions_cube with RPS injection) = ground truth
- NNA = cash transfer flows from BD transactions (already correct -- BD delivers these reliably)
- Market growth = delta_canonical_aua - nna
- Synthetic injection = "AUA Reconciliation" line item (one-time correction, not market growth)
- synthetic_positions_index.parquet (written by script 02) enables script 05 to separate
  synthetic AUA from organic AUA when rearchitecture proceeds

This work is approved but not yet implemented. Pending Andrew's sign-off on diagnostics.

### 6. Asset Mix Overstatement -- Root Cause + Fix

**The problem:** Books tab Firm Overview showed:
- Total AUA: $1.58B (correct)
- Equity: $1.41B, Fixed Income: $519M, Alts: $71M, Other: $33M
- Sum of categories: $2.033B -- $453M MORE than total AUA

**Root cause:**

Script 03 (holdings_lots) has NO sell injection. The phantom lot reconciliation
(lines 1049-1105) uses BD allocations as authority (Rule 1: alloc < $100, Rule 2:
lots > 2× alloc). But BD's allocations are WRONG for the ~$513M in phantom positions
(BD still shows AUA for accounts with missing sell transactions). So those positions
pass both rules and remain as is_open=True in holdings_lots.

Script 02 (positions cube) DOES have sell injection via `_load_realized_sell_events`
and RPS sell rotation -- that's why total AUA (from positions cube) is correct at $1.58B.
But holdings_lots still holds all the phantom positions as open, inflating equity and
fixed income by ~$453M.

**Fix (commit 5800ae2a):**

Modified `_build_rps_synthetic_lots` in script 03 to also identify sell gaps (FIFO > RPS)
and return them as `sell_corrections` dict {(account_id, asset_name): rps_units}.

Added `_apply_rps_lot_corrections(df, sell_corrections)` which:
- Zero-close case (rps_units = 0): vectorized batch close of all open lots for that position
- Partial-reduce case (rps_units > 0): iteratively close newest lots until total matches RPS

Call site in `build_holdings_lots_snapshot` applies corrections BEFORE appending synthetic
buy lots, so the lot DataFrame going into asset classification reflects RPS ground truth.

**Expected result after full rebuild:**
- holdings_lots MV: ~$1.58B (from ~$2.03B)
- Equity: ~$1.0-1.1B (from $1.41B)
- Fixed income: ~$280-320M (from $519M)
- Asset mix sums to approximately total AUA

---

## Decisions Made

| Decision | Rationale |
|---|---|
| Incremental rebuild for 1900 fix, full rebuild for asset mix fix | Incremental is fast (minutes) and fixes portal display; full rebuild required for lot-level corrections to propagate correctly |
| RPS sell corrections applied before buy injection in script 03 | Must close phantom positions first before adding new synthetic lots, otherwise corrections would incorrectly target newly-added positions |
| Architecture: NNA/growth from canonical holdings timeseries | Current mismatch (NNA from raw transactions, AUA from injected cube) causes distorted market appreciation; canonical source must be unified |

---

## Files Modified

| File | Change | Committed |
|---|---|---|
| `gold/03_build_holdings_lots.py` | _build_rps_synthetic_lots returns sell_corrections; _apply_rps_lot_corrections closes phantom lots; call site wired | `5800ae2a` |

---

## Briefs Written

| Brief | Path | Audience |
|---|---|---|
| Two-step rebuild instructions | MCP to AE (20260401T203545Z) | AE |
| NNA/market growth architecture | MCP to AE (20260401T191624Z) | AE |
| Architecture GO | MCP to AE (20260401T191708Z) | AE |

---

## Current State

**Status:** FIXES DEPLOYED. AE running two-phase rebuild.
**Active branch:** CLOUD

Two rebuilds queued with AE:
1. Incremental rebuild (in progress or queued) -- fixes 1900 portal display
2. Full rebuild with script 03 at 5800ae2a -- fixes asset mix overstatement

---

## Next Steps

1. **[0.6.0_AE_PartnerETL]** Complete incremental rebuild → CloudFront invalidation
2. **[0.6.0_AE_PartnerETL]** Upload script 03 (5800ae2a) → full rebuild → verify
   holdings_lots total MV ≈ $1.58B in run summary
3. **[Andrew / Black Diamond vendor]** Investigate Q4 2025 buy transaction delivery
   failure ($259M missing buys from that quarter, still accruing in 2026-Q1)
4. **[Andrew]** Validate PATHFINDER model weights -- are PDFE/PFOE still at 1.5% or
   has the 49F model been updated to higher Pathfinder allocation?
5. **[0.4.0_DS_ClientPlatform]** When Andrew confirms: scope NNA/market growth
   rearchitecture -- compute market appreciation from canonical holdings timeseries

**Do NOT:**
- Trust asset mix numbers until full rebuild with 5800ae2a completes
- Assume PATHFINDER overweights are a bug until model weights are validated
- Modify script 02's sell injection -- it is working correctly for the positions cube

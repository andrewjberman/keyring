# ADVI_PRICES: Post-Fix Verification — 0.4.0_DS_ClientPlatform

**Date:** 2026-03-24
**Branch:** CLOUD

---

## Result

AE ran gold layer FULL rebuild with updated scripts 02 and 03 and re-ran the recon against 2026-03-19 allocations.

| Metric | Before | After | Change |
|---|---|---|---|
| BD AUA | $1,593,308,085 | $1,593,308,085 | — |
| Lot MV | $1,889,291,370 | $1,535,649,187 | -$353.6M |
| Net gap | +$295,983,285 (+18.6%) | -$57,658,898 (-3.6%) | **$353.6M improvement** |
| Gross overshoot | $494,047,695 (4,129 accts) | $116,620,339 (1,986 accts) | -$377.4M |
| RC1 Phantom | $91,211,940 (268 accts) | $1,121,298 (77 accts) | **98.8% eliminated** |
| Lots force-closed | — | 74,035 lots, $351.0M | 2,080 accounts cleaned |
| Largest remaining phantom | $55,917,914 | $48,000 | Noise |

---

## What Changed

Three code fixes deployed to scripts 02 (`positions_cube`) and 03 (`holdings_lots`):

**1. Allocation-authority phantom lot reconciliation (script 03)**
After FIFO builds all lots, loads `silver/allocations/{date}.parquet` and force-closes lots in accounts where BD has zeroed or significantly diminished AUA:
- Rule 1: BD AUA < $100 — account fully removed from BD. Force-close all lots.
- Rule 2: BD AUA >= $100 but lot MV > 2x AUA and lot MV > $50K — incomplete exit transactions. Force-close all lots.

This is the primary driver of the improvement: 2,080 accounts, 74,035 lots, $351M removed.

**2. Phantom account exclusion (script 02)**
Same Rule 1 applied to positions_cube output. Ensures scripts 05 (client_performance), 05b (account_performance), and 06b (mix_timeseries) also report clean numbers.

**3. Temporal guard spillover fix (script 03)**
FIFO sell processing now handles derivatives where BD records buy dates after exercise/expiry. Sell volume blocked by the temporal guard is accumulated and applied in a second pass. Fixed a $55.9M phantom on one derivatives account.

---

## Decomposition of the Remaining -$57.7M Gap

The undershoot is clean, explainable, and matches what the diagnostics predicted:

| Component | Amount | Explanation | Actionable? |
|---|---|---|---|
| T1 pricing undershoot | ~-$41M | Our transaction-observed price for 5 core ETFs (IEFA, IDVZ, Pathfinder US/Focused, iShares EM) is 6-12% below BD's end-of-day NAV. Systematic methodology difference — our T1 captures trade-execution price, BD uses vendor close. | Yes — switch these 5 to yahoo_finance or scoped_override to recover ~$40M |
| Structural gaps (EX1-EX6) | ~-$15M | 394 accounts that cannot be reconciled: bank/savings (53), insurance with zero lots (5), term life (15), alloc-only/held-away (99), de minimis (221), credit (1). No transaction data exists. | No — by design. Documented in `docs/data/structural_gap_exclusions.md` |
| Residual | ~-$2M | Normal pricing variance across ~6,000 accounts | No — noise |

---

## Investigation Path (for reference)

The ADVI_PRICES investigation ran 12 diagnostic scripts testing 4 hypotheses before identifying the root cause:

| Hypothesis | Result |
|---|---|
| Missing exit transaction types | DISPROVEN — zero unrecognized types in data |
| Asset name mismatch in FIFO grouping | DISPROVEN — 0 real matches |
| Dedup/NaN/temporal guard losing sell volume | MINOR — temporal guard fixed one $56M account, dedup and NaN negligible |
| BD transaction feed incomplete | CONFIRMED — 73% of phantom positions had zero sell transactions in all history |

Pattern analysis revealed: 17 of top 25 phantom accounts had BD AUA = $0 with account_type = nan (BD fully removed them); 12 shared the z0814* prefix (custodian cluster); a 2023Q1 sell-stop cohort (76 accounts) suggests a BD feed discontinuity.

The allocation-authority reconciliation was the correct fix because the exit transactions don't exist and can't be recovered. BD's allocation is the system of record for account existence.

---

## What's Deployed

12 commits on CLOUD branch. 3 code changes + 9 diagnostic scripts:

**Code (production impact):**
- `03_build_holdings_lots.py` — temporal guard fix + allocation-authority reconciliation + taxonomy expansion
- `02_build_positions_cube.py` — phantom account exclusion (Rule 1)
- `docs/data/transaction_type_canonical_reference.md` — updated

**Diagnostics (reusable monitoring):**
- `recon_lots_vs_allocations.py` — same-date recon with RC classification and waterfall
- `diag_pricing_divergence.py` — per-security pricing impact by source (ADVI_PRICES-002 WS1)
- `build_structural_exclusion_list.py` — dated exclusion parquet (ADVI_PRICES-002 WS2)
- `docs/data/structural_gap_exclusions.md` — exclusion code reference
- Plus 6 investigation diagnostics (taxonomy, name mismatch, FIFO replay, over/undershoot, patterns, concentration)

---

## Recommended Next Steps (COO decision points)

**1. T1 pricing for 5 core ETFs (recovers ~$40M of undershoot)**
Switch IEFA, IDVZ, Pathfinder US Equity, Pathfinder Focused Opportunities, and iShares Core EM from `transaction_observed` to `yahoo_finance` as the canonical price source. These are high-volume liquid ETFs where Yahoo close is more accurate than trade-execution price. This is a configuration change in `bd_price_update.py`, not a code change. Narrows the gap from -3.6% to approximately -1.0%.

**2. Apply structural exclusion list to monitoring**
Integrate the EX1-EX6 exclusion parquet (`gold/exclusions/structural_gaps_{date}.parquet`) into the daily `05c_validate_aua_vs_silver.py` check so the $15M structural gap is reported separately from the reconciliation error. Currently planned but not yet wired.

**3. Investigate the 2023Q1 sell-stop cohort (AE scope)**
76 partial-sell phantom accounts all had their last sell in Q1 2023. Understanding what changed at BD around that date could prevent future phantom accumulation. Not urgent — the allocation-authority rules catch these going forward.

**4. Push to remote (DT scope)**
12 commits pending on CLOUD. DT should push after COO approval.

---

## Files Modified

| File | Commit |
|------|--------|
| `data/black_diamond/scripts/gold/03_build_holdings_lots.py` | `f1b3f33d`, `4278798e`, `c50877b0` |
| `data/black_diamond/scripts/gold/02_build_positions_cube.py` | `7dd2432b` |
| `docs/data/transaction_type_canonical_reference.md` | `f1b3f33d` |
| `docs/data/structural_gap_exclusions.md` | `4d6a0258` |
| `data/black_diamond/scripts/diagnostics/recon_lots_vs_allocations.py` | `9b039259` |
| `data/black_diamond/scripts/diagnostics/diag_txn_taxonomy_enumeration.py` | `9b039259` |
| `data/black_diamond/scripts/diagnostics/diag_phantom_asset_name_mismatch.py` | `2d0dcad9` |
| `data/black_diamond/scripts/diagnostics/diag_phantom_fifo_replay.py` | `62ce146d` |
| `data/black_diamond/scripts/diagnostics/diag_undershoot_accounts.py` | `2a4153c0` |
| `data/black_diamond/scripts/diagnostics/diag_overshoot_accounts.py` | `2a4153c0` |
| `data/black_diamond/scripts/diagnostics/diag_phantom_zero_sells_patterns.py` | `1fb5bcfe` |
| `data/black_diamond/scripts/diagnostics/diag_phantom_partial_sells_patterns.py` | `1fb5bcfe` |
| `data/black_diamond/scripts/diagnostics/diag_phantom_concentration.py` | `3fbd79db` |
| `data/black_diamond/scripts/diagnostics/diag_pricing_divergence.py` | `0c62a3a2` |
| `data/black_diamond/scripts/diagnostics/build_structural_exclusion_list.py` | `4d6a0258` |

# v2 Cap Exemptions + Min-Observation Guard — ADVI_GLDRST.021b

**Agent:** 0.4.0_DS_ClientPlatform
**Date:** 2026-04-10
**Task order:** `ADVI_GLDRST.021b.ds-t1-cap-exemptions-and-minsample.md`
**Project:** ADVI_GLDRST
**Status:** shipped (code committed, pushed, S3-staged)

## Objective

Stop the T1 50x outlier cap from silently rewriting legitimate prices. Add two narrowly-scoped exclusions:
1. `_T1_CAP_EXEMPTIONS` frozenset — named assets with legitimate regime shifts (stock splits, reverse splits) whose observation count is large but whose asset median is legitimately post-shift.
2. `MIN_OBSERVATIONS_FOR_CAP = 15` — any asset with fewer than 15 daily T1 observations is exempt from the cap entirely. Catches thinly-traded collective-trust-style assets whose history is polluted by synthetic $1.00 accounting entries.

Expected outcome (from TO `<acceptance_criteria>` #4): 31 → 8 capped rows, 14 → 8 distinct assets capped, zero price changes on the 8 corruption rows that must stay caught.

## Change summary

Module-level additions in `data/black_diamond/scripts/silver/build_canonical_prices_v2.py` (above `build_t1_from_transactions`):

```python
_T1_CAP_EXEMPTIONS: frozenset[str] = frozenset({
    'CHIPOTLE MEXICAN GRILL INC COM',           # 50:1 split 2024-06-26 (yfinance confirmed)
    'PRAXIS PRECISION MEDICINES INC COM NEW',   # 1:15 reverse split 2023-11-29 + late-2025 runup (yfinance confirmed)
})

MIN_OBSERVATIONS_FOR_CAP = 15
```

The preceding comment block documents the rationale for both constants, including the observation-count table from the audit (sparse-pollution group: 3-9 obs, corruption group: 30-51 obs, regime-shift group: 36-78 obs), so the 15-point threshold is justified in-code.

Cap-application logic inside `build_t1_from_transactions` (replaces the `outlier_mask`-only path from .021):

```python
asset_median = t1.groupby('asset_name')['price'].median().rename('asset_med')
asset_n_obs  = t1.groupby('asset_name').size().rename('n_obs')
t1 = t1.join(asset_median, on='asset_name').join(asset_n_obs, on='asset_name')

outlier_mask    = (t1['asset_med'] > 0) & (t1['price'] > 50 * t1['asset_med'])
is_exempt       = t1['asset_name'].isin(_T1_CAP_EXEMPTIONS)
has_enough_obs  = t1['n_obs'] >= MIN_OBSERVATIONS_FOR_CAP
should_cap_mask = outlier_mask & ~is_exempt & has_enough_obs
```

The rewrite (`t1.loc[should_cap_mask, 'price'] = asset_med`) and the `capped=True` flag are applied only on `should_cap_mask`. The `source='transaction_observed_capped'` propagation in `resolve_prices_for_asset` from .021 is unchanged — capped rows still surface with the tag.

New console output during each build clearly separates "candidates >50x" from "skipped by named exemption", "skipped by n_obs<15 guard", and "capped at asset median", so a future operator can see at a glance whether the exclusions are firing correctly.

New diff harness: `data/analysis/v2_cap_021b_diff.py`. Independently replicates the .021 path (no exemptions, no guard) so it can compare "021 state" vs "021b candidate" in a single process without needing a git checkout.

## Diff-before-ship result

Harness: `data/analysis/v2_cap_021b_diff.py`
Input: `silver/transactions/` snapshot at 2026-04-10 — 1,767 parquet files, 2,879,975 deduped rows.
Runtime: ~60s load + two T1 builds.

| Metric | Before 021b (021 state) | After 021b | Delta |
|---|---:|---:|---:|
| Rows tagged `transaction_observed_capped` | 31 | **8** | -23 |
| Distinct assets with any capped row | 14 | **8** | -6 |
| CMG rows capped | 4 | 0 | -4 |
| PRAX rows capped | 9 | 0 | -9 |
| Vanguard INSTL 500 IDX TRST GM rows capped | 4 | 0 | -4 |
| Vanguard INSTL TOTAL BD ID GM rows capped | 4 | 0 | -4 |
| Red Rock Resorts rows capped | 1 | 0 | -1 |
| Vanguard Explorer Fund GM rows capped | 1 | 0 | -1 |
| Corruption-group rows (all 2024-08-07) | 8 | 8 | 0 |
| Price changes on corruption-group rows | N/A | **0** | 0 |
| Newly-capped rows (false positives from guard) | N/A | **0** | 0 |

**Matches the TO's expected outcome table exactly.** All 8 hard checks passed in the harness:
- 021 capped == 31 ✓
- 021b capped == 8 ✓
- uncapped_in_021b == 23 ✓
- newly_capped_021b == 0 ✓
- still_capped == 8 ✓
- dropout counts match per-asset expectations ✓
- still-capped counts match per-asset expectations ✓
- price changes on still-capped == 0 ✓

### 23 newly-uncapped rows (the drop-out set)

| Asset | Date | Pre-cap price (now preserved) |
|---|---|---:|
| CHIPOTLE MEXICAN GRILL INC COM | 2024-05-10 | $3,239.2300 |
| CHIPOTLE MEXICAN GRILL INC COM | 2024-05-14 | $3,185.7000 |
| CHIPOTLE MEXICAN GRILL INC COM | 2024-05-16 | $3,145.8800 |
| CHIPOTLE MEXICAN GRILL INC COM | 2024-05-17 | $3,168.4800 |
| PRAXIS PRECISION MEDICINES INC COM NEW | 2025-10-16 | $157.2050 |
| PRAXIS PRECISION MEDICINES INC COM NEW | 2025-10-17 | $189.0800 |
| PRAXIS PRECISION MEDICINES INC COM NEW | 2025-10-27 | $182.6409 |
| PRAXIS PRECISION MEDICINES INC COM NEW | 2025-10-28 | $192.4173 |
| PRAXIS PRECISION MEDICINES INC COM NEW | 2025-12-12 | $267.6550 |
| PRAXIS PRECISION MEDICINES INC COM NEW | 2026-01-09 | $304.8552 |
| PRAXIS PRECISION MEDICINES INC COM NEW | 2026-02-09 | $321.0850 |
| PRAXIS PRECISION MEDICINES INC COM NEW | 2026-02-25 | $345.0347 |
| PRAXIS PRECISION MEDICINES INC COM NEW | 2026-03-30 | $284.6650 |
| RED ROCK RESORTS INC CL A | 2025-07-02 | $54.2297 |
| VANGUARD EXPLORER FUND GM | 2025-03-24 | $100.0000 |
| VANGUARD INSTL 500 IDX TRST GM | 2024-07-29 | $55.6000 |
| VANGUARD INSTL 500 IDX TRST GM | 2024-10-01 | $58.3212 |
| VANGUARD INSTL 500 IDX TRST GM | 2025-01-02 | $60.0000 |
| VANGUARD INSTL 500 IDX TRST GM | 2025-03-24 | $58.3333 |
| VANGUARD INSTL TOTAL BD ID GM | 2024-07-29 | $108.9700 |
| VANGUARD INSTL TOTAL BD ID GM | 2024-10-01 | $113.3482 |
| VANGUARD INSTL TOTAL BD ID GM | 2025-01-02 | $109.6875 |
| VANGUARD INSTL TOTAL BD ID GM | 2025-03-24 | $120.0000 |

All 23 drop-outs now carry plain `source='transaction_observed'` in the final canonical_prices output. None are rewritten.

### 8 still-capped rows (regression check)

| Asset | Date | Pre-cap | Post-cap |
|---|---|---:|---:|
| INVESCO STABLE VALUE RET CL 1 | 2024-08-07 | $60,077.44 | $1.0000 |
| DODGE & COX INCOME X | 2024-08-07 | $40,412.03 | $12.4900 |
| NORTHERN TRST COLL EAFE IDX T3 | 2024-08-07 | $26,108.78 | $159.2880 |
| NORTHERN TRUST S&P 500 TIER 3 | 2024-08-07 | $31,217.93 | $556.5877 |
| NT AGG BOND INDEX DC NL TIER 3 | 2024-08-07 | $71,863.58 | $124.9208 |
| PGIM JENNISON SMALL COMPANY R6 | 2024-08-07 | $8,625.90 | $23.5500 |
| VANGUARD BALANCED INDEX I | 2024-08-07 | $29,441.74 | $48.5815 |
| VANGUARD EMERGING MKTS STOCK IDX INSTL | 2024-08-07 | $5,833.23 | $28.8508 |

All 8 are on 2024-08-07. All 8 prices match the .021 output exactly (no drift). **INVESCO STABLE VALUE RET CL 1 is still caught** — the canonical regression anchor.

## Compiler Tools

### Phase 1 (before writing) — `comp-trace canonical_prices`

Blast radius: 15 upstream consumers (unchanged from .021):
- A_03.positions_cube, B_01.holdings_lots, E_00, E_01, E_05, E_06, E_07, E_08, E_09, E_10, E_11, E_12, E_13, E_14, E_16, bd-price-update

Byte-level diff against `/tmp/phase1_blast.txt` (the .021 baseline) after CRLF/LF normalization: **identical**. No new edges, no dropped consumers, no rename drift.

Saved: `/tmp/phase1_021b_blast.txt` / `/tmp/phase1_021b_blast_clean.txt`.

### Phase 3 (after writing) — re-run

`comp-trace canonical_prices` → CRLF-normalized diff against Phase 1 → **identical**. The exemption frozenset and min-observation guard are purely internal to `build_t1_from_transactions`; they do not add or remove any I/O edge, so the graph is unchanged as expected.

Saved: `/tmp/phase3_021b_blast.txt` / `/tmp/phase3_021b_blast_clean.txt`.

## Artifacts

| Artifact | Path / reference |
|---|---|
| Modified script | `data/black_diamond/scripts/silver/build_canonical_prices_v2.py` |
| New diff harness | `data/analysis/v2_cap_021b_diff.py` |
| Session log | this file |
| S3 upload | `s3://opal-data-bd/code/silver/build_canonical_prices_v2.py` |
| Commit SHA | `{{COMMIT_SHA}}` |
| S3 etag | `{{S3_ETAG}}` |

## Do-not verification

- [x] 50x threshold unchanged.
- [x] Cap replacement value unchanged (still `asset_med`).
- [x] Within-day collapse at line 183-184 untouched.
- [x] `_T1_CAP_EXEMPTIONS` contains exactly CMG and PRAX (no sparse-pollution assets).
- [x] `MIN_OBSERVATIONS_FOR_CAP = 15` is a module constant, not parameterized.
- [x] Audit follow-ups #2 (synthetic $1 filter), #3 (PRAX history truncation), #4 (upstream BD source audit) all deferred — not touched in this TO.
- [x] No gold-runner trigger, no Lambda invocation.
- [x] Upload targets `code/silver/`, not `code/gold/`.
- [x] Diff-before-ship run; all hard checks passed before commit.

## Next Steps — unblocks ADVI_GLDRST.022

ADVI_GLDRST.022 (v2 as nightly pre-step on the gold runner) was waiting on 021b. With this commit shipped and the cap now behaving correctly on production data:

1. The "v2 silently smoothing legitimate prices" blocker is resolved.
2. canonical_prices.parquet produced by v2 now carries accurate T1 values for CMG, PRAX, the Vanguard GM collective trusts, Red Rock Resorts, and Vanguard Explorer Fund GM — all of which flow into A_03.positions_cube and downstream AUA / MV calculations.
3. .022 can now proceed with wiring v2 into the bd-gold-layer-runner's pre-step sequence and moving the script from `code/silver/` to `code/gold/` (or wherever .022 decides it should live).

ADVI_GLDRST.022 stays in `staged` state per the TO — the flip to `in_progress` belongs there, not here.

## Deferred follow-ups (for future TO scope)

From the audit findings doc's "Follow-up recommendations beyond the exemption list" section:

1. **Filter synthetic $1.00 entries out of the median computation.** Root-cause fix for the sparse-pollution group. Would make `MIN_OBSERVATIONS_FOR_CAP` redundant for that class of assets. Riskier than the current guard because it requires detecting which $1.00 rows are synthetic vs legitimate stable-value observations (INVESCO stable value at $1.00 is real).
2. **Truncate pre-regime-shift history for "NEW"-suffixed BD asset names.** Root-cause fix for PRAX. Would make the explicit exemption unnecessary.
3. **Audit the 2024-08-07 BD source file directly.** All 8 corruption cases cluster on exactly one date — almost certainly a single broken input file. Worth pulling the raw BD extract for 2024-08-07 and asking BD to resend rather than relying on the cap as a permanent shield. This is outside DS scope — flag for Andrew.

None of the above are in 021b scope. Noted here so the next DS picking up this area has the trail.

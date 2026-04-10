# v2 Source-Tag and Diff-Before-Ship — ADVI_GLDRST.021

**Agent:** 0.4.0_DS_ClientPlatform
**Date:** 2026-04-10
**Task order:** `ADVI_GLDRST.021.ds-v2-source-tag-and-diff.md`
**Project:** ADVI_GLDRST
**Status:** shipped (code + harness committed, uploaded to `s3://opal-data-bd/code/silver/`)

## Objective

Make the T1 50x outlier cap in `build_canonical_prices_v2.py` auditable without changing its behavior. Add a `transaction_observed_capped` source tag on rows the cap rewrites, document the tradeoff inline, and prove via a diff-before-ship that zero price values changed between runs.

## Change summary

Two functions touched, one downstream resolver updated, one diff harness added.

1. `build_t1_from_transactions` (`data/black_diamond/scripts/silver/build_canonical_prices_v2.py:189-214`):
   - Added `t1['capped']` boolean column (default False).
   - Sets `capped=True` on every row the 50x outlier mask rewrites (same mask, same replacement value — no behavioral change).
   - New inline comment documents the known tradeoff: legitimate 50x+ regime shifts (splits, IPO pops, denom changes) are still silently smoothed in the numeric output, but the source tag makes them detectable.

2. Step 3 spine join (`build_canonical` in the same file):
   - `t1_prices` now carries `capped` → merged into `spine` as `t1_capped` with `fillna(False)` so every spine row has a bool.

3. `resolve_prices_for_asset`:
   - Reads `group_df['t1_capped']` at function entry (defensive `if 't1_capped' in columns` guard).
   - Both Yahoo-first and T1-primary branches now emit `source='transaction_observed_capped'` on rows where T1 supplied the price AND the capped flag is True.
   - `t1_mask` in the staleness check now uses `isin(['transaction_observed', 'transaction_observed_capped'])` so capped rows still participate in the staleness cap (preserves prior behavior for those rows).

4. New file: `data/analysis/v2_cap_tag_diff.py` — one-shot diff harness. Loads silver transactions once, runs an in-lined pre-modification T1 build and the imported new build against the same input, asserts zero price-value drift, prints the capped-row audit table and the 2024-08-07 regression check.

## Inline tradeoff comment (as committed)

```
# Per-asset outlier filter: if any day's T1 price exceeds 50x that asset's
# own historical median, it's a corrupt observation (both BD price and MV
# fields can be simultaneously wrong, e.g. collective trust entries on
# 2024-08-07 where price=$60K and MV=-$3.6B for a $1.00 stable value fund).
# Replace corrupt outliers with the asset's historical median.
#
# Known tradeoff: legitimate 50x+ regime shifts (splits, IPO pops, denom
# changes) are silently rewritten in the numeric output. Capped rows are
# flagged with source='transaction_observed_capped' downstream so any
# consumer surfacing unexpected smoothing can detect and review them.
```

## Diff-before-ship result

Harness: `data/analysis/v2_cap_tag_diff.py`
Input: `silver/transactions/` at 2026-04-10 snapshot — 1,767 parquet files, 2,912,252 rows (2,879,975 after dedup).
Runtime: ~60s load + two T1 builds.

| Metric | Value |
|---|---|
| T1 rows old | 197,408 |
| T1 rows new | 197,408 |
| Row-alignment drift (only_old / only_new) | 0 / 0 |
| Max absolute price delta | **0** |
| Price values changed | **0** |
| Rows newly tagged `transaction_observed_capped` | **31** |
| Distinct assets affected | **14** |
| Old-vs-new capped-mask mismatch | 0 |

**Mandatory acceptance hit:** every price value is identical between the two runs. The only delta is additive — a new `capped` column in T1 and a new `transaction_observed_capped` value in the final `source` column of rows it reaches.

### First 10 capped rows (asset, date, pre-cap price, post-cap price)

| Asset | Date | Pre-cap | Post-cap |
|---|---|---:|---:|
| CHIPOTLE MEXICAN GRILL INC COM | 2024-05-10 | $3,239.23 | $55.4492 |
| CHIPOTLE MEXICAN GRILL INC COM | 2024-05-14 | $3,185.70 | $55.4492 |
| CHIPOTLE MEXICAN GRILL INC COM | 2024-05-16 | $3,145.88 | $55.4492 |
| CHIPOTLE MEXICAN GRILL INC COM | 2024-05-17 | $3,168.48 | $55.4492 |
| DODGE & COX INCOME X | 2024-08-07 | $40,412.03 | $12.4900 |
| INVESCO STABLE VALUE RET CL 1 | 2024-08-07 | $60,077.44 | $1.0000 |
| NORTHERN TRST COLL EAFE IDX T3 | 2024-08-07 | $26,108.78 | $159.2880 |
| NORTHERN TRUST S&P 500 TIER 3 | 2024-08-07 | $31,217.93 | $556.5877 |
| NT AGG BOND INDEX DC NL TIER 3 | 2024-08-07 | $71,863.58 | $124.9208 |
| PGIM JENNISON SMALL COMPANY R6 | 2024-08-07 | $8,625.90 | $23.5500 |

### Regression check — 2024-08-07 collective trust incident

- Total capped rows on 2024-08-07: **8**
- Matches `stable|collective|CTF|common trust`: **1** — `INVESCO STABLE VALUE RET CL 1` ($60,077.44 → $1.00)
- The original incident the cap was written for is still caught. **PASS.**
- The other 7 capped rows on that date (Northern Trust tiers, NT Agg Bond, Dodge & Cox Income X, PGIM Jennison Small Company, etc.) are collective-trust-style vehicles whose names do not match the narrow "stable/collective/CTF" regex but clearly represent the same 2024-08-07 data-quality event. The cap correctly rewrites all of them.

### Finding: the Chipotle rows are a real tradeoff case

Four of the 31 capped rows are legitimate pre-split prices for Chipotle Mexican Grill (CMG had a 50-for-1 stock split on 2024-06-25). Pre-split, CMG traded around $3,000-3,200; post-split, around $55. The asset historical median is the post-split median ($55.45), so the 50x threshold fires and rewrites the pre-split values down to the median.

This is **exactly** the known tradeoff the new inline comment documents: the cap is behaving defensively but silently smoothing a legitimate regime shift. With the new tag in place, any downstream consumer that surfaces `source='transaction_observed_capped'` will see these rows flagged and can review them. No price-value correction in this TO — behavior is unchanged per explicit decision. A follow-up could add a per-asset split-aware exception, but that is out of scope.

## Compiler Tools — blast radius

### Phase 1 (before writing) — `comp-trace canonical_prices`

Upstream consumers of `s3:silver/prices/canonical_prices.parquet`:
- A_03.positions_cube:_load_phantom_exclusion_set (gold)
- B_01.holdings_lots:load_latest_prices (gold)
- E_00, E_01, E_05, E_06, E_07, E_08, E_09, E_10, E_11, E_12, E_13, E_14, E_16 (diagnostics)
- bd-price-update (lambda)

Source-column usage audit (grep for filters / equality / `isin` on `'source'`):

| Consumer | Behavior | Break risk |
|---|---|---|
| A_03.positions_cube | No source filter; pass-through | Safe |
| B_01.holdings_lots | Renames `source`→`price_quality` and merges; pass-through | Safe; capped rows surface as a new `price_quality` value downstream |
| bd-price-update | Writes its own `source='yahoo_finance'`; never filters canonical | Safe |
| E_00.decompose_aua_gap | Uses `source` as groupby category + `fillna('unpriced')` | Safe (new category in breakdown) |
| E_05.gap_by_pricing_source | Uses `source` as groupby category | Safe (new category in breakdown) |
| **E_06.trace_asset_pricing:87** | `source.isin(['yahoo_finance', 'transaction_observed'])` — **excludes capped** | Acceptable per TO ("treat as not T1"). Diagnostic slightly under-counts T1 by the capped count. |
| **E_14.audit_existing_mappings:80** | `source == 'transaction_observed'` — **excludes capped** | Same as above. Diagnostic. |

No consumer raises on unexpected `source` values. All pass the TO's bar ("treat as not T1 or pass-through").

Saved output: `/tmp/phase1_blast.txt` (36 lines).

### Phase 3 (after writing) — re-run

`comp-build` + `comp-trace canonical_prices` → diff against Phase 1 → **identical, zero drift**. No new upstream/downstream edges introduced by the source-tag change.

## Artifacts

| Artifact | Path / reference |
|---|---|
| Modified script | `data/black_diamond/scripts/silver/build_canonical_prices_v2.py` |
| Diff harness | `data/analysis/v2_cap_tag_diff.py` |
| Session log | this file |
| S3 upload | `s3://opal-data-bd/code/silver/build_canonical_prices_v2.py` |
| Commit SHA | `9b4f7a77` on CLOUD |
| S3 etag | `d51a8260513a46d8ab94bde4e49bea69` (matches local md5) |

## Do-not verification

- [x] 50x threshold unchanged (grep `50 *` unchanged).
- [x] Cap replacement value unchanged (still `asset_med`).
- [x] Within-day collapse at line 183-184 untouched.
- [x] No gold-runner trigger, no Lambda invocation.
- [x] Upload goes to `code/silver/`, not `code/gold/`.
- [x] Diff-before-ship run and price values identical.

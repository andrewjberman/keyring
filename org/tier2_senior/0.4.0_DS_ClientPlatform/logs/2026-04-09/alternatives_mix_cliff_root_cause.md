# Session Log — Alternatives Mix Cliff Root Cause Investigation
**Date:** 2026-04-09
**Agent:** 0.4.0_DS (session with Andrew)
**Scope:** Portal ADVI page — Asset Overview header chart showing alternatives drop from ~$66M to ~$10M in Q1 2026

---

## 1. The Observation

The ADVI portal page has two places showing alternatives AUM:

| Widget | Value | Source |
|---|---|---|
| Asset Overview header chart (time series) | ~$10M in Q1 2026 | `firm_mix_views.json` via C_06 → D_03 |
| Firm Overview donut (snapshot) | ~$73M current | `mix_summary.json` via D_03 → firm_composition |

The discrepancy was flagged by Andrew: the header chart showed alternatives falling from ~$66M in Q4 2025 to ~$10M entering Q1 2026. The donut simultaneously showed $73M. The question: which is right, and why are they different?

**The donut is correct. The header chart is wrong.**

---

## 2. Investigation Phase 1 — Classifier Divergence (Red Herring)

Initial hypothesis: two different classifiers were being used.

**Finding:** The two widgets DO use different data paths:
- Header chart: `mix_daily_summary.json` (C_06) → `firm_mix_views.json` (D_03) → `timeseries_overview.json` (D_04)
- Donut: `firm_composition.json` (D_03) → `mix_summary.json` (D_04)

**Ruling it out:** Both use `ETFClassifier` from `lib/etf_classifier.py`. Running the classifier locally against canonical_holdings returned `alternatives` for all 301 structured product rows ($67.06M). Classifier was not the issue.

Key securities in question (from Andrew's securities list):
- 6 Year Shield 25 S&P 500 Index — 29.0% ($21.3M)
- 6 Year Shield 15 S&P 500 Index — 19.2% ($14.1M)
- AQR TA DELPHI PLUS FUND LLC — 16.6% ($12.2M)
- 1 Year Shield 10 S&P 500 Index — 5.1% ($3.75M)
- 6 Year S&P 500 Cap 20% Protect — 4.6% ($3.37M)
- 3 Year Shield 15 S&P 500 Index, 3 Year Shield 10, S&P 500 6 Year -20% Buffer, 6 Year Shield 10

All Allianz Shield annuities and structured buffered products. All in `bd-securities` DynamoDB table with `asset_class = 'alternatives'`, `sub_asset_class = 'Structured Notes'`.

---

## 3. Investigation Phase 2 — Data Inspection

**Downloaded and compared three snapshots:**

| Date | holdings_lots (raw) | canonical_holdings | mix_daily_summary firm |
|---|---|---|---|
| 2025-09-30 | N/A | $52.75M SP (295 rows) | $58.9M alternatives |
| 2025-12-31 | N/A | $54.12M SP (301 rows) | $60.1M alternatives |
| 2026-03-31 | $71.86M (all is_open=True) | $67.29M SP (304 rows) | $10.2M alternatives |

**Key finding from canonical_holdings:** Structured products ARE present and correctly sized in all dates. They are NOT sold, closed, or filtered. The `is_open` flag is irrelevant — canonical_holdings is a different source from holdings_lots.

**Quarterly mix from `firm_mix_views` quarterly series:**

| Quarter | Alternatives |
|---|---|
| 2025-Q3 | $65.0M |
| 2025-Q4 | $66.9M |
| 2026-Q1 | **$10.6M** |
| 2026-Q2 | $9.7M |

The cliff is sharp, not gradual.

---

## 4. Investigation Phase 3 — Pinpointing the Cliff Date

Downloaded `mix_daily_summary.json` (C_06's intermediate output, the authoritative daily source). Inspected firm-level alternatives by date:

```
2026-02-03: $65.3M
2026-02-04: $8.3M   ← CLIFF
```

A $57M single-day drop. Both Feb 3 and Feb 4 canonical_holdings files have **identical** structured product data: 301 rows, $61.88M, 119 accounts, same sources (bd: 291, reconciled: 10). The data did not change. The pipeline processed the same data differently.

**AP gate ruled out:** All 109 insurance accounts (holding Shield/Buffer products) have `ap_last_seen = 2026-04-02`, so they pass the gate for every date. Ghost accounts ruled out: 4 ghosts, zero overlap with insurance.

---

## 5. Investigation Phase 4 — Attempting Local Reproduction

Wrote a simulation of C_06's `process_date` logic locally:
- Loaded canonical_holdings Feb 4
- Applied AP gate, relationship mapping, market_value filter
- Classified using ETFClassifier
- Aggregated per-relationship, then to firm

**My simulation produced:** equity $1144.91M, fi $331.55M, **alternatives $66.26M**

**Stored in mix_daily_summary for Feb 4:** equity $1034.58M, fi $477.68M, **alternatives $8.33M**

Running the same test for Feb 3:
- My simulation: alternatives **$68.88M**
- Stored: alternatives **$65.34M** (close — within noise)

So:
- For Feb 3: local ≈ stored ✓
- For Feb 4: local ≠ stored (off by $57M)

My simulation must be doing something different from what C_06 actually does on EC2.

**Confirmed identical code:** EC2 `C_06.client_mix_timeseries.py` = 38,083 bytes, identical to repo. EC2 `lib/etf_classifier.py` = 5,811 bytes, identical. `insurance_accounts.json`, `s3_layout.py`, `lib/config.py` — all identical. Same S3 bucket (`opal-data-bd`). Same DynamoDB table (`bd-securities`).

---

## 6. Investigation Phase 5 — Finding the Bug

Wrote a test that ran C_06's **actual** `classify_series` function (not my simulation's merge variant) against the Feb 4 canonical_holdings:

```
After mv filter: 83,077 rows, index range [0, 83876]
Is index contiguous? False
Index gaps: 800

classify_series output index range: [0, 83076]
classify_series output length: 83,077

After assignment: NaN asset_class: 797 out of 83,077 (0.96%)

Structured products: 294 rows
  NaN cls:          0
  Alternatives cls: 1   ← should be 294
  Other cls:        {equity: 184, fixed_income: 109, alternatives: 1}
  Alt market_value: $0.10M  ← should be $61.88M
  Misclassified mv: $61.08M
```

**Root cause identified: pandas index alignment bug in `classify_series`.**

---

## 7. The Bug — Detailed Explanation

### classify_series code (C_06.client_mix_timeseries.py:195-217)

```python
def classify_series(ticker_series, name_series):
    classifier = ETFClassifier.instance()
    pairs = pd.DataFrame({
        'ticker': ticker_series.fillna('').astype(str),
        'asset_name': name_series.fillna('').astype(str),
    })
    unique_pairs = pairs.drop_duplicates().copy()
    unique_pairs['asset_class'] = 'equity'
    for idx, row in unique_pairs.iterrows():
        cls = classifier.classify(row['ticker'], row['asset_name'])
        if cls:
            unique_pairs.at[idx, 'asset_class'] = cls
    return pairs.merge(unique_pairs, on=['ticker', 'asset_name'], how='left')['asset_class']
```

### The problem

`pairs` inherits the **non-contiguous index** of `ticker_series` (which comes from `pos['ticker']`). After the upstream filtering steps:

```python
pos = pos[standard_ok | insurance_ok]       # AP gate — may drop rows
pos = pos.dropna(subset=['relationship_id']) # drops accounts not in acct_rel
pos = pos.dropna(subset=['market_value'])    # drops NaN market_values
pos = pos[pos['market_value'] > 0]          # drops zero-value rows
```

`pos` has non-contiguous index. Feb 4 had 800 gaps (83,877 rows in → 83,077 after filtering). `pairs` inherits that non-contiguous index (e.g., [0, 1, 2, ..., 16, 18, 19, ...]).

The `.merge()` call **always resets the output index to `RangeIndex(0..83076)`** regardless of the input index. The merge result is correct row-by-row, but its label is 0..N-1.

When the return value is assigned back:
```python
pos['asset_class'] = classify_series(pos['ticker'], pos['asset_name'])
```

Pandas performs **label-based alignment**. `pos[k]` is assigned `result[k]` — where `result[k]` is the k-th element by LABEL, which corresponds to the **positional row k** in the merge result (i.e., the classification for whatever row happened to be at position k, which is NOT necessarily the row that originally had label k).

For a pos with gaps, rows after the first gap are systematically shifted. A row at label 18 gets the classification intended for label 17 (off by one after the gap at label 17). After 800 gaps, the shift accumulates to as much as 800 positions by the end of the file. The 797 rows with label > 83,076 get NaN (the result only has 83,077 elements labeled 0..83,076).

### Why structured products are disproportionately affected

Shield and Buffer products are in accounts with IDs starting with `z08...` — late alphabetically. The canonical_holdings parquet is ordered by source data ingestion order, which tends to put these accounts near the **end** of the file. With 800 gaps accumulated before the end, the final rows of pos have labels significantly higher than their positional offset in the merge result. Shield product rows at, e.g., label 80,000 get the classification for positional row 80,000, which might correspond to an equity holding at original label 80,800 (due to 800 accumulated gaps). So Shield rows get equity or fixed_income classifications, and the equity/fi rows that were "ahead" in position get the Shield classifications (which are subsequently skipped because those positions exist in accounts with contiguous index).

### Why my simulation was correct

My simulation bypassed the bug:
```python
df_pass = df_pass.merge(unique_pairs, on=['ticker', 'asset_name_str'], how='left')
```

This merges directly into `df_pass`, replacing it with a fresh DataFrame that has `RangeIndex(0..N-1)`. All subsequent operations operate on the clean index. The bug never fires.

---

## 8. Why the Cliff Is at Feb 4, 2026

### Confirmed: canonical_holdings pipeline switch

`gold/canonical/holdings/` is the new pipeline (`B_00.canonical_holdings.py`), introduced around early February 2026 as part of the canonical stack refactor. The git log for `B_00` and `C_06` confirms the switch from reading old `positions_cube` / silver sources to reading canonical_holdings around this period. Before the switch, C_06 either had no filtering that created index gaps, or a `reset_index(drop=True)` was present in the code path. The canonical_holdings source produces non-contiguous indices after the `dropna(relationship_id)` + `mv > 0` filters, triggering the bug from Feb 4 onward.

### What explains the preserved pre-cliff values — confirmed facts vs inference

**Confirmed:**
- `gold/client_timeseries/_watermark.json` contains `data_as_of: 2026-04-02` as of this investigation.
- In `gold_dispatch.sh` (repo and deployed are identical), C_06 is invoked **without** `--incremental` in the `rebuild` and `full` chains. The dispatcher only forwards `--incremental` to C_06 when it was itself invoked with `--incremental`.
- In C_06, watermark gating is only active when `incremental=True`. Full-mode processes all keys from scratch.
- **Deployed C_06 is stale relative to repo.** Repo already contains the `result.index = pairs.index` fix (committed this session). Deployed `code/gold/C_06.client_mix_timeseries.py` does not — it still returns the raw merge result with `RangeIndex(0..N-1)`. This was validated by Codex independently against both the repo and the deployed S3 artifact.

**Unconfirmed operational inference (softened):**
The persistence of correct pre-Feb-4 values in `mix_daily_summary.json` alongside wrong post-Feb-4 values is not fully explained by the runner code. If "full rebuilds" were running end-to-end through C_06, ALL dates would be overwritten with the buggy results (pre-cliff dates would also show ~$0.5M alternatives, not $65M). Since they don't, one of the following must be true — but no EC2 logs from recent runs are available to confirm which:

1. The "full rebuild" invocations did not actually execute C_06 (e.g., it was skipped, timed out, or the run was a `downstream`/`canonical` chain that doesn't include C_06).
2. C_06 ran but encountered an error before writing `mix_daily_summary.json`.
3. There is a separate incremental path being used that isn't the `run_gold_layer.sh full` command.

**Bottom line for operations:** Do not rely on the watermark/runner theory to explain the data shape. The actionable fact is: deployed C_06 is buggy, repo has the fix, and a full rebuild from scratch is needed to repopulate all dates correctly.

---

## 9. The Fix

> **Status:** Fix is in the repo. Deployed S3 artifact (`code/gold/C_06.client_mix_timeseries.py`) does not yet contain it. AE must deploy before the fix takes effect on EC2.

**File:** `data/black_diamond/scripts/gold/C_06.client_mix_timeseries.py`
**Line:** 217 (end of `classify_series`)

**Before:**
```python
    return pairs.merge(unique_pairs, on=['ticker', 'asset_name'], how='left')['asset_class']
```

**After:**
```python
    # merge() resets the index to RangeIndex(0..N-1). Restore the original index
    # so that assignment to a filtered DataFrame (pos['asset_class'] = ...) does
    # positional alignment rather than label-based alignment, which would
    # scramble classifications whenever pos has a non-contiguous index.
    result = pairs.merge(unique_pairs, on=['ticker', 'asset_name'], how='left')['asset_class']
    result.index = pairs.index
    return result
```

**Verification (with fix applied):**

| Date | SP rows correct | Alt market_value | NaN rows |
|---|---|---|---|
| 2026-02-03 | 294/294 | $61.19M | 0 |
| 2026-02-04 | 294/294 | $61.19M | 0 |
| 2026-03-31 | 294/294 | $66.36M | 0 |

The fix restores the original (non-contiguous) index to the merge result. When pandas then assigns `pos['asset_class'] = result`, label-based alignment is correct: `pos[k] = result[k]` maps to the classification for the row that originally had label k.

---

## 10. What Needs to Happen Next

### Immediate (AE deploys)

1. Deploy the fixed `C_06.client_mix_timeseries.py` to EC2 via `deploy-to-ec2.sh`
2. Reset the watermark to force a full reprocess of all canonical_holdings dates:
   - Delete or zero out `gold/client_timeseries/_watermark.json`
   - OR set `data_as_of` to an early date (e.g., `2020-01-01`)
3. Run `gold_dispatch.sh --chain rebuild` (full chain, no `--incremental` flag)
   - This recomputes ALL dates in canonical_holdings with the fixed classifier
   - Overwrites `mix_daily_summary.json` with correct values for all dates
4. Run D_03 to republish `firm_mix_views.json` from the corrected summary
5. Verify: header chart Q1 2026 should show ~$63-67M alternatives (matching the donut)

### Longer term

- Add a `pos = pos.reset_index(drop=True)` call in `process_date` immediately before the `classify_series` call, making it robust against any upstream filtering pattern
- Alternatively, convert the assignment to `.values`: `pos['asset_class'] = classify_series(...).values` — this bypasses index alignment entirely by assigning positionally
- Add a validation check in C_06 that asserts `pos['asset_class'].isna().sum() == 0` after classification, logging any NaN as an ERROR rather than silently scrambling the result
- The `D_00.portal_aggregates.py` header chart `aua_mix` is a separate (smaller) issue: its `_classify_asset()` keyword matcher correctly ignores Shield/Buffer products (since they don't match alternatives keywords). That produces the wrong asset_class labels in D_00's own timeseries_chart but is a separate concern from the C_06 cliff issue. Fix is to replace `_classify_asset()` with `ETFClassifier` (same as D_03), but that is a lower-priority cleanup since the header chart's asset_class breakdown (aua_mix) is secondary to the main mix timeseries.

---

## 11. Data Impact Summary

| Affected artifact | Scope | Impact |
|---|---|---|
| `gold/views/mix_daily_summary.json` | All firm daily entries from ~2026-02-04 onward | Alternatives systematically ~$57M too low; fixed_income ~$130M too high; equity ~$110M too low |
| `gold/artifacts/firm_mix_views.json` | Quarterly/monthly/annual period views | Q1 2026 alternatives shows $10.6M instead of ~$65M |
| `gold/artifacts/firm_mix_views_daily.json` | Daily firm totals | Same corruption as mix_daily_summary |
| `platinum/firm/timeseries_overview.json` | What the portal header chart reads | Propagated from firm_mix_views |
| Per-relationship `gold/client_timeseries/*.json` | All relationship-level mix JSONs for post-Feb-4 dates | Also corrupted — same classify_series bug applies to advisor-level accumulation |

Pre-Feb-4 data is correct (preserved from pre-canonical_holdings C_06 era).

---

## 12. Summary

**Confirmed root cause:** `classify_series` in `C_06.client_mix_timeseries.py` returns a Series with a reset `RangeIndex` from the `.merge()` call, but pandas label-aligns it on assignment to `pos['asset_class']` whose index is non-contiguous after upstream row filtering — causing Shield/Buffer/Delphi structured product rows to receive the asset class of adjacent rows, suppressing ~$57M of alternatives per day since the canonical_holdings pipeline went live in early February 2026.

**Confirmed fix:** `result.index = pairs.index` before returning from `classify_series`. Already in repo; not yet deployed.

**Unconfirmed:** The exact operational reason why pre-cliff dates still show correct values while post-cliff dates are wrong. The runner code does not support a watermark-gating explanation for full-rebuild runs. Root cause of the operational gap is unknown without EC2 execution logs. Treat as a separate question from the bug itself.

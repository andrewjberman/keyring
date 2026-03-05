# Session Log: Yang V2 Phase 2 DS Data Batch

- **Agent**: 0.4.0_DS_ClientPlatform
- **Date**: 2026-03-04
- **Task Order**: ADVI-Y-phase2-ds-data-batch (issued by 2.0.0_SA_COO)
- **Streams**: Y2, Y3, Y5, Y6b, Y6c, Y6d, Y7, Y9, Y10, Y11, Y13
- **Status**: ALL 11 STREAMS CODE-COMPLETE. NOTHING COMMITTED.

## Where I Left Off

### Git State
- **Branch**: `CLOUD` (ahead of origin by 2 commits -- those are prior work, not mine)
- **Last commit on branch**: `5fc407c5` (COO daily log, not mine)
- **All my changes are unstaged.** Zero commits made by this session.

### Unstaged Modified Files (my work only)

| # | File | Lines Changed | Streams |
|---|------|--------------|---------|
| 1 | `data/black_diamond/scripts/gold/09_generate_partner_analytics.py` | +121 | Y7, Y6c, Y6b, Y6d |
| 2 | `data/black_diamond/scripts/gold/10_generate_advisor_rolling_flows.py` | +29 | Y13 |
| 3 | `infra/aws/lambda/bd-pipeline/bd-portal-publisher/lambda_function.py` | +276 | Y3, Y5, Y9 |
| 4 | `org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/data_contract.xml` | +110 | all streams |

Note: `git diff --stat` also shows changes in `response.json`, `portal` submodule,
`yang-generate-positioning/lambda_function.py`, and an RD task order file -- those are NOT
mine. They were dirty before this session started. Do NOT stage them in my commits.

### Untracked Files (my work only)

| File | Purpose |
|------|---------|
| `org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-03-04/yang_v2_phase2_ds_data_batch.md` | This session log |
| `docs/architecture/ADVISOR_INTELLIGENCE_YANG_FEEDBACK_V2.md` | V2 PRD (was already untracked before session, authored by COO) |

### What Still Needs To Happen

1. **Commits (4 batches).** Per the task order's `<delivery_batching>`, commits are batched by priority group:

   **Batch 1 commit** -- script 09 bug fixes (Y7 + Y6c):
   ```
   git add data/black_diamond/scripts/gold/09_generate_partner_analytics.py
   git commit --author="0.4.0_DS_ClientPlatform <0.4.0_DS_ClientPlatform@opal.agent>" \
     -m "0.4.0_DS: Y7 single-account binning fix + Y6c outflow quartile inversion fix (script 09)"
   ```
   Problem: script 09 also contains Y6b+Y6d changes. All 4 streams (Y7, Y6c, Y6b, Y6d) are in the
   same file. There is no way to split Y7+Y6c from Y6b+Y6d without partial staging (`git add -p`).
   **Decision needed**: commit script 09 once with all 4 streams, or use partial staging.
   Recommendation: single commit for script 09 covering Y7+Y6c+Y6b+Y6d.

   **Batch 2** -- investigations (Y2 + Y11):
   No code changes. Session log documents findings. No commit needed for code.

   **Batch 3 commit** -- publisher Lambda extensions (Y3 + Y5 + Y9):
   ```
   git add infra/aws/lambda/bd-pipeline/bd-portal-publisher/lambda_function.py
   git commit --author="0.4.0_DS_ClientPlatform <0.4.0_DS_ClientPlatform@opal.agent>" \
     -m "0.4.0_DS: Y3 asset class AUA mix + Y5 growth decomposition + Y9 NNA drill levels (publisher Lambda)"
   ```

   **Batch 4 commit** -- script 10 extension (Y13):
   ```
   git add data/black_diamond/scripts/gold/10_generate_advisor_rolling_flows.py
   git commit --author="0.4.0_DS_ClientPlatform <0.4.0_DS_ClientPlatform@opal.agent>" \
     -m "0.4.0_DS: Y13 monthly stacked_bar granularity (script 10)"
   ```

   **Org commit** -- data_contract + session log:
   ```
   git add org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/data_contract.xml
   git add org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-03-04/yang_v2_phase2_ds_data_batch.md
   git commit --author="0.4.0_DS_ClientPlatform <0.4.0_DS_ClientPlatform@opal.agent>" \
     -m "0.4.0_DS: data_contract.xml Yang V2 stream findings + session log"
   ```

2. **DT deploy notifications.** After commits, notify DT:
   - "Ready for bd-pipeline deploy: script 09, script 10, publisher Lambda (Yang V2 Phase 2 DS batch)"
   - DT owns `terraform apply` for publisher Lambda. DT owns EC2 deploy for scripts 09/10.

3. **COO notification.** Y11 result: no Advisor field in BD data. Y13 scope adjusted (no `advisors` key).

4. **Push.** `git push` after all commits.

5. **DT deploy brief.** Write `docs/briefs/devops-brief-yang-v2-phase2-ds-batch.md` with deploy instructions.
   Not yet written.

## Syntax Verification

All 3 modified Python files pass `ast.parse()`:
```
OK: 09_generate_partner_analytics.py
OK: 10_generate_advisor_rolling_flows.py
OK: lambda_function.py
```

## Stream-by-Stream Detail

### Priority 1 -- Bug Fixes

**Y7: ADV-AUA single-account binning** -- CODE FIX
- File: `data/black_diamond/scripts/gold/09_generate_partner_analytics.py`
- Function: `calculate_distribution_stats()` (approx line 287)
- Root cause: `np.logspace(log10(X), log10(X), N)` produces N identical bin edges when min_val == max_val
  (single-account relationship with one AUA value). All bin edges collapse, histogram places 0 accounts
  in every bucket, x-ticks show "5m-5m".
- Fix: Guard added before logspace call:
  ```python
  if max_val <= min_val:
      max_val = min_val * 2
  ```
  Ensures at least one non-degenerate bin range.

**Y10: QTD/YTD math** -- NO CODE CHANGE
- Investigated all 3 computation paths:
  1. Script 10 `compute_stacked_bar()` -- `_nna_for_period()` at lines ~995-1004
  2. Script 10 `compute_summary()` -- `nna_ytd`/`nna_qtd` at lines ~1007-1010
  3. Publisher Lambda `build_header_metrics()` -- `_nna_for_period()` helper
- For Q1 2026: QTD start = Jan 1, YTD start = Jan 1. Both produce identical period boundaries.
- Conclusion: code is correct. Reported discrepancy is likely stale deployed data or frontend display issue.

**Y6c: Outflows quartile inversion** -- CODE FIX
- File: `data/black_diamond/scripts/gold/09_generate_partner_analytics.py`
- Function: `calculate_nna_distribution_stats()` (approx line 366)
- Root cause: Percentiles computed on signed NNA values. Most negative outflows land at P10 (bottom).
  Yang expected largest outflows at P90+ (top).
- Fix: Added split percentile computation:
  ```python
  inflows  = vals[vals > 0]
  outflows = vals[vals < 0].abs()  # positive magnitudes for ranking
  ```
  New return keys: `inflow_percentiles`, `outflow_percentiles` (both with p10/p25/p50/p75/p90),
  `inflow_count`, `outflow_count`.
- Applied at all grain levels via the shared `calculate_nna_distribution_stats()` function
  (GEO-state, GEO-city, ADV-architect, ADV-relationship).

### Priority 2 -- Investigations

**Y2: NMNC/NMEC classification audit** -- NO CODE CHANGE
- Found two implementations:
  1. Script 09 CLA view (`build_cla_view()`): period-bookended. `first_seen_date > start_ts` = NMNC.
     Correct per Yang PRD section 1.2.
  2. Publisher Lambda aua view: trailing-12-month. `(row_date - first_seen_date).days / 30.44 <= 12` = NMNC.
     Appropriate for daily time series (vintage classification relative to each day).
- Both are fit for purpose. Different contexts require different classification semantics.

**Y11: Advisor identity field investigation** -- NO CODE CHANGE
- Searched exhaustively:
  - `01_build_advisor_assignments_history.py` line 39: `ADVISOR_FIELDS = ['architect', 'implementor', 'local_ops']`
  - `00_build_accounts_dimension.py`: only `architect`, `implementor`, `local_ops` in `TXN_ACCOUNT_COLS`
  - `04_build_client_dimension.py`: `primary_architect`, `primary_implementor` -- no `advisor_name`/`advisor_id`
  - BD raw transaction/allocation schemas: no "Advisor" field
- Conclusion: No distinct "Advisor" identity field exists in Black Diamond data. Only 3 advisor-type roles.
- Impact on Y13: No `advisors` key added to stacked_bar. Monthly granularity uses architect column only.

### Priority 3 -- Data Extensions

**Y6b: City-level NNA distribution drill** -- CODE EXTENSION
- File: `data/black_diamond/scripts/gold/09_generate_partner_analytics.py`
- New function: `_build_rel_city_lookup(acct_dim)` -- maps relationship_id to modal city
  (uses `client_city` column from accounts_dimension, picks mode, filters nulls via `MODAL_NULLS`).
- Modified: `build_nna_geo_view()` -- added `rel_city_lookup: pd.Series = None` parameter.
  When provided, computes per-state city-level NNA distributions.
- New output key: `drill` in the geo NNA return dict.
  Structure: `drill.{state_key}.by_city.{city_key}` = NNA distribution (same shape as `calculate_nna_distribution_stats()`).
- Modified caller: `generate_header_metrics()` -- builds `rel_city_lookup` and passes to `build_nna_geo_view()`.

**Y6d: Relationship-level NNA distribution drill** -- CODE EXTENSION
- File: `data/black_diamond/scripts/gold/09_generate_partner_analytics.py`
- Modified: `build_nna_adv_view()` -- added `client_dim: pd.DataFrame = None` parameter.
  When provided, computes per-architect relationship-level NNA distributions.
- New output key: `drill` in the adv NNA return dict.
  Structure: `drill.{architect_key}.distribution` = NNA distribution, plus `relationship_count`.
- Modified caller: `generate_header_metrics()` -- passes `client_dim=client_dim` to `build_nna_adv_view()`.

**Y5: Growth decomposition** -- CODE EXTENSION
- File: `infra/aws/lambda/bd-pipeline/bd-portal-publisher/lambda_function.py`
- Location: inside `build_timeseries_chart()`, after existing NNA computation block.
- Aggregates `client_performance.parquet` by year_month. Per month:
  - `aua_start` = first day's total_aua, `aua_end` = last day's total_aua
  - `nna_net` = last day's nna - first day's nna (cumulative diff within month)
  - `market` = (aua_end - aua_start) - nna_net
  - `total` = market + nna_net
- Output key: `growth_decomposition` in timeseries_chart.json result dict.

**Y9: NNA at drill levels** -- CODE EXTENSION
- File: `infra/aws/lambda/bd-pipeline/bd-portal-publisher/lambda_function.py`
- Location: inside `build_timeseries_chart()`, after growth_decomposition block.
- Three new views:
  1. `nna_geo`: per-state daily cumulative NNA/inflows/outflows. Flat keys: `{state}`, `{state}_inflow`, `{state}_outflow`.
  2. `nna_adv`: per-architect daily cumulative NNA/inflows/outflows. Same flat key pattern.
  3. `nna_geo_drill`: per-city NNA within top states. Dict keyed by state name, each containing
     `categories` + `data` arrays with city-level flat keys.
- All three added to result dict (nna_geo_drill conditionally, only when geo_city data exists).

**Y3: Asset class AUA breakdown** -- CODE EXTENSION
- File: `infra/aws/lambda/bd-pipeline/bd-portal-publisher/lambda_function.py`
- New constants (after existing config block, approx line 69):
  - `_CASH_PATTERNS`, `_FIXED_INCOME_PATTERNS`, `_REAL_ESTATE_PATTERNS`, `_ALTERNATIVES_PATTERNS`,
    `_INTL_EQUITY_PATTERNS`, `_EQUITY_PATTERNS` -- tuples of lowercase substrings.
  - `ASSET_CLASS_LABELS` -- dict mapping 6 keys to display labels.
  - Note: "Real Estate" is split out from "Alternatives" (unlike the archived `utils/asset_classifier.py`
    which lumps REITs into alternatives). The 6 categories match the Y3 PRD spec exactly.
- New function: `_classify_asset(name)` -- returns one of 6 asset class keys based on name patterns.
- New function: `_build_aua_mix(today)`:
  1. Lists `gold/holdings_lots/` S3 keys via paginator.
  2. Filters to daily snapshots (YYYY-MM-DD.parquet, skips backfill files).
  3. Picks last available snapshot per month.
  4. Loads each snapshot (columns: `asset_name`, `market_value`, `is_open`), filters to open lots.
  5. Classifies each lot via `_classify_asset()`.
  6. Aggregates `market_value` by asset class.
  7. Returns list of `{period: "YYYY-MM", segments: [{label, value}]}`.
- Called from `build_timeseries_chart()` just before "Assemble response" block.
- Output key: `aua_mix` in timeseries_chart.json result dict (conditional -- only when data exists).

**Y13: Monthly stacked_bar granularity** -- CODE EXTENSION
- File: `data/black_diamond/scripts/gold/10_generate_advisor_rolling_flows.py`
- Location: inside `compute_stacked_bar()`, after existing period loop.
- Computes per-month NNA breakdown by advisor (same pattern as existing period loop but at monthly grain).
- New output key: `result['monthly']` = dict of `"YYYY-MM" -> [AdvisorBarEntry]`.
  Each entry: `{advisor_name, advisor_id, inflows, outflows, nna_net}`.
- No `advisors` key added (Y11 confirmed no distinct Advisor field).

## Data Contract Updates

Updated `org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/data_contract.xml`:
- **source_note**: added Yang V2 Phase 2 summary line.
- **timeseries_chart.json response_shape**: added `<key>` entries for `growth_decomposition`, `nna_geo`,
  `nna_adv`, `nna_geo_drill`, `aua_mix`.
- **yang_v2_stream_findings section**: new XML block with `<finding>` entries for all 11 streams,
  documenting type (bug_fix / investigation / data_extension), file, and root cause/outcome.

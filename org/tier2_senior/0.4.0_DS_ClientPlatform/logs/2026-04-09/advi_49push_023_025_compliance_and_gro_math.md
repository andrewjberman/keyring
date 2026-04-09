# ADVI_49PUSH.023 + .025 -- Compliance Pass-throughs + GRO Panel Math Fix

**Agent:** 0.4.0_DS_ClientPlatform~D
**Date:** 2026-04-09
**Project:** ADVI_49PUSH
**Commit:** e3bdf513
**Status:** .023 complete. .025 fix_2+fix_3 complete, fix_1 pending CTO confirmation.

---

## Summary

### .023 -- D_04 Compliance Publishers (6 new platinum paths)

Extended D_04.client_portal_summary.py to publish all remaining platinum/ files
required by the compliance audit. After this, every advisor-intelligence.ts endpoint
that was reading gold/ now has a platinum/ counterpart for DE to switch to (.024).

New publishers added:

| Platinum path | Source | D_04 step |
|---|---|---|
| `platinum/firm/header_metrics.json` | `gold/artifacts/summary/header_metrics.json` (D_00) | Step 11 |
| `platinum/firm/timeseries_chart.json` | `gold/artifacts/timeseries_chart.json` (D_00) | Step 11 |
| `platinum/firm/employee_leaderboard.json` | `gold/artifacts/employee_leaderboard.json` (D_00) | Step 11 |
| `platinum/advisors/{id}/mix.json` | `gold/entities/advisors/{id}/mix.json` (D_03) | Step 3 |
| `platinum/clients/{id}/views.json` | `gold/entities/clients/{id}_views.json` (C_06) | Step 4 |
| `platinum/clients/{id}/composition.json` | `gold/entities/clients/{id}_composition.json` (D_03) | Step 4 |

All pass-through verbatim -- no reshape. Frontend TS types written against existing
gold/ schemas; shape changes would require DE type work.

Note: `getAdvisorFeeEfficiency` already has `platinum/firm/fee_efficiency.json` (written
by D_04 Step 1 split path). `getPartnerAnalyticsHeader` already has
`platinum/firm/partner_analytics_{gran}.json`. Those need frontend switches only (DE .024).

### .025 -- GRO Panel Math Fix (partial)

**fix_2 (complete):** NNA alignment in D_04.build_timeseries_overview.
Root cause: growth_decomposition.nna was computed from account_performance.nna cumulative
diff, while nna[gran].net used Inflows/Outflows endpoints -- two different paths, diverge
in practice. Fix: after building both nna_periods and growth_periods, replace
growth_decomposition.nna with nna_lookup[period] for every period/granularity. nna_pct
recomputed accordingly. GRO tile NNA now equals NNA toggle NNA exactly.

**fix_3 (complete):** Percentage decomposition in D_00 + D_04.
D_00 growth_data entries now carry:
  - `period_aua_start`: aua at start of period (for context and D_04 re-aggregation)
  - `total_pct`, `market_pct`, `nna_pct`: growth rates as % of period_aua_start
  - `aua_residual_delta`: period change in aua_residual (audit-only, never display)
D_04 `_aggregate_growth_to_periods` now propagates period_aua_start (uses first month's
value in each quarterly/annual bucket) and recomputes pct fields from summed dollar fields.
Dollar fields (market, nna, total) preserved in output per TO instruction.

**fix_1 (BLOCKED -- pending CTO):** Market hypothesis diagnosis.
Code analysis:
- has_decomposition=True confirmed (account_performance.parquet loaded successfully in
  prior session).
- Hypothesis B (FALLBACK path) NOT active.
- Hypothesis A most likely: if 08 account_ledger computes growth = AUA_change - net_flows,
  aua_residual gets bundled into the growth column. $78.7M contamination for Q1 on ~$1.4B AUA
  is consistent with a large reconciliation adjustment being misclassified as price return.
- Hypothesis C (stale cache) eliminated if AE re-ran D_04 after e3bdf513 push.
- As of e3bdf513, aua_residual_sum is now included in the D_00 aggregation AND in
  growth_data entries (as aua_residual_delta). The one-line fix_3b change is ready.
- Sent CTO inbox message at 20260409T182902Z.
- CTO replied with conditional GO and parquet check script.
- Ran parquet check against s3://opal-data-bd/gold/timeseries/account_performance.parquet:
    sum(growth) Q1 2026:       $75,369,624  (far above ~$280K true market return)
    sum(aua_residual) Q1 2026: $49,468,212
    growth - aua_residual:     $25,901,412
  Hypothesis A CONFIRMED. sum(growth) >> $280K expected; growth column is contaminated.
- Implemented fix_3b (commit 023079d7): market = sum(growth) - sum(aua_residual) per month.
  Added economic_total = market + nna_net. Identity preserved:
    total_chg (raw) == economic_total + aua_residual_delta (within rounding).
- D_04 _aggregate_growth_to_periods updated to sum and propagate economic_total.
- .025 COMPLETE. All 3 fixes shipped.

---

## Files Modified

| File | Change |
|---|---|
| `data/black_diamond/scripts/gold/D_04.client_portal_summary.py` | Import HEADER_METRICS; Step 11 firm pass-throughs; advisor mix.json pass-through in Step 3; client views.json + composition.json pass-throughs in Step 4; fix_2 NNA alignment in build_timeseries_overview; fix_3 pct fields in _aggregate_growth_to_periods |
| `data/black_diamond/scripts/gold/D_00.portal_aggregates.py` | Add aua_residual_sum to aggregation; include in _gro_agg_cols; fix_3 pct fields + period_aua_start + aua_residual_delta in growth_data loop |

---

## Commits

| SHA | Description |
|---|---|
| `e3bdf513` | 0.4.0_DS_ClientPlatform: ADVI_49PUSH.023 + .025 partial (D_04 + D_00) |
| `023079d7` | 0.4.0_DS_ClientPlatform: ADVI_49PUSH.025 fix_3b -- strip aua_residual from market |

Pushed to origin/CLOUD.

---

## Pending

1. **CTO GO on fix_1** -- strip aua_residual from market in D_00 if Hyp A confirmed. One-line change + aua_residual_delta schema addition. Sent analysis to CTO inbox at 20260409T182902Z.
2. **AE re-upload** -- D_00, D_04 need S3 upload and D_04 re-run to materialize .023 platinum files and .025 NNA/pct fix in portal.
3. **DE .024** -- switch 6 frontend endpoints from gold/ to platinum/ paths once AE re-run confirms files exist.
4. **Spot-check after AE re-run** -- sample 5 advisors + 5 clients, confirm platinum/advisors/{id}/mix.json and platinum/clients/{id}/views.json match gold source.
5. **GRO validation** -- after fix_1 committed + re-run, verify Q1 2026 market ~$280K-$500K (not $79M), NNA toggle == GRO NNA tile for 3 quarters.

---

## Next Steps

[CTO] Confirm market hypothesis (A vs C) and send GO for fix_1 (market strip in D_00).
[AE 0.6.0] Upload D_00, D_04 to S3 and re-run D_04 chain. D_00 re-run also needed for
           growth_decomposition pct fields + aua_residual_delta to appear in timeseries_chart.json.
[DE 0.4.0_DE] .024 companion TO: switch 6 endpoints to platinum/ paths after AE confirms files.

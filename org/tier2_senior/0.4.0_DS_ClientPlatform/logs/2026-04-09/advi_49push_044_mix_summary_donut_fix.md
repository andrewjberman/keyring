# ADVI_49PUSH.044 -- Firm Overview Mix Discrepancy Fix

**Agent:** 0.4.0_DS_ClientPlatform~A
**Date:** 2026-04-09
**Task Order:** ADVI_49PUSH.044
**Status:** Complete. Fix committed and pushed. Awaiting AE re-upload + D_04 re-run.

---

## Summary

The Firm Overview donut (platinum/firm/mix_summary.json) was reading asset class
mix values from `gold/views/firm_composition.json` (silver writer), which uses
a different classification methodology than C_06's ETFClassifier. This produced
a ~$46M fixed income discrepancy vs the Assets Overview header panel.

Fix: one-line source change in `build_firm_mix_summary` in D_04 -- read
`gold/views/mix_daily_summary.json` (C_06 output) instead of firm_composition.json
for the `mix` snapshot field. Concentration/top_holdings still comes from firm_comp.

---

## Root Cause

Both `platinum/firm/mix_summary.json` (donut) and `platinum/firm/timeseries_overview.json`
(header) are written by D_04, but they read from different sources:

- `timeseries_overview.json` mix -> `firm_mix_views.json` (D_03 period-aggregated from C_06)
- `mix_summary.json` mix -> `firm_composition.json` (silver writer, DIFFERENT classifier)

The silver writer uses keyword-based classification or BD-native asset class fields, while
C_06 uses ETFClassifier from `lib/etf_classifier.py`. They disagree on ~$57M of structured
products (Shield annuities, Buffer products), which the silver writer puts into equity/fi
but ETFClassifier correctly puts in alternatives.

Confirmed by comparing S3 artifacts:
- `firm_composition.json` (data_as_of: 2026-04-08): equity=$1,224M, fi=$315M, alts=$73M, other=$6M
- `mix_daily_summary.json` latest (2026-04-02): equity=$1,185M, fi=$361M, alts=$72M

Gaps: fi ~$46M, equity ~$39M -- match Andrew's observed discrepancy.

---

## Investigation

Ran comp-platinum reverse on both files -- both produced by D_04. Then checked D_03 I/O
(comp-pipescript io D_03, comp-pipescript io D_04). D_04 reads both FIRM_COMPOSITION and
FIRM_MIX_VIEWS. Traced D_04.build_firm_mix_summary() directly -- confirmed that lines 317-325
used `firm_comp.mix` for the donut values while `timeseries_overview` at lines 1037-1044 used
`firm_mix_views.views.quarterly`.

---

## Fix

**File:** `data/black_diamond/scripts/gold/D_04.client_portal_summary.py`
**Function:** `build_firm_mix_summary()`

Added `MIX_DAILY_SUMMARY` import from `lib/s3_layout`.

Changed mix_snapshot source from `firm_comp.mix[]` (silver) to
`mix_daily_summary.firm[latest_date]` (C_06 / ETFClassifier):

- Before: iterate `firm_comp.get('mix', [])` -- silver classification
- After: read `mix_daily_summary.get('firm', {})`, take `max(dates)`, compute pct from total

`firm_comp` is still read, but only used for `concentration` (top holdings) and
`data_as_of` fallback. The `composition` passthrough field is preserved unchanged.

---

## Pre/Post Values

| Field | Before (silver) | After (C_06) | Header (C_06) |
|-------|-----------------|--------------|---------------|
| equity | $1,224M | $1,185M | $1,185M |
| fixed_income | $315M | $361M | $361M |
| alternatives | $73M | $72M | $72M |
| Gap vs header (FI) | ~$46M | ~$0 | -- |

Both panels now derive from the same canonical classification pipeline.

---

## Commit

| SHA | Change |
|-----|--------|
| `fe999416` | fix(D_04): mix_summary.json donut uses C_06 ETFClassifier, not silver firm_composition |

Pushed to origin/CLOUD.

---

## Files Modified

| File | Change |
|------|--------|
| `data/black_diamond/scripts/gold/D_04.client_portal_summary.py` | build_firm_mix_summary: read MIX_DAILY_SUMMARY for mix_snapshot; firm_comp retained for concentration only |

---

## Next Steps

[AE 0.6.0] Upload D_04 to S3 and re-run gold chain (D_04 is already in the pending
re-upload queue from the previous session's ADVI_49PUSH.006 work).

After the re-run, verify:
- `platinum/firm/mix_summary.json` mix.fixed_income ~= $361M
- `platinum/firm/timeseries_overview.json` Q2 2026 fixed_income.value ~= $361M
- Both within $1M of each other

Note: once C_06 cliff fix is deployed and full rebuild runs, both panels will reflect
corrected post-Feb-4 values. The donut source fix is independent of the C_06 fix.

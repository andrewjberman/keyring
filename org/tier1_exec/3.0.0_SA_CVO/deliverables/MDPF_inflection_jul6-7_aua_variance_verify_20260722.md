# Inflection daily-AUA July 6-7 variance -- CVO verify (Andrew-direct)

**Verifier:** 3.0.0_SA_CVO · **Date:** 2026-07-22 · **Trigger:** Andrew-direct ("variance in daily AUA on inflection, bouncing back and forth on July 6 and 7, jumpy and resets -- look into it and verify")

## Verdict: a REAL reclassification event, mis-DISPLAYED by the legacy; the revamp already fixes the display. NOT a real AUM change; NOT a pipeline bug in the revamp.

## What Andrew is seeing (currently-served = LEGACY, router rolled back)
Legacy inflection model vs non_model bounces on 07-06/07-07 (total custody flat ~$202M):
- 07-06: model $136,859,722 (+$14.6M), non_model $65,461,006 (-$14.0M)   <- SPIKE
- 07-07: model $123,562,809 (-$13.3M), non_model $80,123,458 (+$14.7M)   <- RESET
Total flat -> a model<->non_model RECLASSIFICATION swing, not an AUM move.

## Root cause (source-grounded)
1. **Eclipse source totalValue is STABLE** ~$200-203M across 07-06..07-10 (856 portfolios/day) -- NO spike at source. So the swing is model/non-model CLASSIFICATION, not money.
2. **Producer classifies model iff `modelId` resolves to an Opal crosswalk** (`_eclipse_models_for_date`, dim_mdpf_aggregate_aua_timeseries.py). On the **07-10 eclipse partition, 65 "IWM ..." portfolios changed `modelId`** (18->6, 20->3, 16->7, 19->28, ...), moving ~$11.8M from non-crosswalk (non-model) into Opal-crosswalk (model): opal|blend-named value 125.1M (475 pf, 07-09) -> 136.9M (540 pf, 07-10).
3. **PERMANENT, not transient**: the flipped modelIds STAY reassigned through 07-16/17/20 (model bucket holds ~137-139M). A genuine one-time re-mapping in Eclipse, not a data blip that reverts.

## Why it LOOKS like a bounce/reset in the current chart
The legacy's **rederived-business-day date axis MISLABELS** the 07-10 step: it places the 07-10 value ($136,859,722, exact-equal to the eclipse 07-10 partition) at **07-06**, then 07-07 reverts to the pre-step value -> a false up-down. The **revamp's real-trading-day axis dates the step correctly at 07-10** and renders 07-06/07-07 smoothly (122.9M / 123.6M): revamp 07-06/07/08/09 = a smooth ramp, clean single step at 07-10. **The revamp about to re-publish already removes the jumpiness.**

## Residual (business question, NOT a data defect)
Is the 07-10 Eclipse re-mapping of the ~65 "IWM ..." portfolios INTO Opal-crosswalk models correct at the business level? That is a model-classification decision (should these IWM portfolios count as Opal model AUA?), owned by the business/Eclipse mapping -- the pipeline faithfully reflects whatever Eclipse assigns. Flagging for Andrew/DS; the revamp display is correct given the source.

## Grounding
Live-read: opal-data-assets eclipse/inflection/silver/fact_portfolios_full/date={06..20}/ (source), gold/mdpf_revamp/inflection/aggregate_aua_timeseries.json (revamp), opal-data-portal-v2 json/mdpf/inflection/aggregate-aua-timeseries.json (legacy served). modelId trajectory + opal|blend value swept per date; exact value match (legacy 07-06 == eclipse 07-10 == $136,859,722).

# MDPF_STRATID round 1 -- writer census at the Global fold (PRD OPEN ITEM 3; drain act 1)

**By:** `2.0.0_SA_COO~S1`, 2026-10-08 ~21:1xZ, at base f3cc1552bf (before any ST-t-3 code). Instrument: native Grep, count mode, over
the whole repo, then over `portal/src/**`, `infra/aws/lambda/**` and `lib/**`. Claim: measured (code read); the served plane is read at
the one real run.

## The property and its writers

Property: Global's served headline `opal_aggregate_aua`, its SMA node (category-views `nodes.SMA`), and the additive series the tree and
aum-metrics subtract or add (`tax_additive_aua`, `base_excluding_tax_aua`; ST-t-3 adds `sma_additive_aua`).

| # | writer (rule read) | what it writes | in ST-t-3's write set |
|---|---|---|---|
| W1 | `dim_mdpf_aggregate_aua_timeseries.build_global_artifact` (:2245) | Global `opal_aggregate_aua` = 49F(model+non_model) + INF(model) + COT(model, roll-forward carry); by_model over the fixed `GLOBAL_MODEL_KEYS` only | yes (read; edit only if its extension-field validation refuses) |
| W2 | `mdpf_gold_consolidator.apply_taxsma_overlay` (:1648) | Global `opal_aggregate_aua` += 49F Tax + Cottonwood Tax (overlap-withheld); `base_excluding_tax_aua`, `tax_additive_aua`, `tax_coverage`; by_model `tax` additive | yes (behaviour unchanged; AC3 guards it) |
| W3 (new) | `mdpf_gold_consolidator.apply_sma_sleeve_overlay` (ST-t-3) | Global `opal_aggregate_aua` += additive sleeves less overlap; `sma_additive_aua`, `sma_additive_withheld`; by_model `<member>` additive | yes |
| W4 | `mdpf_gold_consolidator._shape_category_views` (:610) | category-views nodes; on a folded doc total = `base_excluding_tax_aua` + every additive SMA member in by_model (:671-676) | yes (read; the probe shows it needs no edit) |
| W5 | `dim_mdpf_aum_metrics` (:225-235, :395-402) | aum-metrics firm total and its labelled `taxsma` component | yes |

N = 5 writers (4 at the base, 1 new). Every one sits in ST-t-3's paths, so no rule outside the round moves Global's figures.

## Readers outside the round (the served plane's consumers)

- `portal/src/pages/ModelPortfolios.tsx` (6 hits), `portal/src/lib/pairedProvenanceRead.ts` (2), `portal/src/api/portal-proxy.ts` (2): the
  page's headline field-reads `opal_aggregate_aua`; its bars + Non-Model band read `model_aua` + `non_model_aua`. An additive amount
  sits in the headline and in neither band -- the SAME treatment Tax has had since 2026-09-30 (`aggregate_basis` INCLUDES_ADDITIVE). The
  PRD puts frontend work out of scope; the PFDE amount (412,892.63) inherits Tax's display, no new behaviour.
- `infra/aws/lambda/opal-assets/opal-assets-daily-emitter/lambda_function.py` (5), `infra/aws/lambda/smartx_ingestion_pipeline/*` (5): their
  own firm artifacts' `opal_aggregate_aua`, not Global's fold. Not readers of the Global served key.
- `org/standards/MDPF_TAXSMA_DATA_CONTRACT.json` names `timeseries_extension_fields` (2 hits): a new `sma_additive_aua` key is outside
  that contract's list. ST-t-3's AC1/AC2 run the shaper and the fold on served bytes; whether the contract needs a row is a question for
  the pair's CTO half, raised there.

## For the never-widen pair (drain act 2)

Blast radius: `s3://opal-data-assets/portal/gold/mdpf/global/{aggregate-aua-timeseries,category-views,aum-metrics}/<run date>.json`;
per-firm keys gain an all-None `sma_additive_aua` field and no figure. Expected outcome from W3's own rule, both branches: Cottonwood
`overlap_model_value` present on the date -> Global total + (PFDE - overlap), PFDE under SMA > ETF Strategies; absent -> no total move,
PFDE in `sma_additive_withheld` as `OVERLAP_UNMEASURED`. Rollback: redeploy the prior `mdpf-gold-lambda` package and slice; the next
scheduled run rewrites the date.

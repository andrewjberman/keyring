# GLDPRE Final Status — 2.0.0_SA_COO

**Date:** 2026-03-20
**CTO validated:** All WS1/WS3/WS4/WS5 code confirmed clean.

---

## Committed

| Commit | Branch | Files | Status |
|---|---|---|---|
| `3ede9fc4` | CLOUD | 06b (ETFClassifier + 4-class), lambda_function.py (mix.json fix) | Clean |
| `a4f71d7` | portal DEV | types.ts (1395-line restore + 4-class), PartnerAnalytics.tsx (4-class), ClientsTab.tsx | Clean except ClientsTab.tsx bug below |

## CTO Fix (Uncommitted in Portal)

ClientsTab.tsx `deriveQuarterlyFromTimeseries` had `structured_notes` and `other` lines
left over from stash pop merge. These reference fields that no longer exist on
MixTimeseriesPoint. CTO removed them. **This fix needs to be committed to portal DEV.**

## Remaining Before GLDRST

| # | Item | Owner | Type |
|---|---|---|---|
| 1 | **Commit ClientsTab.tsx fix** to portal DEV | DT | One commit |
| 2 | **WS2: aua_mix in script 09** | DS (runtime or manual) | CTO confirmed target: script 09, not archived 08. Read 06b classified pcts, apply to 09's AUA totals, write aua_mix.{granularity} in standard {categories, data} format. Replace deprecated aua_mix key. |
| 3 | **Lambda deploy WS3** as partners-api-v1.8.0 | DT | Terraform apply (one-line S3 key change) |
| 4 | **Full gold rerun on EC2** | AE_PartnerETL | After WS1+WS2 deployed to EC2. Produces firm_mix_views.json with 4-class + cash residual. |
| 5 | **Portal DEV->PROD merge** | DT | After gold rerun verified + ClientsTab fix committed. Shared gate with MVP318/MVPLVL/MIXV2. |

## WS2 Spec (from CTO)

- **Target:** `data/black_diamond/scripts/gold/09_generate_partner_analytics.py`
- **Source for class pcts:** 06b output (firm_mix_views.json or client_mix_timeseries.parquet)
- **Source for AUA totals:** client_performance.parquet (already read by 09)
- **Output:** `aua_mix.{granularity}` section in timeseries_chart.json
- **Format:** `{categories: ['Equity', 'Fixed Income', 'Alternatives', 'Cash'], data: [...]}`
- **Cash:** residual = total - equity - fixed_income - alternatives
- **Replaces:** deprecated `aua_mix` key (2 data points, non-standard segments format)

## Dependency Chain

```
ClientsTab.tsx commit (#1)
          |
WS2 (#2) -----> Full gold rerun (#4) -----> Portal merge (#5)
          |                                        |
Lambda deploy (#3) --------------------------------+
```

WS2 and Lambda deploy are independent of each other. Both must complete before gold rerun.
Portal merge is the final gate.

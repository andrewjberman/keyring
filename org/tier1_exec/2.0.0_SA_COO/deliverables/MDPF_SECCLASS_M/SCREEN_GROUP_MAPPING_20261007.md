# Screen-group census and the six-class mapping (MDPF_SECCLASS round 8, cell SC-e-24, FWD-16)

**Author:** `0.9.0_WK_MDPF_SECCLASS~23`, 2026-10-07, task order `MDPF_SECCLASS.TO-SC-e24`. **Claim:** `measured` where a row says so (the code states the mapping), `inferred` where a row says so (a PROPOSAL; the CVO grades it, nothing here is ruled).

**Denominator:** python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/screen_group_census.py --write: portal/src .ts/.tsx/.js/.jsx minus tests (627 files) + 10 producer files; 70 files carry a class-list vocabulary or the words 'asset class', 44 are a screen's file, 26 are excluded with a reason, 0 unaccounted.

Data form: `SCREEN_GROUP_MAPPING_20261007.json`, reproduced by `R10_CHECKS/screen_group_census.py --write`. The six: `cash`, `fixed_income`, `equity`, `structured`, `alternatives`, `commodities`. There is no seventh; `Multi-Asset` is listed below only as a group a screen shows today, and cell SC-e-23 removes it.

## 1. The screens

| # | Screen | Groups shown (count) | Basis |
|---|---|---|---|
| 1 | Positioning > Holdings (treemap, legend and table) | Fixed Income, Equity, Structured, Alternatives, Commodities (5) | measured |
| 2 | Positioning > Summary (allocation by class rows) | Fixed Income, Equity, Structured, Commodities, Alternatives (5) | measured |
| 3 | Investor Reporting > Holdings (treemap and legend) | Cash, Fixed Income, Equity, Structured, Alternatives, Commodities, Multi-Asset, Other, Unclassified (9) | measured |
| 4 | Investor Reporting > Holdings (class-mix bar in the drill tree) | Cash, Fixed Income, Equity, Structured, Alternatives, Commodities, Multi-Asset, Other, Unclassified (9) | measured |
| 5 | Investor Reporting > Holdings (securities table grouped by class) | Fixed Income, Equity, Structured, Alternatives, Commodities, Multi-Asset, Other, Unclassified (8) | measured |
| 6 | Investor Reporting > Holdings (held positions by asset class totals) | Cash, Fixed Income, Equity, Structured, Alternatives, Commodities, Multi-Asset, Other, Unclassified (9) | measured |
| 7 | Attribution > Holdings | Fixed Income, Equity (2) | measured |
| 8 | Attribution > Asset Allocation Summary | Fixed Income, Equity (2) | measured |
| 9 | Attribution > Style vs Policy comparison | Fixed Income, Equity (2) | measured |
| 10 | Capital Market Assumptions > Expectations (columns grouped by class) | Cash, Fixed Income, Equities, Alternatives, Commodities (5) | inferred |
| 11 | Advisor Intelligence > Partner Analytics > AUA mix (49 Financial and Demo) | Fixed Income, Equity, Alternatives, Structured, Commodities, Multi-Asset (6) | inferred |
| 12 | Advisor Intelligence > Partner Analytics > AUA mix (Inflection) | Cash, Fixed Income, Equity, Alternatives, Structured, Commodities, Multi-Asset (7) | measured |
| 13 | Advisor Intelligence > Partner Analytics > AUA mix (Cottonwood) | Cash, Fixed Income, Equity, Alternatives, Structured, Commodities, Multi-Asset, Unclassified, Other (9) | measured |
| 14 | Advisor Intelligence > Books, Advisor book and Profile mix donut (49 Financial and Demo) | Equity, Fixed Income, Alternatives, Structured, Commodities, Multi-Asset, Unclassified (7) | inferred |
| 15 | Advisor Intelligence > Books, Advisor book and Profile mix donut (Inflection) | Cash, Equity, Fixed Income, Alternatives, Structured, Commodities, Multi-Asset, Unclassified (8) | measured |
| 16 | Advisor Intelligence > Books, Advisor book and Profile mix donut (Cottonwood) | Cash, Equity, Fixed Income, Alternatives, Structured, Commodities, Multi-Asset, Unclassified, Other (9) | measured |
| 17 | Advisor Intelligence > Advisor Analytics > AUA mix bars | Cash, Fixed Income, Equity, Alternatives, Structured, Commodities, Multi-Asset, Unclassified, Other (9) | measured |
| 18 | Advisor Intelligence > Performance reporting > Allocation card | Equity, Fixed Income, Alternatives, Cash, structured, commodities (6) | measured |
| 19 | Advisor Intelligence > Inflection Insights > basket tile legend | Equity, Fixed Income, Alternatives, Cash (4) | inferred |

## 2. The mapping of the six, per screen

Each cell is the screen's group that the class lands in. `*` marks an `inferred` cell (a proposal). A class a screen does not draw today is shown with the group it is PROPOSED into and marked `*`.

| # | Cash | Fixed Income | Equity | Structured | Alternatives | Commodities |
|---|---|---|---|---|---|---|
| 1 | Fixed Income | Fixed Income | Equity | Structured | Alternatives | Commodities |
| 2 | Fixed Income | Fixed Income | Equity | Structured | Alternatives | Commodities |
| 3 | Cash | Fixed Income | Equity | Structured | Alternatives | Commodities |
| 4 | Cash | Fixed Income | Equity | Structured | Alternatives | Commodities |
| 5 | Fixed Income | Fixed Income | Equity | Structured | Alternatives | Commodities |
| 6 | Cash | Fixed Income | Equity | Structured | Alternatives | Commodities |
| 7 | Fixed Income | Fixed Income | Equity | Equity | Equity | Equity |
| 8 | Fixed Income | Fixed Income | Equity | Equity | Equity | Equity |
| 9 | Fixed Income | Fixed Income | Equity | Equity | Equity | Equity |
| 10 | Cash | Fixed Income | Equities | Equities* | Alternatives | Commodities |
| 11 | Fixed Income* | Fixed Income | Equity | Structured | Alternatives | Commodities |
| 12 | Cash | Fixed Income | Equity | Structured | Alternatives | Commodities |
| 13 | Cash | Fixed Income | Equity | Structured | Alternatives | Commodities |
| 14 | Fixed Income* | Fixed Income | Equity | Structured | Alternatives | Commodities |
| 15 | Cash | Fixed Income | Equity | Structured | Alternatives | Commodities |
| 16 | Cash | Fixed Income | Equity | Structured | Alternatives | Commodities |
| 17 | Cash | Fixed Income | Equity | Structured | Alternatives | Commodities |
| 18 | Cash | Fixed Income | Equity | structured | Alternatives | commodities |
| 19 | Cash | Fixed Income | Equity | Alternatives* | Alternatives | Alternatives* |

## 3. Notes and where the code states the mapping

**1. Positioning > Holdings (treemap, legend and table).** Five groups; Cash folds into Fixed Income (stated in code). Multi-Asset, Hedge, Other, Unclassified are not drawn here.
- `cash` -> Fixed Income (measured): HoldingsTab.tsx: 'Cash' FOLDS TO 'Fixed Income'; legendClassesFor(foldCash=true)
- files: `portal/src/components/holdings/HoldingsTreemapChart.tsx`, `portal/src/components/holdings/HoldingsBreakdownTable.tsx`, `portal/src/pages/Positioning/tabs/HoldingsTab.tsx`, `portal/src/pages/Positioning/constants/etf-categories.ts`, `portal/src/pages/Positioning/shared/etfAdapter.ts`, `portal/src/pages/Positioning/shared/satelliteAdapter.ts`, `portal/src/pages/Positioning/shared/satelliteSet.ts`, `portal/src/pages/Positioning/shared/bookSet.ts`, `portal/src/api/portal-proxy.ts`
- producers: `infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py`

**2. Positioning > Summary (allocation by class rows).** Five groups; Cash is summed into the Fixed Income row (stated in code).
- `cash` -> Fixed Income (measured): PositioningSummary.tsx ASSET_CLASSES: Fixed Income row served: ['fixed_income','cash'], blurb 'Bonds & Cash'
- files: `portal/src/pages/Positioning/panels/PositioningSummary.tsx`
- producers: `infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py`

**3. Investor Reporting > Holdings (treemap and legend).** Nine groups, the six one-to-one plus Multi-Asset, Other, Unclassified. Multi-Asset is a group this screen shows today; cell SC-e-23 removes it.
- files: `portal/src/pages/InvestorReporting/tabs/holdings/HoldingsTreemap.tsx`, `portal/src/pages/InvestorReporting/tabs/holdings/assetClass.ts`, `portal/src/components/holdings/HoldingsTreemapChart.tsx`, `portal/src/pages/InvestorReporting/contracts/adapt.ts`, `portal/src/pages/InvestorReporting/contracts/index.ts`, `portal/src/pages/InvestorReporting/contracts/wire/HoldingsSnapshot.ts`
- producers: `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py`

**4. Investor Reporting > Holdings (class-mix bar in the drill tree).** CLASS_BAR_ORDER is the key set of ASSET_CLASS_COLOR in rank order: the same nine groups as the treemap. Multi-Asset: SC-e-23 removes it.
- files: `portal/src/pages/InvestorReporting/tabs/holdings/DrillTree.tsx`, `portal/src/components/CategoryViewTree.tsx`, `portal/src/pages/InvestorReporting/tabs/holdings/assetClass.ts`
- producers: `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py`

**5. Investor Reporting > Holdings (securities table grouped by class).** ASSET_CLASS_ORDER (five) plus extraClasses Multi-Asset, Other, Unclassified. A cash row sits under Fixed Income in this table while the treemap and class bar draw Cash as its own group. Multi-Asset: SC-e-23 removes it.
- `cash` -> Fixed Income (measured): HoldingsBreakdownTable.tsx: displayClass 'Cash' -> 'Fixed Income' (PRD s.3 class 1)
- files: `portal/src/pages/InvestorReporting/tabs/holdings/SecurityList.tsx`, `portal/src/components/holdings/HoldingsBreakdownTable.tsx`, `portal/src/pages/InvestorReporting/tabs/holdings/assetClass.ts`
- producers: `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py`

**6. Investor Reporting > Holdings (held positions by asset class totals).** One line per served class in the page's class order (Cash first): the nine groups of the class-mix bar. Multi-Asset: SC-e-23 removes it.
- files: `portal/src/pages/InvestorReporting/tabs/holdings/classTotals.ts`, `portal/src/pages/InvestorReporting/tabs/holdings/assetClass.ts`
- producers: `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py`

**7. Attribution > Holdings.** Two groups by Andrew-direct 2026-10-06 (attribution funnel); source_asset_class keeps the registry class. S23: etf-categories.ts still carries a static Cash / Fixed Income / Equity / Hedge category list (surface for the later round).
- `cash` -> Fixed Income (measured): producer funnel: fixed_income and cash -> Fixed Income
- `structured` -> Equity (measured): producer funnel: every other class -> Equity
- `alternatives` -> Equity (measured): producer funnel: every other class -> Equity
- `commodities` -> Equity (measured): producer funnel: every other class -> Equity
- files: `portal/src/pages/Attribution/constants/etf-categories.ts`, `portal/src/pages/Attribution/constants/holdings-shared.tsx`, `portal/src/pages/Attribution/components/HoldingsCustomTreemapContent.tsx`, `portal/src/pages/Attribution/tabs/SelectionTab.tsx`
- producers: `infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-holdings-attribution/lambda_function.py`

**8. Attribution > Asset Allocation Summary.** Two groups (Fixed Income, Equity); the producer's benchmark table also carries Structured, Commodities, Alternatives at 0.0 'no benchmark'.
- `cash` -> Fixed Income (measured): producer funnel: fixed_income and cash -> Fixed Income
- `structured` -> Equity (measured): producer funnel: every other class -> Equity
- `alternatives` -> Equity (measured): producer funnel: every other class -> Equity
- `commodities` -> Equity (measured): producer funnel: every other class -> Equity
- files: `portal/src/pages/Attribution/components/AssetAllocationSummary.tsx`, `portal/src/pages/Attribution/constants/holdings-shared.tsx`, `portal/src/pages/Attribution/Attribution.tsx`
- producers: `infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-allocation-summary/lambda_function.py`

**9. Attribution > Style vs Policy comparison.** Same two groups and producer as the Asset Allocation Summary.
- `cash` -> Fixed Income (measured): producer funnel: fixed_income and cash -> Fixed Income
- `structured` -> Equity (measured): producer funnel: every other class -> Equity
- `alternatives` -> Equity (measured): producer funnel: every other class -> Equity
- `commodities` -> Equity (measured): producer funnel: every other class -> Equity
- files: `portal/src/pages/Attribution/components/StylePolicyComparison.tsx`, `portal/src/pages/Attribution/constants/holdings-shared.tsx`
- producers: `infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-allocation-summary/lambda_function.py`

**10. Capital Market Assumptions > Expectations (columns grouped by class).** Groups expected return and volatility by class: a class grouping, not a weight mix. Five categories, no Structured.
- `fixed_income` -> Fixed Income (measured): category 'Fixed Income'
- `equity` -> Equities (measured): category 'Equities'
- `structured` -> Equities (inferred): no Structured category; proposed Equities, the side the attribution funnel (Andrew-direct 2026-10-06) puts structured on
- files: `portal/src/pages/CapitalMarketAssumptions/tabs/ExpectationsTab.tsx`, `portal/src/pages/CapitalMarketAssumptions/types.ts`
- producers: `infra/aws/lambda/v2_portal/yang_pipeline/cma/yang-generate-cma/lambda_function.py`

**11. Advisor Intelligence > Partner Analytics > AUA mix (49 Financial and Demo).** includesCash false: the cash slice is filtered out today. Multi-Asset is shown today; SC-e-23 removes it. Demo's `ordered` list is the same.
- `cash` -> Fixed Income (inferred): cash is not drawn here today; proposed to fold into Fixed Income, the fold Positioning states (HoldingsTab.tsx)
- files: `portal/src/pages/AdvisorIntelligence/_partners/49financial/layout.ts`, `portal/src/pages/AdvisorIntelligence/_partners/demo/layout.ts`, `portal/src/pages/AdvisorIntelligence/_shared/components/PartnerAnalytics.tsx`, `portal/src/pages/AdvisorIntelligence/_shared/types/TenantLayoutConfig.ts`, `portal/src/pages/AdvisorIntelligence/_shared/hooks/useTenantLayout.ts`
- producers: `data/black_diamond/scripts/gold/C_06.client_mix_timeseries.py`

**12. Advisor Intelligence > Partner Analytics > AUA mix (Inflection).** Seven groups; the six one-to-one plus Multi-Asset (SC-e-23 removes it).
- files: `portal/src/pages/AdvisorIntelligence/_partners/inflection/layout.ts`, `portal/src/pages/AdvisorIntelligence/_shared/components/PartnerAnalytics.tsx`
- producers: `data/inf/scripts/gold/INF_D_03.composition_artifacts.py`

**13. Advisor Intelligence > Partner Analytics > AUA mix (Cottonwood).** Nine groups; the six one-to-one plus Multi-Asset (SC-e-23 removes it), Unclassified, Other.
- files: `portal/src/pages/AdvisorIntelligence/_partners/cottonwood/layout.ts`, `portal/src/pages/AdvisorIntelligence/_shared/components/PartnerAnalytics.tsx`
- producers: `data/cot/scripts/gold/C_06.client_mix_timeseries.py`

**14. Advisor Intelligence > Books, Advisor book and Profile mix donut (49 Financial and Demo).** normalizeMixTo4Class without includeCash: a cash row is dropped from the donut today. Multi-Asset is shown today; SC-e-23 removes it.
- `cash` -> Fixed Income (inferred): cash is not drawn here today; proposed to fold into Fixed Income, the fold Positioning states (HoldingsTab.tsx)
- files: `portal/src/pages/AdvisorIntelligence/_shared/lib/composition.ts`, `portal/src/pages/AdvisorIntelligence/_shared/tabs/ClientsTab.tsx`, `portal/src/pages/AdvisorIntelligence/_shared/AdvisorBookView.tsx`, `portal/src/pages/AdvisorIntelligence/_shared/panels/ConsolidatedOverviewPanel.tsx`, `portal/src/pages/AdvisorIntelligence/_shared/panels/CanonicalBookView.tsx`, `portal/src/pages/AdvisorIntelligence/_shared/AdvisorBookClientDetail.tsx`
- producers: `data/black_diamond/scripts/gold/D_03.composition_artifacts.py`

**15. Advisor Intelligence > Books, Advisor book and Profile mix donut (Inflection).** includeCash true: eight groups, the six one-to-one plus Multi-Asset (SC-e-23 removes it) and Unclassified.
- files: `portal/src/pages/AdvisorIntelligence/_shared/lib/composition.ts`, `portal/src/pages/AdvisorIntelligence/_shared/tabs/ClientsTab.tsx`, `portal/src/pages/AdvisorIntelligence/_shared/AdvisorBookView.tsx`, `portal/src/pages/AdvisorIntelligence/_shared/panels/ConsolidatedOverviewPanel.tsx`, `portal/src/pages/AdvisorIntelligence/_shared/panels/CanonicalBookView.tsx`, `portal/src/pages/AdvisorIntelligence/_shared/AdvisorBookClientDetail.tsx`
- producers: `data/inf/scripts/gold/INF_D_03.composition_artifacts.py`

**16. Advisor Intelligence > Books, Advisor book and Profile mix donut (Cottonwood).** includeCash and includeOther true: nine groups, the six one-to-one plus Multi-Asset (SC-e-23 removes it), Unclassified, Other.
- files: `portal/src/pages/AdvisorIntelligence/_shared/lib/composition.ts`, `portal/src/pages/AdvisorIntelligence/_shared/tabs/ClientsTab.tsx`, `portal/src/pages/AdvisorIntelligence/_shared/AdvisorBookView.tsx`, `portal/src/pages/AdvisorIntelligence/_shared/panels/ConsolidatedOverviewPanel.tsx`, `portal/src/pages/AdvisorIntelligence/_shared/panels/CanonicalBookView.tsx`, `portal/src/pages/AdvisorIntelligence/_shared/AdvisorBookClientDetail.tsx`
- producers: `data/cot/scripts/gold/D_03.composition_artifacts.py`

**17. Advisor Intelligence > Advisor Analytics > AUA mix bars.** Draws every class a served mix carries (nine possible groups, a class absent from every bar draws nothing). Multi-Asset: SC-e-23 removes it.
- files: `portal/src/pages/AdvisorIntelligence/_shared/components/AdvisorAnalytics.tsx`
- producers: `data/black_diamond/scripts/gold/C_06.client_mix_timeseries.py`

**18. Advisor Intelligence > Performance reporting > Allocation card.** Four classes carry a label; Structured and Commodities render as the raw lower-case token, a group named differently from the shared list.
- `structured` -> structured (measured): classLabel(): an unlabelled class renders the producer's token verbatim
- `commodities` -> commodities (measured): classLabel(): an unlabelled class renders the producer's token verbatim
- files: `portal/src/pages/AdvisorIntelligence/_shared/perfrp/PerfrpAllocation.tsx`

**19. Advisor Intelligence > Inflection Insights > basket tile legend.** Tiles are coloured by the served class through mixPieColor, but the legend lists four. A structured or commodities tile wears its own colour with no legend entry.
- `structured` -> Alternatives (inferred): legend has no Structured entry; MIX_PIE once shared one colour between structured_notes and alternatives
- `commodities` -> Alternatives (inferred): legend has no Commodities entry; the old `hedge` colour was Alternatives' orange
- files: `portal/src/pages/AdvisorIntelligence/_partners/inflection/InflectionInsightsPanel.tsx`

## 4. The proposals (every `inferred` cell)

- Screen 10 (Capital Market Assumptions > Expectations (columns grouped by class)): `structured` -> **Equities**. no Structured category; proposed Equities, the side the attribution funnel (Andrew-direct 2026-10-06) puts structured on.
- Screen 11 (Advisor Intelligence > Partner Analytics > AUA mix (49 Financial and Demo)): `cash` -> **Fixed Income**. cash is not drawn here today; proposed to fold into Fixed Income, the fold Positioning states (HoldingsTab.tsx).
- Screen 14 (Advisor Intelligence > Books, Advisor book and Profile mix donut (49 Financial and Demo)): `cash` -> **Fixed Income**. cash is not drawn here today; proposed to fold into Fixed Income, the fold Positioning states (HoldingsTab.tsx).
- Screen 19 (Advisor Intelligence > Inflection Insights > basket tile legend): `structured` -> **Alternatives**. legend has no Structured entry; MIX_PIE once shared one colour between structured_notes and alternatives.
- Screen 19 (Advisor Intelligence > Inflection Insights > basket tile legend): `commodities` -> **Alternatives**. legend has no Commodities entry; the old `hedge` colour was Alternatives' orange.

Five proposals in all. Two fold `cash` into Fixed Income (screens 11 and 14, which drop a cash slice today), the fold Positioning's table, summary and the Investor Reporting securities table already state in code. The other three (CMA `structured`; Inflection Insights `structured` and `commodities`) have no stated rule on those screens. The only ruled funnel is Attribution's (Andrew-direct 2026-10-06: Fixed Income and Cash to Fixed Income, every other class to Equity), which is why CMA's `structured` is proposed onto Equities; Inflection Insights' pair is proposed onto Alternatives from its legacy colour sharing. Whether to apply the funnel anywhere else is the CVO's to grade.

## 5. S26: the geography list

- Source: `infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py:95` (`ETF_GEOGRAPHY_MAPPING`; the order and the PRD manifest say line 96 and line 95 respectively, the file at this base reads line 95; surprise row filed).
- Distinct values: Emerging, Global, International, US; 92 tickers listed; an unlisted ticker is served `Other`.
- Placement (proposal, not a decision): PROPOSED, not decided (the CTO decides): a new field `geography` on the shared list (the etf-classifications table), one of the four values above, 'Other' where a row has none. Not an existing field: sub_asset_class carries a different grain (US Large Cap, Developed, International, EM ... for equity only; none of its fixed-income values is a region) and the list holds 3,493 rows against this dict's tickers. OPEN: which of the listed tickers have a row today, and who fills the field for the rest, is the placing round's act.

## 6. Files carrying a class vocabulary that are not a screen

- `portal/src/api/endpoints/advisor-intelligence.ts`: API client for AI payloads: types and fetch, draws no group
- `portal/src/api/endpoints/aum.ts`: AUM by model asset-class code (UST, INT, LT ...), a different axis
- `portal/src/api/endpoints/market.ts`: market data client, not a mix
- `portal/src/components/market-performance/ExecutiveSummary.tsx`: Market Performance tab: instrument heat maps and RSI by instrument class, not a mix
- `portal/src/components/market-performance/MarketRegimeModal.tsx`: Market Performance tab: instrument heat maps and RSI by instrument class, not a mix
- `portal/src/components/market-performance/RSIBars.tsx`: Market Performance tab: instrument heat maps and RSI by instrument class, not a mix
- `portal/src/components/market-performance/RSIModal.tsx`: Market Performance tab: instrument heat maps and RSI by instrument class, not a mix
- `portal/src/components/PerformanceHeatMap.tsx`: market heat map, not a mix
- `portal/src/hooks/useRSIValues.ts`: market RSI hook, not a mix
- `portal/src/lib/chartColors.ts`: colour registry (ASSET_CLASS, MIX_PIE): colours only, the groups come from each caller
- `portal/src/lib/dataLoader.ts`: market-instrument grouping for performance heat maps, not a mix by class of a book
- `portal/src/lib/periodResolution.ts`: period maths, names asset class in a comment
- `portal/src/lib/tickerRegistry.ts`: market-instrument registry, not a mix
- `portal/src/pages/AdvisorIntelligence/_shared/perfrp/contract.ts`: perfrp data contract (dim_asset_classification partitions): a dimension name, draws no group
- `portal/src/pages/AdvisorIntelligence/_shared/types.ts`: AI payload types, draws no group
- `portal/src/pages/CapitalMarketAssumptions/components/PhilosophyPillars.tsx`: prose, no class list
- `portal/src/pages/CapitalMarketAssumptions/tabs/OpalViewsTab.tsx`: allocation views by pair/class position (-2..+2), not a mix by class
- `portal/src/pages/Correlation/components/CorrelationMatrix.tsx`: correlation matrix of instruments, not a mix
- `portal/src/pages/Correlation/constants.ts`: correlation matrix of instruments, not a mix
- `portal/src/pages/InvestorReporting/tabs/holdings/AllocationBars.tsx`: bars coloured by model code, not by class
- `portal/src/pages/InvestorReporting/tabs/holdings/palette.ts`: colour picker, no class list drawn
- `portal/src/pages/SecurityAnalysis/components/ChatterBubbles.tsx`: security ranking and chatter, not a mix
- `portal/src/pages/SecurityAnalysis/components/PriceBars.tsx`: security ranking and chatter, not a mix
- `portal/src/pages/SecurityAnalysis/components/RankedList.tsx`: security ranking and chatter, not a mix
- `portal/src/pages/SecurityAnalysis/types.ts`: security ranking and chatter, not a mix
- `portal/src/pages/SecurityScanner/types.ts`: scanner types, not a mix

# Investor Reporting: performance presentation review

> **Organization update, September 10, 2026:** Andrew has replaced the former project/workstream structure with two projects: [IR FE](investor-reporting-ir-fe-brief-20260910.md) for the complete client-facing product and [IR BK](investor-reporting-ir-bk-brief-20260910.md) for ingestion, tenant scoping, transformations and operations. Both briefs map all four source briefs and five supporting documents. The body below remains dated research; its former ownership labels are historical. Permanent FWD IDs are unchanged. Macro IRPT, directive D9, laptop execution.

**Author:** 4.0.0_SA_CRO · September 10, 2026 · RCN-0008 / WS2

**Parent:** [one-project L1 brief](investor-reporting-lightweight-brief-20260910.md)

**Status:** Evidence-backed design for Andrew's selective review; no implementation or endpoint ratification.

**Authority:** [Andrew's exact performance exploration instruction](../../org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260910_0947ET_PERFORMANCE_ENDPOINT_EGRESS.md).

**Reproduction:** [bounded probe](../research/investor_reporting_performance_20260910/probe_performance.py), [sanitized evidence manifest](sources/INVESTOR_REPORTING_PERFORMANCE_EVIDENCE_20260910.json), [interactive presentation sketch](../research/investor_reporting_performance_20260910/presentation-review.html).

## 1. Recommended presentation

The provider APIs can support a common Opal performance report without a new return engine. Black Diamond exposes period and chart endpoints. Orion's small interface hides a flexible calculation endpoint: one tested request returned a household, its two accounts, three period returns, beginning/ending values, and daily performance detail.

Use this common layout:

```text
OPAL / INVESTOR REPORTING
Search clients by name [                         ]
Selected relationship · selected accounts · data through date

Reporting                  Analysis                  Holdings

Performance report          Period [ YTD / presets / custom ]   Export PDF
Beginning value          Ending value          Period return

Cumulative return chart for the selected period
Provider-assigned benchmark when available and verified

Period returns             Selected period | QTD | YTD
Account detail             Beginning value | Ending value | Period return

Time-weighted · Net of fees · Actual returned dates · Source / disclosures
Optional verified sections: cash movement, investment gain, value history
```

**Recommendation P1:** lead with three useful figures, the cumulative return chart, and a compact account table. Keep the household total prominent and allow account selection in the shared header. Preserve the three-tab order Andrew gave. A selected account uses the same report layout.

**Recommendation P2:** use TWR, net of fees, as the proposed initial view; retain the actual vendor configuration and label it. Default to YTD with familiar period presets and custom dates. Both requests already use TWR/net-of-fees settings. This is a product recommendation, not a claim that all provider calculation options are interchangeable. Long-period annualization needs its own verified mapping; the chart represents cumulative growth, even when a period table eventually includes annualized returns.

**Recommendation P3:** start with a return chart. A dollar-value chart and a common contribution/gain bridge are optional extensions until their field mappings reconcile. Do not label ending minus beginning value as investment gain: that difference can include cash movement. The available BD extras can occupy optional sections without forcing Orion fields into false equivalents.

**Recommendation P4:** generate the report automatically after a valid client/account selection, keeping the header immediately responsive from cache. Date changes refresh the report; the PDF uses the same immutable report revision as the reviewed screen. A source change while generating a PDF must not silently change the exported figures.

These four recommendations are the concrete design choices for Andrew to review. The initial screenshot sketch uses synthetic figures and is a discussion artifact, not deployed product behavior.

## 2. What the supplied references actually show

All three HARs were inventoried: **487 entries** (53 BD part 1, 119 BD part 2, 315 Orion). Targeted body inspection covered performance, source settings/groupings, client search and membership. All four screenshots were viewed. This is not a claim to have interpreted every unrelated billing, security, analytics or trading response in those captures.

| Screenshot | Observed surface | Design implication |
|---|---|---|
| 094115 | BD Advisor / Business Intelligence dashboard: firm market value, fees, relationships, flows, executive-summary hierarchy | Useful visual reference; firm metrics do not belong in the selected client's performance report. |
| 094057 | BD Client View: account activity, value chart, allocation, performance, gain/loss and other widgets | Borrow the summary/chart rhythm. Allocation and model detail remain in Holdings; no need to reproduce the entire widget dashboard. |
| 094405 | Orion Performance Viewer: summary and period-detail tables, calculation controls | Sparse presentation does not mean sparse API data. We can render its structured result using the same Opal components. |
| 094202 | Orion Find Entity modal with Household/Portfolio Group/Registration/Account and name autosuggest | This is the search interaction Andrew wants moved into our page header and served from the firm/advisor cache. |

Screenshots are `Screenshot 2026-09-10 <time>.png` in Andrew's Pictures/Screenshots; captures remain in Downloads. No raw screenshot, HAR, token, client name or account identifier is copied into committed artifacts.

## 3. Live findings and minimum vendor calls

Egress was performed during this investigation, 13:50–14:00 UTC. **Nine HTTP requests:** two initial BD performance calls returned 401; seven subsequently returned 200, including one ordinary session-token refresh. There were six successful performance/report calculations: two BD and four Orion. No portfolio, trade, billing or rebalance mutations were performed.

| Provider / surface | Successful observed result | Proposed normal path |
|---|---|---|
| BD `POST /portfolioreporting/api/performance/performancePeriod` | Four ranges; account plus 11 segment children; returns, beginning/ending values, flows, fees, benchmark data. 176,999 response bytes, 1.078 s after session renewal. | One period request. Remove unneeded segment detail only after confirming the reduced request against the same fixture. |
| BD `POST /portfolioreporting/api/performance/performanceSeries` | 63 dated points, cumulative TWR, value arrays and benchmark series. 26,918 bytes, 0.890 s. Last cumulative return and ending value exactly matched the corresponding period result. | One chart request, independent of the period call once scope/options are pinned. |
| Orion `POST /api/v1/Reporting/Scope` | One household plus two accounts; eight calculations per row: four valuation cells, three period returns, one daily breakdown. 92 daily points per row; 119,975 bytes, 2.484 s. | One batched calculation graph for summary, periods, chart and account rows. |

Timings are individual observations, not an SLA or a load benchmark. Counts exclude token renewal/search/membership operations. The BD specimen is one account in the supplied client-view capture, not a proven arbitrary multi-account relationship aggregation. Today's calls do not independently verify the separate 49F credential/tenant route; the earlier 49F implementation remains source evidence.

The BD token was renewed using the capture's own `GET /session/token` and session cookies. No alternate identity or tenant credentials were substituted. This proves the current session flow works; HAR credentials are not a production authentication design. Reuse the repository's tenant-specific credential mechanism for the eventual adapter.

### The Orion response-size experiment

The supplied screenshot's request has `returnStyle.cumulative=false` and a one-day range. Extending it to June 10–September 9, adding account grouping and QTD/YTD summaries worked. Setting `cumulative=true`, however, produced **4,278 rows per group with only 92 distinct date pairs**, repeated end dates, and individual factors that were not a single ready-to-plot cumulative series. Total response: **5,290,686 bytes**. That mode is rejected for the proposed chart based on this specimen; this is not a universal claim about all Orion return-style combinations.

Keeping `cumulative=false` produced **92 distinct daily rows per group**. Linking the vendor factors, `product(factor[0..i]) - 1`, produced the cumulative curve. Its final point matched the separate vendor period return in all **3/3 groups**, maximum absolute difference below `3.3e-13` in decimal-return units. This is presentation-level linking of vendor-calculated factors, not a valuation or TWR engine. Missing/null factors, duplicate dates or a mismatch must fail validation rather than be filled with zero.

## 4. The consolidated shape

One backend Lambda/service, with a BD adapter configured separately for 49F/Cottonwood and an Orion adapter for Inflection, emits a small view-model. The renderer does not receive raw recursive vendor responses. The logical shape below is proposed, not an existing route or deployed schema:

```typescript
type PerformanceReport = {
  version: 'performance.v1';
  reportRevision: string;
  scope: { scopeRef: string; accountSetHash: string; selected: number;
           returned: number; excluded: { accountRef: string; reason: string }[] };
  source: { provider: 'black_diamond' | 'orion'; asOf: string;
            fetchedAt: string; configurationVersion: string };
  method: { measure: 'TWR' | 'MWR'; fees: 'net' | 'gross' | 'unknown';
            valueBasis: string; providerOptionsRef: string };
  periods: { key: string; requestedStart: string; requestedEnd: string;
             returnedStart: string; returnedEnd: string }[];
  summary: ResultRow | null;       // Vendor aggregate for the selected set.
  accounts: ResultRow[];           // Unique, authorized accounts.
  series: { scopeRef: string; kind: 'cumulativeReturn';
            points: { date: string; value: number | null }[];
            basis: 'vendorCumulative' | 'linkedVendorFactors' }[];
  benchmarks: BenchmarkSeries[]; // Optional; identity and dates required.
  optional: { cashMovement: SectionState; valueHistory: SectionState };
};
// ResultRow: scopeRef, display label, currency, periodResults[].
// Each period result: beginning/end money values; decimal return; explicit
// cumulative/annualized/unknown basis; requested/returned dates; coverage.
// Each nullable metric has a status/reason. Zero is an observed value.
// SectionState: supported | unavailable | unverified, with reason/content.
```

Display labels come from the authorized directory or verified response mapping. Raw provider account IDs, cookies and options containing internal identifiers remain server-side. The shared envelope also supplies lifecycle/status, template/disclosure version and export binding specified in the parent design.

| Common field | Black Diamond mapping | Orion mapping / guard |
|---|---|---|
| Selected scope | `parameters.accountFilters.accounts`; returned account membership and one chosen hierarchy | `entity=5` household, exact `entityIds`, account-management overrides; grouping **5 Household / 7 Account**, evidenced by captured GroupingOptions. Never trust the browser to set membership. |
| Beginning / ending value | `levels[].dateRangePoints[].beginningMarketValue / endingMarketValue`, with accrual and value-basis metadata retained | `calculated-activity.value` matched to request `activityOption.valuationMethod` Beginning/Ending Market Value. Bond accrual is separately available; do not add it twice or assume provider bases equal. |
| Period return | `timeWeightedReturns.return` in decimal units; preserve `returnAnnualized` and `returnsAnnualized` metadata | `calculated-performance.performance` in decimal units. Match using group path + `$type` + calculation `id`, because summary and breakdown share an ID in the captured request. |
| Return chart | `seriesPoints.timeWeightedReturns.cumulatives[]` against corresponding `perfDates` / returned ranges | Daily breakdown `factor`; cumulative link as tested. Breakdown `performance` is in **percentage units**, so divide by 100 if used as a daily rate. `factor - 1` matched that conversion for all 276 daily points. |
| Period matching | Four request ranges; response dates, not a presumed name field. Validate the request association and returned dates. | Request graph gives each period calculation an ID; response start/end dates must also match. Preserve effective inception/coverage differences. |
| Benchmark | Native identity/type plus returned rates and cumulative series | Captured request has an empty benchmark list. Benchmark normalization is an optional capability pending an actual named benchmark specimen. |
| Money movement / gain | `netAdditions`, `netGains`, `fees`, `income`, optional activity-summary detail; selected three-month bridge reconciled | `cashFlowAmount`, intraday amounts, fees and dividends remain distinct. A common external-contributions mapping is **not certified** by this sample. |

BD `levels` and `combinedLevels` are alternate overlapping hierarchies: choose one traversal, not concatenation. Duplicate-account metadata and membership checks must survive normalization. Return aggregation belongs to the vendor; do not average account returns or use an account sum as a household return.

### A failed value-chart shortcut worth preserving

The tempting Orion expression `startValue + valueChange` matched the first and last dates but **failed all three rows on the middle sampled date**, compared against explicit Ending Market Value calculations. The check covered **nine cells: three dates × household/two accounts**. Largest discrepancy: **$210.68**. Dividend/intraday fields are present, and some apparent nonzero net-intraday values are floating-point residue. An ad hoc adjustment is not certified.

Therefore Orion's return breakdown is not treated as a dollar-value series. If a dollar chart becomes required, request native valuation points using a supported valuation-series shape or batched explicit valuation calculations and validate that route. Likewise `cashFlowAmount=0` does not establish that every form of cash/income movement is zero. The failed experiment is retained in the evidence, not hidden by choosing only the endpoint dates that matched.

## 5. The autosuggest seam with WS1

The Orion capture shows the exact two-step interaction Andrew described:

1. `GET /api/v1/portfolio/clients/simple/search/{query}` returns **30 suggestions** in the observed query, including label, ID, active state and rep-code fields.
2. After selection, `GET /api/v1/Portfolio/Clients/{id}/PortfolioTree` returns registrations/accounts plus portfolio-group membership. The selected fixture contains **two distinct accounts**; tree appearances must be deduplicated. Value and inception fields are null in parts of the tree, so the tree is not evidence of a populated report-value cache.

Use this interaction pattern with our existing silver data: build a slim firm directory, resolve advisor/tag visibility on the server, serve name suggestions and selected-account context from that cache, then make performance calls after selection. Zero vendor requests per keystroke. A restricted advisor receives only their authorized results; firm-wide access follows verified policy. Query matching and Orion rep-code fields alone are not an authorization policy.

The search row needs a display name, an opaque relationship key, a disambiguator and cached account count. Selecting it resolves the explicit deduplicated account set, provider mapping and coverage. Cache identity data by source revision, permissions by current entitlement revision. Account closure does not automatically remove the right to view historical reporting; access revocation must take effect independently of a warm directory cache.

Existing partner-specific mapping questions from the parent design remain: 49F Schwab household versus native BD IDs, Inflection representative bindings, and Cottonwood's actual advisor/firm policy. This investigation demonstrates the UX and API seam; it does not claim live silver population or entitlement joins were tested.

## 6. What is established, and what the build still needs

Established here: successful live BD period/series calls; successful Orion household/account batching; field-level return units; matched summary/chart returns; one practical small Orion response; actual autosuggest/membership sequence; and a concrete reason to keep derived Orion dollar charts out of the first common view.

Still required before claiming all-partner parity: 49F tenant execution; BD exact multi-account selected-set aggregate; Orion account-exclusion behavior for restricted or narrowed household scope; accrual/currency and long-period annualization fixtures; missing-history and partial-coverage cases; benchmark and cash-movement variants if included; production credential lifecycle/rate limits; UI/PDF identity checks. Today proves one BD account and one Orion household/two-account specimen, not every firm, client or method.

Next product decision is the proposed common core in §1. Broader endpoint/deployment approval is not implied by Andrew reviewing that layout. WS3/YCharts and WS4/model overlays remain separate workstreams within the same project.

## 7. Reproduction and review checks

**Subsequent export direction:** Andrew supplied BD part 3 and its 15-page PDF and requested a standard advisor-brandable report with a full-width narrative arc. The [export/narrative specification](investor-reporting-export-narrative-spec-20260910.md) and [four-page synthetic PDF](../research/investor_reporting_export_20260910/performance-export-review.pdf) now define that proposal using the deck-generation Opal brand assets. They refine the original sketch's basic print treatment. Dashboard remains the default; narrative generation belongs to export/preview and uses the reviewed performance revision. This follow-up inspected local captures and historical-source code; it made no further vendor calls or live historical-data queries.

The source manifest fingerprints the three HARs, four screenshots and saved probe, and records all nine HTTP receipts plus value-free response field/type paths. HAR entry indices are zero-based: BD part 2 token 92, activity summary 109/110, performance 114/117; Orion grouping options 231, suggestions 238/241, selected tree 246, Scope 252. BD part 1 dashboard requests 48/51/52 establish the firm-dashboard distinction.

`probe_performance.py --input-dir <Downloads> --output-dir <repository>/.runtime/codex-seats/4.0.0_SA_CRO/performance-recon` profiles without network calls. The explicit `--live` modes preserve the bounded experiments: `orion-compact`, `orion-daily`, `orion-value-check`, `bd-refresh`. Live flags are tooling, not standing authorization; this report records the current investigation only. The value-check mode depends on the saved daily response. Raw outputs are restricted to the ignored repository runtime directory; token response bodies are never saved. The initial exact replays were performed before the reusable tool was written and are preserved as separate receipts, not falsely attributed to that tool.

Verification: BD period/series return and ending-value equality; Orion summary versus linked-factor parity in 3/3 groups; percentage/factor unit parity across 276 daily points; rejected dollar-value shortcut in 3/9 cells. The standalone sketch was exercised in installed Edge through Playwright: period switching updates values/table/chart, three account-table rows render, no JavaScript page errors, no horizontal overflow at a 390-pixel viewport, and a local review PDF was produced. Desktop and mobile screenshots were visually inspected. This verifies a synthetic review artifact, not the portal integration or production PDF workflow.

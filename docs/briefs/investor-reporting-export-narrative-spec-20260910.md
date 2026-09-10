# Performance Reporting: branded PDF and narrative arc

**Author:** 4.0.0_SA_CRO · September 10, 2026 · RCN-0008 / WS1–WS2

**Parent:** [Lightweight Investor Reporting](investor-reporting-lightweight-brief-20260910.md), one project/four workstreams. This adds an export capability to the [performance presentation proposal](investor-reporting-performance-review-20260910.md).

**Direction:** [Andrew's verbatim instruction](../../org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260910_PERFORMANCE_EXPORT_NARRATIVE.md). Dashboard is the default; Export produces a purpose-designed report. Andrew will provide high-definition advisor logos.

**Status:** Proposed specification and synthetic PDF prototype for review. No production generator, historical coverage census, vendor report execution or report distribution is claimed in this follow-up.

**Shared-export dependency, September 10 WS3 follow-up:** the [YCharts child design](investor-reporting-ycharts-design-20260910.md) reuses the brand assets and export lifecycle described here. Its three generation routes are captured, but the HARs omit PDF bodies and the upload multipart request. Native YCharts section/tab/PDF parity therefore still requires paired Overview, Comparison and Multi-Comp output fixtures and verified section extraction. A working performance PDF template does not close that Analysis-export dependency. WS2's performance/narrative content and permanent endpoint numbering remain separate.

## 1. The product

An advisor selects a client, account scope and period, reviews the dashboard, then chooses **Export report**. A small options panel offers advisor branding, the market-narrative page and optional detail sections. The advisor previews the rendered report and downloads its PDF. The export contains the performance result already reviewed; a change of period, account scope or performance methodology first creates a new report revision.

Use one standard **landscape letter** template, proposed at 11 × 8.5 inches. Its wide page supports the narrative chart and readable account tables. Core page order:

| Page | Content |
|---|---|
| Report overview | Selected client, advisor/firm identity, period/as-of, beginning and ending value, period return, concise period comparison and scope/coverage. This can serve as the cover without an otherwise empty cover page. |
| **The period in context** | Full-width cumulative-return chart; maximum-drawdown interval and selected movement markers; a handful of dated topic annotations with short supporting context and source references. |
| Performance detail | Native provider account/relationship results, dates, fee/return basis, benchmark when verified, and optional validated cash-movement sections. Paginate long tables with repeated headings. |
| Methods and sources | Relevant performance methodology, coverage gaps, narrative evidence dates/sources, market-context distinction, approved provider/firm disclosures and report provenance. Keep footnotes beside the claims they qualify. |

Optional holdings/model appendices consume WS4's existing contract when selected and available. They do not silently become required for a performance-only export. YCharts remains Analysis. No vendor instructional page, empty target-allocation placeholder, or unsupported section is carried into a finished report merely because the vendor template contains it.

The [four-page prototype](../research/investor_reporting_export_20260910/performance-export-review.pdf) demonstrates this page order using **synthetic performance and fictional topic fixtures**, with real Opal brand assets. It is not a client report or an analysis of actual historical events.

## 2. Branding is a generation option

The template consumes the actual [Opal brand guidelines](../../deck_generation/brand/opal_brand_guidelines.pdf), [machine-readable brand specification](../../deck_generation/brand_spec/brand.json) and existing logo package. Use Opal Navy `#163372`, Midnight Blue `#0A1733`, Cool Grey `#C4CBDB`, restrained Electric Purple `#5F3BE3`, white backgrounds and Lato. Charts use direct labels and shape/line distinctions as well as color. Keep vector charts and selectable text in the PDF.

The official Opal logo remains horizontal, preserves its aspect ratio and has the specified 0.5x clear zone. Use the full-color logo on light backgrounds and the appropriate knockout version on dark backgrounds. Advisor branding changes the configured identity/assets, not the report's data or method. Preserve approved attribution/disclosures under every mode.

Proposed generation options:

```text
branding.mode              opal | advisor | co_branded
branding.advisorProfileRef  verified advisor name, title, firm, contact information
branding.logoAssetRef       optional approved high-definition logo + asset version
branding.logoVariant        approved light/dark variant
includeNarrative            enabled in the proposed standard template
includeAccountDetail        enabled in the proposed standard template
optionalSections            verified benchmark, cash movement, holdings/models
```

**Logo input owner: Andrew.** High-definition advisor logos are pending his delivery. Prefer vector SVG/PDF assets, with high-resolution transparent PNG accepted after checking effective resolution at the intended printed size. The generation function supports selecting a stored advisor asset or supplying an approved asset reference; it does not scrape a logo or upscale a screenshot automatically. Store each asset under its verified firm/advisor scope with provenance, checksum, version, dimensions and clear-space requirements. Validate/sanitize image assets during ingestion, including SVG external references. Do not fetch an arbitrary logo URL while rendering a report.

Until an advisor logo is provided, the standard Opal template can render with advisor text and an explicit preview indication that no advisor logo is selected. A requested advisor-branded export cannot silently claim that branding was applied if its required asset is missing. The prototype's advisor placeholder is a design annotation, not a fabricated advisor logo. No logo upload is needed to review this specification.

Brand-source details: the guide's navy HEX value is consistent with `brand.json`; its printed blue-channel RGB value appears inconsistent, so use the HEX value. The guide labels h1 as **48px**, while the extracted JSON says 48pt. The prototype follows 48 CSS pixels (36 PDF points) for the principal title and records smaller page/table styles explicitly. It does not silently treat these units as equivalent. Production export packages Lato locally; the deck engine's PPTX font enforcement is useful precedent but does not validate a separate HTML/PDF renderer.

## 3. What the new Black Diamond capture establishes

The new HAR contains **139 entries**. The supplied PDF contains **15 landscape pages**; all 15 pages were text-extracted, rendered and viewed. Selected report-package fields and page-design structures were inspected; credentials and raw client data remain outside committed artifacts.

| Captured step | Evidence and implication |
|---|---|
| Template catalogue and designs | `GET /request/report/template/`, `/template/{id}`, `/report/design/`, and report-type settings. Templates comprise ordered cover/commentary/standard designs, charts, tables, orientation and settings. |
| Branding/runtime configuration | `/request/report/firmconfiguration` exposes `allowBrandingOption` and other controls; `/type/settings/runtime` provides runtime choices. These are evidence of separate template/configuration concerns, not our product's required option list. |
| Package generation | HAR entry **130**, `POST /request/report/package`, sends the selected template, date range, portfolio scope and additional settings. The selected template contains **nine page designs**. |
| Captured response | HTTP 200 returns a package with **status `Queued`, 0% complete and size 0**, plus account membership and sharing flags. This is job acceptance, not a completed PDF. Sharing flags are false in this specimen. |
| Supplied PDF | Its filename matches the returned package ID. Its 15 pages expand the nine designs through table pagination. This associates the artifacts; the HAR does **not** contain the completed polling/download chain or a matching downloaded-PDF response hash. |

The PDF's sections are cover, commentary-upload instructions, portfolio overview, portfolio-account summary, class/segment detail, actual/target allocation, four holdings pages, account overview, and four gain/loss pages. Some returns are explicitly unavailable because the account was not held for the entire period. Preserve this meaning in our template; a plotted or available since-inception return does not make a YTD return complete.

Architectural lesson: separate **data snapshot + template/branding + render job + output**. Opal can render this standard format from normalized BD or Orion data, regardless of whether Orion offers a comparable branded export screen. These supplied Orion references do not establish that Orion has no export capability elsewhere. No Black Diamond template save, package POST or sharing operation was replayed for this follow-up.

## 4. Narrative arc: select the performance events first

The full-width page answers: **What happened to the selected portfolio, and what market themes were being discussed around those dates?**

Start with the verified, dated, cumulative **TWR** series for the selected scope. With cumulative return `C[t]`, define the linked growth index `W[t] = 1 + C[t]`, including the correct period-start baseline. Running peak `P[t] = max(W[0..t])`; drawdown `D[t] = W[t] / P[t] - 1`. The lowest drawdown identifies the maximum-drawdown trough; retain its preceding peak and first subsequent recovery to that peak, if any. Label it **maximum drawdown within the selected period and available series**. A cash deposit changing account value is not itself performance or a drawdown recovery.

Use native daily data before any visual downsampling. Never apply this formula to annualized observations, a money-weighted-only series, account dollar values, or an average of account returns. Source/method changes, missing observations and late inception remain explicit. Duplicate dates/nonfinite values require resolution; gaps cannot become zero returns. Without a usable series, show the performance tables and an explicit narrative-page limitation.

Proposed event-selection policy:

1. Always evaluate the maximum-drawdown episode, including peak/trough and recovery status. A flat or monotonic series does not receive an invented drawdown.
2. Evaluate sharp negative and positive moves over declared observation windows, plus recoveries. Rank by magnitude and a versioned, history-aware materiality rule.
3. Merge overlapping candidates into episodes and enforce spacing so adjacent days in one selloff do not become several purported independent events.
4. Select a small page-sized set, proposed **three annotations by default**, while retaining the candidate list and exclusion reasons. The layout may accommodate more after review. Event windows, significance thresholds and spacing are configuration to calibrate on actual report histories, not arbitrary acceptance targets in this brief.
5. Freeze selected events before fetching news. A dramatic headline cannot manufacture a portfolio turning point, and missing news cannot erase the measured maximum drawdown. Manual changes in preview retain the measured event and an edit trail; quantities remain read-only derived facts.

The chart marks the peak-to-trough interval and recovery, where present. Each annotation names a date/range, measured movement, a short theme and a restrained paragraph. Prefer a few readable labels over embedding a dense word-cloud image on the chart. The cloud supplies candidate phrases and prominence, while articles supply support.

## 5. Historical evidence retrieval

Repository source inspection found the following paths. They establish storage/access mechanisms, **not a live count of almost a year's complete history**. Before production use, measure earliest/latest dates, expected versus present dates, duplicate runs, missing source timestamps and usable article coverage per requested window.

| Signal | Inspected source | How the narrative uses it |
|---|---|---|
| **Trending Topics — primary** | `portal-proxy.ts::getTrendingTopics` calls `/api/general/trending/topics/{date}`; `portal_data_proxy::get_trending_topics` queries `opal-news-trending-daily` by date. `news_layer3_curation::write_to_dynamodb` persists enriched dated topic rows. | Query only the selected event windows. Preserve original keyword/topic identity, rank/category, article count, analysis, embedded articles and their publication dates. Page through source queries where required. |
| **Topic Cloud — primary** | `news_trending_analysis::save_report_to_s3` writes `s3://opal-data-news-v2/trending_reports/YYYY/MM/DD/trending_report_HHMMSS.json`, then produces `opal-data-portal-v2/json/sentiment/keyword-sentiments.json`. | Read date-partitioned archived reports. Preserve `generated_at`, `analysis_window_days`, true mention counts, scores and sample articles. The archive is written **before** balanced selection, sports/stopword filtering, size normalization and final validation; it is not automatically the exact final cloud shown that day. |
| Keyword drilldown / article evidence | `keyword_drilldown_generator` uses `opal-news-articles`, a default 14-day window and per-keyword summary/article singletons. `sentiment.ts` exposes these current snapshots. | Current 14-day files cannot supply an arbitrary prior-year event. Prefer article references in the dated archive/topic record; otherwise query the event's dated article population. Empty history is missing evidence, not neutral sentiment. |
| Best/Worst Performers | Market Overview performance sources and price-history-dependent APIs, alongside the existing market-data domain. Historical universe and exact ranking snapshots still need certification. | Optional market-breadth context. Keep universe, window and observation dates. Do not call market winners/losers the client's contributors without historical portfolio attribution. Recomputed rankings require the historical universe or an explicit reconstruction label. |
| RSI | `useRSIValues` consumes tiered summary/details; `market.ts` supplies typed price/history-derived data. | Use dated raw indicator observations and their actual calculation window, not today's percentile or the UI fallback of 50. Preserve asset-class/universe scope. |
| Regime | `market.ts::getMarketRegimeHistory`: `json/market/market-regime-history.json`, `timeSeries` for momentum/volatility/correlation/rate regime plus `regimeHistory`. | Add a concise date-aligned context fact when supported. Store the classifier/method version and whether historical labels were reconstructed. Source comments about history length are not a measured coverage guarantee. |
| Fear & Greed | `sentiment.ts` consumes `json/sentiment/fear-greed-index.json` with historical composite values and optional component histories. | Use the dated composite/description; keep raw component metrics distinct from the 0–100 composite. Never export the accessor's synthetic neutral fallback as observed data. |

Two source traps matter. The current trending publisher derives display sentiment values of `+0.6/-0.6` from bullish/bearish categories; these are **not measured sentiment strength**. The client helper that approximates a keyword with the first word of a headline is also unsuitable for historical phrase identity. Use the original dated source fields and evidence, preserving their method/version.

### Time alignment and phrase selection

Each event has an explicitly defined market-session timezone and cutoff. A context window can include preceding sessions and the selected episode, but cannot silently include later news. Filter article publication timestamps against the declared cutoff, deduplicate syndicated/duplicate articles and preserve true counts. Do not sum overlapping seven-day rolling-window counts across daily archives.

Choose among same-day archival runs by the declared cutoff and actual `generated_at`/analysis window, not by lexical filename alone. The inspected archive writer uses a runtime-local `datetime.now()` for the path; the path date is not proof of an Eastern market-session date. If only later reconstruction exists, label it as reconstruction from dated source material. If a final cloud snapshot exists with a stable object version, retain it separately from the pre-filter archive. Re-running today's GPT/stopword logic on old articles is not proof of what the historical UI displayed.

Rank phrases using preserved topic identity, recorded rank/prominence, meaningful changes against comparable prior windows, usable article support and breadth. Count and size are distinct: cloud display size is normalized for legibility. Fetch bullish and bearish context without forcing it to agree with the portfolio's sign. Preserve conflicting signals and neutral observations. Optional signals enrich a selected event when relevant; they do not each require their own paragraph.

An evidence packet contains event dates/return facts, source records and hashes/versions, window definitions, source and publication timestamps, phrase/rank/count/score semantics, cited article metadata, coverage and exclusions. News text is untrusted source content, not instructions to the generator. It cannot direct the renderer, select another client or alter performance facts.

## 6. Narrative generation and report contract

Use a deterministic evidence builder followed by constrained prose generation, or templated prose where sufficient. The language model receives only the permitted event facts and evidence packet. It returns structured annotations with evidence IDs. Quantities, dates and references are verified against those inputs before rendering. It must not invent a topic, article, sentiment observation, benchmark or causal explanation to fill a slot.

Write “During this drawdown, coverage focused on …” or “The recovery coincided with …” when supported. A claim that a theme **caused this client's loss** requires separate attribution evidence; coincident headlines alone do not establish it. Historical holding/exposure evidence would be required to personalize the market context into a portfolio-driver explanation. This feature can be useful without making that stronger claim.

Proposed logical function and stored revision:

```typescript
generatePerformanceExport({
  performanceReportRevision,
  templateRef,
  branding: { mode, advisorProfileRef?, logoAssetRef? },
  sections: { narrative: true, accounts: true, optional: [] },
  narrativePolicyRef
}) -> { exportId, status, previewRef?, pdfRef? }

// Internal immutable bundle:
// authorizedScope + normalizedPerformance + selectedEvents + datedEvidence
// + validatedNarrative + brandAssets + template + disclosures + rendererVersion.
// Each input has a version/hash. Preview and PDF consume that same bundle.
```

Keep the performance data revision distinct from the export revision: changing a logo or narrative text creates a new export revision without changing the provider result. Reauthorize on preview and PDF download, even for a cached output. The cache key includes scope/permission checks, performance revision, sections, brand/profile assets, template/disclosure versions, narrative policy, evidence versions and prose/model/prompt version where used. One advisor's logo/contact details cannot leak into another advisor's export through a client-only cache key.

The logical export job resolves verified inputs, detects events, batch-loads the bounded historical windows, builds/validates narrative, renders print HTML/SVG to PDF, then exposes a protected preview/download. Reuse the approved Opal brand assets/specification; keep rendering in a worker if measured duration requires it. A logical function need not force provider calls, historical retrieval and browser rendering into one long Lambda invocation. Existing dashboard use remains fast because this work begins at export/preview, not during client search.

PDF generation does not call the provider again to recalculate the report. Render retries reuse the same bundle. A failed/partial narrative stage leaves verified performance intact and reports its coverage explicitly; the user may choose a performance-only export. Requested narrative content is never silently replaced by present-day headlines. Generation does not email, share with a vendor portal or distribute the PDF automatically.

## 7. Workstream ownership and proof

**WS1 owns** the export options/preview interaction, branding profile/asset binding, standard page template, renderer, job/download authorization and shared lifecycle. **WS2 owns** performance content/method normalization, event detection, dated market-evidence adaptation, narrative validation and source/coverage metadata. Existing news/market producers remain source owners; **WS4** supplies optional holdings/model appendices. This is a WS1–WS2 capability within the same project, not a fifth project or an unowned shared task.

Proof cases for implementation:

- A hand-calculated drawdown fixture identifies the correct prior peak, trough and recovery; an unrecovered episode remains unrecovered; a flat series with a large deposit creates no return event.
- Duplicate/missing dates, inception gaps, annualized input and mismatched report scope cannot silently produce a valid narrative curve. Downsampling preserves all selected extrema/markers.
- An event before available news history stays explicit; a later article and today's cloud cannot contaminate its context. Same-day duplicate runs and overlapping rolling windows do not multiply counts.
- All annotated facts and references resolve to the frozen evidence packet. A planted unsupported causal sentence is rejected. Conflicting bullish/bearish evidence survives selection.
- Switching advisor/firm assets changes only the authorized export branding; missing, low-resolution or wrong-scope assets have visible outcomes. Long names, varied logo aspect ratios and optional sections fit without clipping.
- Preview and downloaded PDF agree on period, account set, quantities, method, selected events, narrative text and branding revision. Fonts embed, vector charts remain sharp, footnotes/links remain legible, and repeated table headings/page breaks are exercised.

The current offline prototype verifies the page concept, basic event mathematics and rendering with synthetic inputs. Historical coverage, live source permissions, date-vintage fidelity and end-to-end production export remain implementation evidence to collect. No new numerical latency or narrative-accuracy acceptance target is invented here.

## 8. Evidence and reproduction

[Source manifest](sources/INVESTOR_REPORTING_EXPORT_NARRATIVE_EVIDENCE_20260910.json) fingerprints supplied HAR/PDF, brand sources, inspected code and prototype inputs. Capture indices are zero-based: templates 77/78/108, firm/runtime settings 128/129, package 130. HAR packet inventory and PDF inspection are offline; no client identifiers or raw payloads are committed.

[Prototype generator](../research/investor_reporting_export_20260910/build_export_review.py) emits the synthetic print template and PDF. It uses the repository's official Opal logo and local Lato font files. Lato assets for this review were obtained from the [official Google Fonts repository](https://github.com/google/fonts/tree/main/ofl/lato); their source hashes and [license](../research/investor_reporting_export_20260910/FONT_LICENSE.txt) are retained. This asset retrieval is separate from vendor reporting: no BD/Orion report endpoint was called during this follow-up.

The [offline capture profiler](../research/investor_reporting_export_20260910/profile_export_capture.py) reproduces the value-minimized HAR/PDF inventory and source fingerprints. Reproduction uses Python, PyMuPDF, Playwright, installed Microsoft Edge and local Lato Regular/Light/SemiBold files at the recorded hashes. It does not install fonts or packages, fetch client data or send a report job.

```powershell
python docs/research/investor_reporting_export_20260910/build_export_review.py --font-dir <local-Lato-directory> --output <review.pdf>
```

`--no-narrative` demonstrates the performance-only option; `--advisor-name` and `--advisor-logo` demonstrate trusted local review inputs. Production asset ingestion and authorization are specified above, not implemented by this offline fixture builder.

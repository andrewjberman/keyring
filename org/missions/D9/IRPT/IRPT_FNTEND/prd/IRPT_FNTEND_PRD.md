# IRPT_FNTEND -- Investor Reporting frontend: the advisor-facing product, its three tabs, the branded export, the Global view, and design conformity with the portal

```json
{
 "project": "IRPT_FNTEND",
 "directive": "D9",
 "fabric": "laptop",
 "prd_version": "v0.1",
 "step": 4,
 "brief_ref": "docs/briefs/investor-reporting-ir-fe-brief-20260910.md@2acf23d8fd",
 "endpoint_outcomes": ["FWD-1", "FWD-3", "FWD-4", "FWD-5", "FWD-6", "FWD-8", "FWD-11", "FWD-12"],
 "status": "RATIFIED"
}
```

Brief: `docs/briefs/investor-reporting-ir-fe-brief-20260910.md` @`2acf23d8fd`, 35,392 bytes, 25 sections + 9 mapped sources. Counterpart: `IRPT_BCKEND` (`org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md`). Endpoint of record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FWD_IRPT_FNTEND_20260910.md`. Two projects, two decompositions, two task-order sets, two adjudications; no cell is jointly owned. This project OWNS the grade on all eight outcomes below. Five of them cross (FWD-3, 4, 5, 8, 11): each grade reads this project's view AND the counterpart's data, parity, entitlement or execution half; a frontend mock cannot close that half. The browser consumes normalized, authorized contracts only; it never connects to a vendor session and never decides which accounts an advisor may see.

## ENDPOINT (step 2, /endpoint --forward)

```
  FWD-1  An advisor finds an authorized client and opens its relationship and accounts without waiting for a vendor report
         DONE WHEN  EXERCISED -- an advisor who has never used the workspace has searched, selected, and been shown the relationship and its permitted accounts
         ACCEPT     from the header, a search by client name returns an unambiguous selection; the workspace immediately shows the relationship, its permitted underlying accounts, cached context and the directory's as-of; the choice survives a tab switch; an unmapped client stays VISIBLE to an authorized viewer with an explicit capability gap rather than silently missing
         PROOF      a fixture directory carrying duplicate names, an account-only entry and multiple relationships, compared against the expected authorized set; cold and warm timings recorded against the whole captured firm-directory denominator; VENDOR REQUEST COUNT DURING SEARCH IS ZERO. No latency target is invented at L2
         OWNER      IRPT_FNTEND.  CROSSES: IRPT_BCKEND supplies the permitted account set, the directory as-of, the zero-vendor-request guarantee
         CONSTRAINT terminated clients STAY VISIBLE, marked terminated, with actual available dates; a backend rejection or revoked permission clears protected content; frontend role labels are not permissions; opening Holdings never silently turns a selected client into a whole book
         PIN        58266dab2d

  FWD-3  An advisor reads the provider's performance result in an Opal report and exports the same result
         DONE WHEN  EXERCISED -- a captured provider response has been carried to a rendered view and a PDF at one report revision, for each supported partner and scope
         ACCEPT     for the selected account or relationship and period, vendor-calculated performance appears in a common Opal layout and the PDF carries the SAME scope, returned dates, values, method basis, source attribution and approved disclosures; the UI distinguishes TWR/MWR, net/gross, cumulative/annualized, UNITS and UNAVAILABLE fields; a deliberately incomplete provider mapping yields a PARTIAL or UNSUPPORTED result rather than a full-client claim
         PROOF      compare captured request/response, normalized report, rendered view and PDF at one revision per partner and scope; relationship return uses a VENDOR CALCULATION for the exact selected account set -- summing or averaging account returns is not a substitute and a fabricated aggregate fails this outcome
         OWNER      IRPT_FNTEND.  CROSSES: IRPT_BCKEND supplies canonical meaning, UNITS, dates, the vendor-calculation-only rule and the certified fixture this view is graded against; the PDF runs in the counterpart's worker
         CONSTRAINT this project never recalculates a return, never parses a raw provider hierarchy, never infers gain from ending minus beginning value, never averages account returns into a household return, never treats missing data as zero; a benchmark or value-history section appears only when the contract marks it supported; refresh and export are distinct acts; TWR/net/YTD are the design's proposed defaults, never a rewrite of a returned method
         PIN        58266dab2d

  FWD-4  An advisor obtains a YCharts sensitivity analysis in the same client context and exports it
         DONE WHEN  EXERCISED -- an approved report variant has been replayed from an analyst-approved input through its captured request/job/result chain to the tab and the PDF
         ACCEPT     the advisor selects a supported variant, reviews the holdings or saved-portfolio mapping and comparison model it will use, and receives an Opal-branded analysis and matching PDF preserving the input snapshot, configuration, data dates, limitations and vendor attribution; a MODELED comparison is described as modeled; unsupported variants are VISIBLE as unsupported
         PROOF      replay each approved variant end to end
         OWNER      IRPT_FNTEND.  CROSSES: IRPT_BCKEND supplies the chain from validated input through captured request, job and result to a certified section, and the release state behind "unsupported VISIBLE as unsupported"
         CONSTRAINT the request arrives by EMAIL (FWD-9, the counterpart's); a correction submits a new input revision, never overwrites the evidence; the correction UI imposes no universal analyst approval; an embedded vendor PDF is an intermediate preview, not completion; stage evidence shown without invented progress percentages; each native section compared to its paired vendor-output fixture before it is called supported; the 0.30% annual fee is the current recorded setting; NO LIVE VENDOR CALL is authorized by this document
         PIN        58266dab2d

  FWD-5  An advisor sees current holdings organized by models, with the underlying securities and unassigned assets preserved
         DONE WHEN  EXERCISED -- dated holdings and model snapshots have been replayed for all three registry client firms
         ACCEPT     the view starts at the model breakdown and drills into accounts and securities; ACTUAL CUSTODY HOLDINGS REMAIN THE TOTAL-VALUE BASIS; SmartX (49F), Eclipse (INF) or BD Rebalancer (COT) supplies the overlay; target weights, actual sleeve values and inferred estimates are DISTINCT; missing attribution stays VISIBLE without double-counting or redistributing the residual
         PROOF      replay across all three firms including an unassigned account, an unmatched join, a blended model and a multi-relationship membership; UNIQUE UNDERLYING HOLDINGS RECONCILE BEFORE AND AFTER THE OVERLAY; coverage and join exceptions carry DENOMINATORS
         OWNER      IRPT_FNTEND.  CROSSES: IRPT_BCKEND supplies join correctness, the reconcile control, the denominators and the revision-bound nodes this view draws
         CONSTRAINT every slice states its value basis and denominator; percent of parent and percent of total shown distinctly; actual sleeve securities and model target constituents are different drill destinations; partial allocations never squeezed to 100%; unknown classification never shown as Client; absolute values never hide short or negative positions; signed/zero/unknown denominators get the backend-defined alternative state; no holdings time series in v1
         PIN        58266dab2d

  FWD-6  An advisor can keep working when one report is unavailable, and can tell the age of each result
         DONE WHEN  EXERCISED -- a provider has been deliberately failed and a client switched mid-request, with no response landing on the wrong selection
         ACCEPT     client selection and silver-backed holdings stay usable when a provider is slow or down; each tab distinguishes LOADING, READY, STALE, PARTIAL, UNAVAILABLE and FAILED; a late response for a PREVIOUS selection CANNOT populate the current client's tab; cached reports keep their original as-of and revision
         PROOF      delay or fail one provider, switch clients during an outstanding request, expire a cache entry, and complete jobs OUT OF ORDER
         OWNER      IRPT_FNTEND.  CROSSES: IRPT_BCKEND supplies the StatusEnvelope states and the as-of / revision each result carries
         CONSTRAINT retryable, uncertain and needs-correction states are also shown where applicable; a scope switch clears the prior client's data immediately and checks returned selection/revision before display; an over-age directory or revoked grant follows the backend response even against a warm cache; no cookies, raw provider ids or infrastructure diagnostics in the client workflow; an incomplete result never appears as a complete zero-valued report
         PIN        58266dab2d

  FWD-8  An advisor exports a BRANDED Opal report whose narrative page states what was happening in the market at the account's dramatic moves -- as CONTEMPORANEOUS CONTEXT, never as a cause of the return
         DONE WHEN  EXERCISED -- a KNOWN drawdown window has been replayed against the dated topic history and the same inputs selected the SAME inflection points twice
         ACCEPT     the dashboard stays the DEFAULT view and the export is a separate act; the export renders the Opal template from the deck-generation brand guidelines at the SAME performance revision the advisor reviewed, with advisor logo and information as an OPTIONAL input; the narrative page shows the performance time series and, at the max drawdown and other dramatic moves, the Trending Topic and Topic Cloud terms DATED TO THAT WINDOW, with the other sentiment signals as supporting context; inflection-point selection is DETERMINISTIC -- the same series and the same history select the same moments, every run
         PROOF      replay one known drawdown window twice and diff the selected moments; replay a window that PREDATES the news history and confirm it renders MISSING HISTORY rather than an empty topic list
         OWNER      IRPT_FNTEND -- the Opal template, the export options and modals, dashboard-stays-default, the narrative page's composition, MISSING HISTORY rendered as such, preview-to-PDF parity.  CROSSES: IRPT_BCKEND is the lambda -- deterministic inflection selection, dated evidence and prose validity, the frozen bundle, execution of this project's RenderPackage
         CONSTRAINT the artifact must SAY it is contemporaneous context and never assert, imply or rank causes; MISSING HISTORY IS AN ANSWER, NOT AN EMPTY STATE; NOT A BI SURFACE; the high-definition advisor logos are PENDING INPUT, neither invented nor scraped, and a missing logo never blocks the report; preview and PDF bind the same data, narrative, template, disclosure, renderer and asset revisions; a branding edit creates an export revision without re-fetching performance; Analysis exports use their own certified section layout and do not inherit the performance narrative; optional holdings appendices reuse the holdings contract and create no separate required Holdings report; landscape-letter proposal: overview, full-width period-in-context page when selected and supported, performance detail, methods/sources
         PIN        58266dab2d

  FWD-11 An Opal user can run reports and analysis on ALL firms from one Global view, the way Model Portfolios already does it
         DONE WHEN  EXERCISED -- an Opal user has opened the global view, picked a client at a second firm, and run a report and an export
         ACCEPT     someone at Opal, signed in as Opal rather than as any firm, can pick any client from any firm and use every tab and export on them; a firm's advisor can never reach that view or see a second firm through it; the global view shows the same numbers that firm's own advisor would see for that client, never a recomputed or blended one; which firm each result belongs to is always visible
         PROOF      an Opal user opens the global view, selects clients at two different firms, runs a report and an export on each; replay the same requests as a firm advisor and confirm refusal; compare the global-view figures to the firm-scoped figures for the same client and revision
         OWNER      IRPT_FNTEND -- the view, the firm selector, the always-visible firm attribution.  CROSSES: IRPT_BCKEND supplies the cross-firm entitlement class and the `api/scoped/` routes
         CONSTRAINT the firm dropdown is the SAME PATTERN AS MODEL PORTFOLIOS -- Global (All) plus the actual partner firms -- fixed, not a build choice; a firm advisor cannot enter Global through a URL, saved state or altered selector; a firm switch clears the prior selection and protected content before another response can display; Global introduces no blended calculation and never rebinds an email request to another firm
         PIN        2dcd88091f

  FWD-12 The Investor Reporting screens look and behave like the rest of the Opal portal, so an advisor who already uses the portal needs no re-learning
         DONE WHEN  EXERCISED -- an advisor who already uses another portal page has used all three tabs and the export without being shown anything new to learn
         ACCEPT     the page is built from the portal's own header, tabs, client search box, category tree, model colours, panels and brand -- not look-alikes made for this project; the firm dropdown is the Model Portfolios one; an advisor who knows another portal page finds the same controls in the same places doing the same things; the screen and the exported report share one brand; it works at a narrow width
         PROOF      a census of EVERY component the page uses against the portal's existing component set, denominator printed -- each is REUSED from a named existing path or is NEW with a stated reason a reviewer can dispute; a review against the brand guidelines and the brand spec; the Model Portfolios firm dropdown REUSED, not rebuilt; the narrow-viewport exercise the brief's sketch already ran, repeated on the real page
         OWNER      IRPT_FNTEND.  IRPT_BCKEND is NOT ENGAGED
         CONSTRAINT a new component requires a stated need the existing set cannot meet; matching appearance alone is not reuse; accessible table equivalents for every chart; modals, previews and exports carry the same brand as screens
         PIN        5c18c88826
```

## CELL CANDIDATES

One row per candidate cell. The decomposition at L5 is the COO lane's and may split, merge or re-sequence these; every brief section a row consumes is cited by heading so the coverage map can be checked against it.

| cell | serves | brief sections consumed | contracts consumed (C) / produced (P) | paths: reuse | paths: new home | fixtures / evidence | acceptance clause draft |
|---|---|---|---|---|---|---|---|
| F1 route + page identity + navigation entry | FWD-1, FWD-12 | O1; O8; IV.2 route row | -- | `portal/src/App.tsx` | `portal/src/pages/InvestorReporting/` | -- | a lazy route under current navigation conventions, distinct from BI/Positioning; the entry appears where an advisor expects a product entry |
| F2 header: shared header variant, firm dropdown (Model Portfolios pattern), client autosuggest, scope and directory dates | FWD-1, FWD-11, FWD-12 | O1; O7; O8; IV.2 header and combobox rows | C `DirectoryEntry`, `ResolvedScope` | `portal/src/components/PageHeaderVariants.tsx`; `portal/src/components/ui/PageSurfaceControl.tsx`; `portal/src/ui/components/panels/`; `portal/src/ui/components/catalyst/combobox.tsx`; `portal/src/pages/AdvisorIntelligence/_shared/panels/ClientListPanel.tsx`; `portal/src/pages/ModelPortfolios.tsx` (the dropdown pattern) | `portal/src/pages/InvestorReporting/` | fixture directory: duplicate names, account-only entry, multiple relationships, terminated-but-entitled | name search returns an unambiguous selection with a useful discriminator; permitted population, scope and directory dates shown; account selection narrows the relationship; zero vendor calls per keystroke; the dropdown is the Model Portfolios component reused |
| F3 tab navigation, selection persistence, scope-switch clearing | FWD-1, FWD-6 | O1; O6 scope-switch paragraph; IV.2 tabs row | -- | `portal/src/components/TabNavigation.tsx`; `portal/src/hooks/useTabNavigation.ts` | `portal/src/pages/InvestorReporting/` | -- | Reporting -> Analysis -> Holdings with accessible state and focus; switching tabs preserves the selection; a scope switch clears the prior client's data immediately and rejects a stale response by selection/revision |
| F4 Reporting tab: summary cards, cumulative-return chart, period results, account detail, method/coverage labels, presets and custom dates | FWD-3 | O2; IV.3 performance sketch; IV.4 | C `PerformanceReport` | `portal/src/ui/components/panels/` (summary cards) | `portal/src/pages/InvestorReporting/` | `docs/research/investor_reporting_performance_20260910/presentation-review.html`; `docs/briefs/sources/INVESTOR_REPORTING_PERFORMANCE_EVIDENCE_20260910.json`; the counterpart's certified fixtures for 49F BD, Cottonwood BD, Inflection Orion incl. partial scope, differing dates, unavailable metrics | beginning value, ending value, period return lead; actual returned dates, inception limits, currency, TWR/MWR, net/gross, cumulative/annualized, UNITS and UNAVAILABLE shown; benchmark/value-history only when supported; labels, units, chart endpoints and account rows match the certified fixture; no recalculation, no parsing of raw hierarchies; refresh is not export |
| F5 Analysis tab: three variants, request list, input review and correction, stage display, native sections | FWD-4 | O3; IV.1 S3/S8 rows | C `AnalysisRequest`, `AnalysisReport`, `StatusEnvelope` | -- | `portal/src/pages/InvestorReporting/` | YCharts field census; paired vendor-output fixtures (ACTUAL PDFs still missing -- proof gap) | Overview, Comparison, Multi-Comp with primary, ordered comparisons, holdings/input date, fee and settings, generation state; email-ingested requests and released revisions listed per client; inferred inputs inspectable; unresolved securities, grouping, substitutions and cover details correctable as a NEW input revision; stage/release evidence displayed without invented percentages; modeled vs actual distinction and section dates/disclosures preserved; a section is called supported only after its paired-fixture comparison |
| F6 Holdings tab: model-led radial drilldowns, category tree, legends, table equivalents, basis and denominator labels | FWD-5 | O4; IV.2 category-tree and radial rows | C `HoldingsSnapshot` | `portal/src/components/CategoryViewTree.tsx`; `portal/src/lib/modelPortfolioColors.ts`; `portal/src/pages/AdvisorIntelligence/_shared/AdvisorPublicProfile.tsx`, `_shared/components/PartnerAnalytics.tsx`, `_shared/tabs/DistributionTab.tsx` (radial precedents; do NOT inherit the absolute-value shortcut) | `portal/src/pages/InvestorReporting/` | model-overlay evidence fixture cases: observed SmartX allocation, Eclipse assignment, Cottonwood target blend, cash remainder, unknown category, duplicated relationship membership, stale overlay | starts at current value, unique account count, source dates, model coverage; drills Models / SMAs / Client / other categories into subtypes, models, accounts, securities with consistent model colours, breadcrumbs, direct labels and a readable table; every slice states basis and denominator; percent of parent and of total distinct; unassigned, unmapped and unclassifiable amounts distinguishable; summary and drill bound to one scope and revision |
| F7 per-tab lifecycle states, source ages, late-response rejection, recovery actions | FWD-6, FWD-1 | O6; IV.4 | C `StatusEnvelope` | -- | `portal/src/pages/InvestorReporting/` | controlled failure fixtures; out-of-order responses; expiry and revocation on a warm cache | each tab independently shows loading, ready, partial, stale, unavailable, retryable, uncertain, needs-correction and failed as applicable with actual source ages and next actions; a failed Analysis job does not erase holdings or lock search; a stale model map does not relabel old assignments as current; a late response for a previous selection cannot populate the current tab |
| F8 export options and modals: branding choices, narrative page toggle, account detail, optional sections, missing-asset experience, applied-branding display | FWD-8 | O5 first two paragraphs; O5 logos paragraph | C `ExportBundle` (preview), `ExportReceipt`, `StatusEnvelope` | -- | `portal/src/pages/InvestorReporting/` | -- | dashboard is the default and export is a separate act; options for Opal / advisor / co-branding, narrative page, account detail, supported optional sections; approved scoped asset references accepted; the standard Opal template works without a logo and the screen shows what branding was applied; a branding edit creates an export revision without re-fetching performance |
| F9 RenderPackage: standard template, print styles, chart/table layout, packaged fonts, print entry point, render fixtures | FWD-8, FWD-3, FWD-12 | O5; II.2 RenderPackage paragraph; IV.2 brand rows; IV.3 export artifacts | P `RenderPackage` | `deck_generation/brand/opal_brand_guidelines.pdf`; `deck_generation/brand_spec/brand.json`; `deck_generation/engine/brand.py`; the official logo SVG; `docs/research/investor_reporting_export_20260910/build_export_review.py` (prototype), `FONT_LICENSE.txt` | a reusable rendering package under the feature boundary with a print entry point the counterpart executes | `performance-export-review.pdf` (synthetic starting point, not a production report) | versioned package declaring supported schema/template versions, deterministic screen and print components, locally packaged licensed fonts and asset requirements, page options and fixtures; HEX and CSS-pixel/PDF-point distinctions honoured; landscape-letter template per O5; used for on-screen preview and the counterpart's server-side render alike |
| F10 narrative page composition: wide chart, backend-supplied markers and dated annotations, footnotes, MISSING HISTORY rendering | FWD-8 | O5 template paragraph; II.1 narrative row | C `NarrativePacket` | `portal/src/components/market-performance/MarketRegimeIndicator.tsx`, `SentimentGauge.tsx`; `portal/src/hooks/useRSIValues.ts`; `portal/src/pages/MarketPerformance/panels/SentimentPanel/SentimentPanel.tsx` (visual vocabulary only; no live-market dashboard) | `portal/src/pages/InvestorReporting/` | export/narrative evidence | the page places the counterpart's drawdown/movement markers and dated annotations on the curve and never selects events from headlines or invents causal text; every quoted fact and reference comes from the frozen bundle; a window predating the news history renders MISSING HISTORY, never an empty topic list; the page states it is contemporaneous context |
| F11 Global view: Global (All) + partner firms in the firm dropdown, cross-firm client selection, visible firm attribution on every result, review and export | FWD-11 | O7; IV.2 (Model Portfolios pattern) | C `ResolvedScope` (permitted-firm catalogue) | `portal/src/pages/ModelPortfolios.tsx`; `portal/src/components/ui/PageSurfaceControl.tsx` | `portal/src/pages/InvestorReporting/` | -- | an entitled Opal user finds clients across firms, selects one, and uses all three tabs and export in that client's firm context; firm attribution visible everywhere; a firm advisor cannot reach Global by URL, saved state or altered selector; a firm switch clears prior selection and protected content before another response displays; identical figures for the same client and revision in Global and the firm's own view |
| F12 typed client and transport: contract consumption, response handling, no protected stale display, telemetry without client payloads | FWD-2 (contrib), FWD-6, FWD-1 | II.2 handoff contracts; O6; IV.2 API-access row | C all eleven contracts | `portal/src/api/portal-proxy.ts`; `portal/src/api/endpoints/market.ts`, `sentiment.ts`, `trending.ts` (transport and date/status conventions) | `portal/src/api/endpoints/investor-reporting.ts` | negative integration fixtures (swapped ids, revoked grant vs warm cache) | a rejection or revocation clears protected content; permission states honest; no cookies, raw provider ids, infrastructure diagnostics or client payloads in telemetry; no vendor cookies, model joins, news retrieval or email parsing in these modules |
| F13 design conformity: component census, brand review, narrow-viewport exercise on the real route | FWD-12 | O8; IV.2 whole table; IV.4 | -- | every path in IV.2 | -- | `docs/research/investor_reporting_performance_20260910/presentation-review.html` (the narrow-viewport exercise, Edge) | inventory of every component the page uses with the total printed; each REUSED from an exact path or NEW with a reviewable reason; screen and export reviewed against the brand sources; narrow-viewport exercise repeated on the real route |
| F14 consumer fixtures: one representative success/failure fixture per contract, shared with the counterpart | all crossing outcomes | II.2 (contract changes need matching producer/consumer fixtures); V | C all | -- | under the feature boundary beside the render fixtures | -- | each contract has a consumer fixture the counterpart's producer fixture is paired with; a contract change without both is refused |

## CONTRACTS

Consumed from the counterpart, whose PRD carries the field definitions (its II.3 inventory of eleven). This project owns formatting, accessible rendering and interaction; it never redefines a contract's meaning, units or dates. One contract is produced here.

| contract | direction | cells |
|---|---|---|
| `DirectoryEntry` | consumed | F2 |
| `ResolvedScope` | consumed | F2, F11, F12 |
| `PerformanceReport` | consumed | F4 |
| `AnalysisRequest`, `AnalysisReport` | consumed | F5 |
| `HoldingsSnapshot` | consumed | F6 |
| `NarrativePacket` | consumed | F10 |
| `ExportBundle`, `ExportReceipt` | consumed | F8 |
| `StatusEnvelope` | consumed | F7, F12 |
| `RenderPackage` | **produced** | F9 |

## PATHS

| kind | path | cell | use (from IV.2) |
|---|---|---|---|
| reuse | `portal/src/App.tsx` | F1 | add the entry under current lazy-route/navigation conventions; distinct from BI/Positioning |
| reuse | `portal/src/components/PageHeaderVariants.tsx`; `portal/src/components/ui/PageSurfaceControl.tsx`; `portal/src/ui/components/panels/` | F2, F4, F11 | shared header, panels, summary cards, page controls |
| reuse | `portal/src/components/TabNavigation.tsx`; `portal/src/hooks/useTabNavigation.ts` | F3 | tabs, accessible state/focus, existing navigation instrumentation |
| reuse | `portal/src/ui/components/catalyst/combobox.tsx`; `portal/src/pages/AdvisorIntelligence/_shared/panels/ClientListPanel.tsx` | F2 | option/virtual-list and client-drill conventions against the counterpart's viewer-scoped directory |
| reuse | `portal/src/pages/ModelPortfolios.tsx` | F2, F11 | the firm-dropdown pattern (Global (All) + firms) |
| reuse | `portal/src/components/CategoryViewTree.tsx`; `portal/src/lib/modelPortfolioColors.ts` | F6 | registered child structure, unavailable states, canonical model colours; no independent taxonomy or palette |
| reuse | `portal/src/pages/AdvisorIntelligence/_shared/AdvisorPublicProfile.tsx`; `_shared/components/PartnerAnalytics.tsx`; `_shared/tabs/DistributionTab.tsx` | F6 | donut/card/drill presentation; the absolute-value shortcut is NOT inherited |
| reuse | `portal/src/api/portal-proxy.ts`; `portal/src/api/endpoints/market.ts`, `sentiment.ts`, `trending.ts` | F12 | typed transport and date/status conventions; historical narrative data comes from the counterpart, not these current-page fallbacks |
| reuse | `portal/src/components/market-performance/MarketRegimeIndicator.tsx`, `SentimentGauge.tsx`; `portal/src/hooks/useRSIValues.ts`; `portal/src/pages/MarketPerformance/panels/SentimentPanel/SentimentPanel.tsx` | F10 | visual vocabulary for optional dated context; no new live-market dashboard |
| reuse | `deck_generation/brand/opal_brand_guidelines.pdf`; `deck_generation/brand_spec/brand.json`; `deck_generation/engine/brand.py` | F9, F13 | Opal colours, logo clear-space, Lato, packaging precedent; HEX and CSS-pixel/PDF-point distinctions |
| reuse | `deck_generation/brand/logo_package/Opal-Capital-Logo-Package/Full Logo/Full Color/Opal-Capital-Logo-Full-Color.svg` | F9 | trusted Opal asset; advisor assets arrive through the counterpart's scoped ingestion |
| new | `portal/src/pages/InvestorReporting/` | F1-F8, F10, F11 | page, tab and review components |
| new | `portal/src/api/endpoints/investor-reporting.ts` | F12 | the typed client |
| new | a reusable rendering package under the same feature boundary, with a print entry point | F9 | executed by the counterpart's export worker; packaging follows the portal's actual build and deployment constraints and shared-path ownership |

## FIXTURES AND EVIDENCE

| artifact | cell | proves / limits |
|---|---|---|
| `docs/briefs/sources/INVESTOR_REPORTING_FE_BK_SPLIT_EVIDENCE_20260910.json` | all | path existence; nine source hashes |
| `docs/research/investor_reporting_performance_20260910/presentation-review.html`; `docs/briefs/sources/INVESTOR_REPORTING_PERFORMANCE_EVIDENCE_20260910.json` | F4, F13 | synthetic layout/interaction reference exercised in Edge incl. narrow viewport; dated API units and parity findings; does NOT prove portal integration |
| `docs/research/investor_reporting_export_20260910/performance-export-review.pdf`, `build_export_review.py`, `FONT_LICENSE.txt`; `docs/briefs/sources/INVESTOR_REPORTING_EXPORT_NARRATIVE_EVIDENCE_20260910.json` | F8, F9, F10 | four-page synthetic PDF, visual/print starting point, not a production client report |
| `docs/briefs/sources/YCHARTS_COMPARISON_REPORT_FIELD_SCRAPE_20260909.json`; `INVESTOR_REPORTING_YCHARTS_HAR_EVIDENCE_20260910.json`; `INVESTOR_REPORTING_YCHARTS_SOURCE_EVIDENCE_20260910.json` | F5 | section vocabulary, request choices, remaining fixture requirements; captured downloads omit PDF bytes so native section parity is UNRESOLVED |
| `docs/briefs/sources/INVESTOR_REPORTING_MODEL_OVERLAY_EVIDENCE_20260910.json`; `INVESTOR_REPORTING_LIGHTWEIGHT_EVIDENCE_20260910.json` | F6, F2 | coverage/availability fixture cases; inspected component fingerprints; real partial/stale states still required |

## BRIEF COVERAGE

Denominator: 25 sections of the brief at `2acf23d8fd` + 9 source documents = **34 entries**. Every entry maps to a cell and outcome or carries `NOT CONSUMED` with its reason. Unmapped entries: **0**.

| # | entry | consumed by | outcome |
|---|---|---|---|
| 1 | title / preamble (ownership paragraph; Reporting -> Analysis -> Holdings; split changes ownership not meaning) | F1, F12 boundaries; every cell's CROSSES | all |
| 2 | PART I heading | structural | -- |
| 3 | O1 right client, context across tabs | F1, F2, F3, F7 | FWD-1 |
| 4 | O2 clear performance report, provider's meaning intact | F4 | FWD-3 |
| 5 | O3 YCharts analysis in the same client context | F5 | FWD-4 |
| 6 | O4 holdings through model-led radial drilldowns | F6 | FWD-5 |
| 7 | O5 branded report matching the reviewed revision | F8, F9, F10 | FWD-8 |
| 8 | O6 partial, stale or failed results; continue | F7, F3, F12 | FWD-6 |
| 9 | O7 Opal user across all firms from the Global view | F11, F2 | FWD-11 |
| 10 | O8 familiar components and consistent design | F13, F2, F3, F6, F9 | FWD-12 |
| 11 | PART II heading | structural | -- |
| 12 | II.1 two teams with explicit ownership | every cell's CROSSES column; the ownership paragraph above | all |
| 13 | II.2 handoff contracts | CONTRACTS table; F9 (RenderPackage), F12, F14 | all |
| 14 | II.3 scope retained and scope deferred | constraints on F4 and F6 (cohort controls only for supported classifications; unknown is not false; no conflation with Holdings' Client partitions); the NOT-COMMISSIONED list (no Positioning redesign, no BI replacement, no MP rewrite, no new engine, no vendor retirement, no holdings history, no trade entry, no auto distribution) read against every cell | all |
| 15 | PART III qualitative bar | the ACCEPT lines of the ENDPOINT section | all |
| 16 | PART IV heading | structural | -- |
| 17 | IV.1 nine source documents | entries 27-35 below | all |
| 18 | IV.2 existing frontend and brand paths | PATHS table; F1, F2, F3, F6, F9, F10, F11, F12, F13 | FWD-1, 3, 5, 8, 11, 12 |
| 19 | IV.3 review artifacts and evidence | FIXTURES table; F4, F5, F6, F8, F9 | FWD-3, 4, 5, 8 |
| 20 | IV.4 measured findings relevant to FE | F13 (narrow-viewport repeat on the real route); F5 (PDF parity unresolved); F6 (real partial/stale states required); acceptance reads "synthetic fixtures cannot close end-to-end product acceptance" | FWD-4, 5, 12 |
| 21 | IV.5 required detail coverage in the frontend PRD | this table | -- |
| 22 | PART V what must be true | F14 + the dependency register: counterpart contracts and fixtures incl. narrowed relationship behaviour and termination vs revocation; paired YCharts PDFs and section schemas before native rendering is accepted; taxonomy/cohort/attribution bases from the counterpart; brand/disclosure content and the RenderPackage available to the counterpart; both projects bind summary, drill, preview and export to one scope/revision and exercise the crossing proof; existing portal/auth/brand owners' integration procedures | all |
| 23 | PART VI status | NOT CONSUMED: not outcome-bearing; compilation clock and hashes carried by FIXTURES row 1 | -- |
| 24 | PART VII what this brief does not claim | NOT CONSUMED as work: bounds claims (no production frontend, no release policy, no export service, no fresh permission result, no native fidelity certified by assembly); read as the NOT-CLAIMED list against every cell's acceptance | -- |
| 25 | REFS TO CARRY | NOT CONSUMED as work: a link list; each referent is consumed through the entry that cites it | -- |
| 27 | S1 original unification brief | F1, F2, F4, F5 (distinct client-service surface, hierarchy/search, report transparency, cohort semantics, modeled-analysis distinction); broad replacement and history ambitions deferred | FWD-1, 3, 4 |
| 28 | S2 lightweight brief | F1-F8 (three-tab product, fast client context, view/export behaviour, lifecycle states) | FWD-1..8 |
| 29 | S3 YCharts brief | F5 (email-request visibility, input inspection/correction, three choices, recovery states, native analysis, released revisions) | FWD-4 |
| 30 | S4 holdings/model-overlay brief | F6 (advisor-scoped current view, taxonomy/radial drilldowns, basis/denominator/coverage labels; no time series) | FWD-5 |
| 31 | S5 lightweight design | F2, F3, F4, F8, F12 (header/tab/search components, selected-scope behaviour, normalized envelopes, same-revision export, source/code index) | FWD-1, 3, 6, 8 |
| 32 | S6 performance review | F4 (summary/chart/account layout, defaults to review, optional sections, autosuggest interaction, synthetic reference) | FWD-3 |
| 33 | S7 export/narrative specification | F8, F9, F10 (standard branded pages, optional advisor assets, wide narrative chart, freeze/preview/export rules, synthetic PDF); event/data algorithms are the counterpart's | FWD-8 |
| 34 | S8 YCharts design | F5 (request fields/settings, variant/cardinality/orientation, understandable lifecycle, native section schema, PDF fidelity gap); vendor execution is the counterpart's | FWD-4 |
| 35 | S9 model-overlay design | F6 (display-node contract, taxonomy/colours, signed values, percentage/drill rules, scope/revision-bound serving); partner joins are the counterpart's | FWD-5 |

(Entry numbering skips 26 so the source rows read S1..S9 as 27..35; the count is 25 + 9 = 34.)

## SURFACE MANIFEST

Surfaces this project writes, reads or executes. Nothing here is deployed by this document; packaging and deployment follow the portal's actual build constraints and shared-path ownership.

| surface | kind | cell | owner |
|---|---|---|---|
| `portal/src/pages/InvestorReporting/` | new code home | F1-F8, F10, F11 | IRPT_FNTEND |
| `portal/src/api/endpoints/investor-reporting.ts` | new typed client | F12 | IRPT_FNTEND |
| the rendering package under the feature boundary (print entry point) | new package, produced for the counterpart | F9 | IRPT_FNTEND; executed by IRPT_BCKEND's export worker |
| `portal/src/App.tsx` | edit (route entry) | F1 | existing portal owner's integration procedure |
| every IV.2 reuse path | read / import | F2, F3, F6, F9, F10, F11, F12, F13 | their existing owners; reuse never widens ownership |
| `deck_generation/brand/*`, `brand_spec/brand.json`, `engine/brand.py`, the official logo SVG | read | F9, F13 | brand owners |
| the counterpart's `/api/scoped/investor-reporting/...` routes | consume | F12 | IRPT_BCKEND |
| no vendor session, no vendor cookie, no model join, no news retrieval, no email parser | excluded | -- | -- |

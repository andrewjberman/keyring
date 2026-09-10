# IR FE — Investor Reporting frontend project brief

**Author:** 4.0.0_SA_CRO · **Date:** September 10, 2026 · **Mode:** NEW project brief consolidating existing research.  
**Project:** **IR FE**, one of Andrew's two requested projects. Its counterpart is [IR BK](investor-reporting-ir-bk-brief-20260910.md).  
**Canonical code:** `IRPT_FNTEND`, named by Andrew in the [five-message direction](../../org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260910_192xZ_FWD9_YES_FWD10_IMPOSSIBLE_BY_INGESTION_GATE.md) at `2dcd88091f`; the renamed [project endpoint](../../org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FWD_IRPT_FNTEND_20260910.md) carries it. IR FE remains the short name.
**Authority:** [Two-project instruction](../../org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260910_IR_FE_IR_BK_SPLIT.md), initial commit `6226b4a680`; [subsequent priority/device direction](../../org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260910_183xZ_IR_IS_THE_TOP_PROJECT_LAPTOP_AND_SPLITS_FE_BK.md), `c0f5ed8163`. **Both projects run on this laptop. Investor Reporting is the highest-priority work across the board.**  
**Consumer:** Andrew's product review; CTO's L2/PRD work; frontend delivery team and its backend counterpart.  
**Organization:** These two briefs supersede the earlier one-project/four-workstream organization. WS1–WS4 remain source labels in the older documents, not a third umbrella project. Andrew subsequently named **IRPT** as the macro in **D9** ([carried direction](../../org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260910_183xZ_MACRO_IS_IRPT_REGISTER_IN_D9.md), `1f0f1dd3f6`). The single `OPAL_INVRPT` code request was withdrawn by CTO; Andrew has named `IRPT_FNTEND` and `IRPT_BCKEND`, superseding the withdrawn longer codes; register bookkeeping remains with its owner. Andrew has also moved **D9 as a whole to laptop** ([subsequent D9 placement direction](../../org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260910_185xZ_D9_TO_LAPTOP_CLDGRPH_FINISHED_15MIN_RATIFIED.md), `4ff4abd9a4`); MSTR owns the register update. This closes the placement/write-ownership question. These briefs do not close other projects.

**IR FE owns the entire advisor-facing Investor Reporting experience:** the route, shared header and client selector, all three tabs, assumptions/input correction views, charts and tables, report preview, branding options and the reusable PDF presentation package. **IR BK owns every ingestion path, authoritative scope decision, calculation/normalization, data projection and execution service behind it.** The browser uses normalized, authorized Opal contracts; it does not connect to vendor sessions or decide which accounts an advisor may see.

This is the lightweight product already described: **Reporting → Analysis → Holdings**. Performance remains vendor-calculated; Analysis remains YCharts; Holdings is current snapshot only. The project split changes ownership, not the meaning of the numbers or the feature set. Every one of the four source briefs and five supporting documents is mapped to this team's responsibilities in Part IV.

# PART I — THE OUTCOME TERRITORY

### O1 — An advisor finds the right client and keeps that context across the three tabs

The advisor enters Investor Reporting as a distinct portal product, uses the header's name/account search and opens an unambiguous client, relationship or account. The header displays the permitted account population, a useful discriminator, scope and directory dates. Account selection can narrow the relationship. Switching tabs preserves the selection. Search and basic context are available before a vendor report completes.

The proposed opening scope remains the selected client within the advisor's permitted population; a supported, authorized advisor-book/firm selector may expose the same hierarchy explicitly. Do not silently turn a selected client into an entire book when opening Holdings. Entitled terminated clients stay visible, marked terminated, with actual available dates. A backend rejection or revoked permission clears protected content; frontend role labels are not permissions.

**Proof:** exercise duplicate client names, direct account entry, a partly authorized relationship, a terminated-but-entitled client, keyboard navigation and a client switch during an outstanding request. The UI displays precisely the returned authorized scope, rejects stale responses and triggers no vendor call per keystroke. Source: S1 O1/O6; S2 O1/O2; S5 §§1–2; S6 §5.

### O2 — An advisor reads a clear performance report with the provider's meaning intact

Reporting leads with beginning value, ending value and period return, then a cumulative-return chart, period results and compact account detail. Offer YTD/presets/custom dates and show actual returned dates, inception limitations, currency, TWR/MWR, net/gross and cumulative/annualized basis. TWR/net-of-fees and YTD remain the source design's proposed defaults, not permission to rewrite a returned method.

A verified provider benchmark or cash/value-history section appears only when the backend contract marks it supported. Do not infer investment gain from ending minus beginning value, draw a dollar-value chart from an unverified shortcut, average account returns into a household return or treat missing data as zero. Performance generates after valid selection of the active tab; refresh is distinct from export.

**Proof:** render the same normalized contract for 49F BD, Cottonwood BD and Inflection Orion fixtures, including partial scope, differing returned dates and unavailable metrics. Compare labels, units, chart endpoints and account rows to IR BK's certified fixtures. The FE renderer neither recalculates return economics nor parses raw provider response hierarchies. Source: S2 O3; S6 §§1, 3–4, 6.

### O3 — An advisor obtains and reviews the requested YCharts analysis in the same client context

Analysis offers **Overview, Comparison and Multi-Comp**, with the primary portfolio, ordered comparison selections, holdings/input date, fee/settings and generation state. It shows email-ingested requests and available report revisions for the selected client. An authorized advisor or analyst can inspect inferred inputs and correct unresolved securities, account grouping, proposed substitutions and cover details. Corrections submit a new input revision rather than overwriting the evidence.

Clear validated inputs can proceed automatically under the carried proposal. The correction UI does not impose universal analyst approval. Display the newer workflow's 0.30% annual fee correctly, preserve vendor-returned settings and the distinction between modeled analysis and actual performance, and keep section-level dates/disclosures. Render certified sections in Opal components. An embedded vendor PDF is an intermediate preview, not completion of the native Analysis product.

**Proof:** exercise all three variants, comparison order, dollar/weight distinctions, cash, ambiguous share classes, unsupported holdings, a recoverable session interruption and an uncertain submission. Display backend stage/release evidence without invented progress percentages. Compare native sections to paired vendor-output fixtures before calling a section supported. Source: S1 O4/F-M; S2 O4; S3 O1–O6; S8 §§3, 5, 7–8.

### O4 — An advisor reads current holdings through model-led radial drilldowns

Holdings starts with current value, unique account count, source dates and model coverage. Reuse the existing taxonomy to drill through Models, SMAs, Client and other applicable categories into subtypes, registered models/strategies, accounts and securities. Use pie/donut/radial charts with consistent model colors, breadcrumbs, direct labels and a readable table equivalent. V1 has no holdings time-series view.

Every slice identifies its value basis and denominator: observed custody value, observed allocation value, assigned-account value or target attribution. Show percent of parent and percent of total distinctly. Actual sleeve-held securities and model target constituents are different drill destinations. Unassigned, unmapped and classification-unavailable amounts remain distinguishable. Do not squeeze partial allocations to 100%, turn unknown classification into Client or use absolute values to hide short/negative positions. Signed/zero/unknown denominators receive the backend-defined alternative table/summary state.

**Proof:** drill an observed SmartX allocation, an Eclipse account assignment and a Cottonwood target-based blend, plus a cash remainder, unknown category, duplicated relationship membership and stale overlay. Summary and drill remain bound to one scope/revision and retain all qualifiers. Source: S1 O2/O5; S2 O5; S4 O1–O5; S9 §§1–2, 6–8.

### O5 — An advisor previews and downloads a branded report that matches the reviewed revision

The dashboard is the default. Export opens options for Opal/advisor/co-branding, the performance narrative page, account detail and supported optional sections. FE owns the standard template, print styles, chart/table layout and renderer package, reused for on-screen preview and the backend-executed PDF render. BK resolves authorized inputs/assets, runs the job and protects the output.

The performance template uses the landscape-letter proposal: overview, a full-width **period in context** page when selected and supported, performance detail, and methods/sources. FE places the backend-supplied drawdown/movement markers and dated annotations on the curve; it does not select events from headlines or invent causal explanations. Analysis uses its certified section layout and appropriate orientation with the same brand system; it does not inherit the performance/news narrative automatically.

Andrew will supply high-definition advisor logos. The generation options accept approved scoped asset references; the standard Opal template and advisor text work without a logo. FE shows what branding was actually applied. Missing logos do not block the report. Preview and PDF bind the same data, narrative, template, disclosure, renderer and asset revisions. Branding edits create an export revision without re-fetching performance. Optional holdings/model appendices reuse the holdings contract and do not create a separate required Holdings report product.

**Proof:** compare preview and downloaded PDF for each report type, with and without advisor assets/narrative. Exercise long names, varied logo ratios, long tables, missing narrative history and partial sections; check embedded fonts, clear labels, page breaks, footnotes and accessible equivalents. All quoted facts/references come from the frozen bundle. Source: S1 O3/O4; S2 O3/O7; S6 §7; S7 §§1–2, 4, 6–8; S8 §7.

### O6 — An advisor understands partial, stale or failed results and continues using the rest of the product

Each tab has independent loading, ready, partial, stale, unavailable, retryable, uncertain and failed states as applicable. Show actual source ages and understandable next actions. Input correction, safe refresh, resumed work and selecting a previous released revision are distinct actions. A failed Analysis job does not erase holdings or lock client search; a stale model map does not relabel old assignments as current.

A scope switch clears the prior client's data immediately and checks returned selection/revision before display. An over-age directory or revoked grant follows BK's response, including when FE has cached content. Preserve provenance and method/coverage notes in both the screen and export without exposing cookies, raw provider IDs or infrastructure diagnostics in the client workflow.

**Proof:** use controlled failure fixtures and out-of-order responses, including expiry/revocation on a warm cache. Confirm unaffected functions remain usable and incomplete data never appears as a complete zero-valued report. Source: S1 O9; S2 O6; S3 O4/O6; S4 O5; S5 §§1.2, 6.

### O7 — An entitled Opal user runs reports across all firms from the Global view

Use the **same firm dropdown pattern as Model Portfolios** in the Investor Reporting header: Global (All) plus the actual partner firms. An authenticated Opal user with BK's explicit Global entitlement can find clients across firms, select a client and use Reporting, Analysis, Holdings and export in that client's firm context. Firm attribution stays visible on every result, review and export. A firm advisor cannot enter Global through a URL, saved state or altered selector.

FE owns the Global view and FWD-11 acceptance; BK supplies and proves the cross-firm entitlement and scoped execution. A firm switch clears the prior selection and protected content before another response can display. The same client and revision produce the same figures in Global and the firm's own authorized view. Global does not introduce a blended performance calculation or allow rebinding an existing email request to another firm.

**Proof:** an entitled Opal user selects clients at two firms and runs reports/analysis and exports on each; equivalent firm-advisor requests cannot obtain Global access; compare identical revisions and exercise a firm switch with late responses. Source: Andrew's later five-message direction at `2dcd88091f`, FWD-11. This requirement arrived after the nine-source synthesis and is now folded into the FE brief.

### O8 — An advisor finds familiar portal components and consistent design throughout the product

Build the header, tabs, client search, category tree, model colors, cards and radial drilldowns from the existing components named in IV.2. Reuse the Model Portfolios firm-dropdown pattern. Keep controls in consistent places and apply the same Opal brand across screens, modals, previews and exports, including usable narrow-width layouts and accessible table equivalents. New components require a stated need that the existing set cannot meet; matching its appearance alone does not establish reuse.

**Proof:** inventory every component used by the implemented page, print the total, and identify each as reused from an exact repository path or new with a reviewable reason. Review the screen/export against the brand sources and repeat the narrow-viewport exercise on the real route. FE owns this design requirement and its review. FWD-12 is now **ratified**, following Andrew's agreement to the full block at `5c18c88826`. Its component census, brand review and real-route narrow-viewport proof are unchanged. BK is not assigned work on FWD-12.

# PART II — WHERE THE BOUNDARY SITS

### II.1 Two teams with explicit ownership

| Concern | IR FE owns | IR BK owns |
|---|---|---|
| Entry, search and context | Route, header, combobox, selection state, scoped navigation and displayed capabilities | Directory ingestion/projection/search service, identity resolution, permitted account set and refresh/expiry |
| Global firm selection | Opal-only Global/firm dropdown, visible firm attribution and selection/reset experience | Explicit Opal entitlement, permitted firm catalogue, selected-firm resolution and scoped route enforcement |
| Multi-tenant access | Correct response handling, no protected stale display, UI permission states and negative integration fixtures | Authentication integration, firm/advisor/account authorization, tenant credential routing, server/storage enforcement, revocation |
| Performance | Controls, summaries, charts, tables, method/coverage presentation | BD/Orion retrieval, return units/method normalization, exact-scope aggregate, report revision |
| Analysis | Variant/comparison/input-review UI, request history/status, native sections | Mailbox intake, parsing, mapping, YCharts sessions/generation, section extraction, validation/release state |
| Holdings | Radial/category presentation, drill UI, legends/tables and coverage display | Custody/assignment/position joins, canonical taxonomy application, denominators and reconciliation |
| Branding | Options, layout, supplied-profile display and missing-asset experience | Asset ingestion/sanitization, verified firm/advisor binding, versioned protected storage |
| PDF | Shared template/rendering component package, print entry point, layout and visual parity | Export API, frozen bundle, queue/worker/browser runtime, protected asset resolution, receipts/storage/download authorization |
| Narrative | Wide chart composition, annotation/footnote placement and supported edit/preview interactions | Event detection, dated sentiment/news retrieval, evidence/prose validation and revised narrative bundle |
| Operations | Product error/recovery views and frontend telemetry without client payloads | Schedules, retries, leases/checkpoints, secrets/IAM/KMS, logs, data lineage, runtime deployment and release manifests |

Server-side rendering does not move template ownership to BK: BK executes the versioned FE rendering package. FE does not implement a second export job service, backend parser or authorization engine. Existing brand, authentication, taxonomy and source owners retain their shared files; these rows specify each project's integration work, not unilateral ownership of those libraries.

### II.2 Handoff contracts

IR BK Part II.3 is the common wire/data contract inventory. FE consumes `DirectoryEntry`, `ResolvedScope`, `PerformanceReport`, `AnalysisRequest`/`AnalysisReport`, `HoldingsSnapshot`, `NarrativePacket`, `ExportBundle`/`ExportReceipt` and `StatusEnvelope`. All carry explicit version/scope/revision/availability as appropriate. BK owns canonical identity, units, dates and business meanings; FE owns formatting, accessible rendering and interaction. Contract changes need matching producer/consumer fixtures and an explicit compatibility decision, not a copied frontend-only shape.

FE supplies a versioned **RenderPackage** to BK: supported schema/template versions, deterministic screen/print components, locally packaged fonts and asset requirements, page options and render fixtures. BK supplies the immutable **ExportBundle**, executes that package and returns a protected **ExportReceipt**. Provider retrieval and narrative generation happen before rendering. Render retries reuse the bundle; a preview is not allowed to silently call the vendor again.

The first eight FWD IDs remain unchanged; later directions add FWD-9/10/11. [Andrew's ownership/design correction](../../org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260910_192xZ_FWD9_YES_FWD10_IMPOSSIBLE_BY_INGESTION_GATE.md) at `68d8b16a91` supersedes the former ownership rule: **IRPT_FNTEND owns FWD-1/3/4/5/6/8/11/12; IRPT_BCKEND owns FWD-2/7/9/10.** Advisor-facing outcomes are adjudicated under FE, while BK supplies the required data, parity, join, entitlement and execution proof. An FE mock cannot close that proof. In particular, FE owns the branded report outcome even when BK runs its rendering worker. **FWD-12 design/component conformity is ratified at `5c18c88826`**, owned by FE with no BK engagement. This later status change brings FE to eight owned outcomes, all ratified. These are two projects, two decompositions, two task-order sets and two adjudications; shared contracts are handoffs rather than jointly owned cells.

### II.3 Scope retained and scope deferred

Preserve the original brief's independent supervision/billing concepts and its hierarchy in the contracts. Show cohort controls only for supported, authoritative classifications; unknown values are not false. Do not silently conflate those two axes with Holdings' alternative Client display partitions. Broad historical cohort reconstruction and every legacy full-book analytical view are not added to this lightweight v1 by the organizational split.

No Positioning redesign, Advisor Intelligence BI replacement, global Model Portfolios rewrite, new performance/scenario engine, vendor retirement, holdings history, trade entry or automatic report distribution is commissioned here. Positioning links can expose existing model characteristics. S1's vendor-replacement and later BI/agent ambitions remain future context with the dependencies named there.

# PART III — THE QUALITATIVE BAR

1. An advisor can prepare the supported client reports without navigating a vendor interface.
2. The same selected client, method, dates and revision are recognizable across the screen, preview and PDF.
3. A partial or inferred result reads as partial or inferred, even when its chart is visually polished.
4. The Analysis correction view explains the actual unresolved input and does not create unnecessary manual work for valid requests.
5. A model drill shows the client's evidenced holdings or assignment; it never substitutes a firm's model headline AUM.
6. Existing portal components and Opal branding make the three tabs feel like one product.
7. The frontend remains useful when one provider or overlay is unavailable, without showing another client's delayed result.

# PART IV — SUBSTRATE, SOURCE MAP AND FRONTEND PATHS

### IV.1 All nine source documents: what IR FE takes from each

| ID / source | Relevant sections | FE responsibility carried here |
|---|---|---|
| **S1 — [Original unification brief](investor-reporting-unification-brief-20260909.md)** | O1–O6, O9; Part II; F-A/F-C/F-H/F-M; Part VII | Distinct client-service surface, hierarchy/search, report transparency, cohort semantics, product boundaries and the YCharts modeled-analysis distinction. Broad replacement/history ambitions remain deferred. |
| **S2 — [Lightweight brief](investor-reporting-lightweight-brief-20260910.md)** | O1–O7; II.1; F1/F6 | The three-tab product, fast client context, all view/export behavior and independent lifecycle states. Its old single-project/WS ownership is replaced by this split. |
| **S3 — [YCharts brief](investor-reporting-ycharts-brief-20260910.md)** | O1–O6; Part II; F7 | Email-request visibility, input inspection/correction, three report choices, recovery states, native analysis and released revisions. |
| **S4 — [Holdings/model-overlay brief](investor-reporting-model-overlay-brief-20260910.md)** | O1–O5; II.1; F5; Part VII | Advisor-scoped current view, taxonomy/radial drilldowns, basis/denominator/coverage labels and no holdings time series in v1. |
| **S5 — [Lightweight design](investor-reporting-lightweight-design-20260910.md)** | §§1–2, 3.3, 4.3, 5.2, 6–7 | Existing header/tab/search components, selected-scope behavior, normalized envelopes, same-revision export and source/code index. |
| **S6 — [Performance review](investor-reporting-performance-review-20260910.md)** | §§1–2, 4–7 | Concrete summary/chart/account layout, defaults to review, optional sections, autosuggest interaction and synthetic interactive reference. |
| **S7 — [Export/narrative specification](investor-reporting-export-narrative-spec-20260910.md)** | §§1–2, 4, 6–8 | Standard branded pages, optional advisor assets, wide narrative chart, freeze/preview/export rules and synthetic PDF reference. Event/data algorithms move to BK. |
| **S8 — [YCharts design](investor-reporting-ycharts-design-20260910.md)** | §§1, 3, 5.1, 6–8 | Request fields/settings, variant/cardinality/orientation, understandable lifecycle, native section schema and PDF fidelity gap. Vendor execution belongs to BK. |
| **S9 — [Model-overlay design](investor-reporting-model-overlay-design-20260910.md)** | §§1–2, 6–8 | Display-node contract, existing taxonomy/colors, signed-value handling, percentage/drill rules and scope/revision-bound serving. Partner joins belong to BK. |

Later dated findings qualify earlier claims: S6 closes part of the earlier performance capture gap; S3/S8 establish three YCharts routes while leaving PDF/section parity open; S4/S9 establish bounded live holdings joins. An older “not captured” sentence is not a current blanket blocker, and a newer successful fixture is not universal production proof.

### IV.2 Existing frontend and brand paths to use

Paths are repository-relative. These are reuse/integration sources, not newly assigned write locks. Existence is checked in the [split source/path manifest](sources/INVESTOR_REPORTING_FE_BK_SPLIT_EVIDENCE_20260910.json); source behavior is inherited from the dated nine-document research, not newly runtime-tested by this consolidation.

| Concern | Exact existing paths | Intended use |
|---|---|---|
| Route and page identity | `portal/src/App.tsx` | Add the Investor Reporting entry using current lazy-route/navigation conventions; keep it distinct from BI/Positioning. |
| Global selector precedent | `portal/src/pages/ModelPortfolios.tsx`; `portal/src/hooks/useAuth.ts`; `portal/src/components/ui/PageSurfaceControl.tsx` | Inspected partner list/state at lines 236–375 and header dropdown at 1251–1291: `PageSurfaceControl` uses `as="dropdown"`. Reuse the presentation pattern; BK supplies Global permission. The precedent's demo translation, development flags and missing-claim fallback do not grant Investor Reporting access. |
| Header and controls | `portal/src/components/PageHeaderVariants.tsx`; `portal/src/components/ui/PageSurfaceControl.tsx`; `portal/src/ui/components/panels/` | Shared header, panels, summary cards and page controls. |
| Tabs | `portal/src/components/TabNavigation.tsx`; `portal/src/hooks/useTabNavigation.ts` | Reporting → Analysis → Holdings, accessible state/focus and existing navigation instrumentation. |
| Client autosuggest | `portal/src/ui/components/catalyst/combobox.tsx`; `portal/src/pages/AdvisorIntelligence/_shared/panels/ClientListPanel.tsx` | Reuse option/virtual-list and client-drill conventions against BK's viewer-scoped directory. |
| Category tree and colors | `portal/src/components/CategoryViewTree.tsx`; `portal/src/lib/modelPortfolioColors.ts` | Registered child structure, unavailable states and canonical model colors; no independent taxonomy or palette. |
| Radial/drill precedents | `portal/src/pages/AdvisorIntelligence/_shared/AdvisorPublicProfile.tsx`; `portal/src/pages/AdvisorIntelligence/_shared/components/PartnerAnalytics.tsx`; `portal/src/pages/AdvisorIntelligence/_shared/tabs/DistributionTab.tsx` | Donut/card/drill presentation. Do not inherit the absolute-value shortcut identified in S9. |
| API access conventions | `portal/src/api/portal-proxy.ts`; `portal/src/api/endpoints/market.ts`; `portal/src/api/endpoints/sentiment.ts`; `portal/src/api/endpoints/trending.ts` | Existing typed transport and date/status conventions. Historical narrative data comes from BK, not these current-page fallback values. |
| Market-context visual references | `portal/src/components/market-performance/MarketRegimeIndicator.tsx`; `portal/src/components/market-performance/SentimentGauge.tsx`; `portal/src/hooks/useRSIValues.ts`; `portal/src/pages/MarketPerformance/panels/SentimentPanel/SentimentPanel.tsx` | Existing visual vocabulary for optional dated context. No new live-market dashboard is included. |
| Brand authority | `deck_generation/brand/opal_brand_guidelines.pdf`; `deck_generation/brand_spec/brand.json`; `deck_generation/engine/brand.py` | Opal colors, logo/clear-space, Lato and packaging precedent. S7's HEX and CSS-pixel/PDF-point distinctions apply. |
| Official logo package | `deck_generation/brand/logo_package/Opal-Capital-Logo-Package/Full Logo/Full Color/Opal-Capital-Logo-Full-Color.svg` | Trusted Opal source asset; advisor assets arrive separately from Andrew through BK's scoped ingestion. |

**Proposed new FE code homes, not existing implementation:** `portal/src/pages/InvestorReporting/` for page/tab/review components; `portal/src/api/endpoints/investor-reporting.ts` for the typed client; a reusable rendering package under the same feature boundary with a print entry point that BK can execute. Final packaging follows the portal's actual build/deployment constraints and shared-path ownership. Do not put vendor cookies, model joins, news retrieval or email parsers in these modules.

### IV.3 Review artifacts and evidence to carry

- [Performance interaction sketch](../research/investor_reporting_performance_20260910/presentation-review.html) and [performance evidence](sources/INVESTOR_REPORTING_PERFORMANCE_EVIDENCE_20260910.json): synthetic layout/interaction reference plus dated API units and parity findings.
- [Four-page branded PDF](../research/investor_reporting_export_20260910/performance-export-review.pdf), [prototype renderer](../research/investor_reporting_export_20260910/build_export_review.py), [font license](../research/investor_reporting_export_20260910/FONT_LICENSE.txt), and [export evidence](sources/INVESTOR_REPORTING_EXPORT_NARRATIVE_EVIDENCE_20260910.json): visual/print starting point, not a production client report.
- [YCharts comparison field census](sources/YCHARTS_COMPARISON_REPORT_FIELD_SCRAPE_20260909.json), [HAR evidence](sources/INVESTOR_REPORTING_YCHARTS_HAR_EVIDENCE_20260910.json), and [source evidence](sources/INVESTOR_REPORTING_YCHARTS_SOURCE_EVIDENCE_20260910.json): section vocabulary, request choices and remaining fixture requirements.
- [Model-overlay evidence](sources/INVESTOR_REPORTING_MODEL_OVERLAY_EVIDENCE_20260910.json) and [original lightweight source manifest](sources/INVESTOR_REPORTING_LIGHTWEIGHT_EVIDENCE_20260910.json): coverage/availability fixture cases and exact inspected component/source fingerprints.

### IV.4 Measured findings relevant to FE

Existing header/tab/combobox/panel and radial patterns are documented in S5/S9; a complete Investor Reporting route was not claimed by those inspections. S6's standalone synthetic interaction sketch was exercised in Edge, including a narrow viewport; S7's four-page synthetic PDF was rendered and reviewed. Neither proves portal integration. S8's captured report downloads omit actual PDF bytes, leaving native Analysis section parity unresolved. S9's source clocks and unmatched mappings require real partial/stale states. This project can develop against representative contracts while BK obtains missing output specimens, but synthetic fixtures cannot close end-to-end product acceptance.

### IV.5 Required detail coverage in the frontend PRD

The FWD summaries do not replace this brief or its nine underlying source documents. The frontend PRD must map **every section of this brief and all nine documents in IV.1** to the consuming FWD and implementation cell(s), or record **NOT CONSUMED with an explicit reason**. Print the denominator and identify every unmapped entry. An entry with neither a consumer nor a reason is a PRD defect. Carry the applicable fields, units, paths, design details, exceptions and proof requirements into the downstream work; linking a source without making its requirements available to the builder is insufficient.

The evidence manifest inventories the sections and nine sources as the starting denominator. It does not claim that a PRD or cell mapping exists. This is a coverage obligation, not a decomposition performed by this brief. FE's map covers FE work and names BK dependencies through the contracts; it does not combine the projects. Source: Andrew's seventh message and the endpoint coverage obligation at `68d8b16a91`.

# PART V — WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

These are dependencies, not a task sequence or task-order decomposition.

- IR BK provides the versioned contracts, representative success/failure fixtures and current authorization semantics in II.2, including narrowed relationship behavior and termination versus revocation.
- Paired YCharts PDFs and validated section schemas exist for each supported variant before native rendering is accepted. The three captured generation routes alone do not establish chart/table extraction fidelity.
- Canonical taxonomy/member identities, current cohort semantics and position-attribution bases are supplied by BK; frontend labels cannot repair missing source evidence.
- Approved brand/disclosure content and the FE render package are available to BK. Andrew's advisor logos are optional inputs with a working Opal fallback.
- Both teams bind summary, drill, preview and export to the same scope/revision and exercise the crossing proof. FE owns visual/interaction verification; BK owns source/economic/security verification; neither can certify the other half with its own mock.
- The implementation uses existing portal/authentication/brand owners' integration procedures. Register updates are carried by the named owners; IRPT/D9 and laptop execution, including the subsequent D9-wide move, are already directed.

# PART VI — STATUS — NOT OUTCOME-BEARING

This is a September 10 consolidation of the nine listed sources, authored after the 18:3xZ priority/device direction. The accompanying manifest records the exact compilation clock, all nine source hashes and path-existence results. The source investigations retain their own September 9–10 clocks; this turn does not remeasure live vendor, AWS or portal behavior.

The two-project direction initially committed at `6226b4a680`; subsequent laptop/priority context is linked above. This brief creates no route, API, resource, project register row, macro or task order. Delivery validation checks source coverage, local links, referenced path status, contract consistency and document structure. Publication is reported separately against measured `origin/CLOUD`.

# PART VII — WHAT THIS BRIEF DOES NOT CLAIM

No production frontend, automated release policy, export service, fresh permission result or native YCharts fidelity is certified by assembling these sources. Optional defaults remain identified as proposals. Original future ambitions are not silently promoted into lightweight v1. The older nine documents retain their evidence and source numbering; their one-project ownership is superseded by the two new briefs. Permanent FWD IDs and their formal ACCEPT assignment remain with CTO.

## REFS TO CARRY

```text
BRIEF          docs/briefs/investor-reporting-ir-fe-brief-20260910.md
PROJECT        IR FE / IRPT_FNTEND; code named by Andrew at 2dcd88091f; no third umbrella
COUNTERPART    docs/briefs/investor-reporting-ir-bk-brief-20260910.md
SOURCE MAP     Part IV.1, S1-S9; all four briefs and five supporting documents
PATH MAP       Part IV.2-IV.3; companion evidence JSON
EVIDENCE       docs/briefs/sources/INVESTOR_REPORTING_FE_BK_SPLIT_EVIDENCE_20260910.json
CONTRACTS      IR BK Part II.3; FE rendering package described in II.2
ENDPOINT       org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FWD_IRPT_FNTEND_20260910.md
PRIOR ENDPOINT org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FWD_INVESTOR_REPORTING_LIGHTWEIGHT_20260910.md (historical; distribution provenance)
SIBLINGS       IR BK; existing portal/authentication, D1 category/Positioning, D2 identity and brand owners
EXISTING PRD   New FE PRD is CTO-owned; older source PRDs are prior art, not this project's PRD
EXECUTION      Laptop, explicitly ruled; priority across the entire board
MEASURED AT    Compilation/path-check clocks in evidence; source clocks remain attached to their findings
```

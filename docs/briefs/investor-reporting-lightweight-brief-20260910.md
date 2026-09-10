# Lightweight Investor Reporting — L1 brief

> **Organization update, September 10, 2026:** Andrew has replaced the former project/workstream structure with two projects: [IR FE](investor-reporting-ir-fe-brief-20260910.md) for the complete client-facing product and [IR BK](investor-reporting-ir-bk-brief-20260910.md) for ingestion, tenant scoping, transformations and operations. Both briefs map all four source briefs and five supporting documents. The body below remains dated research; its former ownership labels are historical. Permanent FWD IDs are unchanged. Macro IRPT, directive D9, laptop execution.

**Author:** 4.0.0_SA_CRO (Chief Research Officer)  
**Home:** org/tier1_exec/4.0.0_SA_CRO/  
**Recon ID:** RCN-0008, downstream pilot brief  
**Mode:** NEW, one umbrella project under D9 Opal Workflows; four workstreams. Project code not assigned by this brief.  
**Commission:** Andrew-direct, September 10, 2026, this seat; [verbatim direction and clarification](../../org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260910_0919ET_LIGHTWEIGHT_INVESTOR_REPORTING.md).  
**Consumer:** CTO `/endpoint --forward` at L2; COO coordination and workstream staffing downstream.  
**Original evidence cut:** repository code inspected September 10, 09:19–09:29 ET; July captured-vendor research; September 9 YCharts report census. See the [research and proposed design](investor-reporting-lightweight-design-20260910.md) and [source manifest](sources/INVESTOR_REPORTING_LIGHTWEIGHT_EVIDENCE_20260910.json). No vendor calls or live S3 reads were performed for that original cut. **September 10 WS2 follow-up:** Andrew then authorized live BD/Orion performance exploration; the [performance presentation review](investor-reporting-performance-review-20260910.md) records successful calls, exact normalization findings and a proposed common report for his review. No live S3 read or endpoint ratification is claimed.

## Direction and relationship to yesterday's brief

**September 10 export extension:** Andrew added a standard branded performance PDF, optional advisor logos/information that he will provide, and a full-width narrative page joining measured performance events to dated market themes. The [export and narrative specification](investor-reporting-export-narrative-spec-20260910.md) and [synthetic PDF](../research/investor_reporting_export_20260910/performance-export-review.pdf) develop this within WS1–WS2. The dashboard remains the default. Historical source mechanisms were inspected; live history coverage has not been measured.

**September 10 YCharts extension:** The [WS3 child brief](investor-reporting-ycharts-brief-20260910.md) and [retrieval/intake design](investor-reporting-ycharts-design-20260910.md) now cover the supplied six transcripts, request manifest and three HARs. Andrew added every-day email attachment intake, the BDAPI Kimi runner without OTP, accepted session takeovers and encrypted generation records. This remains one umbrella project. All three template-generation routes are captured; actual paired output PDFs and section extraction remain required for native Opal presentation. The supplied login was stored and read-back verified in a separate AWS secret; no production reporting service is claimed.

**September 10 Holdings extension:** The [WS4 child brief](investor-reporting-model-overlay-brief-20260910.md) and [partner joins/design](investor-reporting-model-overlay-design-20260910.md) develop advisor-scoped current holdings, model-first pie/radial taxonomy drilldowns and explicit observed-versus-target attribution. Andrew excludes time-series views from v1. Read-only inspection covered 19 named silver datasets and four legacy identity tables; the follow-up records current join coverage, Cottonwood's August 30 model-source lag and unresolved advisor/identity bindings. Its measured evidence supersedes the original unmeasured WS4 claims only within that scope. This remains the fourth workstream in the same umbrella.

**September 10 ratification relay:** CTO Base message 95374 reports Andrew ratified all eight permanent FWD outcomes. Terminated clients stay visible and marked terminated under entitlement; revocation remains separate. Missing advisor logos do not block the performance export. The stamped endpoint remains CTO-owned; the child briefs do not renumber it.

Deliver a small, useful advisor workspace by combining a precomputed client directory, existing silver holdings, and vendor-calculated reports. Selecting a client establishes the relationship and underlying accounts once. Three tabs use that context: **Reporting**, **Analysis**, **Holdings**, in that order. Reporting presents Black Diamond results for 49 Financial and Cottonwood, and Orion results for Inflection. Analysis presents YCharts sensitivity reports. Holdings starts with model allocations and expands into the securities actually held, distinguishing target constituents from observed model-attributed positions.

Andrew clarified: **one project with four workstreams**, potentially coordinated by separate COO lanes. These are boundaries within one product, not four registrations. Workstream 1 explicitly owns client discovery and entitlement as well as page design. Its scope contract is consumed by the other three.

The [September 9 unification brief](investor-reporting-unification-brief-20260909.md) remains the broader reference. This brief supplies a smaller near-term outcome territory. Full performance-engine replacement, vendor retirement, estate-wide pipeline consolidation, broad BI/agent query capabilities, and historical model reconstruction are outside this pilot. This does not cancel or supersede those projects. D9 placement and the separation of performance reporting from sensitivity analysis remain in force.

# PART I — THE OUTCOME TERRITORY

### O1 — An advisor finds an authorized client and opens its relationship and accounts without waiting for a vendor report

From the header panel, an advisor searches by client name and selects an unambiguous result. The workspace immediately shows the selected relationship, its permitted underlying accounts, basic cached context, and the directory's as-of. The advisor can keep the relationship scope or select an underlying account. Switching tabs preserves this choice. Unmapped clients remain visible to authorized viewers with an explicit capability gap.

**Provable act:** exercise a fixture directory containing duplicate names, an account-only entry, and multiple relationships; compare the visible set to the expected authorized set. Benchmark cold and warm search/selection against the entire captured firm-directory denominator, recording payload size and separate directory/report timings; vendor request count during search is zero. No latency target is invented here. **Owner:** WS1.

### O2 — A restricted advisor can use every tab and export only within their permitted client population

Firm and advisor rights govern suggestions, selected account membership, report retrieval, job polling, cached results, and PDF download. A relationship containing an account outside the viewer's permitted population never silently grants that account or its value. A firm-authorized viewer receives the firm's permitted population under the same rules.

**Provable act:** replay authorized and unauthorized requests with swapped firm, advisor, account, relationship, report, and PDF identifiers, including a revoked grant against a warm cache. The negative requests reveal no protected data. **Owner:** WS1 owns the policy and scope contract; WS2–WS4 each enforce it at their entry points. This is a first-class outcome, not a side effect of a search control.

### O3 — An advisor reads the provider's performance result in an Opal report and exports the same result

For the selected account or relationship and reporting period, the advisor sees vendor-calculated performance in a common Opal layout and exports a PDF with the same scope, returned dates, values, method basis, source attribution, and approved disclosures. The UI distinguishes TWR/MWR, net/gross, cumulative/annualized, and unavailable fields. A normalizer does not change a provider's methodology to make two numbers look comparable.

Export uses a standard Opal template based on the deck-generation brand guidelines, with optional verified advisor identity and high-definition logo assets supplied by Andrew. The advisor previews the chosen branding and sections before downloading. Branding changes create an export revision while preserving the reviewed performance revision. Missing advisor assets have an explicit outcome.

**Provable act:** compare a captured provider request/response, normalized report, rendered view, and PDF at the same report revision for each supported partner and scope. A deliberately incomplete provider mapping yields a partial/unsupported result rather than a full-client claim. Relationship return uses a vendor calculation for the exact selected account set; summing or averaging account returns is not a substitute. **Owner:** WS2 for semantic content and adapter; WS1 for shared rendering/export infrastructure.

### O4 — An advisor obtains a YCharts sensitivity analysis in the same client context and exports it

The advisor selects a supported analysis/report variant, reviews the client holdings or saved-portfolio mapping and comparison model it will use, and obtains an Opal-branded analysis and matching PDF. YCharts remains the analytical source. The report preserves the input snapshot, configuration, data dates, limitations, and vendor attribution. A modeled comparison is described as modeled.

**Provable act:** replay each approved report variant from a validated input revision through its captured request/job/result chain to the tab and PDF; unsupported variants are visible as unsupported. The child brief proposes automatic serving for complete validated requests and human correction for unresolved exceptions, with universal analyst approval an explicit alternative for Andrew to select. The original cut covered one static report. The dated WS3 follow-up now establishes all three generation routes across 1,085 supplied HAR entries, with six successful report POST/PDF-GET pairs. The PDF bodies and upload multipart request are absent; the native section/output parity gap remains explicit in the child brief. **Owner:** WS3.

### O5 — An advisor sees current holdings organized by models, with the underlying securities and unassigned assets preserved

The advisor starts with the selected client's model breakdown and drills into accounts and securities using the existing category taxonomy and pie/radial presentation. V1 is current snapshot only. Actual custody holdings remain the total-value basis. SmartX, Eclipse, or Black Diamond Rebalancer supplies the partner's assignment/model overlay. Target weights, assigned-account values, actual sleeve values, and inferred estimates are distinct; missing attribution remains visible without double-counting or redistributing the residual. The WS4 child brief supplies the detailed current source and attribution contracts.

**Provable act:** replay dated holdings and model snapshots for all three registry client firms, including an unassigned account, an unmatched join, a blended model, and a multi-relationship membership. Unique underlying holdings reconcile before and after the overlay; coverage and join exceptions carry denominators. **Owner:** WS4.

### O6 — An advisor can continue using the workspace when one report is unavailable and can tell the age of each result

Client selection and silver-backed holdings remain usable when a report provider is slow or unavailable. Each tab distinguishes loading, ready, stale, partial, unavailable, and failed results; a late response for a previous selection cannot populate the current client's tab. Cached reports retain their original as-of and revision.

**Provable act:** deliberately delay/fail one provider, switch clients during an outstanding request, expire a cache entry, and complete jobs out of order. Verify that unaffected surfaces work and no response is attached to the wrong selection. **Owner:** WS1 shared lifecycle; WS2–WS4 provider/snapshot status.

### O7 — An advisor explains the reporting period using measured portfolio events and the market themes recorded around those dates

The optional narrative page places the cumulative-return series across a wide page, marks the selected period's maximum drawdown and recovery when present, and annotates a handful of material movements. Dated Trending Topics and Topic Cloud evidence supply the primary context; dated Best/Worst Performers, RSI, Regime and Fear & Greed observations can support it. The prose distinguishes surrounding market discussion from evidence of client-specific return attribution. Missing history remains visible.

**Provable act:** check a known peak/trough/recovery fixture, a flat series, a cash-flow-only value change and an unrecovered decline; verify that event selection precedes news selection. Trace every annotation to dated evidence under its declared cutoff, exclude future articles/current snapshots, preserve conflicting signals, and reject unsupported causal claims. Preview and PDF use identical selected events, evidence and wording. **Owner:** WS2 for events, dated evidence and narrative validation; WS1 for options, page layout and export lifecycle.

# PART II — WHERE THE BOUNDARY SITS

## II.1 One project, four explicit workstream boundaries

| Workstream | Owns | Provides to siblings | Does not own |
|---|---|---|---|
| **WS1 — Page, client discovery, entitlement and shared report presentation** | Header; name search; relationship/account selector; tab order; slim directory projection from silver; firm/advisor policy binding; selected-scope resolution; common state/error model; reusable report/PDF shell; export options/preview, advisor assets and standard branded template | Versioned directory and scope contract; authorization function; shared UI/export components; separate performance/export revision identities | Performance calculation, YCharts analytical mechanics, model-allocation semantics |
| **WS2 — Performance adapter and narrative content** | Black Diamond adapters with separate partner configurations for 49F/COT; Orion adapter for INF; provider field and method normalization; performance report view-model and PDF content; measured events, dated market-evidence adaptation and narrative validation | Versioned performance contract and partner fixtures; event/evidence/narrative bundle; capability/coverage results | A new return engine, approximate household return from account percentages, client authorization policy, ownership of existing news producers |
| **WS3 — YCharts analysis adapter** | Analyst workflow capture; approved report varieties; client input/saved-portfolio resolution; YCharts request/job/result routing; sensitivity view-model and PDF content | Versioned analysis envelope, report variants, provenance, fixture coverage | Rebuilding YCharts analytics or adding uncaptured scenario types |
| **WS4 — Holdings and model overlays** | Snapshot resolver; three partner adapters; model-first presentation data; securities drilldown; actual/target/residual reconciliation | Versioned holdings/overlay contract with separate holdings/model dates and coverage | Trading, rebalancing, altering model assignments, model history reconstruction |

**Ownership check:** five responsibilities were named in Andrew's first message: page, performance, analysis, holdings/model overlays, and client discovery/entitlement. All five are covered: WS1 absorbs page plus discovery/entitlement; WS2, WS3, WS4 cover the remaining three. None is left with an owner called merely “shared.”

Andrew proposes separate COO lanes for the boundaries. The project coordinator must name those lanes at issuance and name one integration owner. This brief does not create task orders, choose serial suffixes, sequence work, or register separate projects. Boundary issues and unexpected findings route to the umbrella project's coordinator; architecture/method questions route to CTO, with Andrew deciding product semantics where needed.

Coordination rule relayed by CTO in message 95164, commit `c51baedac8`: **one issuer per round**; amended Rule 27 binds the round, not the project, so Andrew's four-workstream split across disjoint COO lanes stands as described. WS1 owns shared contracts and presentation files; WS2–WS4 own their adapter/content modules and submit shared-contract changes through that owner. Actual write-path assignments are named at issuance. **Operative ruling, CTO message 95229:** the one-project-per-instance rule exists and is enforced for Tier-2 seat instances in `.tools/to-decomp-ref-lint.py`; it **does not apply to Tier-1 unless Andrew extends it**. A possible future extension is not a pending prerequisite: work proceeds under the current scope. The gate remains in force; a Tier-1 refusal is referred to CTO without overriding it.

## II.2 Reuse and sibling boundaries

Reuse **D10 / OPAL_ASSETS** silver source contracts; **D1_CATVIEWS / MDPF_GLOBAL** model taxonomy; **D3_MODELOVERLAY** SmartX-account join logic; **WSE_COTMDL** Rebalancer shapes; **ADVI_ECLDAT** Eclipse join precedent; **OPAL_ASSETS_49METATABLES** 49F identity/advisor dimensions; **PORTAL_AUTHHARD / ADVI_ROLGAT / ADVI_PROFIL** authenticated identity and scoping mechanisms; **ADVI_BDPARITY / RCN-0001 / RCN-0002** performance request and method evidence; **YALP_MDSRC** YCharts transport code where applicable. These are named as prior art and dependencies, not reassigned by this brief.

Existing gold code may supply reusable functions and semantic evidence. The pilot's production inputs are declared source/silver snapshots and requested vendor results; it must not acquire an implicit dependency on an existing page's gold JSON. Where an identity map exists only in a legacy firm bucket, the manifest must say so and identify the bounded reuse or source extension needed. “All of it is already in opal-data-assets” has not been established.

The source layer remains complete vendor-shaped silver. A slim search directory, business-scope mapping, normalized report, or model overlay is a derived product projection; calling it a cache does not make it a silver transformation. The pilot can avoid a new full analytical pipeline while still owning these small projections and their refresh mechanism.

# PART III — THE QUALITATIVE BAR

1. Searching for a client produces a useful selection before the report provider answers.
2. An advisor sees exactly **Reporting → Analysis → Holdings**, and does not select the client again in each tab.
3. An advisor can trace a performance figure to the provider result and see why two providers' methods differ.
4. The exported PDF corresponds to the report the advisor reviewed, even if the provider revises its data later.
5. Model targets do not masquerade as observed holdings; unexplained assets stay in the reconciliation.
6. A second client selection cannot inherit the first client's delayed report.
7. A coordinator can name the owner of every shared field and every endpoint's scope check.
8. An advisor can trace each narrative annotation to a measured event and dated source evidence; market context does not masquerade as client attribution.

# PART IV — THE SUBSTRATE

### F1 — The portal already has the structural UI pieces

Inspected `App.tsx`, `PageHeaderVariants.tsx`, `TabNavigation.tsx`, `useTabNavigation.ts`, `PageSurfaceControl.tsx`, Catalyst `combobox.tsx`, and `ClientListPanel.tsx`. They provide lazy routing, a text-led header, equal-width tabs, panel/control primitives, a virtualized combobox, and client drill callbacks. This is a strong implementation starting point. The combobox filters the options passed to it; it is not a server-side entitlement or search service. The tab component is not proof of complete keyboard/ARIA behavior. No portal was run or visually graded in this research.

### F2 — A reusable 49F Black Diamond performance request builder already exists

`opal-assets-bd49f-reporting-pull/lambda_function.py` has `body_performance_period`, explicit period and method parameters, `requested_range_index`, and the `performancePeriod` endpoint. It is an account-based reporting pull; broad relationship requests and partner-generalized use are additional contracts. It records that returned date-range names/types may be null, so index plus returned-date validation matters, and that provider-returned inception can override a requested start. The July Cottonwood capture adds the period/series/activity response field inventory. These are code/captured findings, not a new live API validation.

### F3 — Orion has a different request model, and the inspected existing pull is not the requested live client report

The July Orion teardown §4 records the documented recursive `POST /api/v1/Reporting/Scope` calculation graph; it labels that surface DOCS, not captured performance response evidence. The inspected `inf-performance-daily` pull instead generates and polls a saved ExcelReports “Performance Dim” query. Thus the pilot must pin an appropriate on-demand response and tenant-specific configuration. A stored daily dimension cannot silently stand in for a current on-demand report.

### F4 — All three model-source families have repository substrates, but they have different meanings

49F's `a06_dim_identity_crosswalk.py` connects SmartX allocation/account identifiers to Schwab accounts and carries `map_date`/`map_carried`. Eclipse silver schemas carry portfolio/account/model links and nested model details; `INF_E_00.eclipse_model_portfolios.py` joins them to Orion account dimensions and explicitly separates model-headline AUM from decomposable account values. Cottonwood's `rebalancer_schemas.py` declares roster, assignment, blend edges and security leaves, with `external_id` as the holdings join. Those are useful foundations; successful current-data joins and coverage have not been measured in this cut.

### F5 — Client identity and advisor population are partner-specific

The firm registry has **three enabled client firms**, plus test/demo entries excluded from the partner denominator. 49F has a canonical 0833 Schwab scope, hashed household IDs, role-decomposed advisor data, and a BD account crosswalk. INF has native account/household IDs and representative mappings, some inspected inputs still addressed in `opal-data-inf`. COT's membership grain is relationship × account and its current role module describes joint founder coverage without a segmentable advisor dimension. Names, role labels, and advisor IDs cannot be used interchangeably. See design §2 for exact sources and unresolved bindings.

### F6 — Existing authentication is reusable, but the new route needs deliberate coverage

`auth-validator-edge/index.mjs` verifies claims, derives firm/advisor headers, and applies ownership checks to specific existing path patterns. An Investor Reporting route is not automatically protected merely because the old Advisor Intelligence patterns are. The pilot needs server-side account-set authorization for its search, POST bodies, report IDs and export paths, using existing policy semantics. No new authentication system is proposed.

### F7 — YCharts is one analytical provider; report routing remains an evidence gap

The captured September 9 report census covers **one of three sensitivity varietals**, 33 pages, 176 catalog rows and 125 distinct fields. It is the product-2 artifact Andrew identified, not an actual account-performance report. The inspected YCharts client supplies security metrics, time series and scatter data; those methods do not establish a portfolio/report-generation workflow. Analyst transcripts, the complete generation HAR and input/result specimens are needed to identify the report input, job lifecycle, result data, and export mechanism. No cross-provider analytical normalizer is needed; an Opal context/result envelope is still required.

# PART V — WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

1. WS1 owns a versioned directory/scope contract and each sibling enforces it. The JWT identity-to-partner-advisor binding and partial-relationship behavior must be explicit.
2. A source manifest names exact silver keys, input dates, availability markers, key grammar and mapping provenance. It verifies which identity/entitlement inputs actually exist in opal-data-assets and which remain in legacy locations.
3. The 49F 0833 pilot master is pinned to the repository's `08335338` scope; this is a custody-master scope, not a customer account lookup by four-digit suffix.
4. Vendor performance fixtures cover both partners using BD separately, plus INF, and both account and relationship scope. A household has no fabricated aggregate return when the provider cannot evaluate its selected account set.
5. The report owner settles presentation periods and carries the providers' actual fee, annualization and inception bases. Adapter normalization preserves economics and reports unavailable fields.
6. YCharts evidence establishes all approved varieties, input holdings/weights or saved IDs, comparison model mapping, lifecycle, branding/export capability, and report-specific attribution/disclosures. The existing capture provides a floor, not whole-product coverage.
7. The project defines report/cache retention and invalidation, session failure behavior, request limits, and a bounded synchronous-or-job contract based on measured provider behavior. No made-up latency or TTL is ratified here.
8. The holdings adapter distinguishes actual positions, actual model/sleeve valuations, model assignments and target allocations, with duplicate/multi-membership controls.
9. WS1 owns the shared PDF renderer; WS2 and WS3 own their content contracts. PDFs bind to an immutable reviewed report revision, not a fresh provider call during download.
10. Downstream live vendor validation and production access use the applicable authorization and credential contracts. The original repository-only cut made no vendor calls; the separately authorized WS2 follow-up records its bounded live calls in the performance review.
11. The export extension measures historical news/indicator coverage and vintage fidelity before claiming a year of usable history. Topic Cloud's dated pre-filter report archive is distinct from the final cloud displayed on a given day. Advisor assets, narrative evidence, template and prose versions are bound to the export revision.

# PART VI — STATUS — NOT OUTCOME-BEARING

As of the September 10 source-read window, this is a research/design artifact. Workspace reference HEAD observed `0a5b6f435e4ad3d4e620341662640d69a4570627`; portal HEAD observed `5907cbca98eb091124e38a32debefa355c1d4376`. The shared tree may advance independently; the accompanying source manifest fingerprints the inspected file set.

The new page, normalizer Lambdas, client directory and PDF flow were not built or deployed in this turn. No latency, current source freshness, API health, or cross-firm security result has been asserted from code inspection. The initial Andrew-direct record was committed as `822f3d7519`; its one-project clarification is included in this delivery. Push state is LOCAL; origin/CLOUD was observed at `71574353645510c3af85a77de3c09fb6f1117159` before delivery, and is re-measured in the delivery receipt.

# PART VII — WHAT THIS BRIEF DOES NOT CLAIM

The following qualifications describe the original repository-only cut. The linked performance follow-up supplies later live evidence; the export extension supplies local HAR/PDF and historical-source findings; WS3 adds the supplied analyst/capture evidence; WS4 adds bounded live S3 snapshot and identity measurements. None implies production implementation or complete partner/history coverage.

1. Repository source proves intended mechanics, not deployed/current behavior. July capture facts and comments keep their original vintage.
2. No raw HAR was newly parsed, no vendor session used, and no live S3 snapshot read. The response inventory relies on the existing captured research with its stated gaps.
3. Existing 49F account requests do not prove relationship aggregation or Cottonwood credentials/configuration. Orion on-demand request/response pairing remains unverified locally.
4. Neither the YCharts analyst transcripts nor its generation HAR nor the remaining two varietals has been supplied/located in this turn. A specification for their capture is in design §4; their schemas are not invented.
5. A slim derived cache is still work. Existing silver data does not imply that complete client names, current permissions, vendor IDs and model joins are already served under one contract.
6. No separate client directory product, full pipeline replacement, vendor-retirement commitment, trading action, or scenario engine has been added.
7. No existing project status, task order, register row, core document, silver data or served bytes was changed. The pilot does not silently cancel yesterday's broader ambition.
8. The older ADVI_PERFRP restricted PRD was not consulted; the new brief is grounded in Andrew's present instruction, prior recon, and the explicit source list.

## REFS TO CARRY

```text
BRIEF PATH       docs/briefs/investor-reporting-lightweight-brief-20260910.md
DESIGN           docs/briefs/investor-reporting-lightweight-design-20260910.md
EVIDENCE         docs/briefs/sources/INVESTOR_REPORTING_LIGHTWEIGHT_EVIDENCE_20260910.json
PROJECT          NONE-YET: ONE umbrella project, four workstreams, D9 Opal Workflows
EXISTING PRD     NONE created or selected by this brief
PRIOR BRIEF      docs/briefs/investor-reporting-unification-brief-20260909.md
SOURCE DIRECTION org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260910_0919ET_LIGHTWEIGHT_INVESTOR_REPORTING.md
SIBLINGS         Named in II.2; no status or reassignment inferred
PRIOR ART        F1-F7; exact paths in design §7 and the source manifest
MEASURED AT      2026-09-10T13:19Z onward; individual source hashes in evidence manifest
```

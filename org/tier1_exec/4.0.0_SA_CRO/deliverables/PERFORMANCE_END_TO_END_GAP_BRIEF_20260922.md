# Performance reporting across firms: end-to-end connector brief

Prepared by 4.0.0_SA_CRO on 2026-09-22. Read-only product assessment plus proposed closure requirements; no application changes, vendor calls, deployment, or schedule activation.

## Design finding

Andrew's understanding matches the intended design: performance comes from Black Diamond for 49 Financial and Cottonwood, and Orion for Inflection. Opal should request the exact authorized account set and period, retain the provider's calculated return, normalize units and response structure, and render/export the result. This does not require an Opal return engine or reconstruction from holdings, prices, and cash flows.

One deliberate transformation exists: Orion returns compact daily performance factors, which the adapter links into a cumulative curve and reconciles to Orion's own summary return. That is presentation of provider-calculated performance, not computation of a new account/relationship return from positions. Black Diamond supplies cumulative series directly. Account returns must never be summed or averaged to manufacture a relationship return.

The implementation is substantially less connected than the design. Many comments describe an exact-account-set live calculation, but the executable adapters currently pass `None` as the vendor request body. Current live transport is an unauthenticated POST wrapper. Source parsing and correctness work should be retained; request assembly, credential acquisition, server-side identity mapping, response serving, and frontend mapping must be finished.

## Current measurement

At 2026-09-22 19:29:32 UTC, read-only AWS inspection downloaded the deployed performance Lambda and its configured dependency layer, verifying both code digests. The seven performance source files examined match local source ignoring newline representation. The active handler is `entry.lambda_handler`, modified September 21, and `IRPT_PERF_TRANSPORT_MODE=recorded`.

The configured layer contains the Black Diamond helper at the configured override path. It is therefore incorrect to call that helper absent merely because it is not in the function zip. The `requests` package used by the live transport was not found at its standard import locations in either the function zip or its one layer; live packaging requires an explicit import/runtime check. No Lambda or vendor endpoint was invoked.

The export Lambda's deployed entry also matches local source and still returns NOT_READY on submit.

Machine-readable evidence: `.runtime/codex-seats/4.0.0_SA_CRO/performance_connector_audit_20260922.json`.

## Firm-specific adapter map

| Firm | Provider and intended endpoints | Existing work | Remaining provider-specific gap |
|---|---|---|---|
| 49 Financial | Black Diamond: POST `/portfolioreporting/api/performance/performancePeriod` and `/performanceSeries`; ClientView bearer via GET `/session/token` | Recorded period/series responses; parser for TWR, periods, hierarchy, cumulative series, benchmark/value facts; reuse of the existing bd49f reporting-pull body/range helpers | Connect firm's session/token helper; map selected canonical accounts to BD account IDs; build and actually send period AND series requests; prove exact selected-set aggregate as well as account detail; promote fresh response provenance |
| Cottonwood | Same BD endpoint family, a separate Cottonwood credential/session and data plane | Separate tenant routing and reusable BD parser | No Cottonwood performance capture in this adapter's fixture set. Independently prove credential binding, identifiers, selected-set requests, response hierarchy, method, periods, series, and benchmark/value fields. 49F success does not certify COT |
| Inflection | Orion: POST `/api/v1/Reporting/Scope`; configured token path `/api/v1/Security/Token` | Captured native household/account graph; summaries, daily factors, activity values; unit conversion and cumulative linking | Promote the research request graph into a parameterized production builder; connect existing Orion authentication; bind actual selected accounts and date/calculation windows; confirm supported method/fee/accrual/annualization/benchmark settings rather than assume BD parity |

A configured endpoint, token path, or secret name is not an executed connector. `tenants.py` declares all three; `LiveTransport` does not consume those authentication declarations.

## Start-to-finish walk

### 1. Header registry -> authorized relationship/account selection

Directory source adapters, search, resolution, and frontend narrowing exist. Reuse the alphabetical relationship registry/account drilldown proposed in the sensitivity brief. Performance should accept one account or an explicitly selected set within one firm, with an exact membership revision.

Close: distinguish the selected set from the user's entire permitted universe. Do not substitute a whole household for an account subset, or all permitted accounts when selection transport is lost. Carry the selected set, directory revision, and entitlement revision together. A global firm view may list firms; it must not blend their returns.

### 2. Canonical account identity -> vendor account/scope identity

The scope resolver has opaque account IDs and a server-only `vendor_ids` field, initialized empty for callers to populate. The performance path does not populate a vendor-key translation. The BD helper expects vendor account identifiers, while the permissioned scope carries canonical IDs.

Close: connect the existing identity/crosswalk data to a server-owned provider-ID resolver for each firm, including authoritative membership for a multi-account calculation. Retain the reverse mapping for account-detail rows. Missing or ambiguous mappings must name a coverage gap; they cannot broaden the request or silently disappear.

### 3. Date controls -> API event -> provider request

Frontend controls support YTD, 1Y, 3Y, since inception, and custom dates. LiveClient sends `?start=...&end=...` and uses the scope fingerprint as the `{accountSetId}` path value. The deployed entry instead reads top-level `requested_start` and `requested_end`, not those query parameters. It treats the path's accountSetId as a literal individual account ID. The shared served boundary passes the event through without translating these carriers.

Close: resolve the account-set reference to its members, parse/validate start/end from the actual API event, and map presets to vendor request semantics. The frontend's `1970-01-01` since-inception sentinel must not be treated as a real inception date. Vendor-returned inception/history dates remain authoritative.

### 4. Firm routing -> credential/session -> authenticated transport

Tenant routing distinguishes both BD firms and Orion. The existing bd49f reporting-pull has reusable `load_bd_session`, `get_clientview_token`, and authenticated `_request` functions. Research also demonstrates the Orion request surface. The IRPT live transport currently invokes `requests.request('POST', ..., json=body)` without a cookie, Authorization header, token acquisition, or session refresh.

Close: reuse bounded existing provider authentication clients, bind them to the correct firm, handle expiry/refresh and provider errors, and include all runtime dependencies in the deployed artifact. Satisfy existing operational egress gates when performing the acceptance run. Merely changing `recorded` to `live` cannot complete this connector.

There is also a routing defect before fetch: `tenants.py` accepts canonical opaque firm IDs, but `handler.RECORDED_LABELS` is keyed by old `F-49F`/`F-INF` labels. The handler returns NO-CAPTURE when labels are missing, regardless of transport mode. Cottonwood intentionally has no recorded label. Separate test-fixture selection from live routing and use one firm-ID convention.

### 5. Authorized request -> BD/Orion calculation

BD's helper builds a period request, but the handler uses only its range index and discards the body. It builds using only the first requested account. Both BD `adapt` requests and Orion's Scope request pass `None` as the body. Orion's compact graph construction is in the research probe, not in the production adapter. The selected set and requested dates therefore do not reach a real calculation through this path.

Close: build and send complete parameterized payloads for every endpoint. For BD, connect both period and series bodies and certify returned ranges against the actual submitted request. For Orion, build the requested group/calculation graph and choose the correct primary calculation. For relationships/subsets, request the vendor-calculated aggregate for the exact set; if a selected-set aggregate is unsupported, show account results with an explicit unavailable aggregate.

### 6. Provider response -> parsed returns, hierarchy, and dates

This is where the strongest reusable work already exists. BD parses decimal TWR values and cumulative series, preserves source dates, distinguishes overlapping `levels`/`combinedLevels`, and matches range positions with returned dates. Orion uses group path + node type + calculation ID because calculation IDs repeat across groups. It converts daily percent units and links daily factors while carrying the vendor's summary.

Close the remaining generalization gaps: the handler picks `result.nodes[0]` as primary; BD series parsing takes the first series node. These choices must be keyed to the requested identity, not incidental response order. BD's report-wide actual_start is the minimum over all returned ranges, which can include earlier history; this must not masquerade as the requested primary window. Keep period, series, benchmark, and valuation facts aligned to the same selected group and applicable date window. Prove single-account and multi-account behavior separately.

### 7. Parsed results -> common PerformanceReport

`normalize.py` builds a shared report with lineage, requested/actual dates, measurement basis, summary/period returns, cumulative series, account detail, and optional benchmark/value facts. Returns are standardized as decimal fractions. No cross-account return arithmetic is performed.

Close: preserve every requested account's coverage, full source-response/request identity, and period-specific basis. BD currently assigns TWR/net/accrual/USD in the adapter; those claims must remain tied to the effective request and verified response rather than outlive configuration changes. Its report-level annualization is derived from whether any period is annualized, which needs separation when different rows have different bases. Orion explicitly leaves fee/accrual/annualization unknown on its captured surface and did not request a benchmark or money-weighted calculation. Unknown must stay visible until the provider connector establishes more.

The live response wrapper currently has no source response digest; it would leave source_revision unset. Mint/persist a meaningful immutable request/response revision for display, narrative, and export. Do not label a recorded response as a current client answer.

### 8. Backend report -> HTTP response contract -> frontend adapter

The published response contract expects `data` to be a PerformanceReport. `handler.run` returns a diagnostic wrapper `{report, contract_validated, absences, coverage, ...}`. `entry.performance_report` returns that wrapper unchanged; the shared boundary puts it under `data`. The frontend adapter expects `data.returns`, `data.lineage`, etc., not `data.report.returns`.

Close: return the declared report at the declared location, translate coverage/absences into a truthful status, and keep diagnostics separately. The current computation supplies no `_status`; the ReportingTab requires an answer-bearing availability state before rendering. A well-formed numbers object with no usable status still does not make a displayed report. Validate the exact HTTP response with the actual browser adapter, including partial/stale/unavailable cases.

### 9. Frontend wire adapter -> visible report

The screen components exist: summary, cumulative chart, period table, account detail, and method/source labels. However, `adaptPerformanceReport` reads only summary_returns, not period_returns; it assigns null row windows; it sets benchmarks and uncoveredAccountIds to empty arrays; it does not translate optional valuation facts; account names are IDs and ending values are unavailable. All returned account rows are marked covered.

Close: define typed optional benchmark/valuation structures and map every supported source field to the view. Preserve period dates and actual missing-account coverage; join account labels through the authorized directory. Render return units clearly: the shared Metric currently prints the bare supplied number, while the wire's return_units is not carried by this adapter. Deterministic percentage/currency display can be added without changing the underlying financial value. A dropped adapter field is different from a provider that did not supply it.

### 10. Report -> optional narrative/context

Narrative/event/evidence libraries and a narrative route exist. The route is GET `/narrative/{reportId}`, but its compute function expects an inline performance_report plus cutoff_at. It does not load that report by the path ID. Its account-coverage reader expects account-ID lists rather than the report's account_detail rows. The export resolver can request narrative, so this mismatch is a real downstream connector if commentary is included.

Close: persist the report revision; resolve it server-side by ID under current entitlement; retrieve date-bounded context; publish a separately versioned narrative tied to the exact report. Keep narrative optional for a first numerical report. It must not recalculate or modify provider performance.

### 11. Displayed report -> frozen export bundle

Shared layout and bundle resolution exist. The current export fallback fetches performance with start=end=the bundle's business-as-of date; passing a source revision as a frontend request parameter is not an implemented immutable backend report lookup. A cache miss can therefore request a different period than the displayed report.

Close: freeze the complete authorized report payload or retrieve it by an immutable report ID/revision carrying its original account set, date windows, methodology, and source response. The preview and exported PDF must use that same frozen object. Re-fetching latest performance is not a valid substitute. Include the actual provider/firm disclosures required for the selected report; the current performance bundle path supplies an empty disclosure list.

### 12. Export controller -> browser renderer -> stored PDF -> download

Controller, dispatch, renderer validation, receipt, and protected-download modules exist. Today's deployed submit entry still raises NOT_READY rather than calling the controller. The shared render identity/asset authorization chain also has the integration repairs described in the sensitivity brief.

Close: wire submit -> bundle persistence -> working render host and pinned print route -> correct assets/identity -> render -> content/font validation -> artifact and receipt persistence -> authorized download. Prove the performance screen and PDF contain the same values, periods, basis, coverage, and source revision. This shared export gap does not justify delaying an otherwise correct on-screen provider report.

## Recommended completion sequence

1. Repair API request/response contracts and selected-account/vendor-ID resolution. Use the real browser request shape, not a hand-constructed internal event.
2. Connect authenticated, parameterized BD requests for one 49F account through to the actual screen; retain the existing parser/normalizer. Prove period/series alignment and source methodology.
3. Independently commission Cottonwood's BD tenant and Inflection's Orion scope graph, then exact multi-account/relationship/subset behavior for every firm. This is a parallel acceptance matrix, not evidence that one tenant's success covers another.
4. Complete frontend mapping and immutable report publication; support available benchmark/value facts honestly. Add optional narrative after the numerical path works.
5. Connect the shared export chain and prove frozen-report equality in the PDF.

Acceptance: for each firm, one account, a whole relationship, and a subset; YTD, trailing/year, since-inception, and custom windows; provider summary/series reconciliation; expired session, missing history, missing account mapping, and changed permissions. Track one request from canonical selection through vendor IDs/body, raw response, common report, rendered UI, and PDF. The product is complete when these traces reconcile, not when the parsers pass fixture tests.

## Evidence anchors and limits

Source inspected around workspace `257e98b8c3ee19148bc82308c9b9eb57ea2a1134` and portal `7dd3d067a17ee00b878ecfceff23c557649a2331`; shared work may advance concurrently. Fresh AWS code/configuration verification is recorded above. No signed-in UI walkthrough or fresh provider calculation occurred.

- `infra/aws/lambda/investor-reporting/performance/{entry.py,handler.py,tenants.py,transport.py,bd_adapter.py,orion_adapter.py,normalize.py,units.py}`
- `infra/aws/lambda/opal-assets/opal-assets-bd49f-reporting-pull/lambda_function.py`
- `docs/research/investor_reporting_performance_20260910/probe_performance.py`
- `infra/aws/lambda/investor-reporting/_scope/resolve.py` (`vendor_ids`)
- `infra/aws/lambda/investor-reporting/_authz/served.py` (HTTP event/response boundary)
- `docs/contracts/investor-reporting/v1/responses/performance-report.response.schema.json`
- `portal/src/api/endpoints/investor-reporting.ts` (`getPerformanceReport`)
- `portal/src/pages/InvestorReporting/contracts/adapt.ts` (`adaptPerformanceReport`)
- `portal/src/pages/InvestorReporting/tabs/reporting/{period.ts,ReportingTab.tsx}`
- `portal/src/pages/InvestorReporting/render/{values.tsx,performance/PeriodResults.tsx}`
- `portal/src/pages/InvestorReporting/export/resolveBundle.ts`
- `infra/aws/lambda/investor-reporting/narrative/entry.py`
- `infra/aws/lambda/investor-reporting/export/entry.py`

## Andrew-direct request — verbatim record

Channel: user message to Codex seat 4.0.0_SA_CRO, session date 2026-09-22; message timestamp unavailable in model context. Recorded with this brief.

> Great work. Now I want the same style brief, where you cover the walk end to end through all adapters looking for what is missing or incomplete for performance reporting function across firms. my impression is that we simply port the performance over from the existing black diamond/orion endpoints, which should be the current design.

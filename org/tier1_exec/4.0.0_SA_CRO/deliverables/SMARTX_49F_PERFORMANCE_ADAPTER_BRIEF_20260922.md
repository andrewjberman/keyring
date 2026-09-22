# SmartX primary performance adapter for 49 Financial

Prepared by 4.0.0_SA_CRO on September 22, 2026. Specification and evidence review only; no vendor execution, credential changes, deployment, or production routing change performed.

## Product decision and place in the suite

**SmartX is the intended primary production performance provider for 49 Financial. Black Diamond remains the independent verification provider.** This incorporates Andrew's latest direction and supersedes the 49F Black-Diamond-primary routing proposed in the earlier performance/backend briefs. Cottonwood's Black Diamond and Inflection's Orion routes retain their existing roles.

The deliverable is a real 49F client performance channel: select a relationship/account set, obtain the corresponding actual performance from SmartX, display it through the shared PerformanceReport experience, retain an immutable revision, and export that same revision. Model-level return charts alone do not constitute completion of this channel.

The current evidence supports strong model-performance discovery and an identified allocation-performance endpoint. It does **not yet establish a complete SmartX account/household calculation contract**. Closing that gap is required work in this adapter, not a reason to preserve Black Diamond as the unannounced default. If an account or selected-set calculation is unavailable from SmartX, show that limitation and close the entitlement/endpoint gap; never substitute a model return or silently relabel a Black Diamond response.

| Reporting purpose | Primary | Verification / context |
|---|---|---|
| 49F actual account and selected-account-set performance | SmartX, after account scope/methodology proof | Black Diamond for the matching account set and comparable calculation basis |
| 49F actual allocation/sleeve performance | SmartX allocation-performance surface | BD only where its response supports the same sleeve scope; otherwise mark not comparable |
| Model reference/strategy performance | SmartX model-performance surfaces | Context distinct from actual investor results; model figures are never account returns |
| Current model/non-model holdings | Firm LGIC custody/model snapshot | Supplies identities and current ownership context, not a return calculation |
| Cottonwood / Inflection performance | Black Diamond / Orion respectively | Existing firm-specific acceptance requirements remain |

## 1. Endpoint inventory and evidence strength

Endpoint paths below are identified from the repository's May-July 2026 captures, probes, and code. Their current live behavior and service-account permissions must be revalidated for production acceptance. No authenticated SmartX requests were made in this specification turn.

**API base:** `https://api.smartxadvisory.com/api/3.1`.

| Method and path | Proven / observed purpose | Adapter use and work remaining |
|---|---|---|
| `GET /allocations/performance?modelids={modelId}&grouping=m&start={epochSeconds}&end={epochSeconds}` | Nested allocation-performance payload, observed up to approximately 11.7 MB. Exact query appears in the checked-in probe | **First endpoint to characterize for actual investor sleeve performance.** Prove allocation/account identifiers, date-filter behavior, supported grouping, pagination/completeness, method, fees, cash treatment, and whether account or selected-set calculations are included. The probe supplying start/end does not prove the server honors them |
| `GET /models/{modelId}/performance?grouping=daily` | Historically tested daily flow-adjusted model P&L; weekly/monthly grouping also identified. Includes `pnl.percent`, `pnl.dollar`, period ranges, and summary values/flows/fees | Model-reference series and independent model-series reconciliation. Do not treat model-level output as a client's actual return. Retain full period boundaries and completeness |
| `GET /enterprises/allocations?modelid={modelId}` | Allocation roster with account/advisor/value context | Join SmartX allocations to the canonical 49F account census. Scope discovery from a roster is not authorization; prove full coverage rather than reuse a fixed model list |
| `GET /allocations/nonzerosleeve` | July full-app capture: sleeve/account values and timestamps, cash/dividend/interest/fee components | Context and reconciliation of observed sleeve values. A nonzero-only response cannot establish the universe of zero/closed accounts. Historical behavior remains unproven in that capture |
| `GET /models/{modelId}` | Model identity, `reportedModelId`, enterprise and configuration | Resolve distinct vendor ID namespaces and model metadata |
| `GET /users/access` | Model/reported-model/account grants, materially different across observed logins | Establish the production identity's accessible estate. Vendor access does not replace Opal's advisor/account authorization |
| `GET /accounts`; `GET /accounts/counts` | Account roster/count surfaces identified; `/accounts` was empty for the manager login in the earlier sweep | Establish whether the intended service identity can enumerate the required 49F accounts. Counts alone do not establish membership |

**Performance host:** `https://performance.smartxadvisory.com`.

| Method and path | Proven / observed purpose | Adapter use and limits |
|---|---|---|
| `GET /models/performance?model_ids={modelId}&percentages=100&leverages=1&platform={platform}` | Monthly model returns, one benchmark series, risk/return statistics; historically spot-checked and consumed by existing pull code | Model context. Historical probes found date filters ignored; fetch/retain the source series and apply an honest display window. Confirm model performance basis rather than assuming every marketplace series is an actual client track record |
| `GET /models/summary?platform={platform}` | July capture: model statistics and performance-start fields | Metadata/history-floor discovery; not a substitute for actual account return series |

**Authentication:** `POST https://identity.smartxadvisory.com/connect/token`, form-encoded password grant using the existing registered client/scopes. Reuse the established SmartX credential/refresher integration after validating the current identity, entitlement and recovery behavior. Credentials remain in Secrets Manager; neither tokens nor credential values enter report artifacts.

**No verified exact-account-set calculation URL is asserted here.** Discover it from an authenticated account/household report workflow or authoritative vendor contract, capture its actual request/response, and add it to the adapter's versioned endpoint map. Do not invent `/accounts/performance` or assume that the allocation endpoint can aggregate any selected set.

**Previously problematic surfaces:** earlier research found wrong/stale return fields in `/models/{id}/statistics`, stale `/reportedmodels/{reportedModelId}/historicalperformance`, and flow-contaminated/mis-scaled aggregate values in `/enterprises/aum`. Preserve those findings as dated evidence and require new proof before admitting those fields. AUM changes are not investment returns.

## 2. Identity, scope, and account completeness

Use the complete 49F custody account registry as the denominator, including accounts absent from SmartX, zero balances, closed accounts with history, and non-model assets. Join the canonical opaque account ID to the appropriate SmartX account/allocation IDs and the BD account ID used for verification. Retain source IDs server-side.

The account-to-allocation-to-model relationship is dated. A client's present model assignment cannot establish which model/sleeve owned assets throughout a historical return window. Preserve effective dates, allocation opening/closing dates and any vendor performance-history scope. Test model changes, sleeve closures, transfers and cash movements explicitly.

Model IDs and reported-model IDs are different namespaces. The current holdings builder's allocation-account map and valuation joins are useful inputs, but its known duplicate/allocation-grain defects must be repaired before it can certify scope/value reconciliation. Do not derive the performance account universe from its emitted root nodes or from the five-model benchmark script.

Resolve the selected account set and current entitlement before requesting performance. If the discovered vendor request necessarily retrieves a broader authorized enterprise payload, constrain the service identity and handling policy, project only the selected permitted accounts before persistence into user report records, and never return a broader aggregate as the requested subset. Prefer native exact-account selection where supported.

The observed manager login and the July full-app login had very different account/model access. A valid JWT and an HTTP 200 are insufficient: the service identity must expose the required 49F accounts and report capability. Use an appropriately entitled service identity; do not turn a personal captured session into the production connector.

## 3. Adapter composition and concrete code changes

The current IRPT `tenants.py` selects one route per firm. `handler.py` explicitly handles Black Diamond and sends every other route through Orion. Therefore adding a SmartX name to the route map alone would dispatch incorrectly.

Implement a proposed `smartx_adapter.py` and an explicit provider dispatch table. Resolve a server-owned provider policy that identifies `SMARTX` as 49F primary and `BLACK_DIAMOND` as verifier. Route selection must also understand report basis: actual account, actual sleeve/allocation, selected-account aggregate, or model reference. Unsupported provider/basis combinations are explicit outcomes, not the Orion default branch.

Compose these boundaries:

1. **Registry/selection -> vendor crosswalk:** exact requested accounts, historical membership, source revision and authorized scope fingerprint.
2. **Token reader/recovery -> SmartX GET transport:** freshness/expiry checks, one coordinated bounded refresh, correct host allowlist, timeout/backoff, payload limits and safe diagnostics. Authentication expiry is distinct from insufficient entitlement.
3. **Request builder -> endpoint:** validated identifiers/dates/grouping; canonical encoded parameters; complete pagination where the endpoint proves it exists. Do not assume an unobserved pagination token or that window parameters constrain the response.
4. **Response parser -> adapter result:** retain node identity, report level, basis, period ranges, source units, completeness, and exact source-response revision. Select the requested primary node explicitly, never `nodes[0]`.
5. **Normalizer -> shared response:** conformant PerformanceReport and availability envelope, with errors/partial coverage mapped to usable UI states.
6. **Persistence -> UI/history/export:** write the immutable source/result records before publishing a durable ready revision; return its ID and retrieve the same revision for export.

Reuse parsing/reconciliation logic from `pull_smartx_model_monthly_performance.py` where applicable, but do not run that script as the client adapter: it hardcodes five portal models, uses a benchmark-oriented contract, rounds converted daily values, and skips incomplete rows. The new parser must retain/report omitted or malformed records and source precision. Existing auth/catalog code is reusable evidence, not production completeness proof.

The authentication guide's approximately 20 requests/minute is an empirical historical estimate, not a vendor SLA. Establish a shared throttle across IRPT and other SmartX consumers, coalesce identical eligible reads, observe 429/retry behavior, and use bounded payloads/concurrency. A daily token refresh cannot alone cover all-day interactive traffic with the previously observed approximately two-hour token lifetime.

## 4. Units, returns and comparison basis

The shared IRPT return unit is **decimal fraction**. Earlier source evidence distinguishes:

- Daily `pnl.percent`: decimal fraction (`-0.0096` means `-0.96%`); preserve that unit at the IRPT boundary.
- Monthly performance-service returns: percentage points (`0.84` means `0.84%`); divide by 100 when normalizing to the shared unit.
- Allocation-performance fields: units and methodology still require response-level proof; do not copy model-series assumptions onto them.

Do not multiply daily values by 100 merely because the older benchmark sidecar does so; that sidecar has a different output contract. Preserve original units in evidence and round only for display.

Compound a verified sequence of same-scope, non-overlapping subperiod returns only where its semantics support that presentation. Check continuity, partial periods, inception, and requested/actual boundaries; do not silently fill missing trading days or interpolate a monthly return into a daily chart. Do not average sleeve/account/model returns to manufacture account or household performance. Obtain the vendor's own calculation for the exact aggregate set; if unavailable, display verified component results and explicit aggregate unavailability until the account channel is completed.

Method, gross/net fees, accrual, cash, currency, reinvestment, annualization, valuation cutoff and benchmark must be supported by response or validated vendor settings. “Flow-adjusted” in a research note alone does not justify stamping every response TIME_WEIGHTED/NET. Unknown remains unknown and cannot pass a like-for-like certification.

## 5. Black Diamond verification, without changing the primary answer

Retain Black Diamond's existing period/series adapter and finish its authenticated request path. For an eligible SmartX report, obtain a separately identified BD verification result for the same canonical account set and comparable period/basis. Save both original response revisions and a verification receipt linked to the SmartX report.

The receipt records account-set equality, source cutoffs, requested/actual dates, method/fee/currency compatibility, beginning/ending value coverage where available, return differences in basis points, value differences, and reasoned status. Proposed statuses are `MATCH`, `WITHIN_TOLERANCE`, `MISMATCH`, `NOT_COMPARABLE`, and `PENDING/UNAVAILABLE`; final vocabulary belongs in the shared contract. Tolerances must be explicit, versioned and justified before acceptance, not chosen after seeing the discrepancy.

Compare account returns with account returns and sleeve returns with genuinely matching sleeves. A SmartX model reference and BD client account are not comparable merely because they share a model name. Same-day time differences or different fee conventions are explained before numerical grading. Missing/non-comparable verification is never a pass.

Black Diamond is a verification channel, not a blended contribution to SmartX returns. It neither overwrites the SmartX report nor silently becomes the primary when SmartX fails. A verified SmartX report may remain available while a later verification job is pending under an explicit release policy; unexplained material discrepancies block initial production acceptance for that case. Operational verification should run on the agreed sample/schedule or request policy, with both source revisions retained, rather than double every portal keystroke into vendor traffic.

## 6. Contract, frontend, storage and export

The current JSON schema and TypeScript `PerformanceReport` union admit only `BLACK_DIAMOND`, `ORION`, and `UNKNOWN`. Amend the authoritative PRD/contract source, regenerate compatible schema/types, and add **SMARTX** explicitly. Do not disguise SmartX as UNKNOWN or Black Diamond to pass validation.

Extend the agreed contract to distinguish actual-account, sleeve/allocation and model-reference basis; identify the selected scope and primary node; carry per-series/period coverage; and reference the independent verification receipt. The current `account_detail` shape must not be overloaded with a model ID masquerading as an account. Keep the shared response/availability envelope and update frontend fixtures, adapter, period table, chart, history and export together.

The 49F screen should clearly identify SmartX as source, show its actual data window, and make model context distinguishable from investor results. Verification status/detail can show the BD comparison without asking the advisor to choose which provider produced the primary number. Refresh creates a new immutable report revision. Current model holdings remain a snapshot tab, not a substitute for performance history.

Use the proposed reporting backend from `IRPT_REPORTING_BACKEND_AND_LGIC_MODEL_BRIEF_20260922.md`: reporting artifacts in the proposed, policy-bound `opal-data-irpt` families, and canonical client model/holdings Gold/Platinum in `opal-data-49financial`. That bucket proposal and its shared-private-artifact tenancy policy are not yet deployed. Register the exact request/report/verification destinations before writing; verification receipt state belongs outside Gold/Platinum. Raw recurring client/custodial facts follow their existing LGIC source planes; report artifacts pin the selected evidence rather than introducing a duplicate canonical account database.

Store normalized SmartX report, original source evidence, request/settings, account crosswalk revision, method/units, and BD verification as separately addressable records. Freeze the SmartX revision and the chosen verification/disclosure presentation into the export bundle. PDF values must match the screen's SmartX revision; export must not fetch a fresh BD or SmartX calculation.

## 7. Production proof and release sequence

**Stage A — close the account contract.** Walk a known 49F account's SmartX performance screen and capture the actual request/response with the intended service identity. Characterize the allocation endpoint and discover any account/aggregate endpoint. Produce a scrubbed fixture and field dictionary, actual account coverage census, and identified limitations. Model-only access cannot pass this stage.

**Stage B — prove paired adapters.** One account with known holdings and dates must yield a SmartX primary report and a separately sourced BD verification result through the real frontend request contract. Exercise date presets/custom dates, inception/partial history, one and multiple sleeves, non-model/cash exposure, model changes, and a multi-account selected subset. Demonstrate correct units and exact primary-node selection.

**Stage C — prove durability and recovery.** Persist/reopen a report, retry identical work without corrupting revisions, recover one expired token, distinguish revoked/insufficient access, survive throttling and payload limits, and preserve a prior accepted report as explicitly stale when refresh fails. Test mismatch and non-comparable verification outcomes. No raw credentials in evidence.

**Stage D — prove the production channel under the existing Dev-only gate.** Deploy compatible backend/frontend contracts, configure 49F SmartX primary with BD verification, and exercise the actual PROD route with authorized accounts. Trace selection -> SmartX source response -> stored report -> visible screen -> exported PDF -> verification receipt. Confirm the source is SMARTX in the saved record and rendered output. Broaden coverage only as the complete 49F account census and required aggregate scopes pass. A successful local fixture, research endpoint call, or model chart is not the production proof.

Required final evidence: production endpoint/adapter revision, report/run IDs, source-response hashes, exact selected account-set fingerprint, source/actual dates, coverage census, verification results with versioned tolerances, persisted report/export receipts, and reproducible UI/export observations. Uncovered account or aggregation capability is a named completion gap, never concealed by BD fallback.

## Evidence and implementation references

- `docs/architecture/DATA_PLATFORM_D4_smartx_endpoint_sweep.md`: June 24 sweep and dated vendor quirks.
- `docs/architecture/SMARTX_YALIU_HAR_FINDINGS_AND_HISTORY_PLAN_20260714.md`: July account-entitlement differences, nonzero sleeves and model-summary capture; underlying token-bearing HAR is not part of this packet.
- `docs/briefs/mdsrc-smartx-comprehensive-endpoint-inventory-20260521.md`: corrected daily model endpoint discovery.
- `data/smartx/API/AUTHENTICATION.md`; `domains/model-api/endpoints/{README.md,payloads/field_dictionary.md}`; `domains/performance/{DOMAIN.md,endpoints/README.md,endpoints/payloads/field_dictionary.md}`; `tools/sxpl_restin_probe.py`.
- `data/smartx/scripts/pull_smartx_model_monthly_performance.py`: existing daily/monthly parser and different benchmark output units.
- `infra/aws/lambda/smartx_jwt_refresher/lambda_function.py`; `infra/aws/lambda/smartx_rest_pull/lambda_function.py`: reuse points, not reverified deployment claims.
- `infra/aws/lambda/investor-reporting/performance/{handler.py,tenants.py,normalize.py,units.py,transport.py}`; `docs/contracts/investor-reporting/v1/PerformanceReport.schema.json`; `portal/src/pages/InvestorReporting/contracts/wire/PerformanceReport.ts`.
- The performance, model-overlay, storage-state and proposed reporting-backend briefs in this seat's deliverables, with their audit evidence. This brief changes the 49F primary-provider recommendation; their historical deployment observations remain historical facts.

## Andrew-direct requests — verbatim record

Channel: direct user messages to Codex seat 4.0.0_SA_CRO, September 22, 2026. Exact message timestamps unavailable.

> make sure that we get smartx adapter sorted for 49 FInancial as well, spec that out as additional brief, what endpoints and how it fits into the performance reporting suite as designed.

> Yes SmartX is preferable adapter to use for 49 Financial to prove that channel in production. it is good to have black diamond as well for verification on numbers

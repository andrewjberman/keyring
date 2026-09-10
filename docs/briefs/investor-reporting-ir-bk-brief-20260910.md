# IR BK — Investor Reporting backend project brief

**Author:** 4.0.0_SA_CRO · **Date:** September 10, 2026 · **Mode:** NEW project brief consolidating existing research.  
**Project:** **IR BK**, counterpart to [IR FE](investor-reporting-ir-fe-brief-20260910.md). **Two projects, no third umbrella.**  
**Canonical code:** `IRPT_BCKEND`, named by Andrew in the [five-message direction](../../org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260910_192xZ_FWD9_YES_FWD10_IMPOSSIBLE_BY_INGESTION_GATE.md) at `2dcd88091f`; the renamed [project endpoint](../../org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FWD_IRPT_BCKEND_20260910.md) carries it. IR BK remains the short name.
**Authority:** [Andrew's split instruction](../../org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260910_IR_FE_IR_BK_SPLIT.md), initially `6226b4a680`; [priority/device direction](../../org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260910_183xZ_IR_IS_THE_TOP_PROJECT_LAPTOP_AND_SPLITS_FE_BK.md), `c0f5ed8163`; [IRPT/D9 direction](../../org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260910_183xZ_MACRO_IS_IRPT_REGISTER_IN_D9.md), `1f0f1dd3f6`. **Both projects run on this laptop; Investor Reporting has highest priority across the board.**  
**Organization:** Macro **IRPT**, directive **D9**. IR FE and IR BK are the requested project names; Andrew has named `IRPT_FNTEND` and `IRPT_BCKEND`, superseding the withdrawn longer codes. CTO withdrew `OPAL_INVRPT`. These briefs replace the former one-project/WS1–WS4 organization without changing the eight permanent FWD IDs. Andrew subsequently moved **D9 as a whole to laptop** ([subsequent D9 placement direction](../../org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260910_185xZ_D9_TO_LAPTOP_CLDGRPH_FINISHED_15MIN_RATIFIED.md), `4ff4abd9a4`); CTO owns every L3 carrier and writes the tree row, generated index, directive members and macro enum in its own commit, with no MSTR gate ([LD-0542](../../org/tier0/ledger/LD-0542.md), `2f13cdbaeb`; Rule 27/spine correction `08722e8b86`). The placement/write-ownership question is closed. This brief closes no other project.\
**Consumer:** Andrew's design review, CTO's L2/PRD work and the backend delivery team alongside IR FE.

**IR BK owns ingestion, multi-tenant firm/advisor scoping, all ETL and serving operations, provider sessions/retrieval, normalizers, model joins, narrative evidence and export execution.** IR FE owns the client-facing product and the reusable presentation/rendering package. The backend makes the existing data useful: fast directories from Silver and established identity inputs; native BD/Orion performance; native YCharts analysis; current custody holdings with evidenced model overlays. It does not introduce a new return engine, alternate scenario engine or historical holdings product in v1.

# PART I — THE OUTCOME TERRITORY

### O1 — An advisor finds permitted clients quickly and receives only the authorized account population

Serve a compact directory keyed to the authenticated firm/advisor, with stable client/relationship/account identities, disambiguating labels, capability and source-date metadata. Resolve a selection into the unique permitted account set before retrieving any report. Reuse existing daily sources and identity relationships; no provider search per keystroke, whole-firm browser download or name-based authorization.

Every search, resolve, report, review, job-status, asset, export and download request enforces current server-side authorization, including warm caches. A relationship may contain both allowed and disallowed accounts: aggregate only the exact allowed subset or return an explicit unsupported scope. Never request the broader aggregate and hide detail rows afterward. Termination is separate from permission revocation: an entitled terminated client remains discoverable with the available dated records.

**Proof:** duplicate names, cross-firm IDs, overlapping advisor groups, narrow account selection, partly permitted relationships, entitled terminated clients and revoked grants on previously cached reports/downloads. Each response and downstream call has the same authorized scope fingerprint. Sources: S1 O1/O5/O6/F-C; S2 O1/O2; S5 §2; S9 §§2, 7–8.

### O2 — An advisor receives a comparable performance report without losing vendor semantics

Retrieve Black Diamond performance for 49F and Cottonwood using separate tenant routing, and Orion for Inflection. Normalize summaries, periods and daily cumulative returns into one contract with explicit units, method, fee/accrual treatment, dates, currency, scope, benchmark and coverage. Preserve source evidence and vendor-calculated aggregates. Missing or unsupported facts remain absent with reasons; do not reconstruct unsupported dollars, average returns or silently substitute a method.

**Proof:** paired native/normalized fixtures for each tenant, exact selected account sets, daily-to-period parity where meaningful and missing/annualized history cases. S6 proves only a bounded set of current endpoints; remaining scope/method proofs in IV.3 must close for supported production cases. Sources: S1 O3/O7; S2 O3; S6 §§3–7.

### O3 — A submitted holdings email becomes a durable, correctly scoped analysis request

Poll the forwarded holdings mailbox in the cloud every 15 minutes, **every day**, from 08:00 through 23:45 America/New_York. Read verified transport/origin metadata, bind the sender-derived firm through the ingestion gate, capture original message/attachments only to allowed destinations, resolve authorized client ownership, extract and validate inputs, and create a revisioned request. Deterministic parsing handles supported holdings formats before any analyzer proposes corrections. Preserve field-level provenance and the original attachment; current Silver holdings cannot replace what the request actually submitted.

Valid inputs may proceed automatically under the source proposal; uncertain securities, amounts, ownership or intent enter a specific correction state consumed by FE. There is no established universal analyst approval requirement and no automatic outbound email requirement. A duplicate delivery is not a new generation; a deliberate new request with identical holdings is not automatically a duplicate.

**Proof:** representative forwarded messages with real attachments, retries, restart during attachment persistence, pagination/checkpoint recovery, a repeated forward, a new request with identical holdings, unresolved tenant ownership and ambiguous positions. Sources: S3 O1/O2; S8 §§1–3, 6, 8.

### O4 — An advisor receives the correct YCharts variant and can recover an interrupted generation

Run Overview, Comparison and Multi-Comp through the captured YCharts flows using the **same runner style as BDAPI with Kimi**, adapted to YCharts. Store credentials/session material in Secrets Manager and durable report records in encrypted storage. Automation and Alyssa may evict each other's login; bounded session recovery is accepted. There is **no OTP branch** in the planned runner.

Track exact owned portfolio/report objects and immutable input/attempt revisions. Handle uncertain creates without blindly submitting again. Download and validate the actual PDF, then produce certified native sections for FE from paired output evidence. The captured report-generation calls do not themselves prove native section fidelity.

**Proof:** all three report variants, ordered comparisons, effective settings readback, an expired session, a shared-user eviction, a slow/uncertain report POST and a restarted worker. Source report bytes, hashes, validated sections and source coordinates must be available for the same request revision. Sources: S3 O3–O6; S8 §§4–9.

### O5 — An advisor sees current custody holdings with model percentages that state what they measure

Join permitted daily custody holdings to SmartX for 49F, Eclipse for Inflection and BD Rebalancer for Cottonwood. Serve a current snapshot with canonical category/model nodes, accounts, securities, source clocks, coverage and drill evidence. Model attribution may be observed allocation, assigned-account value or target attribution; these are distinct measures. Preserve cash, remainder, unassigned, unmapped and unavailable classification rather than forcing complete percentages.

**Proof:** the partner-specific joins in IV.5, reconciled unique account totals and drill denominators, unresolved models, missing allocation positions, stale assignments, recursive blends and signed values. No model's global AUM is a client's holding; target constituents are not observed sleeve holdings. Sources: S1 O2/O5; S2 O5; S4 O1–O6; S9 §§2–9.

### O6 — An advisor exports a branded, reproducible report with evidence-backed market context

Freeze authorized report inputs, optional advisor assets and a narrative packet into an export bundle. Run FE's versioned render package in the backend job runtime, validate the PDF and store an immutable receipt and protected artifact. Retrying the render uses the frozen bundle; changing branding creates an export revision without recalculating performance.

For the optional wide performance narrative page, detect drawdown/movement episodes from the verified return series before finding dated Trending Topic/Topic Cloud evidence. Supporting sentiment indicators are used only when historical coverage and units are established. Prose cites actual evidence and describes contemporaneous context without claiming unproved causes of client returns. Missing news history allows an explicit performance-only export choice.

**Proof:** same bundle across preview/render/retry, optional advisor logo, inaccessible or invalid assets, historical gaps, event-date/source-cutoff checks and factual/citation validation. Reauthorize the download even when the artifact already exists. Sources: S2 O7; S7 §§1–8; S8 §§6–7.

### O7 — A request is bound to its firm at ingestion and cannot write into another firm's destinations

Andrew's later FWD-10 direction fixes the request firm from the sender's email at ingestion. Bind it immutably before processing or firm storage, using verified origin evidence, an approved sender/domain-to-firm mapping and a pre-enumerated list of that firm's destinations. Neither corrections, retries, a Global viewer nor worker-supplied paths may change the bound firm or write into another firm's locations. Operator recovery exercises prove this gate; they do not substitute for it.

Provide source-completion manifests, explicit business/data clocks, immutable revisions, scoped queues/jobs, leases, retries and operator traces for directory refresh, performance, analysis, holdings and exports. Reconcile each published snapshot to its input lineage. Expose intelligible partial/stale/unavailable states through the shared status contract. Recover one provider or tenant independently while keeping unaffected functions available.

**Proof:** failed source partition, stale model map, duplicated event, expired lease, queue replay, worker restart and revocation during a job. Failed work cannot publish a falsely complete snapshot, overwrite newer output or resurrect permissions. A path manifest identifies each BRONZE/SILVER/GOLD/PLATINUM dependency and its owner. Sources: S1 O8–O10/F-I/F-J; S2 O6; S3 O6; S4 O6; S5 §6; S8 §6; S9 §7.

### O8 — An entitled Opal user can run the same reports for clients at every firm

Serve the Global view through the existing **multitenant `api/scoped/` layout**, with an explicit authenticated Opal entitlement class and a permitted firm catalogue. A selected client resolves to one verified firm and its exact permitted account set for the request, report, job and export. Firm advisors cannot acquire cross-firm permission by selecting Global or swapping identifiers. Global access never changes a previously bound request's tenant or mixes firm data/destinations within a report.

FE owns FWD-11 acceptance, the Model Portfolios-style dropdown/view and visible firm attribution. BK supplies the cross-firm entitlement and server-enforcement proof within that adjudication. The same client and source revision have identical values in Global and firm-scoped results. Cross-firm discovery must return firm discriminators and enforce current permissions; it does not authorize a new all-firm financial aggregate.

**Proof:** an Opal principal selects clients from two firms and generates a report and export for each through scoped routes; replay as firm advisors and refuse cross-firm access. Compare same-revision results, revoke Global permission, and verify every artifact remains within its request's immutable destination policy. Source: Andrew's later five-message direction and FWD-11 at `2dcd88091f`.

# PART II — WHERE THE BOUNDARY SITS

### II.1 What this team owns, and what crosses to FE

| Boundary | IR BK responsibility | FE handoff |
|---|---|---|
| Client discovery and authorization | Ingest identity, build viewer-scoped directory, resolve exact account sets, enforce grants on every route | Stable selection objects, capabilities and understandable denied/partial states |
| Global access | Explicit Opal entitlement, permitted firm catalogue and selected-firm resolution through `api/scoped/` | Global/firm selector capabilities and identical same-client/same-revision results with firm attribution |
| Performance | Vendor routing, retrieval, normalization and source parity | Ready-to-present summaries, series, account rows and method/coverage labels |
| Analysis | Mailbox, attachments/parser, request revisions, sessions, vendor generation, certified extraction and release state | Variant inputs, correction findings, job stages, released native sections |
| Holdings | Current-source selection, joins, classification, denominators and reconciliation | Revision-bound radial nodes, account/security drills and explicit bases |
| Branding and PDF | Ingest/validate scoped assets; freeze inputs; execute FE renderer; protect artifacts | Asset options, bundle for preview, job status and download receipt |
| Narrative | Select events, retrieve historical evidence, validate contextual prose | Dated annotations, event points, citations and coverage for FE composition |
| Operations | Schedules, runtime/IAM/KMS/secrets, queues/checkpoints, releases, lineage and diagnostics | Product status envelope without credentials or infrastructure payloads |

FE owns templates, chart/table layout, print styles and the **RenderPackage**; BK owns the worker/runtime that executes it. There is one rendering package and one backend export service. BK does not design a second client-facing dashboard, and FE does not duplicate vendor parsers or entitlement rules.

### II.2 Shared owners and limits of the consolidation

Coordinate source contracts with OPAL_ASSETS/D10, D1_CATVIEWS, ASSETCLASS_TAXONOMY, D3_MODELOVERLAY, ADVI_ECLDAT, WSE_COTMDL and MDPF3FIRMS. Coordinate authentication with PORTAL_AUTHHARD/ADVI_ROLGAT; the runner pattern with ADVI_BDAPIMIG.P1; shared YCharts session compatibility with YALP_MDSRC; historical market/news inputs with their existing producers; and manifests with OPAL_ADVIPOINTERS. Existing shared code owners retain their boundaries. Reusing a pure helper does not authorize widening its existing deployment or IAM role.

IR BK includes directory ingestion and all multi-tenant security formerly grouped under WS1. WS2-WS4 remain research labels. [Andrew's ownership/design correction](../../org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260910_192xZ_FWD9_YES_FWD10_IMPOSSIBLE_BY_INGESTION_GATE.md) at `68d8b16a91` supersedes the previous acceptance distribution: **IRPT_FNTEND owns FWD-1/3/4/5/6/8/11/12; IRPT_BCKEND owns FWD-2/7/9/10.** BK retains all provider normalization, join correctness, entitlement and export-runtime responsibilities as contributions to the FE-owned advisor outcomes. Those contributions must be read in FE adjudication; FE mocks cannot certify them. FWD-9 is ratified, FWD-10 remains the recut ingestion/storage construction requirement, and FWD-11 remains Global access on Andrew's word. FWD-12 design is now ratified at `5c18c88826` and belongs solely to FE; BK is not engaged on that outcome. Two separate decompositions/task-order sets/adjudications remain required; no cell is jointly owned. The selected BDAPI/Kimi runner strategy and no-OTP direction remain fixed user constraints.

S1's vendor retirement, historical cohort reconstruction, full analytical replacement and later agent/BI ambitions remain future context. Preserve independent supervision and billing semantics when authoritative; do not require the held historical return engine to deliver native vendor performance. V1 adds no holdings time series, trades, alternate scenario engine or automatic distribution.

### II.3 Shared contract inventory — producer and consumer boundary

These are **proposed canonical contracts**, not claims that routes or schemas already exist. BK owns identity, economic meaning, units, dates and wire compatibility. FE owns formatting/interactions and supplies consumer fixtures. Every contract carries schema version, permitted scope/revision, source timestamps and availability as applicable; server-only credential and vendor-routing fields are not exposed to the browser.

| Contract | Required meaning / fields |
|---|---|
| `DirectoryEntry` | Opaque firm/client/relationship/account IDs; display name and masked discriminator; permitted scope/capabilities; termination indicator separate from access; directory/source revision |
| `ResolvedScope` | Current viewer policy, principal class and entitlement revision; permitted-firm catalogue/selection for Opal Global access; verified request firm, unique permitted account set/fingerprint, requested versus resolved scope and partial reason; namespaced vendor IDs stay server-side |
| `PerformanceReport` | Source/provider/tenant lineage; requested and actual dates; currency/method/fee/accrual/annualization; summary/period returns, daily cumulative series, account detail; optional benchmark/value facts only when supported |
| `AnalysisRequest` | Immutable tenant/request/revision and ingestion-gate/destination-policy revision, verified original-sender evidence, original-message/attachment references, normalized holdings with source fields and units, report variant and ordered comparisons, settings, findings/corrections, stage and release policy/state |
| `AnalysisReport` | Exact request/attempt and vendor artifact hash, effective inputs/settings, typed sections with units/dates/source coordinates, disclosures, extraction validation, released revision and protected PDF reference |
| `HoldingsSnapshot` | Scope and source-set revision, business/as-of clocks, unique custody totals, node hierarchy, namespaced model/security IDs, observed/assigned/target basis, amount and denominator, parent/total percentages, provenance, coverage/remainders and drill references |
| `NarrativePacket` | Performance revision, event policy/version, dated peak/trough/recovery/movement events, cited historical evidence with cutoffs, validated prose, coverage and generation/model/prompt versions where used |
| `ExportBundle` | Immutable authorized report revisions plus selected sections, narrative packet, approved asset hashes, template/renderer/disclosure versions and render options; no live vendor requests during render |
| `ExportReceipt` | Export/bundle hash, artifact hash/location held server-side, page/validation facts, created/released timestamps, job state and authorized download route; no vendor signed URL in FE |
| `StatusEnvelope` | Operation and revision; queued/running/ready/partial/stale/unavailable/needs-correction/uncertain/failed states as applicable; source dates, safe retry/recovery actions, public reason code and internal correlation ID |
| `RenderPackage` — FE produces | Supported contract/template versions, deterministic screen/print components, fonts/assets requirements, print entry point and visual fixtures; BK packages and executes the compatible version |

Cache and idempotency keys include tenant, authorized account-set fingerprint, relevant source/schema/config revisions and operation parameters (dates/method/variant/input revision). Client names are never keys. Reauthorize before serving a cached result or artifact; a cache revision is not an enduring grant. Freeze response scope for async jobs and re-check access at consumption. Contract changes require compatible producer/consumer fixtures, not independently copied shapes.

# PART III — THE QUALITATIVE BAR

1. The backend answers the selected permitted population, with no broader aggregate hidden behind a correct-looking UI.
2. Equivalent provider facts share a shape; facts with different meanings retain different labels or capabilities.
3. Every holdings total and drill can be traced to a unique source grain and a stated denominator.
4. A valid request can complete programmatically; uncertainty results in a specific recoverable finding rather than a fabricated answer.
5. Rendering is reproducible from stored inputs and cannot silently change the performance or analysis revision.
6. Partial coverage and old source clocks remain visible through the serving contract.
7. Operators can recover bounded failures without a shared-login contest, duplicate generation or cross-tenant impact.

# PART IV — SUBSTRATE, SOURCE MAP AND IMPLEMENTATION PATHS

### IV.1 All four briefs and five supporting documents

| ID / source | Relevant sections | Backend requirements carried |
|---|---|---|
| **S1 — [Original unification brief](investor-reporting-unification-brief-20260909.md)** | O1–O10; F-B–F-F, F-I–F-M; Parts II/V/VII | Identity/cohort semantics, provider common shape, data-layer independence, business clocks, path manifests and future boundaries; dated restrictions/findings are read with later evidence |
| **S2 — [Lightweight brief](investor-reporting-lightweight-brief-20260910.md)** | O1–O7; Part II; F1–F6 | Fast directory, authorization, native performance/YCharts, daily overlays, independent lifecycle and narrative; former WS ownership replaced |
| **S3 — [YCharts brief](investor-reporting-ycharts-brief-20260910.md)** | O1–O6; F1–F7; Parts V–VII | Daily intake, parsed/corrected inputs, three variants, BDAPI-style session recovery, native output and durable revisions |
| **S4 — [Model-overlay brief](investor-reporting-model-overlay-brief-20260910.md)** | O1–O6; F1–F5; Parts II/V/VII | Current holdings, model basis, category drill, remainders, source age and operator lineage |
| **S5 — [Lightweight design](investor-reporting-lightweight-design-20260910.md)** | §§2–7 | Identity/provider maps, normalizer and serving boundaries, cache/export semantics and 31-path initial source index |
| **S6 — [Performance review](investor-reporting-performance-review-20260910.md)** | §§3–7 | Exact BD/Orion endpoints, units and response traps, selected-scope proof gaps and reproducible probes |
| **S7 — [Export/narrative specification](investor-reporting-export-narrative-spec-20260910.md)** | §§2–8 | Logo option, vendor export findings, deterministic events, dated market/news evidence, frozen generation bundle and proof |
| **S8 — [YCharts design](investor-reporting-ycharts-design-20260910.md)** | §§1–9 | Mailbox/checkpoint/parse flow, runner and secrets, endpoint/body recipe, storage/jobs, section shape, dependencies and missing specimens |
| **S9 — [Model-overlay design](investor-reporting-model-overlay-design-20260910.md)** | §§2–9 | Source grains, partner joins, taxonomy/denominators, ETL/publisher boundary and offline validation recipe |

All source code paths below are repository-relative unless prefixed with S3/Secrets Manager. Their existence and all nine source hashes are recorded in the [split evidence manifest](sources/INVESTOR_REPORTING_FE_BK_SPLIT_EVIDENCE_20260910.json). Behavior and live measurements retain their original source clocks; this consolidation does not make them fresh runtime tests.

### IV.2 Identity, tenant scoping and daily movement

Use `data/firm_registry.json` for the 49F/COT/INF tenant vocabulary, excluding test/demo populations. Integrate the current server-derived JWT/firm/advisor policy at `infra/aws/lambda-edge/auth-validator-edge/index.mjs`; headers/selectors supplied by browsers cannot become grants. Existing partner `roles.ts` files describe presentation vocabulary, not personal-book authority.

| Function | Existing paths / cautions |
|---|---|
| Typed daily source catalogue | `data/assets/scripts/silver/silver_registry.py`; `data/assets/scripts/silver/mirror_schemas.py`; `data/assets/scripts/silver/rebalancer_schemas.py`; `data/assets/scripts/silver/bd49f_dim_conversion.py` |
| 49F relationships and identity | `data/assets/scripts/gold/runners_49f/a01_dim_relationship.py`; `data/assets/scripts/gold/runners_49f/a06_dim_identity_crosswalk.py`; `data/assets/scripts/gold/runners_49f/d08_firm_ownership_map.py`; `data/assets/scripts/gold/runners_49f/bd49f_dim_portfolio_group.py` |
| Historical 49F crosswalk | `data/black_diamond/scripts/bronze/build_schwab_bd_account_xref.py` — fuzzy matching is reconciliation prior art, not an authorization rule |
| Inflection identity | `data/inf/scripts/gold/runners_inf/a00_dim_account.py`; `data/inf/scripts/gold/runners_inf/a01_dim_relationship.py`; `data/inf/scripts/gold/runners_inf/runner_common.py` |
| Cottonwood relationships | `data/cot/scripts/gold/runners_cot/a01_dim_relationship.py` — joint-founder/placeholder advisor roles do not prove an individual book |
| Partner role vocabulary | `portal/src/pages/AdvisorIntelligence/_partners/49financial/roles.ts`; `portal/src/pages/AdvisorIntelligence/_partners/inflection/roles.ts`; `portal/src/pages/AdvisorIntelligence/_partners/cottonwood/roles.ts` — integration references for FE and BK, not authorization grants |
| Business-date selection | `lib/trading_calendar.py` plus each source's completion manifest and contractual date |

49F crosswalk `match_method`, `match_as_of` and `in_0833_universe` matter. Opal `rel_*` identities are not native BD relationship IDs. The measured older 49F bridge had 29,907 rows with `is_primary` all null and a 201-group dimension; grouping overlap must not double-count accounts or manufacture primary economic credit. Inflection's bounded legacy identity fixture mapped 874 of 953 holdings accounts into the 19-rep roster, with five distinct reps and 293 households among those mapped accounts; the remaining 79 require a reason. These fixtures establish gaps, not current access grants.

Maintain BRONZE raw evidence → complete typed SILVER vendor facts → GOLD business Parquet → **PLATINUM JSON via the publisher** in `opal-data-portal-v2`. The product owns its derived outputs rather than depending implicitly on another page's Gold totals. Named legacy identity inputs can be reused as bounded, manifest-declared dependencies. S1's older six Gold trees/three bucket generations remain migration context, not an instruction to merge them blindly.

Select a completed source set by business date and trading calendar. Do not trust the newest partition merely because it exists, mix incomplete outputs or turn missing rows into zero. Carry-forward must name the older date and coverage. The original morning 09:00 ET intent is source context for daily serving, not a newly certified SLA; it is separate from the 08:00–midnight YCharts intake window.

**Sender gate and destinations, following Andrew's later direction:** maintain a versioned `FirmDestinationPolicy`, with its owner named at L4. Before the first request, enumerate every allowed firm bucket/key prefix, metadata/queue/job namespace and export/artifact destination, plus the sender/domain mapping and allowed execution roles. Runtime inputs select from that policy rather than constructing arbitrary destinations. A new firm, alias or location requires a policy update. The proposed shared `opal-data-ycharts` bucket fits only with separately enumerated firm prefixes, such as `firms/49financial/`, `firms/inflection/` and `firms/cottonwood/`, and enforced role/prefix permissions. These are proposed locations, not deployed resources; source read permission does not grant writes.

Verify original-sender evidence through the actual forwarding arrangement; the display From/body and the shared `requests@opalinvest.com` forwarder are not tenant grants. Unknown, spoofed, contradictory or unprovable origins cannot become firm requests. Before binding, unresolved intake may enter only an explicitly enumerated, separately restricted quarantine location. After binding, unresolved client/holdings fields stay within that firm. Opal Global is a separately authenticated portal entitlement; it cannot rebind an email request. An Opal-origin email without an established target-firm routing rule remains unresolved rather than guessing a firm from holdings or the mailbox domain.

**Existing Global/scoped integration sources:** `portal/src/pages/ModelPortfolios.tsx` and `portal/src/components/ui/PageSurfaceControl.tsx` supply the inspected UI pattern; `infra/aws/terraform/partners-api/api-gateway.tf` declares `/api/scoped/advisor-intelligence/` routes using CUSTOM authorization; `infra/aws/lambda-edge/auth-validator-edge/index.mjs` is the existing scope-check integration source. Follow that layout for proposed `/api/scoped/investor-reporting/...` routes. This limited inspection establishes integration points, not complete live Global enforcement or the final route schema. Do not copy the Model Portfolios demo-to-global translation or missing-claim fallback as a grant to private client reporting. L4 must trace the actual authorizer, handler and storage enforcement before implementation.

### IV.3 Performance adapter recipe and evidence limits

| Provider | Retrieval and normalization |
|---|---|
| Black Diamond, separately for 49F and COT | `POST /portfolioreporting/api/performance/performancePeriod` for summaries/periods; `POST /portfolioreporting/api/performance/performanceSeries` for chart data. Preserve native date/cumulative arrays and choose the intended `levels` or `combinedLevels` hierarchy without summing overlapping levels. Period `timeWeightedReturns.return` is decimal; retain beginning/ending market values and annualization metadata. |
| Orion, INF | `POST /api/v1/Reporting/Scope` with native household/account scopes, periods and daily breakdown. Summary `calculated-performance.performance` is decimal; daily breakdown `performance` is percentage. Link daily `factor` values as product minus one where the fixture establishes that basis. Identify response nodes by group path, `$type` and calculation ID together; calculation IDs repeat. |

The tested Orion `cumulative=false` fixture was 119,975 bytes, 92 daily rows and three groups; `cumulative=true` produced roughly 5.3 MB of repeated content. Use the compact supported shape. `startValue + valueChange` failed three of nine explicit valuation comparisons, so it is not a valid dollar-history shortcut. Daily/period parity is method-aware; do not compare annualized, MWR and cumulative TWR as the same quantity.

Reuse bounded helpers from `infra/aws/lambda/opal-assets/opal-assets-bd49f-reporting-pull/lambda_function.py`. `infra/aws/lambda/inf-pipeline/inf-performance-daily/pull_inflection_performance_dim.py` is saved-query prior art, not proof of the on-demand scope endpoint. Earlier reconnaissance lives at `docs/research/bd_dashboard_teardown/BD_DASHBOARD_HAR_TEARDOWN_20260721.md` and `docs/research/competitive_recon/orion_20260722/ORION_TEARDOWN_20260722.md`.

The September 10 evidence included nine HTTP outcomes, two initial 401s and seven successes including refresh, with six successful report calculations around 13:50–14:00 UTC. It does **not** establish 49F live-tenant parity, selected multi-account BD aggregation, Orion subset exclusion, all annualization/accrual/currency/benchmark cases or full historical coverage. Reproduce offline with `docs/research/investor_reporting_performance_20260910/probe_performance.py`; its live option is separate from an offline documentation check. Proposed TWR/net/YTD defaults remain explicit, not source rewrites.

### IV.4 YCharts intake, session library and explicit retrieval instructions

**Mailbox:** `requests@opalinvest.com` forwards into `opalbloomberg@opalinvest.com` on site Z, with holdings attachments. Proposed EventBridge Scheduler expression `cron(0/15 8-23 * * ? *)`, timezone `America/New_York`, provides 64 ticks daily including weekends and follows ET daylight saving. The schedule polls email; it does not log in to YCharts every 15 minutes.

Prefer the established cloud application/certificate pattern with effective Mail.Read access restricted to that mailbox; verify the resulting grant rather than assuming a filter narrows permission. Use folder delta, attachment retrieval/`$value`, immutable message IDs, `nextLink` pagination and durable `deltaLink`. Persist attachments and the intake receipt before advancing a completed checkpoint; use a scan lease and durable outbox/queue handoff. Define initial cutoff, overnight catch-up, delta expiration/resync and Retry-After behavior. Original MIME may be necessary to recover forwarded attachment/metadata structure. An unverified display From or body field is not a grant: verify the original sender, then apply the sender/domain-to-firm gate described in IV.2 before firm storage or processing.

Parse supported CSV/XLSX deterministically, retaining units, source cells, totals, security/share-class mapping, grouping and cash (`$:CASH`). Analyzer proposals cannot discard unmatched holdings or silently substitute ETFs. Capture any approved substitution explicitly. The newer recorded workflow uses annual `management_fee=0.003`; July's `0.01` is historical. Recorded settings include quarterly rebalancing, dividends false, oldest start, prior close, non-qualified and `^SPXTR`; verify effective values after creation. A default tax setting is not inferred client tax status, and a No Benchmark template does not remove the calculation benchmark.

**Session pattern and paths:**

- `infra/aws/ec2/bd-49f-auto-login/bd_49f_auto_login.js`, `infra/aws/ec2/bd-49f-auto-login/run-bd-auto-login.sh`, `infra/aws/ec2/bd-49f-auto-login/package.json`.
- `infra/aws/terraform/bd-49f-auto-login/iam.tf`, `infra/aws/terraform/bd-49f-auto-login/instance.tf`, `infra/aws/terraform/bd-49f-auto-login/main.tf`.
- Existing YCharts consumers: `infra/aws/lambda/ycharts-market-data-pull/ycharts_client.py`, `infra/aws/lambda/ycharts-session-capture/index.mjs`, `infra/aws/terraform/ycharts-pipeline/`.

Adapt the Node/Playwright runner with Kimi DOM fallback, transient EC2/SSM execution, versioned artifacts, native AWS egress and normal TLS. Use a separate YCharts host/role, not the BD host. The shared library exposes `getSession`, `probeSession`, `acquireSession`, `persistSession` and `withAuthenticatedPage`; use lease/fencing for automation. Replace BD's OTP-based success predicate with YCharts identity/cookie/authenticated-probe evidence. Unexpected challenges are explicit failures, not an invented OTP route. Alyssa may evict automation and vice versa; bounded reacquisition avoids a login contest. Preserve browser-managed CSRF/WAF rotation rather than relying on a cookie string alone. Kimi is the selected **browser runner** strategy, not a mandated model for email analysis.

The earlier authorized setup created and read-back verified `ycharts/login/credentials` in Secrets Manager. Credential values never belong in this brief, logs or repository. `ycharts/credentials` is an existing legacy cookie contract, left untouched; `ycharts/session/current` existed without an AWSCURRENT version at the earlier inspection and is a proposed coordinated session output. `astn/kimi/api-key` is the existing configured key reference. Coordinate compatibility with YALP_MDSRC; the older client assumes status 200 and is not by itself a parser for report 201 responses.

**Captured retrieval recipe — S8 §5 remains the detailed body/field authority:**

1. Resolve securities with `GET /search/suggest/report_securities?q=...` and `GET /securities/securities_info?securities=...`, preserving typed P:/M:/S:/cash identities.
2. Upload holdings through `POST /model_portfolios/fixed/holdings_upload/client`. The browser's multipart field names were **not captured**: use the observed browser upload first; do not invent a pure-HTTP upload schema. The captured response includes `status`, `errors`, `rows`, `weight`, `upload_record_id`, `isExtractedHoldings`.
3. Create through `POST /model_portfolios/fixed/` with the captured portfolio/items JSON multipart form, correct units and real upload record. A 201 returns `model_portfolio_id`. Assign an opaque deterministic unique name, checkpoint intent before submission and reconcile uncertain creates using owned identity/fingerprint/name. Never adopt the newest portfolio row.
4. Read back the exact owned object/effective settings; poll `GET /model_portfolios/{id}/status` for calculation readiness. Do not expose the global portfolio collection to a tenant.
5. Retrieve the template catalogue via `GET /custom_pdf_reports/generate/collection?securityId=...`, detail via `GET /custom_pdf_reports/generate/{template_id}`, and validate `POST /custom_pdf_reports/validate_report_securities/{template_id}` with captured `security_ids`/modules shape.
6. Captured templates: Overview `14141822` / `aggregate_security_overview` / primary / portrait; Comparison `14141824` / `aggregate_security_comparison` / primary plus one / portrait; Multi `14141847` / `multi_security_comparison` / primary plus two–five / landscape. IDs are captured configuration, not guaranteed permanent constants; the recorded Multi example contains two comparisons only. S8 preserves the 34-key August versus 33-key July body, single `secondarySecurity` versus Multi array, asymmetric null/empty shapes and duplicate cover fields. Validate the chosen template and preserve consistent fields; do not PUT global preferences.
7. `POST /custom_pdf_reports/{template_id}` is a slow synchronous 201 returning `report_url`/`zip_url`. Opal wraps it in its own async job; do not invent a vendor background job ID. Persist SUBMITTING before the side effect, reconcile uncertainty, and immediately download the returned short-lived URL from the allowed vendor host with TLS. Do not log signed query parameters. Verify actual PDF content/hash and retain an owned encrypted artifact.

**Records and serving:** `opal-data-ycharts` is the proposed SSE-KMS bucket; it was absent at the earlier 15:41:51 UTC inspection. No bucket or pipeline deployment is claimed here. Wrap S8's logical storage layout in an authorized tenant prefix, e.g. proposed `firms/{firm_id}/intake/YYYY/MM/DD/{id}/...`, `firms/{firm_id}/requests/{id}/revisions/{r}/...`, `firms/{firm_id}/generations/{id}/attempts/...`, then `vendor/report.pdf`, `sections/report.json` and `exports/{revision}/report.pdf` under the generation. Unresolved sender identity before binding can enter only a separately enumerated, restricted quarantine location. Once bound, the firm is immutable; unresolved client or holdings inputs stay within that firm's destinations. These are proposed opaque-ID paths, not current resources or raw customer-name keys.

Use DynamoDB tenant/request keys, immutable input revisions, leases/fencing and an outbox; queues carry IDs, not attachment contents. S3 holds immutable evidence/artifacts, not distributed locks. Validated automatic release remains proposed; exceptions go to FE correction. Do not assume all requests require manual approval. For native Analysis, certify text/table extraction with units, dates and source page/coordinates. Charts require reliable underlying data or an identified source-chart representation; do not infer financial numbers from unreviewed visual guesses.

The private packet `C:\Users\AndrewBerman\Desktop\YCharts Transcripts` supplies six transcripts, a manifest and three HARs; the profile records 1,085 entries and six report POST/PDF GET pairs. PDF response bodies are absent. Real output examples for all three families, the missing upload body, real forwarded-message/holdings specimens and effective mailbox access still need proof. `docs/research/investor_reporting_ycharts_20260910/profile_handoff.py` profiles the packet offline; raw HARs, credentials and holdings stay out of committed fixtures.

### IV.5 Partner holdings/model joins, classifications and exact paths

The September 10 investigation verified hashes for **23 Parquet objects** (19 Silver and four legacy identity), **15,753,977 bytes**, sampled around 17:27–17:36 UTC. Full source object keys, hashes, grain/profile counts and offline instructions live in [S9](investor-reporting-model-overlay-design-20260910.md), the [source list](../research/investor_reporting_model_overlay_20260910/source-list.json) and [model evidence](sources/INVESTOR_REPORTING_MODEL_OVERLAY_EVIDENCE_20260910.json). This is bounded measured evidence, not permission to infer complete identity or position attribution.

| Partner | Join, observed coverage and caveat |
|---|---|
| **49F: Schwab 0833 + SmartX** | The selected custody universe is **08335338**, not automatic inclusion of 08242234. Sept 9 custody: 7,442 accounts, 104,807 positions across 6,237 accounts. SmartX Sept 10: 7,453 mappings, 7,434 valid eight-digit keys and 7,431 joined mappings across 5,856 custody accounts using the declared eight-to-ten-digit zero-pad grammar. SmartX UUID is not custody accountId. All joined allocation IDs exist in the 9,980-row roster and valuation table; 7,402 have position rows, leaving 29 without position evidence. The map's allocation ID links the model. `account_allocations` is empty. SmartX intraday 13:06–13:08 UTC versus prior-day custody is a real mixed clock. |
| **INF: Orion + Eclipse** | Sept 10 positions: 35,974 across 953 accounts. Simple portfolios: 845; 790 non-null account IDs all join, 55 null. Model catalogue/composition union: 26 models, with one overlapping ID and no name conflict; 658 of 663 assignments resolve, five do not. Full portfolios include 13 multi-account objects absent from simple membership; do not repeat a full portfolio total for every account without membership evidence. Nullable numeric IDs need declared canonical integer handling; names are not IDs. `targetPercent` units remain to be certified. Managed/excluded flags and assigned-account versus observed-sleeve bases remain explicit. |
| **COT: BD custody + Rebalancer** | Sept 9 holdings: 18,917 rows, 969 accounts, 18,817 unique AccountID/AssetID keys; 100 repeated keys agree on market value. Aug 30 assignments: 950, of which 946 join current holdings; 23 custody accounts have no map. Join assignment `external_id` to custody AccountID, not a different numeric account identifier. Preserve unassigned separately. The 65-model roster includes 23 Opal models; 118 blend rows and 1,595 definitions support target structure. Custody value × recursively composed weights is **target attribution**, not observed sleeve value. The old overlay date must remain visible. |

| Function | Exact existing paths / reuse boundary |
|---|---|
| 49F membership and SmartX source | `data/assets/scripts/gold/runners_49f/b04_account_model_membership.py`; `infra/aws/lambda/opal-assets/opal-assets-silver-smartx/smartx_conversion.py` — reuse exact join/status logic; do not invent missing advisor attribution |
| Eclipse model prior art | `data/inf/scripts/gold/INF_E_00.eclipse_model_portfolios.py` — preserve account/portfolio/model grains and managed/excluded meaning |
| Shared/COT model builders | `data/assets/scripts/gold/build_dim_model_portfolio.py`; `data/assets/scripts/gold/build_cottonwood_mdpf_pair.py` — inspect target recursion, source ownership and reconciliation, not wholesale deployment reuse |
| Canonical taxonomy | `data/mdpf/scripts/gold/mdpf_category_registry.py` — use registered identities and classification rules |
| Category/model architecture | `docs/architecture/D1_ASSET_CATEGORY_VIEWS_PRD.md`; `docs/architecture/D3_ACCOUNT_MODEL_OVERLAY_PRD.md` — prior art for this brief, not a replacement IR BK PRD |
| Offline reproduction | `docs/research/investor_reporting_model_overlay_20260910/profile_snapshot.py`; `docs/research/investor_reporting_model_overlay_20260910/source-list.json` |

Do not union parallel position/assets tables into duplicate custody facts. For SmartX, roster, valuations and position rows are different grains; reconcile equity/cash/fees/accruals, not sum them. Missing positions are not zero. For COT, deduplicate only under a declared equal-value/null policy, additionally checking units/dates; incompatible duplicates become explicit exceptions. Recursive target expansion applies relative/absolute weights exactly once, detects cycles/missing nodes and preserves unresolved mass. The old helper's empty-list cycle handling is not acceptable. An Opal wrapper or Opal leaf retains its proper attribution; never renormalize only surviving Opal children. The newer COT DIVZ key is `opal_div_sma`; older 49F-only SMA statements are historical. Do not invent absent newer schema fields in the Aug 30 fixture.

Registry storage categories are models, strategy, alternative, insurance and client; display includes Models Primary/Custom and SMAs ETF/ALT. Client fee-taking Opal Supervised/Unsupervised and advisory Advised/Residual are **alternative partitions**, not four additive children. Vendor AccountSupervised is not Opal fee-taking status. Unknown classification raises an explicit state, not Client. An older MDPF insurance-view exclusion is not authority to remove holdings from this product.

The denominator is the unique actual custody population for the resolved scope. Assigned and target measures retain their own bases and cannot be spliced into a purported actual-sleeve pie. Carry percent of parent versus total, cash/remainders, signed values and unknown denominators. Securities/model IDs are namespaced; equal tickers across models do not prove position-level ownership. Summary and all drill requests bind to the same snapshot/scope revision.

### IV.6 Narrative evidence, brand assets and export execution

Detect events on a verified **daily cumulative TWR** series before display downsampling: growth `1 + cumulativeReturn`, running peak, drawdown `growth / peak - 1`, with peak/trough/recovery dates. Merge overlapping episodes and calibrate a declared materiality policy; the sources do not establish a universal numeric threshold. Do not substitute MWR, annualized returns or cash-flow-driven value changes, and do not zero-fill missing days.

Primary history: `opal-news-trending-daily` and `opal-news-articles` DynamoDB sources, plus `s3://opal-data-news-v2/trending_reports/YYYY/MM/DD/trending_report_HHMMSS.json`. The prefilter archive is not automatically the historical final Topic Cloud. Verify publication/cutoff timezone, rolling windows and archive coverage; a writer's local path date is not proof of ET semantics. Deduplicate syndicated context and exclude future information. Secondary RSI/regime/Fear & Greed/best-worst evidence requires historical date/universe proof; current neutral/fallback display values cannot become historical observations. Almost a year of usable coverage was requested, not measured in full.

| Source/execution concern | Exact paths |
|---|---|
| News production and curation | `infra/aws/lambda/news_layer3_curation/lambda_function.py`; `infra/aws/lambda/news_trending_analysis/lambda_function.py`; `infra/aws/lambda/keyword_drilldown_generator/lambda_function.py` |
| Existing historical/current serving boundaries | `infra/aws/lambda/portal_data_proxy/lambda_function.py`; `infra/aws/lambda/v2_portal/01_market_overview/lambdas/trending-topics-portal-publisher/lambda_function.py`; `portal/src/api/portal-proxy.ts`; `portal/src/api/endpoints/market.ts`; `portal/src/api/endpoints/sentiment.ts`; `portal/src/api/endpoints/trending.ts` |
| Brand and renderer references | `deck_generation/brand/opal_brand_guidelines.pdf`; `deck_generation/brand_spec/brand.json`; `deck_generation/engine/brand.py`; `deck_generation/brand/logo_package/Opal-Capital-Logo-Package/Full Logo/Full Color/Opal-Capital-Logo-Full-Color.svg` |
| Export fixture and profiling | `docs/research/investor_reporting_export_20260910/profile_export_capture.py`; `docs/research/investor_reporting_export_20260910/build_export_review.py`; `docs/research/investor_reporting_export_20260910/performance-export-review.pdf`; `docs/research/investor_reporting_export_20260910/FONT_LICENSE.txt` |

A constrained prose step may use only selected evidence IDs and must validate dates, quantities and citations. Market context may have coincided with a movement; causation or holding-specific attribution requires separate actual evidence. News text is data, not executable instruction. BK implements a bounded historical adapter and keeps existing news-producer ownership intact.

Andrew will supply optional high-definition advisor logos. BK verifies firm/advisor binding, supported type, dimensions, checksum/version and safe SVG resources, then stores approved assets. Resolve assets before rendering; no arbitrary URL fetch from a report field. FE supplies the fallback Opal template, composition and print package. Performance and export revisions are separate: the bundle pins scope, report, asset, renderer/template/disclosure and narrative policy/model/prompt versions. Package licensed local fonts and preserve CSS-pixel/PDF-point distinctions documented in S7.

The BD export capture has 139 entries and a 15-page sample, but its full queued package chain was not captured. It informs product requirements, not a dependency on reproducing BD's renderer. The four-page Opal PDF is synthetic visual prior art, not a generated client artifact. Queue/runtime rendering, PDF validation, encrypted storage, protected downloads, safe retry and release receipts belong to BK; page/chart design belongs to FE.

### IV.7 Evidence artifacts and proposed new code homes

- [Original lightweight evidence](sources/INVESTOR_REPORTING_LIGHTWEIGHT_EVIDENCE_20260910.json) and [original proposal extraction](sources/INVESTOR_REPORTING_UNIFICATION_PROPOSAL_20260909_extracted.txt).
- [Performance evidence](sources/INVESTOR_REPORTING_PERFORMANCE_EVIDENCE_20260910.json) and [export/narrative evidence](sources/INVESTOR_REPORTING_EXPORT_NARRATIVE_EVIDENCE_20260910.json).
- [YCharts source evidence](sources/INVESTOR_REPORTING_YCHARTS_SOURCE_EVIDENCE_20260910.json), [HAR evidence](sources/INVESTOR_REPORTING_YCHARTS_HAR_EVIDENCE_20260910.json) and [comparison field census](sources/YCHARTS_COMPARISON_REPORT_FIELD_SCRAPE_20260909.json).
- [Model-overlay evidence](sources/INVESTOR_REPORTING_MODEL_OVERLAY_EVIDENCE_20260910.json) and [split source/path manifest](sources/INVESTOR_REPORTING_FE_BK_SPLIT_EVIDENCE_20260910.json).

**Proposed, not existing:** feature-specific service modules under `infra/aws/lambda/investor-reporting/`, deployment definitions under `infra/aws/terraform/investor-reporting/`, and isolated derived-data runners under `data/assets/scripts/gold/investor_reporting/`. Separate handlers/queues by directory, performance, analysis intake/generation, holdings publication, narrative and export as operational boundaries warrant; this is a project brief, not a settled one-Lambda-per-row decomposition. Reuse existing protected transport/publisher infrastructure where its contract fits. Register every concrete read/write path and owner during implementation, including the proposed encrypted YCharts layout; no silent dependency on another page's Gold output.

### IV.8 Required detail coverage in the backend PRD

The backend PRD must map **every section of this brief and all nine source documents in IV.1** to the consuming FWD and implementation cell(s), or record **NOT CONSUMED with an explicit reason**. Print the denominator and all unmapped entries. Missing both a consumer and a reason is a PRD defect. Preserve the applicable endpoint/body recipes, source grains and joins, units, tenant gates, cache keys, source clocks, paths, failure controls, proof gaps and operational requirements in the downstream work. A short FWD description or a link alone is not a replacement for that detail.

The evidence manifest provides the section/source inventory, with coverage pending the actual PRD map. No cells or task orders are authored here. Keep BK's implementation and acceptance dependencies explicit inside its own project; FE-owned advisor outcomes still consume BK's verified data/execution proof. The two coverage maps must not become one combined project. Source: Andrew's seventh message and both endpoint landing obligations at `68d8b16a91`.

# PART V — WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

These are dependencies, not sequenced task orders.

- Current authentication/identity contracts and tested tenant routing are available, including account-subset authorization and grant revocation. Historical identity joins alone cannot establish them.
- Provider credentials and session permissions cover each supported tenant; the remaining performance scope/method fixtures exist before capability is advertised.
- The YCharts handoff's actual PDFs, upload/holdings specimens and real forwarded-message form are obtained; effective cloud mailbox grants and session-library compatibility are verified. Existing authorized credentials are used without copying secrets into briefs.
- Source owners provide completion/date semantics and resolve or expose missing identity/model mappings and target units. Canonical taxonomy/cohort rules remain authoritative.
- Historical sentiment/news evidence meets the chosen date/cutoff policy. Narrative coverage can be partial without blocking a performance-only report.
- FE supplies a compatible versioned RenderPackage and representative consumer fixtures. BK supplies frozen bundles and source/security/economic proof; both exercise the same real end-to-end revisions.
- Register owners carry the already-directed IRPT/D9/laptop representation and Andrew has named the canonical project codes; the extended FWD acceptance ownership and his ingestion/Global rulings are recorded in II.2. This bookkeeping does not reopen the settled two-project scope or delay drafting.

# PART VI — STATUS — NOT OUTCOME-BEARING

This is a September 10 consolidation after the split/priority/device/macro directions. Compilation and source/path-check clocks are in the evidence manifest. Live performance, YCharts/AWS and holdings findings retain the earlier September 9–10 clocks stated in their source evidence; this turn does not remeasure those services.

The previous research produced briefs, profilers, scrubbed evidence and synthetic presentation artifacts. The authorized YCharts login secret was created earlier; that isolated action is not a deployed intake/session/generation service. This brief creates no API, ETL deployment, bucket, scheduler, tenant grant, project row or task order. Documentation validation covers all nine references, local links, path status and FE/BK contract consistency. Publication is reported separately against measured `origin/CLOUD`.

The [IRPT_BCKEND PRD](../../org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md) landed at `d555a33482`, using this brief at `2acf23d8fd`; the project tree landed at `4c5e5fb513`. The [bounded L4 coverage review](sources/INVESTOR_REPORTING_L4_COVERAGE_REVIEW_20260910.md) checks the actual maps and records corrections for CTO. Table coverage alone does not certify lossless requirement carriage or implementation. L1 remains CRO-owned; CTO completes L2 through the L5 handoff; COO owns decomposition. This update changes routing/status references, not the product requirements in the pinned brief.

# PART VII — WHAT THIS BRIEF DOES NOT CLAIM

The bounded source profiles do not certify universal account coverage, fresh authorization, complete historical sentiment, all provider calculation methods, or native YCharts section parity. Proposed defaults and code/resource paths remain labeled. No return engine, vendor retirement, holdings history or broad legacy data migration is silently added. The nine source documents remain evidence authorities with their dated limitations; their former project/workstream ownership is superseded by IR FE and IR BK. FWD IDs remain permanent and formal acceptance assignment belongs to CTO.

## REFS TO CARRY

```text
BRIEF          docs/briefs/investor-reporting-ir-bk-brief-20260910.md
PROJECT        IR BK / IRPT_BCKEND; code named by Andrew at 2dcd88091f
MACRO/HOME     IRPT / D9; D9 whole to laptop directed, all L3 carriers written by CTO; no MSTR gate (LD-0542)
COUNTERPART    docs/briefs/investor-reporting-ir-fe-brief-20260910.md
SOURCE MAP     Part IV.1, S1-S9; four briefs and five supporting documents
PATH MAP       Part IV.2-IV.7; all functions plus companion evidence JSON
CONTRACTS      Part II.3; FE produces RenderPackage, BK produces serving/export contracts
EVIDENCE       docs/briefs/sources/INVESTOR_REPORTING_FE_BK_SPLIT_EVIDENCE_20260910.json
ENDPOINT       org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FWD_IRPT_BCKEND_20260910.md
PRIOR ENDPOINT org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FWD_INVESTOR_REPORTING_LIGHTWEIGHT_20260910.md (historical; distribution provenance)
SIBLINGS       Part II.2; source/auth/runner/taxonomy/news owners retain shared boundaries
EXISTING PRD   org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md @d555a33482 (CTO-owned)
EXECUTION      Laptop; highest priority across the board; no other-project closures by this seat
MEASURED AT    Compilation/path-check clocks in evidence; live findings retain source clocks
```

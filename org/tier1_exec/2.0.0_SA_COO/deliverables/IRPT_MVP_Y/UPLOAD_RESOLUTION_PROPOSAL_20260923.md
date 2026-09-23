# Analysis upload and security resolution: implementation proposal

Owner `2.0.0_SA_COO~Y`, 2026-09-23. For direct CTO review under
`4cdac345db11b6d7934f669adc4643f1111e03ad`. Requirements: CRO brief
`fa42eb206f`, `IRPT_ANALYSIS_UPLOAD_AND_TICKER_RESOLUTION_BRIEF_20260923.md`.
This is a proposal and path manifest, not implementation or deployment approval.
Actual-viewer/acting-submitter source `1385a126e7` and handoff `4a368e2a01`
were completed first. P reports prior adapter integration at `03de809d50`;
new factory integration and direct combined review remain ahead of this work.

## Independently measured baseline

Y reproduced four filled copies of the real downloaded template against source
`1385a126e7`. The original file was read without modification; SHA256
`2b8d09e5485081580b39a155a765307ee64b77281e632ba4e26794857957718d`.
Sheet `holdings_template`, A1 `Symbol`, B1 `Dollars`, extent `A1:AY305`, B2 dollar
number format. A2:B5 were filled in memory with AAPL/MSFT/$:CASH/ALPPL and four
amounts. Other cells and formatting were retained. Full findings are in
`UPLOAD_TEMPLATE_REPRODUCTION_20260923.json`.

| Input | Y-observed result |
|---|---|
| XLSX through upload validator | `CSV_FILENAME` refusal |
| Dollars: 10,20,30,40 | Four `AMBIGUOUS_CURRENCY`, one nonholding skip, one `UNPARSEABLE_QUANTITY` |
| Shares: 1,2,3,4 | One nonholding skip, one `UNPARSEABLE_QUANTITY` |
| Target Weight: .1,.2,.3,.4 | Four `UNITS_UNDETERMINED`, same skip/unparseable pair |
| Current Weight: 10,20,30,40 | Four `UNITS_UNDETERMINED`, same skip/unparseable pair |

Y independently inspected source: upload accepts only csv_base64/.csv; parser
has SHARES/USD/WEIGHT_DECIMAL and no current/target distinction. Portal
`fac3b6a0c7cb55dd75d3c190a1382ce710030381` restricts picker/validator to CSV
and displays one NEEDS_CORRECTION reason. Workspace `4a368e2a01` route manifest
and that Portal endpoint table mark upload NO-HANDLER-AT-HEAD. These are source
observations, not a measurement of today's served application. P's evolving
runtime branch must be reconciled before editing shared routes or packaging.

Y inspected generation upload code: parsed error lists are reduced to lengths;
job failure is `UPLOAD_NOT_VERIFIED`. The Kimi estate request payload specifies
model/temperature/max_tokens/messages, with no web-search tool configuration.
API integration source declares 29000 ms; live deployed timeout was not queried.
CRO's historical endpoint/rejection measurements remain CRO-attributed; Y made
zero vendor calls, secret reads, cloud queries or mutations for this proposal.

## Template adapter and immutable revisions

Add an explicit template reader rather than change the generic mail-attachment
parser's interpretation for every caller. CSV and XLSX use the same A/B contract.
Prefer sheet named holdings_template; otherwise first workbook-order sheet by
relationship ID, not lexicographic ZIP member name. Ignore other sheets and all
cells outside A/B. Stop at last nonblank A/B row; keep original row coordinates.
A1 permits Symbol/Ticker case-insensitively; B1 selects exactly Dollars, Shares,
Target Weight or Current Weight. Dollars means USD by this template contract;
cell display formatting contributes no currency evidence. Preserve original file
bytes and content hash, selected sheet, column header and original cell text.

Carry four distinct bases through normalization and disclosures. Weight bases
must remain distinguishable even though both produce dollars for the current
vendor recipe. Proposal: version the normalized template document as v2, retain
the existing v1 verifier/replay path, and have P admit the explicit v1/v2 union
in compositions. Do not reinterpret old accepted v1 bytes. Current/target weights
record exact decimal total, tolerance, residual and reference notional.

Recommend +/-0.001 sum tolerance. Accepted rounding uses proportional decimal
normalization to one with its factor and residual disclosed; no implicit cash
plug. Totals 95..105 produce a proposed divide-by-100 revision, requiring the
user's click. Outside tolerance requires correction. Shares require a dated
compatible price; no invented price. Merge duplicate canonical symbols only
after row census, retaining every contribution and a visible notice. Normalize
Cash/CASH/$CASH to $:CASH with a notice. Do not treat unknown identifiers as cash.

Initial bounds proposed: current 1 MiB original-file cap, 8 MiB expanded XLSX
cap, 2,000 A/B rows and 200 distinct symbols. Return a declared bound finding;
never silently truncate. Refuse unreadable/encrypted XLSX, external/formula
amounts without an independently accepted numeric value, nonfinite numbers and
malformed encoding. Do not execute formulas, links, macros or workbook content.
CSV cells beyond B are ignored consistently with the template contract.

P owns the upload wire transition: a closed file_base64/file_type arm for the
new template, with an explicitly exclusive legacy csv_base64 arm during client
migration. Never accept both encodings. Old retained input and accepted request
identities remain readable. A new file/correction gets new upload token, parent
revision/ref and an actual approving actor; no edits to old immutable artifacts.

## Complete findings, not first failure

Return findings[] with code, severity, sheet/row/column, bounded display value,
explanation and allowed action. Collect every independent row finding and each
file-level finding; show totals and all affected rows. No raw provider stack or
credential-bearing response is returned. Blocking rows prevent final freeze
until corrected or explicitly excluded; fail-soft AI means users can finish by
manual selection/exclusion, not silently omit unresolved holdings.

| Code | Meaning / action |
|---|---|
| FILE_TYPE_UNSUPPORTED | Use CSV or XLSX |
| FILE_TOO_LARGE / FILE_EXPANSION_LIMIT / HOLDING_LIMIT | Display actual and allowed bound |
| FILE_UNREADABLE / FORMULA_VALUE_UNVERIFIED | Repair unreadable/unsupported content |
| SYMBOL_HEADER_MISSING | A1 must be Symbol or Ticker |
| UNIT_MISSING / UNIT_UNRECOGNIZED | Choose one of the four B1 units |
| NO_HOLDINGS | No nonblank A/B holdings |
| AMOUNT_MISSING / SYMBOL_MISSING | Identify each half-filled row |
| AMOUNT_NOT_A_NUMBER / AMOUNT_NOT_POSITIVE | Identify every invalid, zero or negative amount |
| WEIGHTS_LOOK_LIKE_PERCENT | User-approved divide by 100 |
| WEIGHTS_DO_NOT_SUM_TO_ONE | Show actual total and tolerance |
| WEIGHT_RESIDUAL_NORMALIZED | INFO: show accepted residual and proportional factor |
| SHARES_PRICE_UNAVAILABLE | Supply dated price basis, use Dollars or exclude |
| CASH_SYMBOL_NORMALIZED | INFO: original cash label and canonical cash token |
| DUPLICATE_SYMBOL_MERGED | INFO: original rows and merged amount |
| TICKER_NOT_FOUND / TICKER_AMBIGUOUS | Resolve, suggest, substitute, manual pick or exclude |
| TICKER_CHECK_UNAVAILABLE | Provider/lease unavailable; never mislabel NOT_FOUND |
| TICKER_CORRECTED / TICKER_SUBSTITUTED | INFO: approved revision and disclosure |
| HOLDING_EXCLUDED | INFO: explicitly approved exclusion and original amount |
| RESOLUTION_ROUND_LIMIT | Three vendor-rejection rounds exhausted; manual choice |

## Deterministic resolution and advisory check/swap

One batch service receives distinct normalized symbols with original row mapping.
It checks scoped approved-substitution proposals and exact-identity cache, then
Opal canonical reference data through M-owned reader ports, then one YCharts
securities_info batch for unresolved identities. An Opal reference hit identifies
the security; it is not proof of YCharts availability without a still-valid
provider receipt. A stored substitution is proposed first, never applied without
this user's approval. Cache keys include provider, identifier namespace, source
revision and verified provider-account context; only complete successful reads
cache NOT_FOUND. Proposed FOUND/NOT_FOUND TTLs: 24 hours/15 minutes, configurable.

Check and substitute are distinct Kimi call kinds. Check gets unresolved symbol,
typeahead candidates and optional other symbols only, returning suggestion/null,
confidence and reason. Show "Did you mean ...?" only after deterministic FOUND
validation. No or no validated suggestion leads to swap: identify name/issuer,
security type, asset/subasset, region/cap or bond credit/duration, with evidence
URLs and up to three ranked comparable ETFs. Match the existing classifier
taxonomy, not a parallel taxonomy. Deterministically validate candidates before
display. One further swap may exclude all prior rejected candidates; then manual
selection/exclusion. Coarse segment/exposure similarity is sufficient; report it
as a proxy, not the original asset or a recommendation to trade.

User approval binds original input hash/revision, original row/symbol, proposed
symbol, provider validation receipt, source URLs/rationale, proposal version and
actual approving actor. Stale or foreign proposals refuse. Approval makes a new
retained input revision, preserving original evidence and exclusion census.
Accepted source descriptors/actor separation from e07 and Y1385 remain intact.
Report, on-screen review and PDF display original -> correction/proxy, rationale,
sources, date, approving actor, and current/target/notional treatment. A missing
disclosure is a publication blocker, not optional narration.

## Endpoints and harness

All routes stay behind existing api/scoped authentication/current-viewer guards.
Opal view filters do not narrow authority. Ordinary users retain tenant/owner
policy. Firm and actor come from trusted scope; browser fields confer no grants.

| Method and suffix under /api/scoped/investor-reporting | Closed request / result |
|---|---|
| POST /securities/check | symbols[1..200] -> ordered per-symbol FOUND/NOT_FOUND/AMBIGUOUS or UNAVAILABLE, provider ID/name/type/source/checked_at, denominator and cache counts |
| POST /securities/suggest | request token, symbol, optional context_symbols -> 202 resolution_id/status; eventual validated suggestion or actionable absence |
| POST /securities/substitute | request token, symbol, excluded candidates -> 202 resolution_id/status; eventual identified asset, evidence sources and validated proposals |
| GET /securities/resolutions/{id} | Current-authorized bounded result; never access by opaque ID alone |

Keep deterministic check within a measured request deadline below the declared
29 s gateway integration. Kimi uses durable asynchronous work with idempotency,
fencing, expiry and polling; the queue dispatcher carries IDs/hashes, not file
amounts or credentials. Retry a leased pending resolution without creating
another model task. Lease contention returns 503/Retry-After for synchronous
check; asynchronous work remains queued with bounded expiry.

`.tools/irpt-ticker-check.py` defaults to offline fixtures. Explicit authorized
endpoint mode supports check, optional suggest/substitute and poll; prints N
inputs, unique count, each outcome, unresolved count, latency and pin. No direct
provider login, upload or mutation. A 50-symbol mix is the acceptance harness
target, not a probe authorized by this proposal.

## Shared session, retries and unproven capabilities

All provider access uses the existing IRPT session and transport; never invoke
the credential-login gateway as a fallback. Source inspection found capture-host
publication lease/fence and per-job durable leases. Neither alone proves one
operation lease serializes independent report jobs and resolution calls. P must
adjudicate and implement that shared operation boundary with broker ownership;
the resolver requires its acquire/renew/assert/release port before any request.
Maintain at least 2 s between requests across consumers, not just each process.
Never hold the YCharts lease while waiting on a Kimi response; reacquire and
revalidate session/fence for candidate validation. Contention is a retry state.

Mirror estate call mechanics: model/configured budgets, temperature=1 for the
recorded kimi-k3 configuration, telemetry persisted before call, one transient
retry, timeout terminal, bounded JSON/fence parsing and the BADJSON/EMPTY/
LENGTH_STARVED taxonomy. Restrict retry to declared transient classes; the current
estate code loops HTTP errors more broadly than its prose. Treat provider output
as untrusted data; no commands or unapproved URLs are executed. Only symbols and
optional symbol context leave the estate, never quantities/client/firm/actor IDs.

Per-row vendor rejection is retained as sanitized structured evidence rather
than a list length. Map it to NEEDS_CORRECTION and expose it through owned status.
Each user-approved fix creates a new input and request; keep old one-shot mutation
intents. Limit the generation-rejection lineage to three rounds; prior rejected
proxies are excluded. Timeout/unknown outcome is not a missing-symbol finding.

The following remain explicitly unproven and are not performed here:

1. **Kimi web search:** local estate code does not send a tool configuration.
   Required next action is a bounded CTO-reviewed provider QA invocation using
   the approved same key, with actual tool support, returned sources, latency,
   token count and failure behavior retained. No alternate search vendor is
   chosen if unsupported. This intake grants no secret access or vendor probe.
2. **Session identity:** secret names/DescribeSecret metadata cannot establish
   that credentials and current session belong to the same YCharts user. Obtain
   redacted account-identity evidence from the session owner, or a separately
   authorized broker identity verification, without logging secret values.
3. **YCharts unknown symbol shape:** request Andrew's per-use authorization via
   CTO for 3-5 predeclared symbols, exact lookup and holdings-upload operations,
   one shared session, sanitized retained responses and cleanup/stop conditions.
   No capture is authorized by the brief. Performance Proxy is a separate
   optional probe; plain approved substitutions are the proposed first path.
4. **Cloud wiring:** P supplies reviewed exact ARN role policy, configured
   lambda/queue/storage/package paths and naming-registry-derived resources.
   Same-key design authority is not an applied secret/IAM grant. No cloud change
   or CLOUD push is included in this proposal.

## Exact proposed path manifest and writers

Paths below are proposals, not write claims over another seat. New paths are
marked NEW. P retains all shared schemas/runtime; M retains canonical source
semantics. Do not edit P/M paths in Y's implementation worktree.

| Writer | Exact paths |
|---|---|
| Y template/normalization | `infra/aws/lambda/investor-reporting/intake/template_reader.py` NEW; `intake/uploads.py`, `intake/portfolio.py`, `intake/corrections.py`, `intake/upload_entry.py` under that same root |
| Y resolver | Same root `intake/security_resolution.py`, `intake/resolution_entry.py`, `intake/resolution_worker.py`, `intake/resolution_kimi.py` NEW; names avoid collision with existing `_scope/resolve.py` |
| Y evidence/retry | Same root `ycharts/generate/recipe.py`, `ycharts/generate/job.py`, `ycharts/generate/frozen_worker.py`, `ops/status_loader.py` |
| Y UI | Portal `src/pages/InvestorReporting/tabs/analysis/ProspectComposer.tsx`, `prospect.ts`, `composer.ts`; `SecurityResolutionReview.tsx` NEW in that directory |
| Y tests/harness | Same backend root `intake/tests/test_template_reader.py`, `test_security_resolution.py`, `test_resolution_entry.py`, `test_resolution_kimi.py` NEW; `ycharts/generate/tests/test_resolution_retry.py` NEW; `.tools/irpt-ticker-check.py` NEW |
| P public contracts | `docs/contracts/investor-reporting/v1/AnalysisUploadRequest.schema.json`, `AnalysisUploadResult.schema.json`, `RequestComposition.schema.json`, `routes.json`; `NormalizedPortfolio.schema.json`, `SecurityResolutionRequest.schema.json`, `SecurityResolutionResult.schema.json`, `SecurityResolutionApproval.schema.json` NEW in that directory |
| P shared client/display/export | Portal `src/api/endpoints/investor-reporting.ts`; `src/pages/InvestorReporting/contracts/wire/AnalysisUploadRequest.ts`, `AnalysisUploadResult.ts`, `RequestComposition.ts`, `SecurityResolution.ts` NEW, `responses.ts`; `src/pages/InvestorReporting/contracts/adapt.ts`; `src/pages/InvestorReporting/render/PrintEntry.tsx`, `render/manifest.ts`; backend `infra/aws/lambda/investor-reporting/export/bundle.py`, `export/package.py` for explicit disclosure/contract compatibility |
| P runtime/infra | `infra/aws/terraform/investor-reporting/api/routes.json`, `routes.tf`, `integrations.tf`; `infra/aws/terraform/investor-reporting/intake/resolution.tf` NEW; `intake/iam.tf`; `infra/aws/lambda/ci/lambda-source-map.json`, `build-zip.sh`; existing `build-and-upload.sh` is a deployment path, not authorized for this proposal. P must name the current assembly installer before its edit |
| P broker/storage coordination | Existing `infra/aws/lambda/investor-reporting/ycharts/session/broker.py`, `reports/repository.py`, `reports/retention.py`; shared operation-lease port/path requires broker-owner adjudication before edits |
| M semantics | Reader interfaces for canonical security identity/classification/dated price; exact owned implementation path to be supplied by M, with no Y crosswalk/price fork |

Resource names/addresses must come from `lib/opal_naming.py`; if registry entries
are missing, P names the exact registry delta before implementation. Reuse P's
conditional retained/index facilities for resolution proposals and approved
library records with named families/retention; do not invent a parallel S3 store.

## Implementation sequence and acceptance

1. Preserve current combined Opal closure and integrate Y1385/P375/M485 first.
2. CTO adjudicates this proposal and unresolved shared operation-lease writer;
   P supplies exact remaining assembly/export/resource paths and reviewed wire
   compatibility. M supplies canonical reader/price/classification ports.
3. Y implements template/findings and deterministic resolver with offline
   provider fixtures. P integrates closed schema/client/runtime with exact pins.
4. Y implements async advisory check/swap, explicit revision approval, full
   disclosures and three-round rejection recovery. No live-provider claims from
   synthetic fixtures.
5. Under separately granted QA authority, capture real unknown-symbol responses,
   identity and web-search capability; then exercise the 50-symbol endpoint
   harness and one actual browser template -> check/swap -> approve -> frozen
   input -> generation -> on-screen/PDF disclosure trace. CTO grades the exact
   paired candidate directly; no CVO waiting gate.

Offline matrix includes every B1 basis, dollars formatting and stray cells,
fewer/more than 10 rows, second sheet, real Excel CSV export when available,
whole/decimal weights and residuals, cash variants, duplicates, every invalid
row, typo rejection, CUSIP bond/private REIT/fund, rejected first proxy, malformed
AI/no-source replies, provider outage, cache/library hit, contention, stale
approvals, ordinary/Opal access, revoked ownership, concurrent/repeated approvals,
expired retention and lineage round limit. A single missing findings row,
silent substitution, stale authorization or undisclosed proxy fails acceptance.

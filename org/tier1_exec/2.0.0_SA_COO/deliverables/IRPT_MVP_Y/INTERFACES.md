# IRPT Y interfaces - candidate v1

Owner: `2.0.0_SA_COO~Y`. Authority:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md`
v1.2. Candidate only; no deployed acceptance. Updated 2026-09-22.

## S3 normalized input

Implementation: `infra/aws/lambda/investor-reporting/intake/portfolio.py` at
`e7dd1c3c6c5148580726d6b87faeaa0b0599c0a7`, isolated
worktree `C:/Users/AndrewBerman/Desktop/irpt-mvp-y-20260922`.

`freeze_parsed_portfolio(parsed, owner, source, resolve_security,
declared_currency=None, prices=None, price_date=None, reference_notional=None)`
consumes the existing parser's ParseResult after reviewed corrections. Server
adapters supply verified owner, maintained security resolution, and dated prices.
The function does not authorize, fetch, persist, or dispatch anything.

Owner retains M's complete prospect-owner-v1 including `schema_version`, `firm_id`,
`principal_id`, `advisor_id`, `principal_class`, `ownership_fingerprint`.
FIRM_OPERATIONS may have advisor_id=null. No fake client/accounts.
CSV source is `{lane: CSV_UPLOAD, upload_id, content_sha256}`; the digest must
match parsed bytes. Custody source additionally needs a selected revision, exact
accounts, selection fingerprint and as-of. Its actual adapter awaits M's S2.

Output is `{input_id, content_sha256, document}`. Schema version is
`irpt-normalized-portfolio.v1`; input_id is `portfolio_` followed by the complete
SHA256 of canonical document bytes (sorted compact UTF-8 JSON, finite numbers).
Document records owner/source, parser digest, currency evidence, every accepted
original row and resolved security/revision, price evidence, declared skips,
findings, reconciliation and consolidated dollar holdings. Dollar amounts are
decimal strings recovered from source provenance, preserving cents beyond the
parser float's precision. No unresolved row is silently dropped.

Producer/consumer example (synthetic): CSV `Ticker,Dollars\nAAPL,$10.01\nAAPL,$2.02`
with maintained resolution `AAPL -> S:AAPL @ revision1` produces two provenance
rows and one holdings row `{security_id: S:AAPL, dollars: "12.03"}`. Recipe
consumer reads `verify_frozen_portfolio(result)["holdings"]`; persistence and
current access checks must precede consumption. Hash verification is not access.

Shares require exact-date USD prices with security ID and source revision. Weights
must sum exactly to one and require an explicit reference notional; output labels
`REFERENCE_NOTIONAL`, never client AUM. Undeclared dollar currency requires USD
confirmation. Nonpositive/unknown/unreconciled inputs refuse release. Corrections
must produce a new frozen artifact; correction UI/persistence is not yet wired.

## S4 report repository agreement

P owns `reports/repository.py`. Y agrees `persist` takes current principal before
verified owner. Existing AnalysisReport is unchanged. Existing request_ref is
`{request_id: string, request_revision: integer, attempt_id: string,
attempt_number: integer}`. Y owns durable acceptance/outbox/attempt/certification.
READY requires certified released content and P's successful repository receipt.

Sections consumer: `repository.get(current_principal, report_id, revision)["report"]`
is returned as envelope.data, not status and not a nested `{report: ...}` wrapper.
Store the repository receipt in Y durable state. Retrieval rechecks current access.

Requested P blob operations: immutable put/get/head using registered artifact
family and owned logical identity; SHA256 plus S3 object-version receipt;
same-byte retry idempotence and refusal of different bytes at the same identity.
Families: original CSV, normalized portfolio, frozen request composition, original
vendor PDF and extraction evidence. No caller-chosen bucket/key.

P supplies `ArtifactRepository.put(principal, owner, family, logical_id, data,
content_type)`, `get(principal, artifact_id) -> {ref, data}` and
`head(principal, artifact_id) -> ref`. Ref carries artifact_id/family/sha256/
version_id/byte_length/content_type/immutable. Replacement candidate `0754b10b6c`
repairs the independently reproduced Y-P01 Decimal receipt issue at `70598ece96`;
independent retest closed Y-P01 (evidence `52986b6c7d`). Y integrated it at
`48e9f4d4a6`; supplied repository tests 23/23 PASS in the consumer worktree.

Use canonical families ORIGINAL_CSV, NORMALIZED_PORTFOLIO, REQUEST_COMPOSITION,
ORIGINAL_VENDOR_PDF, EXTRACTION_EVIDENCE. CTO ruling IRPT-S7-01 at `bcd38bba00`
permits conditional placement only: no writable destination until canonical
register record and enforcement; P retention/IAM/IaC are required before live writes.

## S5 public request migration - P/M owner agreement recorded

Preserve current custody seven fields: request_id, client_id, account_ids,
snapshot_id, variant, comparison_keys, report_title. Validate and resolve every
field server-side. Browser request_id is an idempotency token, never authority.
Changing content under the same token must conflict; server request ID remains
server-owned. Unknown fields must fail visibly rather than disappear.

Prospect extension: add owned input_id, with client_id=null,
account_ids=[], snapshot_id=null; variant/comparison_keys/report_title/request_id
retain their meaning. Require exactly one custody or owned prospect basis. P owns
shared schemas/adapters; Y will provide the paired actual-entry/browser patch.
P agreed at 21:09:32Z; M agreed at 21:08:47Z and pinned ownership at `33e630885f`.
Paired frontend serialization, actual HTTP guard and runtime factory remain required.

## Request acceptance foundation

`ycharts/generate/{entry,submission,submission_service,acceptance}.py` at
`6dc4e888e23c9cf08f591c57456233d855cf5cc7`. SubmissionService requires explicit
M owner/current-access/input resolvers and P ArtifactRepository. It freezes all
browser fields, resolved input/profile/catalog, settings and recipe version;
REQUEST_COMPOSITION bytes precede atomic Dynamo acceptance. The retained owner's
access is checked again on retries. Missing runtime service refuses; the concrete
factory is not yet installed. This pin is not deployable completion.

DynamoAcceptance uses irpt-requests (tenant,request_revision) and irpt-jobs
(tenant,job), one conditional transaction. Request key: analysis#REQ-<digest>#1.
Identity binds firm/principal/browser idempotency token; content hash detects
changed inputs under that token. Composition hash binds actual frozen settings/data.
Pending outbox lives on the job row, separate from mailbox numeric sequences.
Tenant-scoped recovery retains pagination cursors on empty filtered pages.

Dispatch uses an expiring conditional claim, sends only canonical _keys IDs/hash,
then marks sent. Crash after send can redeliver: transport is at least once.
Repair `08b1fd5c99` leaves dispatch pending on a refused/unconfirmed claim; only
exact True from dispatch clears it. CVO Y-F01 closed, evidence `ee42e1a646`.
Durable worker intents must fence vendor mutations separately. P packaging/IAM
must include these modules, transaction/get/query/update access on the two existing
tables and existing generation queue send. No new table is needed by this adapter.

## Guarded prospect upload candidate

`bf50e40359` adds `intake/uploads.py`, `upload_entry.py` and consumer tests;
generate `entry.build_entry(service, load_prospect_owner)` injects the durable
service inside M's shared guard. `build_upload_entry(service)` serves proposed
`POST /api/scoped/investor-reporting/analysis/inputs`, `analysis-input-upload`,
CREATE_INPUT. P owns shared route/schema/build registration; no deployed handler
or route is claimed. Runtime factory and maintained adapters remain required.

Upload body: required `upload_token` (8..128 URL-safe ASCII), `filename` (.csv,
basename, <=128 characters), `csv_base64` (nonempty UTF-8 CSV, <=1 MiB decoded).
Optional `declared_currency` (USD), `price_date`, `reference_notional` (decimal
string). Unknown fields and duplicate JSON keys refuse. No browser owner or price.

Original bytes persist under ORIGINAL_CSV before parsing. Immutable `UPLOAD#UP-`
metadata binds firm/principal/token to filename/hash, complete M owner and artifact
receipt. Changed bytes under the same token refuse. Currency confirmation may
produce a new normalized revision under that same original upload. Unresolved
rows retain original bytes and return NEEDS_CORRECTION without an input ID.

NORMALIZED_PORTFOLIO artifact and `INPUT#portfolio_<sha256>` metadata retain the
original UP link. `load_owner(verified_tenant, input_id)` is the M Entry callback;
`read_input(principal, full_M_owner, input_id)` verifies current owner, both retained
records, immutable artifact receipt/hash and exact source binding before returning
`{document, owner, input_ref}`. Returned repository owner augments the full M owner
with `account_ids=[]` and `prospect_input_id=UP-...`; M authorization uses the
retained unaugmented owner. No fabricated client/custody account is created.

Thirteen offline consumer tests PASS at `9da7d87f99`, using actual M owner/Entry, Y parser/service and
P repository with conditional/version-aware AWS doubles. One test traverses both
guarded upload and analysis Entry; its acceptance adapter is a test double. The
separate seventeen submission tests exercise the actual Dynamo adapter with
Stubber. These are distinct boundaries, not persistent-service or E2E proof.

M confirmed maintained security/pricing and accepted custody adapters are pending.
P retention integration is pending: CTO `3c55f37800` approves irpt-retention-v1,
and adds PERFORMANCE_SOURCE_EVIDENCE (twelve families). Original eleven-family
carrier `25a9465c7d` was amended in `705dae3202` (same X10). No writable S7 destination, logical/physical
retention completion or deployment is claimed by this upload candidate.

## Foundation evidence and limits

Nine parser-backed tests pass, including large exact decimals, currency controls,
duplicate/cash, dated shares, weights, nonpositive/unknown positions and tampering.
Both normalizer Python files pass mandatory commit-gate. Sixteen additional actual
entry/service/boto3 Stubber tests passed at the foundation; seventeen pass with the
dispatch repair (two changed Python files pass gate). M Entry prospect guard
`a85e7d6329` integrated `89aadb255c`, fifteen actual Entry tests pass in Y.
Stubber is not a persistent service. Y1-Y7/S1-S7 remain ungraded. No durable worker,
vendor, browser/export, deployment or live permission was exercised by this candidate.

## Replay wire examples and explicit refresh lineage

Binding ruling: CTO IRPT-Y-REPLAY-01 `06a96c4df7`. Implementation pins:
upload `9da7d87f99`, submission/dispatch `08b1fd5c99`; P consumed upload at
`354adae366`. CVO Y-U01 closed in `6401215f60` using unchanged dependency-change
probes. This closure does not prove browser, expiry, concurrency or crash recovery.

The following body is an actual supported upload shape, with synthetic CSV bytes:

```json
{
  "upload_token": "example-upload-0001",
  "filename": "prospect.csv",
  "csv_base64": "VGlja2VyLERvbGxhcnMKQUFQTCwxMDAK",
  "declared_currency": "USD"
}
```

The server derives `UP-<sha256(canonical([firm_id,principal_id,upload_token]))>`.
Original identity binds the filename and exact byte digest as well as the full
verified M owner. Normalization identity is the tenant plus
`NORMALIZATION#<UP>#<sha256(canonical(options))>`. Options always contain exactly
declared_currency, price_date and reference_notional, absent values represented
as null. No credentials, owner or resolver revision comes from the browser.
Successful response data has this shape (angle-bracket tokens denote server
values, not browser inputs or invented measurements):

```json
{
  "upload_id": "UP-<64hex>",
  "input_id": "portfolio_<64hex>",
  "state": "NORMALIZED",
  "input_ref": {
    "input_id": "portfolio_<64hex>",
    "content_sha256": "<64hex>",
    "artifact_ref": "<full P immutable artifact receipt object>"
  },
  "portfolio": "<full frozen normalized document object>"
}
```

An unchanged retry must resend the same token, filename, CSV and semantic options.
Current authorization and original/normalized receipt reads run again. The retained
NORMALIZATION pointer returns the original input/hash before parsing, security
resolution or price resolution, even if those sources advanced. The actual tests
retain price 20 after the price provider changes from 10 to 20 for two shares.
Changing bytes or filename under that upload token raises
`UploadRefused(CHANGED_UPLOAD_SAME_TOKEN)`; public reason INVALID_INPUT. Do not
claim an HTTP 409 mapping that the shared response adapter has not supplied.

Actual supported prospect analysis body:

```json
{
  "request_id": "example-analysis-0001",
  "client_id": null,
  "account_ids": [],
  "snapshot_id": null,
  "input_id": "portfolio_<64hex>",
  "variant": "overview",
  "comparison_keys": [],
  "report_title": "Prospect Overview"
}
```

Replace the input placeholder with the exact accepted upload input ID. Complete
analysis identity binds verified firm/principal/browser request_id. The server ID
is `REQ-<first24hex(sha256(canonical([firm,principal,request_id])))>`, revision 1.
The accepted record binds SHA256 of the entire validated browser body and a
separate immutable composition hash covering resolved input/profile/catalog,
settings and recipe version. Response data is `{identity,stage:"RECEIVED"}`;
identity contains tenant_id, server request_id, revision="1",
ingestion_gate_revision and destination_policy_revision. Shared status is QUEUED,
with WAIT text distinguishing confirmed dispatch from pending dispatch recovery.
QUEUED does not mean vendor execution or READY.

Unchanged hidden retries retain the full body and browser request_id. A changed
input_id, title, variant, selection or any other body content under that same
request_id raises `IdempotencyConflict(CHANGED_INPUTS_SAME_REQUEST_ID)` before
resolving sources or sending. No silent token renewal in a browser retry callback.

An explicit correction to reference_notional from "100" to "200" currently has a
different normalization identity (changed canonical options), can reuse the raw UP
handle, and yields a new immutable input while the old input remains readable.
Submitting that input requires a new browser analysis request_id, for example
example-analysis-0002; the old actual analysis key cannot be rebound. Merely
changing provider data without changing semantic options is replay, not refresh.

**Paired source extension `318e140fb9`:** P agreed at 22:30:03Z to optional
`supersedes_input_id` on upload, paired with a fresh upload_token minted only from
an explicit correction/refresh action. The source consumer is committed; shared
schema and browser integration remain P's next work. A concrete refresh body is
the upload example above with upload_token="example-upload-0002" and an added
supersedes_input_id equal to the actual first response's input_id. Keep filename,
bytes and options unchanged for a same-options dependency refresh; deliberate
corrections may change them under the new token. Hidden retry resends that exact
new body and token, never mints example-upload-0003.

Y reads and verifies the prior owned input before any new storage. Reusing its raw
UP token with this explicit lineage extension refuses
REFRESH_REQUIRES_FRESH_UPLOAD_TOKEN. Original upload metadata binds the full
supersedes_input_ref; frozen normalized document.source carries the same prior
input_id/content_sha256/artifact_ref. Prior input and original bytes remain intact.
Reads verify the retained prior index and immutable artifact receipt and recheck
current authorization. Dropping or replacing lineage under an accepted upload
token conflicts. Different fresh UP identity and frozen lineage produce a new
immutable input even when holdings values are unchanged. The subsequent analysis
uses that input and a new browser request_id as described above.

Seventeen consumer tests plus eleven subtests PASS, gate 2/2. Explicit same-date
price refresh produces 40 while unchanged old request still returns 20. Missing
or foreign prior input refuses before new storage. Same raw-handle changed-options
support without this extension remains a distinct normalization identity, not
permission to rebind an accepted actual key. Browser wiring, P earliest-dependency
expiry/promotion (including lineage), actual concurrency and process-loss controls
remain outstanding. No complete IRPT-Y-REPLAY-01 acceptance is claimed.

## Worker and source-verified publication candidates

`2acea1aeca` adds DynamoGenerationStore on the existing irpt-jobs row: bounded
conditional lease, monotone fence token, composition binding, atomic vendor-intent
and SUBMITTING checkpoint, and conditional state writes. Seven Stubber wire tests
pass. Independent `0d3a30ed09` adds four controls (composition, expiry, foreign job,
release), with no new defect at that boundary. This is not Dynamo server expression,
concurrent/process-loss, assembled vendor recovery or verified READY proof.

`bcfbd380a12e88d06f2c26f7ad48f0ddc4feb212` adds
`ycharts/extract/publication.py`. build_publication invokes actual extractor and
certifier, returning `{fragment,evidence,evidence_sha256}`. It performs no write,
authorization or release. The caller must retain the exact PDF and evidence before
P report publication and only then checkpoint READY. Missing runtime factory and
publisher wiring remain explicit.

Numeric certification now re-parses the complete PDF crop and compares it with
the claimed number. Reproduction before repair: actual 0.30 percent changed to
123.3 with old token and coordinates still certified. The repaired candidate
refuses that mutation and a substring mutation; no supplied token can vouch for
a different value. CVO independently closed Y-C01 numeric repair in its 22:29:14Z
exact retest notice. This does not certify full extraction or publication.

Only uniquely located actual PDF text becomes a disclosure. Census prose, labels
standing in for disclosure lists/tables, and absent/ambiguous chart titles yield
explicit gaps. Chart title match identifies the actual page, not the census page
hint; representation is the full source page with no inferred number. Dates are
re-read on that actual page. P schema `b894019c95` admits undated_sections without
invented dates, merged `2d2c774452` with owner custody fixes. Combined economic and
schema tests 35/35 pass after materializing a missing sparse source dependency.

Publication tests 11/11 pass on actual offline PDF bytes. Three checked-in synthetic
variants have located scalars 24/47/70, emitted 23/46/69, undated 16/32/48, unlocated
records 34/47/60, and one withheld unit-conflict each. Ten chart candidates and sixty
disclosure candidates per variant are not falsely emitted where source content is
absent. These synthetic specimens do not prove real vendor coverage.

Proposed extraction_coverage sent to P: policy_version=source-verified-partial-v1,
scope=PINNED_CENSUS, status PARTIAL or COMPLETE_FOR_CENSUS, canonical census hash,
counts and explicit `{kind,id,reason}` gaps. Located scalar rows equal emitted plus
withheld unit-conflict rows; dated plus undated scalar counts equal emitted scalar
rows. Chart counts are separate although their rows share the public arrays.
Unlocated records can be per-field or per-column; they are not commensurate with
census_fields and must not produce a coverage percentage. Duplicate IDs refuse.
Any failed scalar certification or empty scalar population refuses the fragment.
CERTIFIED describes the emitted scalar denominator only; notes and coverage state
partial completeness explicitly. P accepted the shape/count meanings at 22:30:03Z;
its coverage schema commit and browser handling remain pending.

Retained-inventory correction `3a1256a0742b06c0cbc3fe44388c40b86cb7a3da` addresses
CVO Y-C02: at bcfbd380a1 a retained result could omit chart/disclosure lists and
claim COMPLETE_FOR_CENSUS. verify_extraction now rederives the candidate inventory
from the exact original PDF and census, comparing sections, charts, disclosures,
unlocated records, unit conflicts and denominators. Omission or mutation refuses
EXTRACTION_INVENTORY_BINDING; evidence carries source_inventory_sha256. This is a
pure local verification against original bytes, not a current-source/vendor refresh.
Fifteen actual-PDF tests PASS, gate 2/2; independent unchanged omission retest
closed Y-C02 in a4a45470eb. Use this pin rather than bcfbd380a1 for publication.

## Retained inputs and fenced publication handoff (23:00Z)

P coverage schema beecb3395a is consumed via84da42eced. Complete source fragment
validation bfe5a33e17 passes with the actual P schema (27 publication/schema tests).
The earlier proposed coverage shape is now accepted source schema. P portal
9b871431 is reported available; Y has not consumed or verified it.

Y acc55a4c727e3919f2a972072191e423b81200e7 requires P retained composition
aa1cfaea6b063acac5fc974d397d6a278daa17a0. Runtime must supply its enforced
ArtifactRepository to UploadService. ORIGINAL_CSV has empty dependencies for a
fresh upload, or the prior normalized artifact's retention_ref for explicit
refresh. NORMALIZED_PORTFOLIO depends on the original artifact's retention_ref.
Missing retained references refuse in an enforced composition. Legacy unretained
repositories remain an offline test seam, never a runtime enforcement substitute.
Five new actual Y/P consumer controls verify inherited earliest expiry,
unchanged retry lifetime, expired-parent refusal before storage, pending-policy
refusal and expiry during read. Combined31 PASS plus11subtests. Acceptance
promotion must traverse the same DAG oldest roots first; this is still unwired.
Canonical P policy remains PENDING_ENFORCEMENT; no activation is implied.

FencedReportIndex6cacc808879dc9f8c5a01e18eca6a9ff38d94e7a depends on
2acea1aeca400c19bfdfcbd94fba01f121ac67ee. Both files are under
infra/aws/lambda/investor-reporting/ycharts/generate/. Construct with trusted
P-derived report_id and current DynamoGenerationStore, then pass as report_index
to build_retained_repositories. Artifact repository retains its ordinary index.
The adapter's transaction checks exact job/composition/fence/worker/expiry and
CERTIFYING while conditionally putting P's unchanged report-index item. Reads
recheck the fence before and after; conditional recovery preserves the prior
receipt for P byte verification. User history uses P current-access enforcement,
not the worker adapter. CVO9d33387734 supplies bounded Stubber review only.
P R-P08 history final-release repair must be consumed and retested before claiming
history access/expiry closure.

Decimal recipe/transport386f2e1b49 keeps uploaded dollar text exact, verifies
echo using Decimal and serializes create weightings as exact JSON numbers after
checkpoint. CVO Y-D01 closed e91d9de9d7:19 supplied and7 independent PASS.
No session/vendor invocation or complete worker/READY claim follows.

Request composition6cbb714040 now passes the normalized artifact's retention_ref
to REQUEST_COMPOSITION and verifies accepted composition via actual retained
artifact head before submission dispatch, including unchanged replay. Apply
b258b1696c as well: CVO Y-S01 showed a missing service previously downgraded known
retained refs to the legacy offline branch. Known retention_ref with absent
service now refuses RETENTION_SERVICE_REQUIRED before new storage/accept/dispatch.
54 tests/24subtests PASS; unchanged independent retest is underway.

P upload request/result/response schemas5add22ca9f consumed0bfd68b81669e7bbe25463700d5952e01c67212f;
paired guarded Entry/schema and retained consumer controls19 PASS. Shared portal
uploadAnalysisInput atcb62721c is ready for Y-owned UI integration. Canonical
route stays NO-HANDLER-AT-HEAD pending actual runtime factory and package proof.

M's23:08Z finding corrects the pending security seam: canonical local security_key
is not automatically a YCharts security_id. Prefixing ticker with S: is not proof.
The existing recipe uploads source identifiers and keeps vendor-returned identity
for create; current captured fixture includes unprefixed SPY/AGG. No general
retained vendor crosswalk is known. Y proposed an additive explicit local
security_key, canonical_identifier, canonical_identifier_namespace and
resolution_revision result to M, with local-keyed prices and separate future
vendor-readback binding. This proposal is not yet an implemented shared contract.
Captured template comparison entries remain recipe configuration; firm/advisor/
client profile values require maintained authorized sources.

## Agreed local security resolution (23:17Z)

M agreed the exact additive fields at23:13:12Z. Y source d99a072742 implements:
resolver(identifier, namespace) returns security_key, canonical_identifier,
canonical_identifier_namespace (TICKER/CUSIP/CASH), resolution_revision. Example
test-only resolution is security_key="custody-key-SPY", canonical_identifier="SPY",
canonical_identifier_namespace="TICKER", resolution_revision="pinned-dimension".
Real adapters must use maintained local keys and pinned source receipts; these
test spellings are not runtime defaults.

Frozen evidence and consolidated rows carry identity_kind=CANONICAL_SECURITY,
security_key and those canonical fields. They carry NO security_id. Holdings also
declare identity_kind=CANONICAL_SECURITY. Prices are keyed by security_key and
must repeat that exact key, requested date, USD, positive decimal price and source_revision.
The canonical cash token is $:CASH with CASH namespace; only M's explicitly
identified cash source may produce it. One local key with conflicting identity/
revision, one canonical alias mapping to two keys, and mixed local/vendor
resolutions refuse the entire normalization. Duplicate source position rows
consolidate only under one identical resolution. Legacy captured vendor-resolution
documents remain readable unchanged; no local ID is synthesized into that branch.

No downstream vendor identity is asserted. The future worker must translate
canonical identifiers to its upload request and retain/verify actual returned
vendor identity before create. Existing worker is not yet wired to this new lane.
Actual parser-backed local tests plus upload/retained/shared-schema tests:
48 PASS and18subtests; gate2/2. Maintained M source implementation is still pending.
P upload result portfolio is explicitly an opaque producer object, so the shared
wire schema remains unchanged. CVO Y-S01 independent closure10b5b7f25c at
b258b1696c is recorded separately from this new normalizer source.

## Prospect browser candidate (23:32Z)

Portal2ddf1114 builds on Pcb62721c plus exact digest binding repairc86a5eb5.
ProspectComposer sends the shared upload request with original CSV base64 bytes,
optional USD confirmation/date/reference notional and one action token. Retry
retains that prepared body in memory; explicit refresh uses a new token with
supersedes_input_id. Normalized source rows and exact dollar strings are shown
before Overview submission. The analysis body references accepted input_id and
sets client_id/snapshot_id null and account_ids empty; no browser firm/advisor
authority or fabricated custody selection is sent. Scope revision changes remount
the composer. P's route continues to refuse before transport while uninstalled.

This is bounded UI source, not a complete browser workflow: reload loses local
retry state, comparison catalog selection and request/report reopening remain
unfinished. Six helper/shared-adapter/initial-SSR controls and five P upload
controls PASS,50 assertions; full project TypeScript PASS. No connected browser
was available for visual or event interaction verification. Backend090c819803
aligns accepted identity with canonical AnalysisRequest fields (tenant_firm_id,
revision1, immutable=true), separately checked by45tests/24subtests.

CVO local identity reviewb43fba4bd3 reports40supplied/18subtests and10independent
PASS. Actual maintained M sources and local-to-vendor upload/readback remain
pending. This review does not reopen or pass any integrated criterion.

## Normalized input to vendor upload (23:45Z)

Backendc2a01fb3f8 adds ycharts/generate/normalized_input.py. After current
authorization and retained-artifact verification, prepare_normalized_upload(frozen)
verifies the exact input and returns rows for recipe.step_upload plus local
identity_bindings. Only canonical identifier and exact USD quantity go into the
measured Symbol column. A collision across namespaces that this column cannot
represent refuses; no vendor prefix or gross/net/signed conversion is guessed.

After the worker records/fences its upload mutation intent and calls the actual
recipe, bind_normalized_upload(frozen, upload_checkpoint) rechecks exact input,
positive upload record identity, successful Dollar reconciliation, every unique
returned security ID and exact weighting, and required create display fields.
It returns detached vendor rows for recipe.items_body and a local-to-returned
identity record bound to input_id/content_sha256. The measured recipe requires
exact symbol echo; different vendor IDs require separately evidenced crosswalk
support and currently refuse. Both functions are pure; they do not provide
authorization, retention, mutation claims, vendor execution or READY publication.
Flat package dependencies include intake/portfolio.py and recipe/transport.
15 bridge controls;46 combined tests/7subtests PASS. CVO independent1308dd5a64
reports46 supplied/7subtests and11 independent controls PASS.

## Owned request and report reads (2026-09-23 00:09Z)

Backend e93300e34b exposes OwnedRequestReader.read(verified_principal, issued_id)
and history(verified_principal, limit=25, cursor=None). Public read is
{identity: AnalysisRequest.identity, accepted_at: integer epoch seconds}; history
is {items: read[], next_cursor: string|null}. Fixture:
ops/tests/fixtures/owned_request_history.json. One consistent tenant query,
limit1..50; untrusted owner/tenant-bound seek cursor <=2048 characters; empty page
with continuation allowed. Request-key order is not newest-first order.
Retained full owner/current grants and composition are verified before release,
including final checks after all blob I/O. Checks are sequential, not atomic.

Backend9ac485733e OwnedAnalysisReader(requests=reader,reports=retained_reports)
reads by issued request ID. Actual DynamoGenerationStore binds accepted
composition hash; READY selects immutable P report ID/revision. Report index
full owner must equal accepted owner, kind ANALYSIS, and report.request_ref
request_id/request_revision must equal accepted identity. Actual P get performs
schema/blob/hash/current-access/retention verification. Final job/index/current
owner/both retention checks precede returning the complete AnalysisReport.
NonREADY raises AnalysisUnavailable; this is not a StatusEnvelope. The reader
does not certify reports or make READY transitions. Runtime package needs
ops/owned_requests.py, ops/owned_report.py and generate/durable_job.py dependencies.

P agreed GET /analysis/requests (analysis-request-history) and
GET /analysis/requests/{requestId} (analysis-request-read); sections operation
analysis-report must use the reader's sections() projection once composed, not
its full internal read(). P corrected the earlier full-response proposal:
156a01e114 preserves only request_ref, sections, extraction_validation and optional
undated_sections/extraction_coverage. Vendor artifact/disclosures/release stay off
this route. Fixture ops/tests/fixtures/owned_report_sections.json is generated by
the actual reader; existing closed response schema validates the projection and
rejects full internal report.745c02890e requires actual string READY receipt
fields; CVO closed Y-R01 in6a9d38ffad with unchanged probe12/12PASS.
M6ad86009fe is consumed at ca934b4919. Owned Entry callbacks receive verified
registry tenant/operation/issued path reference; load complete retained owner and
reauthorize it before/after compute. Factory8e8498c9c0 adapts current_owner to Y's
two-field verified principal port. Current status-summary stays on its existing
guard.28 actual Entry controls PASS; P runtime assembly/route installation pending.

## Prospect status dates agreement (2026-09-23 00:30Z)

Authority: CTO IRPT-Y-DATES-01 dea338a397. P proposal00:22:09 and Y agreement,
with00:24:02 correction preserving established portfolio_<64hex> input spelling.
Extension is only status-job with X-IRPT-Status-Dates: prospect-v1; old/unknown
capability gets ordinary UNAVAILABLE with no extra fields until compatible.
operation_kind is prospect_analysis, operation ID/revision bind accepted request.
source_dates has date_basis UNDATED_INPUT|PER_SECTION, business_date absent, and
closed prospect_analysis {source_lane:PROSPECT_ANALYSIS,input_id,content_sha256,
request_id,request_revision,report_id,report_revision,immutable:true}. IDs/hash
and accepted revision must agree with retained artifacts, not just string shape.
section_dates has unique stable section_id and actual ISO as_of_date or explicit
null for undated, <=1000 entries, IDs<=200. UNDATED_INPUT has only undated entries;
PER_SECTION has an actual date plus distinct dates or an undated entry. A valid
single source business date retains ordinary dated contract. No timestamp/default
or parsing/provenance failure qualifies. P shared schema/client pin pending;
Y retained derivation/paired fixtures in progress. All integrated criteria remain
NOT_EVALUATED; READY additionally requires accepted verified report.

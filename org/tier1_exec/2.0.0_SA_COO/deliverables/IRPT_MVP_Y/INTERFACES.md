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

## Evidence and limits

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

Ten offline consumer tests PASS, using actual M owner/Entry, Y parser/service and
P repository with conditional/version-aware AWS doubles. One test traverses both
guarded upload and analysis Entry; its acceptance adapter is a test double. The
separate seventeen submission tests exercise the actual Dynamo adapter with
Stubber. These are distinct boundaries, not persistent-service or E2E proof.

M confirmed maintained security/pricing and accepted custody adapters are pending.
P retention integration is pending: CTO `3c55f37800` approves irpt-retention-v1,
and adds PERFORMANCE_SOURCE_EVIDENCE (twelve families). Original eleven-family
carrier `25a9465c7d` requires amendment. No writable S7 destination, logical/physical
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

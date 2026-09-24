# Analysis 12.03 live journey -- executable runbook (COO~Y)

Owner `2.0.0_SA_COO~Y`. Written 2026-09-24 00:2xZ; REVISED 19:1xZ for the deferred upload (CTO 100667 shape 2, Y
`bb1eb7f92b` / `10a16bd89d` / `d16b7c8743`, P patch `P_UPLOAD_COMPOSITION_20260924.md`). Purpose: the moment P's
deploy lands, Y runs this top to bottom and records the digests it names. Every hop states its owner, the exact call,
the readback that proves it, and the refusal that would stop it. Nothing here is a claim that a hop is live: the
PRECONDITIONS table is the measured state, and each row names who moves it.

## Preconditions (measured 2026-09-24 19:0xZ unless stated; owner per row)

| # | Precondition | Measured | Owner / carrier |
|---|---|---|---|
| A | Host `i-0167fd745ad906a66` RUNNING and held running | DONE 01:52:51Z (P plan 04c77cbe) | done |
| B | Resident installed and polling, single consumer on `irpt-generation` | P receipt 100483: active since 09:39:24Z, package `ab2e088b5b`. Not re-read by Y on the host. | done (P) |
| B2 | **Resident REBUILT with Y `bb1eb7f92b` BEFORE (or in the same window as) the generate deploy in D** | The installed package predates `resolve_upload`. Its `execute` requires `request_id`, so a `resolve_upload` message raises. The message is retried until the DLQ (maxReceiveCount 5), and the upload stays RESOLVING. | P: package + cutover under the ledger |
| C | Current-authority reader on the host role | APPLIED 00:17:29Z (P 99840) | done |
| D | Upload route composed: `irpt-ycharts-generate` at a pin carrying the P patch + Y's three commits + P `19b38e2f22` | Deployed today: handler `generate_installed.lambda_handler`, LastModified 11:21:10Z, CodeSha256 `4fkloyC1...`. That build's upload service is `UploadNotComposed` (NOT_READY). Env carries `IRPT_DIRECTORY_BUCKET_MAP` and `IRPT_GENERATION_QUEUE_URL`. | P: apply, rebuild, deploy (ledger) |
| D2 | Grants (patch note table): generate role writes UPLOAD#/NORMALIZATION# + ORIGINAL_HOLDINGS; resident role writes NORMALIZATION#/INPUT# + NORMALIZED_PORTFOLIO | not read by Y | P: ledgered plan |
| E | Status routes `GET .../analysis/requests[/{requestId}]` declared and served | P batch 42/43 served the three Analysis routes. Not re-read this tick. | P |
| F | Queue `irpt-generation` | 0 visible / 0 in flight, VisibilityTimeout 900, MaximumMessageSize 4096, DLQ `irpt-generation-dlq` maxReceiveCount 5, DLQ depth 0 | measured |
| G | Real login; an Opal viewer, since partner viewers stay refused until `ordinary_authorizer` has a producer | Andrew's browser | Andrew |
| H | Vendor session `ycharts/session/current` captured and graded | run 7 (08:56Z), CRO PASS 100466 | done |
| I | Portal upload screen polls RESOLVING by re-POSTing the same body | Y interface to ~D at 18:29Z | 2.0.0_SA_COO~D |

## The journey, hop by hop

Fixed inputs:
- the template CSV `Ticker,Dollars` / `AAPL,10.01` / `VNQ,2.02`; the v2 template lane, units Dollars;
- expected frozen total 12.03;
- variant `auto`, which derives Overview for one portfolio; `comparison_keys` empty;
- `prepared_for` a real recipient string; `report_title` "Retained input analysis";
- firm = the signed-in user's storage firm (`tenant`).

| Hop | Act (actor) | Exact call | Proves / expected | Readback (Y records) | Refusal signatures that stop the run |
|---|---|---|---|---|---|
| 0 | Sign in (Andrew) | portal login; Investor Reporting > Analysis tab (`tabs/analysis/AnalysisTab.tsx`) | scope bootstrap resolves; header carries firm | portal network: `GET /api/scoped/investor-reporting/status` 200 envelope | `CONTRACT_VERSION`, `NOT_AUTHORIZED` |
| 1a | Upload template (browser via `ProspectComposer.tsx`) | `POST /api/scoped/investor-reporting/analysis/inputs` body `{upload_token, filename: "aapl-vnq.csv", file_base64, file_type: "csv", declared_currency: "USD"}` | `data = {upload_id, input_id: null, state: "RESOLVING"}`; no vendor call from the Lambda | irpt-requests rows `UPLOAD#<upload_id>` (artifact family ORIGINAL_HOLDINGS, content_sha256) and `NORMALIZATION#<upload_id>#<options sha>` state RESOLVING, `requested_at`, `dispatched_at` | `UPLOAD_BODY_*`, `PROSPECT_GUARD_REQUIRED`, `UPLOAD_SERVICE_REQUIRED` (= D not deployed), `INPUT_ACCESS_DENIED` (partner viewer), `UPLOAD_ACTOR_ATTRIBUTION`, `TEMPLATE_*` / `FILE_UNREADABLE` |
| 1b | Queue (server) | one closed message `{kind: "resolve_upload", tenant, upload_id, normalization_revision}` on `irpt-generation` | visible count transiently 1 | `aws sqs get-queue-attributes` ApproximateNumberOfMessages / NotVisible | never appears = D2 (`sqs:SendMessage`) |
| 1c | Resident resolves (host) | `poll_once` -> `ResidentAssembly.resolve_upload`: `decide(phase=resolve)`, one lease-fenced `GET /securities/securities_info?securities=AAPL,VNQ`, freeze, NORMALIZED_PORTFOLIO, `INPUT#`, conditional flip | `NORMALIZATION#` row state NORMALIZED with `input_id`, `resolved_at`; message deleted | `journalctl -u irpt-analysis-resident` shows `IRPT_RESIDENT_POLL handled=1`; the row; the `INPUT#portfolio_<sha>` row and its artifact ref | `retained_for_retry` in the journal: B2 not done (old package), `ACTOR_*` (authority), D2 grants (AccessDenied). A provider outage keeps RESOLVING and the message retries. |
| 1d | Poll (browser re-POSTs the identical body) | same POST as 1a | `data.state == "NORMALIZED"`, `data.input_id`, `data.portfolio.holdings.total_dollars == "12.03"`, schema `irpt-normalized-portfolio.v2` | `input_id`; the NORMALIZED_PORTFOLIO artifact ref | `NEEDS_CORRECTION` with `reason` + findings (e.g. `TICKER_NOT_FOUND`); RESOLVING past 16 min re-sends once |
| 2 | Review frozen input (browser `InputReview.tsx`) | rendered from hop 1 response | AAPL 10.01 + VNQ 2.02 = 12.03 Dollars shown; no Shares prices required | screenshot + the normalized document's two rows and total | any substituted symbol or invented price |
| 3 | Submit (browser `GenerateComposer.tsx`) | `POST /api/scoped/investor-reporting/analysis` body = PUBLIC_FIELDS (`submission.py:16`): `request_id`, `input_id`, `prepared_for`, `variant`, `report_title`, `comparison_keys`, `account_ids`, `client_id: null`, `snapshot_id: null`, `corrections` | `analysis-requests` envelope: `data.identity` (tenant_firm_id, request_id, revision 1, immutable true, gate/policy revisions), `data.stage`, `status NOT_READY state QUEUED` | `identity.request_id`; irpt-requests item `{tenant, request_revision: "analysis#<request_id>#1"}` -> `record.accepted_at`, `composition_ref.sha256`; irpt-jobs item `{tenant, job: <request_id>}` state RECEIVED/outbox | `UPLOAD_SERVICE_REQUIRED` (= D not deployed), `CURRENT_INPUT_ACCESS_REQUIRED` / `CURRENT_VIEWER_CHANGED`, `COMPARISON_CATALOGUE_REQUIRED` (a comparison was selected), `INVALID_INPUT`, `CHANGED_INPUTS_SAME_REQUEST_ID`; `UNEXPECTED` with `TypeError` = P `19b38e2f22` missing from the build |
| 4 | Queue | server-side: closed message `analysis_generate` `{tenant, request_id, composition_sha256, revision "1"}` on `irpt-generation` | SendMessage accepted; visible count transiently 1 | `aws sqs get-queue-attributes` (ApproximateNumberOfMessages / NotVisible) | message never appears = precondition F |
| 5 | Resident claims and grades authority | host `poll_once`; `ResidentAssembly.execute` -> `current_authority.decide` at start | job row `lease_owner` set; decision ALLOWED (scope OPAL_GLOBAL for an Opal Dev/opal-capital actor, else OWN_FIRM == tenant) | `journalctl -u irpt-analysis-resident` line `IRPT_RESIDENT_POLL handled=1`; job row lease/fence | `ACTOR_*` refusals (no lease, message retried to DLQ maxReceiveCount 5); `CLOSED_QUEUE_MESSAGE_REQUIRED` |
| 6 | Vendor session and recipe | identity -> template -> upload echo (Dollars) -> deterministic portfolio create -> 7-setting readback -> validate -> generate | checkpoints `upload`, `portfolio`, `read_back` on the job row; permanent intents `holdings_upload`, `portfolio_create`, `report_create` | irpt-jobs row: `checkpoint_upload`, `checkpoint_portfolio`, `checkpoint_read_back`, intents; state `DOWNLOADING` | `SESSION_*`, `VENDOR_*_REFUSED`, `AMBIGUOUS_*` (parked ATTENTION, never repeated) |
| 7 | Retain PDF, certify, publish | download -> `ORIGINAL_VENDOR_PDF` artifact -> extraction against the pinned census (195040 B, sha `44853788fa6d...`) -> fenced index -> certified READY | job state READY with `detail.report_id`, `revision`, `certification_sha256`; `checkpoint_pdf` | S3 `opal-data-ycharts` keys for the PDF and EXTRACTION_EVIDENCE; irpt-requests index row for the report; the certified AnalysisReport's `provenance.extraction_evidence_ref.sha256` == `detail.certification_sha256` | `PDF_DOWNLOAD_RECEIPT`, `PDF_INDEX_BINDING`, `READY_CERTIFICATION_BINDING` |
| 8 | Screen (browser `ProspectJobStatus.tsx` -> `NativeSections.tsx`, `VendorPdfPreview.tsx`) | `GET /api/scoped/investor-reporting/analysis/{jobId}/sections` (jobId = `identity.request_id`) polled until READY | `analysis-report` envelope with typed sections and truthful partial coverage | the served `data` document hash; the vendor PDF preview served through the owned artifact reader | `NOT_FOUND`, `NOT_AUTHORIZED`, `UNEXPECTED` (ReportRefused) |
| 9 | Reload and history (browser `OwnedRequestHistory.tsx`, `RequestList.tsx`) | reload the tab; `GET .../analysis/requests`; `GET .../analysis/requests/{requestId}` | same report reopens with current access; history lists the request with its revision | second `sections` read returns the identical document; `owned-reopen.test.tsx` shape live | precondition E; `ACCEPTED_RECORD_CHANGED` |
| 10 | Same-revision branded export | `POST /api/scoped/investor-reporting/export` naming the report id + revision; `GET .../export/{exportId}`; follow `data.download_route` | receipt then a download of the SAME revision; vendor original vs branded both authorized | export receipt id, revision echoed, downloaded bytes' sha256 | `IRPT_EXPORT_RENDERER=unavailable` (renderer absence is REPORTED, not a render) |

## What Y records at the end (the evidence the CTO grades)

1. Deployed digests: `irpt-ycharts-generate`, `irpt-status`, `irpt-export-render` CodeSha256 at run time versus the
   source map; host package `SHA256SUMS` sha and the factory module path from P's cutover receipt; wrapper and
   library pins the session installed (wrapper `55ddb8f7947cba7c...`, library `feab2c53331528f0...` at P 5919c5363a,
   the S119 bundle contract, the measured sign-in route/form and the in-page probe with the pair control; superseded
   blobs `5a1a8695...`, `34df3e94...`, `41ffebbe...`).
2. Immutable revisions: `input_id`, `identity.request_id`, `revision`, `composition_ref.sha256`, `accepted_at`,
   `report_id`, `certification_sha256`, the export receipt id.
3. The authority evidence of the job (from the resident log line count, not the evidence body): decisions at
   start / guard / release all ALLOWED, `home_firm_source`, `createdAt_absent` value.
4. Screen: the rendered Analysis tab after hop 8 and after the hop 9 reload, and the history row.
5. Timing: queue put to READY, and READY to first screen render.

## Observing the resident (no second consumer)

The service is the ONE consumer on `irpt-generation` (standing directive). A `resident_main.py --once` run while the
service is active would be a second consumer that can take the job, so it is NOT run against the live queue. The
observation is the service's own journal: one `IRPT_RESIDENT_POLL handled=1` per message (hop 1c, then hop 5), and
`handled=0` per empty 20 s poll. `--once` is only for a stopped service during a P-owned cutover. There it prints
`handled=0` and exits 0 on an empty queue; any exception prints `retained_for_retry` and exits 1, with no body in the log.

## Limits

This runbook proves nothing by itself. Preconditions A-F are P's shared surfaces and G-H are Andrew's; Y owns
the journey semantics, hops 5-7 in code, this document, and the recorded evidence. The Y1-Y7 matrix (every firm,
CSV and XLSX, Dollars and Shares, Overview / Comparison / Multi-Comp, bad symbols, corrections, error / retry /
expiry / revocation, live recovery, both download kinds) runs after this first trace is graded, one reconciled
trace per case, same shape.

# Analysis 12.03 live journey -- executable runbook (COO~Y)

Owner `2.0.0_SA_COO~Y`. Written 2026-09-24 00:2xZ at Y `c4564aad17` against the published v1 route table
(`docs/contracts/investor-reporting/v1/routes.json`), the deployed plane measured this tick, and the portal at
`portal-local-live-20260923` `c70855f3` (Y pin `7a5b24e7` is an ancestor). Purpose: the moment P's installed
boundary lands, Y runs this top to bottom and records the digests it names. Every hop states its owner today,
the exact call, the readback that proves it, and the refusal that would stop it. Nothing here is a claim that a
hop is live; the PRECONDITIONS table is the measured state and each row names who moves it.

## Preconditions (measured 2026-09-24 00:1xZ; owner per row)

| # | Precondition | Measured | Owner / carrier |
|---|---|---|---|
| A | Host `i-0167fd745ad906a66` RUNNING and held running | DONE 2026-09-24T01:52:51Z: P applied plan 04c77cbe (CTO GO 99937; writer B now declares `running`, tag present, enforcer exempt); Y readback 02:0xZ SSM Online, resident policy applied (6 statements) | done |
| B | Resident installed: `irpt-analysis-resident.service` running `resident_main.py --factory MODULE:build_resident_runtime`, single consumer on `irpt-generation` | no `build_resident_runtime` in P's tree; queue has 0 consumers | P: factory / package / SHA256SUMS / cutover receipt (RESIDENT_ASSEMBLY_HANDOFF items 1-3, 5); grant closed at 9baf67bb5f |
| C | Current-authority reader on the host role: `dynamodb:Query` email-index, `GetItem` opal-users-v2, `kms:Decrypt` via dynamodb | APPLIED 00:17:29Z on both roles, zero-diff (P 99840) | done |
| D | `POST /api/scoped/investor-reporting/analysis/inputs` DECLARED with a handler, and LiveClient `analysis-input-upload: true` | routes.json `NO-HANDLER-AT-HEAD` (handler null) -> not in Terraform; portal `contracts/wire/responses.ts:423` = `false`; NO Lambda entry wires it today (`ycharts/generate/entry.py`: 0 references to `build_upload_entry` / `analysis-input-upload`) | P: name the target function in routes.json, compose Y's `intake/upload_entry.build_upload_entry(UploadService)` in that function's factory, register the route (handoff item 4), flip the flag |
| E | `GET .../analysis/requests` and `GET .../analysis/requests/{requestId}` DECLARED on `irpt-status` and LiveClient flags true | routes.json `NO-HANDLER-AT-HEAD`; portal `responses.ts:424-425` = `false`; the handlers exist in `ops/entry.py:200-201` since `8e8498c9c0` (2026-09-22 20:29 ET) but the deployed `irpt-status` (CodeSha256 `Hos/bFii...`, == source map) was built 2026-09-21T15:03Z, so it predates them | P: flip the two rows to DECLARED / handler `irpt-status`, rebuild + deploy irpt-status at a pin carrying 8e8498c9c0, flip the flags |
| F | Submit path: `irpt-ycharts-generate` deployed at a pin carrying HEAD's `entry.py`, role has `sqs:SendMessage` on `irpt-generation`, `IRPT_LIVE_YCHARTS_CALL` set | deployed 2026-09-19, CodeSha256 `1L60sG1G...` != source map `CJ6aBh7B...`; no SendMessage; env unset | P (CRO 6fc3f5f785 item 5) |
| G | Real login at a firm with a real advisor/prospect owner; Global default for an Opal user | localhost:5174 through CloudFront `d2n2nzpeqf34ge.cloudfront.net` (P) | Andrew's browser act; Y prepares |
| H | Vendor session: `ycharts/session/current` secret populated; first automated sign-in approved (D1, 6fc3f5f785) | not exercised on the host | Host workflow under Andrew's standing approval; never an agent ad hoc call |

## The journey, hop by hop

Fixed inputs: CSV `Ticker,Market Value,Currency` / `AAPL,10.01,USD` / `VNQ,2.02,USD`; units Dollars; expected frozen
total 12.03; variant `auto` (derives Overview for one portfolio); `comparison_keys` empty; `prepared_for` a real
recipient string; `report_title` "Retained input analysis". Firm = the signed-in user's storage firm (`tenant`).

| Hop | Act (actor) | Exact call | Proves / expected | Readback (Y records) | Refusal signatures that stop the run |
|---|---|---|---|---|---|
| 0 | Sign in (Andrew) | portal login; Investor Reporting > Analysis tab (`tabs/analysis/AnalysisTab.tsx`) | scope bootstrap resolves; header carries firm | portal network: `GET /api/scoped/investor-reporting/status` 200 envelope | `CONTRACT_VERSION`, `NOT_AUTHORIZED` |
| 1 | Upload template (browser via `ProspectComposer.tsx`) | `POST /api/scoped/investor-reporting/analysis/inputs` body `{upload_token, filename: "aapl-vnq.csv", file_base64, file_type: "csv", declared_currency: "USD"}` (`intake/uploads.py:34-66`) | response `analysis-input-upload` envelope with `data.input_id`, row disposition 2 of 2 accepted, template lane `TEMPLATE_UPLOAD` v2 | `input_id`; the retained ORIGINAL_CSV artifact ref + sha256; NORMALIZED_PORTFOLIO artifact ref (`schema_version irpt-normalized-portfolio.v2`) | `UPLOAD_BODY_*`, `PROSPECT_GUARD_REQUIRED`, `DURABLE_UPLOAD_SERVICE_REQUIRED`, `TEMPLATE_*` |
| 2 | Review frozen input (browser `InputReview.tsx`) | rendered from hop 1 response | AAPL 10.01 + VNQ 2.02 = 12.03 Dollars shown; no Shares prices required | screenshot + the normalized document's two rows and total | any substituted symbol or invented price |
| 3 | Submit (browser `GenerateComposer.tsx`) | `POST /api/scoped/investor-reporting/analysis` body = PUBLIC_FIELDS (`submission.py:16`): `request_id`, `input_id`, `prepared_for`, `variant`, `report_title`, `comparison_keys`, `account_ids`, `client_id: null`, `snapshot_id: null`, `corrections` | `analysis-requests` envelope: `data.identity` (tenant_firm_id, request_id, revision 1, immutable true, gate/policy revisions), `data.stage`, `status NOT_READY state QUEUED` | `identity.request_id`; irpt-requests item `{tenant, request_revision: "analysis#<request_id>#1"}` -> `record.accepted_at`, `composition_ref.sha256`; irpt-jobs item `{tenant, job: <request_id>}` state RECEIVED/outbox | `DURABLE_SUBMISSION_SERVICE_REQUIRED`, `PROSPECT_SUBMISSION_NOT_CONFIGURED`, `INVALID_INPUT`, `CHANGED_INPUTS_SAME_REQUEST_ID` |
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
   library pins the session installed (wrapper `55ddb8f7947cba7c...`, library `a0ffa0e8c5c23787...` at P abce466570,
   the S119 bundle contract, the measured sign-in route/form and the in-page probe with the pair control; superseded
   blobs `5a1a8695...`, `34df3e94...`, `41ffebbe...`).
2. Immutable revisions: `input_id`, `identity.request_id`, `revision`, `composition_ref.sha256`, `accepted_at`,
   `report_id`, `certification_sha256`, the export receipt id.
3. The authority evidence of the job (from the resident log line count, not the evidence body): decisions at
   start / guard / release all ALLOWED, `home_firm_source`, `createdAt_absent` value.
4. Screen: the rendered Analysis tab after hop 8 and after the hop 9 reload, and the history row.
5. Timing: queue put to READY, and READY to first screen render.

## Acceptance command for the installed resident (Y runs on the host once P's receipt names the factory)

```
sudo -u <SERVICE_USER> <ABSOLUTE_PYTHON> /opt/investor-reporting-ycharts/package/ycharts/generate/resident_main.py \
  --factory <MODULE>:build_resident_runtime --once
```
Expected: `IRPT_RESIDENT_POLL handled=0` (empty queue) with exit 0; any exception prints
`IRPT_RESIDENT_POLL retained_for_retry` and exits 1 without a body (the log never carries exception text).

## Limits

This runbook proves nothing by itself. Preconditions A-F are P's shared surfaces and G-H are Andrew's; Y owns
the journey semantics, hops 5-7 in code, this document, and the recorded evidence. The Y1-Y7 matrix (every firm,
CSV and XLSX, Dollars and Shares, Overview / Comparison / Multi-Comp, bad symbols, corrections, error / retry /
expiry / revocation, live recovery, both download kinds) runs after this first trace is graded, one reconciled
trace per case, same shape.

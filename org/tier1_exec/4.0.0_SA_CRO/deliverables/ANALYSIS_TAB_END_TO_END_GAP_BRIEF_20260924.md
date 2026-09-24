# Analysis tab: end-to-end trace brief (the deployed stack, 2026-09-24)

Prepared by 4.0.0_SA_CRO on 2026-09-24 (~05:35-06:05 UTC). Read-only assessment plus proposed closure requirements; no
application changes, vendor calls, deployment, host commands or schedule activation. The three deployed functions the
tab reaches were downloaded and diffed; the live tables, queue, instance and secret metadata were read; nothing was
invoked and no SSM command was sent to the host. `/closer trace` form. Y's own current-state file
(`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/STATUS.md`, as of 23:30Z) and runbook
(`RUNBOOK_1203_LIVE_JOURNEY_20260923.md`) were read AFTER the deployed measurement and agree with it; where this brief
adds to them it says so.

**Conclusion first.** The Analysis tab is an entirely OFFLINE product tonight: nothing a user can do on the deployed
tab reaches YCharts or produces a report. Of the journey's ten hops, the upload (hop 2) and the reload/history pair
(hop 10) have NO ROUTE at all -- the browser client refuses them by name before a network call; the submit (hop 4)
reaches a function built 2026-09-19 that predates every one of Y's commits and whose role cannot even put the message
on the queue; the queue has had zero messages and ZERO receives (nothing polls it -- no Lambda mapping, no resident
service installed); the vendor session leg is the only live progress today (the resident's sign-in proven three times
from the host, the template route answered 200 through the resident's own client class), and it has not yet captured a
bundle, so the resident cannot be installed. Everything downstream -- recipe, PDF, extraction, certification, screen,
history, export -- is built and offline-proven and has never run live. Your 04:32Z session made no Analysis call at
all (0 of 358 entries), which is consistent: there is nothing on that tab to click that answers.

## Design finding

The design (closer CONTRACT v1.4 row "Analysis / COO~Y"; COO_Y.md): an advisor supplies a portfolio -- a prospect's
dollar-template upload or a client's custody holdings -- Opal freezes it as an owned immutable input, submits ONE
durable job, a resident worker on Opal's own YCharts host signs in under Andrew's standing approval (6fc3f5f785: the
always-on host workflow -- sign-in, report-generation calls, ticker lookups), uploads the portfolio to YCharts, reads
back its seven settings, has the VENDOR generate the Overview / Comparison PDF, retains the vendor's original, extracts
it against a pinned census into a typed certified `AnalysisReport`, publishes it under finite retention, and the tab
shows it, keeps its history and exports the same revision. Opal computes no analysis; the vendor does. Agent ad hoc
vendor calls stay prohibited; the host workflow is the one authorized class.

Distance from the design: the COMPONENTS are unusually complete for a product with no live journey -- Y's upload and
normalization, durable submission, resident worker, session broker, recipe, publisher and census are on CLOUD with
18 focused offline cases and 4 controls (Y1-Y5 OFFLINE ONLY in Y's own matrix) -- but the DEPLOYED backend is the
pre-Y build, three of the ten route hops have no handler, the consumer is not installed, and the vendor leg is mid
D1 (sign-in proven, bundle not captured). This is the /closer "components exist, no journey works" case exactly. The
work worth keeping is all of Y's; the unfinished connections are P's shared surfaces (route plane, deploy, grants,
cutover) and the last D1 leg.

## Current measurement

Read from DEPLOYED bytes at 05:41:59 UTC (each zip's own sha256 equals its configuration's):

| function | last modified | members | handler / mem / timeout | what it is |
|---|---|---|---|---|
| `irpt-ycharts-generate` | 2026-09-19T14:29:32Z | 31 | `entry.lambda_handler` / 512 MB / 900 s, no layer | the IB-s-9 submit-and-enqueue entry; `job.py`/`gate.py` byte-equal to CLOUD, `entry.py` (137 diff lines), `recipe.py` (44), `transport.py` (19) differ; ELEVEN CLOUD modules absent from the zip (`acceptance, composition_admission, durable_job, frozen_worker, normalized_input, publication_worker, publisher, recipe_snapshot, report_index, submission, submission_service`) -- Y's entire retained/durable/resident stack |
| `irpt-status` | 2026-09-21T15:03:15Z | 16 | `entry.lambda_handler` / 256 MB / 15 s | serves `analysis-report` (sections), `status-summary`, `status-job`; jobs table by code default `irpt-jobs`; NOT the two owned-history routes |
| `irpt-export-render` | 2026-09-21T15:06:33Z | 20 | `entry.lambda_handler` / 1024 MB / 120 s, `irpt-common:5` | `IRPT_EXPORT_RENDERER=unavailable`; render host = the runner instance, SSM document `irpt-export-render-run` |

Generate's environment carries `IRPT_JOBS_TABLE`, `IRPT_REQUESTS_TABLE`, `IRPT_GENERATION_QUEUE_URL`,
`IRPT_YCHARTS_SESSION_SECRET_ID=ycharts/session/current`, `IRPT_EVIDENCE_BUCKET=opal-data-ycharts`; NOT present:
`IRPT_LIVE_YCHARTS_CALL`, `IRPT_INGESTION_GATE_REVISION`, `IRPT_DESTINATION_POLICY_REVISION` (the identity it mints
reads "unset" for both revisions). Event source mappings on the function: none. CloudWatch REPORT lines, last 3 days:
generate 0, status 0.

Route plane (`docs/contracts/investor-reporting/v1/routes.json` and the portal client at 7975c3bb):
`analysis-input-upload`, `analysis-request-history`, `analysis-request-read` = `NO-HANDLER-AT-HEAD`, handler null, not
in Terraform; `LiveClient.send` throws `NotYetExercisable` (reasonCode `no-handler-at-head`) before any request;
`listAnalysisRequests` rejects `NoDeclaredRoute('analysis-requests-list')` (no list route exists, by design);
`analysis-requests` (POST) -> `irpt-ycharts-generate`; `analysis-report` -> `irpt-status`.

Live state: `irpt-requests` 17 items, ALL `SELECTION#` rows, 0 analysis rows; `irpt-jobs` 1 item (`_opal`, the intake
lease row), 0 jobs; `irpt-generation` 0 visible / 0 in flight and, over the last 6 h, NumberOfMessagesSent 0,
NumberOfMessagesReceived 0, NumberOfEmptyReceives 0 -- nothing has ever been submitted and NOTHING POLLS; runner
`i-0167fd745ad906a66` RUNNING since 01:52:51Z (t3.medium); secret `ycharts/session/current` exists, last changed
2026-05-21, never accessed, described as the C1 capture Lambda's cookie bundle with a ~96 h WAF token -- a legacy
artifact; the resident's D1 work has not versioned it. Registry `infra/logic/registry/reporting_policies.json` on
CLOUD: state PENDING_ENFORCEMENT, 12 families, `ORIGINAL_HOLDINGS` ABSENT (M's row 58ee5b36dd is LOCAL on its branch;
CTO accepted). CTO batch 27 (05:51Z) accepted X10 ACTIVE with `enforcement_ref 0a101a6668`; M writes the row next.

D1 (the vendor session leg, from the CTO's record and P/Y receipts, not re-run): four runs today; run 4 (SSM
6ade1f06, 04:35Z) signed in (1 submission, 302, dashboard), identity leg passed, the template GET from inside the page
405 (WAF captcha) while the Node client with the full cookie jar 200 on the same route -- the resident's client class
passes from EC2; no bundle; three submissions spent; the fourth run waits on P's Node-path commit (P 100286: next at P).

Source pins: workspace c3508c07df (+ this seat's later commits), portal 7975c3bb, Y's branch `irpt-mvp-y-20260922`
@7fec957269, P's backend branch @9f360e8f3b.

Not invoked: any function, the vendor, the host. Machine-readable evidence:
`.runtime/codex-seats/4.0.0_SA_CRO/analysis_trace_20260924/evidence.json` (private, gitignored).

## Adapter map

| Leg | Provider / mechanism | Existing work | Gap |
|---|---|---|---|
| Upload and normalization (prospect CSV/XLSX or client holdings) | Opal (`intake/uploads.py`, `intake/upload_entry.build_upload_entry`, `template_reader`, `security_resolution`, Kimi resolution) | On CLOUD; offline: 2-of-2 row disposition, 12.03 freeze, corrections | No function composes `build_upload_entry`; no route; `ORIGINAL_HOLDINGS` family absent from the CLOUD registry; X10 row pending |
| Durable submission | Opal (`ycharts/generate/submission.py`, `submission_service.py`, `durable_job.py`) | On CLOUD; CTO source review PASS bounded | Absent from the deployed zip; the deployed submit is the 09-19 shape; role has no `sqs:SendMessage` |
| Vendor session | YCharts sign-in from the Opal host (`ycharts/session/broker.py`, the Node wrapper 55ddb8f7 + library a0ffa0e8 on the host; `/account/login/` form, `/dashboard/` identity) | Sign-in proven 3x from EC2; identity via `window.USER`; template GET 200 via the Node client | Bundle never captured (the in-page probe is WAF-fenced); enrolled id unknown; secret unversioned; fourth submission pending P's Node-path commit |
| Recipe: template, Dollars upload echo, portfolio create, 7-setting readback, generate | YCharts internal API through the resident (`recipe.py`, `resident_worker.py`, `frozen_worker.py`) | Offline-proven (18 cases + 4 controls) | Never run live; the resident service is not installed; the queue has no consumer |
| Retain, extract, certify, publish | Opal (`publisher.py`, `ycharts/extract/*`, pinned census 195040 B; families ORIGINAL_VENDOR_PDF / EXTRACTION_EVIDENCE under X10) | Offline-proven; host pydeps verified (pdfplumber 0.11.9 etc.) | Never run live; needs X10 ACTIVE in the package |
| Screen, status, history, export | `irpt-status` (sections / status), the two owned-history routes, `irpt-export-render` | Sections/status routes deployed (09-21, never invoked); history/read handlers exist under `ops/` at HEAD but are not routed; export renderer `unavailable` | No job has ever existed to read; two routes have no handler; export unchanged since the 09-22 brief |

One leg's offline proof certifies no other leg live; tonight no leg has a live proof except the sign-in.

## Start-to-finish walk

### 1. Sign in -> Investor Reporting -> Analysis tab bootstrap -- WORKS

What exists: the portal route (`requireAdmin requireInternal requireDev`, `App.tsx:436`), `TabShell` mounts
`AnalysisTab.tsx` (FE-s-10); the tab bootstraps scope, mounts `ProspectComposer`, `OwnedRequestHistory`,
`GenerateComposer` and, when a request is selected, the review/stage/preview components. `listAnalysisRequests`
rejects `NoDeclaredRoute` client-side, so the tab renders `RequestList` with an UNAVAILABLE envelope carrying
`no-declared-route` (correct: no list route exists; history is hop 10).

Close: nothing on this hop.

### 2. Upload template (ProspectComposer -> POST /analysis/inputs) -- MISSING

What exists: `ProspectComposer.tsx` reads the file, builds `AnalysisUploadRequest` (`upload_token, filename,
csv_base64`, optional currency/price date/notional) and calls `api.uploadAnalysisInput`; Y's `intake/uploads.py`
(template lane v2, row disposition) and `intake/upload_entry.build_upload_entry(UploadService)` are on CLOUD.

The exact mismatch: `routes.json` says `NO-HANDLER-AT-HEAD, handler null` ("installed runtime factory and maintained
adapters are pending. Not declared in Terraform or enabled in LiveClient"); `LiveClient.send` throws
`NotYetExercisable` before any request; the composer prints "This action is unavailable (no-handler-at-head). Your
request is kept for retry." -- a retry cannot change it. Behind the missing route, two registry facts would refuse the
first real upload: `ArtifactRepository` refuses the `ORIGINAL_HOLDINGS` family absent from the CLOUD registry
(`reports/repository.py:325`; M's row LOCAL), and the retention gate (`reports/retention.py:52-59`, the same gate that
stops Performance) requires the policy row ACTIVE with an `enforcement_ref` -- accepted by the CTO at batch 27, row not
yet written.

Close: P names the function in `routes.json`, composes `build_upload_entry(UploadService)` in that function's
factory, declares the route in Terraform and flips the client flag (`responses.ts:423`); M's `ORIGINAL_HOLDINGS` row and
the X10 ACTIVE row land in the same package; the upload function gets Put/Get on `irpt/<firm>/state/original_holdings/*`.
Proof: runbook hop 1 returns `data.input_id` with "2 of 2 accepted" for `AAPL,10.01,USD / VNQ,2.02,USD`.

### 3. Review the frozen input (InputReview) -- INCOMPLETE (offline only)

What exists: `InputReview.tsx` renders hop 2's normalized document (rows, total 12.03 Dollars, flagged rows carry a
control); `normalized_input.py` / frozen recipe offline-proven (Y2).

Close: rides hop 2; proof = the rendered review shows the two rows and 12.03 from a live upload, no substituted symbol,
no invented price.

### 4. Submit (GenerateComposer -> POST /analysis -> irpt-ycharts-generate) -- MISMATCHED

What exists: `GenerateComposer.tsx` builds the browser half (`submission.py:16` PUBLIC_FIELDS at HEAD: `request_id,
input_id, prepared_for, variant, report_title, comparison_keys, account_ids, client_id, snapshot_id, corrections`)
and calls `submitAnalysisRequest` (POST /analysis, v1 envelope). Deployed `entry.py:98-164 submit_analysis` (09-19):
refuses server-owned fields, takes the IB-s-9 BROWSER_FIELDS, mints `identity` (revision "1", gate/policy revisions
from env -> "unset"), ENQUEUES the closed message on `irpt-generation`, answers NOT_READY / QUEUED.

The exact mismatch, three parts: (a) the function's role is receive/delete only on the queue (`ycharts/iam.tf:113-118`
"this job does not enqueue"; Y measured no `sqs:SendMessage`), so the one `send_message` the entry makes raises and
the boundary classifies it -- a QUEUED answer can never be returned by today's bytes; (b) the deployed entry is the
pre-Y shape: Y's `submission_service` (durable acceptance -> `irpt-requests` `analysis#<request_id>#1` with
`composition_ref.sha256`, `irpt-jobs` row RECEIVED) is not in the zip, so even a successful enqueue would leave no
retained request and no job row for hop 9 to read; (c) `IRPT_INGESTION_GATE_REVISION` / `IRPT_DESTINATION_POLICY_REVISION`
unset. Measured: 0 invocations in 3 days; 0 messages ever sent.

Close: P deploys `irpt-ycharts-generate` at a pin carrying HEAD's entry over Y's `submission_service`, grants
`sqs:SendMessage` on `irpt-generation` to the submit role, sets the two revisions and `IRPT_LIVE_YCHARTS_CALL`
(runbook precondition F; CRO 6fc3f5f785 item 5). Proof: one `analysis#` row, one jobs row RECEIVED, one message
visible on the queue, the envelope `NOT_READY / QUEUED` with `identity.request_id`.

### 5. Queue -> consumer -- MISSING

What exists: the queue (core root, DLQ maxReceiveCount 5); the resident consumer `resident_main.py --factory
MODULE:build_resident_runtime` (single long-poll consumer) and P's factory `build_resident_runtime` (5e05823f4e, 11
controls, Y accepted); the cutover plan (host running, resident policy applied 01:52Z).

The exact mismatch: no event source mapping on the Lambda (by design -- the Lambda job is retired in favour of the
resident), and the resident service is not installed: over 6 h the queue recorded 0 receives and 0 empty receives, i.e.
nobody polls. The cutover sequence is gated on the D1 bundle (hop 6): package upload, enrolled id measured from the
bundle, receipt C1, `install-resident.sh`, then Y's `--once` acceptance (`IRPT_RESIDENT_POLL handled=0`).

Close: P's cutover in ONE plan after hop 6 captures the bundle; proof = `handled=0` on the host and NumberOfEmptyReceives
rising every long-poll thereafter.

### 6. Resident -> YCharts session (sign-in, identity, bundle) -- INCOMPLETE (sign-in proven; no bundle)

What exists: the host wrapper and library (pins 55ddb8f7 / a0ffa0e8 at P abce466570), the measured login route
`/account/login/` and form model (auth-username / auth-password, Enter submit, newsletter decoy avoided, `/dashboard/`
warm-up -- this seat's 09-10 model, relayed 100043), `session/broker.py` (bootstrap once, recapture once on an exact
measured sign-out), the S119 bundle contract (schema_version, capture_origin, generation, user_agent, identity.user_id).

The exact mismatch: four runs today; sign-in proven three times and the identity leg once, but the probe that captures
the bundle ran from INSIDE the page and is WAF-fenced (405 captcha on non-navigation fetch), while the resident's own
client class (the Node port with the full jar) answered 200 on the template route -- so the bundle capture must move
to that class (CTO 100216; P's Node-path commit is next). Until it lands: no bundle, no enrolled id, no versioned
secret, no resident install. The secret that does exist (`ycharts/session/current`, 2026-05-21) is the old C1 capture
Lambda's bundle and is not what the resident writes. Vendor submissions are bounded (three spent today).

Close: P's Node-path commit, Y STANDS on the five conditions, ONE run = the fourth submission; proof = a versioned
`ycharts/session/current` carrying the S119 keys, `identity.user_id` a positive integer, receipt C1.

### 7. Recipe: identity -> template -> Dollars upload echo -> portfolio -> 7-setting readback -> generate -- INCOMPLETE (offline only)

What exists: `recipe.py` (the template GET at `:364-375`, the deterministic portfolio create, the seven settings),
`resident_worker.py` (current authority replayed at start / every guard / release / reopen), `frozen_worker.py`;
checkpoints `upload`, `portfolio`, `read_back` and permanent intents on the jobs row; 18 offline cases + 4 controls at
2874e37647 (CTO 2dd385ed59).

The exact mismatch: never run live -- Y4 NOT STARTED: "no vendor PDF ever produced by the resident". The template
route is now known to answer the resident's client class (run 4), which is the one live fact this leg has.

Close: the first live job on the installed resident with the runbook's fixture (12.03 Dollars, variant auto, no
comparisons); proof = the jobs row's three checkpoints and intents, state DOWNLOADING then READY, and the vendor PDF's
receipt.

### 8. Retain PDF -> extract against the pinned census -> certify -> publish -- INCOMPLETE (offline only)

What exists: `publisher.py`, `ycharts/extract/{extract,certify,fonts,publication}.py`, the census (195040 B, sha
`44853788fa6d...`), the fenced report index; host pydeps verified (python 3.12.14, pdfplumber 0.11.9, pdfminer.six
20251230, jsonschema 4.26.0); families ORIGINAL_VENDOR_PDF / EXTRACTION_EVIDENCE / the report under X10.

The exact mismatch: never run live; and the retention gate needs the X10 row ACTIVE in the package the resident runs
(accepted at batch 27; M writes the row; P repackages).

Close: rides hop 7; proof = `provenance.extraction_evidence_ref.sha256 == detail.certification_sha256` on the certified
`AnalysisReport`, and the S3 keys for the PDF and EXTRACTION_EVIDENCE in `opal-data-ycharts`.

### 9. Screen: sections and job status (ProspectJobStatus -> GET /analysis/{jobId}/sections; GET /status/{jobId}) -- INCOMPLETE

What exists: deployed `irpt-status` serves the three routes over `irpt-jobs` (code default) and the evidence bucket;
`ProspectJobStatus.tsx` polls, `NativeSections.tsx` and `VendorPdfPreview.tsx` render; `AnalysisReport` requires
`request_ref, vendor_artifact, effective_inputs, sections, disclosures, extraction_validation, release`.

The exact mismatch: no job has ever existed, so the route has never answered anything but absence (0 invocations in
3 days); the deployed status build (09-21) predates Y's `ops/owned_status.py` / `owned_report.py` and the v2 prospect
dates binding (`ops/prospect_dates.py` at Y 7fec957269, copy AWAITED at P).

Close: P rebuilds `irpt-status` at a pin carrying the ops package at HEAD; proof = runbook hop 8, the served `data`
document hash and the preview through the owned artifact reader.

### 10. Reload and history (OwnedRequestHistory -> GET /analysis/requests, /{requestId}) -- MISSING

What exists: `OwnedRequestHistory.tsx` (list 25, cursor, re-open), `ops/owned_requests.py`, `ops/owned_report.py`,
`OwnedAnalysisRequest` contract; `owned-reopen.test.tsx` offline.

The exact mismatch: both routes `NO-HANDLER-AT-HEAD` (handler null, not in Terraform); the client throws before a
request; `ops/entry.py`'s `ROUTES` at HEAD still lists only the three status routes, so the handlers are in the package
and not on the route table; the component swallows the refusal into a boolean flag (no code shown). The DSGN_IRPTV1 PRD
v0.4 defers these two routes as Y's and lets FWD-7/FWD-8 stand on them as enrichment inputs.

Close: P routes the two operations on `irpt-status` (routes.json handler, `ROUTES`, Terraform, client flags
`responses.ts:424-425`); the component prints the public code; proof = runbook hop 9, the identical document on reload
and the history row with its revision.

### 11. Same-revision export (POST /export -> irpt-export-render) -- INCOMPLETE (unchanged since the 09-22 brief)

What exists: the deployed export function (09-21) with `IRPT_EXPORT_RENDERER=unavailable`, the render host = the same
runner instance by SSM document `irpt-export-render-run`, `IRPT_PORTAL_ORIGIN=https://opalinvest.dev`; the tab's Export
button is permanently disabled (FE-s-9 enables it).

Close: the 09-22 brief's hop 12 stands; not re-measured beyond configuration. Proof = a receipt and a download whose
revision equals the report on screen.

### 12. Refusal -> screen and operator -- INCOMPLETE

What exists: four surfaces render a refusal four ways -- `ProspectComposer` prints the code in a sentence;
`AnalysisTab` renders an UNAVAILABLE envelope with `no-declared-route`; `OwnedRequestHistory` sets boolean flags with no
code; `GenerateComposer` prints `composer-refusal` with the code. Server side, the generate entry's boundary records
an internal error to a `None` sink (the same shape as the Performance trace's hop 12), and its log group carried nothing
to record anyway.

Close: one refusal presentation for the tab (state, public code, the one safe action) and a log sink injected at Entry
construction; proof = the next refusal names its class in the function's log group and its code on the panel.

## Recommended completion sequence

1. **The live thread** = Y's runbook journey, exactly: Andrew signs in on the DEV candidate, Investor Reporting >
   Analysis, uploads `AAPL,10.01,USD / VNQ,2.02,USD` as a prospect, reviews 12.03, submits variant `auto`, the
   resident produces the Overview, the tab shows the certified sections and the PDF preview -- one HAR, the resident's
   log line, the jobs row, the certified report's hash. It crosses hops 1-9. Owners: the shared first hop and every
   route/deploy/grant is P's (preconditions B, D, E, F: cutover, upload route, status rebuild + owned routes, generate
   deploy + SendMessage); the vendor leg is P's Node-path commit + Y STANDS + the fourth D1 submission (precondition H,
   under Andrew's standing host approval); the registry rows are M's (`ORIGINAL_HOLDINGS`) and the X10 ACTIVE row;
   the browser act is Andrew's (G). Y owns hops 5-8 in code and the evidence.
2. Hop 10 (history/reload) and hop 12 (one refusal presentation, a log sink) -- small, P/Y.
3. The client-holdings input path (`GenerateComposer` with a held snapshot) and the comparison catalogue (Y).
4. Export (hop 11) -- the shared chain, unchanged.
5. The Y1-Y7 matrix: every firm, units/variants/corrections, session recovery, downloads.

## Acceptance

One reconciled trace per case, each following one input from the upload (or holdings selection) through the retained
request, the queue message, the resident's authority decision, the vendor requests and the PDF receipt, the extraction
evidence, the certified report, the rendered sections, the reload, and the export. Cases: {prospect upload, client
holdings} x {Overview auto, one comparison, multi-comparison} x {49financial, cottonwood, inflection, an Opal user in
Global} x failure cases {expired session, WAF challenge on the probe class, template refusal, missing registry family,
lease lost mid-job (DLQ), second principal reopening}. The surface is complete when these traces reconcile, not when
the 18 offline cases pass.

## Evidence anchors and limits

Source inspected at workspace c3508c07df (+ this seat's later commits) and portal 7975c3bb; the deployed bytes pinned
by digest; Y's branch @7fec957269 and P's backend branch @9f360e8f3b named for the code the zips lack. Verified fresh:
the three functions' packages and configurations, the route file and client, the tables, the queue's attributes and
6-hour metrics, the instance state, the secret's metadata, the registry row. Taken from the record, not re-run: the D1
runs (CTO batch 25, P 100286), Y's offline case counts. NOT verified: any vendor response, the host's service state
(no SSM command sent), the applied IAM on the generate role beyond the declared statement and Y's measurement, the
export chain beyond configuration.

- `infra/aws/lambda/investor-reporting/ycharts/generate/{entry,job,recipe,transport,submission,submission_service,durable_job,resident_main,resident_worker,frozen_worker,publisher}.py`, `ycharts/session/broker.py`, `ycharts/extract/*`
- `infra/aws/lambda/investor-reporting/intake/{uploads,upload_entry}.py`; `ops/{entry,owned_requests,owned_report,owned_status,prospect_dates,status,status_loader}.py`; `reports/{repository,retention}.py`
- `infra/aws/terraform/investor-reporting/{ycharts,api,core,export}/*.tf`; `docs/contracts/investor-reporting/v1/routes.json` and the Analysis* schemas
- `portal/src/api/endpoints/investor-reporting.ts` (:198-212, :246-270, :954, :1042-1046, :1118-1130, :1214-1245); `portal/src/pages/InvestorReporting/tabs/analysis/{AnalysisTab,ProspectComposer,OwnedRequestHistory,GenerateComposer,InputReview,ProspectJobStatus,NativeSections,VendorPdfPreview}.tsx`
- `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/{STATUS.md,RUNBOOK_1203_LIVE_JOURNEY_20260923.md,RESIDENT_ASSEMBLY_HANDOFF_20260923.md}`; `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/{CONTRACT.md,COO_Y.md,RULINGS.md (batches 25-27)}`
- `.runtime/codex-seats/4.0.0_SA_CRO/analysis_trace_20260924/evidence.json`

## Andrew-direct request -- verbatim record

Channel: the 4.0.0_SA_CRO terminal, 2026-09-24 ~05:3xZ.

> /closer trace IRPT "Analysis Tab". Release your findings to COO~Y afterward. [IMPORTANT: ONLY DO THIS AFTER YOU HAVE
> COMPLETED THE TRACE FOR "PERFORMANCE" AND HAVE ISSUED THAT TRACE TO COO~P]

The Performance trace was completed and issued to 2.0.0_SA_COO~P (msg 100281, @d8abd7dc65) before this trace began.

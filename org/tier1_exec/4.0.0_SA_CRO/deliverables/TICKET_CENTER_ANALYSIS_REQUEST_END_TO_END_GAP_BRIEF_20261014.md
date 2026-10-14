# Ticket Center Analysis Request -> YCDGEN report -> AI commentary -> Open ticket: end-to-end trace brief

Prepared by `4.0.0_SA_CRO~DELL2` on 2026-10-14 (reads 15:10-15:35Z). This is a read-only assessment with proposed closure requirements.
Nothing was changed: no application changes, no vendor or model calls, no Lambda invokes, no queue sends or receives, no deploys, no
schedule activation. Deployed code was downloaded and hashed into the session scratchpad (`sliceB/`, `sliceC/`, `sliceD/`, not
persisted). One read-only DynamoDB scan of `opal-tickets` was run, for counts only.

## Design finding

The intended design (Andrew's dell2 memo of 2026-10-13, and his trace order of today):
- An Opal user files an Analysis Request in the Ticket Center: form plus the advisor's CSV/XLSX.
- The backend fixes typos, swaps missing securities and generates the Opal (YCDGEN) report with no hands.
- An AI layer then writes the investment commentary on that report.
- The still-OPEN ticket carries the attachments: the advisor's file, the generated report, and the commentary as a PDF on the branded
  Opal form.

**How far the build is from that.** Most components exist and are deployed. None of them has carried one real request end to end.
- **Work worth keeping:** the upload door, the ticket API (byte-equal to source), the commentary drafter Lambda (wired to its queue),
  the packager code that renders a branded PDF, the Open queue, and the ticket page's attachment list.
- **The joins between them are unfinished.** The report engine serves only Andrew's login. The resident host is not bound to the
  READY, commentary or packager queues. The commentary flag cannot travel. The ticket page cannot open a commentary or a branded PDF.
- **The report itself would be mostly empty:** 6 of 257 sections carry a value, because no price source is composed.

## Current measurement

| Deployed component | Digest | Last modified | Against source @116d679d62 |
|---|---|---|---|
| `opal-ticket-api` | `Fg8MdfvC...` | 10-14 15:10:00Z | `lambda_function.py` MATCH |
| `irpt-ycharts-generate` (upload POST, analysis POST, catalogue) | `5TRFZf6G...` | 10-14 13:03:45Z | 53 of 68 `.py` equal; 13 differ because source moved after the deploy (incl. `submission.py`, `acceptance.py`, `composition_admission.py`) |
| `irpt-status` (original and pdf readers) | `yNpw441T...` | 10-14 12:19:40Z | configuration only |
| `outlook-global-commentary-draft-lambda` | `xC1GDXXp...` | 10-12 01:04:58Z | 7 of 7 `.py` MATCH |
| `irpt-commentary-composition-read-lambda` | `DbvBUxTG...` | 10-11 16:41:35Z | not diffed |
| `irpt-commentary-draft-store-lambda` | `cwf6bUEb...` | 10-12 00:06:20Z | not diffed |
| Resident r29 tarball (`ec2/investor-reporting-ycharts/resident/irpt-resident-0485393f3a-r29.tar.gz`), host `i-0167fd745ad906a66` | sha256 `2de2adce...` | put 12:38:44Z, installed 12:41Z | worker, packager and installer MATCH; `resident_bindings.json` has `analysis_ready_queue_url`, `commentary_ready_queue_url` and `packager` all **null** |
| Portal PROD `6a5926fc` and DEV `97c66c93` | git tree `17ad3370` (identical) | PROD promote 12:24Z, portal-v2.1.218 | CI success; the deployed CloudFront bundle was not downloaded |

Configured but never executed as a connector:
- the `svc-irpt-packager` secret (LastAccessed null);
- the analysis-ready queue (0 messages ever seen by this read);
- the commentary-ready queue (1 message, unconsumed, since ~10-11 06:10Z; INFERRED from age, body not read).

## Adapter map

| Leg | Provider and endpoint | Existing work | Gap |
|---|---|---|---|
| Filing | portal Ticket Center -> `POST .../analysis/inputs`, ticket CREATE/SUBMIT, `POST .../analysis`, `POST /tickets/{id}/report` | form, upload, browser orchestration `fileAndRequestAnalysis` | staff submit held (J7); orchestration only in the browser |
| Security resolution | `etf-classifications` (DynamoDB), YCharts `securities_info` over the resident's browser session, Kimi K3 typo check | C-SWAP step 1 live; advisory typo suggestion | no swap UI in the Ticket Center; C-SWAP step 2+ design only; AI web-search swap refused by design |
| Report data | Opal: holdings + `etf-classifications` + `opal-data-etfs/bbg/<date>/characteristics.parquet`; YCharts: signed-in browser session | Opal producer (Overview); YCharts worker | no price source (returns, risk and benchmark NOT_AVAILABLE); YCharts path failed 10-11 NO_AUTHENTICATED_PROBE; no single YCharts API call wired |
| Engine choice | resident `producer_for` allow list | C-SWITCH ruled by the CTO, approved by Andrew 10-13 call 1 | allow list is `("andrew@opalinvest.com",)` in r29 and at HEAD |
| Commentary | analysis-ready SQS -> drafter Lambda -> Kimi K3 (`astn/kimi/api-key`) -> draft store -> `/commentary-draft` | all deployed and wired from queue to Lambda | nothing sends to the queue; output is JSON text, not a PDF; reads neither report figures nor transcripts |
| Package | commentary-ready SQS -> resident `opal_packager.py` -> `POST /tickets/{id}/package` | packager renders a branded PDF (report + DRAFT commentary page) and posts 4 pointers | resident bindings null, so nothing consumes the queue |
| Display | Open tab -> ticket page readers (`/original`, `/sections`, `/pdf`) | Open list, Original reader, Form-as-filled inline, Report in-page | no Commentary reader; branded `pdf_ref` not listed; `/pdf` serves the report's own PDF, not the package |

The firms differ: each of 49financial, cottonwood and inflection is in the ticket API's allow lists, but only 49financial was
exercised (release 28/29 sittings). One firm's success does not certify another.

## Start-to-finish walk

The walk follows the filer Andrew set at ~15:2xZ today: an **Opal staff user** (the Ticket Center is internal-only for now; record
@011515bb70). The partner-advisor path is noted where it differs and is parked.

### 1. Opal staff sign-in -> Ticket Center -- WORKS

What exists:
- `portal/src/App.tsx:503-506`@6a5926fc mounts `/ticket-center` behind `requireInternal`.
- Partner reach exists only under the vite dev server (`isPartnerDevReach`, `firmAccess.ts:141-153`). It is off on every deployed
  build, which is correct per Andrew today.

Close: none; the partner-reach cells (AR-y-282, AR-y-283) stay parked until Andrew opens the Ticket Center to client users.

### 2. Staff fills the form -> Submit -- MISMATCHED

What exists: `AnalysisRequestParts.tsx:100-104` (`filingFirm` returns `''` for an internal user) and `analysisRequest.ts:227`, which
holds the submit with "Choose the firm this request is filed under."

The exact mismatch: an internal user has no firm, so the submit never fires. On PROD and deployed DEV, nobody can file.

Close: let the staff filer choose the partner firm and file (cell J7, PRD ADDENDUM v0.6). Proof: a ticket filed from deployed DEV by a
staff login.

### 3. Form fields -- WORKS (two gaps)

What exists, @6a5926fc:
- Title (`TicketCenter.tsx:689`); report type select, which IS the variant sent (`answersFromForm` `:75-85`, `variantFor`
  `analysisRequest.ts:377`; a count mismatch is refused `:352-365`).
- Opal-model checkboxes (`AnalysisRequestParts.tsx:173-182`); Other ETFs with a "Did you mean" hint (`comparisonCatalogue.ts:51-68`).
- Add-commentary checkbox (`:197-199`); upload `.csv,.xlsx` (`:204`).

The exact mismatch:
- (a) There is no holdings swap UI in the Ticket Center. Provider-verified swap suggestions exist only on Investor Reporting
  (`ProspectComposer.tsx:518-528`); the Ticket Center prints NEEDS_CORRECTION findings as text and files nothing (`analysisRequest.ts:253-261`).
- (b) The upload sends `priceDate: ''` (`TicketCenter.tsx:411`).

Close: port the composer's swap list into the Ticket Center findings. Proof: a misspelled holding offers "Use X" and the request files.

### 4. Upload -> stored input -- WORKS (market-value files) / INCOMPLETE (share quantities)

What exists:
- Route `POST /api/scoped/investor-reporting/analysis/inputs` (deployed `generate_installed.py:370`); `UploadService.create`
  (`uploads.py:349`).
- The original and the normalized portfolio are retained under `irpt/<firm>/state/original_holdings/ART-...` and
  `.../normalized_portfolios/ART-...`.
- Today's release-29 sitting read D1 NORMALIZED, with the 49financial store at 285 -> 291 objects.

The exact mismatch: a share-quantity file stops at NEEDS_CORRECTION `SHARES_PRICE_SOURCE_NOT_COMPOSED` (D5), because no price source is
composed.

Close: compose a verified price reader for share files (the round-40 "Shares" enrichment, ruling 7546). Proof: a share-quantity upload
NORMALIZED.

### 5. Typo / missing-security swap -- INCOMPLETE

What is live in r29:
- C-SWAP step 1: known-security lookup in `etf-classifications`.
- Deterministic ticker check through YCharts `securities_info`, which needs the resident's YCharts browser session (`security_resolution.py`).
- An advisory Kimi K3 typo suggestion kept only if YCharts confirms it (`intake/upload_suggestions.py`, `KIMI_CHECK_PROVIDER_VERIFIED`).

What is not live:
- The AI web-search swap is refused by design until provider QA (`intake/resolution_kimi.py`); the earlier swap code was reverted
  (AR-y-277).
- The class-based substitute (C-SWAP step 2+: asset class and sub-class, the designated-proxy table from MDPF_SECCLASS) is design only
  (AR-y-278).

Close: build C-SWAP step 2 and give the suggestion check a verification source that does not need the YCharts session. Proof: an
unknown holding comes back with a recorded `proxy_for`/`method`/`confidence`.

### 6. Submit -> ticket + analysis request -- INCOMPLETE

What exists:
- Staff path: `fileAndRequestAnalysis` (`analysisRequest.ts:417-434`) uploads, creates the ticket, then `POST .../analysis` with
  `{request_id, variant, comparison_keys, input_id, prepared_for, ticket_id, ...}` (`:368-384`), then `POST /tickets/{id}/report`.
- Ticket API: SUBMIT-FORM takes the answers and the upload handle with the firm from the token (`lambda_function.py:174,195`). The
  `input_id` owner check went live at 15:10Z.
- In today's sitting, an internal viewer's analysis was accepted (D6, ANSWER).

The exact mismatch:
- The whole orchestration runs in the browser. If any later call fails, the ticket stays filed with no report.
- This path has never run from a deployed site (hop 2).
- Partner path (parked): it calls SUBMIT and stops (`TicketCenter.tsx:393-434`), and nothing server-side posts the analysis.
  Separately, a partner's own input is refused at the analysis POST (`CLOSED_COMPOSITION_REQUIRED`, row D2-S97). The cause is
  `home_firm_id` set on a non-OPAL_GLOBAL owner (AR-y-318 offline reconstruction, @83eb798a08; not deployed).

Close: after J7, one staff filing from deployed DEV. Proof: the ticket carries `report_ref.request_id` and the request record carries
its `ticket_id`.

### 7. "Add commentary" -> `commentary_requested` on the request -- MISSING

What exists:
- The portal sends only `answers.add_commentary`. `commentary_requested` appears once in `src/`, in a wire type.
- The deployed `irpt-ycharts-generate` refuses any unknown key: `submission.py:16` `PUBLIC_FIELDS`, raising
  `UNKNOWN_OR_SERVER_OWNED_FIELD` at `:51-52`. Deployed `acceptance.py` does not carry the flag. The source (IB-pr-455/456) has moved
  past the live bytes.

The exact mismatch: the flag can neither be sent nor accepted.

**Ordering hazard:** if AR-y-317 (the portal always sends the flag) ships before IB-pr-456, every Ticket Center submission is refused.

Close: IB-pr-456 deployed first (waits on Andrew's act f61b), then AR-y-317. Proof: a request record reads `commentary_requested: true`.

### 8. Request -> resident -> which engine -- MISMATCHED

What exists: r29 `ycharts/generate/resident_worker.py:165` `OPAL_PRODUCER_PRINCIPALS = ("andrew@opalinvest.com",)`. `producer_for`
(`:172-177`) reads `record.owner.principal_id`; every other owner goes to the YCharts path (`:748`). HEAD is the same, and the test at
`test_resident_worker.py:772` asserts `svc-irpt-analysis` -> YCHARTS.

The exact mismatch: any filer who is not Andrew, staff or partner, gets the YCharts path, and that path is broken (hop 9). C-SWITCH
was approved by Andrew on 10-13 (call 1) and ruled by the CTO (pivot first acts, act 2). It has not landed in source or in r29.

Close: key the Opal producer on an accepted record whose `ticket_id` the ticket table confirms as an `analysis_request` (CTO option 3),
under a never-widen pair. Proof: a ticket-filed request traced to OPAL_ENGINE.

### 9. Is Opal's data enough, or one YCharts call -- INCOMPLETE (Opal) / MISSING (YCharts API)

What exists:
- The Opal producer (`ycharts/research/opal_producer.py`, `held_data.py`) reads holdings, `etf-classifications` and
  `opal-data-etfs/bbg/<date>/characteristics.parquet`, and renders with `pricing=False`.
- The one OPAL_ENGINE report on record (REQ-5e4149d2, @46e01935cf) has **257 sections: 6 VALUE, 251 NOT_AVAILABLE**. Returns, risk,
  benchmark and risk-free figures are absent ("NOT_IN_THIS_VERSION").
- The YCharts path is a signed-in browser session (`ycharts-host/ycharts_session.js`; build portfolio, generate, download the vendor
  PDF). It is not an API call. Its last run (10-11 17:10Z) failed NO_AUTHENTICATED_PROBE (@77f135f74f), and no successful run since
  was found.
- The gateway has `ycharts_time_series` and `ycharts_snapshot_metrics` tools, not wired to IRPT (not called here).

The exact mismatch: the Opal database lacks the price and return series the report needs, and there is no working single-call
fallback.

Close: choose ONE price/return source (a verified estate store, or one YCharts data-API read through the gateway), compose it into the
producer, and re-count sections. Proof: the same request renders with return and risk sections VALUE.

### 10. Compile -> report stored -- INCOMPLETE

What exists: `run_opal` (`resident_worker.py:507`) -> `opal_producer.produce`.
- The PDF goes to `irpt/<firm>/state/ycharts_opal_reports/request=<id>/overview.pdf` (the resident's `_address` builder) and is
  retained as family `YCHARTS_OPAL_REPORT`.
- The AnalysisReport document is published through `publication.finish`; the index row is `REPORT#<id>#<rev>`.

The exact mismatch: the Opal engine renders an **Overview only** (`overview_map.json` `report_type: OVERVIEW`). It ignores the chosen
variant (Comparison, Multi-Comp) and the comparisons.

Close: add the comparison variants to the Opal map, or refuse variants 2 and 3 visibly at the form. Proof: a Comparison request renders
its comparison sections.

### 11. Report READY -> analysis-ready queue -- MISSING

What exists: `send_ready_if_ticketed` (`resident_worker.py:233-244`) sends `analysis_ready` only when `ticket_id` is set and
`commentary_requested is True`. The queue URL comes from bindings (`resident_installed.py:411-415`).

The exact mismatch:
- The r29 `resident_bindings.json` has `analysis_ready_queue_url: null`.
- The queue (send allowed only to `irpt-ycharts-runner-role`) holds 0 messages.
- The flag never arrives (hop 7).

The host unit environment was not read; it could set `IRPT_ANALYSIS_READY_QUEUE_URL` outside the bindings.

Close: a resident release whose bindings carry `analysis_ready_queue_url`. Proof: one ticketed, flagged request sends one message.

### 12. Queue -> commentary drafter -- WORKS (wired, never fed)

What exists: event-source mapping c352ea29, Enabled, batch 1, from `outlook-global-commentary-draft-analysis-ready-queue` to
`outlook-global-commentary-draft-lambda`. The only two invocations on record are on 10-11, before the current code.

Close: feed it by closing hops 7 and 11.

### 13. Drafter inputs -- MISMATCHED

What exists:
- The drafter reads only the request's composition, via `irpt-commentary-composition-read-lambda`, projected to variant, comparison
  keys, account type and holdings categories (`drafter.py:30,79-85`).
- `themes = []` (`:83`), and `gold_rows` returns `[]` (`lambda_handler.py:282`), so every draft starts "NO PRECEDENT".

The exact mismatch: Andrew asked for "an AI layer on the output of the YCDGEN ... generated internal report", and said "we already
have all this information saved in the transcripts". The live drafter reads neither the report's figures nor any transcript.

Close: one reader of the produced report's key figures, plus a non-empty transcript source, kept "very simple". Proof: a draft citing
the report's figures.

### 14. Model -- WORKS (configured; not called here)

What exists: `MODEL = "kimi-k3"`, secret `astn/kimi/api-key` (`drafter.py:24-25`). The secret exists.

The exact mismatch: Andrew said he would use "Astra". What Astra names is still unidentified.

Close: one line to Andrew; switching is one setting.

### 15. Drafter -> stored commentary -- MISMATCHED

What exists: `irpt-commentary-draft-store-lambda` stores JSON `{"text","request_id","model","generated_at","status":"DRAFT"}` as
`application/json`, family `ANALYSIS_COMMENTARY` (`commentary_draft_store.py:62,168`), and sets `commentary_ref` once.

The exact mismatch: Andrew asked for "the AI investment commentary pdf on branded opal form". The drafter writes text, not a PDF. The
only branded PDF in the code is the packager's single package PDF: the Opal report with a DRAFT commentary page inside
(`opal_packager.py`, `produce_package`, AR-g-12). There is no standalone commentary PDF. PRD v0.5/v0.6 places the branded PDF after
FWD-1.

Close: Andrew answers one question: is the package PDF (report plus commentary page) what he means, or a separate commentary PDF? Then
build the one he names.

### 16. Commentary ready -> packager -- MISSING

What exists: the drafter sends `commentary_ready` to `outlook-global-commentary-draft-commentary-ready-queue`. Only the resident may
receive from it, and only when bindings carry `commentary_ready_queue_url` and a `packager` block (`resident_installed.py:49-51,
101-106,423-424`).

The exact mismatch: both are null in r29. One message has sat unconsumed since ~10-11 06:10Z (INFERRED; the CTO notes it expires ~10-15
06:10Z).

Close: the same resident release as hop 11, binding `commentary_ready_queue_url` and `packager {api_base, secret_name}`. Proof: the
queue drains and a ticket gains a package.

### 17. Packager -> ticket package -- INCOMPLETE

What exists:
- `POST /tickets/{id}/package` is admitted for `svc-irpt-packager` only (`lambda_function.py:120`), for 49financial, cottonwood and
  inflection.
- It takes four pointers: `report_ref`, `pdf_ref`, `original_ref`, `commentary_ref` (`:144`). It also writes `report_ref` once
  (`:1689-1709`).
- The secret `opal/ticketing/svc-irpt-packager` has never been accessed.

Live table `opal-tickets`:
- 31 tickets; 18 `analysis_request`, all 18 with an attachment.
- 4 with `report_ref`, 1 with a package, 1 with `draft_commentary`, 1 OPEN.
- **The one package is synthetic** (release-28 sitting, pointers `synthetic/r28/...`), on TCK-20261014-2965a5e0. That ticket is still
  OPEN, so it is the only item in the staff Open queue and it shows test pointers.

The exact mismatch: the route works, but no real package has ever been attached.

Close: one real ticket packaged by `svc-irpt-packager` after hop 16. Separately, the synthetic r28 ticket is closed or removed by its
sitting's owner (`0.7.0_AE_CloudOps~AQ2`).

### 18. Open tab -> list -- WORKS

What exists: `GET /api/scoped/tickets?status=open` (`tickets.ts:129-139`), admitted for internal staff and live. Rows show id, type,
title, requester and status.

The exact mismatch: the attachment block renders only when `draft_commentary || package` is present (`TicketCenter.tsx:845`). Before
packaging, the advisor's file and the form are not shown.

Close: show the original and the form from the ticket itself, before a package exists.

### 19. Open ticket -> attachments opened -- INCOMPLETE

What exists (`AnalysisRequestParts.tsx:315-358`), PACKAGE_FILES lists four items:
- **Original:** signed URL via `GET .../analysis/requests/{id}/original` on `irpt-status`.
- **Form as filled:** rendered inline from `answers`.
- **Report:** shown as in-page sections via `GET .../analysis/{jobId}/sections`, not the generated PDF.
- **Commentary:** `packageFileHasReader` is false, so the page shows "(no reader yet)". The draft text shows only from
  `ticket.draft_commentary`.

The exact mismatch:
- The branded `pdf_ref` is not listed (`:311`).
- The live `/pdf` route serves the report's own retained PDF (`ops/owned_report.py:292-320`), not the package PDF.
- The `ANALYSIS_COMMENTARY` family is readable only by the packager (`reports/repository.py:32-35`).
- Every reader is gated on `ticket.report_ref.request_id` (`:324`).

Close: a staff reader for `commentary_ref` and `pdf_ref`, with the commentary attachment shown as the branded PDF Andrew names in hop
15. Proof: staff open every attachment from one OPEN ticket.

### 20. Observability -- MISMATCHED (INFERRED)

What exists: `COMMENTARY-POST` and "draft stored" are `LOG.info` lines (`lambda_handler.py:346,348,355`). The function's log format is
Text with no application log level, and nothing calls `setLevel`.

The exact mismatch: at the runtime's default WARNING level, the proof line named in the pivot direction never appears. A zero count of
it proves nothing.

Close: set the application log level to INFO, or log these at WARNING.

## Recommended completion sequence

1. **The live thread: one Opal staff user, one 49financial market-value file, Overview, no comparisons, Add commentary on, on deployed
   DEV**, to four attachments opened from the OPEN ticket, recorded as ONE trace. It crosses hops 2, 6, 7, 8, 10, 11, 12, 15, 16, 17
   and 19. The first hop (filing, J7) belongs to `2.0.0_SA_COO~Y2`. Five acts are required, in order:
   - (a) J7: the staff submit with a firm choice (portal DEV).
   - (b) C-SWITCH by ticket-confirmed `ticket_id` (hop 8).
   - (c) IB-pr-456 deployed, then AR-y-317 (hop 7); IB-pr-456 waits on Andrew's f61b.
   - (d) ONE resident release binding the analysis-ready queue, the commentary-ready queue and the packager (hops 11 and 16).
   - (e) The ticket page's commentary and branded-PDF readers (hop 19).

   The report will render with most sections NOT_AVAILABLE. That is acceptable for the thread and NOT for Andrew's use.
2. **A report worth reading:** one price/return source composed into the Opal producer (hop 9), then the share-quantity upload (hop 4).
3. **The commentary Andrew described:** the drafter reads the report's figures and the transcripts (hop 13); the PDF shape on his
   answer (hop 15); the model on his answer (hop 14).
4. **The variant he chose:** Comparison and Multi-Comp in the Opal engine (hop 10).
5. **Bad inputs:** the swap UI in the Ticket Center and C-SWAP step 2 (hops 3 and 5).
6. **Hygiene:**
   - INFO logging (hop 20);
   - the original and the form visible before packaging (hop 18);
   - the synthetic r28 ticket out of the Open queue (hop 17);
   - the partner path (hop 6, D2-S97) when Andrew opens the Ticket Center to clients.

## Acceptance

One reconciled trace per case, each following one request:
- from the staff filing through the upload, the ticket, the request record (`ticket_id`, `commentary_requested`) and the resident's
  producer choice;
- then the stored report, the analysis-ready message, the draft, the commentary-ready message and the package pointers;
- ending with each attachment opened from the OPEN ticket.

Cases: firms {49financial, cottonwood, inflection} x variants {Overview, Comparison, Multi-Comp} x inputs {market value, share quantity,
a misspelled ticker, an unknown security} x failures (the drafter fails, the packager fails, the YCharts session is down). Each failure
must be visible on the ticket (FWD-4).

## Evidence anchors and limits

Source inspected at workspace `116d679d62`, portal PROD `6a5926fc` and DEV `97c66c93` (identical trees). Fresh reads at 15:10-15:35Z:
Lambda code downloads and digests, resident tarball sha256 and bindings, queue attributes, event-source mappings, secret metadata (no
values), a counts-only scan of `opal-tickets`, and log-group reads.

**NOT verified:**
- No signed-in UI walk.
- The deployed CloudFront bundle was not downloaded (CI success and the git tree only).
- The resident host's systemd environment and journal (no SSM).
- The body of the stranded commentary-ready message.
- The `irpt-status` code bytes.
- Whether the YCharts session signs in today.
- Whether Kimi K3 answers.
- The live D2 log line (its cause is AR-y-318's offline reconstruction).

Anchors:
- `infra/aws/lambda/ticket_center/lambda_function.py`
- `infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py`, `resident_installed.py`
- `infra/aws/lambda/investor-reporting/ycharts/research/opal_producer.py`, `opal_packager.py`, `held_data.py`
- `infra/aws/lambda/investor-reporting/intake/` (`uploads.py`, `submission.py`, `acceptance.py`, `upload_suggestions.py`, `resolution_kimi.py`)
- `data/transcripts/scripts/commentary/` (`lambda_handler.py`, `drafter.py`, `commentary_draft_store.py`)
- `portal/src/pages/TicketCenter/` (`TicketCenter.tsx`, `analysisRequest.ts`, `AnalysisRequestParts.tsx`), `portal/src/lib/firmAccess.ts`, `portal/src/api/endpoints/tickets.ts`, `investor-reporting.ts`
- `org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md` v0.6 @664ef68df1
- `org/tier2_senior/0.7.0_AE_CloudOps~AQ2/deliverables/irpt_anlreq_r29/` (release-29 sitting)

## Andrew-direct request -- verbatim record

Channel: Andrew at the dell2 terminal, session of `4.0.0_SA_CRO~DELL2`, 2026-10-14 ~15:1xZ.

> I need a /closer trace on "The pivot_docs ticket center YCDGEN workflow". I need to know where are there missing or unfinished adapters. If I were to walk this process end to end, where is it not functional? That means checking frontend at the start and back (does the ticket center properly issue the Analysis Request and does a finished analysis request display in the "Open" tab for Opal Users with the necessary attachments, those being the initial submitted xlsx/csv from the advisor + the YCDGEN generated analysis report + the AI investment commentary pdf on branded opal form)? As far as backend operations, we need to know that when that request is made, we need to track where it goes in our cloud, if we can successfully identify and swap typo/missing securities with our AI web-search and matching solution, if we have all the necesary information in the Opal Database to manage the full report generation (if not can we make a single api call to the necessary YCharts location), do we have a function that compiles that data into a report, where are those reports stored, is the AI Investment commentary solution set up to run and also generate its own report, how do those reports get sourced for displaying in the ticket center "open" tab. We need to make sure this process works end to end and we know every single step and where we are failing. Go investigate now.

Follow-up, ~15:2xZ (record @011515bb70):

> Opal staff should not be "held" from filing, they can file they just realistically won't, but we should have that available for testing. Ticket Center does not need to be displayed for client users at this time, only opal users need to see it, so that part is accurate.

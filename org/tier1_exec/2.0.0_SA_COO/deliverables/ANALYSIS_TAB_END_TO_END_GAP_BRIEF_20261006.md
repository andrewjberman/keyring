# ANALYSIS TAB: end-to-end trace brief

Prepared by 2.0.0_SA_COO~Y on 2026-10-06, at Andrew's word ("run /closer trace 'analysis tab' and identify where the breaks are happening"). Read-only assessment plus proposed closure requirements. No application change, no vendor call, no deploy, no schedule. Reads made: the deployed Lambda configuration and code zip of `irpt-ycharts-generate` and the configuration of six sibling functions; Andrew's own browser recording (HAR) of 2026-10-06 ~18:23Z; DynamoDB and journal reads on the resident host (all earlier today). Claims marked (inferred) were read from code and not run.

## Design finding

The Analysis tab lets an Opal user (Global scope) submit a portfolio and open an Opal-made Overview. The data path is: the browser uploads a holdings file (or picks a client), the intake function stores it and queues a resolve, the resident worker normalises it, the user presses Generate, the resident worker runs the Opal producer, and the status and report routes feed the page.

How far the build is from that design: every hop has code on both sides. The break is that **the two sides disagree about what "Global" means for a write**. The backend treats Global as a read-only scope (resolve fans out over firms; browse refuses `global`; an upload or a prospect submit whose owner firm is `global` or `opal-capital` is refused). The portal treats Global as the working scope and never tells the backend which firm a write is for. Work worth keeping: the Global resolve, search, selection and holdings reads all work live (Andrew's HAR, all 200); the prospect path produced READY Overviews on 2026-10-05; the resident host, producer, classifier and pyarrow now work (B2 installed and proved).

## Current measurement

Read at 2026-10-06 19:16Z from the live account:

| function | handler | last modified | code sha256 |
|---|---|---|---|
| `irpt-ycharts-generate` | `generate_installed.lambda_handler` | 2026-10-04 01:57Z | `uFTONal/Rh...` (592,791 B) |
| `irpt-status` | `status_installed.lambda_handler` | 2026-10-05 04:18Z | `jhGc2J4Q5E...` |
| `irpt-directory-search` | `entry.lambda_handler` | 2026-10-06 01:39Z | `cmNmYm1jey...` |
| `irpt-holdings` | `entry.lambda_handler` | 2026-10-06 01:44Z | `SRANzIGzWj...` |

The deployed `irpt-ycharts-generate` zip was downloaded and compared file by file with source at workspace HEAD: 63 `.py` members, **44 equal, 11 differ** (`canonical_profile_reads`, `composition`, `loaders`, `maintained_sources`, `owned_requests`, `publication_worker`, `publisher`, `repository`, `resident_worker`, `retention`, `served`), 8 have no same-name source file. `submission.py`, `prospect_submission.py`, `generate_installed.py` and `custody_submission.py` are equal to source. `IRPT_DIRECTORY_BUCKET_MAP` holds `49financial`, `cottonwood`, `inflection` only. Not invoked: any upload, any submit, any vendor call. The portal was read at e107538d (served on port 5174), not the deployed portal.

Machine-readable evidence: none beyond the files cited. The HAR is client data and is not committed.

## Adapter map

| Surface | Provider and endpoint | Existing work | Gap |
|---|---|---|---|
| Firm selector | portal state `firmId`; `POST /directory/resolve` | resolve for `global` and per firm works (HAR 200) | the option list is built from the Global context, empty once a firm is chosen |
| Tenant on a write | `?selected_tenant=` on `/analysis/inputs`, `/analysis` | the client-pick path sends it (HAR) | the no-client path sends none |
| Upload | `POST /analysis/inputs` (`irpt-ycharts-generate`) | CSV and XLSX in the template lane, 1 MiB cap | tenantless request from the page; refusal reads as an unnamed error |
| Resolve | SQS `irpt-generation` to the resident worker | worker live on `409e3066d1-st24` | 0 jobs handled since install: nothing has reached it |
| History and status | `GET /analysis/requests`, `GET /status/{id}` (`irpt-status`) | wired | history only mounts after a client is picked |
| Report | `GET /analysis/{id}/sections` | wired; Opal form unlanded on portal DEV | docs contract v1 vs served v2 |
| Custody Generate | `POST /analysis` without `input_id` | none | `snapshot_id` is server-minted, no route returns it |

One firm's or path's success does not certify another's: the 2026-10-05 prospect READY rows were made through the prospect path and certify nothing about the client-pick path.

## Start-to-finish walk

### 1. Sign-in -> Global scope -- WORKS

`POST /directory/resolve` with `selected_tenant=global` returned 200 for Andrew's principal (HAR entry 0); `irpt-directory-search` accepts `global` for an internal principal on the resolve operation only (`_authz/served.py:997-1005`). Close: none.

### 2. Firm selector -> `firmId` -- MISMATCHED

`FirmDropdown.tsx:87-102` builds its options as Global plus `catalogue.firms`; `index.tsx:351` supplies `catalogue.firms` from `globalContext?.firms ?? []`; `globalContext` is null as soon as `firmId` is not `global` (`index.tsx:118`), so after Cottonwood is chosen the list is `[Global]`, the select's value is not in it, and the browser shows "Global (All)". The page state is still Cottonwood (Andrew's screenshot: the identity card reads "Cottonwood Capital Advisors (not supplied)"). So the control shows Global while the page is single-firm. Picking a client does not change `firmId`; the display flips when the context resolves. Close: build the option list from the catalogue query (`index.tsx:96-102`, already fetched for Global) and keep it for the whole session; proof: choose a firm, pick a client, the dropdown still names the firm.

### 3. Firm choice -> `selected_tenant` on the write -- MISMATCHED

`ProspectComposer` takes `(selectedScopeRef ?? scopeRef).selectedTenant` (`AnalysisTab.tsx:266`). With no client picked `selectedScopeRef` is null and `scopeRef` is built by `scopeRefFrom`, which never sets `selectedTenant` (`header/search.ts:420-426`). The code comment at `AnalysisTab.tsx:263-264` records the same defect for an earlier run ("the upload then went out without one") and the fix covered only the picked-client path. The backend refuses a write with no firm: `UploadService._allow` rejects owner firm `global` or `opal-capital` (`intake/uploads.py:170-177`), and the prospect submit does the same (`ycharts/generate/submission.py:127-137`). `directory-browse` with `global` is refused FIRM_BINDING (`served.py:998-999`). Neither refusal has a named public code (inferred: UNEXPECTED). Close: for a write, the portal sends the firm named in the selector (or the picked client's firm), and refuses on the page, in words, when none is chosen; the backend returns a named code. Proof: one upload with the firm chosen shows `selected_tenant=cottonwood` on the request and a `UPLOAD#` row in `irpt-requests`.

### 4. Search and pick a client -> selection -- WORKS

HAR entries 5-8: browse, `POST /selections`, `GET /holdings/sel_...`, all 200 with `selected_tenant=cottonwood`. Close: none.

### 5. Upload a file -> `/analysis/inputs` -> normalised input -- INCOMPLETE

Page: `ProspectComposer.tsx:235-260` builds a JSON body with `file_base64` and `file_type` and calls `analysis-input-upload` (`investor-reporting.ts:1100-1104`). Server: `intake/uploads.py:83-94` accepts `csv` or `xlsx` by extension, 1 MiB cap, stores the original as `ORIGINAL_HOLDINGS`, writes `UPLOAD#` and `NORMALIZATION#` rows, queues one `resolve_upload`, and answers `{upload_id, input_id: null, state: RESOLVING}`; `input_id` appears only after the resident worker resolves it, and the page re-posts the same token to learn it. The page keeps the staged file and result only in React state (no query cache, no storage), and the composer is keyed on `firmId`, scope fingerprint and revision (`AnalysisTab.tsx:265`), under a tab keyed on the whole scope (`TabShell.tsx:165`): any firm or client change discards a staged upload. **Unexplained:** Andrew's screenshot shows "Working…" with "No file chosen yet"; `busy` is set only inside `upload()` (`:237`) and the button is disabled without a file, so a file was cleared while a call was in flight. I did not find the reset by reading; it needs a live reproduction with the browser console open. Measured on the host: 0 of 112 polls handled since 03:40Z, and no cottonwood row dated 2026-10-06, so no upload has reached the backend today. Close: fix hop 3, persist the staged file and result across a remount (hold them above the keyed composer), and reproduce the "Working…" state once with the console open. Proof: upload an XLSX, change the firm selector, the review rows are still there; the row `UPLOAD#` exists.

### 6. Upload -> what the page shows after (history) -- INCOMPLETE

`OwnedRequestHistory` mounts only when a client selection is accepted (`AnalysisTab.tsx:221-222,391-401`), lists submitted requests, not uploaded inputs, and the prospect composer never calls `onSubmitted` (the client composer does, `:277-280`), so a prospect Generate is not re-listed until a remount. The only trace of a reviewed upload is the header prospect card, state in `SelectionWorkspace`, hidden once a client is selected. Close: mount the history for the prospect path and re-list after a prospect Generate. Proof: Generate, the new request appears in the list without a reload.

### 7. Generate -> `POST /analysis` -> queue -> resident worker -- WORKS for a prospect input with a concrete firm; MISSING for a picked client

Prospect: `validate_public_request` (`submission.py:45-85`) accepts `input_id` with null client, snapshot and accounts; one SQS message is sent; the 2026-10-05 prospect requests REQ-01c90366... and REQ-e7af8e8a... read READY in Andrew's HAR (entries 25-26). Picked client: the page builds `snapshot_id` from the holdings' `source_set_revision` (225 characters with commas for this client; `contracts/adapt.ts:1123`), which fails the 200-character, `[A-Za-z0-9_.:-]` check in `contracts/submission-request.ts:15-16` before any send (the HAR shows no POST); the server wants the opaque `cst_` id it mints (`_scope/accepted_custody.py:106`, "never installed as an HTTP request route"), and `custody_submission` raises `CustodyFactoryRequired`. Row `IRPT_YCDGEN-S13`. Close: (prospect) none beyond hop 3; (client) a route that returns the server's snapshot id and a browser that sends it verbatim.

### 8. Status -> report on the page -- INCOMPLETE

`irpt-status` serves `status-job`, history and `analysis-report` (`reports/status_installed.py`). The Opal-form page (cells e-6, j-6) is on portal branches, not on DEV. The docs contract `AnalysisReport.schema.json` (v1) is closed, has no `provider` and requires `vendor_artifact`; the served OPAL_ENGINE document follows the v2 schema that lives only under `infra/.../_contracts/`; `responses/analysis-report.response.schema.json:57-69` still points at v1 properties (read, not run). Close: land e-6, j-6, p-6 on portal DEV after review, and publish the v2 contract under `docs/contracts/`. Proof: Andrew opens an Opal Overview on the page.

## Recommended completion sequence

1. **The live thread: prospect upload to opened report.** One person (Andrew), one Cottonwood portfolio, the Prospect card, firm named in the selector, Overview, Generate, opened on the page, as ONE trace artifact (HAR plus host read plus run record). It crosses hops 1, 2, 3, 5, 7, 8. First-hop owner: the portal seat that owns `index.tsx` and `AnalysisTab.tsx` (hops 2 and 3 are one change there).
2. Staged upload survives a remount and the history shows the new request (hops 5, 6).
3. Named refusal codes for a write with no firm (hop 3, backend).
4. Picked-client Generate (hop 7): the server snapshot id route.
5. Contract publication (hop 8).

## Acceptance

One reconciled trace per case, from the user's selection through the browser request, intake row, queue message, run record, status and rendered page. Cases: firm chosen / not chosen; CSV / XLSX; one remount between upload and Generate; expired session; a firm outside the bucket map.

## Evidence anchors and limits

Source read at workspace `003116dc5f` (local) and portal e107538d. Verified fresh by me: the dropdown option list, the tenant-less `scopeRefFrom`, the two backend refusals, the snapshot id rule, the deployed-vs-source comparison, the HAR. Taken from two read-only helper reports and not re-run by me: the exact line numbers in `uploads.py`, `served.py` and `status_installed.py`, the claim that the history route is mounted only with a client, and that `listAnalysisRequests` on the live client is unserved (I did not confirm this last one and do not rely on it). Not done: no signed-in walkthrough of the no-client upload, no live upload, no console capture, no check of the deployed portal.

- `portal/src/pages/InvestorReporting/index.tsx`, `header/FirmDropdown.tsx`, `header/search.ts`
- `portal/src/pages/InvestorReporting/tabs/analysis/AnalysisTab.tsx`, `ProspectComposer.tsx`, `OwnedRequestHistory.tsx`
- `infra/aws/lambda/investor-reporting/intake/uploads.py`, `ycharts/generate/submission.py`, `_authz/served.py`

## Andrew-direct request -- verbatim record

Channel: this terminal (2.0.0_SA_COO~Y session), 2026-10-06.

> I am suspecting that the frontend is not adequately tied to the backend for any of these operations. I need you to run /closer trace "analysis tab" and identify where the breaks are happening because it is not functional. WHen i upload an xlsx, nothing persists on the frontend that I can see. Furthermore, I don't think you actually understand how firm selection works because as an Opal User, I am global. anything i do is global. i dont believe the firm selector ID even matters beyond search potentially, but even when you do search, the firm selector reverts back to GLobal as depicted here. Run the trace and figure out where the adapters are unfinished/don't exist before we waste more time on thisl

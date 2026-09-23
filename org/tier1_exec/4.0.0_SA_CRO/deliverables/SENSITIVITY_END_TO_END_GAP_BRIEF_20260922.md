# Sensitivity analysis: two inputs, one end-to-end product

Prepared by 4.0.0_SA_CRO on 2026-09-22. Assessment and proposed closure specification; no implementation, deployment, schedule activation, or vendor job performed.

## Finding

There is substantial reusable code, but the product is disconnected at input, request translation, execution, result publication, and export. Lane B is not implemented as a portal upload workflow. Lane A's directory and model/holdings work is not yet a proven selected-account-to-YCharts positions adapter. Parsing three input units does not mean generation supports all three: the current YCharts recipe accepts dollars only.

The target is:

    Lane A: header registry -> relationship -> selected account(s) -> custody positions
                                                                               \
                                                                                -> frozen normalized portfolio
                                                                               /           |
    Lane B: prospect CSV -> column/unit mapping -> validation/correction --------             v
    common recipe/profile/comparisons -> authorized submit -> durable job -> YCharts session
    -> upload holdings -> create portfolio -> verify settings -> generate/download vendor PDF
    -> extract/certify sections -> publish report/status -> portal view
    -> freeze Opal export bundle -> authenticated print renderer -> validate/store -> download

## Connector-by-connector assessment

### 1. Existing data estate to client/relationship registry — source adapters exist

`directory_runner.py` adapts the three firms' existing silver/gold data into common DirectoryEntry records. 49F uses authoritative relationship/account dimensions; Inflection uses Orion account and household mappings; Cottonwood uses Black Diamond Relationship ID. The adapters read data already landed by upstream pipelines; a dropdown keystroke does not call vendors.

Directory artifacts exist in the per-firm serving buckets. The earlier live audit found September 17 source dates, so current refresh completion needs acceptance evidence even though the directory schedule was enabled.

Close: use one top-level relationship grain for client/relationship/household. Preserve vendor and firm identifiers behind a canonical ID; do not merge people merely because names match. Return permitted relationship membership and explicit incomplete/unmapped coverage.

### 2. Registry API to header and account selection — partial adapter, proposed browsing UI absent

The header already has ClientSearch, FirmDropdown, selection adapters, and account narrowing. It is a query-driven combobox. Backend search ranks matches and limits results; an empty query slices the current projection. It has no cursor-based alphabetical registry contract.

Close: add the requested flat, alphabetical, paginated relationship registry in the header, with optional search. Use stable ordering by normalized display name plus canonical ID, and a revision-bound cursor. Clicking a relationship exposes its permitted account list; the selected account(s) become the shared tab context. Use firm/disambiguation labels for duplicate names. A prospect upload needs a separate input selection that does not require a registered client.

### 3. Selected accounts to analysis positions — model snapshot adapters exist; complete positions bridge not established

The holdings builder adapts SmartX/49F, Eclipse/Inflection, and Cottonwood rebalancer/custody sources into a HoldingsSnapshot with model structure, amounts, coverage, and source clocks. This is not automatically a flat, security-level portfolio suitable for YCharts. In particular, model targets, sleeve valuation, custody positions, and residual coverage are different grains and cannot all be summed as holdings. The source exposes a security identifier on the 49F position path; the other builders must not be assumed to supply equivalent security-level output simply because their overlay snapshots reconcile.

Close: a server-side adapter must resolve the selected accounts back to actual custody positions in the Opal data estate, including opal-data-assets where applicable; select a completed source revision; retain ticker/security identity, quantity/value, currency, and dates; consolidate duplicate positions without counting both parent and child values; and reconcile total selected-account value. Actual holdings are the default analysis basis. A target-model analysis must be an explicit different input basis.

The earlier live audit measured empty `investor-reporting/holdings/` prefixes for all three firms, QA snapshots dated September 11, and a disabled production holdings schedule. Populate and refresh the serving path if this snapshot route remains the lane's input dependency.

### 4. Prospect CSV to parsed rows — parser exists; portal connector absent

`intake/parse.py` reads CSV/XLSX and supports SHARES, USD, and WEIGHT_DECIMAL. It preserves row/column provenance, reports ambiguity, proposes rather than silently applies share-class substitutions, and retains unmatched rows. It originates in the intake implementation, not a portal upload flow. A case-insensitive search of the IR frontend and routes found no upload surface; the current composer explicitly requires client, account, and snapshot IDs.

Close: build file selection/upload, server-owned upload identity and storage, column mapping, explicit amount-unit selection, preview, correction, and submit. Give prospect portfolios an authorized advisor/firm ownership context without inventing an existing-client/account relationship. Bind future reads/downloads to that ownership. Connect the parser to this route and replace specimen-only security mapping with a maintained resolver.

The existing Microsoft Graph/email intake adapter is a separate input mechanism. It is not required for either requested lane and cannot substitute for a browser CSV uploader. Its disabled schedule is not a prerequisite to fixing these two lanes.

### 5. Both lanes to the common portfolio — missing assembled adapter; unit conversion unfinished

Use one immutable normalized-portfolio artifact after review, with: source lane; owning firm/advisor; client/account refs OR prospect/upload ref; source revision/as-of; original rows and units; resolved security IDs; analysis amounts; reconciliation totals; findings/corrections; and content hash. Subsequent jobs reference this artifact rather than rebuilding a different latest snapshot.

The parser's normalized rows and the recipe's resolved dollar-holdings envelope are different contracts. `recipe.validate_envelope` and `holdings_csv` refuse non-dollar inputs. No connected conversion is present in this path.

Close each unit explicitly:

- Dollars: preserve the supplied USD values and reconcile the sum.
- Shares: obtain compatible prices from a dated source and compute shares x price; record price source/time and currency. A missing price becomes a correctable finding.
- Weights: distinguish percentage from decimal input, validate the sum and rounding tolerance, then either implement and prove native weight submission to YCharts or use a clearly identified reference notional to make a dollar portfolio. A reference notional must never be presented as actual client AUM. Weights alone do not determine real dollar value.

Both lanes must apply the same cash, duplicate ticker, unsupported security, currency, and non-positive amount rules. Every input row must be represented, corrected, or explicitly excluded with a reason; none disappears silently.

### 6. Portfolio to report composition — recipe adapter exists; catalogue/profile connectors missing

The composer and recipe encode zero comparisons -> Overview, one -> Comparison, two to five -> Multi-Comp. Backend recipe code supplies vendor template details and checks effective settings. The frontend explicitly documents missing comparison-catalogue and advisor/firm profile sources; it currently asks for opaque comparison keys and cannot prefill prepared-for/by/contact details from a real profile.

Close: expose a permissioned comparison/model/ETF catalogue, resolve selections to vendor identities on the server, and supply the actual advisor/firm/prospect or client profile. Freeze comparisons, settings, title, template/recipe version, and profile with the portfolio revision.

### 7. Browser to API/gateway to generation request — routes and authorization exist; request adapter missing

The exact source mismatch is material:

- Composer emits `request_id, client_id, account_ids, snapshot_id, variant, comparison_keys, report_title`.
- LiveClient submits this body unchanged to POST `/api/scoped/investor-reporting/analysis`.
- `generate/entry.py` copies only `variant, comparisons, settings, message_refs, attachment_refs, normalized_holdings, findings, corrections`.
- The intersection is only `variant`. The entry does not resolve the requested selected accounts/snapshot/comparisons/title into the worker's required internal envelope.

Thus transport reachability and a QUEUED answer do not demonstrate that the requested portfolio was accepted intact. For the same permitted scope, changes only in ignored fields can also collapse to the same server request digest.

Close: one versioned public request contract for a normalized portfolio reference and composition; a server resolver that checks ownership/current entitlement, loads the frozen inputs, resolves catalogue/profile, and constructs the actual internal job envelope; validation at both boundaries; real paired frontend-to-handler tests. Existing edge/API guards must support the prospect ownership path as well as account-entitled Lane A. Browser values must not author their own permissions.

### 8. Accepted request to durable worker — queue adapter exists; consumer/storage composition unfinished

The submit entry sends SQS. The earlier live audit found no Lambda event-source mapping for the generation queue. `job.lambda_handler` still refuses the unfinished live setup; it does not assemble the session, queue, fence, and worker dependencies. GenerationJob has reusable orchestration, but JobStore and MemoryBlobs are in-memory implementations in this module.

Close: persist accepted request/revision and durable job identity; connect the queue to an actual worker; adapt job transitions, mutation claims, and artifact storage to the real DynamoDB/S3 implementations. Prove retries/redelivery use durable idempotency, not just a deterministic request string. Keep queued/preparing/generating/extracting/ready/attention states and attempt identity consistent across worker and reader. Wire failure/retry/dead-letter handling without blindly repeating an uncertain vendor mutation.

### 9. Worker to authenticated YCharts — transport/broker adapters exist; operational assembly unfinished

`transport.py` has separate live and replay transports, cookies/CSRF/WAF handling, identity validation, and a protected artifact downloader. `session/broker.py` reads/verifies the versioned session through a Secrets Manager adapter and coordinates bounded recovery. It does not perform login/capture. The browser host/session acquisition and publication layer is a separate connector. The audited host was stopped.

Close: connect worker lease/fence, session acquisition/publication, broker, live transport, refresh/resume, and operational authorization. Prove correct user identity and one recoverable eviction; reconcile an ambiguous POST before trying again. Existing per-use operating gates are part of the current environment; this brief does not change them or treat approval as a substitute for missing code.

### 10. YCharts recipe to original vendor PDF — substantive adapter exists

GenerationJob implements identity/template verification -> holdings upload -> portfolio creation -> effective-settings read-back -> security validation -> report generation -> download. A separate downloader verifies PDF structure and avoids passing session cookies to artifact hosts. Research has produced actual PDFs for the three variants, using a synthetic portfolio; worker replay tests exercise additional control paths.

Close: feed the common normalized artifact through this actual worker, connect durable mutation/receipt storage, and demonstrate all three variants. Read-back must agree with holdings and selected settings. New browser requests must be traceable to the exact resulting PDF, with retries reusing the correct artifact.

### 11. Vendor PDF to certified AnalysisReport — extractor adapter exists; automatic publication connector absent

Extraction/certification libraries emit typed sections with units, dates, source coordinates, disclosures, and explicit unsupported/missing results. They do not justify inventing values from chart pixels. The generation worker currently writes an attempt with `sections: []` and `extraction_validation: UNCERTIFIED`; it does not invoke extraction/certification in `after_create`.

Close: trigger extraction after durable PDF storage, certify against the exact PDF revision, publish AnalysisReport JSON and protected original-PDF reference, and retain supported/unsupported coverage. Define when partial extraction can be displayed/exported and which sections block release. Do not equate 'PDF downloaded' with 'analysis ready'.

### 12. Published report/status to portal — view adapters exist; serving/polling/correction gaps remain

The frontend has AnalysisReport adapters, native section rendering, request/revision displays, and a protected vendor-preview component. But LiveClient refuses request listing because v1 has no list route; the tab's report-selection path depends on that list. The submit composer retains its issued job internally rather than wiring it into the report list/polling path. getJobStatus exists but is not connected to a screen. submitCorrection also refuses because there is no dedicated correction route; the intended revised-submission path needs composition.

The backend status loader reads a job lease and can report RUNNING or UNCERTAIN, never READY. More critically, `ops/entry.py` maps the `/analysis/{jobId}/sections` operation to that same status-only loader, not to a stored AnalysisReport loader.

Close: serve actual job/revision/status and report data from durable stores, wire the issued ID to UI polling and result retrieval, provide permissioned history/list retrieval, and connect correction/resubmission to a new immutable revision. Refresh or reopening the page must recover the job. Ensure the report adapter receives an AnalysisReport, not a status envelope.

### 13. Displayed report to Opal export — bundle/render/download pieces exist; submit chain not connected

The portal has shared report layout/print work and export-bundle adapters. Backend modules freeze/persist bundles, dispatch browser rendering, validate PDF content/fonts, finalize artifacts, and issue receipts/protected download metadata. However, the deployed export entry explicitly returns NOT_READY instead of calling the controller. The prior backend round-17 review found the assembled render-identity contract unproven; follow-on work repairs verifier/enforcer/asset-allowlist mismatches. The local AnalysisTab's own Export control remains disabled; shared export machinery alone is not proof of a connected analysis export.

Close: select the exact released analysis revision -> freeze bundle including portfolio/settings/sections/disclosures/profile/assets -> call export controller -> dispatch to a working render host -> authorize the pinned portal print route and its assets -> render the same shared layout -> validate bytes/content/fonts -> store artifact and final receipt -> expose an authorized Opal download. Carry prospect ownership as well as client/account entitlement through bundle/render/download. Re-check access at download and keep vendor signed URLs server-side. A vendor preview PDF and the final branded Opal PDF are distinct artifacts.

## Recommended closure order and acceptance

1. Agree one normalized portfolio and one request/result contract, with both input identities. Fix the seven-field request mismatch before treating enqueue success as progress.
2. Connect a dollar CSV and a real selected account through that same normalization and validation service. Then prove shares and weights explicitly; do not advertise the parser's units as generation capabilities prematurely.
3. Connect durable queue execution, session/recipe, PDF storage, extraction, and real report/status serving. Prove a complete Overview before expanding the test matrix to Comparison/Multi-Comp.
4. Connect UI polling/history/correction and the header registry browsing experience.
5. Connect and deploy the actual export controller/renderer/receipt/download chain behind the existing Dev gate.

The product acceptance matrix must cover Lane A for each of the three firms and Lane B for dollars, shares, and weights; three variants; duplicate/retry, bad ticker, missing price, incomplete coverage, session expiry, correction, page reload, and revoked access. One run ID must link submitted inputs, normalized artifact, vendor request/settings, original PDF, extracted report, displayed revision, and exported PDF. A successful isolated adapter test is not a substitute for this trace.

## Evidence and limits

Source review used workspace around `ff80aa85dff985ebe51f6a614346f037390fa550` and portal `7dd3d067a17ee00b878ecfceff23c557649a2331`; concurrent shared-workspace activity may advance HEAD. Current source was inspected with comp-which/comp-find/comp-read and bounded direct file reads. No signed-in browser workflow or fresh vendor generation was performed. Live AWS observations cited here are from the preceding audit on the same day, approximately 18:51–18:57 UTC; they were not remeasured for this brief.

Evidence files:

- `data/assets/scripts/gold/investor_reporting/directory_runner.py`
- `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py`
- `infra/aws/lambda/investor-reporting/directory/handler.py`
- `portal/src/pages/InvestorReporting/header/ClientSearch.tsx`
- `portal/src/pages/InvestorReporting/tabs/analysis/{composer.ts,GenerateComposer.tsx,AnalysisTab.tsx}`
- `portal/src/api/endpoints/investor-reporting.ts`
- `infra/aws/lambda/investor-reporting/intake/parse.py`
- `infra/aws/lambda/investor-reporting/ycharts/generate/{entry.py,recipe.py,job.py,transport.py}`
- `infra/aws/lambda/investor-reporting/ycharts/session/broker.py`
- `infra/aws/lambda/investor-reporting/ycharts/extract/{extract.py,certify.py}`
- `infra/aws/lambda/investor-reporting/ops/{entry.py,status_loader.py}`
- `infra/aws/lambda/investor-reporting/export/{entry.py,handler.py,dispatch.py,render.py,download.py}`
- `.runtime/codex-seats/4.0.0_SA_CRO/irpt_product_audit_20260922.json`
- `.runtime/codex-seats/4.0.0_SA_CRO/irpt_data_audit_20260922.json`
- `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_BCKEND_ROUND_17_20260922.md`

## Andrew-direct request — verbatim record

Channel: user message to Codex seat 4.0.0_SA_CRO, session date 2026-09-22; message timestamp unavailable in the model context. Recorded with this brief, not represented as implementation authorization or a message to other seats.

> What I need from you is first a brief on what is needed to close the gap to end to end product for sensitivity analysis. cover every connector. trace the process from start to finish through all layers, including mentions for where there are adapters versus where there are not, and the state of the adapters that are unfinished. THere are two ways that sensitivity analyses can be produced. One is via selecting a relationship/account from the dropdown option/registry (may be good to develop a flat, alphabetical, paginated registry of all client/relationship/household names (these are all same grain, just different vendors refer to them differently). This should appear in the header panel, it is the most logical place for it. You can click any user and it drills down to account list and you can select the account there for various tab functions. the other pathway for sensitivity analyses is uploading a csv that has the columns for ticker and share/dollar/or weight amount. this is because sometimes we want to run ycharts analyses on new accounts who are not currently clients. accordingly the normalization of those holdings, from input lane A (registry, opal-data-assets) versus input Lane B (csv upload) both need to get to the same place. Take it from there and all the way out through the export functionality.

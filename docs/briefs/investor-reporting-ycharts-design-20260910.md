# YCharts Analysis — intake, retrieval and serving design

**September 10, 2026 · 4.0.0_SA_CRO · Investor Reporting WS3.** Companion to the [new child brief](investor-reporting-ycharts-brief-20260910.md). This annex supplies the explicit instructions and sequencing Andrew requested. “Captured” identifies observations in supplied artifacts; “proposed” identifies implementation design. No production execution is implied.

## 1. Product and execution flow

```mermaid
flowchart LR
    A[requests@ forwarder] --> B[Internal Microsoft mailbox]
    B --> C[Cloud mailbox poller]
    C --> D[Attachments and versioned request]
    D --> E{Inputs resolved?}
    E -->|Yes| F[Generation queue]
    E -->|Needs correction| G[Analyst input review]
    G --> F
    F --> H[YCharts session and report runner]
    H --> I[Vendor PDF and evidence]
    I --> J[Section extraction and Opal rendering]
    J --> K{Validation passes?}
    K -->|Yes| L[Authorized Analysis tab and branded export]
    K -->|Exception| M[Authorized correction or review]
    M --> D
```

Use small services with clear state ownership: mailbox Lambda; parser/analyzer worker; durable request ledger and work queue; the **BDAPI-style transient EC2/SSM session and browser runner**; report persistence/section adapter; shared WS1 presentation and authorization. These are components inside the existing project, not new project registrations. The browser runner can issue the known API calls from its authenticated page context, keeping YCharts' browser session and WAF SDK active. Avoid adding a second permanent browser service solely for each stage.

The first usable internal milestone is an automatically generated vendor PDF with its validation state. Full product completion also requires the Opal section rendering and matching export. Treating the vendor PDF viewer as the final Analysis tab would leave parent O4 and child O5 unfinished.

**Release policy proposed for Andrew's review:** automatically serve complete, validated reports; route exceptions to an authorized reviewer. The recordings' existing analyst queue is evidence of today's workflow, not authorization for a mandatory future staffing commitment. Universal analyst approval was asked as an explicit alternative. Until Andrew answers, automatic validated release is the design proposal and no live release policy is enabled. The brief's opening explains which recorded ambiguities motivate exceptions and what evidence lets them proceed programmatically.

## 2. Cloud email intake

### 2.1 Schedule and destination

The public intake address is **requests@opalinvest.com**; the destination mailbox is **opalbloomberg@opalinvest.com**, the Sitez identity. Preserve actual holdings attachments through forwarding. Configure the destination/folder explicitly and verify it with a representative forwarded message; existing desktop/delegated access is not proof of unattended mailbox permission.

Proposed EventBridge **Scheduler**, timezone **America/New_York**, flexible window **OFF**:

```text
cron(0/15 8-23 * * ? *)
```

This expresses 64 scheduled intake ticks daily, including weekends, from 08:00 through 23:45. Midnight ends the window. The named timezone follows Eastern daylight/standard time automatically. These are mailbox ticks, not vendor login or generation ticks. Already accepted generation work may finish outside the intake window; overnight mail is collected on the next scan. [AWS schedule and timezone semantics](https://docs.aws.amazon.com/scheduler/latest/UserGuide/schedule-types.html).

### 2.2 Mailbox authentication and reads

Use a cloud application identity with **Application Mail.Read** scoped to the single intake mailbox. Prefer the estate's established Microsoft application/certificate provisioning pattern once its actual grant is verified. Exchange Application RBAC can express the mailbox scope; inspect both RBAC and Entra grants because permissions are additive and an unscoped Entra grant can defeat that restriction. No Mail.Send or mailbox write permission is needed for this intake design. [Microsoft application RBAC](https://learn.microsoft.com/en-us/exchange/permissions-exo/application-rbac).

For the configured mailbox and intake folder:

```text
GET /v1.0/users/{mailbox-id}/mailFolders/{folder-id}/messages/delta
GET /v1.0/users/{mailbox-id}/messages/{message-id}/attachments
GET /v1.0/users/{mailbox-id}/messages/{message-id}/attachments/{attachment-id}/$value
```

Retrieve message body/routing metadata and original MIME where needed for evidence. List and download actual `fileAttachment` objects; unwrap attached messages if a forwarding rule packages the request that way. A `referenceAttachment` is a link and does not satisfy the agreed file-input contract. Do not start a SharePoint crawler as an implicit fallback. Mail.Read covers attachment reads. [List attachments](https://learn.microsoft.com/en-us/graph/api/message-list-attachments?view=graph-rest-1.0), [attachment contents and types](https://learn.microsoft.com/en-us/graph/api/attachment-get?view=graph-rest-1.0).

Include `Prefer: IdType="ImmutableId"` on every applicable read. Persist mailbox identity and immutable message ID; retain `internetMessageId`, attachment hashes and routing evidence as additional provenance. Immutable IDs survive movement within the same mailbox but not every archive/export/reimport operation. [Microsoft immutable identifiers](https://learn.microsoft.com/en-us/graph/outlook-immutable-id).

### 2.3 Checkpoints, duplicates and failure recovery

Follow every opaque `@odata.nextLink`, then save the completed `@odata.deltaLink`. Delta is per folder; if a mailbox rule moves requests, bind the actual destination folder. Persist each selected message and its attachments before committing the scan checkpoint. Do not use the read/unread flag or a rolling “last 15 minutes” filter as the processing ledger. [Microsoft message delta](https://learn.microsoft.com/en-us/graph/api/message-delta?view=graph-rest-1.0).

Proposed durable behavior:

1. Acquire a short mailbox scan lease; concurrent/retried schedule invocations join the same checkpoint.
2. Persist raw input to S3 and conditional intake records to DynamoDB. Store exact object version/hash receipts. Commit a durable outbox item with request acceptance; dispatch from that outbox to SQS so a crash between database commit and queue send cannot lose work.
3. Deduplicate transport delivery by mailbox/message/attachment identity. A secondary fingerprint can flag forwarded duplicates using source message identity, attachments and normalized request intent within the same authorized scope. Do not deduplicate solely by holdings hash: intentional fresh reports may use identical holdings.
4. Record an explicit activation cutoff for the first run. Initial synchronization can establish the delta cursor while only creating jobs for requests at/after that cutoff; historical backfill is an explicit operation. On an invalid/expired cursor, resynchronize with the existing ledger so old mail does not become new jobs.
5. Honor provider Retry-After and backoff on throttling/transient failures. A failed attachment download leaves retryable durable intake state; advancing a cursor cannot erase it. Late scheduler retries do not discard mail; the next permitted scan resumes the checkpoint.

Recognize requests using the configured route and authenticated sender/advisor mapping. Preserve original forwarding metadata, but treat quoted sender text and body instructions as input, not authority to change permissions, recipients or execution policy. Capture unmatched/ambiguous client mapping for review instead of guessing from a name.

## 3. Input contract and programmatic interpretation

The supplied root `manifest.json` is a completed-run example with both inputs and outputs. Its private client values are not a universal template. The program should separate request inputs, normalized holdings, vendor bindings and attempt/result receipts.

| Contract group | Proposed fields and meaning |
|---|---|
| Identity | `request_id`, `revision`, canonical `firm_id`, `advisor_id`, `client_id`, permitted account set, original sender/requester evidence, mailbox/message/attachment references |
| Request | `variant` = overview/comparison/multicomp; title; prepared-for/by; organization; advisor branding reference; ordered comparisons; source holdings as-of |
| Holdings | Rows containing original symbol/name, input unit, exact decimal dollars or weight, resolved typed YCharts security ID/name, source file/sheet/row, resolution status and proposed substitution if any |
| Configuration | Fee `0.003` annually; weighting mode; rebalance/dividend/start/valuation/tax settings; template identity/version; all requested overrides |
| Validation/review | Check results, missing fields, ambiguous identities, reconciliation differences, resolution evidence, optional human corrections, release basis and revision |
| Vendor/result | Exact `model_portfolio_id` and typed security ID, upload record, effective settings, report request fingerprint, submission state, artifact hash/version/pages, section mapping version, dates, incidents and status |

Parse supported spreadsheets deterministically before interpreting free text. The packet demonstrates spreadsheet holdings and dollars; weight-based input is described by the analyst but still needs a representative upload fixture. Initial parser support should be explicit for tested XLSX/CSV layouts. Preserve original files, ignore decorative inline images and avoid treating untested PDF statements or protected workbooks as successfully parsed. Unsupported formats remain actionable input exceptions.

A schema-constrained analyzer can infer report type, client/advisor, requested models, prepared-for text and column meanings from the email plus attachment labels. Attach source references to inferred fields. Use deterministic schema, total and identifier checks after inference. An LLM does not invent absent holdings, choose an arbitrary similar ticker or alter access scope. Kimi is selected for the **browser runner**; using the estate's structured text-analysis provider for email interpretation is a separate implementation choice, not an assumption that the browser credential can process every document.

Input rules grounded in the recordings and captures:

- Use YCharts' **client portfolio** type. Preserve dollars versus percentages and their units; parse money with decimal arithmetic. A percentage input expressed as 25 must not become a 25.0 fractional weight. Compare included value/weight, excluded value and unresolved rows explicitly.
- Map cash to **`$:CASH`**. Resolve share classes and CUSIPs against YCharts; the recorded BRKB/BRK.B example illustrates why punctuation changes need evidence. Model abbreviations such as LT/LTC need a versioned alias table tied to a specific saved model.
- Do not silently discard unsupported bonds, SMA/REIT labels or ambiguous funds. The recordings describe proposing a closest ETF proxy for analyst review. A clearly marked provisional draft may be generated from an explicit proposed-input revision; it cannot be released as the original holdings analysis without the recorded correction decision.
- Pin **management_fee = 0.003** and **management_fee_frequency = annually**. The July create calls use 0.01; do not inherit them. In UI preferences, a displayed percent may use a different scale from the create API; validate the effective stored portfolio setting.
- August captured defaults: `rebalance_frequency=quarterly`, `reinvest_dividends=false`, `start_of_series=oldest`, `level_as_of_type=prior_close`, `tax_status=non_qualified`, benchmark `^SPXTR`. Preserve these as the recorded recipe until deliberately revised. Do not infer the client's tax status from the default. “No Benchmark” is the report template's presentation, not evidence that the portfolio has no benchmark setting.
- Obtain cover information from the request and controlled advisor/Opal profile. Do not hard-code personal contact values from a HAR or turn a legacy `PUT /accounts/preferences` into an incidental change to Alyssa's defaults.
- Multiple files may describe one account, several accounts or alternatives. Preserve grouping explicitly; conflicting totals or unclear aggregation yield input review. The attachment snapshot is authoritative for that request; current silver holdings are useful context, not a silent replacement.

The example manifest records a two-cent source/confirmed-value difference. Preserve the difference and its explanation, including any precision conversion; do not manufacture a universal tolerance from one example. No fixed holdings-count cap is ratified: one July creation contains 103 items.

## 4. Session library and exact BDAPI runner adaptation

### 4.1 Reuse the chosen implementation

Reference source:

```text
infra/aws/ec2/bd-49f-auto-login/bd_49f_auto_login.js
infra/aws/ec2/bd-49f-auto-login/run-bd-auto-login.sh
infra/aws/ec2/bd-49f-auto-login/package.json
infra/aws/terraform/bd-49f-auto-login/{iam.tf,instance.tf,main.tf}
```

The runner is Node/Playwright with Kimi perception and actions, bounded retries/backoff, DOM fallback, cookie capture and persistence. The current Kimi configuration names `kimi-k2.6` and reads `astn/kimi/api-key`; retain configuration as a versioned dependency rather than assuming that model name is permanent. Reuse the SSM artifact-deployment style and transient EC2 lifecycle. Proposed YCharts resources have their own instance, instance role, inline policy, instance profile and security group. The controller starts the instance and dispatches work; the host's completion lifecycle stops the transient runner as in the reference pattern.

Use native AWS egress, as the selected wrapper does. A legacy proxy comment or TLS bypass in BD source is not a YCharts requirement: preserve normal HTTPS verification and do not add a proxy fallback. Whether YCharts accepts the runner's actual native environment remains a live implementation check.

**No OTP stage.** BD's success logic is coupled to `otpEntered` and firm-specific cookies/identity checks. Replace it with YCharts-specific authenticated-page recognition, required cookie capture and a successful authenticated report-catalog/owned-portfolio probe. Do not fake OTP completion to reuse the BD branch. An unexpected authentication challenge receives a distinct failure reason; this brief does not build an OTP service.

The shared library should expose `getSession`, `probeSession`, `acquireSession`, `persistSession` and `withAuthenticatedPage`. Keep credentials out of model prompts, logs, command arguments and screenshots; fill them locally in the browser. Send only necessary, masked login-page images to Kimi. Persist cookie state only after authenticated success, and consider secret-write failure a failed refresh.

### 4.2 Secret separation — measured current state

| Secret | Measured/current contract | Intended use |
|---|---|---|
| `ycharts/login/credentials` | Created this turn; username/password read-back verified; us-east-1 | New runner's login input. Import the resource into the chosen infrastructure ownership without putting secret values in Terraform state |
| `ycharts/credentials` | Existing value contains `cookies`; used by legacy market-data clients | Preserve its contract. No overwrite or automatic migration in this brief |
| `ycharts/session/current` | Resource exists; AWSCURRENT value absent at inspection | Proposed captured session bundle output, coordinated with YALP_MDSRC consumers |
| `astn/kimi/api-key` | Exact shared-key reference in the BDAPI runner | Read only by the YCharts runner role where authorized |

The older `ycharts-session-capture/index.mjs` expects a login at `ycharts/credentials`; live state contradicts that expectation. The old market-data client's transport also parses JSON only on HTTP 200, whereas report creation returns 201. Neither can be reused unchanged.

Scope the new role to reading YCharts login/current session and the Kimi key, writing **only** the YCharts session, and accessing its own artifacts. Give the intake/parser roles mailbox/input access independently; they do not need vendor passwords. Do not copy the BD `blackdiamond/49f/*` grant. Cookie state belongs in Secrets Manager, not the generation bucket or portal response.

Store a versioned cookie jar with cookie domain/path/expiry attributes, capture time, authenticated identity, browser/user-agent context and successful probe metadata. If existing consumers require a flattened `cookies` field, provide an explicitly versioned compatibility adapter after inspecting those consumers. Include no password in the session bundle.

### 4.3 Browser context, shared login and recovery

The HARs show `ycsessionid`, `csrftoken`, AWS WAF and load-balancer cookies, plus `X-CSRFToken` and `X-AWS-WAF-Token`. Use current browser cookies and the YCharts page's normal SDK; allow Set-Cookie updates. A saved cookie string alone cannot refresh the observed rotating WAF token. Page-context API requests must supply current CSRF/WAF headers; `credentials: include` alone does not add them.

Serialize automation's use of the shared login with a lease/fencing token. Alyssa remains free to sign in and evict it. Check a current session at the start of actual work; start the Kimi runner only when missing/invalid or evicted. On an auth failure, distinguish explicit concurrent-login evidence, ordinary auth expiry, WAF challenge and an unrelated 403 before selecting recovery. Reacquire with bounded backoff; continue from the durable stage. Repeated evictions become a retryable/attention state, not an infinite login contest.

The reference's instance **i-0fa1846f04ed7e337** belongs to BD49F and is not the proposed YCharts host. CTO message 95301 reports a 12:24:50 UTC estate snapshot with five matching declared nodes; vintage and attribution are retained. This seat's compiler graph read failed because the AWS shim was parsed as Python, so it supplies no independent graph measurement. The source is sufficient to specify the pattern; current deployment must be measured before modifying infrastructure.

## 5. Explicit vendor retrieval instructions

### 5.1 Evidence and configuration fixtures

The [HAR inventory](sources/INVESTOR_REPORTING_YCHARTS_HAR_EVIDENCE_20260910.json) is reproducible with the [offline profiler](../research/investor_reporting_ycharts_20260910/profile_handoff.py). Indices below are **zero-based in supplied slim files**. The handoff's original 473-entry numbering is not this 220-entry file's numbering.

| Variant | Captured template / report type | Ordered securities | August POST → PDF GET | Presentation |
|---|---|---|---|---|
| Overview | 14141822 / `aggregate_security_overview` | Primary only | 165 → 168 | Portrait |
| Comparison | 14141824 / `aggregate_security_comparison` | Primary + one comparison | 186 → 190 | Portrait |
| Multi-Comp | 14141847 / `multi_security_comparison` | Primary + 2–5 comparisons; captured example has 2 | 211 → 213 | Landscape |

Template IDs are captured identities, not a permanent cross-tenant API guarantee. Discover and validate the current accessible template by name/type/security cardinality before generation. Keep a versioned request-builder fixture corresponding to the August capture. Read private source fixtures locally; never commit their client values, cookies or signed URLs.

### 5.2 Resolve holdings, upload and create

1. Load the immutable request revision and verify its authorization and input checks. Acquire the job lease and authenticated page. Navigate to `/model_portfolios/fixed/client/new/?targetFolder=null` to enter the normal client-portfolio flow.
2. Resolve securities using YCharts search and metadata. For comparison selection, `GET /search/suggest/report_securities?q=...` returns typed buckets; select a canonical security, not a first text match. Search the portfolio category for Opal saved models. Validate with `GET /securities/securities_info?securities=...`. `P:` denotes a portfolio, `M:` a fund identifier, `S:` a separate account, and cash is `$:CASH`; preserve returned types instead of deriving everything from ticker spelling.
3. Upload the holdings file through the browser's actual file input and capture `POST /model_portfolios/fixed/holdings_upload/client`. **The multipart upload field names are absent from all three HARs.** Browser-driven upload is the explicit initial mechanism. Capture and validate its request before replacing it with pure HTTP; do not invent a `file` field or assume skipping upload works.
4. Parse the upload response. July HAR 03 entries 37/176/306 show `status`, `errors`, `rows`, `weight`, `upload_record_id`, `isExtractedHoldings`; each row has `security_id`, `display_security_id`, `display_name`, `weighting`. Interpret `weighting` using the returned unit and original input. Check every expected holding and the reconciled sum. August entries 42/47 show 400 then 200 with bodies missing; the error schema and exact cause are not established. Retain private diagnostics and show a useful sanitized input error rather than logging raw client data.
5. Set a stable unique vendor name containing an opaque request/revision suffix. Submit `POST /model_portfolios/fixed/` as multipart **`portfolio`** JSON and **`items`** JSON, carrying the real upload record ID. Let the browser set multipart boundaries. Bind exactly the normalized holdings and settings; do not create a saved portfolio when the advisor merely searches for a client.
6. The captured `portfolio` object contains 28 fields, enumerated in the evidence inventory. In addition to name/description/type/settings, carry explicit valuation, benchmark, legacy/proxy flags and the unused null fields from the versioned fixture. Item fields are `security_id`, `display_security_id`, `name`, `weighting`, `weight_text`, `current_weighting`, `target_weighting`, `dollars_weighting`, `shares_weighting`, `avg_cost_basis`. Match each field's captured unit and semantics; do not copy the amount into every numeric field. The initial certified fixture is dollar-weighted; a weight-mode fixture must confirm the alternative.
7. Expect HTTP 201 and persist **`model_portfolio_id`** immediately. July HAR 03 entry 43 proves that response field, alongside `parent_folder_id`. If the field is absent, mark creation indeterminate and reconcile by the exact deterministic name, owner, type, creation evidence and holdings/configuration fingerprint. Never use `rows[0]` or the newest folder/portfolio. Do not retry an uncertain creation blindly.
8. Read back the exact owned object and verify `client_portfolio`, typed `P:` identity, holdings/value and effective settings. The server may resolve `prior_close` to a concrete custom date; preserve requested and effective values separately.
9. Poll `GET /model_portfolios/{id}/status` for that exact object until available, recording any `needsReviewMessage`. The capture's individual status calls show available with `progress:null`; pending calculation is observed in `collection_status` and list state. Validate the individual pending response during implementation. Do not expose the global 375-portfolio collection to the portal or fabricate a percent-complete bar. Use bounded configurable polling; the observed roughly minute-long calculation is a measurement, not an SLA.

### 5.3 Build and submit the requested report

1. Discover `GET /custom_pdf_reports/generate/collection?securityId={primary}` and fetch `GET /custom_pdf_reports/generate/{template_id}`. Verify accessible type, name, orientation and security count, then retain the complete selected template definition plus its hash.
2. Construct primary-first `security_ids`, with exact typed comparison objects. Call `POST /custom_pdf_reports/validate_report_securities/{template_id}` with JSON `{"security_ids":[...],"modules":null}`. The three captured positive results are HTTP 200 `{}`. Negative response shapes are not captured; surface them as validation failures until classified.
3. Build the report envelope from the August fixture, substituting every client/security/cover binding with this request revision. The inventory records all **34 top-level keys** and **34 modal keys**. Preserve their exact names, casing, empty-object/null distinctions and duplicated values; a smaller body has not been validated. The older July body has 33 keys and should not be the default.

| Field group | Required binding |
|---|---|
| Securities | Top-level `security_ids`; `generationModalsState.primarySecurity`; canonical names/types/IDs and ordered comparison objects |
| Comparison asymmetry | Comparison uses `secondarySecurity` and an empty `comparisonSecurities` array. Multi-Comp uses `comparisonSecurities`; Overview/Multi retain the captured empty **object** for `secondarySecurity` with null ID/name/type fields, empty error and false disable flag |
| Template and wizard state | Full fresh `selectedReport`; current captured modal structure including generation flags, menu/fetch state, requested section order and indices; reject drift instead of silently dropping unfamiliar required state |
| Cover | `report_title`, `prepared_for`, `prepared_by`, `organization`, contact fields and `custom_field`, plus their corresponding `reportTitle`/`coverPageInfo` modal values from the same profile |
| Options and disclosure | `as_of_date_option`, `designation_type`, branding group, naming convention, export option, disclosure footnote, custom labels, dollar conversion/security level values, talking points and custom text, plus modal counterparts; derive amounts/labels from the current request |
| Chart/table scope | `fund_chart_securities_choice`, `scatter_plot_securities_choice`, `comp_table_securities_choice`, `timeseries_table_securities_choice` and matching modal choices |
| Unused context | Captured Hartford identity fields remain null; do not copy unrelated client metadata from a fixture |
| Unconfigured scenarios | `sections: []`, `reportState: null`, `serialized_transition_analyses: {}`, `saved_hypothetical_id: null`, `saved_analysis_plan_id: null`, `risk_profile: null`, with matching empty modal configuration |

4. Persist the request fingerprint, template hash and **SUBMITTING** checkpoint before `POST /custom_pdf_reports/{template_id}`. Use page-context JSON fetch, current CSRF/WAF headers, same-origin credentials and normal browser Referer/Origin. Do not replay incidental integrations/notification/background-job calls or update global preferences as part of the report.
5. Allow the POST to finish. **All six observed successful report calls returned HTTP 201 with `{report_url, zip_url}` directly.** The report renderer is synchronous in this capture. Give the client a configurable timeout above the observed 34.7-second maximum with headroom; expose an asynchronous *Opal* job to the portal so a long vendor call does not hold a browser request open. Do not invent a vendor report-job ID or poll `/background_jobs/in_progress` for this result.
6. Persist the successful response securely and download `report_url` immediately. The matching GETs use the same signed URL and return HTTP 200; captured signatures have roughly one-hour validity. Treat it as a temporary capability. Permit only the captured/validated YCharts artifact host and controlled redirects, retain normal TLS checks and redact query strings from logs. A presigned URL is never the permanent portal artifact address.
7. Validate PDF magic/content type, parseability and page count; compute a hash and persist the original bytes to the request's encrypted generation prefix. Empty `zip_url` does not imply a second artifact. Record S3 version/hash before completing the job. All six HAR PDF bodies are absent, so this download/parse step remains a live validation requirement.

### 5.4 Retry decisions

```text
if a durable vendor PDF receipt exists: reuse it for shaping/review
else if a successful report response has a still-valid URL: retry artifact download
else if report submission is indeterminate: reconcile; do not blindly resubmit
else if a verified portfolio binding exists: resume availability/report steps
else if portfolio creation is indeterminate: reconcile exact identity and content
else: perform validated upload/create
```

A lost connection after report POST may mean the vendor completed work. No vendor idempotency key or report-history reconciliation API was established here. Record an **uncertain submission** and inspect authenticated browser/report history or obtain an explicit retry decision before another generation. The same distinction applies to uncertain portfolio creation. Object hashes prevent duplicate storage; they do not prove exactly-once vendor side effects.

## 6. Encrypted records and durable job state

`opal-data-ycharts` returned NoSuchBucket at the measured cut. Proposed creation uses default **SSE-KMS**, blocked public access, TLS-only access, versioning and role/prefix permissions. Bind an actual KMS key and service-role grants through infrastructure code. Do not claim encryption exists before deployment. Set lifecycle/retention deliberately under the existing records policy; no arbitrary retention period or permanent raw-diagnostic retention is introduced here.

Suggested keys use opaque scope/request IDs, with client display names held in protected metadata:

```text
intake/YYYY/MM/DD/{intake_id}/message.eml
intake/YYYY/MM/DD/{intake_id}/attachments/{attachment_id}/source
requests/{request_id}/revisions/{revision}/manifest.json
requests/{request_id}/revisions/{revision}/holdings.json
requests/{request_id}/revisions/{revision}/interpretation.json
requests/{request_id}/revisions/{revision}/review/events/{event_id}.json
generations/{generation_id}/attempts/{attempt_id}/request.json
generations/{generation_id}/attempts/{attempt_id}/receipt.json
generations/{generation_id}/vendor/report.pdf
generations/{generation_id}/sections/report.json
generations/{generation_id}/exports/{export_revision}/report.pdf
```

Vendor request/receipt records are private and may contain client information; logging uses IDs, counts, stage, error class and redacted diagnostics. Keep auth headers/cookies/passwords out of these artifacts. Browser diagnostics are restricted and opt-in; redact credential fields before any screenshot capture or transmission.

DynamoDB owns authoritative request state, revisions, leases, outbox and artifact receipts. SQS messages contain IDs/pointers, not raw attachments. S3 owns immutable input/result objects, not queue locks or atomic state transitions. Use fencing tokens to reject writes by a stale worker, conditional transitions to prevent double release, and a retry/dead-letter path that retains the source request.

Proposed lifecycle: **received → interpreting → needs-input or queued → preparing-portfolio → calculating → generating → shaping → validating → released**, with an exception-review branch and retryable, uncertain, failed and superseded states. A valid request passes through without human intervention under the proposed default. Keep displayed status understandable; engine details belong in operator evidence, not advisor navigation.

## 7. Analysis tab and branded output

Use the parent header and authorized client selector. The Analysis tab offers the three report types, an input/assumptions summary, existing reports by date/revision, ordered comparison selection and current generation status. Request search and job polling must not enumerate the shared YCharts account. Switching clients invalidates the active view binding; a late result stays with its original scope.

Proposed `AnalysisReport` envelope:

```text
identity: request/revision/generation + canonical authorized scope
input: holdings snapshot/hash, account coverage, substitutions and fee/settings
comparisons: ordered typed identities and model/version evidence
vendor: YCharts template identity/hash, generation time, original PDF receipt
sections[]: key, title, status, data_as_of, units, values/series,
            source page/region or structured-response pointer, notes/disclosures
validation: check results, automatic or human release basis, optional reviewer,
            released revision/time
presentation: schema/template version, branding asset revision, export receipt
coverage: available/missing/unverified sections and reasons
```

YCharts is the sole analytical source for this workstream. Prefer structured section data if a subsequent authorized inspection finds it. The current captured output is PDF, so the explicit first shaping design is deterministic PDF text/table extraction with page geometry and a versioned section map; retain each value's page/region and original text, unit and date. Reconcile table totals and series against the vendor output. Sections available only as charts require a validated underlying data source or an explicitly identified source-chart presentation; do not invent numerical series by unreviewed visual guessing.

Use the September 9 comparison census as a starting catalog for exposures, fundamentals, risk and drawdown content. It is not a complete three-variant schema. Obtain paired PDFs for Overview, Comparison and Multi-Comp and decide the supported section set with Alyssa/Andrew from those real outputs. A section lacking reliable extraction stays visibly unsupported/partial until resolved. The packet's separate Yahoo/SEC-based engine and sample reports must not be substituted for YCharts analytics.

Render the certified sections using Opal components and the [shared branded PDF specification](investor-reporting-export-narrative-spec-20260910.md). Preserve the vendor's hypothetical/method disclosures and every material date/footnote. Reuse optional advisor logo/profile assets Andrew will supply, with an Opal-only fallback when an advisor logo is absent. Bind preview, released report and PDF to the same immutable data revision; a logo/template change creates an export revision. The WS2 performance/news narrative remains its own content boundary.

Every request, job, review, report and download route enforces WS1's firm/advisor/client permissions on the server. Return controlled short-lived download access to Opal's own stored artifact after authorization; never serve the vendor's signed URL as the persistent report link. Existing shared-login visibility is not entitlement.

## 8. Dependency sequence and remaining evidence

| Dependency stage | Concrete result needed | Evidence still to obtain |
|---|---|---|
| Intake identity and records | Confirm requests@ delivery/folder, cloud Mail.Read binding, encrypted bucket and durable ledger | A representative forwarded message with real attachment form; application/scope checks and deployed storage controls |
| Typed request and resolver | Reconciled holdings, fee/settings, typed comparison mapping and correction revisions | Representative advisor request phrases, actual attachment layouts and a weight-mode fixture |
| Runner/session adaptation | YCharts-specific BDAPI-style runner, secret interfaces and takeover recovery | Native AWS login/probe and session persistence; no OTP workflow is requested |
| Portfolio/report retrieval | Exact upload/create identity and three report-to-download chains | Missing upload multipart/error body; current create/status responses; actual PDF bytes and boundary comparison counts |
| Section adapter and validation | Paired section fixtures, provenance, automatic checks and exception correction | Three vendor PDF families; extraction fidelity and any graph-only data gaps |
| Shared serving/export | Authorized Analysis tab, same-revision Opal PDF and advisor branding | WS1 scope/export integration and cross-client/revocation behavior |

This order states dependencies, not a task schedule or issuance. Input contracts and UI work can proceed while runner and section evidence are completed. Mailbox service principal/folder facts are implementation discovery items; resolved user choices about daily operation, attachments, session takeovers, Kimi and no OTP are not open questions.

The extra handoff question about transformations/downside is a separate evidence boundary. Its captured `reportState`, sections and saved-analysis fields are null/empty. Default three-template generation can be specified now. A custom scenario editor needs the missing analyst run and its parameter/result mapping before it can be claimed.

## 9. Verification and reproduction

Offline inventory command, using the safely extracted private packet:

```powershell
python docs/research/investor_reporting_ycharts_20260910/profile_handoff.py `
  --packet-dir '.runtime/codex-seats/4.0.0_SA_CRO/ycharts-recon/YCharts HAR Handoff - Andrew' `
  --transcripts-dir 'C:\Users\AndrewBerman\Desktop\YCharts Transcripts' `
  --output 'docs/briefs/sources/INVESTOR_REPORTING_YCHARTS_HAR_EVIDENCE_20260910.json'
```

The profiler makes no network calls and emits hashes, shapes, counts and selected configuration facts. It does not emit holdings values, names, native client portfolio IDs, credentials or signed URLs. Preserve the source ZIP/manifest/HAR hashes so discrepancies in handoff prose remain reproducible.

Implementation acceptance should exercise complete and ambiguous email inputs, duplicate/overnight intake, deliberate revisions, wrong-type model search, money/weight/cash reconciliation, eviction at each side-effect boundary, download persistence failure, three report families and authorized/unauthorized rendering/export. Compare to independently retained input and vendor output, not merely to another copy of the adapter's own JSON. No production acceptance test was run in this design cut.

**Evidence:** [HAR inventory](sources/INVESTOR_REPORTING_YCHARTS_HAR_EVIDENCE_20260910.json), [source and cloud metadata](sources/INVESTOR_REPORTING_YCHARTS_SOURCE_EVIDENCE_20260910.json), [Andrew-direct record](../../org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260910_YCHARTS_INTAKE_AND_SERVING.md). Private source folder: `C:\Users\AndrewBerman\Desktop\YCharts Transcripts`. Source code and measured cloud facts establish research substrate; they do not assert a deployed YCharts reporting service.

# Resident Analysis assembly -- exact installer handoff

Y source `4ed7edaaa8` over `57b228ac53` / `84c6e63806` / `ebf8d33985` / inseparable causal batch `fe0ec628c2`, in `C:/Users/AndrewBerman/Desktop/irpt-mvp-y-20260922`.
Authority: closer CONTRACT v1.4 `f1add564fd`, Andrew always-on approval `6fc3f5f785`, build-first `d44d9f3876`; CTO caller review `47e0f95` consumed.

## Executable Y candidate

`ycharts/generate/resident_main.py --factory <P-installed-module>:build_resident_runtime` runs a resident SQS long-poll consumer. `--once` performs one poll for installation verification. Normal logging is bounded and omits exception values, credentials, signed URLs and customer fields. SIGTERM stops between jobs. No import-time AWS or vendor calls.

The factory returns exactly `{assembly: ResidentAssembly(...), sqs: <boto client>, queue_url: <canonical irpt-generation queue URL>}`. Y's assembly constructs the real per-job Dynamo store, FrozenCompositionWorker, FencedReportIndex, CertifiedReportPublisher, PublicationWorker and generation worker. P does **not** need to implement those components.

`ResidentAssembly` arguments: `requests` (actual OwnedRequestReader), `reports` (actual retained ReportRepository with ordinary index), `admission` (actual CompositionAdmission), `session` (actual ResidentSession), `dynamo_client` (low-level boto Dynamo client), `jobs_table`, `requests_table`, `principal_for(record)`, `census_bytes`, `census_sha256`; optional clock only for controls. `principal_for` resolves the accepted acting submitter's **current** shared directory/authorization state on every call. Never synthesize authority from queue IDs or input owner. First candidate uses the existing same-firm publisher contract; Global cross-firm publication remains explicitly unproved.

Construct `ResidentSession(secrets_client, dynamo_client, jobs_table, enrolled_user_id)` using keyword arguments. It shares the permanent provider-operation row in the existing jobs table, reads only `ycharts/session/current`, enforces the enrolled account, and invokes vendor requests in killable request-only subprocesses. Session capture/publication remains the existing dedicated-host capture workflow; this batch does not implement automatic login/refresh or start another session owner.

Worker sequence: closed canonical queue body (wire revision is string `1`) -> current authority/lease -> retained composition/input/configuration -> identity/template -> exact Dollars upload echo -> deterministic portfolio create -> seven effective settings read back -> frozen cover/variant -> generated PDF -> immutable retained PDF -> actual extraction/certification -> fenced report publication -> certified READY. Visibility/job/provider lease renewal is bounded. Permanent mutation intents survive crashes. Ambiguous mutations park ATTENTION; retained-PDF recovery skips the vendor. READY redelivery verifies the stored report/evidence before deletion.

The maintained census is 195040 bytes, above a 32768-byte checkpoint. This batch retains the complete census as registered EXTRACTION_EVIDENCE, verifies its immutable reference and promotes its dependency graph; the checkpoint carries a reference, not truncated census data. Current source bytes: `docs/briefs/sources/YCHARTS_COMPARISON_REPORT_FIELD_SCRAPE_20260909.json`, SHA256 `44853788fa6d39c8b6011c2f86fc82ea6906c2e006935df549f153378c950905`. Package these exact bytes, not a later filename match. No new storage family is needed for this fix.

## Exact P shared installer delta

1. Consume the above Y batch into the shared package, including session child module and its imports; package Python extraction dependencies and the pinned census. Construct the actual shared repositories/current principal resolver and return the factory shape above. Preserve actual actor versus retained input owner.
2. Bind the existing irpt-generation queue URL and existing jobs/requests tables through canonical outputs. Host role needs exact queue receive/delete/change-visibility, current-secret read, jobs get/update, requests get/query/transaction publication, and the existing registered artifact/retention S3/Dynamo permissions. Do not install a parallel Lambda queue consumer.
3. Install one supervised process on approved dedicated `i-0167fd745ad906a66`, keep host running, no inbound/no opal-gateway. Use the controlled single-session-owner cutover; retire old per-job power cycling and separate six-hour probe only as part of the verified replacement. This Python candidate consumes a valid captured session; automated capture/recovery integration is a remaining Y action, not a claim made by source PASS.
4. Finish the paired browser/upload route and schema/family changes already enumerated in TEMPLATE_UPLOAD_HANDOFF_20260923.md and BROKER_TEMPLATE_CALLER_20260923.md. Actual template lookup must execute through the dedicated host; no Lambda/local vendor fallback. Wire accepted submissions to the canonical queue and expose the retained report through the existing scoped request/report readers.
5. Return deployed package/census digests, installed factory path, service/consumer and authority wiring receipts. Rollback stops the new consumer and preserves queue, immutable inputs, permanent intents and captured session; do not delete/requeue intents or stop the always-on host. No standalone six-hour probe should race the resident owner.

## Measured boundary

10 targeted checks PASS in 5.21 seconds: actual frozen recipe + ResidentSession/OperationLease + recipe functions + actual retained repository/certifier/publication through READY; repeat delivery; ambiguous create with no repeat; large-census retained PDF recovery without vendor acquisition; prior publication recovery controls. AWS conditional effects, HTTP and PDF specimen are offline doubles. Ruff and entrypoint import/help pass. No broad suite repeated.

Not claimed: installed service, live login/session recovery, live two-row PDF contents, browser E2E, all-firm publication, complete holdings readback beyond upload echo, full variants/units/corrections/export matrix. First live proof remains AAPL10.01 + VNQ2.02 =12.03 Dollars Overview through certified Analysis screen/reload. Y continues session-owner/refresh and remaining journey assembly while P installs the shared boundary.

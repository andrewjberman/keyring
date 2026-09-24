# Template upload -- first-hop integration batch

Owner Y; consumer/shared writer P; reviewer CTO. Backend source
`ebf8d339859466b48e0f5f2c4ce9a834ddfff290` on fe0ec628c2. This connects the first
Analysis browser upload hop to retained normalized input; not a deployed worker.

## Exact source and executable consumer

Consume `infra/aws/lambda/investor-reporting/intake/uploads.py` and
`intake/tests/test_template_uploads.py` relative to the same reporting root.
Prior template_reader.py, security_resolution.py, portfolio.py and template
freezer dependencies are the unchanged6cfe source set recorded in
UPLOAD_RESOLUTION_IMPLEMENTATION_20260923.md. fe0 broker.py/recipe.py/job.py and
its test remain one causal-repair batch, not isolated file replacements.

The existing build_upload_entry(service) mounts guarded CREATE_INPUT. The actual
UploadService adds required-for-template callback:
`resolve_template(principal, owner, symbols) -> symbol-to-classified-result map`.
It must call the exact SecurityResolver/classify_batch contract. Bare canonical
security identities are not vendor eligibility. Missing callback refuses before
writing. The server resolves owner/current authority; no browser owner allowed.
Shares still require the existing dated price port; Dollars do not invoke it.

## Literal public request shape

Existing legacy `{upload_token,filename,csv_base64}` remains unchanged. New arm:
`{upload_token,filename,file_type,file_base64}`, file_type exactly csv or xlsx.
Example: upload_token `template-upload-one`, filename `holdings.csv`, file_type
`csv`, file_base64 = base64 of `Ticker,Dollars\nAAPL,10.01\nVNQ,2.02\n`.
Optional unchanged fields: declared_currency USD/null, price_date,
reference_notional, supersedes_input_id. Arms are mutually exclusive. Strict
base64 <=1MiB decoded; filename suffix must match type; CSV UTF8/NUL checks;
XLSX remains binary. Same token cannot change bytes/type or switch legacy/new.

P exact shared changes:
1. `docs/contracts/investor-reporting/v1/AnalysisUploadRequest.schema.json`:
   replace required csv_base64 with exclusive legacy/new oneOf; add file_type
   enum[csv,xlsx], file_base64 string1..1398104; filename permits csv/xlsx with
   arm/type-specific suffix; preserve closed fields and existing optional fields.
2. `AnalysisUploadResult.schema.json`: retain existing NORMALIZED shape with
   portfolio.schema_version irpt-normalized-portfolio.v2; add findings array and
   template object for NEEDS_CORRECTION. That arm has input_id:null and all row
   findings/template, not the legacy required reason field. Preserve prohibition
   on input_ref/portfolio for corrections; allow legacy reason arm separately.
   Y template_reader.finding and read_template are exact field definitions;
   consumer fixture is test_findings_preserve_original_without_partial_input_publication.
3. `infra/logic/registry/reporting_policies.json`: admit ORIGINAL_HOLDINGS under
   existing registered prospect_inputs storage, extension bin, unreferenced30d,
   accepted ceiling2555d, same ancestor promotion. Do not alter legacy ORIGINAL_CSV.
   ArtifactRepository family admission follows registry. CSV text/csv; XLSX
   application/octet-stream (already supported). Original filename/type preserved
   in upload row and frozen source. Do not reinterpret XLSX as UTF8.
4. Install concrete UploadService with actual P repository/index/retention/current
   authority and Y resolver caller, package its modules, expose existing
   POST /api/scoped/investor-reporting/analysis/inputs; align common browser
   request/result adapter. Y remains responsible for Analysis tab and resolver/
   worker assembly, not P. These are exact shared requirements, not installed claims.

## Runtime semantics and evidence

Original artifact -> normalized artifact retention DAG uses actual P repository.
Successful retries read retained winner without provider recheck; read_input
re-reads original artifact, validates ref/hash and reparses entire template
projection. Replacement preserves supersedes_input_ref and original expiry.
Original-only findings do not publish a partial normalized input. Current access
is checked before/after provider resolution and again at retained read/publication.

Run `python -m pytest infra/aws/lambda/investor-reporting/intake/tests -q` in Y
worktree using existing pinned IRPT_* test roots from prior integration evidence.
Latest result:206 tests +18subtests; new test_template_uploads.py16 tests. Paired
Entry and actual P ArtifactRepository/DynamoReportIndex/retention implementation
use explicit offline ORIGINAL_HOLDINGS admission and synthetic provider receipt;
AWS-shaped stores are test doubles. No live or public-schema validation claimed.
P must exercise public schema and actual package consumer with this exact wire.

Next Y work is actual resolver/session and resident generation/certifier caller.
Host authority now Andrew6fc3f5f785/CTOf1add564fd. One controlled session-owner
cutover, no parallel probe, host stays running. First live case is12.03 Dollars
Overview through certified Analysis screen/reload, not merely a PDF download.

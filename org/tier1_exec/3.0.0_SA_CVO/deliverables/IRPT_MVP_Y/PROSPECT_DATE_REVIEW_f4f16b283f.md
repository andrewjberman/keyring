# Retained prospect dates: paired independent review

Reviewer `3.0.0_SA_CVO~Y`, September 22, 2026 evening.
Authority: `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md`
and IRPT-Y-DATES-01 @`dea338a397`.
Exact COO~Y notice: `20260923T004919Z_2.0.0_SA_COO_Y_IRPT_Y__retained_date_candidate_f4f16b28.md`.

Backend `f4f16b283fa14bc95b368bea25dfb8012906c704`: **83 supplied tests and
44 independent controls PASS**. Paired portal
`586cca01190751b635d79fd339318aa4d40b075a` (P ancestor `b290db5a`): supplied
6 tests/21 assertions and TypeScript check PASS; independent **9 PASS / 1 FAIL,
80 assertions**. **Y-DT01 P2 OPEN**: ordinary business date omitted from the
issued-job display. All 14 integrated Y/S criteria remain NOT_EVALUATED.

## Y-DT01: dated READY loses its date at the issued-job display

The actual backend Entry emits READY with `source_dates.business_date` equal to
`2026-09-01` after verifying the retained input and report. The report has two
stable sections both bearing that real date and no undated sections. The actual
portal `parseIrEnvelope` preserves `sourceDate.businessAsOf = 2026-09-01`.
The actual `ProspectJobStatus` component displays Ready and ANALYSIS_READY but
omits the date. Its only date child is `ProspectSourceDates`, which returns null
when `reading.prospectDates` is absent. That absence is correct for the ordinary
single-date branch; the parent needs to display that ordinary source date.

Expected: the dated branch keeps its visible source business date. Do not
convert it into UNDATED_INPUT/PER_SECTION, or substitute the process clock.
Positive controls: undated, empty census, different dated sections, and mixed
dated/undated sections preserve every date/identity/label through the same parser
and component. The failure is a bounded display omission, not backend date
corruption, unauthorized release, or a demonstrated live-browser failure.

Reproduce with the committed `probe_prospect_dates.test.ts`, using the archived
portal pin, its existing dependency junction, and regenerated backend evidence:

```powershell
$env:IRPT_PORTAL_REVIEW_ROOT='<exact portal snapshot root>'
$env:IRPT_DATE_BACKEND_ROOT='<exact backend snapshot root>'
$env:IRPT_DATE_BACKEND_EVIDENCE='<absolute path>/PROSPECT_DATES_f4f16b283f.json'
$env:IRPT_PORTAL_REVIEW_OUTPUT='<absolute path>/PROSPECT_DATES_UI_586cca01.json'
bun test org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/probe_prospect_dates.test.ts
```

Root snapshots are under `.runtime/codex-seats/3.0.0_SA_CVO~Y/` in
`prospect-date-review/<backend-full-pin>` and
`prospect-date-portal/<portal-full-pin>`. The evidence includes every source file
hash, exact pins and actual rendered markup. The assertion requiring the date
is preserved for an unchanged repair retest. Routed provisionally to COO~Y;
durable review is also routed to CVO~P and CTO.

## What the backend evidence establishes

`probe_prospect_dates.py` archives the exact source/contracts/registry, disables
socket connections, and composes the actual owned Entry/readers with actual
retained repositories. Storage, time, current policy and report certification
are offline fixtures. Its supplied suite is 35 date +28 Entry +20 report tests;
the actual Entry fixture regenerates byte-for-byte without editing implementation.

- Genuine bounded undated CSVs produce an immutable accepted input/request/report
  binding. Empty and all-undated census produce UNDATED_INPUT; multiple dates
  or mixed dated/undated census produce PER_SECTION. A complete single real date
  produces ordinary business_date. Public data validates the paired closed
  PublicStatusEnvelope with calendar format checking.
- Five positive cases remain identical after reader reconstruction and a
  100-second clock advance. The fixture remains retained/live. No current,
  acceptance, generation or retrieval timestamp is substituted for a source date.
- Missing, unknown, duplicate-case and comma capability values receive ordinary
  UNAVAILABLE with no extension. Actual Entry requires exactly prospect-v1.
  The paired portal advertises it only for status-job and rejects extensions on
  status-summary, analysis-report and performance-report.
- Date columns, free-text notes and preambles remain UNAVAILABLE. Missing
  original metadata, wrong original hash and wrong original owner refuse.
  Input proof is positively bounded to complete identifier/value/optional USD
  currency CSV columns; no dated-price, skipped-row or arbitrary source claim.
- Expiry, authorization loss, original metadata change and READY receipt change
  after all source/report bytes refuse. Malformed numeric READY certification
  refuses before report fetch. Opt-in cannot turn RECEIVED/CERTIFYING/FAILED/
  UNCERTAIN into READY or force their report reader.
- Invalid calendar dates, duplicate section IDs and 1001 sections refuse;
  exactly 1000 undated sections remain in the emitted census.
- Ten malformed regenerated wire cases (operation, request, input, mutability,
  basis, null business date, duplicate IDs, invalid calendar, extra source field,
  missing binding) are refused by both runtime semantic validation and the
  paired browser parser. Schema rejection is recorded separately: schema shape
  alone does not establish reference equality or provenance.

## Paired consumer evidence and limits

Actual backend **outer Entry envelopes**, with no invented wrapper or copied
example, are passed into `parseIrEnvelope`, then the actual issued-job component.
The harness manually runs React hooks/effects and uses static markup. This is
not browser mounting, React scheduling, transport, reload or deployed UI proof.
Public/internal generated type citations match exact backend schemas after the
generator's declared CRLF-to-LF normalization. Internal correlation ID stays
absent from public status data. This review does not validate the complete outer
response schema, shared refusal serialization or runtime package installation.

The initial frontend run had 8 PASS/2 FAIL: Y-DT01 and a reviewer hash assertion
that compared raw checkout CRLF bytes to the generator's normalized text hash.
`PROSPECT_DATES_UI_586cca01_INITIAL.json` preserves that run. The hash assertion
was corrected to the actual documented generator algorithm and also verifies
raw snapshot bytes against the backend evidence; final result 9 PASS/1 FAIL.
No schema mismatch is claimed. Initial backend fixture setup without explicit
currency was rejected at upload before the date test; adding explicit USD
allowed the intended source-semantics controls. No producer defect claimed there.
The first TypeScript command targeted an unavailable tsc.cmd shim; the installed
`bun node_modules/typescript/bin/tsc --noEmit` completed successfully.

Artifacts: backend JSON, portal JSON and initial JSON, both independent probes,
and `PROSPECT_DATES_VALIDATION.json`. No implementation edits, dependency install,
vendor call, cloud action, policy activation, deployment or push. Existing dated
custody/performance producer paths and an actual frozen export/PDF remain due;
wrong-operation parser negatives do not prove those producer paths. Sequential
metadata/retention checks are not atomic service or IAM evidence.

Push state LOCAL. Bounded backend/date parsing evidence is accepted; Y-DT01
prevents a full paired display PASS. Runtime and all integrated criteria stay open.

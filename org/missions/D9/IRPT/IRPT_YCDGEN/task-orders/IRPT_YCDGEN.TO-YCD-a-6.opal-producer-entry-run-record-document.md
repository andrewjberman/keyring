# IRPT_YCDGEN task order -- `YCD-a-6` -- ROUND 6 (THREAD): THE OPAL PRODUCER: READ, RENDER, AND RECORD ONE OVERVIEW

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R6.md</decomp_doc>
<owned_cells>YCD-a-6</owned_cells>
</decomp_ref>
<to_id>IRPT_YCDGEN.TO-YCD-a-6.opal-producer-entry-run-record-document</to_id>
<issued_to>0.9.0_WK_IRPT_YCDGEN~1</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE thread round; no schedule, trigger or EventBridge rule is added or read
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell; the resident host's role is proved by the issuer's close run
comp-adversary: DECLARED-NOT-APPLICABLE thread round; the lens runs on the enrichment round that touches this surface
</preflight>

**Project:** IRPT_YCDGEN (D9/IRPT, fabric laptop) -- the Analysis report made in house, Opal-branded, with no YCharts call. **Round 6** builds one thread: Andrew submits a Cottonwood portfolio for an Overview and opens an Opal-made report. The first version carries no pricing (returns, risk, benchmark and risk-free print not available, reason `NOT_IN_THIS_VERSION`). No worker calls a vendor, writes the store, deploys or grants: the issuer makes every live act at close. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the round-6 decomposition)

### `YCD-a-6` -- the opal producer: read, render, and record one overview (hops 3 Read, 7 Render and record; FWD-1, FWD-6 (three clocks), FWD-9)
- `ycharts/research/opal_producer.py` (new): R3, using b-6's merged `layout_overview` and s-6's merged v2 schema. The producer calls the layout's `build` with `pricing=False` (b-6 added the parameter; its default stays True) so every price-based element prints NOT_AVAILABLE with `NOT_IN_THIS_VERSION`, and it passes the classifier it is given (b-6's `read_classifications` takes one).
- `ycharts/research/tests/test_opal_producer.py` (new) with fixtures under `ycharts/research/tests/fixtures/opal_producer/` (structure only, invented values).
- The AnalysisReport v2 document is written where `ops/owned_report.py` `OwnedAnalysisReader` reads a report (read that class to find the store and key; do not edit it).

## 2. THE CONTRACTS YOU BUILD AGAINST (inlined from the decomposition and IRPT_BCKEND PRD v0.28)

**R3 The Opal producer.** One new module `ycharts/research/opal_producer.py`: `produce(request_ref, firm, stores) -> run_record`. It reads the accepted holdings with the reader `runner.read_holdings` already implements (import it, never copy it), builds and renders the Overview through `layout_overview.py`, and writes (a) the report artifact, (b) `run.json` v2 and (c) the `AnalysisReport` v2 document. `run.json` holds the request; each input read with its as-of date; one entry per element with `method`, `inputs`, `coverage`, `status`, `reason`; and stage clocks `reading`, `computing`, `rendering` in seconds. Stores are injected, never opened inside `produce`. Nothing is fetched from outside Opal during a run. The addresses are the builder's output for C-STORE's two registered families: `address('irpt','cottonwood','state','ycharts_runs','request=<REQ>',object='run.json')` and `address('irpt','cottonwood','state','ycharts_opal_reports','request=<REQ>',object='overview.pdf')` (`lib/opal_naming.py`); no address is typed by hand.

**R2 No pricing in this version (PRD C-V1).** Return, risk-statistic, benchmark and risk-free elements print NOT_AVAILABLE with reason `NOT_IN_THIS_VERSION`, value null. No price history is read. Holding weights are the accepted dollar amounts renormalized over the holdings that carry an amount; the method says so. Two states only: a value, or NOT_AVAILABLE with a reason from the closed set `COVERAGE_BELOW_0.95`, `STALE_INPUT`, `INPUT_MISSING:<name>`, `NOT_IN_THIS_VERSION`. An aggregate prints only when the holdings with an answer are at least 0.95 of the portfolio by weight.

**R4 The v2 form of AnalysisReport** (IRPT_BCKEND PRD v0.28 item 29, `org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md` section ADDENDUM v0.28). One contract with a `provider` member: `YCHARTS` carries exactly the v1 members. `OPAL_ENGINE` carries `request_ref`, `disclosures` and `release` as v1 and, in place of the vendor members: `opal_artifact` (`sha256`, `byte_length`, `generated_at`, `run_record_key`); `effective_inputs` with `holdings_fingerprint`, `settings`, `inputs_as_of` and no `read_back`; sections with `section_id`, `section_type`, `units`, `as_of_date`, `status` (`VALUE` or `NOT_AVAILABLE`), `reason`, `method`, `coverage`, `page` optional; `computation_validation` (`status`, `checks_run`, `checks_failed`, `notes`). Under `OPAL_ENGINE` the vendor members (`vendor_artifact`, `read_back`, `extraction_validation`) are ABSENT, never null and never defaulted; a consumer that needs one rejects the document. `NOT_AVAILABLE` carries a null value and a `reason` from the closed set in R2. v1 and its schema `_contracts/AnalysisReport.schema.json` (pinned @62301f71e0) are untouched.

## 3. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD at the issuance commit)

- Read first: `runner.py` `read_holdings` (443) and `research_s3` (479) for the reader and the store shapes; `ycharts/generate/frozen_worker.py` `FrozenCompositionWorker.prepare` (32); `lib/opal_naming.py` `address()`; `_contracts/AnalysisReport.v2.schema.json` (merged from s-6); `ops/owned_report.py` for where a report is read.
- b-6 (merged) added to `layout_overview.py`: `read_classifications` (one `ETFClassifier.get_classification` per ticker), computed methods `HOLDINGS_CLASSIFIED`, `ALLOCATION_ASSET_CLASS`, `ALLOCATION_SUB_ASSET_CLASS`, and `pricing=False` / `--no-pricing`. Those three methods are not in `deliverables/maps/overview_map.json`: the producer reads the layout's own element list for them, never the map.
- s-6 (merged) fixed `AnalysisReport.v2.schema.json` readings the contract left open: `inputs_as_of` is an object of input name to date; `coverage` a number 0 to 1 or null; `as_of_date` null only under NOT_AVAILABLE; `reason` absent or null under VALUE.
- Clocks are wall seconds measured around the three stages; no time target is typed.
- If `ycharts/generate/publisher.py` or `publication_worker.py` would reject an OPAL_ENGINE document, that is another lane's file: file a surprise row naming the line; do not edit it.
- Module home and test layout: tests sit beside the code, no `conftest.py`, paths inserted at the top of each test file (as `ycharts/session/tests/test_resident_session.py:9`). Python tests run with `python -m pytest <file> -q -p no:cacheprovider` from your worktree root. Encoding: ASCII only in code and logs; no client figure and no secret in any committed file (C-FIRM, C-SECRET).

## 4. SURFACES AND BOUNDS

You READ (never edit): everything outside your `<paths>`, including `lib/`, `infra/logic/`, `docs/`, `org/missions/D9/IRPT/IRPT_YCDGEN/` (the PRD, the decompositions). NEVER: a vendor call (YCharts, Yahoo, Bloomberg or any other), an S3 or DynamoDB write, a live AWS call of any kind, a deploy, a Terraform command, a cookie, token or session value in any file, a figure value from a client file in any committed file, and none of another cell's files. A check you cannot satisfy inside your `<paths>` is a surprise row appended to `org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md` (one `## <ROW-ID> -- <title>` section with a fenced json row; ids `IRPT_YCDGEN-W1-S<k>`, next unused k; `surfaced_at` the real UTC time), never an edit outside them.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/opal_producer.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_producer.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/fixtures/opal_producer/
org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 5. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- produce reads the accepted holdings through runner.read_holdings's reader, not a copy (tests -k reads_accepted_holdings, >= 1 passed)
- **AC2** -- run.json carries the three clocks reading, computing and rendering as numbers (tests -k run_json_three_clocks, >= 1 passed)
- **AC3** -- every run.json element entry carries method, inputs, coverage, status and reason (tests -k run_json_element_trace, >= 1 passed)
- **AC4** -- the written AnalysisReport document validates against the v2 schema (tests -k document_validates_v2, >= 1 passed)
- **AC5** -- a run opens no connection and builds no client of its own (tests -k no_outside_call, >= 1 passed)
- **AC6** -- the whole test file passes (tests, all, no failure)
- **AC7** -- the producer builds with pricing off, so every price-based element reads NOT_IN_THIS_VERSION (tests -k builds_with_pricing_off, >= 1 passed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="YCD-a-6"><invocation>python -m pytest infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_producer.py -q -p no:cacheprovider -k reads_accepted_holdings</invocation><expect>^[1-9][0-9]* passed</expect></criterion>
  <criterion id="AC2" cell_refs="YCD-a-6"><invocation>python -m pytest infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_producer.py -q -p no:cacheprovider -k run_json_three_clocks</invocation><expect>^[1-9][0-9]* passed</expect></criterion>
  <criterion id="AC3" cell_refs="YCD-a-6"><invocation>python -m pytest infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_producer.py -q -p no:cacheprovider -k run_json_element_trace</invocation><expect>^[1-9][0-9]* passed</expect></criterion>
  <criterion id="AC4" cell_refs="YCD-a-6"><invocation>python -m pytest infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_producer.py -q -p no:cacheprovider -k document_validates_v2</invocation><expect>^[1-9][0-9]* passed</expect></criterion>
  <criterion id="AC5" cell_refs="YCD-a-6"><invocation>python -m pytest infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_producer.py -q -p no:cacheprovider -k no_outside_call</invocation><expect>^[1-9][0-9]* passed</expect></criterion>
  <criterion id="AC7" cell_refs="YCD-a-6"><invocation>python -m pytest infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_producer.py -q -p no:cacheprovider -k builds_with_pricing_off</invocation><expect>^[1-9][0-9]* passed</expect></criterion>
  <criterion id="AC6" cell_refs="YCD-a-6"><invocation>python -m pytest infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_producer.py -q -p no:cacheprovider</invocation><expect>^[0-9]+ passed</expect></criterion>
</proof_of_spec>

## 6. WHEN YOU ARE DONE

Write the instance at `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~1/IRPT_YCDGEN.TO-YCD-a-6.opal-producer-entry-run-record-document.proof_of_spec.json` with `to_id` `IRPT_YCDGEN.TO-YCD-a-6.opal-producer-entry-run-record-document`. Report once: each mechanical criterion's verdict line with the output above it; files written; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~Y):** round 6 cut from PRD v0.5 @e6a801f7f0 section 2 (the thread) and IRPT_BCKEND PRD v0.28 @3a8950aa20 items 29-31; CTO ruling msg 105387 (all cells in one issuance); decomposition round 6 revision 1.0 (`IRPT_YCDGEN_DECOMP_R6.md`). Chain `~1`, second order; starts after b-6 and s-6 are merged. The comp-iam question (the resident host role reads `etf-classifications` and writes the two addresses) is the issuer's close act, not this cell's. Risk WORLD: the gate's floor for infra paths and portal product files; nothing live moves inside the cell.

**DRAIN (2.0.0_SA_COO~Y, 2026-10-05 ~22:1xZ):** worker 0.9.0_WK_IRPT_YCDGEN~1 @6ce099aee3, merged 7e31aaa7b1; a-6.AC1-AC7 PASS on the merged tree (AC6: 12 passed; the whole research test folder 153 passed at the worker). Rows: W1-S6 ARMED -> DISARMED by cell YCD-g-6 (addendum A, CTO msg 105423); W1-S7 ARMED -> DISARMED by YCD-c-6 (it owns owned_report.py and its AC1-AC4 cover the sections and pdf reads); W1-S8 (pricing off still prints YCharts wording on 87 vendor-sourced or builder-only elements and a 'Data: YCharts' footer; run.json and the document are right, the printed page is not) is NOT accepted: it breaks PRD C-BRAND on the page Andrew opens, so it is cut as cell YCD-h-6; W1-S9 and W1-S10 INERT, accepted (the producer builds the three classified elements itself; reasons map into the closed set through closed_reason; as_of is the read date with as_of_basis READ_DATE, so STALE_INPUT cannot fire from this producer).

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>6</round>
<slot>~1</slot>
<fabric>laptop</fabric>

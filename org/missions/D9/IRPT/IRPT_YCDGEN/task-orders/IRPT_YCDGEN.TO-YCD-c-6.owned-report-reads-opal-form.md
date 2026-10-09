# IRPT_YCDGEN task order -- `YCD-c-6` -- ROUND 6 (THREAD): THE SERVER'S READ OF THE OPAL FORM OF ANALYSISREPORT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R6.md</decomp_doc>
<owned_cells>YCD-c-6</owned_cells>
</decomp_ref>
<to_id>IRPT_YCDGEN.TO-YCD-c-6.owned-report-reads-opal-form</to_id>
<issued_to>0.9.0_WK_IRPT_YCDGEN~2</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE thread round; no schedule, trigger or EventBridge rule is added or read
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell; the resident host's role is proved by the issuer's close run
comp-adversary: DECLARED-NOT-APPLICABLE thread round; the lens runs on the enrichment round that touches this surface
</preflight>

**Project:** IRPT_YCDGEN (D9/IRPT, fabric laptop) -- the Analysis report made in house, Opal-branded, with no YCharts call. **Round 6** builds one thread: Andrew submits a Cottonwood portfolio for an Overview and opens an Opal-made report. The first version carries no pricing (returns, risk, benchmark and risk-free print not available, reason `NOT_IN_THIS_VERSION`). No worker calls a vendor, writes the store, deploys or grants: the issuer makes every live act at close. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the round-6 decomposition)

### `YCD-c-6` -- the server's read of the opal form of analysisreport (hops 8 Open (server); FWD-1)
- `ops/owned_report.py`: `OwnedAnalysisReader.sections` and `pdf` accept a `provider: OPAL_ENGINE` document (R4) and keep rejecting a v1 document that lacks its vendor members. For an OPAL_ENGINE document `sections` returns `provider`, `request_ref`, `sections` and `computation_validation` (never `extraction_validation`); `pdf` reads `opal_artifact.sha256` and `byte_length`.
- Tests added to `ops/tests/test_owned_report.py` (keep every existing test passing).

## 2. THE CONTRACTS YOU BUILD AGAINST (inlined from the decomposition and IRPT_BCKEND PRD v0.28)

**R4 The v2 form of AnalysisReport** (IRPT_BCKEND PRD v0.28 item 29, `org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md` section ADDENDUM v0.28). One contract with a `provider` member: `YCHARTS` carries exactly the v1 members. `OPAL_ENGINE` carries `request_ref`, `disclosures` and `release` as v1 and, in place of the vendor members: `opal_artifact` (`sha256`, `byte_length`, `generated_at`, `run_record_key`); `effective_inputs` with `holdings_fingerprint`, `settings`, `inputs_as_of` and no `read_back`; sections with `section_id`, `section_type`, `units`, `as_of_date`, `status` (`VALUE` or `NOT_AVAILABLE`), `reason`, `method`, `coverage`, `page` optional; `computation_validation` (`status`, `checks_run`, `checks_failed`, `notes`). Under `OPAL_ENGINE` the vendor members (`vendor_artifact`, `read_back`, `extraction_validation`) are ABSENT, never null and never defaulted; a consumer that needs one rejects the document. `NOT_AVAILABLE` carries a null value and a `reason` from the closed set in R2. v1 and its schema `_contracts/AnalysisReport.schema.json` (pinned @62301f71e0) are untouched.

## 3. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD at the issuance commit)

- Read first: `ops/owned_report.py` (`sections` 46, `read`, `pdf` 117-140), `ops/tests/test_owned_report.py`, `ops/entry.py` (the `analysis-report` and `status-job` operations, read only), and the merged v2 schema and fixtures from s-6 and a-6's document shape.
- A consumer that needs a vendor member on an OPAL_ENGINE document rejects it; an absent member is never read as a pass.
- Module home and test layout: tests sit beside the code, no `conftest.py`, paths inserted at the top of each test file (as `ycharts/session/tests/test_resident_session.py:9`). Python tests run with `python -m pytest <file> -q -p no:cacheprovider` from your worktree root. Encoding: ASCII only in code and logs; no client figure and no secret in any committed file (C-FIRM, C-SECRET).

## 4. SURFACES AND BOUNDS

You READ (never edit): everything outside your `<paths>`, including `lib/`, `infra/logic/`, `docs/`, `org/missions/D9/IRPT/IRPT_YCDGEN/` (the PRD, the decompositions). NEVER: a vendor call (YCharts, Yahoo, Bloomberg or any other), an S3 or DynamoDB write, a live AWS call of any kind, a deploy, a Terraform command, a cookie, token or session value in any file, a figure value from a client file in any committed file, and none of another cell's files. A check you cannot satisfy inside your `<paths>` is a surprise row appended to `org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md` (one `## <ROW-ID> -- <title>` section with a fenced json row; ids `IRPT_YCDGEN-W2-S<k>`, next unused k; `surfaced_at` the real UTC time), never an edit outside them.

<paths>
infra/aws/lambda/investor-reporting/ops/owned_report.py
infra/aws/lambda/investor-reporting/ops/tests/test_owned_report.py
org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 5. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- sections returns an OPAL_ENGINE document's provider, sections and computation_validation (tests -k opal_engine_sections, >= 1 passed)
- **AC2** -- a v1 document without vendor_artifact is still refused (tests -k v1_requires_vendor_artifact, >= 1 passed)
- **AC3** -- an OPAL_ENGINE document without computation_validation is refused (tests -k opal_absent_computation_validation_refused, >= 1 passed)
- **AC4** -- pdf takes an OPAL_ENGINE document's hash from opal_artifact (tests -k opal_pdf_uses_opal_artifact, >= 1 passed)
- **AC5** -- the whole test file passes (tests, all, no failure)

<proof_of_spec>
  <criterion id="AC1" cell_refs="YCD-c-6"><invocation>python -m pytest infra/aws/lambda/investor-reporting/ops/tests/test_owned_report.py -q -p no:cacheprovider -k opal_engine_sections</invocation><expect>^[1-9][0-9]* passed</expect></criterion>
  <criterion id="AC2" cell_refs="YCD-c-6"><invocation>python -m pytest infra/aws/lambda/investor-reporting/ops/tests/test_owned_report.py -q -p no:cacheprovider -k v1_requires_vendor_artifact</invocation><expect>^[1-9][0-9]* passed</expect></criterion>
  <criterion id="AC3" cell_refs="YCD-c-6"><invocation>python -m pytest infra/aws/lambda/investor-reporting/ops/tests/test_owned_report.py -q -p no:cacheprovider -k opal_absent_computation_validation_refused</invocation><expect>^[1-9][0-9]* passed</expect></criterion>
  <criterion id="AC4" cell_refs="YCD-c-6"><invocation>python -m pytest infra/aws/lambda/investor-reporting/ops/tests/test_owned_report.py -q -p no:cacheprovider -k opal_pdf_uses_opal_artifact</invocation><expect>^[1-9][0-9]* passed</expect></criterion>
  <criterion id="AC5" cell_refs="YCD-c-6"><invocation>python -m pytest infra/aws/lambda/investor-reporting/ops/tests/test_owned_report.py -q -p no:cacheprovider</invocation><expect>^[0-9]+ passed</expect></criterion>
</proof_of_spec>

## 6. WHEN YOU ARE DONE

Write the instance at `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~2/IRPT_YCDGEN.TO-YCD-c-6.owned-report-reads-opal-form.proof_of_spec.json` with `to_id` `IRPT_YCDGEN.TO-YCD-c-6.owned-report-reads-opal-form`. Report once: each mechanical criterion's verdict line with the output above it; files written; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~Y):** round 6 cut from PRD v0.5 @e6a801f7f0 section 2 (the thread) and IRPT_BCKEND PRD v0.28 @3a8950aa20 items 29-31; CTO ruling msg 105387 (all cells in one issuance); decomposition round 6 revision 1.0 (`IRPT_YCDGEN_DECOMP_R6.md`). Chain `~2`, second order; starts after a-6 is merged. Risk WORLD: the gate's floor for infra paths and portal product files; nothing live moves inside the cell.

**DRAIN (2.0.0_SA_COO~Y, 2026-10-05 ~22:5xZ):** worker 0.9.0_WK_IRPT_YCDGEN~2 @944eb9c57e, merged e30b93afa8; c-6.AC1-AC5 PASS on the merged tree (AC5: 32 passed, 23 existing plus 9 new), instance VALID. Row W1-S7 DISARMED by this cell. Row W2-S13 (the published analysis-report RESPONSE schema, `docs/contracts/investor-reporting/v1/responses/analysis-report.response.schema.json`, requires `extraction_validation` and forbids other members, so the OPAL_ENGINE sections answer is outside it) is INERT at runtime: `ops/` imports no jsonschema at runtime (`ops/status.py:189-192`), and the response schema is checked only by `ops/tests/test_owned_report.py:165-175` against the v1 projection. The contract needs a v2 sibling response schema: owner 1.0.0_SA_CTO (IRPT_BCKEND CONTRACTS), carried to the drain-end read; it does not block FWD-1. Worker's added refusal codes ANALYSIS_REPORT_OPAL_FORM, ANALYSIS_REPORT_PROVIDER and ANALYSIS_REPORT_VENDOR_MEMBER_ABSENT ACCEPTED (a v1 document without extraction_validation now refuses with a code where it raised KeyError).

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>6</round>
<slot>~2</slot>
<fabric>laptop</fabric>

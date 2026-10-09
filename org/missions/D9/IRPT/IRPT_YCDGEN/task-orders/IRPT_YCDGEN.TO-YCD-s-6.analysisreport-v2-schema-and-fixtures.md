# IRPT_YCDGEN task order -- `YCD-s-6` -- ROUND 6 (THREAD): THE v2 FORM OF ANALYSISREPORT: SCHEMA FILE AND PRODUCER FIXTURES

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R6.md</decomp_doc>
<owned_cells>YCD-s-6</owned_cells>
</decomp_ref>
<to_id>IRPT_YCDGEN.TO-YCD-s-6.analysisreport-v2-schema-and-fixtures</to_id>
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

### `YCD-s-6` -- the v2 form of analysisreport: schema file and producer fixtures (hops 8 Open (contract); FWD-1, FWD-9)
- `_contracts/AnalysisReport.v2.schema.json` (new): contract R4 as one JSON Schema with a `provider` discriminator, `additionalProperties` false at every level, in the generated style of `_contracts/AnalysisReport.schema.json` (read its header and mirror it).
- Fixtures (new, under `_contracts/fixtures/`): `AnalysisReport.v2.opal.valid.json`, `AnalysisReport.v2.opal.invalid_vendor_member.json` (an OPAL_ENGINE document carrying `vendor_artifact`), `AnalysisReport.v2.opal.invalid_not_available_no_reason.json`, `AnalysisReport.v2.ycharts.valid.json` (the v1 valid fixture plus `provider`).
- `_contracts/tests/test_analysisreport_v2.py` (new): the tests the criteria name.
- Fixtures hold structure only: invented values, no client figure.

## 2. THE CONTRACTS YOU BUILD AGAINST (inlined from the decomposition and IRPT_BCKEND PRD v0.28)

**R4 The v2 form of AnalysisReport** (IRPT_BCKEND PRD v0.28 item 29, `org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md` section ADDENDUM v0.28). One contract with a `provider` member: `YCHARTS` carries exactly the v1 members. `OPAL_ENGINE` carries `request_ref`, `disclosures` and `release` as v1 and, in place of the vendor members: `opal_artifact` (`sha256`, `byte_length`, `generated_at`, `run_record_key`); `effective_inputs` with `holdings_fingerprint`, `settings`, `inputs_as_of` and no `read_back`; sections with `section_id`, `section_type`, `units`, `as_of_date`, `status` (`VALUE` or `NOT_AVAILABLE`), `reason`, `method`, `coverage`, `page` optional; `computation_validation` (`status`, `checks_run`, `checks_failed`, `notes`). Under `OPAL_ENGINE` the vendor members (`vendor_artifact`, `read_back`, `extraction_validation`) are ABSENT, never null and never defaulted; a consumer that needs one rejects the document. `NOT_AVAILABLE` carries a null value and a `reason` from the closed set in R2. v1 and its schema `_contracts/AnalysisReport.schema.json` (pinned @62301f71e0) are untouched.

## 3. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD at the issuance commit)

- Read first: `_contracts/AnalysisReport.schema.json` (366 lines, v1), `_contracts/fixtures/AnalysisReport.valid.json`, how `_contracts/test_owned_outer_contracts.py` loads and validates a schema (use the same validator library).
- The v1 schema is pinned @62301f71e0 and must stay byte-identical.
- IRPT_BCKEND PRD v0.28 item 29 is the source of record; this order inlines it as R4.
- Module home and test layout: tests sit beside the code, no `conftest.py`, paths inserted at the top of each test file (as `ycharts/session/tests/test_resident_session.py:9`). Python tests run with `python -m pytest <file> -q -p no:cacheprovider` from your worktree root. Encoding: ASCII only in code and logs; no client figure and no secret in any committed file (C-FIRM, C-SECRET).

## 4. SURFACES AND BOUNDS

You READ (never edit): everything outside your `<paths>`, including `lib/`, `infra/logic/`, `docs/`, `org/missions/D9/IRPT/IRPT_YCDGEN/` (the PRD, the decompositions). NEVER: a vendor call (YCharts, Yahoo, Bloomberg or any other), an S3 or DynamoDB write, a live AWS call of any kind, a deploy, a Terraform command, a cookie, token or session value in any file, a figure value from a client file in any committed file, and none of another cell's files. A check you cannot satisfy inside your `<paths>` is a surprise row appended to `org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md` (one `## <ROW-ID> -- <title>` section with a fenced json row; ids `IRPT_YCDGEN-W2-S<k>`, next unused k; `surfaced_at` the real UTC time), never an edit outside them.

<paths>
infra/aws/lambda/investor-reporting/_contracts/AnalysisReport.v2.schema.json
infra/aws/lambda/investor-reporting/_contracts/fixtures/AnalysisReport.v2.opal.valid.json
infra/aws/lambda/investor-reporting/_contracts/fixtures/AnalysisReport.v2.opal.invalid_vendor_member.json
infra/aws/lambda/investor-reporting/_contracts/fixtures/AnalysisReport.v2.opal.invalid_not_available_no_reason.json
infra/aws/lambda/investor-reporting/_contracts/fixtures/AnalysisReport.v2.ycharts.valid.json
infra/aws/lambda/investor-reporting/_contracts/tests/test_analysisreport_v2.py
org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 5. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- the valid OPAL_ENGINE fixture validates against the v2 schema (tests -k opal_valid, >= 1 passed)
- **AC2** -- an OPAL_ENGINE document carrying a vendor member is refused (tests -k opal_vendor_member_refused, >= 1 passed)
- **AC3** -- a NOT_AVAILABLE section with no reason is refused (tests -k not_available_needs_reason, >= 1 passed)
- **AC4** -- the YCHARTS branch accepts the v1 valid fixture with a provider member added (tests -k ycharts_branch_is_v1, >= 1 passed)
- **AC5** -- the v1 schema file is byte-identical to its pin @62301f71e0 (tests -k v1_untouched, >= 1 passed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="YCD-s-6"><invocation>python -m pytest infra/aws/lambda/investor-reporting/_contracts/tests/test_analysisreport_v2.py -q -p no:cacheprovider -k opal_valid</invocation><expect>^[1-9][0-9]* passed</expect></criterion>
  <criterion id="AC2" cell_refs="YCD-s-6"><invocation>python -m pytest infra/aws/lambda/investor-reporting/_contracts/tests/test_analysisreport_v2.py -q -p no:cacheprovider -k opal_vendor_member_refused</invocation><expect>^[1-9][0-9]* passed</expect></criterion>
  <criterion id="AC3" cell_refs="YCD-s-6"><invocation>python -m pytest infra/aws/lambda/investor-reporting/_contracts/tests/test_analysisreport_v2.py -q -p no:cacheprovider -k not_available_needs_reason</invocation><expect>^[1-9][0-9]* passed</expect></criterion>
  <criterion id="AC4" cell_refs="YCD-s-6"><invocation>python -m pytest infra/aws/lambda/investor-reporting/_contracts/tests/test_analysisreport_v2.py -q -p no:cacheprovider -k ycharts_branch_is_v1</invocation><expect>^[1-9][0-9]* passed</expect></criterion>
  <criterion id="AC5" cell_refs="YCD-s-6"><invocation>python -m pytest infra/aws/lambda/investor-reporting/_contracts/tests/test_analysisreport_v2.py -q -p no:cacheprovider -k v1_untouched</invocation><expect>^[1-9][0-9]* passed</expect></criterion>
</proof_of_spec>

## 6. WHEN YOU ARE DONE

Write the instance at `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~2/IRPT_YCDGEN.TO-YCD-s-6.analysisreport-v2-schema-and-fixtures.proof_of_spec.json` with `to_id` `IRPT_YCDGEN.TO-YCD-s-6.analysisreport-v2-schema-and-fixtures`. Report once: each mechanical criterion's verdict line with the output above it; files written; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~Y):** round 6 cut from PRD v0.5 @e6a801f7f0 section 2 (the thread) and IRPT_BCKEND PRD v0.28 @3a8950aa20 items 29-31; CTO ruling msg 105387 (all cells in one issuance); decomposition round 6 revision 1.0 (`IRPT_YCDGEN_DECOMP_R6.md`). Chain `~2`, first order; no dependency. Fixtures and schema only: nothing served moves. Risk WORLD: the gate's floor for infra paths and portal product files; nothing live moves inside the cell.

**DRAIN (2.0.0_SA_COO~Y, 2026-10-05 ~21:3xZ):** worker 0.9.0_WK_IRPT_YCDGEN~2 @a9bb757ee3, merged 24bbe559eb; s-6.AC1-AC5 PASS (5 of 5) on the merged tree, instance VALID. Rows W2-S11 (the v1 pin is a PRD pin; the check uses the file's sha256 and the published copy) and W2-S12 (R4 left member types open: inputs_as_of an object of input name to date; coverage a number 0-1 or null; as_of_date null only under NOT_AVAILABLE; reason absent or null under VALUE) are ACCEPTED as issuer readings for a-6, c-6 and e-6.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>6</round>
<slot>~2</slot>
<fabric>laptop</fabric>

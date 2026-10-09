# IRPT_YCDGEN task order -- `YCD-g-6` -- ROUND 6 (THREAD): THE PERSIST HOP FOR THE OPAL FORM: PUBLISHER, PUBLICATION WORKER, RESIDENT VALIDATOR

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R6A.md</decomp_doc>
<owned_cells>YCD-g-6</owned_cells>
</decomp_ref>
<to_id>IRPT_YCDGEN.TO-YCD-g-6.persist-path-for-opal-form</to_id>
<issued_to>0.9.0_WK_IRPT_YCDGEN~3</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE thread round; no schedule, trigger or EventBridge rule is added or read
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell; the resident host's role is proved by the issuer's close run
comp-adversary: DECLARED-NOT-APPLICABLE thread round; the lens runs on the enrichment round that touches this surface
</preflight>

**Project:** IRPT_YCDGEN (D9/IRPT, fabric laptop) -- the Analysis report made in house, Opal-branded, with no YCharts call. **Round 6** builds one thread: Andrew submits a Cottonwood portfolio for an Overview and opens an Opal-made report. The first version carries no pricing (returns, risk, benchmark and risk-free print not available, reason `NOT_IN_THIS_VERSION`). No worker calls a vendor, writes the store, deploys or grants: the issuer makes every live act at close. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the round-6 decomposition)

### `YCD-g-6` -- the persist hop for the opal form: publisher, publication worker, resident validator (hops 7-8 Persist; FWD-1)
- `reports/resident_installed.py` (`REPORT_SCHEMAS`, 47; the validators built at 115-125), `ycharts/generate/publisher.py` (the metadata key check at 107) and `ycharts/generate/publication_worker.py` (47): R7.
- Tests added to `reports/tests/test_resident_installed.py`, `ycharts/generate/tests/test_publisher.py` and `ycharts/generate/tests/test_publication_worker.py`; keep every existing test in them passing.

## 2. THE CONTRACTS YOU BUILD AGAINST (inlined from the decomposition and IRPT_BCKEND PRD v0.28)

**R7 Persist the Opal form.** A document with `provider: OPAL_ENGINE` is persisted and its job reaches READY through a path that accepts the Opal metadata key set `{request_ref, opal_artifact, effective_inputs, release}` (and the `sections` and `computation_validation` the v2 schema carries) and an artifact reference of its own family (name the family in a surprise row; it is not `ORIGINAL_VENDOR_PDF`). The resident validator validates an OPAL_ENGINE document against `_contracts/AnalysisReport.v2.schema.json` and a YCHARTS document against the v1 members, and refuses an OPAL_ENGINE document that carries a vendor member. The YCharts path is unchanged for every existing test. No code path accepts both key sets on one request.

**R4 The v2 form of AnalysisReport** (IRPT_BCKEND PRD v0.28 item 29, `org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md` section ADDENDUM v0.28). One contract with a `provider` member: `YCHARTS` carries exactly the v1 members. `OPAL_ENGINE` carries `request_ref`, `disclosures` and `release` as v1 and, in place of the vendor members: `opal_artifact` (`sha256`, `byte_length`, `generated_at`, `run_record_key`); `effective_inputs` with `holdings_fingerprint`, `settings`, `inputs_as_of` and no `read_back`; sections with `section_id`, `section_type`, `units`, `as_of_date`, `status` (`VALUE` or `NOT_AVAILABLE`), `reason`, `method`, `coverage`, `page` optional; `computation_validation` (`status`, `checks_run`, `checks_failed`, `notes`). Under `OPAL_ENGINE` the vendor members (`vendor_artifact`, `read_back`, `extraction_validation`) are ABSENT, never null and never defaulted; a consumer that needs one rejects the document. `NOT_AVAILABLE` carries a null value and a `reason` from the closed set in R2. v1 and its schema `_contracts/AnalysisReport.schema.json` (pinned @62301f71e0) are untouched.

## 3. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD at the issuance commit)

- Code lives under `infra/aws/lambda/investor-reporting/`. Read first: the three source files at the lines named above, `ycharts/research/opal_producer.py` (merged from a-6: it writes the artifact, `run.json` and the AnalysisReport v2 document through injected stores), `_contracts/AnalysisReport.v2.schema.json` (merged from s-6), and the worker rows IRPT_YCDGEN-W1-S6 and W1-S9 in `org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md`.
- The job reaches READY through the existing job store's state machine (`ycharts/generate/job.py` and `durable_job.py` are read only here); the Opal path reaches READY without the vendor download states `DOWNLOADING`, `EXTRACTING` and `CERTIFYING`, or through a state sequence you name in a surprise row if the machine forces one.
- The generate tests may need `ycharts/generate/tests/netguard.py` and `authz_fixtures.py` (read only); run them as their own headers say.
- Module home and test layout: tests sit beside the code, no `conftest.py`, paths inserted at the top of each test file (as `ycharts/session/tests/test_resident_session.py:9`). Python tests run with `python -m pytest <file> -q -p no:cacheprovider` from your worktree root. Encoding: ASCII only in code and logs; no client figure and no secret in any committed file (C-FIRM, C-SECRET).

## 4. SURFACES AND BOUNDS

You READ (never edit): everything outside your `<paths>`, including `lib/`, `infra/logic/`, `docs/`, `org/missions/D9/IRPT/IRPT_YCDGEN/` (the PRD, the decompositions). NEVER: a vendor call (YCharts, Yahoo, Bloomberg or any other), an S3 or DynamoDB write, a live AWS call of any kind, a deploy, a Terraform command, a cookie, token or session value in any file, a figure value from a client file in any committed file, and none of another cell's files. A check you cannot satisfy inside your `<paths>` is a surprise row appended to `org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md` (one `## <ROW-ID> -- <title>` section with a fenced json row; ids `IRPT_YCDGEN-W3-S<k>`, next unused k; `surfaced_at` the real UTC time), never an edit outside them.

<paths>
infra/aws/lambda/investor-reporting/reports/resident_installed.py
infra/aws/lambda/investor-reporting/reports/tests/test_resident_installed.py
infra/aws/lambda/investor-reporting/ycharts/generate/publisher.py
infra/aws/lambda/investor-reporting/ycharts/generate/publication_worker.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_publisher.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_publication_worker.py
org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 5. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- an OPAL_ENGINE document with its artifact is persisted and its job reaches READY (tests -k opal_engine_publication_ready, >= 1 passed)
- **AC2** -- the YCharts metadata path still requires its vendor_artifact (tests -k v1_publication_unchanged, >= 1 passed)
- **AC3** -- the publication worker refuses a document that mixes the Opal and vendor key sets (tests -k mixed_key_sets_refused, >= 1 passed)
- **AC4** -- the resident validator accepts an OPAL_ENGINE document and refuses one carrying a vendor member (tests -k resident_validator_v2, >= 1 passed)
- **AC5** -- the whole publisher test file passes (tests, all, no failure)
- **AC6** -- a v1 document persists byte-equal to what the unchanged publisher persisted (tests -k v1_document_persists_byte_equal, >= 1 passed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="YCD-g-6"><invocation>python -m pytest infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_publisher.py -q -p no:cacheprovider -k opal_engine_publication_ready</invocation><expect>^[1-9][0-9]* passed</expect></criterion>
  <criterion id="AC2" cell_refs="YCD-g-6"><invocation>python -m pytest infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_publisher.py -q -p no:cacheprovider -k v1_publication_unchanged</invocation><expect>^[1-9][0-9]* passed</expect></criterion>
  <criterion id="AC3" cell_refs="YCD-g-6"><invocation>python -m pytest infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_publication_worker.py -q -p no:cacheprovider -k mixed_key_sets_refused</invocation><expect>^[1-9][0-9]* passed</expect></criterion>
  <criterion id="AC4" cell_refs="YCD-g-6"><invocation>python -m pytest infra/aws/lambda/investor-reporting/reports/tests/test_resident_installed.py -q -p no:cacheprovider -k resident_validator_v2</invocation><expect>^[1-9][0-9]* passed</expect></criterion>
  <criterion id="AC6" cell_refs="YCD-g-6"><invocation>python -m pytest infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_publisher.py -q -p no:cacheprovider -k v1_document_persists_byte_equal</invocation><expect>^[1-9][0-9]* passed</expect></criterion>
  <criterion id="AC5" cell_refs="YCD-g-6"><invocation>python -m pytest infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_publisher.py -q -p no:cacheprovider</invocation><expect>^[0-9]+ passed</expect></criterion>
</proof_of_spec>

## 6. WHEN YOU ARE DONE

Write the instance at `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~3/IRPT_YCDGEN.TO-YCD-g-6.persist-path-for-opal-form.proof_of_spec.json` with `to_id` `IRPT_YCDGEN.TO-YCD-g-6.persist-path-for-opal-form`. Report once: each mechanical criterion's verdict line with the output above it; files written; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~Y):** round 6 cut from PRD v0.5 @e6a801f7f0 section 2 (the thread) and IRPT_BCKEND PRD v0.28 @3a8950aa20 items 29-31; CTO ruling msg 105387 (all cells in one issuance); decomposition round 6 revision 1.0 (`IRPT_YCDGEN_DECOMP_R6.md`). Chain `~3`, first order; addendum A cell (decomposition IRPT_YCDGEN_DECOMP_R6A.md), cut by the issuer as a second workstream (`<workstream>R6A_PERSIST_AND_PAGE</workstream>`, the gate's provision for a disjoint second set of orders in a round; the round-collision limb reads no override) to disarm worker row W1-S6 on the CTO's ruling (msg 105423, cut g-6 as proposed); depends on s-6 and a-6 (merged). AC3 runs in test_publication_worker.py and AC4 in test_resident_installed.py. Risk WORLD: the gate's floor for infra paths and portal product files; nothing live moves inside the cell.

**WRITER READ (2.0.0_SA_COO~Y, 2026-10-05 ~22:1xZ, CTO condition 1 of msg 105423):** a scan of 4,237 task-order files (both roots) for a non-terminal order whose `<paths>` names any of the six files of this cell found 6 hits, all this order (6 files x 1 order); no order of 2.0.0_SA_COO~P names any of them. Status regex is conservative (an unparsed status counts non-terminal). **CONDITION 2:** g-6 ships with d-6 through IRPT_BCKEND's release under one never-widen packet; AC2 and AC6 are the packet's evidence that the YCHARTS path is unchanged.

**DRAIN (2.0.0_SA_COO~Y, 2026-10-05 ~23:0xZ):** worker 0.9.0_WK_IRPT_YCDGEN~3 @bfed18a189, merged a9c65fa1b3 (investigations-file conflict resolved as a union); g-6.AC1-AC6 PASS on the merged tree (AC5: 23 passed), instance VALID; the YCharts path unchanged (v1 byte-equal pin passes against an unmodified HEAD publisher). Opal state sequence RECEIVED -> CERTIFYING -> READY (row W3-S10 INERT, accepted). Rows: W3-S8 ARMED and W3-S11 ARMED -> DISARMED by cell YCD-i-6 (addendum B); W3-S9 ARMED -> DISARMED by the d-6 amendment (resident_worker.py is d-6's file); W3-S12 INERT, accepted (a pre-existing test imports `extract` and needs ycharts/extract on PYTHONPATH when the file runs alone; AC4 selects only the added tests).

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>6</round>
<workstream>R6A_PERSIST_AND_PAGE</workstream>
<slot>~3</slot>
<fabric>laptop</fabric>

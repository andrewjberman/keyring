# IRPT_YCDGEN task order -- `YCD-k-6` -- ROUND 6 (THREAD): THE INSTALLER'S OPAL STORES AND THE WHOLE THREAD PROVED WITH FAKES

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R6C.md</decomp_doc>
<owned_cells>YCD-k-6</owned_cells>
</decomp_ref>
<to_id>IRPT_YCDGEN.TO-YCD-k-6.installer-wiring-and-thread-integration</to_id>
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

### `YCD-k-6` -- the installer's opal stores and the whole thread proved with fakes (hops 2-8 (join); FWD-1)
- `reports/resident_installed.py` (passes `opal_stores`; near line 269) and its test in `reports/tests/test_resident_installed.py`: R11 (1).
- `ycharts/generate/resident_worker.py` and `ycharts/generate/tests/test_resident_worker.py`: only what R11 (2) needs to hand the retained `artifact_ref` to the checkpoint.
- `ycharts/generate/tests/test_opal_thread_integration.py` (new): R11 (3).
- Keep every existing test in those files passing (`test_resident_worker.py`: 53 passed and 8 skipped at the base).

## 2. THE CONTRACTS YOU BUILD AGAINST (inlined from the decomposition and IRPT_BCKEND PRD v0.28)

**R11 The installer supplies the Opal stores; the whole path runs.** (1) `reports/resident_installed.py` passes `opal_stores` to `ResidentAssembly` (`ycharts/generate/resident_worker.py`, the optional `opal_stores(principal, record)` keyword d-6 added). The factory builds, from the installed bindings and ONLY for a principal on the allow list, the stores `opal_producer.produce` takes: the accepted-holdings reader (the one `runner.read_holdings` implements), the classifier (`ETFClassifier` over the `etf-classifications` table), the firm-store put for the run record, the reporting repository's `artifacts` (the retained PDF and the spilled document), and the clock. A principal off the list builds none of them: no client is constructed for it. (2) The `artifact_ref` `produce` returns reaches the publisher's checkpoint, so the job reaches READY with a retained PDF. (3) One test drives `ResidentAssembly.execute` for a listed principal with fake stores through select, produce, persist and READY, then reads the report back through `OwnedAnalysisReader.sections`; and the same request from an unlisted principal takes the YCharts path. Nothing live: fakes only. The allow list keeps its inert placeholder `PRINCIPAL_ID_TO_BE_SET_BY_ISSUER`; the issuer sets the real principal id at release, after this cell. Worker rows IRPT_YCDGEN-W1-S11 and W3-S15 measured the two gaps.

## 3. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD at the issuance commit)

- Code lives under `infra/aws/lambda/investor-reporting/`. Read first: worker rows IRPT_YCDGEN-W1-S11, W1-S12, W3-S9, W3-S15 and W3-S16 in `org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md`; `resident_worker.py` (`OPAL_PRODUCER_PRINCIPALS`, `producer_for`, `execute`, `run_opal`, the READY reopen); `reports/resident_installed.py` (the installer that builds `ResidentAssembly`, near 269, and its bindings: `REQUIRED`, `capture`, `census`); `ycharts/research/opal_producer.py` (`produce`, the `stores` it takes, the run record it returns); `ycharts/research/runner.py` (`read_holdings`, `research_s3`); `ycharts/generate/publisher.py` (`_publish_opal`, `retain_document`, `read_document`) and `publication_worker.py`; `ops/owned_report.py` (`OwnedAnalysisReader.sections`).
- Cell l-6 (addendum D, runs BEFORE you and is merged when you start) reworked the persist hop per the CTO's ruling: the Opal PDF is retained under policy revision `irpt-ycdgen-research-v1`, family `YCHARTS_OPAL_REPORT`, and `reports/retention.py` resolves the policy from each reference's own `policy_revision`. Wire the repository's `artifacts` store accordingly.
- Worker row IRPT_YCDGEN-W3-S17 (yours): after l-6, `resident_worker.py` lines 122 and 429 still put the Opal PDF as family `OPAL_REPORT_PDF` (no longer registered; it now lives at `YCHARTS_OPAL_REPORT` under policy revision `irpt-ycdgen-research-v1`), and four tests in `test_resident_worker.py` are RED on the base because of it: `test_allow_listed_principal_opal_producer`, `test_one_producer_per_request`, `test_one_producer_per_request_a_retained_opal_pdf_publishes_without_p...` and `test_redelivered_ready_opal_job_is_acknowledged_without_a_key_error` (53 passed, 8 skipped before l-6). Rename the family at those lines, fix the fixture that registers it, and make the installer pass the research revision: `reports/composition.py` `build_retained_repositories(additional_policy_revisions=(...))` is opt-in (l-6 added it); call it with `irpt-ycdgen-research-v1` where the installer builds the repositories. The row `irpt-ycdgen-research-v1` is PENDING_ENFORCEMENT in the live registry; a test makes it ACTIVE in a fixture registry only.
- Everything it needs is merged: the v2 schema, the persist path, the retained families, the allow-list switch. You write the join.
- `test_resident_installed.py` run alone has one pre-existing failure, `test_factory_returns_exactly_the_resident_shape_without_any_aws_call` (it imports `extract`; passes with `ycharts/extract` on PYTHONPATH). Run that file with `PYTHONPATH=infra/aws/lambda/investor-reporting/ycharts/extract` for the whole-file check; your criteria select your own tests by `-k`.
- Tests use fakes for every store and client; no live AWS call, no network (the `netguard` fixture in `ycharts/generate/tests/` is the model).
- Module home and test layout: tests sit beside the code, no `conftest.py`, paths inserted at the top of each test file (as `ycharts/session/tests/test_resident_session.py:9`). Python tests run with `python -m pytest <file> -q -p no:cacheprovider` from your worktree root. Encoding: ASCII only in code and logs; no client figure and no secret in any committed file (C-FIRM, C-SECRET).

## 4. SURFACES AND BOUNDS

You READ (never edit): everything outside your `<paths>`, including `lib/`, `infra/logic/`, `docs/`, `org/missions/D9/IRPT/IRPT_YCDGEN/` (the PRD, the decompositions). NEVER: a vendor call (YCharts, Yahoo, Bloomberg or any other), an S3 or DynamoDB write, a live AWS call of any kind, a deploy, a Terraform command, a cookie, token or session value in any file, a figure value from a client file in any committed file, and none of another cell's files. A check you cannot satisfy inside your `<paths>` is a surprise row appended to `org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md` (one `## <ROW-ID> -- <title>` section with a fenced json row; ids `IRPT_YCDGEN-W1-S<k>`, next unused k; `surfaced_at` the real UTC time), never an edit outside them.

<paths>
infra/aws/lambda/investor-reporting/reports/resident_installed.py
infra/aws/lambda/investor-reporting/reports/tests/test_resident_installed.py
infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_resident_worker.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_opal_thread_integration.py
org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 5. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- the installer passes an opal_stores factory to ResidentAssembly (tests -k installer_supplies_opal_stores, >= 1 passed)
- **AC2** -- a principal off the allow list builds none of the Opal stores or clients (tests -k unlisted_principal_builds_no_opal_stores, >= 1 passed)
- **AC3** -- a listed principal's request reaches READY with a retained PDF and its report reads back through sections (tests -k opal_thread_ready_end_to_end, >= 1 passed)
- **AC4** -- the retained artifact_ref reaches the checkpoint (tests -k opal_artifact_ref_reaches_checkpoint, >= 1 passed)
- **AC5** -- the same request from an unlisted principal takes the YCharts path (tests -k unlisted_principal_takes_ycharts_path, >= 1 passed)
- **AC6** -- the whole integration test file passes (tests, all, no failure)
- **AC7** -- the whole resident worker test file passes again, the four red tests green (tests, all, no failure)
- **AC8** -- the installer builds the repositories with the research policy revision (tests -k installer_wires_ycdgen_research_revision, >= 1 passed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="YCD-k-6"><invocation>python -m pytest infra/aws/lambda/investor-reporting/reports/tests/test_resident_installed.py -q -p no:cacheprovider -k installer_supplies_opal_stores</invocation><expect>^[1-9][0-9]* passed</expect></criterion>
  <criterion id="AC2" cell_refs="YCD-k-6"><invocation>python -m pytest infra/aws/lambda/investor-reporting/reports/tests/test_resident_installed.py -q -p no:cacheprovider -k unlisted_principal_builds_no_opal_stores</invocation><expect>^[1-9][0-9]* passed</expect></criterion>
  <criterion id="AC3" cell_refs="YCD-k-6"><invocation>python -m pytest infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_opal_thread_integration.py -q -p no:cacheprovider -k opal_thread_ready_end_to_end</invocation><expect>^[1-9][0-9]* passed</expect></criterion>
  <criterion id="AC4" cell_refs="YCD-k-6"><invocation>python -m pytest infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_opal_thread_integration.py -q -p no:cacheprovider -k opal_artifact_ref_reaches_checkpoint</invocation><expect>^[1-9][0-9]* passed</expect></criterion>
  <criterion id="AC5" cell_refs="YCD-k-6"><invocation>python -m pytest infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_opal_thread_integration.py -q -p no:cacheprovider -k unlisted_principal_takes_ycharts_path</invocation><expect>^[1-9][0-9]* passed</expect></criterion>
  <criterion id="AC7" cell_refs="YCD-k-6"><invocation>python -m pytest infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_resident_worker.py -q -p no:cacheprovider</invocation><expect>^[0-9]+ passed</expect></criterion>
  <criterion id="AC8" cell_refs="YCD-k-6"><invocation>python -m pytest infra/aws/lambda/investor-reporting/reports/tests/test_resident_installed.py -q -p no:cacheprovider -k installer_wires_ycdgen_research_revision</invocation><expect>^[1-9][0-9]* passed</expect></criterion>
  <criterion id="AC6" cell_refs="YCD-k-6"><invocation>python -m pytest infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_opal_thread_integration.py -q -p no:cacheprovider</invocation><expect>^[0-9]+ passed</expect></criterion>
</proof_of_spec>

## 6. WHEN YOU ARE DONE

Write the instance at `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~1/IRPT_YCDGEN.TO-YCD-k-6.installer-wiring-and-thread-integration.proof_of_spec.json` with `to_id` `IRPT_YCDGEN.TO-YCD-k-6.installer-wiring-and-thread-integration`. Report once: each mechanical criterion's verdict line with the output above it; files written; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~Y):** round 6 cut from PRD v0.5 @e6a801f7f0 section 2 (the thread) and IRPT_BCKEND PRD v0.28 @3a8950aa20 items 29-31; CTO ruling msg 105387 (all cells in one issuance); decomposition round 6 revision 1.0 (`IRPT_YCDGEN_DECOMP_R6.md`). Chain `~1`, the round's JOIN, after every other cell merged; addendum C cell (decomposition IRPT_YCDGEN_DECOMP_R6C.md), cut by the issuer to disarm worker rows W1-S11 and W3-S15. AC1 and AC2 run in test_resident_installed.py; AC3-AC5 and AC6 in the integration file. Release order: this cell, then the issuer sets Andrew's principal id. Risk WORLD: the gate's floor for infra paths and portal product files; nothing live moves inside the cell.

**DRAIN (2.0.0_SA_COO~Y, 2026-10-06 ~00:3xZ):** worker 0.9.0_WK_IRPT_YCDGEN~1 @2c721e21f2, merged d2b625e697; k-6.AC1-AC8 PASS on the merged tree and at the worker (AC7: 53 passed, 8 skipped, the four red d-6 tests green; AC6: 3 passed), instance VALID. Cross-cell check on the merged tree: every test directory of the touched packages passes together (ycharts/research/tests, ycharts/generate/tests, reports/tests, ops/tests, _contracts/tests, and lib/tests/test_irpt_destination.py 73 passed), no failure. The worker's negative control (the worker ignoring the returned artifact_ref) fails two of three integration tests with ATTENTION OPAL_PRODUCER_OUTPUT. Rows: W1-S11, W3-S15 and W3-S17 DISARMED by this cell; W3-S18 cured (the installer test file now puts ycharts/extract on its path and passes alone, 19 passed); W1-S14 INERT, accepted. **W1-S13 ARMED, carried to the release:** the Overview element map has no installed home; the installer reads it from a new optional pinned `opal_map` binding that no bindings file carries yet, and the default classifier opener (`layout_overview._default_classifier`) and the default firm-store opener (`runner.research_s3`) were exercised only as fakes. Disarm owner 2.0.0_SA_COO~Y: the release package carries `deliverables/maps/overview_map.json` with its sha256 in the `opal_map` binding, and the issuer's close run exercises both default openers once against the real stores.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>6</round>
<workstream>R6C_WIRING</workstream>
<slot>~1</slot>
<fabric>laptop</fabric>

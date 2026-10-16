# TO-AR-ty-51 -- FWD-5 tests: the report repository refuses another firm's report, history and artifact (AR-ty-51, round 46, workstream ~TX)

<to_id>IRPT_ANLREQ.TO-AR-ty-51</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~214</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>46</round>
<workstream>~TX</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~TX (gates and tests) | **Decomp cell:** `AR-ty-51` (`decompositions/IRPT_ANLREQ_DECOMP_R46_TX.md`) |
**outcome_ref:** FWD-5 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`AR-ty-51`: "FWD-5 tests: the report repository refuses another firm's report, history and artifact." A TEST cell: you add 1 new test file(s) and edit no other file. FWD-5 says another firm never sees the request, the package or the commentary; round 45 mapped where each read is bound to the firm and found these reads bound in code but with no test that fails when the binding is removed.

**What to test.** Rows 1, 2, 4, 5 and 8 of the report-side record `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~211/FWD5_REPORT_SIDE_BINDING_MAP.md`, all in `infra/aws/lambda/investor-reporting/reports/repository.py`: `ReportRepository.get` (line 181, the firm decider in `_allow`, reached from get at line 240), `ReportRepository.list` with a data_firm naming another firm (line 296: foreign rows are dropped, the page is empty), `ReportRepository.list` history row whose tenant differs (line 289: `ReportRefused` 'history tenant binding failed' for the whole page), `ArtifactRepository.get` as a user principal of another firm (line 386, `ReportDenied` 'artifact access denied' at line 388), `ArtifactRepository.head` with a foreign data_firm (line 487, which forwards to get).

**Files you create (and the only source-tree files you may write):**

infra/aws/lambda/investor-reporting/reports/tests/test_cross_firm_report_reads.py

**Model your tests on:** `infra/aws/lambda/investor-reporting/reports/tests/test_repository.py` (fakes keyed by tenant, lines 35 and 365 to 370) and `infra/aws/lambda/investor-reporting/reports/tests/test_interactive_storage.py`.

**How to write each test.** Open the neighbouring test file named in the row (it holds the fakes, fixtures and the way the code under test is built); copy that construction. Each test builds a caller of firm A and a stored record owned by firm B (use plain synthetic names such as `firm-a` and `firm-b`; no real client name, no secret), calls the real code under test (a fake for storage and signing only), and asserts the exact refusal the row names (the exception type and its closed code, or the status, or the empty page). Where the row says the refusal is silent (a skipped row, an empty page) assert that shape. For each test add one same-firm control test that proves the same call succeeds for the owning firm, so the refusal is shown to come from the firm and not from a broken fixture. Name EVERY test function `test_cross_firm_<what>`; the check refuses any other test name in your file. Do not edit the code under test; if a row is not as the record says, write the test for what the code does and file a surprise row.

**Run them** from your worktree root with `python -m pytest -q <your file(s)>`; every test must pass. A test that needs a package the sparse cone lacks: widen nothing, file a `BLOCKING` surprise row naming the folder (`IRPT_ANLREQ-D2-W214-S<k>`, next unused under the surprise channel) and stop on that test.

### ACCEPTANCE

<criterion id="AR51-ty-AC1" cell_refs="AR-ty-51"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_ANLREQ_T2/R46_CHECKS/r46_checks.py tests 8 infra/aws/lambda/investor-reporting/reports/tests/test_cross_firm_report_reads.py</invocation><expect>R46-TESTS-OK</expect></criterion>
`AR51-ty-AC1` -- every file exists, every test function is named `test_cross_firm_*`, the tests pass, and at least 8 tests pass. Dry-run at box/dell2 39eef25c48: `R46-TESTS-FAIL absent: ...` -- FAIL as expected. The checker's own `--self-test` (green pair plus four mutants refused) reads `R46-SELFTEST-OK`.

<expected_criteria>AR51-ty-AC1</expected_criteria>

## BOUNDS

- **Grant.** The test file(s) listed, this order's file, your deliverables folder, the surprise channel. You edit NO code under test and NO other test.
- **No network, no AWS, no secret, no deploy.** Fakes only. No real firm, client or person name; no credential, token or address.
- **Refusal clause.** If a cited line is not what the record says, write the test for what the code does and file a surprise row; if a function is not importable in the sparse cone, file the `BLOCKING` row and stop on it.
- **No alarms, monitors or notifications.** A refusal is a test.

<paths>
infra/aws/lambda/investor-reporting/reports/tests/test_cross_firm_report_reads.py
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention). Everything else named here you READ.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R46_TX.md</decomp_doc> (round 46, workstream ~TX), cell `AR-ty-51`.
<owned_cells>AR-ty-51</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion id: AR51-ty-AC1. Instance at `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~214/IRPT_ANLREQ.TO-AR-ty-51.fwd5-report-repository-cross-firm-tests.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> AR51-ty-AC1` BEFORE the flip. Commit the test file(s) first, then pin.
</proof_of_spec>

**REPORT:** the test files, the count passed, for each test the one guard line it fails without (you removed the guard in a scratch copy and the test failed, or you say you did not), the check line, commits.

---

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- new test files only; no source file, edge or consumer changes. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no permission change.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger is touched. comp-routes and comp-cache: DECLARED-NOT-APPLICABLE.
comp-adversary: RUN -- `comp-adversary compose` on this order at read-vintage c39947a0a2: the neighborhood is the decomposition only, 0 unproven dependencies; the only cited paths it flags GONE are the files this order creates (the new test file(s) or record, and the proof instance). Traps named for the worker: a test that mocks the very guard it claims to prove; a lookup that misses before the firm binding is reached, which proves nothing about the binding; a test that passes with the guard removed; a cited line that is a comment instead of the code that decides.
</preflight>

- Cut on the CTO's parallelization ruling, Move 2 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_IRPT_PARALLELIZE_WORKSTREAM_ASSIGNMENTS_20261015.md`, msg 8742): `2.0.0_SA_COO~T2` takes IRPT_ANLREQ FWD-5, "FWD-5's cross-firm tests on the paths that run today". Risk WORLD only because the gate's path floor (`<paths>` under `infra/`, spine v3.19 L6) admits no lower class: the work is new test files and no deploy, no AWS call, no source edit.
- Base: `AR51-ty-AC1` FAIL as expected (`R46-TESTS-FAIL absent`) at box/dell2 39eef25c48, run by the issuer before the cut.

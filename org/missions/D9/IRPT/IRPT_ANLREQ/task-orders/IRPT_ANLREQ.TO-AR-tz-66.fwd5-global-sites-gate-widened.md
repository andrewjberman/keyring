# TO-AR-tz-66 -- FWD-5 gate: the global-admissions gate covers every OPAL_GLOBAL equality site under infra/aws/lambda (AR-tz-66, round 51, workstream ~TX)

<to_id>IRPT_ANLREQ.TO-AR-tz-66</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~230</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>51</round>
<workstream>~TX</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~TX (gates and tests) | **Decomp cell:** `AR-tz-66` (`decompositions/IRPT_ANLREQ_DECOMP_R51_TX.md`) |
**outcome_ref:** FWD-5 | **depends_on:** none (the record is merged)

---

## WORKER FACE

### THE CELL

`AR-tz-66`: "the global-admissions gate covers every OPAL_GLOBAL equality site under infra/aws/lambda." The CTO ruled that every global (every-firm) admission is a named row of a register (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_IRPT_ANLREQ_FOUR_LANES_END_TO_END_20261015.md` ADDENDUM 7 item 4). The round-47 gate scans only two files. Round 50 classified all sites in a cited-line record, `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~229/OPAL_GLOBAL_SITES_CLASSIFIED.md` (40 rows over 21 files at HEAD; verdicts `ADMITS` 10, `REFUSES-TESTED` 1, `NOT-APPLICABLE` 29; READ it first, it is your input). The register is `org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R19_GLOBAL_ADMISSIONS_REGISTER.md` (rows G1 to G3; `2.0.0_SA_COO~V2` owns it). Write ONE new test file that makes both halves of the rule mechanical over the whole denominator.

**What to build** in `infra/aws/lambda/ticket_center/tests/test_cross_firm_global_sites_widened.py` (stdlib and pytest only; derive the repository root from the test file's own location, never a drive letter or an absolute path; name EVERY test `test_cross_firm_<what>`):

1. **A declared table in the test file**, copied from the record: one entry per FILE that holds at least one site (path relative to the repo root, the number of sites in that file, and the file's verdict: `ADMITS` when any of its sites is ADMITS, else `NOT-APPLICABLE` or `REFUSES-TESTED` as the record says). Print the denominator in every assertion message (files scanned, sites found).
2. **Completeness test (GREEN today):** scan every non-test `.py` file under `infra/aws/lambda` (exclude every `tests` folder and every `__pycache__`) for lines where `principal_class` (any of its spellings: `principal_class`, `["principal_class"]`, `.get("principal_class")`) is compared with `==` or `in` against the literal `OPAL_GLOBAL`. The set of files and the per-file site counts must EQUAL the declared table: a new site in a file, a new file, or a removed site fails with the file named and a message saying to classify it in the record and the register. (If your count at HEAD differs from the table you copied, the table you copied from the record is the claim and your scan is the instrument: report the difference in a surprise row and make the table equal what the scan finds, citing the line.)
3. **Register-coverage test, marked `@pytest.mark.xfail(strict=True, reason="S134 item 4: 8 ADMITS files are not register rows; V2 adds them")`:** every file whose declared verdict is `ADMITS` is named (by repo-relative path or file name) in at least one register row. Today 8 of the 10 ADMITS sites (6 files) are not rows, so the test fails and the `xfail` makes the suite green; the day `2.0.0_SA_COO~V2` adds the rows it XPASSES, and `strict=True` turns that into a failure that tells the next reader to delete the marker. The failing message names each unregistered file.
4. **A control and two in-memory mutants:** the same check functions applied to in-memory text: a copy of the table with one file's count lowered returns a violation for the completeness check; a copy of the register text with a row removed returns a violation for the coverage check; the unmodified inputs return none for the completeness check.

At least 4 tests must run and pass (the xfail counts as neither). Do not edit the register, the record, any code or any other test. Use plain names; no secret, no client data.

### ACCEPTANCE

<criterion id="AR66-tz-AC1" cell_refs="AR-tz-66"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_ANLREQ_T2/R46_CHECKS/r46_checks.py tests 4 infra/aws/lambda/ticket_center/tests/test_cross_firm_global_sites_widened.py</invocation><expect>R46-TESTS-OK</expect></criterion>
`AR66-tz-AC1` -- the file exists, every test function is named `test_cross_firm_*`, the tests pass (an xfail is not a pass or a failure) and at least 4 pass. Dry-run at box/dell2 9a9ecafe8c: `R46-TESTS-FAIL absent: ...` -- FAIL as expected.

<expected_criteria>AR66-tz-AC1</expected_criteria>

## BOUNDS

- **Grant.** The test file listed, this order's file, your deliverables folder, the surprise channel. No other file.
- **No network, no AWS, no secret, no deploy.**
- **Refusal clause.** If the record or the register is absent in your cone, file a `BLOCKING` row naming the folder and stop.
- **No alarms, monitors or notifications.** A gate is a test.

<paths>
infra/aws/lambda/ticket_center/tests/test_cross_firm_global_sites_widened.py
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_ANLREQ_T2/R46_CHECKS/r46_checks.py tests 4 infra/aws/lambda/ticket_center/tests/test_cross_firm_global_sites_widened.pyESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention). Everything else you READ.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R51_TX.md</decomp_doc> (round 51, workstream ~TX), cell `AR-tz-66`.
<owned_cells>AR-tz-66</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion id: AR66-tz-AC1. Instance at `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~230/IRPT_ANLREQ.TO-AR-tz-66.fwd5-global-sites-gate-widened.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> AR66-tz-AC1` BEFORE the flip. Commit the test file first, then pin.
</proof_of_spec>

**REPORT:** the test file, the count passed and xfailed, the printed denominators (files, sites), any difference between your scan and the record, the two mutants' violation text, the check line, commits.

---

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a new test file only; no source file, edge or consumer changes. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no permission change.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger is touched. comp-routes and comp-cache: DECLARED-NOT-APPLICABLE.
comp-adversary: RUN -- `comp-adversary compose` on this order at read-vintage HEAD: the neighborhood is the decomposition only, 0 unproven dependencies. Traps named for the worker: a scan that stops at the two files the round-47 gate named; a table copied from the record that your own scan contradicts, silently adjusted; an xfail without strict=True, which would hide the day the rows arrive; a hard-coded drive letter or absolute path.
</preflight>

- Step 2 of disarming the issuer-owned ARMED row `IRPT_ANLREQ-D2-W224-S1`, after the round-50 record. Risk WORLD only by the gate's path floor (`<paths>` under `infra/`, spine v3.19 L6): one new test file, no deploy.
- Base: `AR66-tz-AC1` FAIL as expected (`R46-TESTS-FAIL absent`) at box/dell2 9a9ecafe8c.

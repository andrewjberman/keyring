# TO-AR-tz-64 -- FWD-5 gate: every global (every-firm) admission in code is a row of V2's register (AR-tz-64, round 47, workstream ~TX)

<to_id>IRPT_ANLREQ.TO-AR-tz-64</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~224</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>47</round>
<workstream>~TX</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~TX (gates and tests) | **Decomp cell:** `AR-tz-64` (`decompositions/IRPT_ANLREQ_DECOMP_R47_TX.md`) |
**outcome_ref:** FWD-5 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`AR-tz-64`: "FWD-5 gate: every global (every-firm) admission in code is a row of V2's register." A TEST cell: ONE new test file, no other edit. The CTO ruled (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_IRPT_ANLREQ_FOUR_LANES_END_TO_END_20261015.md`, ADDENDUM 7 item 4) that the `OPAL_GLOBAL` admissions stand for Opal staff only, each named in a register, so that no global admission is implicit. `2.0.0_SA_COO~V2` wrote the register: `org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R19_GLOBAL_ADMISSIONS_REGISTER.md` (rows G1 to G3, and the rule at its end: "A new global admission is a row here in the same commit that adds it, or the commit is wrong"). This test is the GATE that makes the rule mechanical. It is green today and must go red when someone adds an admission that is not a row.

**What to build.** In `infra/aws/lambda/ticket_center/tests/test_cross_firm_global_register.py` write tests that read the register file and the code, both by repo-relative path found from the test file's own location (walk up to the repository root; derive it, never hard-code a drive or an absolute path):

1. Enumerate every site in the code where a principal class `OPAL_GLOBAL` is admitted before a firm comparison: in `infra/aws/lambda/investor-reporting/_scope/interactive_access.py` (`authorize_current`) and `infra/aws/lambda/investor-reporting/reports/resident_installed.py` (`make_authorize`), by the text `OPAL_GLOBAL` in an equality test on `principal_class`. Print the denominator: how many sites and how many files you scanned. Also enumerate the ticket service's explicit global marker: the text `scope_all_firms` in `infra/aws/lambda/ticket_center/lambda_function.py` (zero sites today is fine: V2's fix adds it; the test must not fail when the marker is absent, and must require a register row when it is present).
2. Parse the register's table (columns `#`, `where`, `principal`, `what it admits`, `reason`, `source at HEAD`): the rows G1, G2, G3 name a file in the `where` or `source` cell.
3. Assert: every file that holds a global-admission site is named in at least one register row (by its repo-relative path or its file name); every register row that names an `OPAL_GLOBAL` file points at a file that still holds the site (a stale row fails); and the denominators are printed in the assertion message.
4. A synthetic mutant inside the test file: given an in-memory copy of a code file's text with one extra `principal_class == "OPAL_GLOBAL"` admission in a NEW file name, the same check function returns a violation naming that file (the gate bites); and a copy of the register with a row removed returns a violation (the gate bites the other way). The two mutants run on text in memory, never on the repository files.

Name EVERY test function `test_cross_firm_<what>`. At least three tests. Use only the standard library and pytest. Do not edit the register or any code.

**File you create:**

infra/aws/lambda/ticket_center/tests/test_cross_firm_global_register.py

**Run it** from your worktree root with `python -m pytest -q infra/aws/lambda/ticket_center/tests/test_cross_firm_global_register.py`; all tests pass today.

### ACCEPTANCE

<criterion id="AR64-tz-AC1" cell_refs="AR-tz-64"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_ANLREQ_T2/R46_CHECKS/r46_checks.py tests 3 infra/aws/lambda/ticket_center/tests/test_cross_firm_global_register.py</invocation><expect>R46-TESTS-OK</expect></criterion>
`AR64-tz-AC1` -- the file exists, every test function is named `test_cross_firm_*`, the tests pass and at least 3 pass. Dry-run at box/dell2 3086b5fe82: `R46-TESTS-FAIL absent: ...` -- FAIL as expected.

<expected_criteria>AR64-tz-AC1</expected_criteria>

## BOUNDS

- **Grant.** The test file listed, this order's file, your deliverables folder, the surprise channel. You edit NO code, NO register and NO other test.
- **No network, no AWS, no secret, no deploy.**
- **Refusal clause.** If the register file is absent in your cone, file a `BLOCKING` surprise row naming the folder (`IRPT_ANLREQ-D2-W224-S<k>`) and stop; if its table has another shape than described, parse what it has and say so in a row.
- **No alarms, monitors or notifications.** A gate is a test.

<paths>
infra/aws/lambda/ticket_center/tests/test_cross_firm_global_register.py
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else you READ. The register lives under `org/missions/D7/TCKT/TCKT_VNEXT/` (in your cone).

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R47_TX.md</decomp_doc> (round 47, workstream ~TX), cell `AR-tz-64`.
<owned_cells>AR-tz-64</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion id: AR64-tz-AC1. Instance at `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~224/IRPT_ANLREQ.TO-AR-tz-64.fwd5-global-admissions-register-gate.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> AR64-tz-AC1` BEFORE the flip. Commit the test file first, then pin.
</proof_of_spec>

**REPORT:** the test file, the count passed, the printed denominators (sites and files), the two mutants' violation text, the check line, commits.

---

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a new test file only; no source file, edge or consumer changes. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no permission change.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger is touched. comp-routes and comp-cache: DECLARED-NOT-APPLICABLE.
comp-adversary: RUN -- `comp-adversary compose` on this order at read-vintage HEAD: the neighborhood is the decomposition only, 0 unproven dependencies; the only cited paths it flags GONE are the files this order creates and its proof instance. Traps named for the worker: a red test that fails on an import or a typo instead of the behaviour; a control that is not run against the same fixture as its red twin; a test that mocks the very check it claims to prove; making a red test pass by editing the code under test; a register parse that hard-codes an absolute path.
</preflight>

- Cut on the CTO's ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_IRPT_ANLREQ_FOUR_LANES_END_TO_END_20261015.md` ADDENDUM 7 item 4 ("OPAL_GLOBAL stays for staff only, with each admission named in a register") as a gate, never an alarm. Risk WORLD only because the gate's path floor admits no lower class: one new test file under `infra/`.
- Base: `AR64-tz-AC1` FAIL as expected (`R46-TESTS-FAIL absent`) at box/dell2 3086b5fe82.

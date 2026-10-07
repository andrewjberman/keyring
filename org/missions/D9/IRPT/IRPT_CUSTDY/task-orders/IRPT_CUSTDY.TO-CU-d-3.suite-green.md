# TO IRPT_CUSTDY.TO-CU-d-3 -- round 4 CU-d-3 (E3): the suite green -- the S7 tracer test retired or re-pointed, the failed count printed

<to_id>IRPT_CUSTDY.TO-CU-d-3</to_id>
<project>IRPT_CUSTDY</project>
<issued_to>0.9.0_WK_IRPT_CUSTDY~11</issued_to>
<issued_by>2.0.0_SA_COO~K2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>
<workstream>~K2</workstream>

**Directive:** D9 | **Fabric:** laptop (placement dell2) | **Decomp cell:** `CU-d-3` (`decompositions/IRPT_CUSTDY_DECOMP.round4.md`) |
**outcome_ref:** FWD-1 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`CU-d-3`, item E3 of the CTO's round-3 analysis: "the suite green". `python -m pytest -q data/assets/scripts/gold/irpt_custody/tests`
reads 1 failed at HEAD: `tests/test_advisor_projection_refused.py::test_none_source_names_the_seam_line` (line ~114 asserts a
`NONE-SOURCE file=...:<line> owner=FOO_BAR refused=1 distinct=4 via_none=1` line). Cause: `data/assets/scripts/gold/irpt_custody/none_source.py`
traces accounts the custodian-key projection REFUSES because the seam maps them to the string `'None'`; IRPT_BCKEND's fix (@b43f82c155)
changed `infra/aws/lambda/investor-reporting/_ids/ids.py` (~line 388) to return the raw account for an empty, `'None'` or `'nan'` mapping, so
a `'None'` mapping no longer refuses and the fixture produces nothing to trace. The tracer did its job (it found the bug that fix closed).

**Decide and do ONE of these, and say which in your report:**
- **Retire:** delete `none_source.py`'s refusal-tracing test and mark the tool as historical in its docstring (keep the file; nothing imports
  it at run time), or
- **Re-point:** make the test's fixture use a projection that still refuses for a reason the fixed `ids.py` keeps (read it to find one), so
  the tracer's code path is still exercised.
Do not change `ids.py` or any IRPT_BCKEND file. Do not skip or xfail the test to make the count green -- that is weakening, which the
refusal clause forbids.

**Build a NEW script `data/assets/scripts/gold/irpt_custody/tests/run_suite_check.py`** that runs `pytest -q` over
`data/assets/scripts/gold/irpt_custody/tests` in a subprocess (bounded: `timeout` 300 s), parses the summary, and prints, as its LAST line,
`SUITE dir=data/assets/scripts/gold/irpt_custody/tests passed=<n> failed=<n> errors=<n> skipped=<n> xfailed=<n>`. It must not be collected as
a test (no `test_` prefix in the file name; no `test_` functions).

### ACCEPTANCE

<criterion id="CU12-AC1" cell_refs="CU-d-3"><invocation>python data/assets/scripts/gold/irpt_custody/tests/run_suite_check.py</invocation><expect>failed=0 errors=0</expect></criterion>
`CU12-AC1` -- the whole `irpt_custody` suite on your branch reads 0 failed and 0 errors. The issuer re-runs it on CLOUD after every round-4
merge (the analysis's criterion is "on CLOUD").

<expected_criteria>CU12-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No AWS call.** Never edit another cell's or another project's file.
- **Refusal clause.** If the criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `IRPT_CUSTDY-W11-S<k>`; `disposition` one of UNDER_INVESTIGATION | GRADUATED | DISMISSED_WITH_REASON | DECOMP_INVALIDATING), and do
  not weaken a test.

<paths>
data/assets/scripts/gold/irpt_custody/tests/test_advisor_projection_refused.py
data/assets/scripts/gold/irpt_custody/none_source.py
data/assets/scripts/gold/irpt_custody/tests/run_suite_check.py
org/missions/D9/IRPT/IRPT_CUSTDY/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_CUSTDY/decompositions/IRPT_CUSTDY_DECOMP.round4.md</decomp_doc> (round 4), cell `CU-d-3`.
<owned_cells>CU-d-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CU12-AC1. Instance at `org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/0.9.0_WK_IRPT_CUSTDY~11/IRPT_CUSTDY.TO-CU-d-3.suite-green.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CU12-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** which of retire / re-point you chose and why, the `SUITE` line, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a test repair; no schedule.
comp-iam: DECLARED-NOT-APPLICABLE no IAM change; the cell makes no AWS call at all (tests and a test runner only).
comp-adversary: RUN -- no firm data; the anti-weakening rule (no skip/xfail) is on the face; BLIND: whether the fixed ids.py keeps any refusal path to re-point onto.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: round-3 analysis @ec25e39844 section 2 S7 and section 3 E3; row S7; decomposition round 4 constraint 4.

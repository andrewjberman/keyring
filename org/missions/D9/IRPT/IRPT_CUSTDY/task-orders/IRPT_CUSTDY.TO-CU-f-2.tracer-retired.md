# TO IRPT_CUSTDY.TO-CU-f-2 -- round 6 CU-f-2 (E2): the tracer test retired -- removed with a commit naming why; the suite 0 failed

<to_id>IRPT_CUSTDY.TO-CU-f-2</to_id>
<project>IRPT_CUSTDY</project>
<issued_to>0.9.0_WK_IRPT_CUSTDY~15</issued_to>
<issued_by>2.0.0_SA_COO~K2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>6</round>
<workstream>~K2</workstream>

**Directive:** D9 | **Fabric:** laptop (placement dell2) | **Decomp cell:** `CU-f-2` (`decompositions/IRPT_CUSTDY_DECOMP.round6.md`) |
**outcome_ref:** FWD-1 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`CU-f-2`, item E2 of the CTO's round-5 analysis (ruling S10, verbatim): "The tracer test is RETIRED. Its purpose (naming the seam line that
refused) ended when IRPT_BCKEND made the guard case-insensitive (IB-pr-348). This is the second time it went red on an upstream fix. A test
that exists only to observe a defect goes when the defect does."

The test is `test_none_source_names_the_seam_line` in `data/assets/scripts/gold/irpt_custody/tests/test_advisor_projection_refused.py`
(it fails at HEAD: `assert last.endswith(':%d owner=FOO_BAR refused=1 distinct=4 via_none=1' % want)`). The tool it exercised,
`data/assets/scripts/gold/irpt_custody/none_source.py`, stays as a historical tool: mark it so in its docstring (nothing imports it at run time).

**Build:**
1. Remove `test_none_source_names_the_seam_line` (and any fixture used only by it) from `tests/test_advisor_projection_refused.py`. The other
   tests in that file stay and must pass. Do not skip or xfail it -- remove it.
2. `none_source.py`: a docstring note -- historical; its finding (row W5-S1) was fixed upstream by IRPT_BCKEND IB-pr-339 and IB-pr-348; its
   test was retired by the CTO's ruling S10 (round-5 analysis @f6160117ce).
3. Your commit message names why (the ruling, verbatim in short) -- the CTO's criterion (1).

### ACCEPTANCE

<criterion id="CU18-AC1" cell_refs="CU-f-2"><invocation>python data/assets/scripts/gold/irpt_custody/tests/run_suite_check.py</invocation><expect>failed=0 errors=0</expect></criterion>
`CU18-AC1` -- the CTO's criterion (2): the `irpt_custody` suite on your branch reads 0 failed and 0 errors; the issuer re-runs it on CLOUD.

<expected_criteria>CU18-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file.
- **No AWS call.** Never edit another cell's or another project's file.
- **A surprise row is committed in the same turn you write it.**
- **Refusal clause.** If the criterion cannot be met as written, stop, write the reason in your report and a row (id `IRPT_CUSTDY-W15-S<k>`;
  `disposition` one of UNDER_INVESTIGATION | GRADUATED | DISMISSED_WITH_REASON | DECOMP_INVALIDATING), and do not weaken a test.

<paths>
data/assets/scripts/gold/irpt_custody/tests/test_advisor_projection_refused.py
data/assets/scripts/gold/irpt_custody/none_source.py
org/missions/D9/IRPT/IRPT_CUSTDY/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_CUSTDY/decompositions/IRPT_CUSTDY_DECOMP.round6.md</decomp_doc> (round 6), cell `CU-f-2`.
<owned_cells>CU-f-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CU18-AC1. Instance at `org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/0.9.0_WK_IRPT_CUSTDY~15/IRPT_CUSTDY.TO-CU-f-2.tracer-retired.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CU18-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** the removal, the `SUITE` line, the commit message, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a test retirement; no schedule.
comp-iam: DECLARED-NOT-APPLICABLE no IAM change; the cell makes no AWS call at all (a test file and a docstring).
comp-adversary: RUN -- removal (not skip) per the ruling; the other tests in the file stay; BLIND: none.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: round-5 analysis @f6160117ce section 2 (S10) and section 4 E2; rows S7, S10.

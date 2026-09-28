# TO IRPT_BCKEND.TO-IB-yr-2 -- The lookup-capture test runs from pinned fixtures in the test tree, with no env var

<to_id>IRPT_BCKEND.TO-IB-yr-2</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~64</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<issued_date>2026-09-28</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>19</round>
<workstream>~Y</workstream>

**Directive:** D9 | **Fabric:** laptop | **Workstream:** ~Y | **Decomp cell:** `IB-yr-2` (`decompositions/IRPT_BCKEND_DECOMP_R19_Y.md`)
| **outcome_ref:** FWD-4 backend half (suite hygiene) | **depends_on:** none

---

## WORKER FACE

### THE CELL

`IB-yr-2` -- `test_pinned_actual_capture_omission_not_universal_nonexistence` in
`C:/Users/AndrewBerman/Desktop/ajb_workspace/infra/aws/lambda/investor-reporting/intake/tests/test_security_resolution.py`
(line 31) reads `os.environ["IRPT_LOOKUP_FIXTURE_ROOT"]`, so the suite fails with `KeyError` wherever that variable is
unset (1 failed, 23 passed). It reads three recorded vendor captures that live outside the test tree, in
`C:/Users/AndrewBerman/Desktop/ajb_workspace/org/tier1_exec/4.0.0_SA_CRO/deliverables/IRPT_YCHARTS_LOOKUP_CAPTURE_20260923/`.

**Build:**
1. Copy exactly three files, byte for byte (use `cp`, not an editor), from that capture directory into
   `infra/aws/lambda/investor-reporting/intake/tests/fixtures/lookup_capture/`: `02_securities_info.json`,
   `03_suggest_ALPPL.json`, `04_suggest_BREIT.json`.
2. In the test, take the fixture root from `IRPT_LOOKUP_FIXTURE_ROOT` when it is set, and otherwise default to that
   new directory, resolved relative to the test file (`Path(__file__).resolve().parent / "fixtures" / "lookup_capture"`).
   Change nothing else in the test or its assertions.

### ACCEPTANCE (run from your worktree root)

<criterion id="Y19-2-AC1" cell_refs="IB-yr-2"><invocation>env -u IRPT_LOOKUP_FIXTURE_ROOT python -m pytest -q -p no:cacheprovider infra/aws/lambda/investor-reporting/intake/tests/test_security_resolution.py</invocation><expect>24 passed</expect></criterion>
`Y19-2-AC1` -- the built behaviour: the whole module passes with the variable unset. Base: `1 failed, 23 passed` (KeyError).

<criterion id="Y19-2-AC2" cell_refs="IB-yr-2"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/R19_CHECKS/r19_y2_fixture_copies.py</invocation><expect>COPIES-IDENTICAL 3/3</expect></criterion>
`Y19-2-AC2` -- the three copies are byte-identical to the CRO capture (sha256). Base: 3 MISSING, exit 1.

<expected_criteria>Y19-2-AC1,Y19-2-AC2</expected_criteria>

Base dry-run 2026-09-28 20:2xZ at CLOUD 810a66317f: AC1 `1 failed, 23 passed`; AC2 `MISSING` x3, rc 1.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. The CRO capture directory
  and the check in `R19_CHECKS/` are READ-ONLY. No AWS call, no deploy.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise
  row, and do not weaken the test to pass.

<paths>
infra/aws/lambda/investor-reporting/intake/tests/test_security_resolution.py
infra/aws/lambda/investor-reporting/intake/tests/fixtures/lookup_capture/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP_R19_Y.md</decomp_doc> round 19, workstream ~Y, cell `IB-yr-2`.
<owned_cells>IB-yr-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: Y19-2-AC1, Y19-2-AC2. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~64/IRPT_BCKEND.TO-IB-yr-2.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> Y19-2-AC1,Y19-2-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT (your final message):** each criterion's output line and the commit hash.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule, trigger or scheduled producer is touched; source and test files only.
comp-blast: DECLARED-NOT-APPLICABLE -- a test file and three fixture copies; nothing served.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call.
comp-adversary: RUN -- the risk is a copy that drifts from the capture; AC2 pins all three by sha256 against the CRO source.
lane: the <paths> block IS the grant; no open order holds these files.
</preflight>

Source: `STATUS~Y.md` @37cb971b4a next-list item 8, cut on 1.0.0_SA_CTO 102417. It supersedes the "to the drain" ruling
in decomp @89f619e28b.

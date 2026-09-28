# TO IRPT_BCKEND.TO-IB-yr-1 -- A saved portfolio that is not fixed refuses a tolerated setting BEFORE the vendor generates

<to_id>IRPT_BCKEND.TO-IB-yr-1</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~63</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<issued_date>2026-09-28</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>19</round>
<workstream>~Y</workstream>

**Directive:** D9 | **Fabric:** laptop | **Workstream:** ~Y | **Decomp cell:** `IB-yr-1` (`decompositions/IRPT_BCKEND_DECOMP_R19_Y.md`)
| **outcome_ref:** FWD-4 backend half | **depends_on:** none

---

## WORKER FACE

### THE CELL

`IB-yr-1` -- the Analysis resident creates a vendor portfolio, reads its saved settings back, then asks the vendor to
generate a PDF report. One setting, `level_as_of_type`, is TOLERATED when it differs (the vendor stores `custom_date`
where `prior_close` was sent), but only on a Static portfolio. Today that rule is enforced only AFTER generation and
download, by reading the Type the vendor printed in the PDF (`tolerance_requires_static` in
`C:/Users/AndrewBerman/Desktop/ajb_workspace/infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py`, lines 259-271,
called at lines 219-220). The saved-portfolio read the resident already makes (`GET /model_portfolios/fixed/{id}`, in
`step_read_back` in `.../ycharts/generate/recipe.py` lines 629-701) returns an object `portfolio` that can carry
`model_portfolio_type` (a recorded advisor read shows `model_portfolio_type=fixed`).

**Build:**
1. In `recipe.step_read_back`, when the settings come from the saved portfolio (`source == "saved_portfolio"`), return
   the saved `model_portfolio_type` as a new result key `saved_portfolio_type` (the raw value, or `None` when the key is
   absent). Change nothing else in the comparison rows.
2. In `resident_worker.py`, right after the read-back (line ~200, before `step_validate` and before any generation):
   if any read-back row is `tolerated` AND `saved_portfolio_type` is present AND is not `"fixed"`, raise
   `WorkerAttention("TOLERANCE_REQUIRES_STATIC")`. When the type is `"fixed"` or absent, change nothing: the existing
   printed-type check after download still decides. Keep `saved_portfolio_type` in the semantic read-back checkpoint
   (the dict filtered at line ~203) so a redelivery that resumes from the checkpoint applies the same rule.
3. Do NOT remove or weaken `tolerance_requires_static`: it stays the second line.
4. Optionally add a test to `.../ycharts/generate/tests/test_resident_worker.py`; do not change existing tests.

### ACCEPTANCE (run from your worktree root)

<criterion id="Y19-1-AC1" cell_refs="IB-yr-1"><invocation>python -m pytest -q -p no:cacheprovider org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/R19_CHECKS/test_r19_y1_pregen_static.py -k not_fixed</invocation><expect>1 passed</expect></criterion>
`Y19-1-AC1` -- the built behaviour: a saved type "dynamic" with a tolerated setting ends ATTENTION TOLERANCE_REQUIRES_STATIC
with no generation POST, no download, no PDF checkpoint and no publication. Fails at the base (the vendor generates first).

<criterion id="Y19-1-AC2" cell_refs="IB-yr-1"><invocation>python -m pytest -q -p no:cacheprovider org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/R19_CHECKS/test_r19_y1_pregen_static.py -k fixed_or_absent</invocation><expect>2 passed</expect></criterion>
`Y19-1-AC2` -- the difference control: a saved type "fixed", or no saved type, still generates once, downloads once and
publishes READY through the printed-type check. Passes at the base and must still pass.

<expected_criteria>Y19-1-AC1,Y19-1-AC2</expected_criteria>

Base dry-run 2026-09-28 20:2xZ at CLOUD 810a66317f: AC1 `1 failed` (READY != ATTENTION), AC2 `2 passed`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. The check file in
  `R19_CHECKS/` is READ-ONLY: never edit it. No AWS call, no deploy, no vendor call; the harness replays recorded
  fixtures.
- **Served code moves only through 2.0.0_SA_COO~P's next resident and generate builds**, never by you.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise
  row, and do not weaken the test to pass.

<paths>
infra/aws/lambda/investor-reporting/ycharts/generate/recipe.py
infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_resident_worker.py
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP_R19_Y.md</decomp_doc> round 19, workstream ~Y, cell `IB-yr-1`.
<owned_cells>IB-yr-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: Y19-1-AC1, Y19-1-AC2. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~63/IRPT_BCKEND.TO-IB-yr-1.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> Y19-1-AC1,Y19-1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT (your final message):** each criterion's output line, the diff summary per file, and the commit hash.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule, trigger or scheduled producer is touched; source and test files only.
comp-blast: DECLARED-NOT-APPLICABLE -- two source files inside one Lambda package family; no served move in this cell (P ships it).
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call.
comp-adversary: RUN -- the risk is a FALSE refusal: the rule refuses only on a PRESENT non-"fixed" type; absent defers to the PDF check (AC2's None arm).
lane: the <paths> block IS the grant; no open order holds these files.
</preflight>

Source: `STATUS~Y.md` @37cb971b4a next-list item 6, cut on 1.0.0_SA_CTO 102417 ("cut your independent cells now").
The earlier YAGNI ruling (decomp @89f619e28b) is superseded: the cell is shaped so the inferred premise cannot cause a
wrong refusal on the portfolios we create (all via `/model_portfolios/fixed/`).

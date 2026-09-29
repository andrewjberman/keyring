# TO IRPT_BCKEND.TO-IB-yr-201 -- A Comparison names its compared models to the vendor, and refuses a PDF that prints none

<to_id>IRPT_BCKEND.TO-IB-yr-201</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~71</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<issued_date>2026-09-29</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>20</round>
<workstream>~Y</workstream>

**Directive:** D9 | **Fabric:** laptop | **Workstream:** ~Y | **Decomp cell:** `IB-yr-201` (`decompositions/IRPT_BCKEND_DECOMP_R20_Y.md`)
| **outcome_ref:** FWD-4 backend half (Comparison / Multi-Comp) | **depends_on:** none

---

## WORKER FACE

### THE CELL

`IB-yr-201` -- the first live Comparison report (window 21, REQ-e4b7f5ab) went READY and certified, but its PDF prints
only the client portfolio: the chosen model "Opal Long-Term" (`P:1728413`) appears nowhere. The cause, by source diff:
`C:/Users/AndrewBerman/Desktop/ajb_workspace/infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py`
line 210 sends `security_ids = ["P:" + str(portfolio["model_portfolio_id"])]` (the client portfolio ONLY) to both
`recipe.step_validate` (line 211) and `recipe.generation_body` (line 212). The research builder whose Comparison PDFs
DID print the model sends the primary plus every comparison:
`C:/Users/AndrewBerman/Desktop/ajb_workspace/docs/research/investor_reporting_ycharts_variants_20260911/recipe_contract.py`
lines 211-218 (it also requires the template's `num_required_securities == min_comparisons + 1`, and refuses a
duplicate id). Each prepared comparison is a catalogue entry with `vendor_id` and `name` (see `frozen_worker.py:95` and
`recipe.generation_body`, which already reads `c["vendor_id"]`).

**Build:**
1. In `.../ycharts/generate/recipe.py`, add
   `report_security_ids(model_portfolio_id, comparisons, template) -> list[str]`: returns
   `["P:" + str(model_portfolio_id)] + [c["vendor_id"] for c in comparisons]`. Raise `RecipeRefused` when
   `len(comparisons)` is outside `template["comparison_securities"]["min"]..["max"]`, and when any id repeats (the
   primary included). Pure; no I/O; no new import.
2. In `resident_worker.py`, replace line 210 with `security_ids = recipe.report_security_ids(portfolio["model_portfolio_id"],
   prepared["comparisons"], plan["template"])`, and pass that same list to `step_validate` and `generation_body`.
3. In `resident_worker.py`, add `missing_comparisons(pdf_bytes, comparisons) -> list[str]`: the chosen comparison
   names (`c["name"]`, stripped) that the PDF's text does NOT print as a whole name (pdfplumber page text; the same
   whole-name match as `case_trace.printed_labels`: a name not inside a longer word or hyphenated name). Import
   pdfplumber INSIDE the function: `recipe.py` is also imported by the generate Lambda, so nothing PDF-related goes there.
   Then, right after the PDF download and before `tolerance_requires_static` and before any PDF is retained: if
   `prepared["comparisons"]` is non-empty and `missing_comparisons(data, prepared["comparisons"])` is non-empty, raise
   `WorkerAttention("COMPARISON_NOT_PRINTED")`.
4. Do not change existing tests; you may add tests to `.../ycharts/generate/tests/test_resident_worker.py`.

### ACCEPTANCE (run from your worktree root)

<criterion id="Y20-1-AC1" cell_refs="IB-yr-201"><invocation>python -m pytest -q -p no:cacheprovider org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/R20_CHECKS/test_r20_y1_comparison.py::test_ids_primary_then_comparisons_with_the_template_count</invocation><expect>1 passed</expect></criterion>
`Y20-1-AC1` -- `report_security_ids` returns primary + comparisons and refuses a wrong count and a duplicate. Base:
AttributeError.

<criterion id="Y20-1-AC2" cell_refs="IB-yr-201"><invocation>python -m pytest -q -p no:cacheprovider org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/R20_CHECKS/test_r20_y1_comparison.py::test_wiring_the_resident_sends_report_security_ids</invocation><expect>1 passed</expect></criterion>
`Y20-1-AC2` -- the resident calls it exactly once per generation (spied on the harness's Overview run: comparisons []),
and the run still ends READY. Base: the spy is never called.

<criterion id="Y20-1-AC3" cell_refs="IB-yr-201"><invocation>python -m pytest -q -p no:cacheprovider org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/R20_CHECKS/test_r20_y1_comparison.py::test_printed_missing_comparisons_on_real_pdfs</invocation><expect>1 passed</expect></criterion>
`Y20-1-AC3` -- `missing_comparisons` is [] on the synthetic comparison.pdf (prints "Opal Long-Term") and names it on
overview.pdf. Base: AttributeError.

<expected_criteria>Y20-1-AC1,Y20-1-AC2,Y20-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. The check in
  `R20_CHECKS/`, the research contract and the PDF fixtures are READ-ONLY. No AWS call, no deploy, no vendor call.
- **Served code moves only through 2.0.0_SA_COO~P's next resident build**, never by you.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise
  row, and do not weaken the test to pass.

<paths>
infra/aws/lambda/investor-reporting/ycharts/generate/recipe.py
infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_resident_worker.py
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP_R20_Y.md</decomp_doc> round 20, workstream ~Y, cell `IB-yr-201`.
<owned_cells>IB-yr-201</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: Y20-1-AC1, Y20-1-AC2, Y20-1-AC3. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~71/IRPT_BCKEND.TO-IB-yr-201.comparison-names-its-models.proof_of_spec.json`
(the ORDER FILE's basename, which the gate's complete-flip search globs), validated with
`python .tools/proof-of-spec-check.py <instance> Y20-1-AC1,Y20-1-AC2,Y20-1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT (your final message):** each criterion's output line, the diff summary per file, and the commit hash.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule, trigger or scheduled producer is touched; source and test files only.
comp-blast: DECLARED-NOT-APPLICABLE -- two resident source files; nothing served moves in this cell (~P ships the resident).
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call.
comp-adversary: RUN -- two risks named: (1) generate imports recipe, so pdfplumber stays out of recipe.py (the check lives in resident_worker, imported lazily); (2) a Comparison refused by name before retention is a named ATTENTION, never a published wrong report.
lane: the <paths> block IS the grant; no open order holds these files.
</preflight>

Source: rows S194 (@90c1f17d67) and S196 (@550178487a); W21 part-Y record @a89e14436b; CTO round-19 analysis section 6 item 3.

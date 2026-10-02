# TO IRPT_BCKEND.TO-IB-pr-292 -- The export submit path's Analysis branch: no narrative step, the analysis template, the report's own as-of as the cutoff

<to_id>IRPT_BCKEND.TO-IB-pr-292</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~101</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-10-02</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>29</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** CTO round-28 ~P analysis E2 (msg 104156); row IRPT_BCKEND-W101-S2 |
**Decomp cell:** `IB-pr-292` (decomposition section 27) | **outcome_ref:** FWD-9 (hop 12) | **depends_on:** none (queued on this slot
after TO-IB-pr-291)

---

## WORKER FACE

**The cell.** The export's submit path is Performance-only: `export/submit_installed.py` `_validate` raises "only a Performance report
exports", and `export/narrative_submit.py` `cutoff_for` and `serve_submit` read `dates.actual_end`, which an Analysis report does not
carry. Give the submit path an Analysis branch.

**What exists (read first).** `export/submit_installed.py`, `export/narrative_submit.py`, `export/submit_service.py`,
`export/handler.py` (`:256-258` already chooses `analysis-portrait-letter` for a non-performance kind; `:313-316` forbids the text
"Narrative" in an analysis PDF), `export/retained_export.py` (`resolve()` returns `kind` and, for ANALYSIS, `request_id`; merged
@9079753aa7). The contract: `docs/contracts/investor-reporting/v1/AnalysisReport.schema.json` -- an Analysis report has no report-level
date; each section carries `as_of_date`.

**What you build.**
- The Analysis branch: for a resolved ANALYSIS report there is NO narrative step (no narrative packet is built or requested), the
  template is `analysis-portrait-letter`, and the cutoff is the report's own as-of -- the LATEST `as_of_date` among the retained
  report's sections -- never `dates.actual_end`. `submit_installed._validate` admits ANALYSIS with that cutoff; PERFORMANCE is
  validated exactly as today; any other kind stays refused by name.
- `export/tests/test_submit_analysis_branch.py`: at least 4 tests naming both kinds -- an ANALYSIS submission validates with the
  latest section as-of as cutoff; it requests no narrative; its template is `analysis-portrait-letter`; a PERFORMANCE submission
  validates exactly as before.
- The real one (reads only; nothing submitted, persisted, dispatched or written): pass the real retained READY report
  `RPT-1f49504f501a6633b1f9cccc5f37ecf6` (request `REQ-e4b7f5aba7fb218c37f28002`; its bucket and key are in
  `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~101/ANALYSIS_EXPORT_R28.json`) through the new validation and
  write `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~101/SUBMIT_ANALYSIS_R29.json`:
  `{"report_ref": {"bucket", "key", "report_id"}, "validated": true, "cutoff": "YYYY-MM-DD", "template": "analysis-portrait-letter",
  "narrative_step": false}`.

<criterion id="IB29-2-AC1" cell_refs="IB-pr-292"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r29/p29_2_ac1_submit_analysis_tests.py" .</invocation><expect>IB29-2-AC1 PASS</expect></criterion>
`IB29-2-AC1` -- the new test file names both kinds; at least 4 new tests pass beside the existing export suites, none failing. Base:
FAIL (no file).

<criterion id="IB29-2-AC2" cell_refs="IB-pr-292"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r29/p29_2_ac2_real_submit_validation.py" .</invocation><expect>IB29-2-AC2 PASS</expect></criterion>
`IB29-2-AC2` -- the seam with the real neighbour: the real READY report validates with the cutoff equal to its latest section
as-of, the analysis template and no narrative step. Base: FAIL (no record).

<expected_criteria>IB29-2-AC1,IB29-2-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file.
- **AWS:** reads only. No write, no submit, no dispatch, no deploy, no vendor call.
- **Refusal clause.** A PERFORMANCE answer that moves is a defect, stopped with a row; a field the Analysis branch needs that the
  retained report lacks is a row, never an invented value.

<paths>
infra/aws/lambda/investor-reporting/export/submit_installed.py
infra/aws/lambda/investor-reporting/export/narrative_submit.py
infra/aws/lambda/investor-reporting/export/tests/test_submit_analysis_branch.py
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r29/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read without a grant (never written): `infra/aws/lambda/investor-reporting/` (all of it), `docs/contracts/investor-reporting/v1/`, `lib/`.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 27 (round 29, workstream ~P), cell `IB-pr-292`.
<owned_cells>IB-pr-292</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB29-2-AC1, IB29-2-AC2. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~101/IRPT_BCKEND.TO-IB-pr-292.submit-analysis-branch.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IB29-2-AC1,IB29-2-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message: the commit hashes, each criterion's last line, the cutoff used, and any surprise row id.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- two source files of the export function and one new test; 0 served bytes move in the cell.
comp-iam: DECLARED-NOT-APPLICABLE -- no role changes.
comp-routes: DECLARED-NOT-APPLICABLE -- the submit route is unchanged; what it admits widens to ANALYSIS at the served move.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: a request-driven submit path; no schedule, trigger or cron is created or moved.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- IB29-2-AC1 base FAIL (no test file), IB29-2-AC2 base FAIL (no record), dry-run at the base 2026-10-02 ~10:2xZ.
lane: the <paths> block IS the grant.
</preflight>

# TO IRPT_BCKEND.TO-IB-pr-281 -- Hop 12: the retained-export path admits an Analysis report (resolve, grant, print query), proven on one real READY report built locally

<to_id>IRPT_BCKEND.TO-IB-pr-281</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~101</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-10-02</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>28</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** 1.0.0_SA_CTO RULINGS batch 126 item 1 (msg 104117); trace
`org/tier1_exec/4.0.0_SA_CRO~X/deliverables/ANALYSIS_END_TO_END_GAP_BRIEF_20261001.md` section 12 | **Decomp cell:** `IB-pr-281`
(decomposition section 26) | **outcome_ref:** FWD-9 (the Analysis export) | **depends_on:** none

---

## WORKER FACE

**The cell.** An advisor can export a Performance report as an Opal-branded PDF; an Analysis report cannot. The refusal is in the
export Lambda's own resolver. Make the retained-export path admit a retained ANALYSIS report, prove it with tests for both kinds, and
build ONE real READY Analysis report into a bundle and print query locally. You build and prove; you never submit, render, upload,
build an artifact or deploy (the served move is the issuer's next act).

**The code (repo-relative).**
- `infra/aws/lambda/investor-reporting/export/retained_export.py`: `resolve()` (`:56-76`) refuses unless `report_kind == "PERFORMANCE"`
  and the owner carries a server-issued `account_set_id` ("only a retained Performance report over a server-issued selection exports");
  `render_grant()` pins `accountSetId`/`jobId`/`reportId`; `print_query()` hard-codes `kind: "performance"` and the REQUESTED window.
- Already Analysis-aware, read them: `export/handler.py:211, :256-258` (`report_kind`, template `analysis-portrait-letter` for anything
  not `performance`), `:313-316` (an analysis PDF must not carry the text "Narrative"); `ops/owned_report.py:90` (an ANALYSIS
  authorization row); `reports/repository.py` (`get`, `list(principal, report_kind=...)`, `_report_identity`); the render grant module
  `infra/aws/lambda/investor-reporting/_render_identity/grant.py`.
- The print page (portal, READ ONLY): `portal/src/pages/InvestorReporting/render/PrintEntry.tsx` reads `?kind=performance|analysis`
  and renders `AnalysisDocument` from the bundle. It is not yours to change: if it cannot render what your bundle carries, that is a
  row naming the field, never a portal edit.
- Contracts: `docs/contracts/investor-reporting/v1/AnalysisReport.schema.json`, `ExportBundle.schema.json`.

**What you build.**
- In `retained_export.py`: `resolve()` admits a retained report whose kind is ANALYSIS, read back under the current principal exactly as
  the Performance arm is (the repository's own authorization; a report the caller cannot read stays refused), with the analysis
  request's own identity in place of an account set; PERFORMANCE behaves exactly as today; any other kind stays refused with a named
  message. `render_grant()` and `print_query()` take the kind from the resolved report: for ANALYSIS the pinned ids name the request/
  job and report, and the query carries `kind: "analysis"` and the report's ids (no requested Performance window). Keep every refusal
  a named `ExportSubmitRefused`.
- `infra/aws/lambda/investor-reporting/export/tests/test_retained_export_analysis.py`: at least 5 tests, naming both kinds -- an
  ANALYSIS report resolves; a PERFORMANCE report still resolves as before; an unknown kind is refused; an ANALYSIS report the caller
  cannot read is refused; the analysis grant and print query carry the analysis ids and `kind: "analysis"`.
- The real one: list the retained ANALYSIS reports through `reports/repository.py` (reads only) and pick one whose request is READY
  (the live thread ran Cottonwood jobs). Build its bundle and print query through the new path with nothing persisted, dispatched or
  submitted. Save the bundle to `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~101/analysis_export_bundle_R28.json`
  and write `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~101/ANALYSIS_EXPORT_R28.json`:
  `{"report_ref": {"bucket", "key", "report_id", "revision"}, "request_status": "READY", "bundle_file": "<the saved bundle's
  repo-relative path>", "print_query": {...}}`. No client name, account number or figure goes in either file beyond what the bundle
  itself is.

<criterion id="IB28-1-AC1" cell_refs="IB-pr-281"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r28/p28_1_ac1_analysis_export_tests.py" .</invocation><expect>IB28-1-AC1 PASS</expect></criterion>
`IB28-1-AC1` -- the test file names both kinds and at least 5 tests pass with none failing. Base: FAIL (no test file).

<criterion id="IB28-1-AC2" cell_refs="IB-pr-281"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r28/p28_1_ac2_real_analysis_bundle.py" .</invocation><expect>IB28-1-AC2 PASS</expect></criterion>
`IB28-1-AC2` -- the seam with the real neighbour: a real retained READY Analysis report reads back from S3 with the AnalysisReport
keys, and the locally built bundle carries every ExportBundle key, exactly one authorized row naming that report, no live vendor
request, a non-empty selection no larger than the report's sections, and an analysis print query naming the report. Base: FAIL.

<expected_criteria>IB28-1-AC1,IB28-1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file.
- **AWS:** reads only (the reports repository, the retained report object). No write, no Lambda invoke, no render dispatch, no
  artifact upload, no vendor call.
- **Refusal clause.** A field the print page needs that the retained report lacks is a row naming it (the bundle never invents one);
  a resolver change that moves any PERFORMANCE answer is a defect, stopped with a row.

<paths>
infra/aws/lambda/investor-reporting/export/retained_export.py
infra/aws/lambda/investor-reporting/export/tests/test_retained_export_analysis.py
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r28/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read without a grant (never written): `infra/aws/lambda/investor-reporting/` (export, reports, ops, `_authz`, `_render_identity`),
`docs/contracts/investor-reporting/v1/`, `portal/src/pages/InvestorReporting/render/`, `lib/`, `infra/logic/registry/`.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 26 (round 28, workstream ~P), cell `IB-pr-281`.
<owned_cells>IB-pr-281</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB28-1-AC1, IB28-1-AC2. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~101/IRPT_BCKEND.TO-IB-pr-281.analysis-export-resolve.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IB28-1-AC1,IB28-1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message: the commit hashes, each criterion's last line, the report id and revision used, and any surprise row
id (`IRPT_BCKEND-W101-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule.
comp-iam: DECLARED-NOT-APPLICABLE in this cell -- reads under the worker's session; the served move's packet reads the export role's grants on retained ANALYSIS reports.
comp-blast: RUN -- one source file and one test file of the export function; 0 served bytes move in the cell.
comp-routes: RUN as a reading -- the export submit route is unchanged; what it admits widens to ANALYSIS at the served move.
comp-cache: DECLARED-NOT-APPLICABLE.
comp-adversary: RUN -- IB28-1-AC1 base FAIL (no test file), IB28-1-AC2 base FAIL (no record), dry-run at the base 2026-10-02 ~08:2xZ.
lane: the <paths> block IS the grant; export/** is IRPT_COMPLETION_P.
</preflight>

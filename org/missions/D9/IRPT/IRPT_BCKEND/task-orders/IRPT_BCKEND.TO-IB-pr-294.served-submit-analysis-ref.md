# TO IRPT_BCKEND.TO-IB-pr-294 -- The served submit takes the Analysis branch: an Analysis bundle pins the retained report by analysis_report_ref, and the packaged contracts equal the published ones

<to_id>IRPT_BCKEND.TO-IB-pr-294</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~101</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-10-02</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>31</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** CTO round-28 ~P analysis ADDENDUM 2, cell E6, and PRD ADDENDUM v0.24 (CONTRACTS row
ExportBundle; batch 149 @11e1413e28; ratified-text half re-signed by 3.0.0_SA_CVO @e978d1f839, msg 104196); rows IRPT_BCKEND-W101-S5,
W101-S6 | **Decomp cell:** `IB-pr-294` (decomposition section 27 addendum note: round 31, one cell; row IRPT_BCKEND-S267) |
**outcome_ref:** FWD-9 (hop 12) | **depends_on:** IB-pr-292 (merged @4f3f36d16c); queued on slot 101 after TO-IB-pr-293

---

## WORKER FACE

**The cell.** `export/submit_service.py` `serve_submit` (`:39-93`) always builds a narrative packet (`narrative_submit.build_and_bind`,
which reads `dates.actual_end`) and freezes it as `narrative_packet_ref`, which the ExportBundle contract requires. An Analysis
report has no narrative and no `dates.actual_end`. The ruled contract (PRD v0.24): an Analysis bundle carries `analysis_report_ref`
(`report_id`, `revision`, `sha256`) IN PLACE OF `narrative_packet_ref` -- exactly one of the two; both, or neither, is refused; never
a null. Separately, the packaged `_contracts/AnalysisReport.schema.json` is older than the published docs copy and refuses the real
report (row W101-S6).

**What exists (read first).**
- `export/submit_service.py` (`serve_submit`), `export/narrative_submit.py` (`build_and_bind`, `cutoff_for` -- its Analysis branch
  merged @4f3f36d16c), `export/submit_installed.py` (`_validate`, the Analysis cutoff), `export/handler.py` (`:209`, `:233`, `:425`
  pass `narrative_packet_ref`), `export/bundle.py` (`freeze` `:86-110`, `rebrand` `:144`, `validate`, `contracts_dir`).
- `export/retained_export.py` `resolve()` returns `kind` (PERFORMANCE | ANALYSIS) and the retained report.
- Contracts: `docs/contracts/investor-reporting/v1/ExportBundle.schema.json`, `AnalysisReport.schema.json`, `CONTRACT.md` (`:318-333`,
  the ExportBundle field table; `:330` is the `narrative_packet_ref` row); packaged copies in
  `infra/aws/lambda/investor-reporting/_contracts/` (both differ from the docs copies today, `$id` included).
- The PRD v0.24 CONTRACTS row ExportBundle: `org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md`.
- The real retained READY report: `RPT-1f49504f501a6633b1f9cccc5f37ecf6` (bucket and key in
  `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~101/SUBMIT_ANALYSIS_R29.json`).

**What you build.**
- `serve_submit`: for a resolved ANALYSIS report, no narrative packet is built or requested; the bundle carries `analysis_report_ref`
  for the resolved report and its revision; the cutoff is the report's own as-of (the latest section `as_of_date`), never
  `dates.actual_end`. A PERFORMANCE request's path is unchanged.
- The ExportBundle schema (docs copy first, then the packaged copy byte-equal to it): exactly one of `narrative_packet_ref` or
  `analysis_report_ref`; `CONTRACT.md` `:330` and a new row for `analysis_report_ref` say the same. `bundle.freeze` and `rebrand`
  carry whichever reference the bundle has. The packaged `AnalysisReport.schema.json` made byte-equal to its docs copy.
- Tests: `export/tests/test_serve_submit_analysis.py` (at least 3; name analysis, narrative and `actual_end`);
  `export/tests/test_bundle_report_ref.py` (at least 3; an Analysis bundle with `analysis_report_ref` validates, "both" refused,
  "neither" refused); `export/tests/test_packaged_contracts_match_docs.py` (at least 2; one per schema file, byte equality).
- Records in your deliverables folder: `NARRATIVE_REF_READERS_R31.json` -- every reader of `narrative_packet_ref` (comp-find, the
  denominator printed) as `{"files_scanned": n, "census_command": "...", "readers": [{"path", "how", "disposition":
  "handles"|"never-receives", "why"}]}`, listing at least `export/submit_service.py`, `export/narrative_submit.py`,
  `export/handler.py`, `export/bundle.py`; `PACKAGED_CONTRACT_R31.json` -- the real report validated against the PACKAGED copy
  (reads only): `{"report_ref": {"bucket", "key", "report_id"}, "schema_path": "infra/aws/lambda/investor-reporting/_contracts/AnalysisReport.schema.json", "valid": true, "cutoff": "YYYY-MM-DD"}`.

<criterion id="IB31-1-AC1" cell_refs="IB-pr-294"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r31/p31_1_ac1_serve_submit_analysis.py" .</invocation><expect>IB31-1-AC1 PASS</expect></criterion>
`IB31-1-AC1` -- (a) the new serve_submit tests pass (at least 3) and the whole `export/tests` folder fails 0. Base: FAIL (no file).

<criterion id="IB31-1-AC2" cell_refs="IB-pr-294"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r31/p31_1_ac2_bundle_exactly_one_ref.py" .</invocation><expect>IB31-1-AC2 PASS</expect></criterion>
`IB31-1-AC2` -- (b) exactly-one tests pass; the stored client fixtures validate unchanged on the packaged schema; the reader census
lists the four readers, each `handles` or `never-receives` with a why. Base: FAIL (no file).

<criterion id="IB31-1-AC3" cell_refs="IB-pr-294"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r31/p31_1_ac3_packaged_contracts_equal.py" .</invocation><expect>IB31-1-AC3 PASS</expect></criterion>
`IB31-1-AC3` -- (c) both packaged schemas byte-equal to the docs copies, a test asserts it, the real report validates on the packaged
copy (cutoff 2026-09-29), and the `_contracts` suite fails 0. Base: FAIL (bytes differ).

<expected_criteria>IB31-1-AC1,IB31-1-AC2,IB31-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. The stored fixtures in
  `_contracts/fixtures/` are NOT granted: a client fixture that would have to change is a row.
- **The published v1 contract changes under PRD v0.24.** `PATH_MANIFEST.json` calls the docs copy "IMMUTABLE once IB-rt-1 flips
  complete"; the ratified PRD addendum is the authority for this change. Do not edit `PATH_MANIFEST.json`; if a gate or test reads it
  and refuses, file a row.
- **AWS:** reads only (the real report). No write, no submit, no dispatch, no deploy, no vendor call.
- **Refusal clause.** A PERFORMANCE answer that moves is a defect: stop and file a row. An existing test that moves is a row, never an
  edit to that test. A reader outside `<paths>` that would receive an Analysis bundle is a row naming it.

<paths>
infra/aws/lambda/investor-reporting/export/submit_service.py
infra/aws/lambda/investor-reporting/export/narrative_submit.py
infra/aws/lambda/investor-reporting/export/handler.py
infra/aws/lambda/investor-reporting/export/bundle.py
infra/aws/lambda/investor-reporting/_contracts/ExportBundle.schema.json
infra/aws/lambda/investor-reporting/_contracts/AnalysisReport.schema.json
docs/contracts/investor-reporting/v1/ExportBundle.schema.json
docs/contracts/investor-reporting/v1/CONTRACT.md
infra/aws/lambda/investor-reporting/export/tests/test_serve_submit_analysis.py
infra/aws/lambda/investor-reporting/export/tests/test_bundle_report_ref.py
infra/aws/lambda/investor-reporting/export/tests/test_packaged_contracts_match_docs.py
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r31/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read without a grant (never written): `infra/aws/lambda/investor-reporting/` (all of it), `docs/contracts/investor-reporting/v1/`, `lib/`.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 27 addendum note (round 31, workstream ~P), cell `IB-pr-294`.
<owned_cells>IB-pr-294</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB31-1-AC1, IB31-1-AC2, IB31-1-AC3. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~101/IRPT_BCKEND.TO-IB-pr-294.served-submit-analysis-ref.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IB31-1-AC1,IB31-1-AC2,IB31-1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message: the commit hashes, each criterion's last line, the readers with their dispositions, and any surprise
row id (`IRPT_BCKEND-W101-S<k>`).

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the served submit (`export/submit_service.py`) and the published v1 ExportBundle contract; existing bundles keep validating (the stored client fixtures are graded by AC2); 0 served bytes move in the cell.
comp-iam: DECLARED-NOT-APPLICABLE -- no role changes.
comp-routes: DECLARED-NOT-APPLICABLE -- the submit route is unchanged; what it admits widens to ANALYSIS at the served move (E4).
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: a request-driven submit path and a contract file; no schedule, trigger or cron is created or moved.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- IB31-1-AC1 base FAIL (no file), IB31-1-AC2 base FAIL (no file), IB31-1-AC3 base FAIL (packaged AnalysisReport not byte-equal), dry-run at the base 2026-10-02 ~11:2xZ.
lane: the <paths> block IS the grant.
</preflight>

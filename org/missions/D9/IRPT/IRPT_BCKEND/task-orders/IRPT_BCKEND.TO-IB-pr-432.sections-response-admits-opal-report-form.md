# TO IRPT_BCKEND.TO-IB-pr-432 -- the published sections response admits the Opal-made report form the handler already answers

<to_id>IRPT_BCKEND.TO-IB-pr-432</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~290</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>130</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2` msg 4923 (rows IRPT_YCDGEN-W2-S13, IRPT_YCDGEN-W6-S4; `2.0.0_SA_COO~G2` msg 4936) | **Decomp cell:** `IB-pr-432` (decomposition section 123) | **outcome_ref:** FWD-4

---

## WORKER FACE

Root: `C:/dev/wk-irpt-bckend-290/` (bash `/c/dev/wk-irpt-bckend-290`). Work only there. No AWS call, no deploy, no handler edit.

**The defect.** The route `GET /api/scoped/investor-reporting/analysis/{jobId}/sections` (operation `analysis-report`, handler
irpt-status) answers two forms, by `infra/aws/lambda/investor-reporting/ops/owned_report.py` (about lines 85-104):
- an `OPAL_ENGINE` report answers `provider`, `request_ref`, `sections`, `computation_validation` and `retained_ref`, never
  `extraction_validation`;
- a vendor report (no `provider`, or `YCHARTS`) answers `request_ref`, `sections`, `extraction_validation` and `retained_ref`.

The published response schema `docs/contracts/investor-reporting/v1/responses/analysis-report.response.schema.json` states only the
second: its `data` member is closed (`additionalProperties: false`), requires `extraction_validation`, and has no `provider` and no
`computation_validation`. So the handler's Opal answer fails its own contract. The ratified text already admits the form: PRD
ADDENDUM v0.28 item 29 (`org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md`, about lines 665-692): `provider: OPAL_ENGINE`
carries `computation_validation` in place of the vendor members, and under it the vendor members are ABSENT, never null. The
portal's sections reader already reads `computation_validation` (CTO msg 4923), so no reader goes first.

**Build:**
1. Change the response schema's `data` member so it admits EXACTLY two closed forms and nothing between them:
   - the vendor form, exactly as it stands today (same required members, same optional members, `additionalProperties: false`);
     if `provider` is admitted on it at all, only as the constant `YCHARTS`, optional;
   - the Opal form: required `provider` (constant `OPAL_ENGINE`), `request_ref`, `sections`, `computation_validation`; optional
     `retained_ref`; `additionalProperties: false`; no `extraction_validation`, `undated_sections` or `extraction_coverage`.
   Take each Opal member's shape by `$ref` from the v2 report contract, never by retyping it: the v2 schema is
   `infra/aws/lambda/investor-reporting/_contracts/AnalysisReport.v2.schema.json` (read its `$id` and `$defs`); `retained_ref` by the
   same `$ref` the vendor form uses. Keep the envelope members (`contract_version`, `operation`, `firm_id`, `unprojected_grant`,
   `status`, the `x-` annotations) untouched; update the `data` description to say both forms.
2. **The reference must resolve where the repo's own tests resolve it.** The test
   `_contracts/tests/test_seam_paired.py::test_every_declared_route_has_a_response_contract_whose_refs_resolve` builds its own
   registry; it FAILS at base for another route (`analysis-request-original`, not yours). Read how it and
   `validate_against_response_contract` find schema files. If a `$ref` into the v2 schema cannot resolve in that registry because
   the v2 file is outside the folder it loads, STOP and file a row saying which line builds the registry and what it loads; do not
   edit a test, do not copy the v2 schema into another folder, do not inline its shapes.
3. **Producer fixtures**, in `infra/aws/lambda/investor-reporting/_contracts/fixtures/`, each made by the handler's own code path
   (run `owned_report.py`'s sections function over the existing report fixtures or the existing tests' fakes; do not hand-write an
   answer): `analysis-report.sections.opal.valid.json` and `analysis-report.sections.vendor.valid.json`, in the wrapper form the
   folder's other fixtures use (`_fixture`, `_source`, `_expect`, `instance`), plus one `analysis-report.sections.opal.invalid.json`
   (the Opal answer with `extraction_validation` added; `_expect` says refused). Synthetic values only. A firm id in a fixture is
   an opaque `fir_` id or absent: the commit-time naming gate REFUSES a file carrying a real firm's name or the tenant code of
   one, and a hand edit to pass it is not allowed; if the handler's answer carries one, stop and file a row.
4. **Run** `python -m pytest _contracts -q -p no:cacheprovider -rf` from `infra/aws/lambda/investor-reporting/`. At base:
   `2 failed, 203 passed`, both failures `analysis-request-original`. After: the same two and no other.
5. **Record** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~290/IB130-1_sections_response_record.json`:
   `{files_changed:[...], v2_schema_id, handler_answers:[{form:"OPAL_ENGINE"|"YCHARTS", built_by:"<file>:<function>", invocation,
   validates}], readers_named:[...], packaged_in_functions:[...], suite_before, suite_after}`. `handler_answers`: the handler's own
   answer of each form validated against the changed schema's `data` member (script in your deliverables folder; `invocation` is
   the command). `readers_named`: every reader of this response schema file or of the sections answer you can name from the repo
   (tests, the portal's reader by file name if the worktree has it, other functions), each with one line on whether it reads the
   schema or the answer. `packaged_in_functions`: functions whose row in `infra/aws/lambda/ci/lambda-source-map.json` stages the
   response schema file (do not edit the map).

<criterion id="IB130-1-AC1" cell_refs="IB-pr-432"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r130/p130_cells.py" . IB130-1-AC1</invocation><expect>IB130-1-AC1 PASS</expect></criterion>
<criterion id="IB130-1-AC2" cell_refs="IB-pr-432"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r130/p130_cells.py" . IB130-1-AC2</invocation><expect>IB130-1-AC2 PASS</expect></criterion>
<criterion id="IB130-1-AC3" cell_refs="IB-pr-432"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r130/p130_cells.py" . IB130-1-AC3</invocation><expect>IB130-1-AC3 PASS</expect></criterion>

<expected_criteria>IB130-1-AC1, IB130-1-AC2, IB130-1-AC3</expected_criteria>

What AC1 does, exactly: it loads every schema file with an `$id` from `docs/contracts/investor-reporting/v1/`, its `responses/`
folder and `infra/aws/lambda/investor-reporting/_contracts/*.schema.json` into one registry and validates four documents against
the response schema's `data` member: (a) the members `provider`, `request_ref`, `sections`, `computation_validation` of
`AnalysisReport.v2.opal.valid.json` must VALIDATE; (b) `request_ref`, `sections`, `extraction_validation` of
`AnalysisReport.valid.json` must VALIDATE; (c) document (a) plus `extraction_validation` must be REFUSED; (d) document (a) without
`computation_validation` must be REFUSED. At base (a) fails and (b), (c), (d) hold.

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. No handler, no test file, no `_authz/`, no portal, no source map, no other schema.
- **Refusal clause:** if a criterion cannot be met as written, or the two forms cannot be stated without retyping a v2 shape, stop,
  file a row and report. Never weaken a check or a test; do not edit `p130_cells.py`.
- **Row ids** are `IRPT_BCKEND-D2-W290-S<k>`; `surfaced_at` is `date -u +%FT%TZ` at filing; append only, keeping the channel
  file's existing line endings byte for byte; check the id is free just before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~290" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~290@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~290 <0.9.0_WK_IRPT_BCKEND~290@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only. Do not push. Use no gate override.

<paths>
docs/contracts/investor-reporting/v1/responses/analysis-report.response.schema.json
infra/aws/lambda/investor-reporting/_contracts/fixtures/analysis-report.sections.opal.valid.json
infra/aws/lambda/investor-reporting/_contracts/fixtures/analysis-report.sections.vendor.valid.json
infra/aws/lambda/investor-reporting/_contracts/fixtures/analysis-report.sections.opal.invalid.json
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~290/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-432.sections-response-admits-opal-report-form.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 123 (round 130, workstream ~P), cell `IB-pr-432`.
<owned_cells>IB-pr-432</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB130-1-AC1, IB130-1-AC2, IB130-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~290/IRPT_BCKEND.TO-IB-pr-432.sections-response-admits-opal-report-form.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: the schema's two forms in two lines; how each `$ref` resolves and in which registry; the
fixtures and the handler path that made each; the suite's last line before and after; the four arms of AC1; the readers named;
which functions package the schema file; each criterion's last line; the proof checker's result; commit hashes; any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the tool was not run by the issuer; one contract schema file and three new fixtures; no handler, route, function or deployed byte changes. The consumer is named by the CTO (msg 4923): the portal's sections reader is tolerant and already reads computation_validation; the worker's record names every reader it finds.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p130_cells.py dry-run at base box/dell2 on dell2 2026-10-11 ~13:0xZ: AC1 FAIL (arm a not as expected; arms b, c, d as expected; 60 schema files in the registry), AC2 PASS (a bound: 2 failed, 203 passed), AC3 FAIL (no record); commit-gate clean. Measured at base: the two report fixtures carry no retained_ref, so arm (a) is validated without one and the Opal form's retained_ref is optional by the issuer's choice, as on the vendor form.
lane: the <paths> block IS the grant. Class WORLD by the L6 floor (its paths name infra/); it deploys nothing. The ratified-text signer 3.0.0_SA_CVO is told at issuance: the file is a contract file, and the form is PRD ADDENDUM v0.28 item 29.
</preflight>

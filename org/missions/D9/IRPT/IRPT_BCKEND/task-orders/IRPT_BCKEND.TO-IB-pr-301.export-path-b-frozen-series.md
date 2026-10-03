# TO IRPT_BCKEND.TO-IB-pr-301 -- P-6's server half: submit-export accepts a PATH B (platinum) Performance export, pins the series revision at submit, and the render reads exactly that version (nothing served)

<to_id>IRPT_BCKEND.TO-IB-pr-301</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~104</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-10-03</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>36</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** CTO RULINGS batch 201 (P-6: PATH A for 49 Financial retires whole in P-2's
window) and batch 203 (@6db3bdede2, msg 104531). Batch 203 ruled YES to 2.0.0_SA_COO~D's server half, with one amendment: the
export FREEZES the series it renders. Cut beside IB-pr-299 and IB-pr-300 in ROUND 36 (GATE (x), row S267). | **Decomp cell:**
`IB-pr-301` (decomposition section 28) | **outcome_ref:** P-6 (export survives the retirement) | **depends_on:** none (IRPT_DASHBD
DB-b-16's summary route and coverage check are merged)

---

## WORKER FACE

**Why.** After P-6, PATH A (`performance/retained.py`) no longer composes 49 Financial. A 49 Financial Performance export today
reads PATH A's retained report:
- `export/retained_export.py`, through `submit_service.py` and `submit_async.py`;
- packaged by `irpt-export-render`.
So the export must also accept a PATH B source. ~D's page half is being built to send it. The ruled shape is in
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/p6/P6_PRINT_EXPORT_PATH_B_PLAN.md`, section "Server half". Read it,
and read batch 203 in `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/RULINGS.md`.

**What you build.**
1. **Submit.** `submit-export` accepts a PATH B Performance export:
   `performance_source: {"path": "PLATINUM", "account_id": <acc_...>, "start": <YYYY-MM-DD>, "end": <YYYY-MM-DD>}`, with no
   retained report.
   - It is authorized by the reporting read route's per-account coverage check: the same `_check_covered` as
     `infra/aws/lambda/investor-reporting/reporting/entry.py`, against the submitter's resolved `permitted_account_set`.
   - An uncovered account is refused `OBJECT_NOT_COVERED`, and no bundle is written.
2. **Freeze (batch 203 item 1).** After coverage passes, the bundle pins the series as ONE immutable revision INSIDE
   `authorized_report_revisions`, carrying the account id, start, end, the platinum `series.json.gz` S3 `VersionId`, its sha256,
   and `series.as_of`.
   - No new top-level field is added.
   - Any additive change to the item shape is a version bump in `ExportBundle.schema.json` in this same cell. Update BOTH copies,
     `infra/aws/lambda/investor-reporting/_contracts/` and `docs/contracts/investor-reporting/v1/`; `test_packaged_contracts_match_docs`
     keeps them equal. Add the rule-24 record if an enum grows.
3. **Render (batch 203 item 2).** The render reads THAT EXACT VersionId, never the current object. Choose ONE carrier and name it
   in your report:
   - a version parameter on the reporting route, under the same coverage; or
   - the render role reading that one prefix by VersionId. A role grant is IAM text in
     `infra/aws/terraform/investor-reporting/export/` (not applied; it rides the window's never-widen half).
4. **`print_query` carries `account`** beside `kind=performance`, `start` and `end` for a PATH B export.
5. **Receipt (batch 203 item 3).** The receipt names the frozen `as_of`, so a publish that lands between preview and submit is
   visible.
6. **PATH A exports (retained reports, Cottonwood and anything not PLATINUM) are unchanged.**
7. **Tests.** Create `infra/aws/lambda/investor-reporting/export/tests/test_export_path_b.py`, at least 5 tests, naming `PLATINUM`,
   `VersionId`, `as_of` and `OBJECT_NOT_COVERED`:
   - a covered PATH B submit pins VersionId, sha256 and as_of inside `authorized_report_revisions`;
   - an uncovered account is refused with no bundle;
   - the render reads the pinned version when the current object differs (a stub S3 with two versions);
   - the receipt names the frozen as_of;
   - `print_query` carries the account;
   - a retained PATH A export is unchanged.

<criterion id="IB36-3-AC1" cell_refs="IB-pr-301"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r36/p36_pytest_floor.py" . IB36-3-AC1</invocation><expect>IB36-3-AC1 PASS</expect></criterion>
`IB36-3-AC1` -- the PATH B export tests pass (at least 5). Base: FAIL (no file).

<criterion id="IB36-3-AC2" cell_refs="IB-pr-301"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r36/p36_pytest_floor.py" . IB36-3-AC2</invocation><expect>IB36-3-AC2 PASS</expect></criterion>
`IB36-3-AC2` -- the whole export suite passes, at least 173 (168 at the base), 0 failed. It includes the check that both schema
copies agree. Base: FAIL (168).

<expected_criteria>IB36-3-AC1,IB36-3-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Workers IB-pr-299 (the performance adapter) and IB-pr-300 (the holdings producer's handler)
  are building beside you. Do not touch their files.
- **AWS:** none. No plan, no apply, no invoke, no S3 read or write. Tests use stubs.
- **Refusal clause.** A change to a retained (PATH A) export's behaviour, or an existing test that moves, is a defect: stop and
  file a row. A render that can read the current object instead of the pinned version is a defect. No client name in any record.

<paths>
infra/aws/lambda/investor-reporting/export/submit_service.py
infra/aws/lambda/investor-reporting/export/submit_async.py
infra/aws/lambda/investor-reporting/export/retained_export.py
infra/aws/lambda/investor-reporting/export/bundle.py
infra/aws/lambda/investor-reporting/export/dispatch.py
infra/aws/lambda/investor-reporting/export/render.py
infra/aws/lambda/investor-reporting/export/receipt.py
infra/aws/lambda/investor-reporting/export/handler.py
infra/aws/lambda/investor-reporting/export/entry.py
infra/aws/lambda/investor-reporting/export/tests/test_export_path_b.py
infra/aws/lambda/investor-reporting/_contracts/ExportBundle.schema.json
docs/contracts/investor-reporting/v1/ExportBundle.schema.json
infra/aws/lambda/investor-reporting/reporting/entry.py
infra/aws/terraform/investor-reporting/export/b2_render.tf
infra/aws/terraform/investor-reporting/export/iam.tf
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~104/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read without a grant (never written): `infra/aws/lambda/investor-reporting/`, `infra/aws/terraform/investor-reporting/`,
`docs/contracts/`, `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/p6/`, `lib/`.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 28 (round 36, workstream ~P), cell `IB-pr-301`.
<owned_cells>IB-pr-301</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB36-3-AC1, IB36-3-AC2. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~104/IRPT_BCKEND.TO-IB-pr-301.export-path-b-frozen-series.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IB36-3-AC1,IB36-3-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message must give:
- the commit hashes and each criterion's last line;
- the submit shape and its refusals;
- the frozen revision item and the schema version;
- the render's carrier (route parameter or role grant) with its text;
- the receipt field;
- any surprise row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the served export submit and render (irpt-export-render and the submit function), the ExportBundle contract (both copies), possibly the reporting read route and the render role's policy text; 0 served bytes move in the cell. The deploys, any route or role apply, and the page half land in P-2's window under its never-widen half; one rollback reverts both.
comp-iam: RUN -- only if the render reads by VersionId under its own role: a grant scoped to the platinum reporting prefix and s3:GetObjectVersion, never wider; text only.
comp-routes: RUN -- only if the reporting route gains a version parameter: the same route key, the same coverage; no new route.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- IB36-3-AC1 base FAIL (no file), IB36-3-AC2 base FAIL (168 < 173), dry-run at the base 2026-10-03 ~03:5xZ.
lane: the <paths> block IS the grant.
</preflight>

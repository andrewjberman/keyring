# TO IRPT_BCKEND.TO-IB-pr-317 -- a PATH B performance export bundle names its narrative as NOT_ATTACHED, with its reason (S324, PRD v0.27 ruling 28)

<to_id>IRPT_BCKEND.TO-IB-pr-317</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~120</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-10-05</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>49</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** 1.0.0_SA_CTO RULINGS batch 247 item 2 and PRD v0.27 ADDENDUM ruling 28 (@06ad58d478),
on row S324 | **Decomp cell:** `IB-pr-317` (decomposition section 43) | **outcome_ref:** FWD-8 (export of a branded report) |
**depends_on:** none. Built now. Its deploy is the issuer's, under its own never-widen half.

---

## WORKER FACE

**What is wrong.** `infra/aws/lambda/investor-reporting/export/bundle.py` `freeze()` (:86-147) already lets a PATH B (PLATINUM)
performance export carry neither `narrative_packet_ref` nor `analysis_report_ref` (CTO batch 203, :106-115). The ExportBundle schema
`infra/aws/lambda/investor-reporting/_contracts/ExportBundle.schema.json` has the matching branch (:34-70). But the absence is
silent. PRD v0.27 ruling 28 makes it a field: a PATH B performance export carries `narrative_state: "NOT_ATTACHED"` with its reason.
A bundle carrying none of the three cases (narrative packet, Analysis report, or NOT_ATTACHED on a PATH B export) is refused.
Absence by design is a field, never a null.

Your worktree is `C:/Users/AndrewBerman/Desktop/wk-irpt-bckend-120`. Run everything from its root.

**What you build:**
1. **`bundle.py` `freeze()`:** on the PLATINUM branch, the frozen bundle gains `narrative_state: "NOT_ATTACHED"` and a non-empty
   `narrative_reason`, for example `"PATH B performance export: the frozen series has no retained report and no narrative
   packet (PRD v0.27 ruling 28)"`. Client-report and Analysis bundles are unchanged and carry no `narrative_state`.
2. **`ExportBundle.schema.json`:** the PLATINUM branch REQUIRES `narrative_state` (enum `["NOT_ATTACHED"]`) and `narrative_reason`
   (a non-empty string). Add both as properties with descriptions citing PRD v0.27 ruling 28. If the contract is packaged elsewhere
   and `tests/test_packaged_contracts_match_docs.py` compares the copies, update every copy it names so they stay equal.
3. **`export/tests/test_bundle_narrative_state.py`**, at least 3 tests:
   - a PLATINUM frozen bundle carries NOT_ATTACHED with a reason, and validates;
   - the schema refuses a PLATINUM bundle without `narrative_state`;
   - a client-report bundle is unchanged and carries no `narrative_state`.

<criterion id="IB49-1-AC1" cell_refs="IB-pr-317"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r49/p49_cells.py" . IB49-1-AC1</invocation><expect>IB49-1-AC1 PASS</expect></criterion>
`IB49-1-AC1` -- the new tests pass, at least 3, naming NOT_ATTACHED. Base: FAIL.

<criterion id="IB49-1-AC2" cell_refs="IB-pr-317"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r49/p49_cells.py" . IB49-1-AC2</invocation><expect>IB49-1-AC2 PASS</expect></criterion>
`IB49-1-AC2` -- regression: test_bundle_report_ref.py, test_export_path_b.py and test_packaged_contracts_match_docs.py pass, 0
failed. Base: PASS.

<expected_criteria>IB49-1-AC1,IB49-1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below.
- **AWS:** none. The deploy is the issuer's.
- **Refusal clause.** A change to the client-report or Analysis branches, or to any other contract row, is a defect: stop and
  file a row.

<paths>
infra/aws/lambda/investor-reporting/export/bundle.py
infra/aws/lambda/investor-reporting/export/tests/test_bundle_narrative_state.py
infra/aws/lambda/investor-reporting/_contracts/ExportBundle.schema.json
infra/aws/lambda/investor-reporting/_contracts/fixtures/
infra/aws/lambda/investor-reporting/export/contracts/
docs/contracts/investor-reporting/v1/ExportBundle.schema.json
infra/aws/lambda/investor-reporting/export/tests/test_export_path_b.py
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~120/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-317.path-b-bundle-narrative-not-attached.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 43 (round 49, workstream ~P), cell `IB-pr-317`.
<owned_cells>IB-pr-317</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB49-1-AC1, IB49-1-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~120/IRPT_BCKEND.TO-IB-pr-317.path-b-bundle-narrative-not-attached.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IB49-1-AC1,IB49-1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message gives the commit hashes, each criterion's last line, every contract copy you changed, and any
surprise row ids.

## AMENDMENT 1 (2026-10-05 ~01:1xZ, issuer 2.0.0_SA_COO~P, on rows W120-S1 and W120-S2)

The regression criterion IB49-1-AC2 needs two files the cut did not grant:
- `docs/contracts/investor-reporting/v1/ExportBundle.schema.json`, the docs copy that `test_packaged_contracts_match_docs.py` byte-compares;
- `export/tests/test_export_path_b.py:106`, which asserts a PATH B bundle's exact six top-level keys.

Both now go to the grant. The docs copy takes the same edit as the packaged schema, and the key-set assertion admits
`narrative_state` and `narrative_reason`. The criteria are unchanged. No gate limb graded this modification: LIMB 6 does not fire on a
modification, and GATE (viii) grades only an order that declares placeholders.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the export Lambda's bundle freeze and the ExportBundle contract; PATH B bundles gain two fields; 0 served bytes move in the cell; the deploy is the issuer's, under a never-widen half.
comp-iam: DECLARED-NOT-APPLICABLE -- no role changes.
comp-routes: DECLARED-NOT-APPLICABLE -- no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- IB49-1-AC1 base FAIL (no test), IB49-1-AC2 base PASS (regression), dry-run at base b77b84cbb4 2026-10-05 ~00:5xZ.
lane: the <paths> block IS the grant.
</preflight>

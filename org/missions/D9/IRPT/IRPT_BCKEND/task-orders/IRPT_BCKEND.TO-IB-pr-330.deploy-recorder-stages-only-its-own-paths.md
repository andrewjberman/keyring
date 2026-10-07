# TO IRPT_BCKEND.TO-IB-pr-330 -- the deploy recorder stages only its own paths and never duplicates a CHANGELOG entry (row S344)

<to_id>IRPT_BCKEND.TO-IB-pr-330</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~133</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>61</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop (project placement; seat on dell2) | **Ordered by:** `1.0.0_SA_CTO~DELL2` round analysis rounds 47-60,
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_BCKEND_ROUNDS_47_60_20261007.md` @e363a194ed section 5, item E-P2 |
**Risk:** declared at the L6 floor its `<paths>` imply (an `infra/` path floors at WORLD, spine v3.19); the analysis's own class for E-P2 is in its section 5 | **Decomp cell:** `IB-pr-330` (decomposition section 54) | **outcome_ref:** row S344 (release records); no FWD moves directly | **depends_on:** none.

---

## WORKER FACE

**The defect (row IRPT_BCKEND-S344, held from the predecessor's r57 log, not re-measured).** `infra/aws/lambda/ci/record-terraform-deploy.sh`
swept the already-dirty `infra/aws/lambda/ci/source-map-reconcile-audit.jsonl` into its own commit; the lane gate refused that commit; each retry
appended another `infra/aws/terraform/investor-reporting/CHANGELOG.json` entry (r57: four duplicates of irpt-holdings). A later fix,
8be38c9dec (`0.7.0_AE_CloudOps~RV`, 2026-10-06: node first, quoted `$JSON_TOOL` sites), may already change the staging.

**What you build** (your worktree is `C:/dev/wk-irpt-bckend-133`; run everything from its root):

1. **Measure first.** Read how the recorder stages and commits at HEAD. Write `infra/aws/lambda/ci/tests/test_record_terraform_deploy_paths.sh` (new):
   it builds a throwaway git repo in a temp dir (never this repo), copies in the recorder and the minimum fixture files it needs
   (a fixture source map, a fixture CHANGELOG.json, a DIRTY fixture `source-map-reconcile-audit.jsonl`), runs the recorder there with
   a stub `aws`, and asserts (a) the recorder's commit carries only the recorder's own output paths, not the dirty audit file, and
   (b) running it a second time for the same deploy (a forced retry) leaves exactly ONE CHANGELOG entry for that deploy.
2. **If HEAD already passes both**, commit the test only and say so in your report (the CTO's clause: the cell closes on that read with
   no code). **Otherwise** change `record-terraform-deploy.sh` minimally so both pass: stage by explicit pathspec, and make the
   CHANGELOG append idempotent per deploy identity.
3. Never run the recorder against this repository's real source map or CHANGELOG.

<criterion id="IB61-2-AC1" cell_refs="IB-pr-330"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r61/p61_cells.py" . IB61-2-AC1</invocation><expect>IB61-2-AC1 PASS</expect></criterion>
`IB61-2-AC1` -- the new test passes (own paths only; a forced retry adds no second CHANGELOG entry). Base: FAIL (no test).

<criterion id="IB61-G-133" cell_refs="IB-pr-330"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r61/p61_cells.py" . IB61-G-133</invocation><expect>IB61-G-133 PASS</expect></criterion>
`IB61-G-133` -- a GUARD: your commits touch only your grant. Base: PASS.

<expected_criteria>IB61-2-AC1,IB61-G-133</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, and nothing else.
- **HOLD (laptop `1.0.0_SA_CTO` ruling A, 2026-10-07 08:5xZ):** nothing you produce, land or grade may carry a date before 2024-01-01
  through `lib/trading_calendar.py` on this box. Use 2026 dates in every test and fixture.
- **No vendor call, ever.** No call off Opal infrastructure.
- **A test that fails for a reason you did not cause** is a surprise row and a stop on that criterion, never an edit to another test.
- Every invocation finishes inside 120 s; scope it so it does.
- **Refusal clause.** Running the recorder against the real `lambda-source-map.json` or `CHANGELOG.json`, or an AWS write, is a defect: stop and file a row.

<paths>
infra/aws/lambda/ci/record-terraform-deploy.sh
infra/aws/lambda/ci/tests/test_record_terraform_deploy_paths.sh
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~133/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-330.deploy-recorder-stages-only-its-own-paths.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 54 (round 61, workstream ~P), cell `IB-pr-330`.
<owned_cells>IB-pr-330</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB61-2-AC1, IB61-G-133. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~133/IRPT_BCKEND.TO-IB-pr-330.deploy-recorder-stages-only-its-own-paths.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IB61-2-AC1,IB61-G-133` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message gives the commit hashes, each criterion's last line, any suite's last line, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- nothing is deployed by this order; any release is the issuer's after the drain.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS permission is added.
comp-routes: DECLARED-NOT-APPLICABLE -- no route or CloudFront behaviour changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- every criterion dry-run at base 6e462d3499 2026-10-07 ~09:0xZ: build checks FAIL, guards PASS (p61_cells.py).
lane: the <paths> block IS the grant.
</preflight>

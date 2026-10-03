# TO IRPT_BCKEND.TO-IB-pr-310 -- the source map records the live code of irpt-ycharts-generate, irpt-holdings and irpt-status

<to_id>IRPT_BCKEND.TO-IB-pr-310</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~113</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-10-03</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>44</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** CTO RULINGS batch 234 item 1 (msg 104804, @a5c484c7cb): "S264:
record-terraform-deploy.sh already takes --function (14346d1f09). Run it per function for irpt-ycharts-generate (after irpt-y5v D1),
irpt-holdings and irpt-status; close on deployed_code_sha256 equal to live." The irpt-y5v-20261003 ledger's D1 closed at
22:12:32Z. | **Decomp cell:** `IB-pr-310` (decomposition section 37) | **outcome_ref:** row S264 (the source map names the running
code) | **depends_on:** none.

---

## WORKER FACE

**What is wrong.** `infra/aws/lambda/ci/lambda-source-map.json` still records the 2026-09-24 deploys of three functions. Each has
since been re-deployed, so its row's `deployed_code_sha256` differs from the code that is live.

Your worktree is `C:/Users/AndrewBerman/Desktop/wk-irpt-bckend-113`. Run everything from its root.

**What you do, once per function** (irpt-ycharts-generate, irpt-holdings, irpt-status, one at a time):
1. Read the live hash:
   `python -c "import boto3;print(boto3.client('lambda',region_name='us-east-1').get_function_configuration(FunctionName='<fn>')['CodeSha256'])"`
2. Run the recorder with that function only and that hash:
   `bash infra/aws/lambda/ci/record-terraform-deploy.sh investor-reporting --function <fn> --code-sha256 <hash> --author "0.9.0_WK_IRPT_BCKEND~113 <0.9.0_WK_IRPT_BCKEND~113@opal.agent>"`
   - The recorder commits its own changes (source map, the pipeline's CHANGELOG, the reconcile audit) through safe-commit.
   - Read its output. It must name exactly one function in "Resolved deployment set". It must not print `HALF-LANDED`.
   - If it refuses or names another function, stop and file a row. Do not edit the source map by hand.

<criterion id="IB44-2-AC1" cell_refs="IB-pr-310"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r44/p44_record_three_functions.py" . IB44-2-AC1</invocation><expect>IB44-2-AC1 PASS</expect></criterion>
`IB44-2-AC1` -- each of the three rows' `deployed_code_sha256` equals the function's live CodeSha256, read when the check runs.
Base: FAIL.

<criterion id="IB44-2-AC2" cell_refs="IB-pr-310"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r44/p44_record_three_functions.py" . IB44-2-AC2</invocation><expect>IB44-2-AC2 PASS</expect></criterion>
`IB44-2-AC2` -- a GUARD: against base 80ba60328c, no other function row changes, and no row is added or removed. Base: PASS.

<expected_criteria>IB44-2-AC1,IB44-2-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below.
- **AWS:** reads only: the Lambda configuration reads above and the recorder's own reconcile reads. No apply, no S3 or Lambda write.
- **Refusal clause.** A hand edit of the source map, a `--all` run, or a run without `--function` is a defect: stop and file a row.

<paths>
infra/aws/lambda/ci/lambda-source-map.json
infra/aws/terraform/investor-reporting/CHANGELOG.json
infra/aws/lambda/ci/source-map-reconcile-audit.jsonl
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~113/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 37 (round 44, workstream ~P), cell `IB-pr-310`.
<owned_cells>IB-pr-310</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB44-2-AC1, IB44-2-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~113/IRPT_BCKEND.TO-IB-pr-310.source-map-records-three-functions.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IB44-2-AC1,IB44-2-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message gives the commit hashes, each recorder run's "Resolved deployment set" line and reconcile line, each
criterion's last line, and any surprise row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- infra/aws/lambda/ci/lambda-source-map.json rows irpt-ycharts-generate, irpt-holdings, irpt-status (the drift consumer verify-local.sh reads them); a record only, 0 served bytes move; live CodeSha256 at the cut: jKsI7pZW (ycharts-generate, after irpt-y5v D1), tS/APci3 (holdings), hC6Pramt (status).
comp-iam: DECLARED-NOT-APPLICABLE -- reads only.
comp-routes: DECLARED-NOT-APPLICABLE -- no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- IB44-2-AC1 base FAIL (all three differ), IB44-2-AC2 base PASS (guard), dry-run at base 80ba60328c 2026-10-03 ~22:5xZ.
lane: the <paths> block IS the grant.
</preflight>

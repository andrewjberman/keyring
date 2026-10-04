# TO IRPT_BCKEND.TO-IB-pr-312 -- the 49F producer row names its live role, and the Inflection producer gains its source-map row

<to_id>IRPT_BCKEND.TO-IB-pr-312</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~115</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-10-04</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>46</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** row W114-S1 (IB-pr-311 amendment 1 carried these two steps); `1.0.0_SA_CTO`
msg 104879: the naming gate @7de9db9085 admits the whole edit after the CVO's rulings (msgs 104877 and @7b38f056ca), "steps 1-2 may
land; keep tf_file in the inf row". | **Decomp cell:** `IB-pr-312` (decomposition section 39) | **outcome_ref:** rows S293 and
W114-S1 | **depends_on:** none. WORLD is the gate floor for the source map; a record only.

---

## WORKER FACE

**What is wrong.** In `infra/aws/lambda/ci/lambda-source-map.json`, the `irpt-holdings-performance-lambda` row names
`iam_role: irpt-holdings-performance-role`, but the live role is `irpt-49f-holdings-performance-role`. The Inflection producer
`irpt-inf-holdings-performance-lambda` runs the same artifact (live CodeSha256 `0PuFBxdJSbFHNJ9+Z3weyzLvXyZhgZFk2dkGAbIYb/0=`,
role `irpt-inf-holdings-performance-role`), and it has no row.

Your worktree is `C:/Users/AndrewBerman/Desktop/wk-irpt-bckend-115`. Run everything from its root.

**What you do, in order:**
1. **The edit.** A tested script exists: `C:/Users/ANDREW~1/AppData/Local/Temp/claude/C--Users-AndrewBerman-Desktop-ajb-workspace/f93b4325-6e92-4916-aeeb-f7fa7012b408/scratchpad/w114_edit.py`.
   Read it first. Run it from the worktree root, without arguments first: it must print `roundtrip variants matching: 1` or more,
   meaning it rewrites the file byte-identically. Then run it with `--apply`. It does three things:
   - sets the 49F row's `iam_role` to `irpt-49f-holdings-performance-role`;
   - inserts the Inflection row right after the 49F row, as a copy of it with `tf_resource`
     `module.irpt_holdings_performance_inf.aws_lambda_function.this`, `iam_role` `irpt-inf-holdings-performance-role` and an
     IB-er-501 `_build_note`, keeping `tf_file`;
   - drops the copy's deploy-record fields.
   Then `git diff --stat` shows only the source map. Commit it with safe-commit. The naming limb must read PASS; if it refuses,
   stop and file a row.
2. **Record the Inflection function.** Read its live hash:
   `python -c "import boto3;print(boto3.client('lambda',region_name='us-east-1').get_function_configuration(FunctionName='irpt-inf-holdings-performance-lambda')['CodeSha256'])"`
   Then run, with a timeout of at least 900 s:
   `bash infra/aws/lambda/ci/record-terraform-deploy.sh investor-reporting --function irpt-inf-holdings-performance-lambda --code-sha256 <hash> --author "0.9.0_WK_IRPT_BCKEND~115 <0.9.0_WK_IRPT_BCKEND~115@opal.agent>"`
   Its "Resolved deployment set" names exactly that function, and it must not print `HALF-LANDED`. Afterwards
   `git status --porcelain` shows nothing staged. If the recorder's own commit did not land, commit its written files with
   safe-commit and say so.

<criterion id="IB46-1-AC1" cell_refs="IB-pr-312"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r46/p46_performance_rows_complete.py" . IB46-1-AC1</invocation><expect>IB46-1-AC1 PASS</expect></criterion>
`IB46-1-AC1` -- read against live: the adapter, the 49F producer and the Inflection producer rows each carry `deployed_code_sha256`
and `iam_role` equal to live; the Inflection row's `tf_resource` is its module address and its `tf_file` equals the 49F row's.
Base: FAIL.

<criterion id="IB46-1-AC2" cell_refs="IB-pr-312"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r46/p46_performance_rows_complete.py" . IB46-1-AC2</invocation><expect>IB46-1-AC2 PASS</expect></criterion>
`IB46-1-AC2` -- a GUARD: against base 7de9db9085, no row other than the 49F and Inflection rows changes, and the only row added is
the Inflection one. Base: PASS.

<criterion id="IB46-1-AC3" cell_refs="IB-pr-312"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r46/p46_performance_rows_complete.py" . IB46-1-AC3</invocation><expect>IB46-1-AC3 PASS</expect></criterion>
`IB46-1-AC3` -- a GUARD: `.tools/comp-lambdamap check` reports no finding beyond the 14 at the base. Base: PASS.

<expected_criteria>IB46-1-AC1,IB46-1-AC2,IB46-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below.
- **AWS:** reads only: the Lambda configuration read above and the recorder's own reconcile reads.
- **Refusal clause.** A `--all` run, a run without `--function`, or a hand edit beyond the script's three changes is a defect:
  stop and file a row.

<paths>
infra/aws/lambda/ci/lambda-source-map.json
infra/aws/terraform/investor-reporting/CHANGELOG.json
infra/aws/lambda/ci/source-map-reconcile-audit.jsonl
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~115/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-312.performance-rows-role-and-inflection-entry.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 39 (round 46, workstream ~P), cell `IB-pr-312`.
<owned_cells>IB-pr-312</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB46-1-AC1, IB46-1-AC2, IB46-1-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~115/IRPT_BCKEND.TO-IB-pr-312.performance-rows-role-and-inflection-entry.proof_of_spec.json`.
It names row W114-S1 as resolved by this order. Validate it with `python .tools/proof-of-spec-check.py <instance> IB46-1-AC1,IB46-1-AC2,IB46-1-AC3`
BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message gives the commit hashes, the naming limb's line from the edit commit, the recorder's "Resolved
deployment set" and reconcile lines, each criterion's last line, and any surprise row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- infra/aws/lambda/ci/lambda-source-map.json: the 49F producer row's iam_role and a new irpt-inf-holdings-performance-lambda row; a record only, 0 served bytes move; live at the cut: 0PuFBxdJ (both producers), roles irpt-49f-holdings-performance-role and irpt-inf-holdings-performance-role; the naming gate @7de9db9085 reads the edit PASS (CTO msg 104879).
comp-iam: DECLARED-NOT-APPLICABLE -- reads only; iam_role is a record of the live role, not a grant.
comp-routes: DECLARED-NOT-APPLICABLE -- no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- IB46-1-AC1 base FAIL (49F iam_role != live), IB46-1-AC2 base PASS, IB46-1-AC3 base PASS (14 of 14), dry-run at base 7de9db9085 2026-10-04 ~02:2xZ.
lane: the <paths> block IS the grant.
</preflight>

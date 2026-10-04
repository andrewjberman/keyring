# TO IRPT_BCKEND.TO-IB-pr-311 -- the source map records what runs for the performance adapter and both holdings-performance producers

<to_id>IRPT_BCKEND.TO-IB-pr-311</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~114</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-10-04</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>45</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** row IRPT_BCKEND-S293 (owner 2.0.0_SA_COO~P: "run record-terraform-deploy.sh for
both applies, add the Inflection function's entry (it shares the producer artifact by design), and correct the iam_role field");
CTO batch 234 item 1 names S293 as the same class as S264; CVO grade @e73818b94f re-reads it as open. | **Decomp cell:**
`IB-pr-311` (decomposition section 38) | **outcome_ref:** row S293 | **depends_on:** none. WORLD is the gate floor for the
source map; a record only, no served bytes move.

---

## WORKER FACE

**What is wrong.** `infra/aws/lambda/ci/lambda-source-map.json` does not record what runs for three functions. Live values at
the cut (us-east-1):
- `irpt-performance-adapter`: live CodeSha256 `NU6YVERLJ0i6qmazBYWUF+1xVDPGHwdMKqQ5vgjmVc4=`. The row's `deployed_code_sha256` is
  still the 09-24 value.
- `irpt-holdings-performance-lambda` (49 Financial): live CodeSha256 `0PuFBxdJSbFHNJ9+Z3weyzLvXyZhgZFk2dkGAbIYb/0=`, live role
  `irpt-49f-holdings-performance-role`. The row has no `deployed_code_sha256`, and its `iam_role` reads
  `irpt-holdings-performance-role`.
- `irpt-inf-holdings-performance-lambda` (Inflection): it runs the same artifact (CodeSha256 `0PuFBxdJ..`) with role
  `irpt-inf-holdings-performance-role`, and it has NO row.

Your worktree is `C:/Users/AndrewBerman/Desktop/wk-irpt-bckend-114`. Run everything from its root.

**What you do, in order:**
1. **Correct the 49F role.** In the `irpt-holdings-performance-lambda` row, set `iam_role` to `irpt-49f-holdings-performance-role`.
   Change nothing else by hand in that row.
2. **Add the Inflection row** `irpt-inf-holdings-performance-lambda`, directly after the 49F row. It shares the 49F function's
   artifact by design (`infra/aws/terraform/investor-reporting/holdings-performance/lambda.tf:67-86`: `artifact_key` is the 49F
   zip). Build it as a copy of the 49F row with these differences:
   - `tf_resource`: `module.irpt_holdings_performance_inf.aws_lambda_function.this`;
   - `iam_role`: `irpt-inf-holdings-performance-role`;
   - `_build_note`: one sentence naming IB-er-501 (the Inflection producer) and stating that it shares
     `investor-reporting/irpt-holdings-performance-lambda.zip` with the 49F row by design (row S293);
   - drop `last_deployed_commit`, `last_deployed_at`, `deployed_code_sha256` and `recorded_by`. The recorder writes those.
   Keep `source_dir`, `files`, `staged_from`, `_staged_from_note`, `tf_file`, `pipeline`, `artifact_s3_key` and `artifact_sha256`
   equal to the 49F row's values. Commit steps 1 and 2 together.
3. **Record each function, one run each** (irpt-performance-adapter, irpt-holdings-performance-lambda,
   irpt-inf-holdings-performance-lambda). Read the live hash:
   `python -c "import boto3;print(boto3.client('lambda',region_name='us-east-1').get_function_configuration(FunctionName='<fn>')['CodeSha256'])"`
   Then run:
   `bash infra/aws/lambda/ci/record-terraform-deploy.sh investor-reporting --function <fn> --code-sha256 <hash> --author "0.9.0_WK_IRPT_BCKEND~114 <0.9.0_WK_IRPT_BCKEND~114@opal.agent>"`
   - Give each run a timeout of at least 900 s. A previous worker's `timeout 300` cut a run off before its commit.
   - Its "Resolved deployment set" names exactly one function, and it must not print `HALF-LANDED`. If it refuses, stop and
     file a row.
   - After each run, `git status --porcelain` shows nothing staged. If the recorder's own commit did not land, commit its
     written files yourself with safe-commit and say so.

<criterion id="IB45-1-AC1R" cell_refs="IB-pr-311"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r45/p45_performance_rows_recorded.py" . IB45-1-AC1R</invocation><expect>IB45-1-AC1R PASS</expect></criterion>
`IB45-1-AC1R` -- read against live: irpt-performance-adapter and irpt-holdings-performance-lambda each carry `deployed_code_sha256` =
live CodeSha256. Base: FAIL. (Amendment 1 replaces IB45-1-AC1; see below.)

<criterion id="IB45-1-AC2" cell_refs="IB-pr-311"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r45/p45_performance_rows_recorded.py" . IB45-1-AC2</invocation><expect>IB45-1-AC2 PASS</expect></criterion>
`IB45-1-AC2` -- a GUARD: against base ad781b948a, no other row changes, and the only row added is the Inflection one. Base: PASS.

<criterion id="IB45-1-AC3" cell_refs="IB-pr-311"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r45/p45_performance_rows_recorded.py" . IB45-1-AC3</invocation><expect>IB45-1-AC3 PASS</expect></criterion>
`IB45-1-AC3` -- a GUARD: `.tools/comp-lambdamap check` reports no finding beyond the 14 at the base. Base: PASS.

<expected_criteria>IB45-1-AC1R,IB45-1-AC2,IB45-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below.
- **AWS:** reads only: the Lambda configuration reads above and the recorder's own reconcile reads. No apply, no S3 or Lambda write.
- **Refusal clause.** A `--all` run, a run without `--function`, or a hand edit of any field other than the two named in steps
  1-2 is a defect: stop and file a row.

<paths>
infra/aws/lambda/ci/lambda-source-map.json
infra/aws/terraform/investor-reporting/CHANGELOG.json
infra/aws/lambda/ci/source-map-reconcile-audit.jsonl
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~114/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-311.performance-rows-record-what-runs.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 38 (round 45, workstream ~P), cell `IB-pr-311`.
<owned_cells>IB-pr-311</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB45-1-AC1R, IB45-1-AC2, IB45-1-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~114/IRPT_BCKEND.TO-IB-pr-311.performance-rows-record-what-runs.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IB45-1-AC1R,IB45-1-AC2,IB45-1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message gives the commit hashes, each recorder run's "Resolved deployment set" and reconcile lines, each
criterion's last line, and any surprise row ids.

## AMENDMENT 1 (2026-10-04 ~01:5xZ, issuer 2.0.0_SA_COO~P, on row W114-S1)

safe-commit's naming limb (`.tools/naming-gate.py`, ENFORCE since `org/mcp/naming-gate.enforce`) refuses steps 1-2. The live
names `irpt-49f-holdings-performance-role` and the Inflection row's three `inf` strings are new firm-token literals in a JSON
string, outside every permitted context. The gate admits a new literal only through an R20 declared exception, which Andrew
acknowledges, or a context carve-out such as the source map's `packaged_as` names (0.0.0_AB_MSTR, 2026-09-23). Neither is
this order's to make.

- **Removed from this order:** step 1 (the 49F `iam_role` correction), step 2 (the Inflection row) and the Inflection recorder
  run. They are carried on row W114-S1, and the gate question goes to `1.0.0_SA_CTO`.
- **Kept:** the two recorder runs that landed: irpt-performance-adapter @c64bd53784 and irpt-holdings-performance-lambda
  @37090d00b1.
- **The build criterion** IB45-1-AC1 becomes IB45-1-AC1R (those two deploy records = live). AC2 and AC3 are unchanged.
- **Gate limb.** This is a modification with `<placeholders>NONE</placeholders>`. `.tools/to-pipeline-gate.py` LIMB 6 does not
  fire on a modification, and GATE (viii) grades only an order that declares placeholders, so no gate limb grades it.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- infra/aws/lambda/ci/lambda-source-map.json rows irpt-performance-adapter, irpt-holdings-performance-lambda and a new irpt-inf-holdings-performance-lambda (the drift consumer verify-local.sh and comp-lambdamap read them); a record only, 0 served bytes move; live at the cut: NU6YVERL (adapter), 0PuFBxdJ (both producers), roles irpt-49f-holdings-performance-role and irpt-inf-holdings-performance-role.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only; the iam_role field is a record of the live role, not a grant.
comp-routes: DECLARED-NOT-APPLICABLE -- no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- IB45-1-AC1 base FAIL (adapter YPSX1+ != live NU6YVERL), IB45-1-AC2 base PASS, IB45-1-AC3 base PASS (14 of 14 findings at the base; the check runs comp-lambdamap through Git Bash, since a bare bash resolves to WSL here and read 0), dry-run at base ad781b948a 2026-10-04 ~01:2xZ.
lane: the <paths> block IS the grant.
</preflight>

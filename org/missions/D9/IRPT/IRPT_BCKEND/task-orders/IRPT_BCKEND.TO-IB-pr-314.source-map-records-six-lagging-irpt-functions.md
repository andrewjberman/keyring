# TO IRPT_BCKEND.TO-IB-pr-314 -- the source map records the live code of the six investor-reporting functions that lag it (E3, S178)

<to_id>IRPT_BCKEND.TO-IB-pr-314</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~117</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-10-04</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>47</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** 1.0.0_SA_CTO ROUND ANALYSIS rounds 42-46 (msg 104972) section 3 item E3:
"S178 by batch 234's class rule: the recorder runs --function for every IRPT function whose source map lags live." The CTO
classes it LOCAL. WORLD is the gate floor for the source map, and this is a record only. | **Decomp cell:** `IB-pr-314`
(decomposition section 40) | **outcome_ref:** row S178 | **depends_on:** none.

---

## WORKER FACE

**What is wrong.** Six investor-reporting rows in `infra/aws/lambda/ci/lambda-source-map.json` do not record the code that is live.
Read at the cut (2026-10-04 ~21:2xZ):

| function | map deployed_code_sha256 | live CodeSha256 |
|---|---|---|
| irpt-directory-refresh | d5fqVJ0f.. | DXuzx9jp.. |
| irpt-directory-search | o9Qu0Jm7.. | AVSIaHEh.. |
| irpt-export-render | none | WDAv+kWK.. |
| irpt-holdings-refresh-lambda | none | SGwrvwLH.. |
| irpt-intake-poller | none | YpE2MyUw.. |
| irpt-narrative | none | es/S9azu.. |

Do NOT touch `irpt-ycharts-generate`. It also lags, but it is `2.0.0_SA_COO~Y`'s moving row (S320).

Your worktree is `C:/Users/AndrewBerman/Desktop/wk-irpt-bckend-117`. Run everything from its root.

**What you do, once per function, one at a time:**
1. Read the live hash:
   `python -c "import boto3;print(boto3.client('lambda',region_name='us-east-1').get_function_configuration(FunctionName='<fn>')['CodeSha256'])"`
2. Run the recorder with a timeout of at least 900 s:
   `bash infra/aws/lambda/ci/record-terraform-deploy.sh investor-reporting --function <fn> --code-sha256 <hash> --author "0.9.0_WK_IRPT_BCKEND~117 <0.9.0_WK_IRPT_BCKEND~117@opal.agent>"`
   - Its "Resolved deployment set" names exactly that function, and it must not print `HALF-LANDED`.
   - Afterwards `git status --porcelain` shows nothing staged. If the recorder's own commit did not land, commit its written
     files yourself with safe-commit and say so.
   - If the recorder refuses a function (for example "no functions{} entry" or a pipeline mismatch), stop on that one function,
     file a row naming the refusal, and go on to the next.

<criterion id="IB47-2-AC1" cell_refs="IB-pr-314"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r47/p47_e3_recorder.py" . IB47-2-AC1</invocation><expect>IB47-2-AC1 PASS</expect></criterion>
`IB47-2-AC1` -- the six rows each carry `deployed_code_sha256` = the live CodeSha256, read when the check runs. Base: FAIL.

<criterion id="IB47-2-AC2" cell_refs="IB-pr-314"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r47/p47_e3_recorder.py" . IB47-2-AC2</invocation><expect>IB47-2-AC2 PASS</expect></criterion>
`IB47-2-AC2` -- a GUARD: against base 2fd59da001, no row outside the six changes (irpt-ycharts-generate excepted as ~Y's), and none is
added or removed. Base: PASS.

<criterion id="IB47-2-AC3" cell_refs="IB-pr-314"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r47/p47_e3_recorder.py" . IB47-2-AC3</invocation><expect>IB47-2-AC3 PASS</expect></criterion>
`IB47-2-AC3` -- a GUARD: comp-lambdamap check reports no finding beyond the 14 at the base. Base: PASS.

<expected_criteria>IB47-2-AC1,IB47-2-AC2,IB47-2-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below.
- **AWS:** reads only: the Lambda configuration reads and the recorder's own reconcile reads.
- **Refusal clause.** A `--all` run, a run without `--function`, a hand edit of the source map, or any change to
  irpt-ycharts-generate's row is a defect: stop and file a row.

<paths>
infra/aws/lambda/ci/lambda-source-map.json
infra/aws/terraform/investor-reporting/CHANGELOG.json
infra/aws/lambda/ci/source-map-reconcile-audit.jsonl
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~117/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-314.source-map-records-six-lagging-irpt-functions.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 40 (round 47, workstream ~P), cell `IB-pr-314`.
<owned_cells>IB-pr-314</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB47-2-AC1, IB47-2-AC2, IB47-2-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~117/IRPT_BCKEND.TO-IB-pr-314.source-map-records-six-lagging-irpt-functions.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IB47-2-AC1,IB47-2-AC2,IB47-2-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message gives the commit hashes, each recorder run's "Resolved deployment set" and reconcile lines, each
criterion's last line, and any surprise row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- infra/aws/lambda/ci/lambda-source-map.json: six investor-reporting rows; a record only, 0 served bytes move; the lag census at the cut read 15 IRPT rows: 5 in parity, 7 lagging (six here, plus irpt-ycharts-generate = ~Y's S320), and 3 rows naming no live function (irpt-reporting-gold/publish/read-lambda; the live names carry 49f), which is filed as its own row and is not this cell's.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only.
comp-routes: DECLARED-NOT-APPLICABLE -- no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- IB47-2-AC1 base FAIL (six lag), IB47-2-AC2 base PASS, IB47-2-AC3 base PASS (14 of 14), dry-run at base 2fd59da001 2026-10-04 ~21:3xZ.
lane: the <paths> block IS the grant.
</preflight>

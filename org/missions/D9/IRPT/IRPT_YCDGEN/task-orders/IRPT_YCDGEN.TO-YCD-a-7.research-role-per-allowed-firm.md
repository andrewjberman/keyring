# IRPT_YCDGEN task order -- `YCD-a-7` -- ROUND 7: ONE RESEARCH ROLE PER ALLOWED FIRM (row D2-S19)

<to_id>IRPT_YCDGEN.TO-YCD-a-7.research-role-per-allowed-firm</to_id>
<issued_to>0.9.0_WK_IRPT_YCDGEN~9</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<placeholders>NONE</placeholders>
<round>7</round>
<workstream>R7_RESEARCH_ROLES</workstream>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

## THE CELL

The Opal engine writes its research answers on a per-firm principal, `irpt-<firm>-ycharts-research-role`, which the resident runner
role assumes. Today only cottonwood's role exists, so an Opal request for any other firm fails on `sts:AssumeRole`.

`infra/aws/terraform/investor-reporting/ycharts/resident.tf` (lines about 186-265) builds every research role, its policy, and the
runner's `AssumeTheFirmResearchPrincipal` list `for_each` over `local.ycdgen_firms`. That local is the `firms` list of policy row
`irpt-ycdgen-research-v1` in `infra/logic/registry/reporting_policies.json`. The row names `["cottonwood"]`.

1. **Widen the row.** Set `firms` of `irpt-ycdgen-research-v1` to `["cottonwood", "49financial", "inflection"]`, in that order.
   - These are the firms on the generate path's allow list. Each has an enabled client FIRM scope with its own bucket in
     `infra/logic/registry/scopes.json`.
   - Change nothing else in the row or the file, and keep the file's formatting byte-preserving.
2. **Every code reader of that row's firm list.** Search the repo for `irpt-ycdgen-research-v1` and for readers of its `firms`, with
   the native Grep tool, over `infra/` and `lib/`. For each reader, make sure three firms behave:
   - the research runner chooses the firm's OWN role ARN by firm (see
     `infra/aws/lambda/investor-reporting/ycharts/research/tests/test_runner.py:327`, which asserts the cottonwood ARN);
   - no reader assumes a single firm.

   Add one test in `infra/aws/lambda/investor-reporting/ycharts/research/tests/test_runner.py`: for each of the three firms, the
   assumed RoleArn names that firm's own role, and never another firm's. If a reader outside `<paths>` needs a change, stop and file
   a row.
3. **No Terraform change is expected.** The roles, policies and assume list follow the row. If you find a statement that hard-codes
   cottonwood, file a row and do not edit the `.tf`: the issuer rules on it.

## ACCEPTANCE (worktree root, after your last commit)

<criterion id="R7-AC1" cell_refs="YCD-a-7"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r7/r7_checks.py firms</invocation><expect>^R7-FIRMS-OK</expect></criterion>

<criterion id="R7-AC2" cell_refs="YCD-a-7"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r7/r7_checks.py fence</invocation><expect>^R7-FENCE-OK firms=3</expect></criterion>

<criterion id="R7-AC3" cell_refs="YCD-a-7"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r7/r7_checks.py regress</invocation><expect>^R7-REGRESS-OK</expect></criterion>

<expected_criteria>R7-AC1,R7-AC2,R7-AC3</expected_criteria>

Issuer dry run at box/dell2 (base):

| criterion | reads at base | meaning |
|---|---|---|
| AC1 | FAIL, `firms=['cottonwood']` | the row is not yet widened |
| AC2 | `R7-FENCE-OK firms=1` | it must read `firms=3` |
| AC3 | OK | base red set: the two custody files; allow at least 600 s |

## BOUNDS

- **Grant.** The `<paths>` block only. No terraform plan or apply, no AWS calls, no installs.
- Every `.py` edit passes `.tools/commit-gate.sh`.
- **Refusal clause.** If a criterion cannot be met as written: stop, file a row, report, and do not weaken a check.
- **Rows** are `IRPT_YCDGEN-D2-W9-S<k>`. APPEND a `## <id>` heading plus one fenced json block at the END of
  `org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md`. Gate:
  `python .tools/surprise-row-gate.py --check <path>`.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_YCDGEN~9" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_YCDGEN~9@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_YCDGEN~9 <0.9.0_WK_IRPT_YCDGEN~9@opal.agent>" -F <msgfile> -- <paths>`.
  - Write the message file with the Write tool. Do not pre-`git add`.
  - ASCII only. Use the native Grep/Glob/Read tools.
  - `reporting_policies.json` is a registry file. If owned-paths refuses it, commit it alone with
    `GIT_COMMIT_AUTHOR_OVERRIDE=<the lane the refusal names>` (audited), and name the lane in your report.

<paths>
infra/logic/registry/reporting_policies.json
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_runner.py
infra/aws/lambda/investor-reporting/ycharts/research/runner.py
org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~9/
org/missions/D9/IRPT/IRPT_YCDGEN/task-orders/IRPT_YCDGEN.TO-YCD-a-7.research-role-per-allowed-firm.md
org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R7.md</decomp_doc>
<owned_cells>YCD-a-7</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: R7-AC1, R7-AC2, R7-AC3. Instance at
`org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~9/IRPT_YCDGEN.TO-YCD-a-7.research-role-per-allowed-firm.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_YCDGEN.TO-YCD-a-7.research-role-per-allowed-firm`.
- Validate with `python .tools/proof-of-spec-check.py <instance> R7-AC1,R7-AC2,R7-AC3` BEFORE the flip to complete.
</proof_of_spec>

**REPORT (final message):**
- each criterion's output lines;
- every reader of the row's firm list, and what it does with three firms;
- the new test's name;
- any lane override;
- commits and row ids.

<!-- ===================== RECORD FACE ===================== -->

<preflight>
comp-blast: RUN (by reading) -- one registry row's firms list; resident.tf derives +2 research roles, +2 policies and the runner's assume list (3 explicit ARNs) from it at the next plan. reporting_policies.json is also staged in irpt-ycharts-generate (a changed member at that function's next release census). Nothing applies in this cell; the apply is the applier's never-widen pair.
comp-iam: RUN -- the derived change is IAM: two new firm-scoped roles (copies of cottonwood's, each on its own bucket) and the runner's AssumeRole list. The pair's CTO half reads the plan's policy diff and a simulate showing each role DENIED on the other firms' buckets (CTO ruling @f29d0d8ca1 condition 3).
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger is added or read.
comp-adversary: RUN -- read resident.tf :22-30, :186-265 and the registry rows (the policy row firms=['cottonwood']; scopes for cot/49f/inf, each with its own bucket); CloudTrail and IAM evidence of row D2-S19. Traps: a wildcard assume, a cross-firm prefix, a reader assuming one firm, a typed role name. AC2 (fence) and the pair's simulate cover the cross-firm arm.
lane: R7_RESEARCH_ROLES (the research roles' registry row and the runner's role choice).
</preflight>

Source: CTO ruling @f29d0d8ca1 (msg 3019); row IRPT_YCDGEN-D2-S19 @31b9816847; decomposition R7.

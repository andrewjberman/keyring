# TO IRPT_BCKEND.TO-IB-pr-422 -- the adapter role's two vendor session-read policies no longer depend on the retired plan variable; Terraform PLAN ONLY; packet

<to_id>IRPT_BCKEND.TO-IB-pr-422</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~283</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>120</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2` msg 4488 (ruling on this seat's msg 4485; row `IRPT_BCKEND-D2-W282-S1`) | **Decomp cell:** `IB-pr-422` (decomposition section 113) | **outcome_ref:** FWD-2

---

## WORKER FACE

Root: `C:/dev/wk-irpt-bckend-283/` (bash `/c/dev/wk-irpt-bckend-283`). Work only there.

**Why.** IB-pr-421 retired the one-use plan that the performance adapter demanded before a Black Diamond or Orion call. The retired gate
had a second half in Terraform: in `infra/aws/terraform/investor-reporting/performance/retained.tf` (about lines 177-214) the adapter
role's two secret-read policies exist only when `var.approved_performance_plan` names their firm. That variable is unset, so the live
role `aws_iam_role.performance_adapter` holds no `secretsmanager:GetSecretValue`. IB-pr-421's zip without these two policies would write a
use record and then fail the credential read. The CTO ruled one release: the zip plus these two policies, under one pair.

**Build -- PLAN ONLY. Nothing is applied in this cell.**
1. **Ungate the two policies by removing their dependence on `var.approved_performance_plan`, NOT by setting that variable** (CTO
   condition 1). The four blocks stay, under their present addresses:
   `data.aws_secretsmanager_secret.performance_cot_session`, `aws_iam_role_policy.performance_approved_session`,
   `data.aws_secretsmanager_secret.performance_inf_session`, `aws_iam_role_policy.performance_approved_inf_session`.
   Their `count` no longer reads `local.performance_plan_firm` or the variable. If a `count` must remain for another reason (for
   example a firm that is not packaged), say which and why in the packet. Leave the variable's declaration, the plan environment
   variables and every other use of `performance_plan_firm` as they are: they are a later cleanup, and a change there is a plan line
   this order forbids.
2. **Each grant names its ONE secret ARN, read from the plan and printed: no wildcard, `GetSecretValue` only** (CTO condition 2).
3. **Plan the root** `infra/aws/terraform/investor-reporting/performance/` the way this repository plans (read `.tools/safe-apply`
   and its help first; a plan needs no apply and makes no change). **The plan's adds are exactly those two policies; anything else is
   a STOP** (CTO condition 3): no change to any other resource, no destroy, no change to the Lambda or its environment. Data sources
   read at plan time are not adds.
4. **Run the plan through safe-apply's naming limb BEFORE the packet is written** (CTO condition 4). A hand-typed resource name
   stopped another apply on this box today after its pair was signed. If the naming limb refuses a policy name, STOP and file a row
   naming the refusal and what the builder (`lib/opal_naming.py name()`) returns for it; do not rename a policy on your own and do not
   edit `infra/logic/registry/`.
5. **Census** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~283/IB120-1_plan_census.json`:
   `{root, plan_command, adds:[addresses], changes:[addresses], destroys:[addresses], grants:[{policy_address, policy_name,
   actions:[...], resources:[...]}], naming_limb:"PASS"|"REFUSED", naming_limb_invocation, live_role_policies_before:[names]}`.
   `live_role_policies_before` is `aws iam list-role-policies` on the adapter's role, read now.
6. **Packet** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~283/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-422.md`: it says
   plainly that this is an IAM WIDENING of one role by two single-secret reads; it names both policy addresses and names, both secret
   ARNs, the plan's add / change / destroy counts, the naming limb's result with its invocation, Branch A (apply these two policies in
   the same act as IB-pr-421's zip, policies first) and Branch B (remove the two policies through the same Terraform path; state
   which commit to revert and that the role returns to the policy list read before), and that it is one release with IB-pr-421
   (packet `deliverables/0.9.0_WK_IRPT_BCKEND~282/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-421.md`, built
   `OF+8j4ucXsxwJ195NKEQZnma22T8bYVUriw9YP859RU=`). It states what is NOT exercised: no secret was read and no vendor was called.

<criterion id="IB120-1-AC1" cell_refs="IB-pr-422"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r120/p120_cells.py" . IB120-1-AC1</invocation><expect>IB120-1-AC1 PASS</expect></criterion>
<criterion id="IB120-1-AC2" cell_refs="IB-pr-422"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r120/p120_cells.py" . IB120-1-AC2</invocation><expect>IB120-1-AC2 PASS</expect></criterion>
<criterion id="IB120-1-AC3" cell_refs="IB-pr-422"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r120/p120_cells.py" . IB120-1-AC3</invocation><expect>IB120-1-AC3 PASS</expect></criterion>

<expected_criteria>IB120-1-AC1, IB120-1-AC2, IB120-1-AC3</expected_criteria>

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. **NO `terraform apply`, no `safe-apply` in apply mode, no AWS write of any kind.**
  Plan and AWS reads only. Do not read a secret's VALUE (`get-secret-value` is forbidden); a secret's ARN and name are all you need.
- **No vendor call.** No Lambda code or environment change. No other Terraform root.
- **Refusal clause:** STOP, file a row, and report on any of: a plan line that is not one of the two policy adds; a refused naming
  limb; a plan that cannot run (say exactly why and what you tried); a criterion that cannot be met as written. Never weaken a check;
  do not edit `p120_cells.py`.
- **Row ids** are `IRPT_BCKEND-D2-W283-S<k>`; `surfaced_at` is `date -u +%FT%TZ` at filing; check the id is free just before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~283" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~283@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~283 <0.9.0_WK_IRPT_BCKEND~283@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only. Do not push.
- A Terraform working directory (`.terraform/`, plan files) stays out of the commit; plan output saved as evidence goes under your
  deliverables folder as text with no secret value in it.

<paths>
infra/aws/terraform/investor-reporting/performance/
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~283/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-422.adapter-role-vendor-session-reads-ungated.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 113 (round 120, workstream ~P), cell `IB-pr-422`.
<owned_cells>IB-pr-422</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB120-1-AC1, IB120-1-AC2, IB120-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~283/IRPT_BCKEND.TO-IB-pr-422.adapter-role-vendor-session-reads-ungated.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: the Terraform commit; the plan's add / change / destroy lists; both secret ARNs and policy names;
the naming limb's invocation and result; the role's policy list read before; each criterion's last line; the proof checker's result;
any row ids. If you stopped on the refusal clause, say exactly where and why.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the tool was not run by the issuer; the cell's own plan is the blast read (its adds must be exactly two IAM role policies on one role, 0 changes, 0 destroys), graded by IB120-1-AC2.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: the tool was not run by the issuer; the cell IS the IAM change, plan only, and its census prints each grant's actions and resources from the plan (CTO msg 4488 conditions 2 and 3).
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p120_cells.py dry-run at base box/dell2 on dell2 2026-10-11 ~08:3xZ: AC1 FAIL (4 gated counts), AC2 FAIL (no census), AC3 FAIL (no census); commit-gate clean.
lane: the <paths> block IS the grant; ~P's performance Terraform root.
</preflight>

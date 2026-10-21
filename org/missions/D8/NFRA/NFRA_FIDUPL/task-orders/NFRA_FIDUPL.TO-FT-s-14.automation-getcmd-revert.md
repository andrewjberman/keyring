# TO NFRA_FIDUPL.TO-FT-s-14 -- revoke the account-wide ssm:GetCommandInvocation grant (the document never calls it)

<to_id>NFRA_FIDUPL.TO-FT-s-14</to_id>
<project>NFRA_FIDUPL</project>
<issued_to>0.7.0_AE_CloudOps~NFRA1</issued_to>
<issued_by>2.0.0_SA_COO~P1</issued_by>
<issued_date>2026-10-21</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>fidelity-r3-automationrevert</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `FT-s-14` (`decompositions/NFRA_FIDUPL_DECOMP_R3.md` section 13) | **outcome_ref:** FWD-9 (C-SCHEDULE) |
**depends_on:** FT-s-13 (applied 10:23Z and 10:26Z; the manual start succeeded at 10:28Z)

---

## WORKER FACE

### THE CELL

**FT-s-14** -- FT-s-13 step 2B added `ssm:GetCommandInvocation` to the automation role's `ListOwnCommandStar` statement (Resource `*`) at 10:26Z on the CTO's ask to cover every step the document runs, because the simulator read it as implicitDeny. The manual start of the document at 10:27:27Z then succeeded end to end, and CloudTrail for `Automation-bf5bc3dd-...` shows `ListCommandInvocations` calls and NO `GetCommandInvocation`. The grant is account-wide and unused: revert it. Your own flag in the FT-s-13 report (a wider read of command output than before) is accepted.

### WHAT TO DO

1. Open a change-management entry first (`.tools/deploy_ledger.py open --slug nfra-fidupl-automation-getcmd-revert-<date> ...`). WAIT until the 10:45Z scheduled leg's automation execution is terminal (read `describe-automation-executions`: the leg starts at 10:45Z; expect terminal by about 10:52Z): the leg must run on the policy that proved the document, and the revert is applied only after it. If the leg did NOT start an execution, apply at once and say so.
2. Edit `infra/aws/terraform/canonical-fidelity-ec2/automation.tf`: remove `"ssm:GetCommandInvocation"` from the `Action` list of the `ListOwnCommandStar` statement and make its STAR-OK comment true again (it lists `ssm:ListCommands` and `ssm:ListCommandInvocations` only). Change NOTHING else. The plan must show one in-place update of `aws_iam_role_policy.automation` whose only difference is that one action. Apply with `safe-apply` on the whole root (no `-target`).
3. Read back: `fidupl_round_checks.py ft14a` (the simulator no longer allows it on `*`) and `fidupl_round_checks.py ft6r`. Do NOT start an execution by hand. The 11:15Z-style next fire is NOT the proof of this; the 10:45Z leg already ran on the proven policy, and the next scheduled leg after the revert is its regression read (the document does not call the action).
4. Close the ledger entry. Report counts only: the before decision, the plan line, the apply line and time, the two check lines.

### ACCEPTANCE

<criterion id="FT-s-14-AC1" cell_refs="FT-s-14"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py ft14a</invocation><expect>R1-FT14A-OK the account-wide GetCommandInvocation grant is revoked</expect></criterion>
`FT-s-14-AC1` -- the automation role is no longer allowed `ssm:GetCommandInvocation` on `*`.

<criterion id="FT-s-14-AC2" cell_refs="FT-s-14"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py ft6r</invocation><expect>R1-FT6R-OK</expect></criterion>
`FT-s-14-AC2` -- the three rules are still ENABLED.

<expected_criteria>FT-s-14-AC1,FT-s-14-AC2</expected_criteria>

Dry-run at the base: `FT-s-14-AC1` base: FAIL as expected (the grant is live); `FT-s-14-AC2` base: PASS as expected.

## BOUNDS

- **Grant.** The `<paths>` block below and your deliverables folder.
- **WORLD.** One Terraform apply of one IAM policy resource under `safe-apply` (never bare apply, never `-target`). Ledger first, closed last. No alert; no change to any other statement, role, rule or document.
- **Refusal clause.** A plan that shows more than that one action removed: stop and file a surprise row (`NFRA_FIDUPL-D1-<your slot>-S<k>`, next unused).

<paths>
infra/aws/terraform/canonical-fidelity-ec2/automation.tf
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/NFRA/NFRA_FIDUPL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_DECOMP_R3.md</decomp_doc> (round 3, section 13 addendum), cell `FT-s-14`.
<owned_cells>FT-s-14</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: FT-s-14-AC1, FT-s-14-AC2. Instance at `org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/0.7.0_AE_CloudOps~NFRA1/NFRA_FIDUPL.TO-FT-s-14.getcmd-revert.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> FT-s-14-AC1,FT-s-14-AC2` BEFORE the flip. Commit the records first, then pin.
</proof_of_spec>

**REPORT:** the before decision, the plan line, the apply line and time, the two check lines, every surprise row id, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no rule, cron, state or target changes; denominator 0 schedules changed.
comp-iam: RUN -- one action removed from one statement of one inline policy (a revoke); denominator 1 statement changed, 0 actions added, 0 principals.
comp-adversary: DECLARED-NOT-APPLICABLE -- a revoke of an unused read grant.
lane: the paths block.
</preflight>

Source: CloudTrail for Automation-bf5bc3dd (ListCommandInvocations only); FT-s-13 report flag; CTO msg 9055.

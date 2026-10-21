# TO NFRA_FIDUPL.TO-FT-s-15 -- the third resource form SSM checks (automation-execution/*), and one one-shot proof of the ROLE path

<to_id>NFRA_FIDUPL.TO-FT-s-15</to_id>
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
<workstream>fidelity-r3-schedulethird</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `FT-s-15` (`decompositions/NFRA_FIDUPL_DECOMP_R3.md` section 14) | **outcome_ref:** FWD-9 (C-SCHEDULE) |
**depends_on:** FT-s-13, FT-s-14 (applied 10:48Z)

---

## WORKER FACE

### THE CELL

**FT-s-15** -- The 10:45Z leg failed too. CloudTrail (StartAutomationExecution 10:45:04Z, assumed role `fidelity-alongside-schedule-role`): AccessDenied on `arn:aws:ssm:us-east-1:313476888478:automation-execution/*`. SSM authorizes the start against THREE resource forms: `automation-definition/<name>`, `document/<name>` and `automation-execution/*`; the schedule policy now names the first two. Add the third to the same statement, simulate all three forms, and prove the ROLE path with ONE one-shot run today (CTO msg 9065). The manual start at 10:27Z proved the document and the automation role; this proves the schedule role through EventBridge.

### WHAT TO DO

1. Open a change-management entry first (`.tools/deploy_ledger.py open --slug nfra-fidupl-schedule-third-form-<date> ...`).
2. Edit `infra/aws/terraform/canonical-fidelity-ec2/schedule.tf`: in the statement `StartTheRunDocumentOnly` add to `Resource` the string `"arn:aws:ssm:${local.region}:${data.aws_caller_identity.current.account_id}:automation-execution/*"`. Change NOTHING else. The plan must show one in-place update of `aws_iam_role_policy.schedule` whose only difference is that one added resource. Apply with `safe-apply` on the whole root (no `-target`).
3. Read back `fidupl_round_checks.py ft15s` (all three forms allowed; expect OK) and `fidupl_round_checks.py ft6r`.
4. **The one-shot proof (a temporary resource outside Terraform, named in this order and deleted after its read).** Create ONE EventBridge rule named `fidelity-alongside-oneshot-proof-20261021` (a name that ends in the date; the `fidelity` prefix keeps it within the lane of the naming gate's reads: `ft6r` counts rules by the `fidelity` prefix, so delete it BEFORE you run `ft6r` again) with a one-time cron `cron(<MM> <HH> 21 10 ? 2026)` set 6 to 8 minutes ahead of now, state ENABLED, then `put-targets` copying the SAME target as `fidelity-alongside-fetch-leg-1-daily` exactly (read it with `list-targets-by-rule`: same `Arn` with `:$DEFAULT`, same `RoleArn`, same `Input`, `Id` `fidelity-run`). Check the sign-in cap first (the trailing hour holds the 10:27Z manual start). After the fire read, in this order: `describe-automation-executions` (the execution id, terminal status, step names), the run record the wrapper writes (`_runs/<day>/run-<id>.json` outcome and counts, content as-of), the rule's `Invocations` and `FailedInvocations` for that minute, then `remove-targets` and `delete-rule`, then confirm with `list-rules --name-prefix fidelity-alongside-oneshot` that nothing is left. If the one-shot fails, stop and report CloudTrail's `errorMessage` for the start; do NOT create a second one.
5. Close the ledger entry. Report counts only: the plan line, the apply line and time, `ft15s`, the one-shot's execution id, status, the run record outcome, the metric counts, the deletion confirmation.

### ACCEPTANCE

<criterion id="FT-s-15-AC1" cell_refs="FT-s-15"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py ft15s</invocation><expect>R1-FT15S-OK schedule start allowed on all 3 resource forms</expect></criterion>
`FT-s-15-AC1` -- the schedule role is allowed to start the run on all three resource forms.

<criterion id="FT-s-15-AC2" cell_refs="FT-s-15"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py ft6r</invocation><expect>R1-FT6R-OK</expect></criterion>
`FT-s-15-AC2` -- exactly the three standing rules are ENABLED (the one-shot is deleted).

<expected_criteria>FT-s-15-AC1,FT-s-15-AC2</expected_criteria>

Dry-run at the base: `FT-s-15-AC1` base: FAIL as expected (the third form is implicitDeny); `FT-s-15-AC2` base: PASS as expected.

## BOUNDS

- **Grant.** The `<paths>` block below and your deliverables folder.
- **WORLD.** One Terraform apply of one IAM policy resource under `safe-apply` (never bare apply, never `-target`), and ONE temporary EventBridge rule with one target, created and deleted by you, fired once. Ledger first, closed last. No alert; no change to the three standing rules, their crons, states, targets, inputs, or any other statement or role.
- **Refusal clause.** A plan that shows more than that one resource added: stop and file a surprise row (`NFRA_FIDUPL-D1-<your slot>-S<k>`, next unused).

<paths>
infra/aws/terraform/canonical-fidelity-ec2/schedule.tf
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/NFRA/NFRA_FIDUPL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_DECOMP_R3.md</decomp_doc> (round 3, section 14 addendum), cell `FT-s-15`.
<owned_cells>FT-s-15</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: FT-s-15-AC1, FT-s-15-AC2. Instance at `org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/0.7.0_AE_CloudOps~NFRA1/NFRA_FIDUPL.TO-FT-s-15.third-form.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> FT-s-15-AC1,FT-s-15-AC2` BEFORE the flip. Commit the records first, then pin.
</proof_of_spec>

**REPORT:** the plan line, the apply line and time, `ft15s`, the one-shot's execution id, status, run record outcome, metric counts, the deletion confirmation, every surprise row id, commits.

---

## RECORD FACE

<preflight>
comp-schedule: RUN -- one temporary one-shot rule is created and deleted; the three standing rules, crons, states and targets are not touched; denominator 3 standing rules unchanged, 1 temporary rule created and deleted.
comp-iam: RUN -- one resource ARN form (automation-execution/*, the form SSM checks the start against) is added to one statement of one inline policy; denominator 1 statement changed, 0 actions, 0 principals.
comp-adversary: DECLARED-NOT-APPLICABLE -- the one-shot starts the same document the schedule starts; the CTO's order (msg 9065) is the record.
lane: the paths block.
</preflight>

Source: CloudTrail StartAutomationExecution AccessDenied 2026-10-21T10:45:04Z; CTO msg 9065; schedule.tf as merged.

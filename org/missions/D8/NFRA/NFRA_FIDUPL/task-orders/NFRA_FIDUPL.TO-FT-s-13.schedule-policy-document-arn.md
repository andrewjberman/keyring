# TO NFRA_FIDUPL.TO-FT-s-13 -- the schedule role must be allowed to start the run on the document/ ARN form (CloudTrail: AccessDenied at 10:15:02Z)

<to_id>NFRA_FIDUPL.TO-FT-s-13</to_id>
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
<workstream>fidelity-r3-schedulepolicy</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `FT-s-13` (`decompositions/NFRA_FIDUPL_DECOMP_R3.md` section 12) | **outcome_ref:** FWD-9 (C-SCHEDULE) |
**depends_on:** FT-s-12 (applied 09:57Z)

---

## WORKER FACE

### THE CELL

**FT-s-13** -- After the FT-s-12 apply (target ARNs now end in `:$DEFAULT`) the 10:15Z leg again showed FailedInvocations 1. CloudTrail names the cause (event `StartAutomationExecution`, 2026-10-21T10:15:02Z, assumed role `fidelity-alongside-schedule-role`): **AccessDenied**, "not authorized to perform ssm:StartAutomationExecution on resource `arn:aws:ssm:us-east-1:313476888478:document/fidelity-alongside-uploader-document` because no identity-based policy allows the ssm:StartAutomationExecution action". SSM authorizes the start on the DOCUMENT ARN (`:document/<name>`); the schedule role's policy allows only the `automation-definition/<name>` forms. The fix adds that one ARN form of the SAME single document to the policy's first statement. No other statement, action, role or document is touched.

### WHAT TO DO

1. Open a change-management entry first (`.tools/deploy_ledger.py open --slug nfra-fidupl-schedule-policy-document-arn-<date> ...`). Before the change measure and record: `simulate-principal-policy` of the schedule role for `ssm:StartAutomationExecution` on `arn:aws:ssm:us-east-1:313476888478:document/fidelity-alongside-uploader-document` (expect implicitDeny) and `fidupl_round_checks.py ft13s` (expect FAIL).
2. Edit `infra/aws/terraform/canonical-fidelity-ec2/schedule.tf`: in the policy statement `StartTheRunDocumentOnly` add to `Resource` the string `"arn:aws:ssm:${local.region}:${data.aws_caller_identity.current.account_id}:document/${aws_ssm_document.run.name}"`. Change NOTHING else. The plan must show exactly one in-place update of `aws_iam_role_policy.schedule` whose only difference is that one added resource. Apply with `safe-apply` on the whole root (no `-target`). The rules stay ENABLED.
3. Read back: `fidupl_round_checks.py ft13s` (allowed) and `fidupl_round_checks.py ft6r`. Do NOT start an execution by hand; the 10:45Z leg proves it (SPEED: the 10:45Z leg is 25 minutes after this order is sent). Report the apply time at once.
4. Close the ledger entry. Report counts only: before and after simulation decisions, the plan line, the apply line, the apply time.

### ACCEPTANCE

<criterion id="FT-s-13-AC1" cell_refs="FT-s-13"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py ft13s</invocation><expect>R1-FT13S-OK schedule start allowed</expect></criterion>
`FT-s-13-AC1` -- the schedule role is allowed to start the run on the document/ ARN form.

<criterion id="FT-s-13-AC2" cell_refs="FT-s-13"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py ft6r</invocation><expect>R1-FT6R-OK</expect></criterion>
`FT-s-13-AC2` -- the three rules are still ENABLED.

<expected_criteria>FT-s-13-AC1,FT-s-13-AC2</expected_criteria>

Dry-run at the base: `FT-s-13-AC1` base: FAIL as expected (implicitDeny on the document/ form); `FT-s-13-AC2` base: PASS as expected.

## BOUNDS

- **Grant.** The `<paths>` block below and your deliverables folder.
- **WORLD.** One Terraform apply of one IAM policy resource under `safe-apply` (never bare apply, never `-target`). Ledger first, closed last. No alert, no change to a cron, a rule state, an input, a role, a trust policy or any other statement.
- **Refusal clause.** A plan that shows more than that one policy update: stop and file a surprise row (`NFRA_FIDUPL-D1-<your slot>-S<k>`, next unused).

<paths>
infra/aws/terraform/canonical-fidelity-ec2/schedule.tf
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/NFRA/NFRA_FIDUPL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_DECOMP_R3.md</decomp_doc> (round 3, section 12 addendum), cell `FT-s-13`.
<owned_cells>FT-s-13</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: FT-s-13-AC1, FT-s-13-AC2. Instance at `org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/0.7.0_AE_CloudOps~NFRA1/NFRA_FIDUPL.TO-FT-s-13.schedule-policy.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> FT-s-13-AC1,FT-s-13-AC2` BEFORE the flip. Commit the records first, then pin.
</proof_of_spec>

**REPORT:** the before and after decisions, the plan line, the apply line and time, the two check lines, every surprise row id, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no rule, cron, state or target changes; denominator 0 schedules changed.
comp-iam: RUN -- one resource ARN (the same single document, its document/ form) is added to one statement of one inline policy; denominator 1 statement changed, 0 actions, 0 principals, 0 roles added.
comp-adversary: DECLARED-NOT-APPLICABLE -- the grant names one document; the 10:45Z leg is the proof.
lane: the paths block.
</preflight>

Source: CloudTrail StartAutomationExecution AccessDenied 2026-10-21T10:15:02Z; CTO msgs 9047 and 9048; schedule.tf as merged.

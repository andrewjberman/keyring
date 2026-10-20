# TO NFRA_FIDUPL.TO-FU-s-13 -- the automation role may verify its own command (ssm:ListCommands, ssm:ListCommandInvocations)

<to_id>NFRA_FIDUPL.TO-FU-s-13</to_id>
<project>NFRA_FIDUPL</project>
<issued_to>0.7.0_AE_CloudOps~NFRA1</issued_to>
<issued_by>2.0.0_SA_COO~P1</issued_by>
<issued_date>2026-10-20</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>fidelity-automation-iam</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `FU-s-13` (`decompositions/NFRA_FIDUPL_DECOMP.md` section 12) | **outcome_ref:** FWD-1 |
**depends_on:** FU-s-9 (the automation, applied)

---

## WORKER FACE

### THE CELL

**FU-s-13** -- The run automation (`fidelity-alongside-uploader-document`) ends `Failed` at its `runWrapper` step even though the command runs, because the automation role is not allowed `ssm:ListCommands`. Execution 9c7fa8c2-9db3-4245-ab34-3e6fdd333f96 failed with exactly: `fidelity-alongside-automation-role ... is not authorized to perform: ssm:ListCommands ... no identity-based policy allows the ssm:ListCommands action`. The `aws:runCommand` action also lists the command's invocations. Add the two actions to the role's policy so a scheduled run can end `Success`. CTO ruling 8793 item 4.

**Read first:** `infra/aws/terraform/canonical-fidelity-ec2/automation.tf` (the role policy statements; today `ssm:SendCommand` and `ssm:GetCommandInvocation` are on the document and instance ARNs, `ssm:DescribeInstanceInformation` is on `*` under a `STAR-OK` comment), your own earlier ledgers for FU-s-9, and `org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/0.7.0_AE_CloudOps~NFRA1/`.

### WHAT TO DO

1. Open a change-management entry (`.tools/deploy_ledger.py open --slug nfra-fidupl-automation-iam-<date> ...`, one leg: policy widened).
2. In `automation.tf`, add ONE statement to the automation role's policy: `Action = ["ssm:ListCommands", "ssm:ListCommandInvocations"]` on `Resource = ["*"]`, with the `# STAR-OK: <reason>` comment the guard `fu6g` requires (these two list actions have no resource-level support). Do not widen any other statement, add no wildcard action, change no other resource.
3. Plan (AMENDED 2026-10-20 ~21:40Z on CTO ruling, msg after 8806: the WHOLE root, no `-target`): it must read exactly `Plan: 1 to add, 2 to change, 0 to destroy.` and name, line by line, (a) ADD the per-G list secret `fidelity/alongside/perg-list` (metadata only, `ignore_changes` on its value, no secret version), (b) CHANGE the box role policy (the one per-secret read grant, no wildcard), (c) CHANGE the automation role policy (the two `ssm` list actions of step 2). Anything else in the plan is a surprise row and a stop. FR-s-5's resources belong in the applied world (FR-s-5 is complete on fakes). Apply the root once with `safe-apply`, no `-target`, and ONLY after the issuer's message says APPLY (the attempt window must have reported first, so no IAM change lands mid-run). Close the ledger. The secret's VALUE is not written by this order (the executor writes it later from the off-git list).
4. Run the criteria below and put the lines verbatim in your report. **Do not start the automation and do not sign in**: the criteria check the grant, not a run.

### ACCEPTANCE

<criterion id="FU13-AC1" cell_refs="FU-s-13"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py fu13i</invocation><expect>R1-FU13I-OK the automation role may ListCommands and ListCommandInvocations</expect></criterion>
`FU13-AC1` -- the live role may list commands and invocations (the IAM simulator, no run).

<criterion id="FU13-AC2" cell_refs="FU-s-13"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py fu6g</invocation><expect>R1-FU6G-OK</expect></criterion>
`FU13-AC2` -- the root's guard still passes (no wildcard action, the STAR-OK comment present, no ingress, no secret version). A second criterion, with its reason: it is the guard that fails if the new statement is written carelessly.

<expected_criteria>FU13-AC1,FU13-AC2</expected_criteria>

Dry-run at the base: `FU13-AC1` base: FAIL as expected (the role lacks both actions); `FU13-AC2` base: PASS as expected. (The whole-root plan expectation is graded by the seat's report of the plan line, not by a third criterion.)

## BOUNDS

- **Grant.** The `<paths>` block below and your deliverables folder.
- **WORLD.** This order changes two IAM policies and adds one secret (metadata only). Ledger first, closed last; the apply is by `safe-apply` only; nothing is stopped, started or deleted; no secret value anywhere; no alert.
- **Refusal clause.** A premise that fails (the plan shows more than one change, an automation execution is in progress) is a surprise row (`NFRA_FIDUPL-D1-<your slot>-S<k>`, next unused) and you stop.

<paths>
infra/aws/terraform/canonical-fidelity-ec2/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/NFRA/NFRA_FIDUPL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_DECOMP.md</decomp_doc> (round 1, section 12 addendum), cell `FU-s-13`.
<owned_cells>FU-s-13</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: FU13-AC1, FU13-AC2. Instance at `org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/0.7.0_AE_CloudOps~NFRA1/NFRA_FIDUPL.TO-FU-s-13.automation-iam.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> FU13-AC1,FU13-AC2` BEFORE the flip. Commit the root edit first, then pin.
</proof_of_spec>

**REPORT:** the plan line, the apply result, the two check lines verbatim, the ledger id, every surprise row id, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- the schedule rules are not touched; denominator 0 schedules created or changed by this order.
comp-iam: RUN -- ONE statement is added to the automation role policy (ssm:ListCommands, ssm:ListCommandInvocations on *, which have no resource-level support); denominator 1 IAM statement added, 0 widened. comp-iam is blind to the role's computed names and to the aws:runCommand action's internal calls; the live check is the IAM simulator in FU13-AC1.
comp-adversary: DECLARED-NOT-APPLICABLE -- two read-only list actions; they expose command ids and statuses of the account, not their content.
lane: the paths block.
</preflight>

Source: CTO msg 8793 item 4; automation execution 9c7fa8c2-9db3-4245-ab34-3e6fdd333f96 (runWrapper step failure message).

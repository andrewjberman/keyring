# TO NFRA_FIDUPL.TO-FT-s-12 -- the schedule target ARN needs the :$DEFAULT version suffix (the 09:45Z fire failed at the EventBridge-to-SSM hop)

<to_id>NFRA_FIDUPL.TO-FT-s-12</to_id>
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
<workstream>fidelity-r3-schedulefix</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `FT-s-12` (`decompositions/NFRA_FIDUPL_DECOMP_R3.md` section 11) | **outcome_ref:** FWD-9 (C-SCHEDULE) |
**depends_on:** FT-s-6 (the schedule is ENABLED)

---

## WORKER FACE

### THE CELL

**FT-s-12** -- The first scheduled fire (09:45Z) failed: rule `fidelity-alongside-fetch-leg-1-daily` shows Invocations 1 and FailedInvocations 1 in `AWS/Events`, no Automation execution since 09:00Z, no SSM command on the box, no run record. The three rule targets carry the document ARN with NO version suffix (`.../automation-definition/fidelity-alongside-uploader-document`); an EventBridge target for an SSM Automation document needs the suffix `:$DEFAULT` (or a document version). The schedule role's policy is not at fault: it allows `ssm:StartAutomationExecution` on the document ARN and on `...:*`, and `iam:PassRole` on the automation role for `ssm.amazonaws.com` (a simulator PassRole implicitDeny comes from the missing `iam:PassedToService` context key). CTO msgs 9047 and 9048.

### WHAT TO DO

1. Open a change-management entry first (`.tools/deploy_ledger.py open --slug nfra-fidupl-schedule-target-suffix-<date> ...`). Before the change measure and record (counts only): the three targets' ARNs as applied, and one `simulate-principal-policy` of the schedule role for `ssm:StartAutomationExecution` on the document ARN WITH the `:$DEFAULT` suffix (expect allowed).
2. Edit `infra/aws/terraform/canonical-fidelity-ec2/schedule.tf`: in `aws_cloudwatch_event_target.window` change `arn = aws_ssm_document.run.arn` to `arn = "${aws_ssm_document.run.arn}:$DEFAULT"` (the `$D` is not an interpolation; keep it literal). Change NOTHING else (no cron, no state, no input, no IAM). The plan must show exactly three in-place updates of `aws_cloudwatch_event_target.window[...]` and nothing else (`fidupl_round_checks.py fu6p` style read; no `-target`). Apply with `safe-apply` on the whole root. The rules stay ENABLED.
3. Read back: `fidupl_round_checks.py ft12t` (all three target ARNs end in `:$DEFAULT`) and `fidupl_round_checks.py ft6r` (rules still ENABLED). Do NOT start an execution by hand unless the issuer says so; the 10:15Z leg proves it. If the 10:15Z leg is closer than the apply, say so and the issuer decides.
4. Close the ledger entry. Report counts only: the before ARNs (suffix present or absent), the plan line, the two check lines, the apply time.

### ACCEPTANCE

<criterion id="FT-s-12-AC1" cell_refs="FT-s-12"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py ft12t</invocation><expect>R1-FT12T-OK rule targets</expect></criterion>
`FT-s-12-AC1` -- all three rule targets end in `:$DEFAULT`.

<criterion id="FT-s-12-AC2" cell_refs="FT-s-12"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py ft6r</invocation><expect>R1-FT6R-OK</expect></criterion>
`FT-s-12-AC2` -- the three rules are still ENABLED.

<expected_criteria>FT-s-12-AC1,FT-s-12-AC2</expected_criteria>

Dry-run at the base: `FT-s-12-AC1` base: FAIL as expected (no suffix applied); `FT-s-12-AC2` base: PASS as expected.

## BOUNDS

- **Grant.** The `<paths>` block below and your deliverables folder.
- **WORLD.** One Terraform apply of three target updates under `safe-apply` (never bare apply, never `-target`). Ledger first, closed last. No alert, no change to a cron, a rule state, an input or any IAM statement.
- **Refusal clause.** A plan that shows more than the three target updates, or an IAM change: stop and file a surprise row (`NFRA_FIDUPL-D1-<your slot>-S<k>`, next unused).

<paths>
infra/aws/terraform/canonical-fidelity-ec2/schedule.tf
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/NFRA/NFRA_FIDUPL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_DECOMP_R3.md</decomp_doc> (round 3, section 11 addendum), cell `FT-s-12`.
<owned_cells>FT-s-12</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: FT-s-12-AC1, FT-s-12-AC2. Instance at `org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/0.7.0_AE_CloudOps~NFRA1/NFRA_FIDUPL.TO-FT-s-12.schedule-target.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> FT-s-12-AC1,FT-s-12-AC2` BEFORE the flip. Commit the records first, then pin.
</proof_of_spec>

**REPORT:** the before ARNs, the plan line, the two check lines, the apply time, every surprise row id, commits.

---

## RECORD FACE

<preflight>
comp-schedule: RUN -- three rule targets change their ARN only; denominator 3 rules, 0 cron changes, 0 state changes.
comp-iam: DECLARED-NOT-APPLICABLE -- no grant changes; the schedule role's policy already allows the suffixed ARN; denominator 0 IAM statements changed.
comp-adversary: DECLARED-NOT-APPLICABLE -- a target ARN suffix; the 10:15Z leg is the proof.
lane: the paths block.
</preflight>

Source: CTO msgs 9047 and 9048; AWS/Events FailedInvocations 1 at 09:45Z; schedule.tf as merged.

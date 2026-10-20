# TO NFRA_FIDUPL.TO-FU-s-9 -- autoshutdown off for the Fidelity box, as one root edit and one apply

<to_id>NFRA_FIDUPL.TO-FU-s-9</to_id>
<project>NFRA_FIDUPL</project>
<issued_to>0.7.0_AE_CloudOps~NFRA1</issued_to>
<issued_by>2.0.0_SA_COO~P1</issued_by>
<issued_date>2026-10-20</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>fidelity-autoshutdown</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `FU-s-9` (`decompositions/NFRA_FIDUPL_DECOMP.md` section 8, the CTO addendum) | **outcome_ref:** FWD-7 |
**depends_on:** FU-x-1 (its automation run must have ended; the issuer sends you the word)

---

## WORKER FACE

### THE CELL

**FU-s-9** -- Autoshutdown off for the Fidelity box: one edit of the Terraform root adds the tag `AutoShutdown=disabled` to the instance and removes the `stopInstance` step from `automation.tf` (with the `onFailure` references to it), applied by the CloudOps seat under `safe-apply` AFTER FU-x-1's automation run has ended. Contract rows: C-TF, FWD-7. Ruled by the CTO (msg 8621, ruling @630242a029) on Andrew's word ("Turn off autoshutdown for this box").

**ADDED 2026-10-20 ~13:15Z (live finding, worker row NFRA_FIDUPL-D1-W1-S8, execution b065d07e-53e7-47b6-9c07-476c21f1d6df):** FU-x-1's one automation run failed at 13:02Z because the automation role lacks `ec2:DescribeInstanceStatus`, which the `aws:changeInstanceState` start step needs; the run never reached the wrapper. The same root edit and the same apply fix it (edit (c) below). Row S8 names you as its disarm owner.

**Read first:** `org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_R1_WORKER_REFERENCE.md` (the facts every cell shares) and the cell text above. The account's `ec2-auto-shutdown-enforcer` stopped the box at 2026-10-20T00:51Z (your row NFRA_FIDUPL-D1-S5); its only exemption is the tag `AutoShutdown=disabled` (`infra/aws/lambda/ec2-auto-shutdown-enforcer/lambda_function.py:18` and `:114`, per the CRO).

### WHAT TO DO

HOLD until the issuer messages you that FU-x-1's automation run has ended; no execution of the automation document may be in progress when you apply (read `aws ssm describe-automation-executions` for the document and confirm none is `InProgress`).

1. Open a change-management entry first (`.tools/deploy_ledger.py open --slug nfra-fidupl-autoshutdown-off-20261020 ...`, legs: root edit applied; tag live; document version without a stop step; repaired sign-in files delivered).
2. Edit `infra/aws/terraform/canonical-fidelity-ec2/` ONLY: (a) add the tag `AutoShutdown = "disabled"` to the instance's tags (keep every tag already there); (b) delete the `stopInstance` step of the automation document (about `automation.tf` lines 129-135) AND every `onFailure = "step:stopInstance"` that points at it (about lines 89, 99 and 117), so the document stays valid and the run ends after the wrapper step. (c) in `automation.tf`, add `ec2:DescribeInstanceStatus` to the automation role policy: put it in the existing `ReadBoxStateStar` statement beside `ec2:DescribeInstances` (neither supports a resource-level scope) and extend its `# STAR-OK:` comment to name it, so the IAM guard check stays green; (d) add an output `automation_role_arn` (the automation role's ARN) to `outputs.tf`. Do not change anything else and do not remove any permission.
3. `terraform plan` must show exactly three changes (the instance tags, the automation document, the automation role policy) plus the new output, and nothing added or destroyed; stop and file a surprise row if it shows more.
4. Apply ONLY through `.tools/safe-apply.sh`. Never stop, start or terminate the instance. The ledger is closed last.
5. **Re-deliver the repaired code (added 2026-10-20 ~14:00Z).** The FU-s-2 repair (measured login selectors, step trace) is merged on box/dell1 at 46c10823e4. Re-deliver `signin.py` and `signin_recon.py` from `infra/aws/ec2/canonical-fidelity/` at that head (or later) to `/opt/fidelity-uploader/` on the box exactly as you delivered the others (SSM, base64 chunks), the box is running, do not stop it. Then criterion FU9-AC5 reads the md5 of both files on the box against the repo.
6. Run the five criteria below and record each line verbatim.

### ACCEPTANCE

<criterion id="FU9-AC1" cell_refs="FU-s-9"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/r1_checks.py fu8t</invocation><expect>R1-FU8T-OK AutoShutdown=disabled on the instance</expect></criterion>
`FU9-AC1` -- the tag is live on the instance.

<criterion id="FU9-AC2" cell_refs="FU-s-9"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/r1_checks.py fu8d</invocation><expect>R1-FU8D-OK no stop step in live document version</expect></criterion>
`FU9-AC2` -- the live automation document version has no stop step and keeps its start step.

<criterion id="FU9-AC3" cell_refs="FU-s-9"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/r1_checks.py fu7a</invocation><expect>R1-FU7A-OK No changes\.</expect></criterion>
`FU9-AC3` -- after the apply, `terraform plan` reads No changes.

<criterion id="FU9-AC4" cell_refs="FU-s-9"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/r1_checks.py fu8p</invocation><expect>R1-FU8P-OK the automation role is allowed ec2:DescribeInstanceStatus</expect></criterion>
`FU9-AC4` -- the live automation role is allowed `ec2:DescribeInstanceStatus` (IAM simulation). A fourth criterion, with its reason: the live trace failed on exactly this missing permission and the other three cannot see it.

<criterion id="FU9-AC5" cell_refs="FU-s-9"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/r1_checks.py fu9m</invocation><expect>R1-FU9M-OK signin.py,signin_recon.py match the repo on the box</expect></criterion>
`FU9-AC5` -- the repaired sign-in files on the box match the repo. A fifth criterion, with its reason: the box holds the OLD sign-in code and the live trace needs the repaired code.

<expected_criteria>FU9-AC1,FU9-AC2,FU9-AC3,FU9-AC4,FU9-AC5</expected_criteria>

Dry-run at the base (the box still holds the pre-repair files): `FU9-AC5` base: FAIL as expected.

Dry-run at the base (HEAD of box/dell1 at the cut; `FU9-AC4` base: FAIL as expected, no automation_role_arn output yet): `FU9-AC1` base: FAIL as expected (tag AutoShutdown=None); `FU9-AC2` base: FAIL as expected (live document version 2 has a stop step); `FU9-AC3` base: PASS as expected (the root currently plans No changes; it is the after-apply bar).

## BOUNDS

- **Grant.** The `<paths>` block below and your deliverables folder. Everything else named here you READ.
- **WORLD.** This order changes AWS. The ledger is opened first and closed last; the apply is by `safe-apply` only; nothing is stopped, started, deleted or destroyed.
- **No secret, no alert.** No secret value anywhere; no SNS, SES or notification of any kind.
- **Refusal clause.** A premise that fails against live state (the plan shows more than two changes, an execution is in progress) is a surprise row (`NFRA_FIDUPL-D1-<your slot>-S<k>` in the investigation file, next unused) and you stop that piece.

<paths>
infra/aws/terraform/canonical-fidelity-ec2/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/NFRA/NFRA_FIDUPL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_DECOMP.md</decomp_doc> (round 1, section 8 addendum), cell `FU-s-9`.
<owned_cells>FU-s-9</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: FU9-AC1,FU9-AC2,FU9-AC3,FU9-AC4,FU9-AC5. Instance at `org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/0.7.0_AE_CloudOps~NFRA1/NFRA_FIDUPL.TO-FU-s-9.autoshutdown-off.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> FU9-AC1,FU9-AC2,FU9-AC3,FU9-AC4,FU9-AC5` BEFORE the flip. Commit code first, then pin.
</proof_of_spec>

**REPORT:** what changed and where, the plan's three changes, each check line verbatim, the ledger id, every surprise row id, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- the schedule rules are not touched; denominator 0 schedules created or changed by this order.
comp-iam: DECLARED-NOT-APPLICABLE -- no grant is added or removed; denominator 0 IAM statements changed.
comp-adversary: DECLARED-NOT-APPLICABLE -- a two-line root edit; no new surface.
lane: the paths block.
</preflight>

Source: CTO ruling @630242a029 (msg 8621) on Andrew-direct 2026-10-20 ~12:50Z; CRO msg 8618.


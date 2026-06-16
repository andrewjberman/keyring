# Deploy-completion ledger -- NFRA_GCONTR EC2-WRITES fix (iam:GetInstanceProfile + WARN)

**class:** deploy_completion
**status:** OPEN
**opened:** 20260616T162258Z
**owner:** 0.7.0_AE_CloudOps
**project / TO:** NFRA_GCONTR (EC2-WRITES derive gap)
**authorization:** JOINT GATE -- COO operational GO 162005Z + CTO concur 162018Z (additive read-only IAM, AE-autonomous via safe-apply, no Andrew gate)
**code commit:** 2895884ad (WARN comp_aws_cli.py:1638 + item2a.tf +iam:GetInstanceProfile)

## What
Add iam:GetInstanceProfile to the derive_runner_task role (so the Fargate derive can resolve
instance-profile -> role -> emit EC2-producer WRITES edges) + a LOUD WARN replacing the silent
except that hid the gap. Closes the estate-wide 0-EC2-WRITES-edges blind spot (NNA + platinum/firm
become graph_contracts Q2-resolvable).

## Legs (finish in-session or roll back + escalate loud to COO)
- [ ] L1: comp-iam on the iam.tf (Phase-2 mandate) -> 0 NEW gaps
- [ ] L2: terraform plan -> exactly the 1 perm add (0 unrelated drift); HALTGT clears
- [ ] L3: safe-apply (Rule 18) -> applied; terraform plan again = 0-diff
- [ ] L4: rebuild derive image (zip + WARN'd comp_aws_cli.py) -> CodeBuild -> ECR :latest SUCCEEDED (deploys the WARN; perm already live via L3)
- [ ] L5: VERIFY on the SCHEDULED nightly derive (NOT ad-hoc): EC2-WRITES edges appear, comp-kuzu EC2 WRITES > 0, bd-exporter-ec2-role -> opal-data-bd

## Close criteria
iam.tf applied 0-diff + image rebuilt (both legs landed). L5 verification is the next nightly's
artifacts (event-driven, next-morning review). Then RAVC2 COO+CTO; ping CVO to re-verify NNA + EC2 surfaces.

## Rollback
Additive read-only IAM perm -- removable via a reverting safe-apply (recoverable). No data path touched.

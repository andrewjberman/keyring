# Deploy-completion ledger -- NFRA_GCONTR EC2-WRITES fix (iam:GetInstanceProfile + WARN)

**class:** deploy_completion
**status:** CLOSED COMPLETE (deploy legs landed; L5 nightly-verify deferred to next-morning per no-ad-hoc-derive)
**opened:** 20260616T162258Z
**closed:** 20260616T1624Z
**owner:** 0.7.0_AE_CloudOps
**project / TO:** NFRA_GCONTR (EC2-WRITES derive gap)
**authorization:** JOINT GATE -- COO operational GO 162005Z + CTO concur 162018Z (additive read-only IAM, AE-autonomous via safe-apply, no Andrew gate)
**code commit:** 2895884ad (WARN comp_aws_cli.py:1638 + item2a.tf +iam:GetInstanceProfile)

## What
Add iam:GetInstanceProfile to the derive_runner_task role (so the Fargate derive can resolve
instance-profile -> role -> emit EC2-producer WRITES edges) + a LOUD WARN replacing the silent
except that hid the gap. Closes the estate-wide 0-EC2-WRITES-edges blind spot (NNA + platinum/firm
become graph_contracts Q2-resolvable).

## Legs -- DEPLOY LEGS ALL LANDED (L5 = deferred next-morning verify)
- [x] L1: comp-iam gaps -> Total: 0 missing | 202 deny-present | 0 coverage-unknown = 0 NEW gaps
- [x] L2: terraform plan -> Plan: 0 add, 1 change, 0 destroy = exactly `+ iam:GetInstanceProfile` on derive_runner_describe, 0 unrelated drift; HALTGT cleared
- [x] L3: safe-apply (saved plan ec2writes.tfplan) -> Apply complete 0/1/0; re-plan = "No changes" (0-diff verified)
- [x] L4: derive image rebuilt -> CodeBuild e6d47d7b SUCCEEDED -> ECR :latest (carries the EC2_WRITES_PROFILE_RESOLVE_FAIL WARN; perm live via L3)
- [ ] L5 (DEFERRED, event-driven next-morning): SCHEDULED nightly derive (02:00Z) emits EC2-WRITES edges; comp-kuzu EC2 WRITES > 0; bd-exporter-ec2-role -> opal-data-bd. NO ad-hoc derive (per discipline). Then CVO re-verifies NNA + EC2 surfaces Q2-resolvable -> unblocks the held NNA policy limb.

## Closure note
DEPLOY is COMPLETE (iam.tf applied 0-diff + WARN image in ECR; both legs in-session, no stranded leg).
L5 is OBSERVATION of the scheduled nightly (not an ad-hoc run) -> tracked as a next-morning artifact
review, NOT a half-deploy. code 2895884ad; CodeBuild e6d47d7b; safe-apply 0/1/0.

## Close criteria
iam.tf applied 0-diff + image rebuilt (both legs landed). L5 verification is the next nightly's
artifacts (event-driven, next-morning review). Then RAVC2 COO+CTO; ping CVO to re-verify NNA + EC2 surfaces.

## Rollback
Additive read-only IAM perm -- removable via a reverting safe-apply (recoverable). No data path touched.

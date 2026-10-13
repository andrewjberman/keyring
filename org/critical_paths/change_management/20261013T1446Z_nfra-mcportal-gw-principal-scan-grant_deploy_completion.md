# Deploy Completion Record
**Date opened:** 2026-10-13T14:46:12.836192+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261013T151747Z
**Deploy:** NFRA_MCPORTAL MP-z-4: one dynamodb:Scan grant on gateway-access-state-table for opal-gateway-role (never-widen pair SIGNED: CTO~Z @d9b228d530, COO~MP @b12118d890)
**Authored by:** 0.7.0_AE_CloudOps~MQ
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | aws_iam_role_policy.gw_access_state_principal_scan (safe-apply of the saved targeted plan .build/z4.tfplan) | terraform apply output showing 1 added 0 changed 0 destroyed, plus a 0-diff targeted re-plan | safe-apply.sh -chdir=infra/aws/terraform/opal-gateway apply .build/z4.tfplan -> rc=0, 2026-10-13 ~14:5xZ. NOTE ON THE APPLY SUMMARY LINE: the invocation was piped through tail -30 and the "Apply complete! Resources: ..." line was cut by my own tail, so it is NOT quoted here and I will not reconstruct it. The resource IS applied, proven on two planes instead: (a) terraform state show aws_iam_role_policy.gw_access_state_principal_scan reads id=opal-gateway-role:gateway-access-state-principal-scan-policy with one statement, Action ["dynamodb:Scan"], Resource ["arn:aws:dynamodb:us-east-1:313476888478:table/gateway-access-state-table"], Sid AccessStatePrincipalScanOnly, no Condition; (b) the 0-DIFF TARGETED RE-PLAN required by this leg: terraform plan -detailed-exitcode -target=aws_iam_role_policy.gw_access_state_principal_scan -> "No changes. Your infrastructure matches the configuration.", detailed exit code 0 (2 would mean changes present). The plan applied was the SAVED targeted plan (COO half condition 1); the opal-gateway Terraform did not move between plan and apply (git diff 6fe140d0a8..HEAD over infra/aws/terraform/opal-gateway/ = only my own new file), so no re-plan was owed. The entry and its sentinel were committed before the act at bb2470d479 (COO half condition 2). | CLOSED 20261013T151158Z |
| L2 | verify | live IAM read-back of gateway-access-state-principal-scan-policy on opal-gateway-role | z4.AC1.sh RESULT: PASS -- actions=dynamodb:Scan resources=1 problems=0 and 4 of 4 simulation arms | z4.AC1.sh RESULT: PASS, exit=0, run from the worktree root 2026-10-13 ~14:5xZ. Live IAM, not state: aws iam get-role-policy --role-name opal-gateway-role --policy-name gateway-access-state-principal-scan-policy parsed to "actions=dynamodb:Scan resources=1 problems=0" (every statement Allow, no NotAction/NotResource, action set exactly {dynamodb:Scan}, resource set exactly the one table ARN). Then 4 of 4 simulate-principal-policy arms, ONE --resource-arns per call, each its own invocation (Rule 22a): scan access-state allowed; scan mcportal-grant-changes-table allowed (pre-existing control, unchanged); scan opal-users-v2 implicitDeny (the refused arm -- no other table); getitem access-state allowed (pre-existing strong read, unchanged). The allowed arms are read together with the refused one, never alone: an allowed proves the pattern matches the string typed, and the simulation ran AFTER the resource existed, never as its pre-apply proof. | CLOSED 20261013T151200Z |

## Log

- 20261013T144612Z OPENED by 0.7.0_AE_CloudOps~MQ with 2 leg(s)
- 20261013T151158Z LEG L1 closed: safe-apply.sh -chdir=infra/aws/terraform/opal-gateway apply .build/z4.tfplan -> rc=0, 2026-10-13 ~14:5xZ. NOTE ON THE AP
- 20261013T151200Z LEG L2 closed: z4.AC1.sh RESULT: PASS, exit=0, run from the worktree root 2026-10-13 ~14:5xZ. Live IAM, not state: aws iam get-role-pol
- 20261013T151747Z CLOSED -- all 2 legs proven

# Deploy Completion Record
**Date opened:** 2026-09-11T00:04:39.757689+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260911T001606Z
**Deploy:** IRPT_BCKEND IB-s-8: apply the investor-reporting/ycharts root -- YCharts runner host APPLIED STOPPED, its role, its security group and the two SSM documents
**Authored by:** 0.9.0_WK_IRPT_BCKEND~3
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | terraform root infra/aws/terraform/investor-reporting/ycharts (state key investor-reporting/ycharts/tfstate) -- 9 resources ADD, 0 change, 0 destroy | safe-apply Apply complete line | safe-apply 2026-09-11T00:05-00:06Z: 'Apply complete! Resources: 9 added, 0 changed, 0 destroyed.' -- aws_instance.runner i-0167fd745ad906a66, aws_iam_role.runner arn:aws:iam::313476888478:role/irpt-ycharts-runner-role, aws_security_group.runner sg-0f643b4963ad6ff15, aws_ec2_instance_state.runner, aws_iam_role_policy.runner, aws_iam_role_policy_attachment.runner_ssm, aws_iam_instance_profile.runner, aws_ssm_document.deploy irpt-ycharts-deploy, aws_ssm_document.run irpt-ycharts-run | CLOSED 20260911T001534Z |
| L2 | verify | the host is STOPPED on the live plane | aws ec2 describe-instances State.Name == stopped | aws ec2 describe-instances --instance-ids i-0167fd745ad906a66 -> {"Id":"i-0167fd745ad906a66","State":"stopped","Type":"t3.medium","Profile":"arn:aws:iam::313476888478:instance-profile/irpt-ycharts-runner-profile"} -- the host is STOPPED on the live plane, as aws_ec2_instance_state declares | CLOSED 20260911T001534Z |
| L3 | verify | the root is CONVERGED after the apply | terraform plan: No changes. Your infrastructure matches the configuration. | terraform.exe -chdir=infra/aws/terraform/investor-reporting/ycharts plan -no-color -input=false -lock=false -> 'No changes. Your infrastructure matches the configuration.' rc=0, taken after the apply | CLOSED 20260911T001534Z |
| L4 | git | the runner, the terraform, the ledger sentinel and the deliverables on wk-irpt_bckend-1-3 | commit hash | commit ff12d98c4d on wk-irpt_bckend-1-3 (LOCAL, worker branch -- a worker never pushes): the runner, its tests, the four .tf files, PATH_MANIFEST.json and this ledger entry with its sentinel | CLOSED 20260911T001534Z |

## Log

- 20260911T000439Z OPENED by 0.9.0_WK_IRPT_BCKEND~3 with 4 leg(s)
- 20260911T001534Z LEG L1 closed: safe-apply 2026-09-11T00:05-00:06Z: 'Apply complete! Resources: 9 added, 0 changed, 0 destroyed.' -- aws_instance.runner
- 20260911T001534Z LEG L2 closed: aws ec2 describe-instances --instance-ids i-0167fd745ad906a66 -> {"Id":"i-0167fd745ad906a66","State":"stopped","Type":"t
- 20260911T001534Z LEG L3 closed: terraform.exe -chdir=infra/aws/terraform/investor-reporting/ycharts plan -no-color -input=false -lock=false -> 'No chang
- 20260911T001534Z LEG L4 closed: commit ff12d98c4d on wk-irpt_bckend-1-3 (LOCAL, worker branch -- a worker never pushes): the runner, its tests, the four
- 20260911T001606Z CLOSED -- all 4 legs proven

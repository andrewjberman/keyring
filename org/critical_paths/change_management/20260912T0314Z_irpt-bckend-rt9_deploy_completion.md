# Deploy Completion Record
**Date opened:** 2026-09-12T03:14:23.872682+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260912T032740Z
**Deploy:** IB-rt-9 arm (e): the research root ABSORBED into the ycharts root -- import + state rm, no resource destroyed, then the research root deleted from the tree
**Authored by:** 0.9.0_WK_IRPT_BCKEND~3
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | terraform plan investor-reporting/ycharts | the pre-move plan shows EXACTLY the two absorbed resources to ADD and nothing else: 'Plan: 2 to add, 0 to change, 0 to destroy' | pre-move plan of investor-reporting/ycharts (vendored .tools/terraform.exe v1.9.8 after init): '# aws_cloudwatch_log_group.research_probe will be created', '# aws_secretsmanager_secret.research_session will be created', 'Plan: 2 to add, 0 to change, 0 to destroy' -- EXACTLY the two absorbed resources and nothing else; the root read 'No changes' immediately before research_absorbed.tf was added. Saved: deliverables/0.9.0_WK_IRPT_BCKEND~3/IB-rt-9_arm_e_premove_plan.txt | CLOSED 20260912T032648Z |
| L2 | activation | terraform import into investor-reporting/ycharts | both resources present in the ycharts state list; import BEFORE state rm so no failure can leave them unowned | terraform import x2 into the ycharts root, both 'Import successful!': aws_secretsmanager_secret.research_session (arn ...secret:ycharts/session/research-20260911-FQCIve) and aws_cloudwatch_log_group.research_probe (/aws/lambda/irpt-ycharts-research-20260911). ycharts state list went 17 -> 19 and carries both addresses. TRAP PAID: the log-group id begins with a slash and Git Bash rewrote it to 'C:/Program Files/Git/aws/lambda/...' -- the first attempt failed InvalidParameterException on logGroupNamePrefix and MSYS_NO_PATHCONV=1 was required; the piped rc read 0 on that failure because a pipeline's rc is its LAST command's, so the ERROR TEXT was the reading, not the rc | CLOSED 20260912T032648Z |
| L3 | activation | terraform state rm in investor-reporting/ycharts-research-20260911 | the research state list is EMPTY and neither resource was destroyed (state rm forgets, never deletes) | terraform state rm x2 in the research root: 'Removed aws_secretsmanager_secret.session', 'Removed aws_cloudwatch_log_group.probe', 'Successfully removed 1 resource instance(s).' each; research state list is now 0 line(s). NEITHER OBJECT WAS DESTROYED, verified INDEPENDENTLY of terraform: describe-secret returns ycharts/session/research-20260911 with its ARN and describe-log-groups returns /aws/lambda/irpt-ycharts-research-20260911 retention 7 -- state rm forgets, it never deletes | CLOSED 20260912T032648Z |
| L4 | activation | safe-apply.sh apply investor-reporting/ycharts | the apply changes ONLY the two absorbed resources' tags (default_tags adds Project=OpalPortal); 0 to add, 0 to destroy | HALT_ACK=1 bash .tools/safe-apply.sh -chdir=infra/aws/terraform/investor-reporting/ycharts apply -input=false -auto-approve: halt gate fired ('worker 0.9.0_WK_IRPT_BCKEND~3 has no inbox; scanning its issuer 2.0.0_SA_COO~B'), then 'Plan: 0 to add, 2 to change, 0 to destroy' and 'Apply complete! Resources: 0 added, 2 changed, 0 destroyed.' THE ONLY WORLD CHANGE, read off the plan diff: tags_all gains Project=OpalPortal on each absorbed resource (this root's default_tags), plus force_overwrite_replica_secret=false and recovery_window_in_days=7 written into state for the secret, which import does not read and which are already the live values. No replace, no destroy, no rename. Owner=4.0.0_SA_CRO and Purpose=YChartsBoundaryTest carried VERBATIM | CLOSED 20260912T032740Z |
| L5 | verify | terraform plan investor-reporting/ycharts | post-apply plan reads 'No changes. Your infrastructure matches the configuration.' | post-apply terraform plan of investor-reporting/ycharts: 'No changes. Your infrastructure matches the configuration.' ycharts state list holds 19 resources including aws_cloudwatch_log_group.research_probe and aws_secretsmanager_secret.research_session | CLOSED 20260912T032740Z |
| L6 | verify | aws ec2 describe-instances i-0167fd745ad906a66 | the runner host reads STOPPED, read live and not asserted from the .tf | aws ec2 describe-instances --instance-ids i-0167fd745ad906a66 --query Reservations[].Instances[].[InstanceId,State.Name] -> 'i-0167fd745ad906a66 stopped', read LIVE from the control plane and not asserted from instance.tf. Bound 1 holds: no login, no capture, no vendor call rode on any of this | CLOSED 20260912T032740Z |

## Log

- 20260912T031423Z OPENED by 0.9.0_WK_IRPT_BCKEND~3 with 6 leg(s)
- 20260912T032648Z LEG L1 closed: pre-move plan of investor-reporting/ycharts (vendored .tools/terraform.exe v1.9.8 after init): '# aws_cloudwatch_log_gro
- 20260912T032648Z LEG L2 closed: terraform import x2 into the ycharts root, both 'Import successful!': aws_secretsmanager_secret.research_session (arn ..
- 20260912T032648Z LEG L3 closed: terraform state rm x2 in the research root: 'Removed aws_secretsmanager_secret.session', 'Removed aws_cloudwatch_log_gro
- 20260912T032740Z LEG L4 closed: HALT_ACK=1 bash .tools/safe-apply.sh -chdir=infra/aws/terraform/investor-reporting/ycharts apply -input=false -auto-appr
- 20260912T032740Z LEG L5 closed: post-apply terraform plan of investor-reporting/ycharts: 'No changes. Your infrastructure matches the configuration.' yc
- 20260912T032740Z LEG L6 closed: aws ec2 describe-instances --instance-ids i-0167fd745ad906a66 --query Reservations[].Instances[].[InstanceId,State.Name]
- 20260912T032740Z CLOSED -- all 6 legs proven

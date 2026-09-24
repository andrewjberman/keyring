# Deploy Completion Record
**Date opened:** 2026-09-24T01:50:37.496590+00:00
**Status:** OPEN
**Deploy:** IRPT resident cutover infrastructure half: runner resident policy + host running (plan 04c77cbe / 9b6e6fa98e; CTO GO 99936, Y 99916)
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A1 | activation | safe-apply of the SAVED plan 04c77cbe only (1 create / 1 update / 16 no-op) | apply output line + sha of the apply output | safe-apply of the SAVED plan .runtime/ycharts-resident/resident.tfplan (sha256 04c77cbe7e1fc4ca... re-read before the act) from the backend worktree ycharts root, HALT_ACK=1: aws_iam_role_policy.runner_resident Creation complete [irpt-ycharts-runner-role:irpt-ycharts-runner-resident-policy]; aws_ec2_instance_state.runner Modifications complete after 22s [i-0167fd745ad906a66]; Apply complete 1 added / 1 changed / 0 destroyed rc=0 at 2026-09-24T01:53:01Z; apply.log sha256 37176f79693c96a8... | CLOSED 20260924T015652Z |
| P1 | verify | get-role-policy irpt-ycharts-runner-resident-policy equals the decoded document (6 statements, resource lists equal) | decoded policy diff | iam get-role-policy irpt-ycharts-runner-role/irpt-ycharts-runner-resident-policy (readback-policy.json): 6 statements ConsumeTheGenerationQueue, JobStateAcceptanceAndRetainedIndexes, TransactionalPublication, RetainVendorPdfEvidenceAndCertifiedAnalysis, ReadFrozenCompositionAndNormalizedInput, ReportEncryptionViaS3ForResidentFamiliesOnly; whole document EQUAL (sort_keys json) to the plan's after.policy; per-statement Resource/Action/Condition equal 6 of 6 | CLOSED 20260924T015652Z |
| I1 | verify | describe-instance-status i-0167fd745ad906a66 running; AutoShutdown=disabled tag present | readback lines | ec2 describe-instances i-0167fd745ad906a66: State running, PublicIp 52.90.35.83, tag AutoShutdown=disabled present; ssm describe-instance-information PingStatus Online agent 3.3.4624.0 (readback-instance.json) | CLOSED 20260924T015652Z |
| V1 | verify | re-plan ycharts root -detailed-exitcode rc 0; recorder | plan rc line | terraform plan -detailed-exitcode ycharts root after the apply: rc 0, 'No changes. Your infrastructure matches the configuration.' (post-plan.log). Recorder: record-terraform-deploy.sh is lambda-function scoped (--function/--all) and this root carries no function, so no recorder row applies; the state itself is the record | CLOSED 20260924T015652Z |
| C1 | verify | cutover receipt with MEASURED booleans (legacy probe off, per-job power cycle off, no other queue consumers, factory installed, enrolled_user_id pinned) | receipt path + sha |  | OPEN |

## Log

- 20260924T015037Z OPENED by 2.0.0_SA_COO~P with 5 leg(s)
- 20260924T015652Z LEG A1 closed: safe-apply of the SAVED plan .runtime/ycharts-resident/resident.tfplan (sha256 04c77cbe7e1fc4ca... re-read before the ac
- 20260924T015652Z LEG P1 closed: iam get-role-policy irpt-ycharts-runner-role/irpt-ycharts-runner-resident-policy (readback-policy.json): 6 statements Co
- 20260924T015652Z LEG I1 closed: ec2 describe-instances i-0167fd745ad906a66: State running, PublicIp 52.90.35.83, tag AutoShutdown=disabled present; ssm 
- 20260924T015652Z LEG V1 closed: terraform plan -detailed-exitcode ycharts root after the apply: rc 0, 'No changes. Your infrastructure matches the confi

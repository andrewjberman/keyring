# Deploy Completion Record
**Date opened:** 2026-07-08T19:06:11.337246+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260708T190921Z
**Deploy:** NFRA_WEBSITE Patricia scoped IAM + DLM EBS snapshots (Andrew-direct)
**Authored by:** 0.7.0_AE_CloudOps~A
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | iam_patricia.tf + dlm.tf on CLOUD ae3a41c7e | hash pushed | iam_patricia.tf + dlm.tf committed ae3a41c7e (+ earlier e090fa6c8) and pushed to CLOUD | CLOSED 20260708T190921Z |
| L2 | verify | 5 resources applied via safe-apply + 0-diff re-plan | apply 5/0/0 + 0-diff | safe-apply(HALTGT) 5 added/0/0 (DLM policy-0c0c24e7981c5522c + role + attach + Patricia user + inline policy); 0-diff re-plan = No differences | CLOSED 20260708T190856Z |
| L3 | verify | Patricia console login profile CLI-created reset-required | create-login-profile output | aws iam create-login-profile OK: user patricia@thewhitelabelcreative.com, PasswordResetRequired=true. NOTE: AWS default password baseline rejected the initially-chosen value (all-lowercase+digits; needs uppercase or symbol) -> a minimal-compliant variant was set (VALUE NOT RECORDED HERE -- held out-of-band, flagged to Andrew; password rotated after this ledger to void an earlier in-proof value). Delivery HELD. | CLOSED 20260708T190857Z |
| L4 | verify | applied Patricia policy scope live-confirmed firm-sep | live get-user-policy | Live get-user-policy = 8 scoped SIDs (Describe/Control/SsmStartSession/SsmSessionControl/SsmReadState/BackupBucketFull/WebsiteLogsRead/SelfManageCredsMfa); ZERO attached managed; grep of applied policy = no opal-data/SM/lambda-artifacts/other-bucket -> firm-sep confirmed applied | CLOSED 20260708T190858Z |

## Log

- 20260708T190611Z OPENED by 0.7.0_AE_CloudOps~A with 4 leg(s)
- 20260708T190856Z LEG L2 closed: safe-apply(HALTGT) 5 added/0/0 (DLM policy-0c0c24e7981c5522c + role + attach + Patricia user + inline policy); 0-diff re
- 20260708T190857Z LEG L3 closed: aws iam create-login-profile OK: user patricia@thewhitelabelcreative.com, PasswordResetRequired=true. NOTE: AWS default 
- 20260708T190858Z LEG L4 closed: Live get-user-policy = 8 scoped SIDs (Describe/Control/SsmStartSession/SsmSessionControl/SsmReadState/BackupBucketFull/W
- 20260708T190921Z LEG L1 closed: iam_patricia.tf + dlm.tf committed ae3a41c7e (+ earlier e090fa6c8) and pushed to CLOUD
- 20260708T190921Z CLOSED -- all 4 legs proven

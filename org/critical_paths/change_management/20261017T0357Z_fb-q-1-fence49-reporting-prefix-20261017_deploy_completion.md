# Deploy Completion Record
**Date opened:** 2026-10-17T03:57:24.963230+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261017T040215Z
**Deploy:** ADVI_FIRMBKTS TO-FB-q-1 (WORLD): regenerate the opal-data-49financial bucket policy so irpt-export-render-role gains GetObject on irpt/49financial/platinum/reporting/ (Deny NotResource + Allow Resource, one entry each); ONE targeted safe-apply of aws_s3_bucket_policy.opal_data_49financial, plan 0 add 1 change 0 destroy; pair COO 300f9d398d + CTO 1045f1b75b; reach ruling c783217cff
**Authored by:** 0.7.0_AE_CloudOps~ADVI1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | FENCE49_RECORD.json plus proof instance plus this ledger, committed with explicit paths | commit hash | git: record commit cb5ee5e9c5 on box/laptop (FENCE49_RECORD.json; grader fence49 OK applies=1); proof instance follows in the status commit; push state LOCAL | CLOSED 20261017T040214Z |
| L2 | activation | ONE scoped safe-apply of aws_s3_bucket_policy.opal_data_49financial | apply output: 0 added, 1 changed, 0 destroyed | safe-apply rc=0 from tree c45b4f09c2, saved plan, 1 target: 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.' tagauthz PASSED, tombstone CLEAN; one apply, no second | CLOSED 20261017T040214Z |
| L3 | verify | get-bucket-policy read back: two statements changed by one entry each, every other statement byte-equal to the saved prior JSON | per-statement diff counts | get-bucket-policy read back 2026-10-17: 37 statements before and after, 0 added, 0 removed; changed DenyScopedExemption3ObjectsOutsidePrefix (NotResource +1) and AllowScopedExemption3Objects (Resource +1), each by the reporting prefix entry only; 35 of 35 others byte-equal to saved prior JSON; Allow Resource includes prefix, action s3:GetObject only | CLOSED 20261017T040214Z |
| L4 | verify | post-apply scoped plan reads No changes | plan output | post-apply scoped plan -detailed-exitcode: exit 0, No changes. Your infrastructure matches the configuration. | CLOSED 20261017T040215Z |

## Log

- 20261017T035724Z OPENED by 0.7.0_AE_CloudOps~ADVI1 with 4 leg(s)
- 20261017T040214Z LEG L1 closed: git: record commit cb5ee5e9c5 on box/laptop (FENCE49_RECORD.json; grader fence49 OK applies=1); proof instance follows i
- 20261017T040214Z LEG L2 closed: safe-apply rc=0 from tree c45b4f09c2, saved plan, 1 target: 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.
- 20261017T040214Z LEG L3 closed: get-bucket-policy read back 2026-10-17: 37 statements before and after, 0 added, 0 removed; changed DenyScopedExemption3
- 20261017T040215Z LEG L4 closed: post-apply scoped plan -detailed-exitcode: exit 0, No changes. Your infrastructure matches the configuration.
- 20261017T040215Z CLOSED -- all 4 legs proven

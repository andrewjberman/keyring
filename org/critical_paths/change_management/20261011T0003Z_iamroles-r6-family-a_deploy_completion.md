# Deploy Completion Record
**Date opened:** 2026-10-11T00:03:49.068421+00:00
**Status:** HELD-PRE-APPLY -- gate: external / naming-gate OLDER-limb carrier refusal on the 'bd' firm token (row Z-S34): both adopted role names are refused as NEW hand-kept carriers of 'bd' (read through lookup('49financial')), and the audited placement override does NOT reach that limb -- measured on two runs, the gate prints no NAMING-PLACE line at all. Remedy is an R20 declared exception or a registry row under infra/logic/registry/, owner 1.0.0_SA_CTO~Z, acknowledged by Andrew per CLAUDE.md Rule 30. NOTHING WAS APPLIED: bd-pipeline state holds 0 of the 2 roles (17 aws_iam_role entries as the positive control) and both roles read Tags [] (held since 2026-10-11T00:28:04.578409+00:00)
**Deploy:** NFRA_IAMROLES202609 IAM-w-2 PHASE B: adopt bd-merge-daily-lambda-role and bd-pipeline-task-role into bd-pipeline (-target import + four default tags each)
**Authored by:** 0.7.0_AE_CloudOps~IR
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| TF | activation | aws_iam_role.bd_merge_daily_lambda_role + aws_iam_role.bd_pipeline_task_role | the SAVED targeted plan reads 2 to import / 0 to add / 2 to change / 0 to destroy, tags_all is the only changed attribute on each of the two roles, the four keys are exactly Environment ManagedBy Project System, and NO other address is listed (205 resource_changes, 2 non-no-op) -- anything else is a STOP and nothing is applied |  | OPEN |
| TAGS | verify | bd-merge-daily-lambda-role + bd-pipeline-task-role | LIVE after the apply: list-role-tags reads exactly those four keys on BOTH roles; list-role-policies still reads one inline policy each (bd-merge-daily-policy; BDPipelineTaskPolicy) with 0 attached managed policies; and get-role shows row 2 trust principal STILL ecs-tasks.amazonaws.com -- the pair names that trust as a branch condition, not a hope |  | OPEN |
| REPLAN | verify | infra/aws/terraform/bd-pipeline | the targeted re-plan reads 0 to add, 0 to change, 0 to destroy, recorded in POST_APPLY_family_a.md beside the untargeted module plan; AND after the drain the untargeted plan in the SHARED tree reads 0 to destroy (A4-r6, row Z-S27) |  | OPEN |

## Log

- 20261011T000349Z OPENED by 0.7.0_AE_CloudOps~IR with 3 leg(s)
- 20261011T002804Z HELD-PRE-APPLY gate=external/naming-gate OLDER-limb carrier refusal on the 'bd' firm token (row Z-S34): both 

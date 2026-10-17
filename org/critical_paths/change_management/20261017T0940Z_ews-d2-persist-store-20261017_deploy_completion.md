# Deploy Completion Record
**Date opened:** 2026-10-17T09:40:01.965942+00:00
**Status:** OPEN
**Deploy:** TCKT_EARLYWARN TO-EWS-d2: ews launcher logs items_opened per rule and persists its open-items store to s3://opal-data-49financial/schwab/49financial/state/ews_store/current/ews.db; fence admission for opal-clientops-ews-role (Get/List/Put, that prefix only) on opal-data-49financial; image rebuilt through opal-clientops-ews-build. Only task family pulling the opal-clientops-ews-task repo tag is opal-clientops-ews-task (one describe-task-definition family sweep: 1 family). One-time cost: the replacement task replays 573 dates (~3.5h at 0.25 vCPU), no resize.
**Authored by:** 0.7.0_AE_CloudOps~TM1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | exemptions.json row + module (role grant, task env) + Dockerfile + ledger sentinel committed with explicit paths | commit ids recorded |  | OPEN |
| L2 | tf-lambda | safe-apply of infra/aws/terraform/shared-infra: opal-data-49financial DenyForeignFirmPrincipals admits opal-clientops-ews-role, plan touching ONLY that bucket policy | plan resource list, replan No changes for the 49financial policy, live policy read shows the one new entry |  | OPEN |
| L3 | s3-prefix | image build source zip re-landed under s3://opal-313476888478-lambda-artifacts/client-ops-early-warning/ | landed sha256 equals the staged zip |  | OPEN |
| L4 | activation | CodeBuild start-build pushes the new image to opal-clientops-ews-task | build SUCCEEDED, digest read from ECR describe-images |  | OPEN |
| L5 | tf-lambda | safe-apply of infra/aws/terraform/client-ops-early-warning: task role store grant, task env EWS_PERSIST_*, new task definition by digest, service replaces the task | plan resource list, replan No changes, exactly one task RUNNING on the new definition |  | OPEN |
| L6 | verify | ews_check.py running, iam, ledger, persist-iam and the manifest persist_bucket/persist_key | EWS-RUN-OK, EWS-IAM-OK, EWS-LED-OK, EWS-PIAM-OK |  | OPEN |
| L7 | verify | new task first pass ends: ews_check.py counts and persist-object | EWS-CNT-OK, EWS-POBJ-OK |  | OPEN |

## Log

- 20261017T094001Z OPENED by 0.7.0_AE_CloudOps~TM1 with 7 leg(s)

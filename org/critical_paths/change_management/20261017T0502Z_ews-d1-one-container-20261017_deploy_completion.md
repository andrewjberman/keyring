# Deploy Completion Record
**Date opened:** 2026-10-17T05:02:29.380730+00:00
**Status:** OPEN
**Deploy:** TCKT_EARLYWARN TO-EWS-d1: the Client Ops Early Warning runtime as ONE always-on Fargate task (own cluster opal-clientops-ews-cluster, new ECR repo, new CodeBuild image build); Schwab daily rules on, mail poller off by launcher. New repo and new task family: no other task family pulls the image tag it moves (the repo is created by this deploy).
**Authored by:** 0.7.0_AE_CloudOps~TM1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | module infra/aws/terraform/client-ops-early-warning + Dockerfile + this ledger sentinel committed with explicit paths | commit ids recorded |  | OPEN |
| L2 | s3-prefix | image build source zip under s3://opal-313476888478-lambda-artifacts/client-ops-early-warning/ | landed sha256 equals the staged zip | s3://opal-313476888478-lambda-artifacts/client-ops-early-warning/ews_ctx.zip VersionId QtvPsw4UXH.f9_D9CbL6R5fLjBIbh__A, 274901 bytes; landed sha256 79421db0153b6a3c73f0880116e67b16be50d2c88c1d939905f2adfeb479313f equals the staged zip (re-downloaded and hashed) | CLOSED 20261017T050747Z |
| L3 | tf-lambda | safe-apply 1 of infra/aws/terraform/client-ops-early-warning: ECR repo, CodeBuild project and roles, cluster, log group, security group, task and execution roles (no task, no service) | plan resource list, replan No changes |  | OPEN |
| L4 | activation | CodeBuild start-build pushes the image to the new ECR repo | build SUCCEEDED, image digest read from ECR describe-images |  | OPEN |
| L5 | tf-lambda | safe-apply 2: the task definition (image by digest) and the one-task service | plan resource list, replan No changes |  | OPEN |
| L6 | verify | ews_check.py running, iam and ledger arms and the deploy manifest EWS_DEPLOY.json | EWS-RUN-OK, EWS-IAM-OK, EWS-LED-OK |  | OPEN |

## Log

- 20261017T050229Z OPENED by 0.7.0_AE_CloudOps~TM1 with 6 leg(s)
- 20261017T050747Z LEG L2 closed: s3://opal-313476888478-lambda-artifacts/client-ops-early-warning/ews_ctx.zip VersionId QtvPsw4UXH.f9_D9CbL6R5fLjBIbh__A,

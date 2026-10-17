# Deploy Completion Record
**Date opened:** 2026-10-17T05:02:29.380730+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261017T054943Z
**Deploy:** TCKT_EARLYWARN TO-EWS-d1: the Client Ops Early Warning runtime as ONE always-on Fargate task (own cluster opal-clientops-ews-cluster, new ECR repo, new CodeBuild image build); Schwab daily rules on, mail poller off by launcher. New repo and new task family: no other task family pulls the image tag it moves (the repo is created by this deploy).
**Authored by:** 0.7.0_AE_CloudOps~TM1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | module infra/aws/terraform/client-ops-early-warning + Dockerfile + this ledger sentinel committed with explicit paths | commit ids recorded | committed with explicit paths on box/dell1: 4eaf095926 (module, Dockerfile, ledger open) and 0ab8f5225b (Dockerfile trading_calendar fix, manifest, surprise rows); push state LOCAL, box-sync pushes | CLOSED 20261017T052841Z |
| L2 | s3-prefix | image build source zip under s3://opal-313476888478-lambda-artifacts/client-ops-early-warning/ | landed sha256 equals the staged zip | s3://opal-313476888478-lambda-artifacts/client-ops-early-warning/ews_ctx.zip VersionId QtvPsw4UXH.f9_D9CbL6R5fLjBIbh__A, 274901 bytes; landed sha256 79421db0153b6a3c73f0880116e67b16be50d2c88c1d939905f2adfeb479313f equals the staged zip (re-downloaded and hashed) | CLOSED 20261017T050747Z |
| L3 | tf-lambda | safe-apply 1 of infra/aws/terraform/client-ops-early-warning: ECR repo, CodeBuild project and roles, cluster, log group, security group, task and execution roles (no task, no service) | plan resource list, replan No changes | safe-apply 1 of infra/aws/terraform/client-ops-early-warning: Apply complete, 15 added 0 changed 0 destroyed (plan file planned moments before); replan No changes | CLOSED 20261017T051106Z |
| L4 | activation | CodeBuild start-build pushes the image to the new ECR repo | build SUCCEEDED, image digest read from ECR describe-images | CodeBuild opal-clientops-ews-build:2c3a3758-6a38-45e8-bc25-8cf8d1693f5b SUCCEEDED; ECR describe-images read: tag ews-20261017T051135Z digest sha256:5d68df7ee4dbde7d2f4fa5503924f65f1e2401c74f47911defa47697942b867d, 154874649 bytes | CLOSED 20261017T051228Z |
| L5 | tf-lambda | safe-apply 2: the task definition (image by digest) and the one-task service | plan resource list, replan No changes | safe-apply 2 (task def :1 + service, image 5d68df7e..), a launcher defect then found (lib/trading_calendar.py absent from image; log: run_pending failed type=ModuleNotFoundError), image rebuilt (CodeBuild 6fe0270a, digest sha256:2c1aef59b3d3fb0b88591faa5e80e46d75f25fc191b02124752805b3e634a86b), safe-apply 3: 1 added 1 changed 1 destroyed, service on task-definition :2; replan No changes; exactly one task RUNNING (73ccdcc4753448c68c1dd7156111588a) | CLOSED 20261017T052628Z |
| L6 | verify | ews_check.py running, iam and ledger arms and the deploy manifest EWS_DEPLOY.json | EWS-RUN-OK, EWS-IAM-OK, EWS-LED-OK | ews_check.py running: EWS-RUN-OK (task 73ccdcc4.. RUNNING, 1 container, 1 task in cluster). ews_check.py iam as written: EWS-BAD rc=254 (lone '*' wildcard-expanded by aws.exe on dell1, row TCKT_EARLYWARN-D1-S3); the same code with only the aws cwd set to an empty dir: EWS-IAM-OK. Manifest EWS_DEPLOY.json written. ledger arm runs after this close. | CLOSED 20261017T054943Z |

## Log

- 20261017T050229Z OPENED by 0.7.0_AE_CloudOps~TM1 with 6 leg(s)
- 20261017T050747Z LEG L2 closed: s3://opal-313476888478-lambda-artifacts/client-ops-early-warning/ews_ctx.zip VersionId QtvPsw4UXH.f9_D9CbL6R5fLjBIbh__A,
- 20261017T051106Z LEG L3 closed: safe-apply 1 of infra/aws/terraform/client-ops-early-warning: Apply complete, 15 added 0 changed 0 destroyed (plan file 
- 20261017T051228Z LEG L4 closed: CodeBuild opal-clientops-ews-build:2c3a3758-6a38-45e8-bc25-8cf8d1693f5b SUCCEEDED; ECR describe-images read: tag ews-202
- 20261017T052628Z LEG L5 closed: safe-apply 2 (task def :1 + service, image 5d68df7e..), a launcher defect then found (lib/trading_calendar.py absent fro
- 20261017T052841Z LEG L1 closed: committed with explicit paths on box/dell1: 4eaf095926 (module, Dockerfile, ledger open) and 0ab8f5225b (Dockerfile trad
- 20261017T054943Z LEG L6 closed: ews_check.py running: EWS-RUN-OK (task 73ccdcc4.. RUNNING, 1 container, 1 task in cluster). ews_check.py iam as written:
- 20261017T054943Z CLOSED -- all 6 legs proven

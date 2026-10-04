# Deploy Completion Record
**Date opened:** 2026-10-04T19:11:10.141871+00:00
**Status:** OPEN
**Deploy:** IRPT_YCDGEN close: Cottonwood research principal irpt-cot-ycharts-research-role (assumed by the runner role) replaces the inert host-role grant; row IRPT_YCDGEN-S1; packet blob 97578e0eda
**Authored by:** 2.0.0_SA_COO~Y
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| D1 | activation | ONE targeted safe-apply of aws_iam_role.ycdgen_research, aws_iam_role_policy.ycdgen_research, aws_iam_role_policy.runner_resident (2 add, 1 change) | safe-apply rc + get-role/get-role-policy + simulate WITH the bucket policy | safe-apply rc=0 of y_principal_d1.tfplan (2 added, 1 changed, 0 destroyed) ~19:2xZ; after-read 19:22:34Z (close/AFTER_READ_PRINCIPAL_20261004.txt): trust names only irpt-ycharts-runner-role; policy Put/Get on the two research prefixes; host statement AssumeTheFirmResearchPrincipal; WITH the cottonwood bucket policy both research prefixes allowed, ycharts_opal_reports implicitDeny; WITH the 49financial bucket policy explicitDeny; runner sts:AssumeRole allowed | CLOSED 20261004T192316Z |
| V1 | verify | the close run's kept answers and run.json read back from opal-data-cottonwood research tables | keys + sizes read back |  | OPEN |

## Log

- 20261004T191110Z OPENED by 2.0.0_SA_COO~Y with 2 leg(s)
- 20261004T192316Z LEG D1 closed: safe-apply rc=0 of y_principal_d1.tfplan (2 added, 1 changed, 0 destroyed) ~19:2xZ; after-read 19:22:34Z (close/AFTER_RE

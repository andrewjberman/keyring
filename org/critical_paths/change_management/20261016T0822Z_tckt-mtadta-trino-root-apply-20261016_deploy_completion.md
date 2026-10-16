# Deploy Completion Record
**Date opened:** 2026-10-16T08:22:53.812739+00:00
**Status:** OPEN
**Deploy:** TCKT_MTADTA round 2: apply the trino root (new resources only)
**Authored by:** 0.7.0_AE_CloudOps~TM1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| apply | activation | infra/aws/terraform/trino (safe-apply, create-only plan) | plan shows only creates, 0 destroy/replace; safe-apply rc=0; replan exit 0 |  | OPEN |
| bucket-policy | verify | opal-data-trino bucket policy | r2_check_r1.py applied prints R1-APPLIED-OK |  | OPEN |
| key-policy | verify | trino CMK key policy (root + access role only) | r2_check_r1.py applied prints R1-APPLIED-OK |  | OPEN |
| aliases | verify | globgrph-trino-access-lambda aliases collector + member | r2_check_r1.py applied prints R1-APPLIED-OK |  | OPEN |
| group | verify | IAM group globgrph-trino-access-group (no member added) | r2_check_r1.py applied prints R1-APPLIED-OK; refusals prints R1-REFUSALS-OK |  | OPEN |

## Log

- 20261016T082253Z OPENED by 0.7.0_AE_CloudOps~TM1 with 5 leg(s)

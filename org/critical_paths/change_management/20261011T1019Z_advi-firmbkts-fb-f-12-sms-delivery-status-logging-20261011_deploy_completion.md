# Deploy Completion Record
**Date opened:** 2026-10-11T10:19:24.235042+00:00
**Status:** OPEN
**Deploy:** ADVI_FIRMBKTS TO-FB-f-12 (laptop, FBL): enable account-level SNS SMS delivery-status logging (role opal-sms-delivery-status-role, DeliveryStatusIAMRole, success sampling 0, two delivery log groups at 14-day retention) via inf-pipeline Terraform and safe-apply; rollback = remove DeliveryStatusIAMRole/sampling (prior: only MonthlySpendLimit 50), role and groups are inert
**Authored by:** 0.7.0_AE_CloudOps~FBL
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | pre-act reads: get-sms-attributes (every attribute), topic attributes, existing sns delivery log groups | printed in the entry |  | OPEN |
| L2 | verify | plan JSON of infra/aws/terraform/inf-pipeline changes EXACTLY role, role policy, 2 log groups, sms preferences | plan summary line |  | OPEN |
| L3 | activation | safe-apply of the saved plan | apply summary |  | OPEN |
| L4 | verify | read-back AC1-AC4 + every other SMS attribute byte-equal + post-apply plan no changes | AC outputs + plan line |  | OPEN |

## Log

- 20261011T101924Z OPENED by 0.7.0_AE_CloudOps~FBL with 4 leg(s)

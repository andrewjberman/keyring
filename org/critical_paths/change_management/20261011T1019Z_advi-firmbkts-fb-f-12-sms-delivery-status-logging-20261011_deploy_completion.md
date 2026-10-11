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
| L1 | verify | pre-act reads: get-sms-attributes (every attribute), topic attributes, existing sns delivery log groups | printed in the entry | get-sms-attributes: MonthlySpendLimit=50 only; topic opal-infrastructure-alerts no delivery-status attributes; no sns/us-east-1/313476888478/ log groups (0); evidence_f12/pre_act_record.txt | CLOSED 20261011T102414Z |
| L2 | verify | plan JSON of infra/aws/terraform/inf-pipeline changes EXACTLY role, role policy, 2 log groups, sms preferences | plan summary line | terraform 1.15.8 plan -target on exactly aws_iam_role.sms_delivery_status, aws_iam_role_policy.sms_delivery_status, aws_cloudwatch_log_group.sns_sms_delivery, aws_cloudwatch_log_group.sns_sms_delivery_failure, aws_sns_sms_preferences.account: 5 resource_changes, 5 create, nothing else (amendment 1); trust sns.amazonaws.com; policy 5 logs actions on the DirectPublishToPhoneNumber* group ARN only; prefs after = monthly_spend_limit 50, sampling 0, role arn known after apply; file plan_targeted_five_final.out | CLOSED 20261011T105141Z |
| L3 | activation | safe-apply of the saved plan | apply summary |  | OPEN |
| L4 | verify | read-back AC1-AC4 + every other SMS attribute byte-equal + post-apply plan no changes | AC outputs + plan line |  | OPEN |

## Log

- 20261011T101924Z OPENED by 0.7.0_AE_CloudOps~FBL with 4 leg(s)
- 20261011T102414Z LEG L1 closed: get-sms-attributes: MonthlySpendLimit=50 only; topic opal-infrastructure-alerts no delivery-status attributes; no sns/us
- 20261011T105141Z LEG L2 closed: terraform 1.15.8 plan -target on exactly aws_iam_role.sms_delivery_status, aws_iam_role_policy.sms_delivery_status, aws_

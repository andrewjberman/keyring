# Deploy Completion Record
**Date opened:** 2026-09-03T23:38:24.167259+00:00
**Status:** OPEN
**Deploy:** NFRA_OPSEC202609.TO-OP-S-6 login-abuse alarm (OP-s-6 / FWD-4) -- the project's ONLY authorised notification: two alarms on the auth path + one SNS topic + one metric filter. The SNS SUBSCRIPTION is DELIBERATELY ABSENT: C-6 needs one named person, nobody has supplied the name, and row NFRA_OPSEC202609-Z-S97 holds that gap ARMED at 2.0.0_SA_COO~Z. BASELINE BEFORE FIRST EDIT, unscoped: 'Plan: 0 to add, 1 to change, 0 to destroy' -- the 1 change is a PRE-EXISTING standing churn on aws_wafv2_web_acl.opal_cloudfront_protection whose removed and added rule blocks are byte-identical after normalisation, is NOT this task order's and must NOT ride this apply
**Authored by:** 0.7.0_AE_CloudOps~T
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | cloudwatch-alarms.tf +4 resources committed under 0.7.0_AE_CloudOps~T, fmt+validate clean, unscoped baseline quoted | commit hash + baseline plan line |  | OPEN |
| L2 | activation | safe-apply TARGETED to exactly the 4 new addresses so the pre-existing web-ACL churn does NOT ride along -- ROLLBACK: terraform destroy -target on the same 4 addresses (2 alarms, 1 metric filter, 1 SNS topic), all additive and independently removable, no existing resource is modified so there is nothing to restore | apply output + enumerated changed-resource list with change types |  | OPEN |
| L3 | verify | S6-AC1 -- both alarms exist on the auth path with MetricName/Namespace/Threshold/ComparisonOperator/AlarmActions pasted, alarm count moved against the face's before-denominator of 49, both addresses in terraform state list | describe-alarms + state list |  | OPEN |
| L4 | verify | S6-AC2 -- the alarm TRANSITIONED on a staged burst, graded on the alarm and not the rule, with the PRE-BURST alarm state stated so the transition is a change and not a standing condition | describe-alarm-history + the WAF BlockedRequests datapoint for the same window |  | OPEN |
| L5 | verify | S6-AC4 -- moratorium census with denominators: exactly 2 alarms, exactly 1 topic, 0 dashboards, 0 additional subscribers, 0 GuardDuty/SecurityHub/Config; control that must be able to fail = account-wide dashboard count unchanged | census with counts + the account-wide control |  | OPEN |
| L6 | verify | S6-AC5 -- UNSCOPED re-plan after the apply, expected to read 4-fewer-to-add with the SAME single pre-existing churn and nothing of this seat's outstanding; push state MEASURED by ls-remote + is-ancestor | re-plan + ls-remote |  | OPEN |

## Log

- 20260903T233824Z OPENED by 0.7.0_AE_CloudOps~T with 6 leg(s)

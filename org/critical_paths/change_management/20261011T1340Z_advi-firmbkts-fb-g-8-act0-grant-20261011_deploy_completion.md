# Deploy Completion Record
**Date opened:** 2026-10-11T13:40:47.317505+00:00
**Status:** OPEN
**Deploy:** ADVI_FIRMBKTS TO-FB-g-8 (window act 0): create ONE inline policy advi-49f-platinum-canonical-rw-policy on role bd-exporter-ec2-role (root infra/aws/terraform/bd-pipeline), the producers' grant for the canonical platinum home; pair COO half @0911fa9901 + CTO half @37ef51525c; rollback = aws iam delete-role-policy of that one name; the QA runner shares the role and is a recipient of the Allow
**Authored by:** 0.7.0_AE_CloudOps~FB1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | pre-write reads: both pair halves SIGNED at the current bytes, the role's 16 inline policies and none of this name, the actor's iam:PutRolePolicy read at the role ARN | the entry carries the read lines |  | OPEN |
| L2 | activation | scoped plan of bd-pipeline (-target module.opal_name_platinum_grant and the policy resource) reads exactly Plan: 1 to add, then .tools/safe-apply.sh on the saved plan | the plan summary line and the apply result line |  | OPEN |
| L3 | verify | AC1 get-role-policy returns the two Sids, AC2 the role holds 17 inline policies, AC3 the scoped plan reads No changes | the three outputs quoted |  | OPEN |
| L4 | git | proof instance written and TO-FB-g-8 status flipped complete in one commit | commit hash |  | OPEN |

## Log

- 20261011T134047Z OPENED by 0.7.0_AE_CloudOps~FB1 with 4 leg(s)

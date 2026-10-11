# Deploy Completion Record
**Date opened:** 2026-10-11T16:10:20.347307+00:00
**Status:** OPEN
**Deploy:** ADVI_FIRMBKTS TO-FB-f-18 (act 4b identity side): ONE inline policy advi-49f-exec-summary-canonical-put-policy on exec-summary-generator-role (root infra/aws/terraform/exec-summary, aws_iam_role_policy.exec_summary_canonical_put): s3:PutObject on arn:aws:s3:::opal-data-49financial/advi/49financial/platinum/advisors/*/exec_summary.json and nothing else; pair act 4b/4c COO half (amended @dd143981f4) + CTO half @6f5335f5c0; rollback = aws iam delete-role-policy of that one name; inert until act 4b moves the generator's mode
**Authored by:** 0.7.0_AE_CloudOps~FB1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | pre-write reads: pair SIGNED at the current bytes, the role's inline policies printed before (the new name absent) | the entry carries the list |  | OPEN |
| L2 | activation | scoped plan of the exec-summary root reads Plan: 1 to add, 0 to change, 0 to destroy (one aws_iam_role_policy); .tools/safe-apply.sh on the saved plan | plan summary line and apply result line |  | OPEN |
| L3 | verify | AC1 the one statement, one action, one resource; AC2 the role holds exactly the legacy policy and the new one; AC3 scoped plan No changes | the three outputs quoted |  | OPEN |
| L4 | git | proof instance written and TO-FB-f-18 status flipped complete in one commit | commit hash |  | OPEN |

## Log

- 20261011T161020Z OPENED by 0.7.0_AE_CloudOps~FB1 with 4 leg(s)

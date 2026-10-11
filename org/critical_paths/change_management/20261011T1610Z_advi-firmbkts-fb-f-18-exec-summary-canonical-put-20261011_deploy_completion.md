# Deploy Completion Record
**Date opened:** 2026-10-11T16:10:20.347307+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261011T161329Z
**Deploy:** ADVI_FIRMBKTS TO-FB-f-18 (act 4b identity side): ONE inline policy advi-49f-exec-summary-canonical-put-policy on exec-summary-generator-role (root infra/aws/terraform/exec-summary, aws_iam_role_policy.exec_summary_canonical_put): s3:PutObject on arn:aws:s3:::opal-data-49financial/advi/49financial/platinum/advisors/*/exec_summary.json and nothing else; pair act 4b/4c COO half (amended @dd143981f4) + CTO half @6f5335f5c0; rollback = aws iam delete-role-policy of that one name; inert until act 4b moves the generator's mode
**Authored by:** 0.7.0_AE_CloudOps~FB1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | pre-write reads: pair SIGNED at the current bytes, the role's inline policies printed before (the new name absent) | the entry carries the list | act 4b/4c COO half (amended, dd143981f4) and CTO half 6f5335f5c0 SIGNED at the current bytes (0 uncommitted); role exec-summary-generator-role inline policies before: exec-summary-generator-policy only, advi-49f-exec-summary-canonical-put-policy absent | CLOSED 20261011T161328Z |
| L2 | activation | scoped plan of the exec-summary root reads Plan: 1 to add, 0 to change, 0 to destroy (one aws_iam_role_policy); .tools/safe-apply.sh on the saved plan | plan summary line and apply result line | scoped plan Plan: 1 to add, 0 to change, 0 to destroy (one aws_iam_role_policy; one statement ExecSummaryCanonicalPut s3:PutObject on arn:aws:s3:::opal-data-49financial/advi/49financial/platinum/advisors/*/exec_summary.json, no Condition); --dry-seat-gates CLEAR; .tools/safe-apply.sh on the saved plan 16:11:49Z-16:12:25Z: Apply complete! Resources: 1 added, 0 changed, 0 destroyed | CLOSED 20261011T161328Z |
| L3 | verify | AC1 the one statement, one action, one resource; AC2 the role holds exactly the legacy policy and the new one; AC3 scoped plan No changes | the three outputs quoted | AC1 ExecSummaryCanonicalPut / s3:PutObject / arn:aws:s3:::opal-data-49financial/advi/49financial/platinum/advisors/*/exec_summary.json; AC2 advi-49f-exec-summary-canonical-put-policy + exec-summary-generator-policy; AC3 No changes. Your infrastructure matches the configuration.; read 2026-10-11T16:12:25Z | CLOSED 20261011T161328Z |
| L4 | git | proof instance written and TO-FB-f-18 status flipped complete in one commit | commit hash | proof instance and act4b_iam evidence committed with this entry; TO-FB-f-18 status flipped complete in the same commit; commit hash is this commit | CLOSED 20261011T161328Z |

## Log

- 20261011T161020Z OPENED by 0.7.0_AE_CloudOps~FB1 with 4 leg(s)
- 20261011T161328Z LEG L1 closed: act 4b/4c COO half (amended, dd143981f4) and CTO half 6f5335f5c0 SIGNED at the current bytes (0 uncommitted); role exec-
- 20261011T161328Z LEG L2 closed: scoped plan Plan: 1 to add, 0 to change, 0 to destroy (one aws_iam_role_policy; one statement ExecSummaryCanonicalPut s3
- 20261011T161328Z LEG L3 closed: AC1 ExecSummaryCanonicalPut / s3:PutObject / arn:aws:s3:::opal-data-49financial/advi/49financial/platinum/advisors/*/exe
- 20261011T161328Z LEG L4 closed: proof instance and act4b_iam evidence committed with this entry; TO-FB-f-18 status flipped complete in the same commit; 
- 20261011T161329Z CLOSED -- all 4 legs proven

## ACT 4B IDENTITY SIDE OUTCOME (0.7.0_AE_CloudOps~FB1, 2026-10-11T16:13:28Z)

- **Pair:** act 4b/4c COO half (amended, last commit `dd143981f4`) and CTO half (`6f5335f5c0`), SIGNED at the current bytes, 0 uncommitted;
  `FB-g-28` merged @ef5c7f45cb.
- **Role's inline policies before:** `exec-summary-generator-policy` (one policy; the new name absent). `evidence/act4b_iam/role_policies_before.txt`.
- **Plan (scoped, saved):** `Plan: 1 to add, 0 to change, 0 to destroy`; one `aws_iam_role_policy` (`exec_summary_canonical_put`), nothing
  else in 2 resource_changes. Document: one statement `ExecSummaryCanonicalPut`, Allow, `s3:PutObject`, one resource
  `arn:aws:s3:::opal-data-49financial/advi/49financial/platinum/advisors/*/exec_summary.json`; no Condition, NotAction, NotResource or
  Principal. `evidence/act4b_iam/analysis_plan.txt`.
- **Seat gates:** `--dry-seat-gates` first: CLEAR (open_call, overlap, upset, open_deploy all clear). No hits to read.
- **Apply:** 16:11:49Z to 16:12:25Z, `Apply complete! Resources: 1 added, 0 changed, 0 destroyed.`
- **After (16:12:25Z):** AC1 one statement, one action, one resource; AC2 the role holds `advi-49f-exec-summary-canonical-put-policy + exec-summary-generator-policy`; AC3 `No changes.`
- **Order against act 3c:** `FB-f-17` applied @5a8c78f135 at 16:07Z; both are now live, so the generator's Put at the canonical home is
  allowed only for `exec_summary.json` under `advisors/`; the move itself is act 4b's, not this entry's.
- **Rollback, unused:** `aws iam delete-role-policy --role-name exec-summary-generator-role --policy-name advi-49f-exec-summary-canonical-put-policy`.

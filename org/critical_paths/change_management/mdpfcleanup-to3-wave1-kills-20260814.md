# DEPLOY LEDGER — OPAL_MDPFCLEANUP.TO-3 wave-1 non-reserved kills (4 class-applies)

**Opened:** 2026-08-14T18:2xZ by 0.7.0_AE_CloudOps (deploy-start; NEVER#6)
**Authority:** Andrew "all recs approved" @874b52729c (TO-1 ratified set); CTO per-apply gates.
**Doctrine:** consumers first, binary last · one class per apply · expected-rows-only plans ·
0-diff + tag each · rollback = same-window revert commit. No reserved acts (EC2/S3 = TO-4).

| Apply | Root | Rows (state addresses) | Status |
|---|---|---|---|
| 1 (K2, ENABLED consumer — starts the TO-4 access-log clock) | smartx-pipeline | event_rule.account_distribution_daily + event_target.account_distribution_lambda + lambda_permission.eventbridge_account_distribution | OPEN |
| 2 (K2, ENABLED dead event leg) | cot-pipeline | event_rule.cot_session_complete + event_target.cot_session_complete_target + lambda_permission.eventbridge_cot_session_complete | OPEN |
| 3 (K1, both bd rows: rules DISABLED) | bd-pipeline | bd_49f_runner + bd_49f_fees_runner full sets (rules, targets, permissions, lambda modules, IAM roles/policies/attachments, log groups) | OPEN |
| 4 (K1, smartx: rule DISABLED + trigger-less fn + drifted sched) | smartx-pipeline | daily_trigger rule + autostart set (fn/IAM/logs/target/permission/artifact-data) + model_monthly_pull set (drifted scheduler + fn/IAM/logs/attachment/artifact-data) | OPEN |

**Consumer-exercise per kill (the test that would have FAILED were a consumer live)** and
**rollback act** land in proof_TO-3 per-claim; rollback for every row = `git revert` of the
removal commit + re-apply within the same window (all resources are declarative TF state).

**Close (filled only when TRUE, per apply):**
- [ ] Apply 1: commit ______ plan-rows ______ 0-diff ______ tag ______
- [ ] Apply 2: commit ______ plan-rows ______ 0-diff ______ tag ______
- [ ] Apply 3: commit ______ plan-rows ______ 0-diff ______ tag ______
- [ ] Apply 4: commit ______ plan-rows ______ 0-diff ______ tag ______
- [ ] CLOSED at ______ with proof_TO-3 commit ______

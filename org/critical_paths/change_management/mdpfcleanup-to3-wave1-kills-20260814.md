# DEPLOY LEDGER — OPAL_MDPFCLEANUP.TO-3 wave-1 non-reserved kills (4 class-applies)

**Status:** CLOSED 2026-08-14T18:35Z. Re-stamped 2026-08-26 by `2.0.0_SA_COO`.

> No top-level `**Status:**` line existed, so this read OPEN for 287h. **The body's own close line says it: `[x] CLOSED 2026-08-14T18:35Z -- applies 1,2,4 landed clean; apply 3 STOPPED->KEEP; proof_TO-3 commit rides this close.`** Apply 3 was DELIBERATELY stopped and kept -- **a ruled non-action, not an unfinished leg**, and reading it as one is the error this stamp forecloses.

**Opened:** 2026-08-14T18:2xZ by 0.7.0_AE_CloudOps (deploy-start; NEVER#6)
**Authority:** Andrew "all recs approved" @874b52729c (TO-1 ratified set); CTO per-apply gates.
**Doctrine:** consumers first, binary last · one class per apply · expected-rows-only plans ·
0-diff + tag each · rollback = same-window revert commit. No reserved acts (EC2/S3 = TO-4).

| Apply | Root | Rows (state addresses) | Status |
|---|---|---|---|
| 1 (K2, ENABLED consumer — starts the TO-4 access-log clock) | smartx-pipeline | event_rule.account_distribution_daily + event_target.account_distribution_lambda + lambda_permission.eventbridge_account_distribution | CLOSED 18:21Z |
| 2 (K2, ENABLED dead event leg) | cot-pipeline | event_rule.cot_session_complete + event_target.cot_session_complete_target + lambda_permission.eventbridge_cot_session_complete | CLOSED 18:24Z |
| 3 (K1, both bd rows: rules DISABLED) | bd-pipeline | bd_49f_runner + bd_49f_fees_runner full sets | STOPPED-PRE-EDIT -> rows KEEP (FALSIFIED-LIVE: runners invoked 08-13T22:21Z/08-14T00:09Z via the ENABLED session chain, InvokeRunner grant session-chain.tf:121; zero mutations; CTO 182639Z report) |
| 4 (K1, smartx: rule DISABLED + trigger-less fn + drifted sched) | smartx-pipeline | daily_trigger rule + autostart set + model_monthly_pull set + scheduler-role companions (15 destroys) | CLOSED 18:33Z |

**Consumer-exercise per kill (the test that would have FAILED were a consumer live)** and
**rollback act** land in proof_TO-3 per-claim; rollback for every row = `git revert` of the
removal commit + re-apply within the same window (all resources are declarative TF state).

**Close (filled only when TRUE, per apply):**
- [x] Apply 1: commit 5dc5863a7d; plan 0/0/3 (saved w1a1.tfplan, exact rows); 0-diff clean; absence ResourceNotFoundException + found-control cot-bronze-complete ENABLED; tag smartx-pipeline-v0.9.1
- [x] Apply 2: commit 5b989deb27; plan 0/0/3 (saved w1a2.tfplan); 0-diff clean; absence + found-control verified; tag cot-pipeline-v0.7.5
- [x] Apply 3: STOPPED PRE-EDIT, zero mutations -- bd rows FALSIFIED-LIVE, rolled to KEEP per the ratified disputed-row rule (no commit, no plan, no apply)
- [x] Apply 4: commit a3b36fd877; saved w1a4t.tfplan 15/0/0 (full-root plan REJECTED dirty: 2 unrelated KEEP-Lambda updates surfaced->COO); targeted 0-diff clean + full-root residual == exactly the 2 surfaced rows; absence x2 ResourceNotFoundException + found-control ingestion-pipeline FOUND; tag smartx-pipeline-v0.9.2. DRIFT-HEAL CORRECTED: CloudTrail DeleteSchedule smartx-model-monthly-pull-daily errorCode NONE = the schedule EXISTED live (TO-0 absence probe had queried the BASE name -- wrong-bucket class, corrected in proof_TO-0 rev3); the delete was REAL and exactly the ratified row.
- [x] CLOSED 2026-08-14T18:35Z -- applies 1,2,4 landed clean; apply 3 STOPPED->KEEP; proof_TO-3 commit rides this close.

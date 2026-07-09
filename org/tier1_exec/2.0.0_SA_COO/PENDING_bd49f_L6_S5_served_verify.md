# PENDING VERIFICATION -- bd-49f L6 served-property exercise (S5)

**STATUS:** OPEN. Fires AFTER the ~04:00Z 2026-07-10 scheduled gold. **Trigger owner: 2.0.0_SA_COO (/drive tick) + MSTR (respawn-executor).**
**Ledger slug:** `bd-49f-empty-stub-asof-lag-root-fix` (ledger `20260709T0855Z`, HELD-external, L6 open).
**Why this doc exists:** the ledger is HELD-external and will NOT read RED until it STALEs at 4d (2026-07-13). Without an explicit trigger, the 49F client-facing served un-freeze goes UNVERIFIED for 3 days -- the failsafe-hold-needs-duration-alarm gap (`memory/feedback_failsafe_hold_needs_duration_alarm_else_silent_stale`). Flagged by 0.6.0 (100429Z). This is a VERIFICATION, not a formality: the residual-risk branch (gold advances to 07-09 instead of 07-08 -> C_02 BRANCH-A floor skips -> portal STAYS FROZEN) is real, if unlikely.

## TRIGGER (any live agent, after ~04:30Z 2026-07-10)
Respawn `0.6.0_AE_PartnerETL` (MSTR) OR hand to any live AE. Fully specified, takes minutes.

## S5 EXERCISE (the SERVED property, not the re-pull)
1. **Check the runner:** CW `/aws/lambda/bd-49f-runner` ~00:00Z 07-10. Expect allocations landed `as_of=2026-07-09` (real, ~12.9MB). If "REJECTED allocations @as_of=2026-07-09" -> BD had no 07-09 snapshot = the guard WORKING (not a failure); gold should still certify off 07-08.
2. `aws s3 ls s3://opal-data-bd/gold/validation/aua_certification/` -> PASS = a NEW cert JSON exists (expected `2026-07-08.json`).
3. **Read it:** `certified_aua` MUST NOT equal `1,837,159,865.68` (the frozen figure). Predicted `$1,844,022,461.17` +/- price/restatement drift. A cert whose DATE advanced but whose VALUE is still exactly the frozen number => D_00 is still holding = **FAIL**, not pass.
4. **Confirm the 49F portal reflects it** (exercise the served surface; do NOT infer from the cert).
5. **RAVC CTO.** Then close the ledger:
   - `python .tools/deploy_ledger.py hold --slug bd-49f-empty-stub-asof-lag-root-fix --release`
   - `python .tools/deploy_ledger.py close-leg --leg L6 --proof "<served evidence>"`
   - `python .tools/deploy_ledger.py close --slug bd-49f-empty-stub-asof-lag-root-fix`

## FAIL BRANCH (no new cert)
Read `silver/allocations/2026-07-09.parquet` row count. 0 rows => the 07-09 stub never healed; re-pull: `invoke bd-49f-runner {"date":"2026-07-10","table":"allocations","force":true}` (-> as_of=2026-07-09) and wait for the following gold. **Escalate to CTO before ANY served touch.**

## ALSO OPEN (routed to CTO, not part of S5)
- bd-cot-freshness-probe:211 -- identical filename-anchored defect (cot lane, firm-sep, first estate-rollout target).
- astn-wsjft-orchestrator (s3:GetObject+PutObject) + etfs-reports-orchestrator (s3:PutObject) IAM gaps (non-NFRA, post-NFRA disposition).
- SilverNewestPartitionDegenerate alarm -- add AFTER 07-09 self-heals (CTO agreed).

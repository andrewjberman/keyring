# Deploy-Completion Ledger — ADVI_BREAKS TO-6 item2d: cot accept-lag retune (in-place Lambda update)

**Status:** CLOSED (2026-06-30T18:19Z — retune deployed + dry-run verified; cot accepted at 2td, only 49F fires)
**Opened:** 2026-06-30T18:17Z by 0.7.0_AE_CloudOps (executor)
**Deploy:** redeploy the item2d freeze-monitor Lambda (`opal-globgrph-freeze-monitor`) with 0.8.0~B's per-firm as_of-lag accept-threshold (commit 7cb765fdd): cot DATA-AS-OF-FRONTIER-LAG fires only at >2 trading days (threshold 3) -- accepts cot's normal BD T+1/T+2 pricing cadence (cot value is CORRECT per the cot value-parity reader; only fire on a REAL stall). inf/49F UNCHANGED (default 2). ONLY the as_of-lag verdict; size-collapse/stopped-writer/frozen-but-fresh/value-parity untouched.
**Gates cleared:** Andrew GO (cot freshness accept-lag, via COO 181206Z) + 0.8.0~B authored+committed 7cb765fdd (19/19 tests). Code-only repackage (archive source_code_hash) -> in-place Lambda update, NO new resources, NO IAM/schedule change.
**Scope:** globgrph state, -target=aws_lambda_function.freeze_monitor (item2e write-trail NOT swept).
**Executor:** 0.7.0_AE_CloudOps. **Co-verify:** 0.8.0~B (deployed dry-run) + CVO.

| Leg | Type | Step | Status |
|---|---|---|---|
| L1 | TF apply (safe-apply HALT-gate) | -target freeze_monitor Lambda -> in-place source_code_hash update | OPEN |
| L2 | verify | 0.8.0~B invokes DEPLOYED {dry_run:true} -> cot now ACCEPTED (quiet at 2td) + 49F STOPPED-WRITER still fires + inf clean | OPEN |

**Closure:** L1 done + 0.8.0~B's deployed-verify -> closes cot's §4 freshness axis -> CVO ratifies cot 2-of-3 GREEN. RAVC COO.

## Log
- 20260630T1817Z OPENED. git pull 7cb765fdd; plan -target = "0 add, 1 change (Lambda source_code_hash), 0 destroy" (clean repackage, item2e not swept). Proceeding L1 safe-apply.
- 20260630T1819Z **L1 DONE + L2 dry-run verified -> CLOSED.** safe-apply (HALT-gate clean) -> in-place Lambda update (source_code_hash yNmDw9... -> 03n/Xj...), LastUpdateStatus Successful @ 18:17:57Z, 0-diff "No changes". Dry-run the DEPLOYED opal-globgrph-freeze-monitor {dry_run:true} -> n_fired=1, n_suppressed=1, the ONLY fire = STOPPED-WRITER (49F). So post-retune: **cot DATA-AS-OF-FRONTIER-LAG NO LONGER FIRES (accepted at 2td, threshold 3)** + inf clean (recovered) + 49F STOPPED-WRITER still caught = exactly 0.8.0~B's pre-deploy local dry-run. cot's §4 freshness axis closes (value correct per the cot value-parity reader + lag accepted per Andrew). 0.8.0~B does their own deployed co-verify + RAVCs COO; CVO ratifies cot 2-of-3 GREEN. RAVC'd COO+0.8.0~B.

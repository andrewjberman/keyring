# Deploy-Completion Ledger — ADVI_BREAKS TO-6 item2d: cot accept-lag retune (in-place Lambda update)

**Status:** OPEN
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

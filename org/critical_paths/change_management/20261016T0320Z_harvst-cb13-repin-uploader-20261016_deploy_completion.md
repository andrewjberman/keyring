# Deploy Completion Record
**Date opened:** 2026-10-16T03:20:37.311517+00:00
**Status:** OPEN
**Deploy:** AMGT_HARVST HVST-cb-13: re-pin the dell1 runner from new pin R=ddd7dcdc38 (uploader fix c1df06b1ef + seed 4d2a3e2187), SEED silver_known once with the runner stopped, check no duplicates. Rollback: Branch F (stop file, re-register from C:/dev/wk-harvest-runner-pin-3c1e8bcdb1 with wsj,barrons).
**Authored by:** 0.7.0_AE_CloudOps~SC1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| PIN | verify | C:/dev/wk-harvest-runner-pin-ddd7dcdc38 | worktree detached at R, rev-parse reads R, locked for new and old |  | OPEN |
| STOP | verify | C:/dev/ajb_workspace/.runtime/harvest-cycle/STOP | STOP-FILE no further cycle line read, Stop-ScheduledTask, process census 0 (positive control), STOP left in place until the seed |  | OPEN |
| SEED | verify | C:/dev/ajb_workspace/.runtime/harvest-cycle/runtime/silver_known_seed.json | seed dry-run read then real run once, rows_without_hash 0, snapshot exists with seeded_at |  | OPEN |
| ARM | verify | scheduled task Opal Data Harvest - Continuous Cycle | STOP deleted, -Plan read then registered once from the new pin, XML read back, T0 written after the seed, started once |  | OPEN |
| CHECK | verify | seed_silver_known check --since T0 | check ends DUPLICATES=0 rc 0 after the first upload-harvest line |  | OPEN |
| WINDOW | verify | the +3 and +15 minute reads R1-R5 and R7 | cb13_reads.out with controls |  | OPEN |

## Log

- 20261016T032037Z OPENED by 0.7.0_AE_CloudOps~SC1 with 6 leg(s)

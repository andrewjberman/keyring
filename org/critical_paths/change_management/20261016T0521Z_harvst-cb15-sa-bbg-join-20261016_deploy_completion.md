# Deploy Completion Record
**Date opened:** 2026-10-16T05:21:50.303000+00:00
**Status:** OPEN
**Deploy:** AMGT_HARVST HVST-cb-15: sa and bbg join the dell1 harvest runner (same pin ddd7dcdc38), silver_known seeded once for sa+bbg with the runner stopped, C-a4' read at the end of the first sa/bbg uploading cycle. Rollback: Branch F (stop file, re-register wsj,barrons from the same pin).
**Authored by:** 0.7.0_AE_CloudOps~SC1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| STOP | verify | C:/dev/ajb_workspace/.runtime/harvest-cycle/STOP | STOP-FILE no further cycle line, Stop-ScheduledTask, process census 0 harvest python rows with a positive control, STOP left in place until the seed |  | OPEN |
| SEED | verify | C:/dev/ajb_workspace/.runtime/harvest-cycle/runtime/silver_known_seed.json | seed sa+bbg dry-run then real once, rows_without_hash 0, snapshot holds wsj+barrons+sa+bbg tables |  | OPEN |
| ARM | verify | scheduled task Opal Data Harvest - Continuous Cycle | STOP deleted, -Plan read then registered once with the new publisher list from the same pin, XML read back, T0 after the seed, started once |  | OPEN |
| CHECK | verify | seed_silver_known check --since T0 over four publishers | DUPLICATES=0 after the first sa and bbg uploads, parts_read above 0 for sa or bbg |  | OPEN |
| WINDOW | verify | +3 and +15 reads and the C-a4' read at the end of the first sa/bbg uploading cycle | cb15_reads.out and cb15_c_a4.out |  | OPEN |

## Log

- 20261016T052150Z OPENED by 0.7.0_AE_CloudOps~SC1 with 5 leg(s)

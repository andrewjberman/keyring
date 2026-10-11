# Deploy Completion Record
**Date opened:** 2026-10-11T08:34:08.911143+00:00
**Status:** OPEN
**Deploy:** MDPF DEMQUE t27 register the standing non-trading-day drawer mdpf-demque-drawer-daily at site Z
**Authored by:** 0.7.0_AE_CloudOps~ZQ
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 12.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | Windows task mdpf-demque-drawer-daily, DAILY 10:00 ET, action standing_drawer.py --apply from the repo root | schtasks /Query of that exact name plus its exported XML showing one daily 10:00 trigger and the repo-root action; the 07:00 and 08:30 task definitions byte-unchanged |  | OPEN |
| L2 | verify | AC2 dq_t27_sched.py | DRSCH-OK: the four non-trading days of 2026-10-12..2026-10-25, the task registered, and a trading day drawing 0 against scratch output and actuals |  | OPEN |
| L3 | verify | the first scheduled fire, today 2026-10-11 10:00 ET (CTO half condition 3) | AC3 FIRE-OK read from the fire's own marker, its actuals line and cells_drawn: outcome DRAWN and cells_drawn equal to min(5858, 15720 minus already drawn) and not over today's room |  | OPEN |
| L4 | verify | CTO half condition 2, the non-DRAWN / over-room branch | either the fire was DRAWN and within room so no rollback is owed, or the task is deleted and a row filed; stated as a read either way, never as a default |  | OPEN |

## Log

- 20261011T083408Z OPENED by 0.7.0_AE_CloudOps~ZQ with 4 leg(s)

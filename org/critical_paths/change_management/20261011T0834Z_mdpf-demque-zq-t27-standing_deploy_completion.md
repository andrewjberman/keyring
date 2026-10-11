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
| L1 | activation | Windows task mdpf-demque-drawer-daily, DAILY 10:00 ET, action standing_drawer.py --apply from the repo root | schtasks /Query of that exact name plus its exported XML showing one daily 10:00 trigger and the repo-root action; the 07:00 and 08:30 task definitions byte-unchanged | Registered mdpf-demque-drawer-daily, State Ready, NextRunTime 2026-10-11 10:00:00 local (today), LastTaskResult 267011 = has-not-yet-run. Name DERIVED by standing_drawer.py --task-name under Python 3.11 and compared to the expected string before registering; 0 pre-existing rows for that name, so nothing was overwritten. Definition confirmed on TWO independent instruments (exported XML text and the ScheduledTask object model, after an attribute-tolerant re-read -- a bare <Actions> regex missed Context=Author and must not be cited): Command C:/Users/Opal Bloomberg/AppData/Local/Programs/Python/Python311/python.exe, Arguments 'data/mdpf/scripts/demque/standing_drawer.py --apply', WorkingDirectory the repo root, CalendarTrigger ScheduleByDay DaysInterval 1 from 2026-10-11T10:00:00-04:00, Principal InteractiveToken. INTERPRETER CHOSEN BY MEASUREMENT, not by copying t24: Python 3.11.9 carries blpapi, Python 3.14.7 does NOT (pandas and pyarrow are on both). The three named tests pass under 3.11 as well as 3.14, and AC1 reads DRW-OK under 3.11 -- the tests use a stub client so they would NOT have caught a task bound to the blpapi-less interpreter. Existing daily tasks byte-UNCHANGED: OPAL_BBGTML_daily_pull 1563 chars, OPAL_DEMQUE_bbg_ledger_upload 3605, OPAL_BBGTML_freshness_check 1266, each identical to its t27-before export with a negative control on a mismatched pairing reading False. Device task denominator 214 before, 215 after = exactly one added. Entry opened BEFORE registering per CTO half condition 1. | CLOSED 20261011T084630Z |
| L2 | verify | AC2 dq_t27_sched.py | DRSCH-OK: the four non-trading days of 2026-10-12..2026-10-25, the task registered, and a trading day drawing 0 against scratch output and actuals | AC2 dq_t27_sched.py: DRSCH-OK 4 fires in 14 days, task mdpf-demque-drawer-daily registered, a trading day draws 0. Its three printed arms: schedule fires ['2026-10-17','2026-10-18','2026-10-24','2026-10-25'] for the 2026-10-12..2026-10-25 window; task registered under the built name; trading-day arm cells_drawn=0 stop_reason=TRADING_DAY against scratch output and actuals. AC1 re-run after the registration still DRW-OK, so registering regressed nothing. | CLOSED 20261011T084630Z |
| L3 | verify | the first scheduled fire, today 2026-10-11 10:00 ET (CTO half condition 3) | AC3 FIRE-OK read from the fire's own marker, its actuals line and cells_drawn: outcome DRAWN and cells_drawn equal to min(5858, 15720 minus already drawn) and not over today's room |  | OPEN |
| L4 | verify | CTO half condition 2, the non-DRAWN / over-room branch | either the fire was DRAWN and within room so no rollback is owed, or the task is deleted and a row filed; stated as a read either way, never as a default |  | OPEN |

## Log

- 20261011T083408Z OPENED by 0.7.0_AE_CloudOps~ZQ with 4 leg(s)
- 20261011T084630Z LEG L1 closed: Registered mdpf-demque-drawer-daily, State Ready, NextRunTime 2026-10-11 10:00:00 local (today), LastTaskResult 267011 =
- 20261011T084630Z LEG L2 closed: AC2 dq_t27_sched.py: DRSCH-OK 4 fires in 14 days, task mdpf-demque-drawer-daily registered, a trading day draws 0. Its t

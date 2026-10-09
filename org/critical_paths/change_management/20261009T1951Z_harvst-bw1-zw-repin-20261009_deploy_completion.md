# Deploy Completion Record
**Date opened:** 2026-10-09T19:51:46.393283+00:00
**Status:** OPEN
**Deploy:** HVST-bw-1 site Z runner re-pin b5a7a3a4b6 with old state; AMENDMENT 2 C-f and C-g
**Authored by:** 0.7.0_AE_CloudOps~ZW
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 24.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| PIN | verify | wk-harvest-runner-pin-b5a7a3a4b6 | new pin b5a7a3a4b6 plus old pin positive control |  | OPEN |
| STOP | verify | old runner cycle and STOP removal | stopped_by_operator record ended_at and C-g path time Test-Path False plus process census |  | OPEN |
| ARM | activation | Opal Data Harvest - Continuous Cycle | new workdir old state runtime bbg wsj barrons one start timestamp |  | OPEN |
| GC | verify | new runner reaper exemption | kill-maint dryrun EXEMPT PID |  | OPEN |
| CYCLE | verify | first post-repin bbg cycle | ended cycle record and bw2 evidence |  | OPEN |

## Log

- 20261009T195146Z OPENED by 0.7.0_AE_CloudOps~ZW with 5 leg(s)

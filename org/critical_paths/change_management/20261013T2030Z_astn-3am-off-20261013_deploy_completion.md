# Deploy Completion Record
**Date opened:** 2026-10-13T20:30:12.740418+00:00
**Status:** OPEN
**Deploy:** HVST-bz-8: disable the astn-wsjft-3am-run schedule
**Authored by:** 0.7.0_AE_CloudOps~HV1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| EDIT | git | orchestrator.tf state DISABLED | commit hash |  | OPEN |
| APPLY | activation | targeted safe-apply of aws_scheduler_schedule.astn_run (trigger disarm; order said tf-schedule, not a valid kind) | plan 0/1/0 then Apply complete 0 added 1 changed 0 destroyed |  | OPEN |
| VERIFY | verify | get-schedule State DISABLED, expression target input unchanged | AC1 AC2 AC3 |  | OPEN |

## Log

- 20261013T203012Z OPENED by 0.7.0_AE_CloudOps~HV1 with 3 leg(s)

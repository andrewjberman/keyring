# Deploy Completion Record
**Date opened:** 2026-09-26T17:48:23.428377+00:00
**Status:** OPEN
**Deploy:** S147 experiment (CTO 101385): irpt-performance-adapter memory_size 1536 -> 3008 MB; rollback 1536; gate DELTA=0 on report bytes
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| M1 | verify | latency + DELTA=0 | 3 new-window recomputes timed (Duration); one served report byte-compared with the same engine code locally on the same data (DELTA=0), a difference = STOP + revert |  | OPEN |
| irpt-performance-adapter | tf-lambda | module.irpt_performance_adapter.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20260926T174823Z OPENED by 2.0.0_SA_COO~P with 2 leg(s)

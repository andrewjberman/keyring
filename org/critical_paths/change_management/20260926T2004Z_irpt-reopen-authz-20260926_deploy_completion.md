# Deploy Completion Record
**Date opened:** 2026-09-26T20:04:22.428614+00:00
**Status:** OPEN
**Deploy:** P-REOPEN-01: irpt-performance-adapter = live Zs2OK7C5 + entry.py @260399e940 + f49_engine.py @8d7a8b10fe; packet d01c36c4 (CTO SIGNOFF_REOPEN_AUTHZ_20260926.md, CRO @219f9450da); rollback artifact S3 version AHiiInq1WnKvFVFbQBqfaS0nFM.8N7ZN
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| B0 | verify | before arm on the live code | reopen_authz_arm.py before: V1 ok past frontier; V2 OBJECT_NOT_COVERED (negative control); V0 refused; owner digest |  | OPEN |
| D1 | activation | irpt-performance-adapter artifact + apply | census vs Zs2OK7C5: exactly entry.py + f49_engine.py; safe-apply; readback; import census; 0-diff replan |  | OPEN |
| A1 | verify | after arm + compare | reopen_authz_arm.py after + compare: 5 PASS or same-turn rollback to Zs2OK7C5 |  | OPEN |
| T1 | verify | ruling A phase split | one irpt_engine_phases line from the fresh read, sent to the S147 card |  | OPEN |

## Log

- 20260926T200422Z OPENED by 2.0.0_SA_COO~P with 4 leg(s)

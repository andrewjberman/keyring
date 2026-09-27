# Deploy Completion Record
**Date opened:** 2026-09-27T05:09:25.184602+00:00
**Status:** OPEN
**Deploy:** irpt-performance-adapter code-only: COT actual_start = the account's first series point (backend 05778597eb); plan stays null; DELTA=0 on every reachable surface (49F arms, reopens; COT/INF fresh refused without a plan)
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| B0 | verify | before arms on Ll6t4VPa | reopen_authz_arm.py before (V1/V2/V0 + past-frontier) recorded before the build |  | OPEN |
| D1 | activation | irpt-performance-adapter apply | zip census vs Ll6t4VPa = bd_selected.py only; plan with the null var-file 0/1/0 code only; safe-apply; readback CodeSha + env still no plan; replan 0 |  | OPEN |
| A1 | verify | DELTA=0 + the change | reopen_authz_arm after + compare all PASS with V1/V2 data identical; replay of RPT-b683f188's recorded provider bytes through the DEPLOYED zip's bd_selected gives actual 2026-07-21; or same-turn rollback to Ll6t4VPa |  | OPEN |

## Log

- 20260927T050925Z OPENED by 2.0.0_SA_COO~P with 3 leg(s)

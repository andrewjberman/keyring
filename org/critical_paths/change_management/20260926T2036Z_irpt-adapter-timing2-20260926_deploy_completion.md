# Deploy Completion Record
**Date opened:** 2026-09-26T20:36:29.208002+00:00
**Status:** OPEN
**Deploy:** S147 second timing line (CTO 101487): irpt-performance-adapter = live 8a6zq+x9 + entry.py + retained.py @b18cb77c7d; timings only, DELTA=0 held by the reopen arm; rollback 8a6zq+x9 (S3 version 3F8gPQNBK1o62ZnJ56EvJ0ZjgZeHawRL)
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| D1 | activation | irpt-performance-adapter artifact + apply | census vs 8a6zq: exactly entry.py + retained.py; code-only plan with the live INF plan var; safe-apply; readback; replan 0 |  | OPEN |
| Z1 | verify | DELTA=0 | reopen_authz_arm after-run on the new code vs REOPEN_ARM_AFTER_20260926.json: V1/V2 same ref + data sha, V0 refused |  | OPEN |
| T1 | verify | the two timing lines | one fresh read logs irpt_performance_timing + irpt_retained_phases; the re-ranked card to the CTO |  | OPEN |

## Log

- 20260926T203629Z OPENED by 2.0.0_SA_COO~P with 3 leg(s)

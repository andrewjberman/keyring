# Deploy Completion Record
**Date opened:** 2026-09-27T17:26:57.238972+00:00
**Status:** OPEN
**Deploy:** irpt-export-render ryEMGlRu -> 3EST/hewG: the export admits the reopen rule's callers (backend f92445392d; CTO 101991 (a)); code only 0/1/0; rollback S3 version 9atDu8b.; halves pending
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| D1 | activation | irpt-export-render apply | both halves at HEAD; census 58/58 only retained_export.py; plan 0/1/0 code only; safe-apply; readback CodeSha 3EST/hewG; replan 0 |  | OPEN |
| A1 | verify | proof arms | next K8 window: a second in-scope principal exports READY; a principal missing one account refused; owner unchanged; grant/receipt name the caller |  | OPEN |

## Log

- 20260927T172657Z OPENED by 2.0.0_SA_COO~P with 2 leg(s)

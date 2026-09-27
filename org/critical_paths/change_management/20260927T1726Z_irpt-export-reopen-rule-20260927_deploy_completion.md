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
| D1 | activation | irpt-export-render apply | both halves at HEAD; census 58/58 only retained_export.py; plan 0/1/0 code only; safe-apply; readback CodeSha 3EST/hewG; replan 0 | both halves at HEAD naming blob 12a1afda (CTO @96a286d416 101994: safe-apply only, CodeSha from the live function; arm 2 on the served bytes by direct invoke or a named departure; CRO @700fecf1a6 101995: roll back to 9atDu8b the same turn on any arm failure); census 58/58 only retained_export.py; re-plan 0/1/0 code only (source_code_hash ryEMGlRu -> 3EST/hewG); safe-apply 17:34:21Z 'Resources: 0 added, 1 changed, 0 destroyed'; readback (live get-function-configuration) CodeSha256 3EST/hewGXFU891RW5Y8T18GtIrrGbGE85Ka9e7hzSI= Active/Successful, IRPT_EXPORT_RENDER=on unchanged; replan -detailed-exitcode 0. Rollback root: S3 version 9atDu8b. (ryEMGlRu). | CLOSED 20260927T173744Z |
| A1 | verify | proof arms | next K8 window: a second in-scope principal exports READY; a principal missing one account refused; owner unchanged; grant/receipt name the caller |  | OPEN |

## Log

- 20260927T172657Z OPENED by 2.0.0_SA_COO~P with 2 leg(s)
- 20260927T173744Z LEG D1 closed: both halves at HEAD naming blob 12a1afda (CTO @96a286d416 101994: safe-apply only, CodeSha from the live function; arm 2

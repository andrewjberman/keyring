# Deploy Completion Record
**Date opened:** 2026-09-27T21:58:18.516427+00:00
**Status:** OPEN
**Deploy:** Comparison catalogue v2 in generate AND resident together (backend 4b563c98a0; ~Y 102113) + the resident Static-only level tolerance (backend 12a67ed5ee; CTO 101971 item 2); generate code only; resident fe64236bbb-lt -> fe64236bbb-st; halves pending
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | verify | generate artifact build + upload | census vs live G/TqLPdL: ONLY templates.json differs; flat import |  | OPEN |
| U2 | verify | resident package st upload | SUMS vs lt: ONLY extract.py, recipe.py, resident_worker.py, templates.json + bindings; tar sha recorded |  | OPEN |
| D1 | activation | generate safe-apply | both halves at HEAD; plan 0/1/0 code only; readback CodeSha; replan 0 |  | OPEN |
| D2 | activation | resident install lt -> st | both halves at HEAD; queue 0/0; controlled stop; install rc 0; polls; host shas == the package; rollback root lt kept |  | OPEN |

## Log

- 20260927T215818Z OPENED by 2.0.0_SA_COO~P with 4 leg(s)

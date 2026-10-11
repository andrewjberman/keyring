# Deploy Completion Record
**Date opened:** 2026-10-11T15:02:49.353030+00:00
**Status:** OPEN
**Deploy:** IRPT_YCDGEN r13: eight conditional writes to irpt-jobs (XB-0c52 ORDER, consent 111d835ee5)
**Authored by:** 0.7.0_AE_CloudOps~ANL
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| BEFORE | verify | four queue counts, no receive | counts printed |  | OPEN |
| ROW7 | verify | row 7 REQ-448d42480cadd873fa74c3cf written, consistent read-back FAILED, job_detail type S equal | read-back line |  | OPEN |
| STATUS7 | verify | status answer of request 7 through irpt-status reads FAILED / ANALYSIS_FAILED | state and reason |  | OPEN |
| ROWS-1-6-8 | verify | rows 1-6 and 8 each conditional write and read-back, or Branch B reported | per-row line |  | OPEN |
| AFTER | verify | four queue counts again, unchanged | counts printed |  | OPEN |

## Log

- 20261011T150249Z OPENED by 0.7.0_AE_CloudOps~ANL with 5 leg(s)

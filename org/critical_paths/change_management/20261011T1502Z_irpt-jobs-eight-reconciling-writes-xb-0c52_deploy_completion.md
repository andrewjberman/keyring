# Deploy Completion Record
**Date opened:** 2026-10-11T15:02:49.353030+00:00
**Status:** CLOSED -- REFUSED BY GATE, nothing created -- closed 20261011T150554Z
**Deploy:** IRPT_YCDGEN r13: eight conditional writes to irpt-jobs (XB-0c52 ORDER, consent 111d835ee5)
**Authored by:** 0.7.0_AE_CloudOps~ANL
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| BEFORE | verify | four queue counts, no receive | counts printed | irpt-generation-dlq 8 visible/0 notvisible/0 delayed; source irpt-generation 0/0/0; commentary-ready 1/0/0; commentary-ready-dlq 0/0/0; no receive; all eight rows read RECEIVED with no job_detail (consistent get-item) | CLOSED 20261011T150409Z |
| ROW7 | verify | row 7 REQ-448d42480cadd873fa74c3cf written, consistent read-back FAILED, job_detail type S equal | read-back line |  | OPEN |
| STATUS7 | verify | status answer of request 7 through irpt-status reads FAILED / ANALYSIS_FAILED | state and reason |  | OPEN |
| ROWS-1-6-8 | verify | rows 1-6 and 8 each conditional write and read-back, or Branch B reported | per-row line |  | OPEN |
| AFTER | verify | four queue counts again, unchanged | counts printed | after ROLLBACK of row 7: irpt-generation-dlq 8/0/0, source irpt-generation 0/0/0, commentary-ready 1/0/0, commentary-ready-dlq 0/0/0 - equal to BEFORE; all eight irpt-jobs rows read state RECEIVED, no job_detail | CLOSED 20261011T150554Z |

## Log

- 20261011T150249Z OPENED by 0.7.0_AE_CloudOps~ANL with 5 leg(s)
- 20261011T150409Z LEG BEFORE closed: irpt-generation-dlq 8 visible/0 notvisible/0 delayed; source irpt-generation 0/0/0; commentary-ready 1/0/0; commentary-r
- 20261011T150554Z LEG AFTER closed: after ROLLBACK of row 7: irpt-generation-dlq 8/0/0, source irpt-generation 0/0/0, commentary-ready 1/0/0, commentary-rea
- 20261011T150554Z CLOSED -- REFUSED BY GATE before apply, world untouched: ABORTED AT STATUS7 GATE, not completed. Row 7 written (job_detail type S equal, state FAILED) then status answer of REQ-448d42480cadd873fa74c3cf through irpt-status as owner replay read UNAVAILABLE/FIRM_BINDING (expected FAILED/ANALYSIS_FAILED); row 7 ROLLED BACK per the ask (RECEIVED, job_detail absent, read back); rows 1-6 and 8 NEVER written (0 of 7 attempted); control: same status call on the 

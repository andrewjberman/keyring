# Deploy Completion Record
**Date opened:** 2026-10-11T15:27:01.341596+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261011T152908Z
**Deploy:** IRPT_YCDGEN r13 re-issue 1: eight conditional writes to irpt-jobs, four row checks (XB-0162 ORDER, CTO half 715dcd3b69)
**Authored by:** 0.7.0_AE_CloudOps~ANL
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| BEFORE | verify | four queue counts, no receive | counts printed | irpt-generation-dlq 8/0/0; source irpt-generation 0/0/0; commentary-ready 1/0/0; commentary-ready-dlq 0/0/0; no receive; all eight rows RECEIVED, no job_detail | CLOSED 20261011T152744Z |
| ROW7 | verify | row 7 written, one consistent get-item, four checks all true | check line | row 7 REQ-448d42480cadd873fa74c3cf WRITTEN; one consistent get-item: (i) state FAILED (ii) job_detail type S (iii) four members with packet values (iv) sorted-key reserialise equals stored string: ALL true | CLOSED 20261011T152823Z |
| ROWS-1-6-8 | verify | rows 1-6 and 8 each written with four checks true, or Branch B reported | per-row line | rows 1,2,3,4,5,6,8 each WRITTEN (no Branch B) and each four checks ALL true on one consistent get-item | CLOSED 20261011T152908Z |
| AFTER | verify | four queue counts again, unchanged | counts printed | irpt-generation-dlq 8/0/0; source irpt-generation 0/0/0; commentary-ready 1/0/0; commentary-ready-dlq 0/0/0; equal to BEFORE; eight rows FAILED with job_detail type S, attribute set = original 7 + job_detail | CLOSED 20261011T152908Z |

## Log

- 20261011T152701Z OPENED by 0.7.0_AE_CloudOps~ANL with 4 leg(s)
- 20261011T152744Z LEG BEFORE closed: irpt-generation-dlq 8/0/0; source irpt-generation 0/0/0; commentary-ready 1/0/0; commentary-ready-dlq 0/0/0; no receive;
- 20261011T152823Z LEG ROW7 closed: row 7 REQ-448d42480cadd873fa74c3cf WRITTEN; one consistent get-item: (i) state FAILED (ii) job_detail type S (iii) four 
- 20261011T152908Z LEG ROWS-1-6-8 closed: rows 1,2,3,4,5,6,8 each WRITTEN (no Branch B) and each four checks ALL true on one consistent get-item
- 20261011T152908Z LEG AFTER closed: irpt-generation-dlq 8/0/0; source irpt-generation 0/0/0; commentary-ready 1/0/0; commentary-ready-dlq 0/0/0; equal to BE
- 20261011T152908Z CLOSED -- all 4 legs proven

# Deploy Completion Record
**Date opened:** 2026-09-27T16:22:26.120971+00:00
**Status:** OPEN
**Deploy:** window 16: K8, the FIRST real export, re-cut on local portal DEV e8a00b23 (IV-e-65: the export names the report by its RPT- id) -- window 14's shape (packet NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W16_K8_EXPORT_20260927.md); created after window 15 closes; halves pending
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| C1 | activation | K1 + K1-CRED | both halves at HEAD naming the blob; window 15 closed; pins + portal HEAD e8a00b23 re-read equal; pre-read + censuses; put + read-back | both halves at HEAD naming blob 907073b1 (CTO @93780555f5 101962: opens only after window 15's amendment principal is deleted -- deleted 16:47:34Z; CRO @ff6622ce41 101963); pins re-read 16:5xZ equal: adapter bOefL9nx no plan, IRPT_EVIDENCE_BUCKET opal-data-ycharts; irpt-export-render ryEMGlRu IRPT_EXPORT_RENDER=on; SSM doc v5; irpt-status bMMJ/bQ+5; directory-search o1TXq5PH; portal HEAD e8a00b23, 0 tracked changes; C: 23 GB free; tracked media 929; pre-read epoch 1790528299 ABSENT; censuses before: users 51 digest 76cbe66b, SELECTION# 49, REPORT# 49F 20 / COT 2 / INF 1, 49F irpt-requests 142, exr 2, render tokens 0, W16 chain census; K1-CRED then K1 put USER#usr_irptuiwalk_1790528299 at 17:00:08Z, read-back EQUAL; cap cron b276224e 18:54Z (120 min = 19:00Z). Note: the session scratchpad was deleted by another process's temp cleanup at about 16:5xZ and recreated; the before-census files were re-taken after it. | CLOSED 20260927T170220Z |
| K1C | verify | K1-CRED deleted after the login | ParameterNotFound |  | OPEN |
| K8 | verify | ONE export | exactly 1 export POST; READY with %PDF page_count>=1 (served object) or a named NOT_READY/DEPENDENCY_UNAVAILABLE; render token ParameterNotFound |  | OPEN |
| D1 | verify | K1 delete after the export is terminal (<= 120 min) | failing consistent read |  | OPEN |
| A1 | verify | route audit + write trace | 0 outside the classes; export rows/objects traced to the exportId; users == baseline; 0 new media in git; K1 absent |  | OPEN |

## Log

- 20260927T162226Z OPENED by 2.0.0_SA_COO~P with 5 leg(s)
- 20260927T170220Z LEG C1 closed: both halves at HEAD naming blob 907073b1 (CTO @93780555f5 101962: opens only after window 15's amendment principal is de

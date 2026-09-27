# Deploy Completion Record
**Date opened:** 2026-09-27T06:03:20.216267+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260927T063353Z
**Deploy:** window 10: K8, the FIRST real export -- ~D's K7 49F ****9978 YTD read + ONE export POST (render ON), window 9's shape (packet NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W10_K8_EXPORT_20260927.md); no vendor call; halves pending
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| C1 | activation | K1 + K1-CRED | both halves at HEAD naming the blob; W10-4 pins re-read equal; pre-read + censuses; put + read-back | both halves at HEAD naming blob a15c2ffb (CTO @4392c7ab8f 101825: /download body out of the HAR, local PDF only in gitignored tmp/, PDF audit reads the served object; CRO @5e2f9b7ad4 101826: no new *.pdf/*.png/*.har in git -- baseline 963 tracked, list saved); W10-4 pins re-read 06:1xZ equal: adapter bOefL9nx no plan, IRPT_EVIDENCE_BUCKET opal-data-ycharts; irpt-export-render ryEMGlRu IRPT_EXPORT_RENDER=on; SSM doc irpt-export-render-run v5; irpt-status bMMJ/bQ+5; directory-search o1TXq5PH; C: 12 GB free; pre-read epoch 1790489867 K1/email/K1-CRED ABSENT; censuses before: users 51 digest 76cbe66b, SELECTION# 49, REPORT# 49F 20 / COT 1 / INF 1; 49F irpt-requests 142 rows {ARTIFACT 20, PERFORMANCE_ACCEPTED 20, REPORT 20, RETENTION 60, SELECTION 22}; irpt-jobs 49financial 0; opal-data-ycharts firms/49financial/generations/ 2 objects; /irpt/render-token/ 0 parameters; K1-CRED then K1 put USER#usr_irptuiwalk_1790489867 at 06:19:10Z, read-back EQUAL; cap cron at 08:13Z (120 min = 08:19Z). | CLOSED 20260927T062001Z |
| K1C | verify | K1-CRED deleted after the login | ParameterNotFound | ~D 101830 logged in 06:22:11Z; 06:22:5xZ ssm delete-parameter /irpt/ui-walk-principal/1790489867/password; the named get-parameter -> ParameterNotFound. | CLOSED 20260927T062314Z |
| K8 | verify | ONE export | exactly 1 export POST; READY with %PDF page_count>=1 or a named NOT_READY/DEPENDENCY_UNAVAILABLE; render token ParameterNotFound | NOT RUN -- a named page refusal, 0 export POSTs (~D 101831). K7 06:24:42Z: 49F ****9978 YTD, two GETs 01-01..09-22, both 200 PARTIAL, the SAME retained report RPT-b5e0a16e (revision 39c11079..; 6,237/6,445 ms), face 8.05% net answered 01-02..09-22; a REOPEN: 49F REPORT# 20 -> 20 and the report row existed before the window. K8: the Export dialog opened and refused 'investor-reporting-render/1.0.0 cannot render reportKind performance-report: 39c11079.. is absent' and 'Export waits for the report: it has not been read yet', with no submit control. 39c11079 IS RPT-b5e0a16e's own revision (irpt-requests REPORT#RPT-b5e0a16e..#39c11079..). The throw site is portal src/pages/InvestorReporting/export/resolveBundle.ts:255 (resolveOne: cache miss, then the fetcher threw client-side with 0 requests) -- a portal defect at DEV 200d257a in DSGN_IRPTV1 (~D's lane; ~D filing). Nothing exported: render tokens /irpt/render-token/ 0 -> 0, evidence-bucket firms/49financial/generations/ 2 -> 2 objects, irpt-jobs 49financial 0 -> 0. K8 carries to a later window after ~D's fix. | CLOSED 20260927T063352Z |
| D1 | verify | K1 delete after the export is terminal (<= 120 min) | failing consistent read | ~D 101832 done, browser closed; no export ran, so nothing was non-terminal; 06:32:17Z walk_principal.py --kind=uiwalk delete 1790489867: K1 consistent GetItem no Item (VERIFIED); K1-CRED ParameterNotFound (deleted 06:22:5xZ); cap cron 0d8c809f cancelled. | CLOSED 20260927T063353Z |
| A1 | verify | route audit + write trace | 0 outside the classes; export rows/objects traced to the exportId; users == baseline; K1 absent | HAR w10-20260927.har (451 entries, sha256 488da2d7bb7289a7.. re-hashed equal; leaks clean per ~D): writes = POST auth/login 1, auth/refresh 4, investor-reporting/directory/resolve 2, investor-reporting/selections 3; 0 export API requests (the only '/export' URLs are localhost:5174 source-module GETs of export/*.tsx and fixtures), /analysis 0, /auth/admin 0 -> 0 outside the classes. Write trace: SELECTION# 49 -> 49 (the page re-used an existing selection), REPORT# 49F 20 -> 20 / COT 1 -> 1 / INF 1 -> 1, 49F irpt-requests 142 -> 142 (0 added, 0 gone), W10 chain census (cottonwood) before == after, render tokens 0 -> 0, exr objects 2 -> 2; users 51 -> 51 digest 76cbe66b.. equal; no vendor call. CRO 101826: git ls-files *.pdf/*.png/*.har 963 -> 963, 0 new. Proof of no later use: K1 absent. | CLOSED 20260927T063353Z |

## Log

- 20260927T060320Z OPENED by 2.0.0_SA_COO~P with 5 leg(s)
- 20260927T062001Z LEG C1 closed: both halves at HEAD naming blob a15c2ffb (CTO @4392c7ab8f 101825: /download body out of the HAR, local PDF only in gitig
- 20260927T062314Z LEG K1C closed: ~D 101830 logged in 06:22:11Z; 06:22:5xZ ssm delete-parameter /irpt/ui-walk-principal/1790489867/password; the named get
- 20260927T063352Z LEG K8 closed: NOT RUN -- a named page refusal, 0 export POSTs (~D 101831). K7 06:24:42Z: 49F ****9978 YTD, two GETs 01-01..09-22, both
- 20260927T063353Z LEG D1 closed: ~D 101832 done, browser closed; no export ran, so nothing was non-terminal; 06:32:17Z walk_principal.py --kind=uiwalk de
- 20260927T063353Z LEG A1 closed: HAR w10-20260927.har (451 entries, sha256 488da2d7bb7289a7.. re-hashed equal; leaks clean per ~D): writes = POST auth/lo
- 20260927T063353Z CLOSED -- all 5 legs proven

# Deploy Completion Record
**Date opened:** 2026-09-27T16:22:26.120971+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260927T171214Z
**Deploy:** window 16: K8, the FIRST real export, re-cut on local portal DEV e8a00b23 (IV-e-65: the export names the report by its RPT- id) -- window 14's shape (packet NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W16_K8_EXPORT_20260927.md); created after window 15 closes; halves pending
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| C1 | activation | K1 + K1-CRED | both halves at HEAD naming the blob; window 15 closed; pins + portal HEAD e8a00b23 re-read equal; pre-read + censuses; put + read-back | both halves at HEAD naming blob 907073b1 (CTO @93780555f5 101962: opens only after window 15's amendment principal is deleted -- deleted 16:47:34Z; CRO @ff6622ce41 101963); pins re-read 16:5xZ equal: adapter bOefL9nx no plan, IRPT_EVIDENCE_BUCKET opal-data-ycharts; irpt-export-render ryEMGlRu IRPT_EXPORT_RENDER=on; SSM doc v5; irpt-status bMMJ/bQ+5; directory-search o1TXq5PH; portal HEAD e8a00b23, 0 tracked changes; C: 23 GB free; tracked media 929; pre-read epoch 1790528299 ABSENT; censuses before: users 51 digest 76cbe66b, SELECTION# 49, REPORT# 49F 20 / COT 2 / INF 1, 49F irpt-requests 142, exr 2, render tokens 0, W16 chain census; K1-CRED then K1 put USER#usr_irptuiwalk_1790528299 at 17:00:08Z, read-back EQUAL; cap cron b276224e 18:54Z (120 min = 19:00Z). Note: the session scratchpad was deleted by another process's temp cleanup at about 16:5xZ and recreated; the before-census files were re-taken after it. | CLOSED 20260927T170220Z |
| K1C | verify | K1-CRED deleted after the login | ParameterNotFound | ~D logged in 17:02:23Z (msg 20260927T170305Z); 17:0xZ ssm delete-parameter /irpt/ui-walk-principal/1790528299/password; the named get-parameter -> ParameterNotFound. | CLOSED 20260927T170413Z |
| K8 | verify | ONE export | exactly 1 export POST; READY with %PDF page_count>=1 (served object) or a named NOT_READY/DEPENDENCY_UNAVAILABLE; render token ParameterNotFound | RUN and REFUSED server-side, a named refusal with nothing written; the tenant AND report-reference hops now hold. K7 (~D 101984): 8.05% PARTIAL, RPT-b5e0a16e (a REOPEN of a report an earlier window's principal computed). K8: ONE POST /export?selected_tenant=49financial at 17:04:54Z with authorized_report_revisions {report_id RPT-b5e0a16e2f287219af5dd6174c49d8fb, revision 39c11079..} (IV-e-65 live); 200 ok=false UNAVAILABLE/OBJECT_NOT_COVERED. irpt-export-render log 17:04:56Z: ReportDenied 'report access denied' (corr-73d2bfaaa1ca). Cause: export/retained_export.py:34-50 authorizer admits a report ONLY when the caller IS its owner (same firm_id AND principal_id) -- every walk window uses a NEW principal, and RPT-b5e0a16e's owner is an earlier window's; the adapter's reopen (P-REOPEN-01) admits a second authorized viewer, the export does not. A product gap (a second viewer can read but not export), an authorization decision for the CTO. Nothing exported: render tokens 0->0, exr 2->2, 49F irpt-requests 142->142. | CLOSED 20260927T171213Z |
| D1 | verify | K1 delete after the export is terminal (<= 120 min) | failing consistent read | ~D 101984: walk closed 17:06:25Z; the export terminal at submit (refused); 17:10:49Z walk_principal.py --kind=uiwalk delete 1790528299: K1 consistent GetItem no Item (VERIFIED); K1-CRED ParameterNotFound (deleted 17:04Z); cap cron b276224e cancelled. | CLOSED 20260927T171213Z |
| A1 | verify | route audit + write trace | 0 outside the classes; export rows/objects traced to the exportId; users == baseline; 0 new media in git; K1 absent | HAR w16-20260927.har (454 entries, sha256 be336c172e20b7fa..): writes = POST auth/login 1, auth/refresh 4, directory/resolve 2, selections 3, export 1 (the admitted K8 POST); no download; 0 outside the classes. Byte-proof (~D): HEAD e8a00b23, 0 tracked, 0 /__mockcot/ of 454. Write trace: REPORT# 49F 20->20 / COT 2->2 / INF 1->1; SELECTION# 49->49; 49F irpt-requests 142->142; W16 chain census before == after; render tokens 0->0; exr 2->2; users 51->51 digest 76cbe66b.. equal; tracked media 929->929 (0 new). K1 absent. | CLOSED 20260927T171214Z |

## Log

- 20260927T162226Z OPENED by 2.0.0_SA_COO~P with 5 leg(s)
- 20260927T170220Z LEG C1 closed: both halves at HEAD naming blob 907073b1 (CTO @93780555f5 101962: opens only after window 15's amendment principal is de
- 20260927T170413Z LEG K1C closed: ~D logged in 17:02:23Z (msg 20260927T170305Z); 17:0xZ ssm delete-parameter /irpt/ui-walk-principal/1790528299/password; 
- 20260927T171213Z LEG K8 closed: RUN and REFUSED server-side, a named refusal with nothing written; the tenant AND report-reference hops now hold. K7 (~D
- 20260927T171213Z LEG D1 closed: ~D 101984: walk closed 17:06:25Z; the export terminal at submit (refused); 17:10:49Z walk_principal.py --kind=uiwalk del
- 20260927T171214Z LEG A1 closed: HAR w16-20260927.har (454 entries, sha256 be336c172e20b7fa..): writes = POST auth/login 1, auth/refresh 4, directory/res
- 20260927T171214Z CLOSED -- all 5 legs proven

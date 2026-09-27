# Deploy Completion Record
**Date opened:** 2026-09-27T14:55:54.625794+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260927T151356Z
**Deploy:** window 14: K8, the FIRST real export, re-cut on local portal DEV 55bbdd71 (IV-e-64: submit/receipt/download carry selectedTenant) -- window 12's shape (packet NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W14_K8_EXPORT_20260927.md); no vendor call; halves pending
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| C1 | activation | K1 + K1-CRED | both halves at HEAD naming the blob; pins + portal HEAD 55bbdd71 re-read equal; pre-read + censuses; put + read-back | both halves at HEAD naming blob 423314f1 (CTO @426fa8c8ce 101926, CRO @bae0782a84 101923: only the page pin moves, every condition carries); pins re-read 15:0xZ equal: adapter bOefL9nx no plan, IRPT_EVIDENCE_BUCKET opal-data-ycharts; irpt-export-render ryEMGlRu IRPT_EXPORT_RENDER=on; SSM doc irpt-export-render-run v5; irpt-status bMMJ/bQ+5; directory-search o1TXq5PH; portal HEAD 55bbdd71, 0 tracked changes; C: 15 GB free; tracked media baseline 929; pre-read epoch 1790521328 ABSENT; censuses before: users 51 digest 76cbe66b, SELECTION# 49, REPORT# 49F 20 / COT 1 / INF 1, 49F irpt-requests 142, exr 2, render tokens 0, W14 chain census; K1-CRED then K1 put USER#usr_irptuiwalk_1790521328 at 15:03:02Z, read-back EQUAL; cap cron 3ca23588 at 16:57Z (120 min = 17:03Z). | CLOSED 20260927T150623Z |
| K1C | verify | K1-CRED deleted after the login | ParameterNotFound | ~D logged in 15:04:16Z (msg 20260927T150439Z); 15:0xZ ssm delete-parameter /irpt/ui-walk-principal/1790521328/password; the named get-parameter -> ParameterNotFound. | CLOSED 20260927T150623Z |
| K8 | verify | ONE export | exactly 1 export POST; READY with %PDF page_count>=1 (served object) or a named NOT_READY/DEPENDENCY_UNAVAILABLE; render token ParameterNotFound | RUN and REFUSED server-side, a named refusal with nothing written; the TENANT hop now holds (S23). K7 (~D 101932): 8.05% PARTIAL, RPT-b5e0a16e (a reopen). K8: ONE POST /export?selected_tenant=49financial at 15:06:10Z, 200 ok=false UNAVAILABLE/DEPENDENCY_UNAVAILABLE; no export id, no download, no PDF. irpt-export-render log 15:06:13Z: ReportRefused 'invalid report reference' (corr-27eb154e587e, classified DEPENDENCY_UNAVAILABLE). Cause: the POST body's authorized_report_revisions = [{report_id: 39c11079.. (the REVISION hash), revision: 39c11079.., authorization_ref: 39c11079..}], but the server requires report_id RPT-<32 hex> (reports/repository.py:17, :67-68) -- it should be RPT-b5e0a16e2f287219af5dd6174c49d8fb; the adapter's answer carries report_id/revision/sha256 in data.retained_ref. A portal wire-mapping defect (~D, P 15:12:37Z). Nothing exported: render tokens 0->0, exr 2->2, 49F irpt-requests 142->142. K8 carries to a later window. | CLOSED 20260927T151355Z |
| D1 | verify | K1 delete after the export is terminal (<= 120 min) | failing consistent read | ~D 101932: walk closed 15:07:50Z; the export was terminal at submit (refused, no job); 15:11:59Z walk_principal.py --kind=uiwalk delete 1790521328: K1 consistent GetItem no Item (VERIFIED); K1-CRED ParameterNotFound (deleted 15:06Z); cap cron 3ca23588 cancelled. | CLOSED 20260927T151355Z |
| A1 | verify | route audit + write trace | 0 outside the classes; export rows/objects traced to the exportId; users == baseline; 0 new media in git; K1 absent | HAR w14-20260927.har (453 entries, sha256 41cc5d63903394ce..; leak-clean per ~D): writes = POST auth/login 1, auth/refresh 4, investor-reporting/directory/resolve 2, investor-reporting/selections 3, investor-reporting/export 1 (the admitted K8 POST); no download; 0 outside the classes. Byte-proof (~D): HEAD 55bbdd71, 0 tracked changes, 0 /__mockcot/ of 453. Write trace: REPORT# 49F 20->20 / COT 1->1 / INF 1->1; SELECTION# 49->49; 49F irpt-requests 142->142; W14 chain census before == after; render tokens 0->0; exr 2->2; users 51->51 digest 76cbe66b.. equal; tracked media 929 -> 929 (0 new). K1 absent. | CLOSED 20260927T151355Z |

## Log

- 20260927T145554Z OPENED by 2.0.0_SA_COO~P with 5 leg(s)
- 20260927T150623Z LEG C1 closed: both halves at HEAD naming blob 423314f1 (CTO @426fa8c8ce 101926, CRO @bae0782a84 101923: only the page pin moves, every
- 20260927T150623Z LEG K1C closed: ~D logged in 15:04:16Z (msg 20260927T150439Z); 15:0xZ ssm delete-parameter /irpt/ui-walk-principal/1790521328/password; 
- 20260927T151355Z LEG K8 closed: RUN and REFUSED server-side, a named refusal with nothing written; the TENANT hop now holds (S23). K7 (~D 101932): 8.05%
- 20260927T151355Z LEG D1 closed: ~D 101932: walk closed 15:07:50Z; the export was terminal at submit (refused, no job); 15:11:59Z walk_principal.py --kin
- 20260927T151355Z LEG A1 closed: HAR w14-20260927.har (453 entries, sha256 41cc5d63903394ce..; leak-clean per ~D): writes = POST auth/login 1, auth/refre
- 20260927T151356Z CLOSED -- all 5 legs proven

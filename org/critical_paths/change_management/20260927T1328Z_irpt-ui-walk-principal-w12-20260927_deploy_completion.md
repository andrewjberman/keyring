# Deploy Completion Record
**Date opened:** 2026-09-27T13:28:08.108962+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260927T140500Z
**Deploy:** window 12: K8, the FIRST real export, re-cut on local portal DEV 1f149d69 (IV-e-53) -- ~D's K7 49F ****9978 YTD read + ONE export POST (render ON), window 10's shape (packet NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W12_K8_EXPORT_20260927.md); no vendor call; halves pending
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| C1 | activation | K1 + K1-CRED | both halves at HEAD naming the blob; pins re-read equal; pre-read + censuses; put + read-back | both halves at HEAD naming blob 36c196ed (CTO @0fe93a1b92 101890: only the page pin moves, window 10's conditions carried; CRO @377a66b6de 101891: byte-proof checks on 1f149d69; K8 grades the export hop only); pins re-read 13:3xZ equal: adapter bOefL9nx no plan, IRPT_EVIDENCE_BUCKET opal-data-ycharts; irpt-export-render ryEMGlRu IRPT_EXPORT_RENDER=on; SSM doc irpt-export-render-run v5; irpt-status bMMJ/bQ+5; directory-search o1TXq5PH; portal HEAD 1f149d69; C: 14 GB free; tracked *.pdf/*.png/*.har baseline 929 (list saved); pre-read epoch 1790516081 K1/email/K1-CRED ABSENT; censuses before: users 51 digest 76cbe66b, SELECTION# 49, REPORT# 49F 20 / COT 1 / INF 1, 49F irpt-requests 142 rows, exr objects 2, /irpt/render-token/ 0, W12 chain census; K1-CRED then K1 put USER#usr_irptuiwalk_1790516081 at 13:35:19Z, read-back EQUAL; cap cron at 15:29Z (120 min = 15:35Z). | CLOSED 20260927T133624Z |
| K1C | verify | K1-CRED deleted after the login | ParameterNotFound | ~D 101898 logged in 13:42:26Z; 13:43:4xZ ssm delete-parameter /irpt/ui-walk-principal/1790516081/password; the named get-parameter -> ParameterNotFound. | CLOSED 20260927T134411Z |
| K8 | verify | ONE export | exactly 1 export POST; READY with %PDF page_count>=1 (served object) or a named NOT_READY/DEPENDENCY_UNAVAILABLE; render token ParameterNotFound | RUN and REFUSED server-side, a named refusal with nothing written. K7 13:43:42Z (~D 101902): 2 Performance GETs carrying selected_tenant=49financial, PARTIAL, RPT-b5e0a16e (a reopen; 49F REPORT# 20 -> 20), 8.05% on the face. K8: the preview resolved on 1f149d69 (IV-e-53 works), and exactly ONE POST /export at 13:44:21Z answered 200 UNAVAILABLE/UNEXPECTED (HAR w12-20260927.har). irpt-export-render log 13:44:22Z: BucketUnmapped, then submit-export public_reason_code UNEXPECTED (corr-83fe081e2112) -- the POST carried no selected_tenant, because buildSubmitRequest (portal submit.ts:64-78, ExportButton.tsx:213) never sets selectedTenant, so served.py resolved the internal viewer's own firm. Nothing exported: no exportId, render tokens 0 -> 0, no irpt-export-render-run SendCommand, evidence-bucket firms/49financial/generations/ 2 -> 2, 49F irpt-requests 142 -> 142. Fix (submit + receipt + download selectedTenant) cut by ~D as a direct act (101907). K8 carries to a later window. | CLOSED 20260927T140500Z |
| D1 | verify | K1 delete after the export is terminal (<= 120 min) | failing consistent read | ~D 101907: walk closed and browser shut 14:01:27Z; the export was terminal at submit (refused, no job); 14:03:20Z walk_principal.py --kind=uiwalk delete 1790516081: K1 consistent GetItem no Item (VERIFIED); K1-CRED ParameterNotFound (deleted 13:43:4xZ); cap cron 31d9d62d cancelled. | CLOSED 20260927T140500Z |
| A1 | verify | route audit + write trace | 0 outside the classes; export rows/objects traced to the exportId; users == baseline; 0 new media in git; K1 absent | HAR w12-20260927.har (462 entries, sha256 7bfe69acee655fcb.. re-hashed; leaks clean per ~D): writes = POST auth/login 1, auth/refresh 5, investor-reporting/directory/resolve 2, investor-reporting/selections 3, investor-reporting/export 1 (the admitted K8 POST); no download; 0 outside the classes. CRO 101891 byte-proof: HEAD 1f149d69, 0 tracked changes, 0 /__mockcot/ at start and end. Write trace: REPORT# 49F 20->20 / COT 1->1 / INF 1->1; SELECTION# 49->49; 49F irpt-requests 142->142; W12 chain census (cottonwood) before == after; render tokens 0->0; exr objects 2->2; users 51->51 digest 76cbe66b.. equal; tracked *.pdf/*.png/*.har 929 -> 929 (0 new). Proof of no later use: K1 absent. | CLOSED 20260927T140500Z |

## Log

- 20260927T132808Z OPENED by 2.0.0_SA_COO~P with 5 leg(s)
- 20260927T133624Z LEG C1 closed: both halves at HEAD naming blob 36c196ed (CTO @0fe93a1b92 101890: only the page pin moves, window 10's conditions carrie
- 20260927T134411Z LEG K1C closed: ~D 101898 logged in 13:42:26Z; 13:43:4xZ ssm delete-parameter /irpt/ui-walk-principal/1790516081/password; the named get
- 20260927T140500Z LEG K8 closed: RUN and REFUSED server-side, a named refusal with nothing written. K7 13:43:42Z (~D 101902): 2 Performance GETs carrying
- 20260927T140500Z LEG D1 closed: ~D 101907: walk closed and browser shut 14:01:27Z; the export was terminal at submit (refused, no job); 14:03:20Z walk_p
- 20260927T140500Z LEG A1 closed: HAR w12-20260927.har (462 entries, sha256 7bfe69acee655fcb.. re-hashed; leaks clean per ~D): writes = POST auth/login 1,
- 20260927T140500Z CLOSED -- all 5 legs proven

# Deploy Completion Record
**Date opened:** 2026-10-20T14:15:50.323771+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261020T142806Z
**Deploy:** IRPT_ANLREQ TO-PROMOTE-GUARD: promote ONE portal branch cand/dell2/anlreq-submission-guard-commentary (head e9ca1106dd, ONE commit cut from PROD f48e09ddf95e, 2 files: the submission guard admits the optional boolean commentary_requested) DEV->PROD via /prod-deploy chosen-set release; Opal-internal, row dell2-20261020T115847Z-4bfc APPROVED by the CTO; rollback = revert of the promote on PROD
**Authored by:** 0.4.0_DT_ClientPlatform~DELL2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | PROD push of release containing only branch cand/dell2/anlreq-submission-guard-commentary | promoted sha and PROD before/after | origin/PROD f48e09ddf95e (portal-v2.1.247) -> 4546cee0528c (push receipt f48e09dd..4546cee0; origin/PROD re-read before push = f48e09ddf95e); release = 1 non-merge commit e9ca1106dd + 1 builder merge, 2 files, 0 trade; tag portal-v2.1.248 peels to 4546cee0528c | CLOSED 20261020T142805Z |
| L2 | verify | deploy.yml CI run on promoted sha | gh run view --json conclusion success, tag peeled; PROD content equals the branch | run 39438860151 Deploy to Production completed success 14:26:36Z (Build 14:25:57Z, Deploy to S3 + CloudFront 14:26:16Z = live, Tag 14:26:36Z), the only workflow on 4546cee0528c; diff e9ca1106dd origin/PROD empty; branch head ancestor of origin/PROD rc 0 | CLOSED 20261020T142805Z |
| L3 | verify | Ticket Center and New Analysis Request render read on PROD | screenshot read or ABSENT with reason | stubbed session (a stub, not a staff login) on the served PROD bundle: the Ticket Center opened and the New Analysis Request form rendered with the five Opal models at first paint and the File Analysis Request button (probes PASS, nonsense probe FAIL); firms cannot load in the stub; nothing filed; screenshot guard_prod_analysis_request_form_stubbed.png | CLOSED 20261020T142806Z |

## Log

- 20261020T141550Z OPENED by 0.4.0_DT_ClientPlatform~DELL2 with 3 leg(s)
- 20261020T142805Z LEG L1 closed: origin/PROD f48e09ddf95e (portal-v2.1.247) -> 4546cee0528c (push receipt f48e09dd..4546cee0; origin/PROD re-read before 
- 20261020T142805Z LEG L2 closed: run 39438860151 Deploy to Production completed success 14:26:36Z (Build 14:25:57Z, Deploy to S3 + CloudFront 14:26:16Z =
- 20261020T142806Z LEG L3 closed: stubbed session (a stub, not a staff login) on the served PROD bundle: the Ticket Center opened and the New Analysis Req
- 20261020T142806Z CLOSED -- all 3 legs proven

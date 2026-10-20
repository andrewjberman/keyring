# Deploy Completion Record
**Date opened:** 2026-10-20T09:19:12.634615+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261020T093032Z
**Deploy:** IRPT_ANLREQ TO-PROMOTE-V024: promote ONE branch cand/dell2/anlreq-v024-prod-recut (head 6755297790, EIGHT commits cut from PROD e890aaa94f, 26 files: the v0.24 Ticket Center Analysis Request set) DEV->PROD via /prod-deploy chosen-set release; Opal-internal, row dell2-20261020T085534Z-935a APPROVED by the CTO; rollback = revert of the promote on PROD
**Authored by:** 0.4.0_DT_ClientPlatform~DELL2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | PROD push of release containing only branch cand/dell2/anlreq-v024-prod-recut | promoted sha and PROD before/after | origin/PROD e890aaa94fea (portal-v2.1.246) -> f48e09ddf95e (push receipt e890aaa9..f48e09dd; origin/PROD re-read before push = e890aaa94fea); release = 8 non-merge commits of cand/dell2/anlreq-v024-prod-recut (head 6755297790) + 1 builder merge, 26 files, 0 trade; tag portal-v2.1.247 peels to f48e09ddf95e | CLOSED 20261020T093031Z |
| L2 | verify | deploy.yml CI run on promoted sha | gh run view --json conclusion success, tag peeled; PROD content equals the branch | run 39400700239 Deploy to Production completed success 09:28:56Z (Build 09:28:24Z, Deploy to S3 + CloudFront 09:28:44Z = live, Tag 09:28:55Z), the only workflow on f48e09ddf95e; diff 6755297790 origin/PROD empty; branch head ancestor of origin/PROD rc 0 | CLOSED 20261020T093031Z |
| L3 | verify | staff Ticket Center read on PROD | screenshot read or ABSENT with reason | ABSENT: stubbed internal Dev admin session, no live API; the Analysis Request form on the served bundle shows the five Opal models at first paint, Advisor optional, no report type or commentary choice; the Firm chooser reads Firms not loaded (resolve-scope failed); nothing filed; screenshot v024_prod_analysis_request_form_stubbed.png | CLOSED 20261020T093032Z |

## Log

- 20261020T091912Z OPENED by 0.4.0_DT_ClientPlatform~DELL2 with 3 leg(s)
- 20261020T093031Z LEG L1 closed: origin/PROD e890aaa94fea (portal-v2.1.246) -> f48e09ddf95e (push receipt e890aaa9..f48e09dd; origin/PROD re-read before 
- 20261020T093031Z LEG L2 closed: run 39400700239 Deploy to Production completed success 09:28:56Z (Build 09:28:24Z, Deploy to S3 + CloudFront 09:28:44Z =
- 20261020T093032Z LEG L3 closed: ABSENT: stubbed internal Dev admin session, no live API; the Analysis Request form on the served bundle shows the five O
- 20261020T093032Z CLOSED -- all 3 legs proven

# Deploy Completion Record
**Date opened:** 2026-10-20T15:57:05.211583+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261020T164039Z
**Deploy:** IRPT_ANLREQ TO-PROMOTE-WALK: promote ONE portal branch cand/dell2/anlreq-andrew-walk-v2 (head d5d2fdeab3, ONE commit cut from PROD 4546cee0528c, 12 files under src/pages/TicketCenter: the Analysis Request form always sends the Advisor) DEV->PROD via /prod-deploy chosen-set release; Opal-internal, row dell2-20261020T153500Z-4664 APPROVED by the CTO; cand/dell2/anlreq-andrew-walk excluded; rollback = revert of the promote on PROD
**Authored by:** 0.4.0_DT_ClientPlatform~DELL2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | PROD push of release containing only branch cand/dell2/anlreq-andrew-walk-v2 | promoted sha and PROD before/after | PROD 4546cee0528c -> 234cddba2d83 pushed 16:34:58Z from release/20261020T162841Z, PROMOTE-LIST one branch cand/dell2/anlreq-andrew-walk-v2 @602ca19ef4 (row 5779) | CLOSED 20261020T164038Z |
| L2 | verify | deploy.yml CI run on promoted sha | gh run view --json conclusion success, tag peeled; PROD content equals the branch | run 39458711957 completed success on 234cddba2d83, live 16:37:16Z; tag portal-v2.1.249 peeled to it; diff 602ca19ef4 vs origin/PROD 0 lines, ancestor rc 0 | CLOSED 20261020T164038Z |
| L3 | verify | Ticket Center form render read on PROD (Advisor required) | screenshot read or ABSENT with reason | stubbed session on PROD: form opens, Advisor placeholder (required) and pre-filled Dev User PASS, Needed by and date input absent, five models PASS, nonsense probes FAIL; screenshot read (irpt_anlreq_walk/walk_prod_analysis_request_form_stubbed.png) | CLOSED 20261020T164039Z |

## Log

- 20261020T155705Z OPENED by 0.4.0_DT_ClientPlatform~DELL2 with 3 leg(s)
- 20261020T164038Z LEG L1 closed: PROD 4546cee0528c -> 234cddba2d83 pushed 16:34:58Z from release/20261020T162841Z, PROMOTE-LIST one branch cand/dell2/anl
- 20261020T164038Z LEG L2 closed: run 39458711957 completed success on 234cddba2d83, live 16:37:16Z; tag portal-v2.1.249 peeled to it; diff 602ca19ef4 vs 
- 20261020T164039Z LEG L3 closed: stubbed session on PROD: form opens, Advisor placeholder (required) and pre-filled Dev User PASS, Needed by and date inp
- 20261020T164039Z CLOSED -- all 3 legs proven

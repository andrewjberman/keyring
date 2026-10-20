# Deploy Completion Record
**Date opened:** 2026-10-20T15:57:05.211583+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-PROMOTE-WALK: promote ONE portal branch cand/dell2/anlreq-andrew-walk-v2 (head d5d2fdeab3, ONE commit cut from PROD 4546cee0528c, 12 files under src/pages/TicketCenter: the Analysis Request form always sends the Advisor) DEV->PROD via /prod-deploy chosen-set release; Opal-internal, row dell2-20261020T153500Z-4664 APPROVED by the CTO; cand/dell2/anlreq-andrew-walk excluded; rollback = revert of the promote on PROD
**Authored by:** 0.4.0_DT_ClientPlatform~DELL2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | PROD push of release containing only branch cand/dell2/anlreq-andrew-walk-v2 | promoted sha and PROD before/after |  | OPEN |
| L2 | verify | deploy.yml CI run on promoted sha | gh run view --json conclusion success, tag peeled; PROD content equals the branch |  | OPEN |
| L3 | verify | Ticket Center form render read on PROD (Advisor required) | screenshot read or ABSENT with reason |  | OPEN |

## Log

- 20261020T155705Z OPENED by 0.4.0_DT_ClientPlatform~DELL2 with 3 leg(s)

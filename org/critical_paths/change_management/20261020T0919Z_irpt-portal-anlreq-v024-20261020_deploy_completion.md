# Deploy Completion Record
**Date opened:** 2026-10-20T09:19:12.634615+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-PROMOTE-V024: promote ONE branch cand/dell2/anlreq-v024-prod-recut (head 6755297790, EIGHT commits cut from PROD e890aaa94f, 26 files: the v0.24 Ticket Center Analysis Request set) DEV->PROD via /prod-deploy chosen-set release; Opal-internal, row dell2-20261020T085534Z-935a APPROVED by the CTO; rollback = revert of the promote on PROD
**Authored by:** 0.4.0_DT_ClientPlatform~DELL2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | PROD push of release containing only branch cand/dell2/anlreq-v024-prod-recut | promoted sha and PROD before/after |  | OPEN |
| L2 | verify | deploy.yml CI run on promoted sha | gh run view --json conclusion success, tag peeled; PROD content equals the branch |  | OPEN |
| L3 | verify | staff Ticket Center read on PROD | screenshot read or ABSENT with reason |  | OPEN |

## Log

- 20261020T091912Z OPENED by 0.4.0_DT_ClientPlatform~DELL2 with 3 leg(s)

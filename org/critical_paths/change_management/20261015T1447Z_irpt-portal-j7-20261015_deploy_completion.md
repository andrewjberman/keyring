# Deploy Completion Record
**Date opened:** 2026-10-15T14:47:01.713917+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-PROMOTE-J7: promote ONE portal commit 6f4e5f671f09 (staff firm chooser) DEV->PROD via /prod-deploy chosen-set release; c8c3 excluded; rollback = revert of the promote merge on PROD
**Authored by:** 0.4.0_DT_ClientPlatform~DELL2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | PROD push of release containing only 6f4e5f671f09 | promoted sha and PROD before/after |  | OPEN |
| L2 | verify | deploy.yml CI run on promoted sha | gh run view --json conclusion success, tag peeled |  | OPEN |
| L3 | verify | staff read of Ticket Center on PROD | screenshot read or ABSENT with reason |  | OPEN |

## Log

- 20261015T144701Z OPENED by 0.4.0_DT_ClientPlatform~DELL2 with 3 leg(s)

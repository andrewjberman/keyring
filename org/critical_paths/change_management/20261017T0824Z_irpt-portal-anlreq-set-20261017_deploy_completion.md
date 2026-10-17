# Deploy Completion Record
**Date opened:** 2026-10-17T08:24:32.010200+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-PROMOTE-SET: promote ONE branch cand/dell2/anlreq-prod-recut-v2 (head 24034edcbb, 20 cherry-picked commits cut from PROD fa21a303d8, 36 files, Trade Request form excluded) DEV->PROD via /prod-deploy chosen-set release; client-facing pages included under Andrew word 9063a44a4c, row dell2-20261017T081434Z-4df0 APPROVED; rollback = git revert -m 1 of the promote merge on PROD
**Authored by:** 0.4.0_DT_ClientPlatform~DELL2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | PROD push of release containing only branch cand/dell2/anlreq-prod-recut-v2 | promoted sha and PROD before/after |  | OPEN |
| L2 | verify | deploy.yml CI run on promoted sha | gh run view --json conclusion success, tag peeled; PROD content equals the branch |  | OPEN |
| L3 | verify | staff Ticket Center read on PROD | screenshot read or ABSENT with reason |  | OPEN |

## Log

- 20261017T082432Z OPENED by 0.4.0_DT_ClientPlatform~DELL2 with 3 leg(s)

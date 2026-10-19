# Deploy Completion Record
**Date opened:** 2026-10-19T15:40:15.619311+00:00
**Status:** OPEN
**Deploy:** IRPT_DASHBD TO-DB-b-336: promote ONE approved branch cand/dell2/irpt-promote-all-dell2-ir-set-20261019 (head 8c52f547f4, three commits on PROD d729ee6d8456, 49 files: the Investor Reporting Performance set, the Trade Request form and the reveal of Trade Request in the New Ticket list; five dell1 files and commentary-always excluded) DEV->PROD via /prod-deploy chosen-set release; client-facing pages, Andrew word 2026-10-19 (records 142xZ and 144xZ) with the CTO closing the approval row; rollback = git revert -m 1 of the promote merge on PROD
**Authored by:** 0.4.0_DT_ClientPlatform~DELL2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | PROD push of release containing only branch cand/dell2/irpt-promote-all-dell2-ir-set-20261019 | promoted sha and PROD before/after |  | OPEN |
| L2 | verify | deploy.yml CI run on promoted sha | gh run view --json conclusion success, tag peeled |  | OPEN |
| L3 | verify | PROD pages read as staff-class and attachment-upload route read | screenshots read, route and env key names stated or ABSENT with reason |  | OPEN |

## Log

- 20261019T154015Z OPENED by 0.4.0_DT_ClientPlatform~DELL2 with 3 leg(s)

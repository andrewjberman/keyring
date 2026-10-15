# Deploy Completion Record
**Date opened:** 2026-10-15T17:59:39.709181+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-PROMOTE-HINT: promote TWO portal commits a6b83f692084 (filing hint, call 469b) and 406345bce1 (c8c3, commentary_requested always sent) DEV->PROD via /prod-deploy chosen-set release; keep-equal-pair excluded; rollback = revert of the promote merge on PROD (both), or c8c3 alone on ~Y2's word
**Authored by:** 0.4.0_DT_ClientPlatform~DELL2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | PROD push of release containing only a6b83f692084 and 406345bce1 | promoted sha and PROD before/after |  | OPEN |
| L2 | verify | deploy.yml CI run on promoted sha | gh run view --json conclusion success, tag peeled |  | OPEN |
| L3 | verify | staff read of Ticket Center on PROD | screenshot read or ABSENT with reason |  | OPEN |

## Log

- 20261015T175939Z OPENED by 0.4.0_DT_ClientPlatform~DELL2 with 3 leg(s)

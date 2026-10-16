# Deploy Completion Record
**Date opened:** 2026-10-16T03:48:08.734268+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-PROMOTE-PRICEDATE: promote TWO portal commits 39bebae9 (AR-y-360 no price-date input, T-1 close sentence) and 83993e17 (AR-y-361 prospect header as-of T-1 close) from cand/dell2/anlreq-no-price-date-t1-asof DEV->PROD via /prod-deploy chosen-set release; client-facing page, Andrew call 40fa; rollback = git revert -m 1 of the promote merge on PROD
**Authored by:** 0.4.0_DT_ClientPlatform~DELL2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | PROD push of release containing only 39bebae9 and 83993e17 | promoted sha and PROD before/after |  | OPEN |
| L2 | verify | deploy.yml CI run on promoted sha | gh run view --json conclusion success, tag peeled |  | OPEN |
| L3 | verify | prospect composer read on PROD | screenshot read or ABSENT with reason |  | OPEN |

## Log

- 20261016T034808Z OPENED by 0.4.0_DT_ClientPlatform~DELL2 with 3 leg(s)

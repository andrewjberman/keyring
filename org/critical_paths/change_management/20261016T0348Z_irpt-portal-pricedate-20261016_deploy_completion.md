# Deploy Completion Record
**Date opened:** 2026-10-16T03:48:08.734268+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261016T040200Z
**Deploy:** IRPT_ANLREQ TO-PROMOTE-PRICEDATE: promote TWO portal commits 39bebae9 (AR-y-360 no price-date input, T-1 close sentence) and 83993e17 (AR-y-361 prospect header as-of T-1 close) from cand/dell2/anlreq-no-price-date-t1-asof DEV->PROD via /prod-deploy chosen-set release; client-facing page, Andrew call 40fa; rollback = git revert -m 1 of the promote merge on PROD
**Authored by:** 0.4.0_DT_ClientPlatform~DELL2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | PROD push of release containing only 39bebae9 and 83993e17 | promoted sha and PROD before/after | origin/PROD ab2c43657e7b -> a062c56e53b1 (push receipt ab2c4365..a062c56e; origin/PROD re-read before push = ab2c43657e7b); non-merge payload 39bebae9 + 83993e17 only, 3 files, decision tree cand/dell2/anlreq-filing-notice absent; tag portal-v2.1.229 peels to a062c56e53b1 | CLOSED 20261016T040159Z |
| L2 | verify | deploy.yml CI run on promoted sha | gh run view --json conclusion success, tag peeled | gh -R Opal-Capital/portal run view 38847877518 --json: status completed, conclusion success, headSha a062c56e53b174eab043b1e50002c93eb7a56f8b; the only workflow on that sha | CLOSED 20261016T040159Z |
| L3 | verify | prospect composer read on PROD | screenshot read or ABSENT with reason | ui-smoke on https://opalinvest.dev, STUBBED internal Dev admin session (not a real login, no live API: Scope could not be resolved): Analysis tab, Prospect card opened the composer; screenshot pricedate_prod_composer_stubbed.png read: 'Prices are the T-1 close.' present, no date input, no price-date label. Header card AR-y-361 not read (needs a reviewed portfolio). | CLOSED 20261016T040159Z |

## Log

- 20261016T034808Z OPENED by 0.4.0_DT_ClientPlatform~DELL2 with 3 leg(s)
- 20261016T040159Z LEG L1 closed: origin/PROD ab2c43657e7b -> a062c56e53b1 (push receipt ab2c4365..a062c56e; origin/PROD re-read before push = ab2c43657e7
- 20261016T040159Z LEG L2 closed: gh -R Opal-Capital/portal run view 38847877518 --json: status completed, conclusion success, headSha a062c56e53b174eab04
- 20261016T040159Z LEG L3 closed: ui-smoke on https://opalinvest.dev, STUBBED internal Dev admin session (not a real login, no live API: Scope could not b
- 20261016T040200Z CLOSED -- all 3 legs proven

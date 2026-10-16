# Deploy Completion Record
**Date opened:** 2026-10-16T06:35:10.883290+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261016T065040Z
**Deploy:** IRPT_DASHBD TO-PROMOTE-UD: promote ONE approved branch cand/dell2/irpt-fwd10-unreported-days-sentence (head 9c24c7bdac, four commits, six files) DEV->PROD via /prod-deploy chosen-set release; Investor Reporting dashboard Performance tab, client-facing, Andrew approve 92c0; DB-c-26 excluded; rollback = git revert -m 1 of the promote merge on PROD
**Authored by:** 0.4.0_DT_ClientPlatform~DELL2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | PROD push of release containing only the four approved commits | promoted sha and PROD before/after | origin/PROD a062c56e53b1 -> 8012cd1afbaa (push receipt a062c56e..8012cd1a; origin/PROD re-read before push = a062c56e53b1); non-merge payload 7fa4d968 7ee50085 0018e4be 9c24c7bd only, 6 files, head 9c24c7bdac = approval head, DB-c-26 d562c6fc absent; tag portal-v2.1.230 peels to 8012cd1afbaa | CLOSED 20261016T065040Z |
| L2 | verify | deploy.yml CI run on promoted sha | gh run view --json conclusion success, tag peeled | gh -R Opal-Capital/portal run view 38862904307 --json: status completed, conclusion success, headSha 8012cd1afbaad0e537cf48b1fa5f5ddb1e549f9f; the only workflow on that sha | CLOSED 20261016T065040Z |
| L3 | verify | served bundle carries the sentence text (fixture-only) | match count in the one bundle file | FIXTURE-ONLY: served https://opalinvest.dev entry index-CEyGf5X_.js names resolveBundle-D6is_523.js (http 200, 71990 bytes): 'not reported by the source' 1 match, control unreported_trading_days 1, negative control 0. No live account carries unreported_trading_days yet; no page opened, no user minted, no client login. | CLOSED 20261016T065040Z |

## Log

- 20261016T063510Z OPENED by 0.4.0_DT_ClientPlatform~DELL2 with 3 leg(s)
- 20261016T065040Z LEG L1 closed: origin/PROD a062c56e53b1 -> 8012cd1afbaa (push receipt a062c56e..8012cd1a; origin/PROD re-read before push = a062c56e53b
- 20261016T065040Z LEG L2 closed: gh -R Opal-Capital/portal run view 38862904307 --json: status completed, conclusion success, headSha 8012cd1afbaad0e537c
- 20261016T065040Z LEG L3 closed: FIXTURE-ONLY: served https://opalinvest.dev entry index-CEyGf5X_.js names resolveBundle-D6is_523.js (http 200, 71990 byt
- 20261016T065040Z CLOSED -- all 3 legs proven

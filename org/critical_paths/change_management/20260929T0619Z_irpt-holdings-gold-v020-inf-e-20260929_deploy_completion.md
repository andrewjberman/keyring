# Deploy Completion Record
**Date opened:** 2026-09-29T06:19:10.931045+00:00
**Status:** OPEN
**Deploy:** TO-IB-er-301: producer to PRD v0.20 (rulings 13-17), re-emit all 557 49F holdings-gold days, mint the Inflection slice 2020-04-27..2026-09-25
**Authored by:** 0.4.0_DS_ClientPlatform~E
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | producer + sources.json + tests on branch ds-e-irpt-r3-holdings | commit hash |  | OPEN |
| L2 | s3-prefix | opal-data-49financial irpt/49financial/gold/holdings_performance_{daily,manifest} 557 days re-emitted under v0.20 | E3-AC4 PASS line |  | OPEN |
| L3 | s3-prefix | opal-data-inflection irpt/inflection/gold/holdings_performance_{daily,manifest} every computable trading day | E3-AC1 + E3-AC2 PASS lines |  | OPEN |
| L4 | verify | all three acceptance checks re-run by the issuer from the workspace root | check output |  | OPEN |

## Log

- 20260929T061910Z OPENED by 0.4.0_DS_ClientPlatform~E with 4 leg(s)

# Deploy Completion Record
**Date opened:** 2026-10-06T21:42:03.820971+00:00
**Status:** OPEN
**Deploy:** MX-s-17: point opal-bd-transaction-download and opal-bd-realized-download at code/silver/merge-daily-incremental.py (never-widen halves CTO @fb8486aa9f + COO @27501e83dd)
**Authored by:** 0.7.0_AE_CloudOps~MI
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| S9 | verify | read-only SSM import check (boto3+pandas) on the documents target instance -- Z-W24-S9 disarm | yes |  | OPEN |
| D1 | activation | opal-bd-transaction-download v4 set DEFAULT, Default==Latest read back | yes |  | OPEN |
| D2 | activation | opal-bd-realized-download v4 set DEFAULT, Default==Latest read back | yes |  | OPEN |

## Log

- 20261006T214203Z OPENED by 0.7.0_AE_CloudOps~MI with 3 leg(s)

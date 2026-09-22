# Deploy Completion Record
**Date opened:** 2026-09-22T02:23:06.674519+00:00
**Status:** OPEN
**Deploy:** AMGT-rk-91 move M2: filings/v1 source.json to filing_source silver + filing_attempt state
**Authored by:** 0.9.0_WK_AMGT_RESAPP~91
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | filing_source silver (14 rows) + filing_attempt state (180 keys) copies | per-object round-trip equal (AC4) |  | OPEN |
| L2 | activation | state grant added to opal-amgt-scoped-api-grants + opal-amgt-scoped-api redeployed | live re-read present + invoke equal (AC6) |  | OPEN |
| L3 | activation | filings/v1 grant removed from opal-amgt-scoped-api-grants | live re-read absent, state present, invokes equal (AC6) |  | OPEN |

## Log

- 20260922T022306Z OPENED by 0.9.0_WK_AMGT_RESAPP~91 with 3 leg(s)

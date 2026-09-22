# Deploy Completion Record
**Date opened:** 2026-09-22T20:14:46.589007+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260922T201749Z
**Deploy:** Lenovo 992_HK_Equity issuer-site filings battery
**Authored by:** 0.9.0_WK_AMGT_RESAPP~118
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| w4 | s3-prefix | opal-data-harvest/amgt/harvest/state/filing_attempt/security_key=992_HK_Equity/UNRESOLVED-SOURCE.json | AC3 | AC3: filing_attempt_992 count unchanged 1 (CHANGED-HELD wrote nothing, rk-105 write-once contract); foreign 0 | CLOSED 20260922T201737Z |
| w5 | s3-prefix | opal-data-harvest/filings/v1/992_HK_Equity/ | AC3 | AC3: filings_v1_992 count unchanged 1 (added 0, foreign 0); UNRESOLVED-SOURCE.source.json unchanged | CLOSED 20260922T201737Z |
| w3 | s3-prefix | opal-data-harvest/issuer-site/harvest/bronze/document/ | AC4 | AC4: issuer_doc_bronze pre 0 post 0 added 0 (crawl visited 1 page, 0 candidates); sec_filing_bronze pre 0 post 0 added 0; company_tickers pre 0 post 1 added 1 (step 1 ran, first estate-wide) | CLOSED 20260922T201737Z |
| v | verify | served thesis route for 992 | AC5 | AC5: thesis 992_HK_Equity -> 200, control CAT_US_Equity -> 200, no regression | CLOSED 20260922T201738Z |

## Log

- 20260922T201446Z OPENED by 0.9.0_WK_AMGT_RESAPP~118 with 4 leg(s)
- 20260922T201737Z LEG w4 closed: AC3: filing_attempt_992 count unchanged 1 (CHANGED-HELD wrote nothing, rk-105 write-once contract); foreign 0
- 20260922T201737Z LEG w5 closed: AC3: filings_v1_992 count unchanged 1 (added 0, foreign 0); UNRESOLVED-SOURCE.source.json unchanged
- 20260922T201737Z LEG w3 closed: AC4: issuer_doc_bronze pre 0 post 0 added 0 (crawl visited 1 page, 0 candidates); sec_filing_bronze pre 0 post 0 added 0
- 20260922T201738Z LEG v closed: AC5: thesis 992_HK_Equity -> 200, control CAT_US_Equity -> 200, no regression
- 20260922T201749Z CLOSED -- all 4 legs proven

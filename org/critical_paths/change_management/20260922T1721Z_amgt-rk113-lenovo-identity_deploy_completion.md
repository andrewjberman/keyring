# Deploy Completion Record
**Date opened:** 2026-09-22T17:21:13.750339+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260922T172645Z
**Deploy:** AMGT-rk-113 Lenovo identity pull (992 HK Equity)
**Authored by:** 0.9.0_WK_AMGT_RESAPP~113
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| w1 | s3-prefix | opal-data-harvest/bloomberg/harvest/bronze/identity/security_key=992_HK_Equity/ | AC3 | AC3: identity_bronze D0+1=4, exactly one 992 key | CLOSED 20260922T172236Z |
| w3 | s3-prefix | opal-data-harvest/crosswalk/v1/ | AC3 | AC3: records 96=pre 96, others_byte_equal 95 of 95, 992_non_identity_equal True | CLOSED 20260922T172236Z |
| w2 | git | lib/research/identity/registrations.json | AC3 | AC3: registrations G0+1=8, 992 row (ENRICH, MEASURED) | CLOSED 20260922T172236Z |
| v | verify | crosswalk resolve 992 | AC4 | AC4: resolve('992 HK')/'992 HK Equity' security_key+resolution unchanged; provenance gains only the anticipated provenance.identity line (B1); CAT US/CSL AU/6861 JP controls equal_to_pre True | CLOSED 20260922T172615Z |

## Log

- 20260922T172113Z OPENED by 0.9.0_WK_AMGT_RESAPP~113 with 4 leg(s)
- 20260922T172236Z LEG w1 closed: AC3: identity_bronze D0+1=4, exactly one 992 key
- 20260922T172236Z LEG w2 closed: AC3: registrations G0+1=8, 992 row (ENRICH, MEASURED)
- 20260922T172236Z LEG w3 closed: AC3: records 96=pre 96, others_byte_equal 95 of 95, 992_non_identity_equal True
- 20260922T172615Z LEG v closed: AC4: resolve('992 HK')/'992 HK Equity' security_key+resolution unchanged; provenance gains only the anticipated provenan
- 20260922T172645Z CLOSED -- all 4 legs proven

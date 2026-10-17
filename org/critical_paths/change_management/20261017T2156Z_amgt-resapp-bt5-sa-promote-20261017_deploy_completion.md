# Deploy Completion Record
**Date opened:** 2026-10-17T21:56:05.118163+00:00
**Status:** OPEN
**Deploy:** AMGT_RESAPP bt-5: PROD promote of amgt-sa-earnings-long-dates + amgt-sa-price-currency-trim + amgt-sa-model-tooltip-last-rows (Security Analysis, Opal-internal), then fold-back preparation
**Authored by:** 0.4.0_DT_ClientPlatform~H2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | portal PROD push of the release branch | PROD head hash, ls-remote read |  | OPEN |
| L2 | verify | CI deploy workflow on the PROD head | conclusion success read by headSha |  | OPEN |
| L3 | verify | PROMOTE_RECEIPT_BT5.md, overlap-sha file and fold branch prepared | receipt path, sha count, TREE-EQUALS-DEV |  | OPEN |

## Log

- 20261017T215605Z OPENED by 0.4.0_DT_ClientPlatform~H2 with 3 leg(s)

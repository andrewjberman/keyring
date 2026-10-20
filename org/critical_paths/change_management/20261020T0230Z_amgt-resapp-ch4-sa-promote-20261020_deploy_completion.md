# Deploy Completion Record
**Date opened:** 2026-10-20T02:30:14.770114+00:00
**Status:** OPEN
**Deploy:** AMGT_RESAPP ch-4: chosen-set PROD promote of amgt-sa-reader-words + amgt-sa-status-words (Security Analysis, Opal-internal); no DEV write, no fold-back
**Authored by:** 0.4.0_DT_ClientPlatform~H2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | portal PROD push of the chosen-set release branch | PROD head hash, ls-remote read |  | OPEN |
| L2 | verify | CI deploy workflow on the PROD head, tag peeled | conclusion success read by headSha, tag peeled to the PROD head |  | OPEN |
| L3 | verify | PROMOTE_RECEIPT_CH4.md written and committed | receipt path and commit |  | OPEN |

## Log

- 20261020T023014Z OPENED by 0.4.0_DT_ClientPlatform~H2 with 3 leg(s)

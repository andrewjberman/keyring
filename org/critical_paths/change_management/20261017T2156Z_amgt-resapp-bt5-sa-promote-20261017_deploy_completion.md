# Deploy Completion Record
**Date opened:** 2026-10-17T21:56:05.118163+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261017T220246Z
**Deploy:** AMGT_RESAPP bt-5: PROD promote of amgt-sa-earnings-long-dates + amgt-sa-price-currency-trim + amgt-sa-model-tooltip-last-rows (Security Analysis, Opal-internal), then fold-back preparation
**Authored by:** 0.4.0_DT_ClientPlatform~H2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | portal PROD push of the release branch | PROD head hash, ls-remote read | PROD 856fb37b -> d1bed0fbbce13db794e5f91b92452464394f8f3a; ls-remote read refs/heads/PROD = d1bed0fbbce13db794e5f91b92452464394f8f3a | CLOSED 20261017T215814Z |
| L2 | verify | CI deploy workflow on the PROD head | conclusion success read by headSha | gh run 39073112254 Deploy to Production completed success on headSha d1bed0fbbce13db794e5f91b92452464394f8f3a (only workflow for that sha); tag portal-v2.1.238 peels to it | CLOSED 20261017T220201Z |
| L3 | verify | PROMOTE_RECEIPT_BT5.md, overlap-sha file and fold branch prepared | receipt path, sha count, TREE-EQUALS-DEV | receipt 5ac72ac795 PROMOTE_RECEIPT_BT5.md; FOLDBACK_OVERLAP_SHAS_R113.txt 121 shas; fold branch cand/dell1/prod-into-dev-fold-r113 002681be TREE-EQUALS-DEV (local, not registered); AC1 10 EQUAL; AC2 completed success; AC3 6 | CLOSED 20261017T220246Z |

## Log

- 20261017T215605Z OPENED by 0.4.0_DT_ClientPlatform~H2 with 3 leg(s)
- 20261017T215814Z LEG L1 closed: PROD 856fb37b -> d1bed0fbbce13db794e5f91b92452464394f8f3a; ls-remote read refs/heads/PROD = d1bed0fbbce13db794e5f91b9245
- 20261017T220201Z LEG L2 closed: gh run 39073112254 Deploy to Production completed success on headSha d1bed0fbbce13db794e5f91b92452464394f8f3a (only work
- 20261017T220246Z LEG L3 closed: receipt 5ac72ac795 PROMOTE_RECEIPT_BT5.md; FOLDBACK_OVERLAP_SHAS_R113.txt 121 shas; fold branch cand/dell1/prod-into-dev
- 20261017T220246Z CLOSED -- all 3 legs proven

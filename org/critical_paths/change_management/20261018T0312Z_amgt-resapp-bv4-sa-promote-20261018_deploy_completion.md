# Deploy Completion Record
**Date opened:** 2026-10-18T03:12:18.408325+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261018T031916Z
**Deploy:** AMGT_RESAPP bv-4: PROD promote of amgt-sa-remaining-date-bypasses (Security Analysis, Opal-internal), then fold-back preparation
**Authored by:** 0.4.0_DT_ClientPlatform~H2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | portal PROD push of the release branch | PROD head hash, ls-remote read | PROD 26d998f7 -> ff61156612682ec15c67d79c92f6ce30a1d95a4f; ls-remote read refs/heads/PROD = ff61156612682ec15c67d79c92f6ce30a1d95a4f | CLOSED 20261018T031436Z |
| L2 | verify | CI deploy workflow on the PROD head | conclusion success read by headSha | gh run 39092905765 Deploy to Production completed success on headSha ff61156612682ec15c67d79c92f6ce30a1d95a4f (only workflow for that sha); tag portal-v2.1.240 peels to it | CLOSED 20261018T031815Z |
| L3 | verify | PROMOTE_RECEIPT_BV4.md, overlap-sha file and fold branch prepared | receipt path, sha count, TREE-EQUALS-DEV | receipt 8d85badf52 PROMOTE_RECEIPT_BV4.md; FOLDBACK_OVERLAP_SHAS_R115.txt 129 shas; fold branch cand/dell1/prod-into-dev-fold-r115 39d439fb TREE-EQUALS-DEV (local, not registered); AC1 5 EQUAL; AC2 completed success; AC3 6 | CLOSED 20261018T031916Z |

## Log

- 20261018T031218Z OPENED by 0.4.0_DT_ClientPlatform~H2 with 3 leg(s)
- 20261018T031436Z LEG L1 closed: PROD 26d998f7 -> ff61156612682ec15c67d79c92f6ce30a1d95a4f; ls-remote read refs/heads/PROD = ff61156612682ec15c67d79c92f6
- 20261018T031815Z LEG L2 closed: gh run 39092905765 Deploy to Production completed success on headSha ff61156612682ec15c67d79c92f6ce30a1d95a4f (only work
- 20261018T031916Z LEG L3 closed: receipt 8d85badf52 PROMOTE_RECEIPT_BV4.md; FOLDBACK_OVERLAP_SHAS_R115.txt 129 shas; fold branch cand/dell1/prod-into-dev
- 20261018T031916Z CLOSED -- all 3 legs proven

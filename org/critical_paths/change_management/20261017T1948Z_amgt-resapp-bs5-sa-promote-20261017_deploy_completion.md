# Deploy Completion Record
**Date opened:** 2026-10-17T19:48:11.390068+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261017T195521Z
**Deploy:** AMGT_RESAPP bs-5: PROD promote of amgt-sa-price-currency-rule (Security Analysis, Opal-internal), then fold-back preparation
**Authored by:** 0.4.0_DT_ClientPlatform~H2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | portal PROD push of the release branch | PROD head hash, ls-remote read | PROD 932cea99 -> 856fb37b785c4b8a10190771410e3dfc9ac8e789; ls-remote read refs/heads/PROD = 856fb37b785c4b8a10190771410e3dfc9ac8e789 | CLOSED 20261017T195054Z |
| L2 | verify | CI deploy workflow on the PROD head | conclusion success read by headSha | gh run 39064168223 Deploy to Production completed success on headSha 856fb37b785c4b8a10190771410e3dfc9ac8e789 (only workflow for that sha); tag portal-v2.1.237 peels to it | CLOSED 20261017T195442Z |
| L3 | verify | PROMOTE_RECEIPT_BS5.md, overlap-sha file and fold branch prepared | receipt path, sha count, TREE-EQUALS-DEV | receipt a580659b1d PROMOTE_RECEIPT_BS5.md; FOLDBACK_OVERLAP_SHAS_R112.txt 116 shas; fold branch cand/dell1/prod-into-dev-fold-r112 118ede74 TREE-EQUALS-DEV (local, not registered); AC1 6 EQUAL; AC2 completed success; AC3 6 | CLOSED 20261017T195521Z |

## Log

- 20261017T194811Z OPENED by 0.4.0_DT_ClientPlatform~H2 with 3 leg(s)
- 20261017T195054Z LEG L1 closed: PROD 932cea99 -> 856fb37b785c4b8a10190771410e3dfc9ac8e789; ls-remote read refs/heads/PROD = 856fb37b785c4b8a10190771410e
- 20261017T195442Z LEG L2 closed: gh run 39064168223 Deploy to Production completed success on headSha 856fb37b785c4b8a10190771410e3dfc9ac8e789 (only work
- 20261017T195521Z LEG L3 closed: receipt a580659b1d PROMOTE_RECEIPT_BS5.md; FOLDBACK_OVERLAP_SHAS_R112.txt 116 shas; fold branch cand/dell1/prod-into-dev
- 20261017T195521Z CLOSED -- all 3 legs proven

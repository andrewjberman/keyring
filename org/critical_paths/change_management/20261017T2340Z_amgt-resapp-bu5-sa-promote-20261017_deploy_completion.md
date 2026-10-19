# Deploy Completion Record
**Date opened:** 2026-10-17T23:40:53.497876+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261017T234710Z
**Deploy:** AMGT_RESAPP bu-5: PROD promote of amgt-sa-peers-subject-currency + amgt-sa-page-dates-long-form + amgt-sa-model-grid-scroll-cue (Security Analysis, Opal-internal), then fold-back preparation
**Authored by:** 0.4.0_DT_ClientPlatform~H2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | portal PROD push of the release branch | PROD head hash, ls-remote read | PROD d1bed0fb -> 26d998f7f34015d3ad9d70360e9135ecf5d1ddfe; ls-remote read refs/heads/PROD = 26d998f7f34015d3ad9d70360e9135ecf5d1ddfe | CLOSED 20261017T234301Z |
| L2 | verify | CI deploy workflow on the PROD head | conclusion success read by headSha | gh run 39080069302 Deploy to Production completed success on headSha 26d998f7f34015d3ad9d70360e9135ecf5d1ddfe (only workflow for that sha); tag portal-v2.1.239 peels to it | CLOSED 20261017T234622Z |
| L3 | verify | PROMOTE_RECEIPT_BU5.md, overlap-sha file and fold branch prepared | receipt path, sha count, TREE-EQUALS-DEV | receipt 6ee6d1d9e9 PROMOTE_RECEIPT_BU5.md; FOLDBACK_OVERLAP_SHAS_R114.txt 126 shas; fold branch cand/dell1/prod-into-dev-fold-r114 6d328695 TREE-EQUALS-DEV (local, not registered); AC1 27 EQUAL; AC2 completed success; AC3 6 | CLOSED 20261017T234710Z |

## Log

- 20261017T234053Z OPENED by 0.4.0_DT_ClientPlatform~H2 with 3 leg(s)
- 20261017T234301Z LEG L1 closed: PROD d1bed0fb -> 26d998f7f34015d3ad9d70360e9135ecf5d1ddfe; ls-remote read refs/heads/PROD = 26d998f7f34015d3ad9d70360e91
- 20261017T234622Z LEG L2 closed: gh run 39080069302 Deploy to Production completed success on headSha 26d998f7f34015d3ad9d70360e9135ecf5d1ddfe (only work
- 20261017T234710Z LEG L3 closed: receipt 6ee6d1d9e9 PROMOTE_RECEIPT_BU5.md; FOLDBACK_OVERLAP_SHAS_R114.txt 126 shas; fold branch cand/dell1/prod-into-dev
- 20261017T234710Z CLOSED -- all 3 legs proven

# Deploy Completion Record
**Date opened:** 2026-10-17T18:16:50.838734+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261017T182418Z
**Deploy:** AMGT_RESAPP br-5: PROD promote of amgt-sa-changed-object-cells + amgt-sa-pe-footer-words + amgt-sa-peers-currency (Security Analysis, Opal-internal), then fold-back preparation
**Authored by:** 0.4.0_DT_ClientPlatform~H2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | portal PROD push of the release branch | PROD head hash, ls-remote read | PROD 99d2b2a7 -> 932cea99e8cabffa7ca28d2d57aba1e923d4e591; ls-remote read refs/heads/PROD = 932cea99e8cabffa7ca28d2d57aba1e923d4e591 | CLOSED 20261017T181910Z |
| L2 | verify | CI deploy workflow on the PROD head | conclusion success read by headSha | gh run 39057551567 Deploy to Production completed success on headSha 932cea99e8cabffa7ca28d2d57aba1e923d4e591 (only workflow for that sha); tag portal-v2.1.236 peels to it | CLOSED 20261017T182418Z |
| L3 | verify | PROMOTE_RECEIPT_BR5.md, overlap-sha file and fold branch prepared | receipt path, sha count, TREE-EQUALS-DEV | receipt 82d3572422 PROMOTE_RECEIPT_BR5.md; FOLDBACK_OVERLAP_SHAS_R111.txt 111 shas; fold branch cand/dell1/prod-into-dev-fold-r111 f3aa4207 TREE-EQUALS-DEV (local, not registered); AC1 13 EQUAL; AC2 completed success; AC3 6 | CLOSED 20261017T182418Z |

## Log

- 20261017T181650Z OPENED by 0.4.0_DT_ClientPlatform~H2 with 3 leg(s)
- 20261017T181910Z LEG L1 closed: PROD 99d2b2a7 -> 932cea99e8cabffa7ca28d2d57aba1e923d4e591; ls-remote read refs/heads/PROD = 932cea99e8cabffa7ca28d2d57ab
- 20261017T182418Z LEG L2 closed: gh run 39057551567 Deploy to Production completed success on headSha 932cea99e8cabffa7ca28d2d57aba1e923d4e591 (only work
- 20261017T182418Z LEG L3 closed: receipt 82d3572422 PROMOTE_RECEIPT_BR5.md; FOLDBACK_OVERLAP_SHAS_R111.txt 111 shas; fold branch cand/dell1/prod-into-dev
- 20261017T182418Z CLOSED -- all 3 legs proven

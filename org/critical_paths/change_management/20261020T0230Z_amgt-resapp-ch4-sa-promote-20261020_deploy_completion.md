# Deploy Completion Record
**Date opened:** 2026-10-20T02:30:14.770114+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261020T023848Z
**Deploy:** AMGT_RESAPP ch-4: chosen-set PROD promote of amgt-sa-reader-words + amgt-sa-status-words (Security Analysis, Opal-internal); no DEV write, no fold-back
**Authored by:** 0.4.0_DT_ClientPlatform~H2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | portal PROD push of the chosen-set release branch | PROD head hash, ls-remote read | PROD ba2c3412 -> e890aaa94fea58506a6670cf663a38f67345617d (release/20261020T023043Z, fast-forward); ls-remote read refs/heads/PROD = e890aaa94fea58506a6670cf663a38f67345617d | CLOSED 20261020T023350Z |
| L2 | verify | CI deploy workflow on the PROD head, tag peeled | conclusion success read by headSha, tag peeled to the PROD head | gh run 39359584436 Deploy to Production completed success on headSha e890aaa94fea58506a6670cf663a38f67345617d (the only workflow listed for that sha); tag portal-v2.1.246 peels to it (rev-parse tag^{commit} = e890aaa94f) | CLOSED 20261020T023649Z |
| L3 | verify | PROMOTE_RECEIPT_CH4.md written and committed | receipt path and commit | receipt bb7678a264 PROMOTE_RECEIPT_CH4.md; FOLDBACK_OVERLAP_SHAS_R126.txt 153 shas; fold branch cand/dell1/prod-into-dev-fold-r126 8de015fca6 TREE-EQUALS-DEV, rev-list DEV..HEAD 4 (local, nothing registered, DEV not written) | CLOSED 20261020T023848Z |

## Log

- 20261020T023014Z OPENED by 0.4.0_DT_ClientPlatform~H2 with 3 leg(s)
- 20261020T023350Z LEG L1 closed: PROD ba2c3412 -> e890aaa94fea58506a6670cf663a38f67345617d (release/20261020T023043Z, fast-forward); ls-remote read refs/
- 20261020T023649Z LEG L2 closed: gh run 39359584436 Deploy to Production completed success on headSha e890aaa94fea58506a6670cf663a38f67345617d (the only 
- 20261020T023848Z LEG L3 closed: receipt bb7678a264 PROMOTE_RECEIPT_CH4.md; FOLDBACK_OVERLAP_SHAS_R126.txt 153 shas; fold branch cand/dell1/prod-into-dev
- 20261020T023848Z CLOSED -- all 3 legs proven

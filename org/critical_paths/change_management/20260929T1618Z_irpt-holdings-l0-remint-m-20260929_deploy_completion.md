# Deploy Completion Record
**Date opened:** 2026-09-29T16:18:55.165349+00:00
**Status:** OPEN
**Deploy:** L0 re-mint: irpt_holdings_{49f,inf,cot} from CLOUD a11debe552 (CATEGORY, vendor keys, assigned strategy, 49F registration labels)
**Authored by:** 0.9.0_WK_IRPT_BCKEND~76
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 24.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| M1 | s3-prefix | safe-deploy --mint-bundle irpt_holdings_49f | BUNDLE MINTED line + head-object members-sha256 + member-count | BUNDLE MINTED [standalone] irpt_holdings_49f -> s3://opal-data-49financial/irpt/49financial/code/gold/investor-reporting-holdings.tar.gz (md5=8b122a961fb1fb54e4a0a5fe6cadcc05); head-object members-sha256=c695465758ea424b332dc639a0e0eadef3d4286053206ed96ce90b1fa0a06e3b member-count=43 | CLOSED 20260929T162316Z |
| M2 | s3-prefix | safe-deploy --mint-bundle irpt_holdings_inf | BUNDLE MINTED line + head-object members-sha256 + member-count | BUNDLE MINTED [standalone] irpt_holdings_inf -> s3://opal-data-inflection/irpt/inflection/code/gold/investor-reporting-holdings.tar.gz (md5=8b122a961fb1fb54e4a0a5fe6cadcc05); head-object members-sha256=c695465758ea424b332dc639a0e0eadef3d4286053206ed96ce90b1fa0a06e3b member-count=43 | CLOSED 20260929T162342Z |
| M3 | s3-prefix | safe-deploy --mint-bundle irpt_holdings_cot | BUNDLE MINTED line + head-object members-sha256 + member-count | BUNDLE MINTED [standalone] irpt_holdings_cot -> s3://opal-data-cottonwood/irpt/cottonwood/code/gold/investor-reporting-holdings.tar.gz (md5=8b122a961fb1fb54e4a0a5fe6cadcc05); head-object members-sha256=c695465758ea424b332dc639a0e0eadef3d4286053206ed96ce90b1fa0a06e3b member-count=43 | CLOSED 20260929T162342Z |
| Q1 | verify | irpt-holdings-refresh-lambda QA fire {"qa": true} publishes to holdings_qa | 3 of 3 Success + per-firm holdings_qa read: CATEGORY names, source_vendor_keys, COT assigned_strategy, 49F registration labels |  | OPEN |
| V1 | verify | 49financial SERVED Holdings object read at next scheduled irpt-holdings-snapshot publication | key+VersionId equal before/after the QA fire |  | OPEN |
| V2 | verify | inflection SERVED Holdings object read at next scheduled irpt-holdings-snapshot publication | key+VersionId equal before/after the QA fire |  | OPEN |
| V3 | verify | cottonwood SERVED Holdings object read at next scheduled irpt-holdings-snapshot publication | key+VersionId equal before/after the QA fire |  | OPEN |

## Log

- 20260929T161855Z OPENED by 0.9.0_WK_IRPT_BCKEND~76 with 7 leg(s)
- 20260929T162316Z LEG M1 closed: BUNDLE MINTED [standalone] irpt_holdings_49f -> s3://opal-data-49financial/irpt/49financial/code/gold/investor-reporting
- 20260929T162342Z LEG M2 closed: BUNDLE MINTED [standalone] irpt_holdings_inf -> s3://opal-data-inflection/irpt/inflection/code/gold/investor-reporting-h
- 20260929T162342Z LEG M3 closed: BUNDLE MINTED [standalone] irpt_holdings_cot -> s3://opal-data-cottonwood/irpt/cottonwood/code/gold/investor-reporting-h

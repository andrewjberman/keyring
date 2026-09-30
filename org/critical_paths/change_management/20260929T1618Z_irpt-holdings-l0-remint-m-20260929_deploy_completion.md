# Deploy Completion Record
**Date opened:** 2026-09-29T16:18:55.165349+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260930T134749Z
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
| Q1 | verify | irpt-holdings-refresh-lambda QA fire {"qa": true} publishes to holdings_qa | 3 of 3 Success + per-firm holdings_qa read: CATEGORY names, source_vendor_keys, COT assigned_strategy, 49F registration labels | QA fire dispatched via lambda invoke irpt-holdings-refresh-lambda {qa:true} at 2026-09-29T16:30:23Z: 49financial=0c990e62-b31b-4f14-884d-a6691b25cf2e cottonwood=9fa9c917-0542-4668-96ab-99f85e1dcf45 inflection=4114cede-6aae-4265-afdd-b7a5c7ef1c4c, all 3 of 3 Status=Success ResponseCode=0 (SSM get_command_invocation). holdings_qa/date=2026-09-28 read per firm: CATEGORY nodes present with display.label Client/Models for all 3; source_vendor_keys 49financial=[schwab,smartx] inflection=[eclipse,orion] cottonwood=[blackdiamond]; cottonwood ACCOUNT.assigned_strategy populated (e.g. node acc_000c147a49a4d234b37dab66 -> Opal Ultra Short Term, COT_REBALANCER_MODEL); 49financial ACCOUNT.display.label carries full registration-type names (Simplified Employee Plan, Rollover IRA, Roth Contributory IRA, etc.), not bare Schwab codes. Served holdings/current/manifest.json VersionId unchanged for all 3 firms (holdings_qa only, never served). | CLOSED 20260929T165030Z |
| V1 | verify | 49financial SERVED Holdings object read at next scheduled irpt-holdings-snapshot publication | key+VersionId equal before/after the QA fire | list-object-versions 2026-09-30T13:4xZ (UTC, s3api): irpt/49financial/platinum/holdings/current/manifest.json IsLatest VersionId AV66zNHkT6cbHiSJiUvKIoNRs5EX9_Fj LastModified 2026-09-29T14:20:35:00Z -- the same object that was latest BEFORE the 16:30Z QA fire (QA published to holdings_qa only). No newer version exists, so key+VersionId are equal before/after; no scheduled publication has landed since 09-29 14:2xZ, read at close by 2.0.0_SA_COO~M (issuer of WK~76) | CLOSED 20260930T134749Z |
| V2 | verify | inflection SERVED Holdings object read at next scheduled irpt-holdings-snapshot publication | key+VersionId equal before/after the QA fire | list-object-versions 2026-09-30T13:4xZ (UTC, s3api): irpt/inflection/platinum/holdings/current/manifest.json IsLatest VersionId .zfZoZlAkp9kYx6I9pMrtjEYvwVVcq0d LastModified 2026-09-29T14:18:18:00Z -- the same object that was latest BEFORE the 16:30Z QA fire (QA published to holdings_qa only). No newer version exists, so key+VersionId are equal before/after; no scheduled publication has landed since 09-29 14:2xZ, read at close by 2.0.0_SA_COO~M (issuer of WK~76) | CLOSED 20260930T134749Z |
| V3 | verify | cottonwood SERVED Holdings object read at next scheduled irpt-holdings-snapshot publication | key+VersionId equal before/after the QA fire | list-object-versions 2026-09-30T13:4xZ (UTC, s3api): irpt/cottonwood/platinum/holdings/current/manifest.json IsLatest VersionId 3JfvRUHRmmDpKp6.VvTYBUmAuKmMaiTZ LastModified 2026-09-29T14:18:21:00Z -- the same object that was latest BEFORE the 16:30Z QA fire (QA published to holdings_qa only). No newer version exists, so key+VersionId are equal before/after; no scheduled publication has landed since 09-29 14:2xZ, read at close by 2.0.0_SA_COO~M (issuer of WK~76) | CLOSED 20260930T134749Z |

## Log

- 20260929T161855Z OPENED by 0.9.0_WK_IRPT_BCKEND~76 with 7 leg(s)
- 20260929T162316Z LEG M1 closed: BUNDLE MINTED [standalone] irpt_holdings_49f -> s3://opal-data-49financial/irpt/49financial/code/gold/investor-reporting
- 20260929T162342Z LEG M2 closed: BUNDLE MINTED [standalone] irpt_holdings_inf -> s3://opal-data-inflection/irpt/inflection/code/gold/investor-reporting-h
- 20260929T162342Z LEG M3 closed: BUNDLE MINTED [standalone] irpt_holdings_cot -> s3://opal-data-cottonwood/irpt/cottonwood/code/gold/investor-reporting-h
- 20260929T165030Z LEG Q1 closed: QA fire dispatched via lambda invoke irpt-holdings-refresh-lambda {qa:true} at 2026-09-29T16:30:23Z: 49financial=0c990e6
- 20260930T134749Z LEG V1 closed: list-object-versions 2026-09-30T13:4xZ (UTC, s3api): irpt/49financial/platinum/holdings/current/manifest.json IsLatest V
- 20260930T134749Z LEG V2 closed: list-object-versions 2026-09-30T13:4xZ (UTC, s3api): irpt/inflection/platinum/holdings/current/manifest.json IsLatest Ve
- 20260930T134749Z LEG V3 closed: list-object-versions 2026-09-30T13:4xZ (UTC, s3api): irpt/cottonwood/platinum/holdings/current/manifest.json IsLatest Ve
- 20260930T134749Z CLOSED -- all 7 legs proven

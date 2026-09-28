# Deploy Completion Record
**Date opened:** 2026-09-28T19:18:46.411839+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260928T192305Z
**Deploy:** R4 D.0: re-mint irpt_holdings_{49f,inf,cot} from CLOUD bcf7a6adde+ (cash rule + UIC-16); nothing scheduled runs them
**Authored by:** 0.9.0_WK_IRPT_BCKEND~42
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| M1 | s3-prefix | safe-deploy --mint-bundle irpt_holdings_49f | BUNDLE MINTED line + head-object members-sha256 + member-count | BUNDLE MINTED [standalone] irpt_holdings_49f -> s3://opal-data-49financial/irpt/49financial/code/gold/investor-reporting-holdings.tar.gz (md5=8a38d29f52d1eabc6892a3f8fec49a14); head-object echoed members-sha256=a2866ed29a82318385469985f53fbdebcc59ff4b718c3360a0a6568a2728961f member-count=40 | CLOSED 20260928T192248Z |
| M2 | s3-prefix | safe-deploy --mint-bundle irpt_holdings_inf | BUNDLE MINTED line + head-object members-sha256 + member-count | BUNDLE MINTED [standalone] irpt_holdings_inf -> s3://opal-data-inflection/irpt/inflection/code/gold/investor-reporting-holdings.tar.gz (md5=8a38d29f52d1eabc6892a3f8fec49a14); head-object echoed members-sha256=a2866ed29a82318385469985f53fbdebcc59ff4b718c3360a0a6568a2728961f member-count=40 | CLOSED 20260928T192248Z |
| M3 | s3-prefix | safe-deploy --mint-bundle irpt_holdings_cot | BUNDLE MINTED line + head-object members-sha256 + member-count | BUNDLE MINTED [standalone] irpt_holdings_cot -> s3://opal-data-cottonwood/irpt/cottonwood/code/gold/investor-reporting-holdings.tar.gz (md5=8a38d29f52d1eabc6892a3f8fec49a14); head-object echoed members-sha256=a2866ed29a82318385469985f53fbdebcc59ff4b718c3360a0a6568a2728961f member-count=40 | CLOSED 20260928T192248Z |

## Log

- 20260928T191846Z OPENED by 0.9.0_WK_IRPT_BCKEND~42 with 3 leg(s)
- 20260928T192248Z LEG M1 closed: BUNDLE MINTED [standalone] irpt_holdings_49f -> s3://opal-data-49financial/irpt/49financial/code/gold/investor-reporting
- 20260928T192248Z LEG M2 closed: BUNDLE MINTED [standalone] irpt_holdings_inf -> s3://opal-data-inflection/irpt/inflection/code/gold/investor-reporting-h
- 20260928T192248Z LEG M3 closed: BUNDLE MINTED [standalone] irpt_holdings_cot -> s3://opal-data-cottonwood/irpt/cottonwood/code/gold/investor-reporting-h
- 20260928T192305Z CLOSED -- all 3 legs proven

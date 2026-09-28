# Deploy Completion Record
**Date opened:** 2026-09-28T20:57:58.909952+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260928T210152Z
**Deploy:** R4 D.0 amendment 1: re-mint irpt_holdings_{49f,inf,cot} after re-tracing _IRPT_HOLDINGS_CLOSURE to add lib/silver_ids.py; nothing scheduled runs them
**Authored by:** 0.9.0_WK_IRPT_BCKEND~42
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| M1 | s3-prefix | safe-deploy --mint-bundle irpt_holdings_49f | BUNDLE MINTED line + head-object members-sha256 + member-count | BUNDLE MINTED [standalone] irpt_holdings_49f -> s3://opal-data-49financial/irpt/49financial/code/gold/investor-reporting-holdings.tar.gz member-count=41 members-sha256=185dd52f6a97cdd49924fd84cd7060585f6f09db4e7eb3a6957f4ab927f8b9a1; head-object confirms Metadata members-sha256=185dd52f6a97cdd49924fd84cd7060585f6f09db4e7eb3a6957f4ab927f8b9a1 member-count=41 | CLOSED 20260928T210136Z |
| M2 | s3-prefix | safe-deploy --mint-bundle irpt_holdings_inf | BUNDLE MINTED line + head-object members-sha256 + member-count | BUNDLE MINTED [standalone] irpt_holdings_inf -> s3://opal-data-inflection/irpt/inflection/code/gold/investor-reporting-holdings.tar.gz member-count=41 members-sha256=185dd52f6a97cdd49924fd84cd7060585f6f09db4e7eb3a6957f4ab927f8b9a1; head-object confirms Metadata members-sha256=185dd52f6a97cdd49924fd84cd7060585f6f09db4e7eb3a6957f4ab927f8b9a1 member-count=41 | CLOSED 20260928T210137Z |
| M3 | s3-prefix | safe-deploy --mint-bundle irpt_holdings_cot | BUNDLE MINTED line + head-object members-sha256 + member-count | BUNDLE MINTED [standalone] irpt_holdings_cot -> s3://opal-data-cottonwood/irpt/cottonwood/code/gold/investor-reporting-holdings.tar.gz member-count=41 members-sha256=185dd52f6a97cdd49924fd84cd7060585f6f09db4e7eb3a6957f4ab927f8b9a1; head-object confirms Metadata members-sha256=185dd52f6a97cdd49924fd84cd7060585f6f09db4e7eb3a6957f4ab927f8b9a1 member-count=41 | CLOSED 20260928T210137Z |

## Log

- 20260928T205758Z OPENED by 0.9.0_WK_IRPT_BCKEND~42 with 3 leg(s)
- 20260928T210136Z LEG M1 closed: BUNDLE MINTED [standalone] irpt_holdings_49f -> s3://opal-data-49financial/irpt/49financial/code/gold/investor-reporting
- 20260928T210137Z LEG M2 closed: BUNDLE MINTED [standalone] irpt_holdings_inf -> s3://opal-data-inflection/irpt/inflection/code/gold/investor-reporting-h
- 20260928T210137Z LEG M3 closed: BUNDLE MINTED [standalone] irpt_holdings_cot -> s3://opal-data-cottonwood/irpt/cottonwood/code/gold/investor-reporting-h
- 20260928T210152Z CLOSED -- all 3 legs proven

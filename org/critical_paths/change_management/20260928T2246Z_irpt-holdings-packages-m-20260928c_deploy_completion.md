# Deploy Completion Record
**Date opened:** 2026-09-28T22:46:42.096193+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260928T225400Z
**Deploy:** R4 D.0 (amendment 3 Step 9): re-mint irpt_holdings_{49f,inf,cot} after the 49F peak-RSS fix (redistribute_holdouts narrowed copy, commit c81280bd75); nothing scheduled runs them
**Authored by:** 0.9.0_WK_IRPT_BCKEND~42
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| M1 | s3-prefix | safe-deploy --mint-bundle irpt_holdings_49f | BUNDLE MINTED line + head-object members-sha256 + member-count | BUNDLE MINTED [standalone] irpt_holdings_49f -> s3://opal-data-49financial/irpt/49financial/code/gold/investor-reporting-holdings.tar.gz (md5=5378afa5b2afe0f7c8fcbf6d7f143a79); head-object members-sha256=94f2e3433d9ecc018027418ebb057c4ce6bfd2bb5baa45b8edb697f036421e5e member-count=41 | CLOSED 20260928T225318Z |
| M2 | s3-prefix | safe-deploy --mint-bundle irpt_holdings_inf | BUNDLE MINTED line + head-object members-sha256 + member-count | BUNDLE MINTED [standalone] irpt_holdings_inf -> s3://opal-data-inflection/irpt/inflection/code/gold/investor-reporting-holdings.tar.gz (md5=5378afa5b2afe0f7c8fcbf6d7f143a79); head-object members-sha256=94f2e3433d9ecc018027418ebb057c4ce6bfd2bb5baa45b8edb697f036421e5e member-count=41 | CLOSED 20260928T225342Z |
| M3 | s3-prefix | safe-deploy --mint-bundle irpt_holdings_cot | BUNDLE MINTED line + head-object members-sha256 + member-count | BUNDLE MINTED [standalone] irpt_holdings_cot -> s3://opal-data-cottonwood/irpt/cottonwood/code/gold/investor-reporting-holdings.tar.gz (md5=5378afa5b2afe0f7c8fcbf6d7f143a79); head-object members-sha256=94f2e3433d9ecc018027418ebb057c4ce6bfd2bb5baa45b8edb697f036421e5e member-count=41 | CLOSED 20260928T225343Z |

## Log

- 20260928T224642Z OPENED by 0.9.0_WK_IRPT_BCKEND~42 with 3 leg(s)
- 20260928T225318Z LEG M1 closed: BUNDLE MINTED [standalone] irpt_holdings_49f -> s3://opal-data-49financial/irpt/49financial/code/gold/investor-reporting
- 20260928T225342Z LEG M2 closed: BUNDLE MINTED [standalone] irpt_holdings_inf -> s3://opal-data-inflection/irpt/inflection/code/gold/investor-reporting-h
- 20260928T225343Z LEG M3 closed: BUNDLE MINTED [standalone] irpt_holdings_cot -> s3://opal-data-cottonwood/irpt/cottonwood/code/gold/investor-reporting-h
- 20260928T225400Z CLOSED -- all 3 legs proven

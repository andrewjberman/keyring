# Deploy Completion Record
**Date opened:** 2026-10-04T19:53:00.400919+00:00
**Status:** OPEN
**Deploy:** MDPF_SECCLASS batch 183 ONE packet: 32 multi_asset rows, the irpt_holdings re-mint (inf, cot, 49f) + directory bundle, route contract pin 4cc72587d6; COO half @1131610939 (blob a520d58900), CTO half batch 240; Andrew-direct ~22:1xZ 2026-10-03 'proceed call 2'
**Authored by:** 2.0.0_SA_COO~M
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P | verify | PROD carries readers; four served bundles at the half's versions; move dry run 7/0; CTO cond. 2 cot regroup count (each regrouped account 0 class change, equal total); CTO cond. 1 49F paired read before its mint | reads |  | OPEN |
| M | verify | 7 MOVES via move_multi_asset_rows.py --write; read back each row | get-item readback | 19:53:40Z move_multi_asset_rows.py --write (pre-read dry run 19:3xZ 7 MOVE / 0 REFUSED): WROTE {MOVE 7, ALREADY 0, REFUSED 0, WRITTEN 7, FAILED 0}; one conditional UpdateItem per row (compare-and-set on today's class, sub class, classified_by). Consistent get-item readback: AOR, VSMGX, VWELX, VWENX, ABALX multi_asset / Fixed Mix; VTHRX, VTIVX multi_asset / Target Date; each classified_by seed, updated_by mdpf-secclass-multi-asset, last_updated 2026-10-04T19:53:41.888776Z. Rollback: each row back to the TSV's column 4 (today's class / sub class / classified_by). | CLOSED 20261004T195528Z |
| S | verify | 13 ticker WRITES: module edit committed, seed-etf-classifications.py; 0 conflicts after M | seed output + readback | Module edit committed 96f17cdbe9 (20 tickers into infra/aws/lambda/v2_portal/_shared/etf_classification.py; _shared tests 80 passed; ruff clean; 0 non-ASCII added). 20:07:31Z seed-etf-classifications.py --region us-east-1 (no flag): 197 tickers, 177 already correct, 20 written (the 13 new tickers plus the 7 rows moved at M gaining name / sector / style, class unchanged), 1 preserved (VNQ management_style), 0 CONFLICT. Consistent get-item readback: 20 of 20 read multi_asset with a sub_asset_class. Second dry run: rows to write 0 of 197. Note: in --dry-run mode the script prints 'Writing N item(s)' and 'Items written: N' while skipping put_item (read: SGIIX, CAIBX, AAETX, MDLOX were ABSENT after the dry runs) -- the summary text misleads, the rule does not write. | CLOSED 20261004T201033Z |
| C | verify | 12 CUSIP: WRITES via write_cusip_rows.py | readback | Set file R9_CHECKS/MULTI_ASSET_CUSIP_SET_20261004.tsv (the 12 WRITE CUSIP: lines of MULTI_ASSET_ROW_SET_20261003.tsv, mechanically reformatted). Dry run: named 12, plan 12, already_present 0, refused 0 (table rows 2,854). 20:14:56Z write_cusip_rows.py --write: WRITTEN 12 of 12 (conditional put through etf_classification_scheduled.write()). Consistent get-item readback: 12 of 12 multi_asset with a sub_asset_class and identifier_namespace CUSIP. Re-run dry run: plan 0, already_present 12, refused 0, table rows 2,866 (= 2,841 + 13 tickers + 12 CUSIP rows). Rollback: a delete, on Andrew's word only. | CLOSED 20261004T201649Z |
| H | git | SERVE-RELEASE-ACK commit removing the DEPLOY-SERVE-HELD lines of 103971 and 103981 | commit hash |  | OPEN |
| R | s3-prefix | safe-deploy irpt_holdings_inf, irpt_holdings_cot (after cond. 2), directory bundle, irpt_holdings_49f (only through cond. 1); prior VersionIds recorded | deployed MATCH + prior VersionIds |  | OPEN |
| T | activation | irpt-holdings staged_from[8] pin to 4cc72587d6; build; safe-apply; live CodeSha256 | CodeSha256 read |  | OPEN |
| V | verify | next scheduled Holdings publication per firm: the packet's holdings carry multi_asset; account totals unchanged; readers render multi_asset | served reads |  | OPEN |

## Log

- 20261004T195300Z OPENED by 2.0.0_SA_COO~M with 8 leg(s)
- 20261004T195528Z LEG M closed: 19:53:40Z move_multi_asset_rows.py --write (pre-read dry run 19:3xZ 7 MOVE / 0 REFUSED): WROTE {MOVE 7, ALREADY 0, REFUS
- 20261004T201033Z LEG S closed: Module edit committed 96f17cdbe9 (20 tickers into infra/aws/lambda/v2_portal/_shared/etf_classification.py; _shared test
- 20261004T201649Z LEG C closed: Set file R9_CHECKS/MULTI_ASSET_CUSIP_SET_20261004.tsv (the 12 WRITE CUSIP: lines of MULTI_ASSET_ROW_SET_20261003.tsv, me

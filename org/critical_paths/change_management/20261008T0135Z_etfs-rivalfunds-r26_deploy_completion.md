# Deploy Completion Record
**Date opened:** 2026-10-08T01:35:58.592724+00:00
**Status:** OPEN
**Deploy:** ETFS_RIVALS rounds 25+26 readers (RIV-rg-1 narrowed by RIV-rg-2): five rivalfunds Lambdas at CLOUD 0576fb051f, one republish of 2026-10-07 refresh_a1 true; must move no served figure (halves: COO a4ce155438, CTO e081a672d4; rg-2 J1 MET ADJUDICATION_v33; C1 MET msg 31527)
**Authored by:** 2.0.0_SA_COO~RV
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 14.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | safe-apply of C:/tmp/rv_apply26.tfplan: 5 aws_lambda_function.stage in place | five live CodeSha256 equal the plan after-set, MemorySize 3008, 5 of 5 |  | OPEN |
| L2 | verify | ONE republish etfs-rivalfunds-daily-lambda only publish-page date 2026-10-07 refresh_a1 true | return status OK plus REPORT Max Memory Used and Duration |  | OPEN |
| L3 | verify | served read: the three rebuilt tables row for row against the objects before them (one moved row is a rollback); chart data identical; sizes | the reads printed |  | OPEN |
| L4 | verify | first daily run on the shared reader, 2026-10-08 11:00Z (gold_canonical_shape and gold_trade_schedule) | status and REPORT lines; read with ledger etfs-rivalfunds-r22 L4 |  | OPEN |

## Log

- 20261008T013558Z OPENED by 2.0.0_SA_COO~RV with 4 leg(s)

# Deploy Completion Record
**Date opened:** 2026-10-08T00:05:30.570427+00:00
**Status:** OPEN
**Deploy:** ETFS_RIVALS RIV-mr-1 alone (the marker read-out, render.py only): five rivalfunds Lambdas at content pin fd633ec4d2 (live f9f8334ef6 + commit 339ba875be), one republish of 2026-10-07 refresh_a1 false (halves: COO 888f6d1b61, CTO 86a90330bc; mr-1 J1 MET ADJUDICATION_v30)
**Authored by:** 2.0.0_SA_COO~RV
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | safe-apply of C:/tmp/rv_apply25mr.tfplan: 5 aws_lambda_function.stage in place | five live CodeSha256 equal the plan after-set, MemorySize 3008, 5 of 5 |  | OPEN |
| L2 | verify | ONE republish etfs-rivalfunds-daily-lambda only publish-page date 2026-10-07 refresh_a1 false | return status OK plus REPORT Max Memory Used and Duration |  | OPEN |
| L3 | verify | served read: sizes against the prediction; 0 moved table rows (CTO C2: a moved row is a rollback); chart data identical; the same key classes as rounds 23 and 24 | the reads printed |  | OPEN |

## Log

- 20261008T000530Z OPENED by 2.0.0_SA_COO~RV with 3 leg(s)

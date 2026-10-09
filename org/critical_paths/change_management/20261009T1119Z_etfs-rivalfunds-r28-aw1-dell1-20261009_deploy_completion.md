# Deploy Completion Record
**Date opened:** 2026-10-09T11:19:42.145016+00:00
**Status:** OPEN
**Deploy:** ETFS_RIVALS R28 aw-1: rivalfunds code package at pin 39889dd4d7 to the five rivalfunds Lambdas (code only), applied from dell1
**Authored by:** 0.7.0_AE_CloudOps~DELL1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | the untargeted safe-apply of the window plan in /c/tmp/rv-r28-dell1/infra/aws/terraform/etfs-rivalfunds, moving exactly the five aws_lambda_function.stage code packages | five CodeSha256 moved and equal to the built packages, LastModified after the apply, State Active, LastUpdateStatus Successful, MemorySize still 3008, and a re-plan reading no changes |  | OPEN |
| L2 | verify | the 13:00Z sweep of 2026-10-09 (etfs-rivalfunds-sweep-daily, 09:00 ET) -- READ AND CLOSED BY THE ISSUER 2.0.0_SA_COO~V1, not by this seat | the issuer's read of the sweep; AC2 and the COO half's branches B and C are the issuer's and the CVO's to grade |  | OPEN |

## Log

- 20261009T111942Z OPENED by 0.7.0_AE_CloudOps~DELL1 with 2 leg(s)

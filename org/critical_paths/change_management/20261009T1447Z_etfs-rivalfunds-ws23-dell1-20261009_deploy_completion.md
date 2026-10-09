# Deploy Completion Record
**Date opened:** 2026-10-09T14:47:26.399081+00:00
**Status:** OPEN
**Deploy:** ETFS_RIVALS WS2/WS3: rivalfunds code package at pin b48273e3d0 to the five rivalfunds Lambdas (code only), applied from dell1 under the signed pair (COO @683b767406, CTO @20bd5c33db)
**Authored by:** 0.7.0_AE_CloudOps~RV1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | the safe-apply of the saved plan C:/tmp/rv_apply_ws23.tfplan from C:/tmp/rv-ws23-dell1/infra/aws/terraform/etfs-rivalfunds, moving exactly the five aws_lambda_function.stage code packages | five CodeSha256 moved and equal to the built zips (AC1), LastModified after the apply, State Active, LastUpdateStatus Successful, MemorySize 3008, the five environment key sets equal to the pre-apply read, and a re-plan at the same pin reading no changes |  | OPEN |
| L2 | verify | the issuer's read of the 2026-10-10 11:00Z chain and 13:00Z sweep against the writers table, and the per-key G2 compare against this deploy's snapshot (CTO condition 8) -- READ AND CLOSED BY THE ISSUER 2.0.0_SA_COO~V1, not by this seat | the issuer's read; AC2 and the COO half's branches are the issuer's and the CVO's to grade |  | OPEN |

## Log

- 20261009T144726Z OPENED by 0.7.0_AE_CloudOps~RV1 with 2 leg(s)

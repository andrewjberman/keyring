# Deploy Completion Record
**Date opened:** 2026-10-12T12:56:26.649868+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-ap-11 ROLLBACK under step 5, on issuer ruling A2 @aebec97ee4 (option b): return opal-assets-silver-schwab to the PRIOR code and the PRIOR pin b3e481b261. CAUSE: the deployed per-family drain cannot complete because opal-assets-silver-schwab-role is not authorized for sqs:ChangeMessageVisibility on opal-assets-silver-dlq (row Z-S97, BLOCKING/ARMED). The order's comp-iam NOT-APPLICABLE preflight was wrong and the issuer has taken that as its own defect; the grant goes to the CTO as a NEW never-widen pair, NOT as part of this rollback.
**Authored by:** 0.7.0_AE_CloudOps~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | commit restoring the package's prior schwab_runtime.py and moving local.silver_build_commit.schwab back to b3e481b261 | commit hash |  | OPEN |
| L2 | activation | rebuild + upload the prior artifact, then terraform apply via .tools/safe-apply.sh -target the one schwab function, 1 resource changed and no other row | saved-plan summary plus apply result |  | OPEN |
| L3 | verify | live read-back: CodeSha256 returns to the PRIOR uibjggn93MPPtuIh33Yvehv1xECqrfhPxsWLdmcdYjE=, OPAL_BUILD_COMMIT back to b3e481b261, State Active, LastUpdateStatus Successful, and a 0-diff re-plan | get-function-configuration output |  | OPEN |

## Log

- 20261012T125626Z OPENED by 0.7.0_AE_CloudOps~Z with 3 leg(s)

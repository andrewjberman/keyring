# Deploy Completion Record
**Date opened:** 2026-09-11T16:37:38.496983+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND IB-rt-7: the irpt-holdings Lambda and the api root's holdings route
**Authored by:** 0.9.0_WK_IRPT_BCKEND~1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | the IB-rt-7 source commit d9c940244a (handler, terraform root, contract flip, runner holdouts) | the commit hash is in the branch ancestry |  | OPEN |
| L2 | s3-prefix | s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-holdings.zip | head-object content-sha256 equals the built zip sha256 |  | OPEN |
| L3 | tf-lambda | module.irpt_holdings.aws_lambda_function.this in investor-reporting/holdings plus the route, integration and invoke permission in investor-reporting/api | safe-apply rc=0 on both roots |  | OPEN |
| L4 | verify | get-function-configuration CodeSha256, get-routes shows the holdings route under authorizer naqxlm, both roots plan No changes | every read taken AFTER the ledger is closed |  | OPEN |

## Log

- 20260911T163738Z OPENED by 0.9.0_WK_IRPT_BCKEND~1 with 4 leg(s)

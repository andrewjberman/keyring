# Deploy Completion Record
**Date opened:** 2026-10-01T04:15:35.617178+00:00
**Status:** OPEN
**Deploy:** SERVED MOVE of TO-IB-pr-271 (drained @cc20caf7b8; IRPT_BCKEND round 27 cell IB-pr-275, row S238): the served boundary refuses a SERVICE subject outside its allowedFirmIds -- five opal-users-v2 read grants apply and are simulated FIRST (CTO sweep-5 analysis section 2 item 1), then six functions take served.py @f6c6b56f40 plus the profile-reader closure; irpt-narrative excluded
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 12.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| G1 | activation | aws_iam_role_policy.performance_adapter_service_profile_read (root investor-reporting/performance) | safe-apply 1 add 0 change 0 destroy + simulate-principal-policy allowed x3 actions, one resource per call, context entries passed |  | OPEN |
| G2 | activation | aws_iam_role_policy.irpt_directory_service_profile_read (root investor-reporting/directory) | safe-apply 1 add 0 change 0 destroy + simulate allowed x3 |  | OPEN |
| G3 | activation | aws_iam_role_policy.export_render_service_profile_read (root investor-reporting/export) | safe-apply 1 add 0 change 0 destroy + simulate allowed x3 |  | OPEN |
| G4 | activation | aws_iam_role_policy.holdings_service_profile_read (root investor-reporting/holdings) | safe-apply 1 add 0 change 0 destroy + simulate allowed x3 |  | OPEN |
| G5 | activation | aws_iam_role_policy.irpt_status_service_profile_read (root investor-reporting/ops) | safe-apply 1 add 0 change 0 destroy + simulate allowed x3 |  | OPEN |
| F1 | tf-lambda | module.irpt_performance_adapter.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed CodeSha256 equals uploaded sha + member census: only served.py and reader closure differ from the BEFORE zip |  | OPEN |
| F2 | tf-lambda | module.irpt_directory_search.aws_lambda_function.this | same as F1 |  | OPEN |
| F3 | tf-lambda | module.irpt_ycharts_generate.aws_lambda_function.this | same as F1 |  | OPEN |
| F4 | tf-lambda | module.irpt_export_render.aws_lambda_function.this | same as F1 |  | OPEN |
| F5 | tf-lambda | module.irpt_holdings.aws_lambda_function.this | same as F1 |  | OPEN |
| F6 | tf-lambda | module.irpt_status.aws_lambda_function.this | same as F1 |  | OPEN |
| V1 | verify | served boundary on irpt-performance-adapter, both branches | a SERVICE subject selecting a foreign firm is refused AND the same subject selecting its own firm is served (row S238 disarm prints; CTO reads both) |  | OPEN |

## Log

- 20261001T041535Z OPENED by 2.0.0_SA_COO~P with 12 leg(s)

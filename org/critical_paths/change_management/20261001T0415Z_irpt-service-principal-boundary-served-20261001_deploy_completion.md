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
| G1 | activation | aws_iam_role_policy.performance_adapter_service_profile_read (root investor-reporting/performance) | safe-apply 1 add 0 change 0 destroy + simulate-principal-policy allowed x3 actions, one resource per call, context entries passed | safe-apply 05:10:41Z-05:12:04Z targeted: Plan 1 to add, 0 to change, 0 to destroy; Apply complete 1 added; get-role-policy reads the three statements (Query email-index, GetItem table, kms:Decrypt on key 64f25291); simulate-principal-policy irpt-performance-adapter-role: Query allowed, GetItem allowed, kms:Decrypt (with both context entries) allowed, one resource per call; positive control irpt-ycharts-generate-role allowed x3, negative control irpt-narrative-role implicitDeny x3 | CLOSED 20261001T052552Z |
| G2 | activation | aws_iam_role_policy.irpt_directory_service_profile_read (root investor-reporting/directory) | safe-apply 1 add 0 change 0 destroy + simulate allowed x3 |  | OPEN |
| G3 | activation | aws_iam_role_policy.export_render_service_profile_read (root investor-reporting/export) | safe-apply 1 add 0 change 0 destroy + simulate allowed x3 | safe-apply 05:13:12Z-05:14:52Z targeted: Plan 1 to add, 0 to change, 0 to destroy; Apply complete 1 added; simulate-principal-policy irpt-export-render-role: Query allowed, GetItem allowed, kms:Decrypt (with both context entries) allowed, one resource per call; same positive and negative control roles as G1 | CLOSED 20261001T052553Z |
| G4 | activation | aws_iam_role_policy.holdings_service_profile_read (root investor-reporting/holdings) | safe-apply 1 add 0 change 0 destroy + simulate allowed x3 |  | OPEN |
| G5 | activation | aws_iam_role_policy.irpt_status_service_profile_read (root investor-reporting/ops) | safe-apply 1 add 0 change 0 destroy + simulate allowed x3 |  | OPEN |
| F1 | tf-lambda | module.irpt_performance_adapter.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed CodeSha256 equals uploaded sha + member census: only served.py and reader closure differ from the BEFORE zip | under both halves (COO @40c790a0bf, CTO @d9972c6eb4, blob fbfe345d89): safe-apply 05:19:28Z targeted Plan 0 to add, 1 to change, 0 to destroy; applied 05:21:01Z; live CodeSha256 XslOsVc9AreOFwsgzC4frrDu4/m6ItTGeqoQRn8lN7M= equals the AFTER column; replan No changes; BEFORE and AFTER lambda invoke: empty headers -> CONTRACT_VERSION, enforcer-reaching event (firm cottonwood, non-existent user, performance-report) -> NOT_AUTHORIZED with a business date, no FunctionError, no errorMessage, identical both sides | CLOSED 20261001T052553Z |
| F2 | tf-lambda | module.irpt_directory_search.aws_lambda_function.this | same as F1 |  | OPEN |
| F3 | tf-lambda | module.irpt_ycharts_generate.aws_lambda_function.this | same as F1 | under both halves: safe-apply 05:21:46Z targeted Plan 0/1/0; applied 05:23:14Z; live CodeSha256 ESedDkLy40enY0fsupacLrXaUXzFw+UauPKNauOqeYc= equals AFTER; replan No changes; BEFORE and AFTER invoke: empty headers -> CONTRACT_VERSION, enforcer-reaching event (analysis-requests) -> NOT_AUTHORIZED with a business date, no FunctionError, no errorMessage, identical both sides | CLOSED 20261001T052553Z |
| F4 | tf-lambda | module.irpt_export_render.aws_lambda_function.this | same as F1 | under both halves: safe-apply 05:23:47Z targeted Plan 0/1/0; applied 05:25:02Z; live CodeSha256 WO5gDeP/fZ4jPl75NQ66BCR+9ixoRJVneIGsoBSxd6I= equals AFTER; replan No changes; BEFORE and AFTER invoke: empty headers -> CONTRACT_VERSION, enforcer-reaching event (export-receipt) -> NOT_AUTHORIZED with a business date, no FunctionError, no errorMessage, identical both sides | CLOSED 20261001T052553Z |
| F5 | tf-lambda | module.irpt_holdings.aws_lambda_function.this | same as F1 |  | OPEN |
| F6 | tf-lambda | module.irpt_status.aws_lambda_function.this | same as F1 |  | OPEN |
| V1 | verify | served boundary on irpt-performance-adapter, both branches | a SERVICE subject selecting a foreign firm is refused AND the same subject selecting its own firm is served (row S238 disarm prints; CTO reads both) |  | OPEN |

## Log

- 20261001T041535Z OPENED by 2.0.0_SA_COO~P with 12 leg(s)
- 20261001T052552Z LEG G1 closed: safe-apply 05:10:41Z-05:12:04Z targeted: Plan 1 to add, 0 to change, 0 to destroy; Apply complete 1 added; get-role-poli
- 20261001T052553Z LEG G3 closed: safe-apply 05:13:12Z-05:14:52Z targeted: Plan 1 to add, 0 to change, 0 to destroy; Apply complete 1 added; simulate-prin
- 20261001T052553Z LEG F1 closed: under both halves (COO @40c790a0bf, CTO @d9972c6eb4, blob fbfe345d89): safe-apply 05:19:28Z targeted Plan 0 to add, 1 to
- 20261001T052553Z LEG F3 closed: under both halves: safe-apply 05:21:46Z targeted Plan 0/1/0; applied 05:23:14Z; live CodeSha256 ESedDkLy40enY0fsupacLrXa
- 20261001T052553Z LEG F4 closed: under both halves: safe-apply 05:23:47Z targeted Plan 0/1/0; applied 05:25:02Z; live CodeSha256 WO5gDeP/fZ4jPl75NQ66BCR+

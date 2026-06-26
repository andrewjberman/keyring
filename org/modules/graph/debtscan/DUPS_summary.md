# comp-dups dimension summary -- 2026-06-26

Auto-emitted by `comp-dups --nightly` (NFRA_DEBTSCAN dups dimension). Advisory; NEVER removes.
Full candidate JSON is gitignored (regenerable); this small summary is the tracked audit trail.

## Suppression (audited, no silent suppression): 523 pairs
- BENIGN_CROSS_FIRM: 275
- BENIGN_IAM_POLICY_SPLIT: 148
- BENIGN_SERVICE_SPLIT: 84
- BENIGN_ENV_TWIN: 16

## CLASS A-high -- TF EXACT-label cross-module collisions: 10
- aws_iam_role_policy.step_functions_lambda_invoke <infra\aws\multi-account\terraform\environments\prod> ~ <infra\aws\terraform\bd-pipeline>
- aws_iam_role_policy.step_functions_lambda_invoke <infra\aws\multi-account\terraform\environments\staging> ~ <infra\aws\terraform\bd-pipeline>
- aws_iam_role.bd_exporter <infra\aws\ec2\bd-exporter\terraform> ~ <infra\aws\terraform\bd-pipeline>
- aws_dynamodb_table.opal_users_v2 <infra\aws\terraform\portal-auth> ~ <infra\aws\terraform\shared-infra>
- aws_cloudwatch_event_target.lambda <infra\aws\lambda\deprecated> ~ <infra\aws\multi-account\terraform\modules\lambda> [dead=INFERRED_DEAD_GRAPH_PENDING]
- aws_cloudwatch_log_group.lambda <infra\aws\multi-account\terraform\modules\lambda> ~ <infra\aws\terraform\modules\yang-lambda>
- aws_lambda_function.this <infra\aws\lambda\deprecated> ~ <infra\aws\terraform\modules\yang-lambda> [dead=INFERRED_DEAD_GRAPH_PENDING]
- aws_lambda_function.this <infra\aws\lambda\deprecated> ~ <infra\aws\multi-account\terraform\modules\lambda> [dead=INFERRED_DEAD_GRAPH_PENDING]
- aws_lambda_function.this <infra\aws\multi-account\terraform\modules\lambda> ~ <infra\aws\terraform\modules\yang-lambda>
- aws_iam_instance_profile.bd_exporter <infra\aws\ec2\bd-exporter\terraform> ~ <infra\aws\terraform\bd-pipeline>

## CLASS C1 -- CONTENT exact-body dup families: 6
- x3 (1267L) ['build_transaction_engine.py', 'build_transaction_engine_GOOD_1015AM.py', 'build_transaction_engine_v1_GOOD_2026-01-21_1015AM.py']
- x2 (145L) ['lambda_function.py', 'lambda_function_updated.py']
- x2 (771L) ['lambda_function.py', 'lambda_function_v1_backup.py']
- x2 (1348L) ['build_transaction_engine_BAD_with_closure_detection.py', 'build_transaction_engine_v2_BAD_closure_detection_2026-01-21_1432PM.py']
- x2 (248L) ['lambda_function.py', 'lambda_smartx_query.py']
- x2 (134L) ['lambda_function.py', 'lambda_function_simple.py']

## CONTENT corpus scanned: 3185 first-party py bodies

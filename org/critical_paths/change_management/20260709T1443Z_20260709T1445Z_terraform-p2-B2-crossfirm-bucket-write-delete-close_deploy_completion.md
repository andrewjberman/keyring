# Deploy Completion Record
**Date opened:** 2026-07-09T14:43:29.619539+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260709T144701Z
**Deploy:** B2: remove AmazonS3FullAccess + AmazonDynamoDBFullAccess from market-update-lambda-role. PARTIAL REMEDIATION of a live NEVER#1/NEVER#2 exposure: eliminates cross-firm WRITE+DELETE into opal-data-{bd,cot,inf} incl bd/gold and the SEV1 platinum artifact.
**Authored by:** 0.5.0_AE_OpalETL
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| tf-apply | verify | market-overview: detach S3FullAccess + DynamoDBFullAccess, add table-scoped DDB inline | apply + post-apply re-plan No changes | safe-apply: 1 added, 0 changed, 2 destroyed (detach AmazonS3FullAccess + AmazonDynamoDBFullAccess; create aws_iam_role_policy.market_update_dynamodb_scoped). Post-apply drift plan: 'No changes.' | CLOSED 20260709T144700Z |
| crossfirm-closed | verify | s3 Put/Delete on opal-data-bd,-cot,-inf -> implicitDeny vs the pre-apply allowed baseline | comp-denytest output | comp-denytest --from-plan --baseline, rc=0 PASS. Change type DERIVED from the plan (attachment DELETE -> allow-removal -> expected implicitDeny). 3/3 implicitDeny on s3:PutObject into opal-data-{bd,cot,inf}/gold/, against a pre-apply baseline recording all three as ALLOWED -- falsifiable, not vacuous. Additionally, the two worst capabilities directly: s3:DeleteObject opal-data-bd/gold/* -> implicitDeny; s3:PutObject opal-data-bd/platinum/firm/header_metrics.json (the SEV1 must-always-be-right artifact) -> implicitDeny. | CLOSED 20260709T144701Z |
| ddb-scoped | verify | market-updates + opal-news-trending-daily still allowed; a third table (opal-news-articles) implicitDeny | simulate | dynamodb:Scan market-updates -> allowed; dynamodb:Query opal-news-trending-daily -> allowed; dynamodb:Scan opal-news-articles (a third table, previously reachable via DynamoDBFullAccess) -> implicitDeny. The scoping bites. | CLOSED 20260709T144701Z |
| no-collateral | verify | the role retains secretsmanager GetSecretValue on opal/external-apis | simulate | market-update-lambda-role retains secretsmanager:GetSecretValue on opal/external-apis -> allowed (comp-denytest --also-allowed with the explicit action; v3.2 refuses a bare ARN). No behaviour exercise: the feature is DARK -- 0 organic invocations across all three lambdas in 90 days (CTO ruled capability-verify only). Stated, not skipped. | CLOSED 20260709T144701Z |

## Log

- 20260709T144329Z OPENED by 0.5.0_AE_OpalETL with 4 leg(s)
- 20260709T144700Z LEG tf-apply closed: safe-apply: 1 added, 0 changed, 2 destroyed (detach AmazonS3FullAccess + AmazonDynamoDBFullAccess; create aws_iam_role_p
- 20260709T144701Z LEG crossfirm-closed closed: comp-denytest --from-plan --baseline, rc=0 PASS. Change type DERIVED from the plan (attachment DELETE -> allow-removal -
- 20260709T144701Z LEG ddb-scoped closed: dynamodb:Scan market-updates -> allowed; dynamodb:Query opal-news-trending-daily -> allowed; dynamodb:Scan opal-news-art
- 20260709T144701Z LEG no-collateral closed: market-update-lambda-role retains secretsmanager:GetSecretValue on opal/external-apis -> allowed (comp-denytest --also-a
- 20260709T144701Z CLOSED -- all 4 legs proven

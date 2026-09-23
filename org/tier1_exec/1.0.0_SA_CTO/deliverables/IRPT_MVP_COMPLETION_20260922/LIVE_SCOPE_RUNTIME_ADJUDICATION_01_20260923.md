# Live scope runtime adjudication 01

CTO 1.0.0_SA_CTO. Authority: Andrew's direct Proceed on the live scope repair, delegated fork adjudication ecf350639a, CONTRACT.md, and LIVE_SMOKE_SCOPE_20260923.md. Applies only to the directory/scope/browse/selection repair.

## Evidence reviewed

P record LIVE_SCOPE_REPAIR_20260923.md at 475b471784; shared interface candidates backend 124c0694b7 and Portal 504b775e. CTO independently read the protected plan JSON and calculated both binary plan hashes in the isolated irpt-smoke-p-backend-20260923 worktree.

| Plan | SHA256 | Managed actions |
|---|---|---|
| api.tfplan | 156c4b2a46569336bfbab6a5188d090b57824a662bf21c379ea68ef250217652 | Create GET directory/browse and POST selections only |
| directory.tfplan | c058a53307141c93ffbbe1bbd4601ae905bff8693c9f75a14e78e076d1f27e67 | Create directory_selection inline policy; update existing directory Lambda environment only |

Both new routes stay under /api/scoped/investor-reporting, on API 7k3ed8px20, CUSTOM authorizer naqxlm, existing integration g9302sp. No existing route, authorizer or invocation-policy change appears in these plans.

The policy binds irpt-directory-role to DynamoDB GetItem/PutItem on the exact irpt-requests table, with LeadingKeys restricted to 49financial, inflection and cottonwood. The existing SelectionStore uses that tenant partition key and immutable SELECTION# reference sort key. KMS Decrypt/GenerateDataKey are limited to the exact core key, DynamoDB ViaService and irpt-requests encryption context. No Scan, Query, DeleteItem or UpdateItem is added. The Lambda environment delta is only IRPT_REQUESTS_TABLE=irpt-requests. No destruction or schedule/render mutation appears.

The directory plan still names prior object version 4FHLOwjjMQh5LNUWnJRG6La1dJxen2kD and prior code hash cmh6XwybmdXSiWQkQZMeer7wtw0QW/1lXnAIJlPjJKg=. It cannot deliver the repair.

## Decision and next action

The bounded resource/permission scope is accepted for this repair. **Do not apply these old-artifact plans.** This is not a request for another Andrew approval.

P has preparatory GO to assemble M's exact committed producer/header candidate with the shared interface changes, run the existing actual Entry-to-consumer regression and authorization controls, and build the exact single-function irpt-directory-search package through the canonical builder. Check the flat package's actual imports, handlers, schema and pinned dependency bytes. Do not weaken checks or ship a source-only proof as a package proof.

After that package passes, P has GO for the canonical artifact upload limited to s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-directory-search.zip. Record the immutable uploaded object version, package SHA256, source/dependency manifest and prior live version for rollback. This permission is artifact staging only; it does not grant code deployment or invocation, and it does not extend to any other Lambda or artifact key.

Refresh the same bounded Terraform plans against the exact new object version/hash. Freeze all contributing source and IaC changes in named commits. Return the new plan hashes, complete managed action list and relevant acceptance receipts to CTO for the live apply decision. Expected changes are the accepted routes, policy and environment plus this directory Lambda's exact code version/hash; any additional mutation is a new concrete fork for CTO. Use the canonical safe-apply and deployment-recording path after that decision.

The reviewer must independently retest the real bootstrap response through the frontend parser, retain negative authorization controls, and assess cursor/firm/search context isolation. Successful source or package tests do not close Andrew's live failure; the deployed authorized journey must be measured after application. Render/key/vendor holds remain outside this bounded repair.

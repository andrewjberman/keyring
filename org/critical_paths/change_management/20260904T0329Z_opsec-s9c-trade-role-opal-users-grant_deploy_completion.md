# Deploy Completion Record
**Date opened:** 2026-09-04T03:29:04.689870+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260904T035420Z
**Deploy:** TO-OP-S-9C: remove the residual opal-users grant from trade-submission-lambda-role (trade-pipeline/iam.tf:63-64) after a deployed-bytes + config oracle agreed it is unused
**Authored by:** 0.7.0_AE_CloudOps~X
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | BEFORE: five invocable functions invoked and their responses captured; the two mail senders' dormancy recorded as UNCOMPUTABLE-BY-CONSTRUCTION | 5 of 5 invoke results pasted | BEFORE, 5 of 5 invoked, all StatusCode 200 with no FunctionError: trade-authorizer {isAuthorized:false}; trade-auth-handler 400; trade-dashboard-api 200; trade-identifier-cache 404; trade-parquet-batch-export {error: No submission_id provided} (it declined cleanly rather than running an export). The two mail senders were NOT invoked per ruling 20149 and file UNCOMPUTABLE-BY-CONSTRUCTION: no event source mapping, API-Gateway-only resource policy, dormant since 2026-07-14, mail egress bars a driven invoke. | CLOSED 20260904T035418Z |
| L2 | git | SITEZ commit removing trade-pipeline/iam.tf:63-64 | commit hash | commit aabf8ca2e9 on SITEZ: trade-pipeline/iam.tf DynamoDBAccess loses exactly the two opal-users ARNs; the trade-security-identifiers trailing comma corrected; a 30-line evidence comment added in place. terraform validate Success. ASCII-only in the added lines. | CLOSED 20260904T035419Z |
| L3 | activation | terraform apply on the trade-pipeline root | apply output | UNSCOPED apply on the trade-pipeline root (safe: its baseline planned 'No changes. Your infrastructure matches the configuration.' BEFORE the edit, unlike portal-auth). jwt_secret supplied from the LIVE function's own value via TF_VAR, so the clean baseline ALSO proves the correct secret was supplied -- a wrong one would have shown the authorizer's environment changing. Result: 'aws_iam_role_policy.trade_submission_policy: Modifications complete after 0s' / 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.' | CLOSED 20260904T035419Z |
| L4 | verify | AFTER: the same five invoked, same results as the before; APPLIED-plane get-role-policy showing table/opal-users absent from trade-submission-policy | 5 of 5 plus the live policy read | AFTER, 5 of 5 invoked: every response BYTE-IDENTICAL to its before, same StatusCode, same FunctionError, same body. APPLIED-plane get-role-policy on trade-submission-lambda-role/trade-submission-policy: DynamoDBAccess resources 8 -> 6, removing exactly table/opal-users and table/opal-users/index/*, with all six trade-* ARNs preserved and 0 exact table/opal-users grants remaining in the policy. The separate opal-users-v2-access policy was not touched. | CLOSED 20260904T035420Z |
| L5 | verify | UNSCOPED re-plan 0-diff on trade-pipeline; residual set re-enumerated estate-wide; runbook entry written where a person diagnosing a failed trade will meet it | plan output + census + runbook path | UNSCOPED re-plan on trade-pipeline: 'No changes. Your infrastructure matches the configuration.' -- a TRUE 0-diff on this root, so S9C-AC5's limb is satisfiable here unlike S911-AC4 on portal-auth. RESIDUAL RE-ENUMERATED estate-wide via comp-iam refresh-census at 2026-09-04T03:45:22Z: 224 roles / 1191 inline statements, EXACT table/opal-users grants remaining ESTATE-WIDE = 0, with the positive control still returning 4 roles for the v2 ARN. Trajectory across three censuses at this seat: 2 -> 1 -> 0. Residual caveat carried honestly: 174 UNRESOLVED attached-managed statements were not searched. RUNBOOK: infra/aws/terraform/trade-pipeline/README.md now opens with 'IF A TRADE FAILS ON A DYNAMODB ACCESS DENIAL -- CHECK THIS FIRST', naming the rollback as one apply and stating the two-of-seven gap. | CLOSED 20260904T035420Z |

## Log

- 20260904T032904Z OPENED by 0.7.0_AE_CloudOps~X with 5 leg(s)
- 20260904T035418Z LEG L1 closed: BEFORE, 5 of 5 invoked, all StatusCode 200 with no FunctionError: trade-authorizer {isAuthorized:false}; trade-auth-hand
- 20260904T035419Z LEG L2 closed: commit aabf8ca2e9 on SITEZ: trade-pipeline/iam.tf DynamoDBAccess loses exactly the two opal-users ARNs; the trade-securi
- 20260904T035419Z LEG L3 closed: UNSCOPED apply on the trade-pipeline root (safe: its baseline planned 'No changes. Your infrastructure matches the confi
- 20260904T035420Z LEG L4 closed: AFTER, 5 of 5 invoked: every response BYTE-IDENTICAL to its before, same StatusCode, same FunctionError, same body. APPL
- 20260904T035420Z LEG L5 closed: UNSCOPED re-plan on trade-pipeline: 'No changes. Your infrastructure matches the configuration.' -- a TRUE 0-diff on thi
- 20260904T035420Z CLOSED -- all 5 legs proven

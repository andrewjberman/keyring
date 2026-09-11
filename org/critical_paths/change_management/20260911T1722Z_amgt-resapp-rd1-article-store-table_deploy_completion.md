# Deploy Completion Record
**Date opened:** 2026-09-11T17:22:19.004355+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260911T172922Z
**Deploy:** AMGT_RESAPP.TO-AMGT-rd-1 -- THE ARTICLE STORE: new DynamoDB table opal-amgt-articles, genuinely separate from opal-news-articles and opal-data-research, via safe-apply on infra/aws/terraform/amgt-resapp/ (round 5, Andrew-direct 2026-09-11 ~12:1xZ TABLES FIRST)
**Authored by:** 0.9.0_WK_AMGT_RESAPP~1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | infra/aws/terraform/amgt-resapp/ module (main.tf + dynamodb.tf) committed | commit hash | infra/aws/terraform/amgt-resapp/ (main.tf + dynamodb.tf) committed at b679dcb294 (ledger opened first at db28a5d1be, module content lands in this later commit on the same branch, both LOCAL on wk-amgt_resapp-5-1). | CLOSED 20260911T172906Z |
| L2 | activation | safe-apply on infra/aws/terraform/amgt-resapp creates aws_dynamodb_table.amgt_articles (opal-amgt-articles) | apply output showing 1 added, 0 changed, 0 destroyed | safe-apply on infra/aws/terraform/amgt-resapp ran 2026-09-11: comp-tagauthz gate PASSED (0 candidate resources carry an overwritten access-granting tag), tombstone-gate CLEAN, aws_dynamodb_table.amgt_articles created in 24s. Apply complete! Resources: 1 added, 0 changed, 0 destroyed. Outputs: amgt_articles_table_arn=arn:aws:dynamodb:us-east-1:313476888478:table/opal-amgt-articles, amgt_articles_table_name=opal-amgt-articles. | CLOSED 20260911T172906Z |
| L3 | verify | describe-table opal-amgt-articles is ACTIVE with BillingMode PAY_PER_REQUEST on the live plane, plus a negative-control describe-table on a bogus name | describe-table output x2 | AC2: describe-table --table-name opal-amgt-articles --query Table.[TableName,TableStatus,BillingModeSummary.BillingMode] --output text => 'opal-amgt-articles ACTIVE PAY_PER_REQUEST'. AC3 negative control: describe-table --table-name opal-amgt-articles-NOPE-xyz => ResourceNotFoundException, confirming the instrument discriminates present from absent. | CLOSED 20260911T172906Z |

## Log

- 20260911T172219Z OPENED by 0.9.0_WK_AMGT_RESAPP~1 with 3 leg(s)
- 20260911T172619Z LEG L1 closed: infra/aws/terraform/amgt-resapp/ (main.tf + dynamodb.tf) committed at db28a5d1be (with the ledger-open commit; module co
- 20260911T172906Z LEG L1 closed: infra/aws/terraform/amgt-resapp/ (main.tf + dynamodb.tf) committed at b679dcb294 (ledger opened first at db28a5d1be, mod
- 20260911T172906Z LEG L2 closed: safe-apply on infra/aws/terraform/amgt-resapp ran 2026-09-11: comp-tagauthz gate PASSED (0 candidate resources carry an 
- 20260911T172906Z LEG L3 closed: AC2: describe-table --table-name opal-amgt-articles --query Table.[TableName,TableStatus,BillingModeSummary.BillingMode]
- 20260911T172922Z CLOSED -- all 3 legs proven

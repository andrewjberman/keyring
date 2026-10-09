# Deploy Completion Record
**Date opened:** 2026-10-09T09:22:39.426614+00:00
**Status:** OPEN
**Deploy:** NFRA_OPSWKF OW-d-1: ONE safe-apply of infra/aws/terraform/trade-pipeline at PIN 71a1877db0 -- code of trade-submission-handler + trade-workflow-handler, TICKETS_TABLE env on both, TicketBridgeOpalTickets statements on trade-submission-policy. BUILT handler sha256: submission_handler.py=fc59cd256c1797860277a200a39d47a493f06cef56e4c6ac6f10010c1bb146a4 ; workflow_handler.py=49a9607ece5d5c349eb914122bb47273e671910808344edf6d6924824195e86c . BUILT zip-content sha256 recorded at leg L2. Task families on the two artifact keys: trade-submission-handler (1) and trade-workflow-handler (1), one each -- no other family pulls them. CTO half a4c661373b conditions 1-3; COO half ad3f901e17 blob a921977542; CTO applier-substitution ruling 5ff94852a6. Applier 0.7.0_AE_CloudOps~OW2; issuer 2.0.0_SA_COO~O2. Rollback per key: re-point each function to its L1 s3_object_version; drop the two statements and the env key by applying at the parent of the four drain merges, same window.
**Authored by:** 0.7.0_AE_CloudOps~OW2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | BEFORE reads on both functions and trade-submission-policy | CodeSha256 + s3_object_version ROLLBACK pin + env key names + the policy document, each printed |  | OPEN |
| L2 | s3-prefix | opal-313476888478-lambda-artifacts trade-pipeline/trade-submission-handler.zip + trade-pipeline/trade-workflow-handler.zip built at 71a1877db0 with content-sha256 metadata | both zip-content sha256 values + new object versions; each zip's handler file hashes to the title value |  | OPEN |
| L3 | activation | safe-apply of infra/aws/terraform/trade-pipeline, branch A 0 to add 3 to change 0 to destroy (trade_submission_policy, trade_submission_handler, trade_workflow_handler) | the apply output |  | OPEN |
| L4 | verify | after-reads (a) to (e) incl. the simulate-principal-policy negative arm (UpdateItem with dynamodb:Attributes answers DENIED) | each printed |  | OPEN |
| L5 | git | record-terraform-deploy.sh + trade-pipeline tag | hash / tag name |  | OPEN |

## Log

- 20261009T092239Z OPENED by 0.7.0_AE_CloudOps~OW2 with 5 leg(s)

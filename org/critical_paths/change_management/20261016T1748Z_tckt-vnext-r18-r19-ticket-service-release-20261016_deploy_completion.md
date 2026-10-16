# Deploy Completion Record
**Date opened:** 2026-10-16T17:48:22.569495+00:00
**Status:** OPEN
**Deploy:** TCKT_VNEXT TO-R18-REL (AMENDMENT 1) with TO-R19-REL folded: ONE opal-ticket-api release under the combined pair (COO half blob 643ba43746, CTO half blob 2f52cca81d), built_from_sha de2fdb4a4f; +3 routes, +4 env values, ROUTING_MATRIX meeting primary, +1 IAM statement TicketAttachmentsTradeForm, new Lambda code; client-notice map ships empty
**Authored by:** 0.7.0_AE_CloudOps~TV2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| S1 | verify | preconditions 1 to 6 of the pair section 3 measured by the applier (8 blobs, MIG-OK, live baseline, per-tree sweep, 3 bucket policies and CORS, terraform) | all read true and printed |  | OPEN |
| U1 | activation | package zip uploaded to s3://opal-313476888478-lambda-artifacts/ticket-center/opal-ticket-api.zip with content-sha256 metadata, previous S3 VersionId recorded as the rollback | head-object metadata equals the zip sha256 base64 |  | OPEN |
| P1 | verify | terraform plan of infra/aws/terraform/ticket-center saved to a planfile | plan summary equals the pair section 4 exactly |  | OPEN |
| A1 | activation | safe-apply of the saved planfile, function Active and Successful | CodeSha256 equals the package base64 sha256 |  | OPEN |
| V1 | verify | r18_rel_check.py and r19_rel_check.py against the live function, routes and role | both print REL-OK |  | OPEN |

## Log

- 20261016T174822Z OPENED by 0.7.0_AE_CloudOps~TV2 with 5 leg(s)

# Deploy Completion Record
**Date opened:** 2026-10-16T17:48:22.569495+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261016T180143Z
**Deploy:** TCKT_VNEXT TO-R18-REL (AMENDMENT 1) with TO-R19-REL folded: ONE opal-ticket-api release under the combined pair (COO half blob 643ba43746, CTO half blob 2f52cca81d), built_from_sha de2fdb4a4f; +3 routes, +4 env values, ROUTING_MATRIX meeting primary, +1 IAM statement TicketAttachmentsTradeForm, new Lambda code; client-notice map ships empty
**Authored by:** 0.7.0_AE_CloudOps~TV2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| S1 | verify | preconditions 1 to 6 of the pair section 3 measured by the applier (8 blobs, MIG-OK, live baseline, per-tree sweep, 3 bucket policies and CORS, terraform) | all read true and printed | measured at HEAD a3b930322d..0e0f96296c: 8 of 8 blobs equal at worktree, HEAD and de2fdb4a4f; r19_mig_check MIG-OK rows_written=19 markers_live=19 internal_rows_scanned=23; live CodeSha256 Fg8MdfvC..., 10 env keys, Active/Successful; 86-tree sweep, 0 live open ledger names opal-ticket-api (2 hits are stale snapshots of entries CLOSED on trunk); 3 of 3 bucket policies and CORS match; terraform v1.15.8 | CLOSED 20261016T174939Z |
| U1 | activation | package zip uploaded to s3://opal-313476888478-lambda-artifacts/ticket-center/opal-ticket-api.zip with content-sha256 metadata, previous S3 VersionId recorded as the rollback | head-object metadata equals the zip sha256 base64 | package JwdnACONAnxwqzhsVgqgU+nRoLdmS7MyLmzXmZuXsR4= (hex 27076700238d027c70ab386c560aa053e9d1a0b7664bb3322e6cd7999b97b11e, 40287 bytes) uploaded; head-object metadata equals; round-trip read equals; rollback = S3 VersionId BU27czeb9mc1fcnw.i5aSQbXNavPqt2g (holds live CodeSha256 Fg8MdfvC...), copy saved; delta vs live package = lambda_function.py only (blob 501c460978) | CLOSED 20261016T175159Z |
| P1 | verify | terraform plan of infra/aws/terraform/ticket-center saved to a planfile | plan summary equals the pair section 4 exactly | plan saved C:/dev/tv2-rel-r1819-out/tf.plan: Plan: 4 to add, 1 to change, 0 to destroy = routes meeting, attachment_upload, attachment_open; new inline policy opal-ticket-attachments-trade-form-policy (one statement TicketAttachmentsTradeForm, Put+Get on 3 snake_case prefixes, no List/Delete); Lambda in place: +TICKET_ATTACH_BUCKET_TEMPLATE, +TICKET_ATTACH_KEY_TEMPLATE, +ANALYST_INTAKE_ALLOWED_FIRMS, +CLIENT_NOTICE_CONTACT_MAP=jsonencode({}), ROUTING_MATRIX meeting_request.primary only, source_code_hash JwdnACONAnxwqzhsVgqgU+nRoLdmS7MyLmzXmZuXsR4=; equals pair section 4 | CLOSED 20261016T175439Z |
| A1 | activation | safe-apply of the saved planfile, function Active and Successful | CodeSha256 equals the package base64 sha256 | safe-apply of the saved planfile rc=0 at 2026-10-16T17:57:19Z: Apply complete! Resources: 4 added, 1 changed, 0 destroyed; live opal-ticket-api State=Active LastUpdateStatus=Successful CodeSha256=JwdnACONAnxwqzhsVgqgU+nRoLdmS7MyLmzXmZuXsR4= (equals the package); post-apply plan: No changes | CLOSED 20261016T180142Z |
| V1 | verify | r18_rel_check.py and r19_rel_check.py against the live function, routes and role | both print REL-OK | r18_rel_check.py: REL-OK code JwdnACONAnxw, 2 env, 3 routes once each, coordinator routing, TicketAttachmentsTradeForm on 3 prefixes; r19_rel_check.py: REL-OK code_sha256=JwdnACONAnxwqzhsVgqgU+nRoLdmS7MyLmzXmZuXsR4= contact_map_firms=0 intake_firms=3 | CLOSED 20261016T180143Z |

## Log

- 20261016T174822Z OPENED by 0.7.0_AE_CloudOps~TV2 with 5 leg(s)
- 20261016T174939Z LEG S1 closed: measured at HEAD a3b930322d..0e0f96296c: 8 of 8 blobs equal at worktree, HEAD and de2fdb4a4f; r19_mig_check MIG-OK rows_
- 20261016T175159Z LEG U1 closed: package JwdnACONAnxwqzhsVgqgU+nRoLdmS7MyLmzXmZuXsR4= (hex 27076700238d027c70ab386c560aa053e9d1a0b7664bb3322e6cd7999b97b1
- 20261016T175439Z LEG P1 closed: plan saved C:/dev/tv2-rel-r1819-out/tf.plan: Plan: 4 to add, 1 to change, 0 to destroy = routes meeting, attachment_uplo
- 20261016T180142Z LEG A1 closed: safe-apply of the saved planfile rc=0 at 2026-10-16T17:57:19Z: Apply complete! Resources: 4 added, 1 changed, 0 destroye
- 20261016T180143Z LEG V1 closed: r18_rel_check.py: REL-OK code JwdnACONAnxw, 2 env, 3 routes once each, coordinator routing, TicketAttachmentsTradeForm o
- 20261016T180143Z CLOSED -- all 5 legs proven

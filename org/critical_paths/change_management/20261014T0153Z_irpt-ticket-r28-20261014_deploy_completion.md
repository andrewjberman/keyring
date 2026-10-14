# Deploy Completion Record
**Date opened:** 2026-10-14T01:53:26.395201+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261014T020412Z
**Deploy:** IRPT_ANLREQ TO-APPLY-R28a unit L1: opal-ticket-api ticket_center/lambda_function.py (SUBMIT-FORM takes an analysis request, a client-human's own-firm LIST, PACKAGE records report_ref once) to CodeSha256 C/Rt/FnSq..; pair COO blob e9bb20d7fe + CTO half @d3adae2fc8
**Authored by:** 0.7.0_AE_CloudOps~AQ2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | census (no open entry naming opal-ticket-api); R0b live CodeSha256 4sDK8P5m.., key latest _EWULf4C_.., object hash; R0d fresh; T3 before envelope | reads printed | census 34 worktrees, 105 entries, 0 errors: no open entry names opal-ticket-api (6 entries name it or irpt-status; the only non-closed one is this window's own irpt-status-r28-20261014); R0b live CodeSha256 4sDK8P5m.., key ticket-center/opal-ticket-api.zip latest _EWULf4C_.. (21 versions), object hash equal; R0d fresh 2026-10-14T01:42:20Z turned_back 0 (R0D_RECOUNT.txt), L2 irpt-status closed S1-S3 true first; T3 before (retaken 01:5xZ): invoke 200, body 224 bytes, sha256 6ca48466f4d4cc48.. (deterministic) | CLOSED 20261014T015421Z |
| L2 | s3-prefix | detached worktree at 4279513f95 (core.longpaths), guard printed, no diff, TMPDIR new empty folder, BUILD_ONLY digest equals C/Rt/FnSqOj7SnZC1GeoEilj8jbCKdvAUHnxYrnNZNM=, then upload, read back equals the staged zip 0bf46dfc59d2 | digest, VersionId, readback | worktree 4279513f95f67fae07d12889df70dc63954a2d5a detached with core.longpaths, guard 8 mentions at base and in the worktree copy, no diff, TMPDIR a new empty folder outside the repo, BUILD_ONLY digest C/Rt/FnSqOj7SnZC1GeoEilj8jbCKdvAUHnxYrnNZNM= equals EXPECTED and the kept build bytes equal the staged zip (sha256 0bf46dfc59d2..); real run (script verify: write VERIFIED size=34057) landed new VersionId 7vn6xyMOZjpSaKwiT73UaNfXj6mNSljr; read back by VersionId: 34057 bytes, sha256 equals the staged zip 0bf46dfc59d2.. | CLOSED 20261014T015533Z |
| L3 | verify | scoped plan -target=module.opal_ticket_api.aws_lambda_function.this from infra/aws/terraform/ticket-center: 0 add 1 change 0 destroy, the three code attributes only | plan summary and attributes | scoped plan from infra/aws/terraform/ticket-center -target=module.opal_ticket_api.aws_lambda_function.this saved outside the repo: Plan: 0 to add, 1 to change, 0 to destroy; attributes last_modified, s3_object_version (_EWULf4C_.. -> 7vn6xyMOZjpSaKwiT73UaNfXj6mNSljr), source_code_hash (4sDK8P5m.. -> C/Rt/FnSqOj7SnZC1GeoEilj8jbCKdvAUHnxYrnNZNM=) only; environment, role, tags not in the diff; the root pins no version, the data source read the key's new latest. | CLOSED 20261014T015920Z |
| L4 | activation | safe-apply on the saved plan | Apply complete 0/1/0 | pre-apply mail check by get_delivery_state: 0 non-READ; .tools/safe-apply.sh on the saved plan 01:56:23Z-01:58:10Z: Apply complete! 0 added, 1 changed, 0 destroyed (seat-gates APPLY-WHO ADMITTED, CROSSBOX-DEPLOY CLEAR, comp-tagauthz PASSED). No aws lambda update-function-code used. | CLOSED 20261014T015920Z |
| L5 | verify | T1 CodeSha256 C/Rt/FnSq..; T2 one member lambda_function.py sha256 cfa99176..; T3 credential-less refusal envelope equals before | T1-T3 | T1 live CodeSha256 C/Rt/FnSqOj7SnZC1GeoEilj8jbCKdvAUHnxYrnNZNM= (CodeSize 34057, LastModified 2026-10-14T01:58:04Z, Successful) TRUE; T2 live zip ONE member lambda_function.py sha256 cfa99176f89f7cdb32c3e171bdfdf930a605ee51fd3e590b1a55e878073d4d70 TRUE; T3 credential-less refusal envelope after: invoke 200, no FunctionError, body sha256 6ca48466f4d4cc48.. equals T3 before TRUE. | CLOSED 20261014T015921Z |
| L6 | git | artifact_* and last_deployed_* for opal-ticket-api applied to the trunk map in own worktree; commit | commit hash | Map record commit 8fdee64bb2 on scratch branch aq2-r28-map (own full worktree, core.longpaths), merged to box/dell2 as bbbbf7521f via safe-merge. Net diff lambda-source-map.json only: 2 of 235 entries (irpt-status: the status.py row of the repin diff, applied cleanly, plus the record; opal-ticket-api: the record); verified by a parsed old-vs-new comparison. last_deployed_commit is the last commit touching source_dir (irpt-status 9441d74dbb, opal-ticket-api cbdfe204a0); the build bases were a4b7c48fad and 4279513f95 and source_dir is unchanged between them and the map head. | CLOSED 20261014T020412Z |

## Log

- 20261014T015326Z OPENED by 0.7.0_AE_CloudOps~AQ2 with 6 leg(s)
- 20261014T015421Z LEG L1 closed: census 34 worktrees, 105 entries, 0 errors: no open entry names opal-ticket-api (6 entries name it or irpt-status; the o
- 20261014T015533Z LEG L2 closed: worktree 4279513f95f67fae07d12889df70dc63954a2d5a detached with core.longpaths, guard 8 mentions at base and in the work
- 20261014T015920Z LEG L3 closed: scoped plan from infra/aws/terraform/ticket-center -target=module.opal_ticket_api.aws_lambda_function.this saved outside
- 20261014T015920Z LEG L4 closed: pre-apply mail check by get_delivery_state: 0 non-READ; .tools/safe-apply.sh on the saved plan 01:56:23Z-01:58:10Z: Appl
- 20261014T015921Z LEG L5 closed: T1 live CodeSha256 C/Rt/FnSqOj7SnZC1GeoEilj8jbCKdvAUHnxYrnNZNM= (CodeSize 34057, LastModified 2026-10-14T01:58:04Z, Succ
- 20261014T020412Z LEG L6 closed: Map record commit 8fdee64bb2 on scratch branch aq2-r28-map (own full worktree, core.longpaths), merged to box/dell2 as b
- 20261014T020412Z CLOSED -- all 6 legs proven

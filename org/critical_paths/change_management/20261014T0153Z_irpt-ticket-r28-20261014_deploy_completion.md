# Deploy Completion Record
**Date opened:** 2026-10-14T01:53:26.395201+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-APPLY-R28a unit L1: opal-ticket-api ticket_center/lambda_function.py (SUBMIT-FORM takes an analysis request, a client-human's own-firm LIST, PACKAGE records report_ref once) to CodeSha256 C/Rt/FnSq..; pair COO blob e9bb20d7fe + CTO half @d3adae2fc8
**Authored by:** 0.7.0_AE_CloudOps~AQ2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | census (no open entry naming opal-ticket-api); R0b live CodeSha256 4sDK8P5m.., key latest _EWULf4C_.., object hash; R0d fresh; T3 before envelope | reads printed |  | OPEN |
| L2 | s3-prefix | detached worktree at 4279513f95 (core.longpaths), guard printed, no diff, TMPDIR new empty folder, BUILD_ONLY digest equals C/Rt/FnSqOj7SnZC1GeoEilj8jbCKdvAUHnxYrnNZNM=, then upload, read back equals the staged zip 0bf46dfc59d2 | digest, VersionId, readback |  | OPEN |
| L3 | verify | scoped plan -target=module.opal_ticket_api.aws_lambda_function.this from infra/aws/terraform/ticket-center: 0 add 1 change 0 destroy, the three code attributes only | plan summary and attributes |  | OPEN |
| L4 | activation | safe-apply on the saved plan | Apply complete 0/1/0 |  | OPEN |
| L5 | verify | T1 CodeSha256 C/Rt/FnSq..; T2 one member lambda_function.py sha256 cfa99176..; T3 credential-less refusal envelope equals before | T1-T3 |  | OPEN |
| L6 | git | artifact_* and last_deployed_* for opal-ticket-api applied to the trunk map in own worktree; commit | commit hash |  | OPEN |

## Log

- 20261014T015326Z OPENED by 0.7.0_AE_CloudOps~AQ2 with 6 leg(s)

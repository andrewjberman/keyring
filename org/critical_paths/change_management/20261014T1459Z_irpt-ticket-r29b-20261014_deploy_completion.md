# Deploy Completion Record
**Date opened:** 2026-10-14T14:59:25.772270+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-APPLY-R30a: release 29b -- the ticket service owner check: (G) ONE new statement IrptRequestsInputOwnerRead on the ticket role policy opal_ticket_api_ddb (dynamodb:GetItem on irpt-requests for the three firms, four owner attributes; the only widening), THEN (U and C) opal-ticket-api code at expected CodeSha256 Fg8MdfvCvcB8at9K+Bh+IpmuNel8TNWXaKth0W2pv4A= with ONE added environment variable IRPT_REQUESTS_TABLE; signed pair COO blob 355d8e9e8a + CTO half @5389d0d949; rollback CODE first (VersionId 7vn6xyMOZjpSaKwiT73UaNfXj6mNSljr) then GRANT
**Authored by:** 0.7.0_AE_CloudOps~AQ2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| G | activation | scoped plan -target=aws_iam_role_policy.opal_ticket_api_ddb shows ONE in-place update adding only the signed statement; safe-apply; get-role-policy reads the statement exactly once and the three earlier statements unchanged | plan summary and read-back |  | OPEN |
| U | s3-prefix | throwaway worktree detached at ebbadcb0e1, guard printed, BUILD_ONLY digest Fg8MdfvC.., then upload of one new version, read back sha256 160f0c75fbc2.. | digest equal, VersionId, sha256 equal |  | OPEN |
| C | activation | scoped plan -target=module.opal_ticket_api.aws_lambda_function.this 0/1/0 on environment, last_modified, s3_object_version, source_code_hash only; safe-apply | plan and apply lines |  | OPEN |
| V | verify | T1 CodeSha256, T2 one member lambda_function.py d112ba42.., T3 envelope equal, T4 environment plus one variable, T5 simulator a-d with T5c out-of-firm DENIED; A_AFTER_R30a.txt | printed reads |  | OPEN |

## Log

- 20261014T145925Z OPENED by 0.7.0_AE_CloudOps~AQ2 with 4 leg(s)

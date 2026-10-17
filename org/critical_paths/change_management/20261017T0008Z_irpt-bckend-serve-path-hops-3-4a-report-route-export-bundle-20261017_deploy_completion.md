# Deploy Completion Record
**Date opened:** 2026-10-17T00:08:01.730632+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND TO-IB-pr-616 (pair 551 hops 3 and 4): the report route GET /api/scoped/investor-reporting/reporting/client/{client_id}/report on irpt-49f-reporting-read-lambda with a new read bundle, and a new irpt-export-render bundle (code only, the filled-report switch untouched); the IAM statement leg is NOT released in this run. Consumers of irpt-export-render-role (one describe sweep 2026-10-17T00:0xZ): Lambda functions scanned 244, using the role: irpt-export-render only; ECS ACTIVE task families scanned 9, using the role: none.
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | lambda-source-map artifact_sha256 stamps for the two functions plus this ledger sentinel and the release record, committed with explicit paths | commit ids recorded |  | OPEN |
| L2 | s3-prefix | artifact key for irpt-49f-reporting-read-lambda: ONE NEW VERSION (rollback target the prior version whose code hash is WjnDxvu2..) | new VersionId, landed sha256 equals the built zip |  | OPEN |
| L3 | tf-lambda | ONE safe-apply of infra/aws/terraform/investor-reporting/reporting-read: ONE aws_apigatewayv2_route added plus the read Lambda code attributes, no existing route, authorizer or integration changed | plan resource list, replan No changes, live CodeSha256 equals the built zip, route present, summary and series routes unchanged |  | OPEN |
| L4 | s3-prefix | artifact key for irpt-export-render: ONE NEW VERSION (rollback target the prior version whose code hash is 5/9LZBbT..) | new VersionId, landed sha256 equals the built zip |  | OPEN |
| L5 | tf-lambda | ONE safe-apply of infra/aws/terraform/investor-reporting/export, code attributes only, the filled-report switch untouched | plan resource list, replan No changes, live CodeSha256 equals the built zip |  | OPEN |
| L6 | verify | IB247-1 release record written, p247_cells AC1 and AC2 run, proof instance validated | record, criteria output, proof VALID |  | OPEN |
| L7 | verify | hop 4b IAM statement on irpt-export-render-role: NOT RELEASED by the GO (step 6 owed); left OPEN for the issuer | issuer disposition |  | OPEN |

## Log

- 20261017T000801Z OPENED by 0.7.0_AE_CloudOps~IB2 with 7 leg(s)

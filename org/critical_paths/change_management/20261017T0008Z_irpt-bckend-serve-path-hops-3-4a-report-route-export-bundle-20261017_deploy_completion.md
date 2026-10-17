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
| L2 | s3-prefix | artifact key for irpt-49f-reporting-read-lambda: ONE NEW VERSION (rollback target the prior version whose code hash is WjnDxvu2..) | new VersionId, landed sha256 equals the built zip | new VersionId J9krUD0Q (read bundle), prior T..BI8f98 kept as rollback; landed sha256 z634S2QsrfCpY4c3cD2UGwicdmLDo6/Rmng8SrEskCQ= equals the BUILD_ONLY zip; write VERIFIED size 283583 | CLOSED 20261017T002634Z |
| L3 | tf-lambda | ONE safe-apply of infra/aws/terraform/investor-reporting/reporting-read: ONE aws_apigatewayv2_route added plus the read Lambda code attributes, no existing route, authorizer or integration changed | plan resource list, replan No changes, live CodeSha256 equals the built zip, route present, summary and series routes unchanged | plan 1 add 1 change 0 destroy (route irpt_reporting_read_filled plus the read function code attributes); naming gate PASS 6 graded; ONE safe-apply 00:14Z-00:15Z; replan No changes; live CodeSha256 z634S2Qs.. equal; routes 125 to 126; summary, account and series routes unchanged, same authorizer naqxlm | CLOSED 20261017T002634Z |
| L4 | s3-prefix | artifact key for irpt-export-render: ONE NEW VERSION (rollback target the prior version whose code hash is 5/9LZBbT..) | new VersionId, landed sha256 equals the built zip | new VersionId 6kLEkE0n (export bundle), prior eM3_IMEM kept as rollback; landed sha256 5bIgn/MLNgtNtDnRpmE3OejAMw2IpoJBmzzRfHvFLXI= equals the BUILD_ONLY zip; write VERIFIED size 428531 | CLOSED 20261017T002635Z |
| L5 | tf-lambda | ONE safe-apply of infra/aws/terraform/investor-reporting/export, code attributes only, the filled-report switch untouched | plan resource list, replan No changes, live CodeSha256 equals the built zip | plan 0 add 1 change 0 destroy (export function code attributes only); naming gate WARN 28 graded (6 WARN on existing unchanged policy and log-group names, none on this change); ONE safe-apply 00:20Z-00:21Z; replan No changes; live CodeSha256 5bIgn/ML.. equal; environment unchanged (14 variables) | CLOSED 20261017T002635Z |
| L6 | verify | IB247-1 release record written, p247_cells AC1 and AC2 run, proof instance validated | record, criteria output, proof VALID | IB247-1 release record and criteria output written; AC1 PASS, AC2 PASS, AC3 owed (step 6 not released); proof instance VALID | CLOSED 20261017T002635Z |
| L7 | verify | hop 4b IAM statement on irpt-export-render-role: NOT RELEASED by the GO (step 6 owed); left OPEN for the issuer | issuer disposition |  | OPEN |

## Log

- 20261017T000801Z OPENED by 0.7.0_AE_CloudOps~IB2 with 7 leg(s)
- 20261017T002634Z LEG L2 closed: new VersionId J9krUD0Q (read bundle), prior T..BI8f98 kept as rollback; landed sha256 z634S2QsrfCpY4c3cD2UGwicdmLDo6/Rmn
- 20261017T002634Z LEG L3 closed: plan 1 add 1 change 0 destroy (route irpt_reporting_read_filled plus the read function code attributes); naming gate PAS
- 20261017T002635Z LEG L4 closed: new VersionId 6kLEkE0n (export bundle), prior eM3_IMEM kept as rollback; landed sha256 5bIgn/MLNgtNtDnRpmE3OejAMw2IpoJBm
- 20261017T002635Z LEG L5 closed: plan 0 add 1 change 0 destroy (export function code attributes only); naming gate WARN 28 graded (6 WARN on existing unc
- 20261017T002635Z LEG L6 closed: IB247-1 release record and criteria output written; AC1 PASS, AC2 PASS, AC3 owed (step 6 not released); proof instance V

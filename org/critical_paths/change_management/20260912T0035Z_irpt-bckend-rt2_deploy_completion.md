# Deploy Completion Record
**Date opened:** 2026-09-12T00:35:50.892763+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND IB-rt-2: the guarded entry ships WITH its shared modules -- six roots, one at a time, each verified by extract-and-import before the next
**Authored by:** 0.9.0_WK_IRPT_BCKEND~2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | irpt-directory-search (root: infra/aws/terraform/investor-reporting/directory) ROLLBACK: handler -> handler.lambda_handler + restore artifact sha iAWpaqFylkOnmiy2GhcwKYOn+wrBaxSZTV6glMLcCOU= (prior S3 object version) | artifact_sha256 == S3 content-sha256 == live CodeSha256, printed |  | OPEN |
| L1V | verify | irpt-directory-search extract-and-import of the DEPLOYED artifact in the flat /var/task layout, fresh interpreter, repo off sys.path | IMPORT-OK line + negative control FIRES |  | OPEN |
| L2 | activation | irpt-performance-adapter (root: .../performance) ROLLBACK: handler -> handler.lambda_handler + restore artifact sha GvxYnH9LIwWRfdbFdCpWxNZ0RJe9AItzPKX9bfdKgoI= | artifact_sha256 == S3 content-sha256 == live CodeSha256, printed |  | OPEN |
| L2V | verify | irpt-performance-adapter extract-and-import of the DEPLOYED artifact, layer mounted as /opt/python | IMPORT-OK line + negative control FIRES |  | OPEN |
| L3 | activation | irpt-narrative (root: .../narrative) ROLLBACK: handler -> handler.lambda_handler + restore artifact sha nuMb7eMlN8ou41LSSUOsUDR8T5U5uilo7N1XUcwU1IQ= | artifact_sha256 == S3 content-sha256 == live CodeSha256, printed |  | OPEN |
| L3V | verify | irpt-narrative extract-and-import of the DEPLOYED artifact, layer mounted | IMPORT-OK line + negative control FIRES |  | OPEN |
| L4 | activation | irpt-export-render (root: .../export) ROLLBACK: handler -> handler.lambda_handler + restore artifact sha W6fWlpva77QiSAn5DuhMGRpro+Ho485pLVvwcuDySRM= | artifact_sha256 == S3 content-sha256 == live CodeSha256, printed |  | OPEN |
| L4V | verify | irpt-export-render extract-and-import of the DEPLOYED artifact, layer mounted | IMPORT-OK line + negative control FIRES |  | OPEN |
| L5 | activation | irpt-status (root: .../ops) ROLLBACK: handler -> status.lambda_handler + restore artifact sha puH1OBabqlGAI1KcV4P7SfuCq71S0H3ueEyXsUK9PmE= | artifact_sha256 == S3 content-sha256 == live CodeSha256, printed |  | OPEN |
| L5V | verify | irpt-status extract-and-import of the DEPLOYED artifact, no layer | IMPORT-OK line + negative control FIRES |  | OPEN |
| L6 | activation | irpt-ycharts-generate (root: .../ycharts) ROLLBACK: handler -> job.lambda_handler + restore artifact sha hiVUThOsWCSe304UfRug466Oqv6tqvL/8fjKskUUpoo= | artifact_sha256 == S3 content-sha256 == live CodeSha256, printed |  | OPEN |
| L6V | verify | irpt-ycharts-generate extract-and-import of the DEPLOYED artifact, no layer | IMPORT-OK line + negative control FIRES |  | OPEN |

## Log

- 20260912T003550Z OPENED by 0.9.0_WK_IRPT_BCKEND~2 with 12 leg(s)

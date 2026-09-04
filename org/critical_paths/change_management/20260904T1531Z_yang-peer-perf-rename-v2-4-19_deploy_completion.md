# Deploy Completion Record
**Date opened:** 2026-09-04T15:31:03.262063+00:00
**Status:** OPEN
**Deploy:** yang-generate-peer-performance: accept renamed long-term labels (Ultra long term=LTA, Long term=LTC) -- Andrew-direct 2026-09-04, deploy authorized 'according to procedures'; single-function build, targeted apply, replay of Yang's 20260831 upload
**Authored by:** 4.0.0_SA_CRO~C
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit of lambda_function.py under GIT_COMMIT_AUTHOR_OVERRIDE=CLOUD_OPS_OR_ETL + tag yang-v2.4.19 | commit hash + tag name; push state stated (MSTR pushes CLOUD) |  | OPEN |
| L2 | verify | artifact s3://opal-313476888478-lambda-artifacts/yang-pipeline/yang-generate-peer-performance.zip | build-and-upload sha256 line == S3 object metadata content-sha256 |  | OPEN |
| L3 | activation | safe-apply -target=module.generate_peer_performance in infra/aws/terraform/yang-pipeline | apply output + get-function-configuration CodeSha256 == uploaded sha + 0-diff plan |  | OPEN |
| L4 | verify | YangDataPipeline replay of uploads/manifest.json (20260831 peer file) + served json/peers/peer_performance.json | execution SUCCEEDED + JSON generated_at today, data_as_of 2026-08-31, 5 models, 1Y values == raw cells (LTA 16.6039, LTC 15.6316) |  | OPEN |

## Log

- 20260904T153103Z OPENED by 4.0.0_SA_CRO~C with 4 leg(s)

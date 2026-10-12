# Deploy Completion Record
**Date opened:** 2026-10-12T15:36:09.600180+00:00
**Status:** OPEN
**Deploy:** HVST-by-6 roll back opal-research-pull-enqueue to the tier-only code
**Authored by:** 0.7.0_AE_CloudOps~HV1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| BUILD | verify | S3 object version S9217s5ck1gZJvwSC.Ayeg4vFAkV063z (by-2's deploy) read: content-sha256 cWiraC3E..., member sha256 1778584a... equals git show 31590746f1:infra/aws/lambda/research/pull_enqueue/lambda_function.py | version head-object metadata plus its zip member hashed |  | OPEN |
| UPLOAD | activation | s3://opal-313476888478-lambda-artifacts/research/opal-research-pull-enqueue.zip (copy-object of that version over the key, metadata COPY) | new latest VersionId read back, content-sha256 cWiraC3EeuTU9WDIpc5RXzpw6+RT9WxoeqfH/eZiaxo= |  | OPEN |
| APPLY | activation | module.harvest_enqueue in infra/aws/terraform/harvest (targeted, safe-apply) | plan 0 add 1 change 0 destroy; CodeSha256 Q342L4Vn... -> cWiraC3E... |  | OPEN |
| ARMS | verify | opal-research-pull-enqueue deployed function: package source read back, then four no-ticker invokes | source sha256 equals 31590746f1, no userType clause, CodeSha256 equals by-2 deploy; dev_non_internal_tier 403, advisor_non_dev 403, no_context 403, internal_no_ticker 400 |  | OPEN |

## Log

- 20261012T153609Z OPENED by 0.7.0_AE_CloudOps~HV1 with 4 leg(s)

# Deploy Completion Record
**Date opened:** 2026-10-12T15:36:09.600180+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261012T153931Z
**Deploy:** HVST-by-6 roll back opal-research-pull-enqueue to the tier-only code
**Authored by:** 0.7.0_AE_CloudOps~HV1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| BUILD | verify | S3 object version S9217s5ck1gZJvwSC.Ayeg4vFAkV063z (by-2's deploy) read: content-sha256 cWiraC3E..., member sha256 1778584a... equals git show 31590746f1:infra/aws/lambda/research/pull_enqueue/lambda_function.py | version head-object metadata plus its zip member hashed | S3 version S9217s5ck1gZJvwSC.Ayeg4vFAkV063z (the version by2_plan.out line 19 deployed; by5_plan.out line 19 moved off it): head-object ContentLength 2690, content-sha256 cWiraC3EeuTU9WDIpc5RXzpw6+RT9WxoeqfH/eZiaxo=; downloaded by version, member lambda_function.py sha256 1778584aa7309505cc3c2252dd863cd21d405f074be6b0f57d25fa96ed33f484 == git show 31590746f1:infra/aws/lambda/research/pull_enqueue/lambda_function.py (by6_restore.out) | CLOSED 20261012T153705Z |
| UPLOAD | activation | s3://opal-313476888478-lambda-artifacts/research/opal-research-pull-enqueue.zip (copy-object of that version over the key, metadata COPY) | new latest VersionId read back, content-sha256 cWiraC3EeuTU9WDIpc5RXzpw6+RT9WxoeqfH/eZiaxo= | s3api copy-object of that version over s3://opal-313476888478-lambda-artifacts/research/opal-research-pull-enqueue.zip, --metadata-directive COPY: CopySourceVersionId S9217s5ck1gZJvwSC.Ayeg4vFAkV063z, new latest VersionId pHqpZEyjzx1PPaeKAGgJUIB.1hQUU.v2, ContentLength 2690, content-sha256 cWiraC3EeuTU9WDIpc5RXzpw6+RT9WxoeqfH/eZiaxo= read back by head-object of the key (by6_restore.out); no rebuild | CLOSED 20261012T153705Z |
| APPLY | activation | module.harvest_enqueue in infra/aws/terraform/harvest (targeted, safe-apply) | plan 0 add 1 change 0 destroy; CodeSha256 Q342L4Vn... -> cWiraC3E... | plan 0 to add, 1 to change, 0 to destroy (by6_plan.out; s3_object_version kwFo21Dq... -> pHqpZEyjzx1PPaeKAGgJUIB.1hQUU.v2, source_code_hash Q342... -> cWiraC3E...); safe-apply of the saved planfile: Apply complete! Resources: 0 added, 1 changed, 0 destroyed (by6_apply.out); CodeSha256 Q342L4VnpBkMJfFt/ughTj2AhS3gIa1n+pmjVqrslu0= -> cWiraC3EeuTU9WDIpc5RXzpw6+RT9WxoeqfH/eZiaxo=, State Active, LastUpdateStatus Successful, LastModified 2026-10-12T15:38:20Z; comp-iam read identical | CLOSED 20261012T153931Z |
| ARMS | verify | opal-research-pull-enqueue deployed function: package source read back, then four no-ticker invokes | source sha256 equals 31590746f1, no userType clause, CodeSha256 equals by-2 deploy; dev_non_internal_tier 403, advisor_non_dev 403, no_context 403, internal_no_ticker 400 | served package read back (by6_package.out): lambda_function.py sha256 1778584a... == git show 31590746f1 == repo file; USERTYPE CLAUSE PRESENT: no; CODESHA256 EQUALS BY-2 DEPLOY: yes. Four ticker-free invokes: dev_non_internal_tier 403, advisor_non_dev 403, no_context 403, internal_no_ticker 400 (by6_arms.out), each Invoke StatusCode 200, no FunctionError | CLOSED 20261012T153931Z |

## Log

- 20261012T153609Z OPENED by 0.7.0_AE_CloudOps~HV1 with 4 leg(s)
- 20261012T153705Z LEG BUILD closed: S3 version S9217s5ck1gZJvwSC.Ayeg4vFAkV063z (the version by2_plan.out line 19 deployed; by5_plan.out line 19 moved off i
- 20261012T153705Z LEG UPLOAD closed: s3api copy-object of that version over s3://opal-313476888478-lambda-artifacts/research/opal-research-pull-enqueue.zip, 
- 20261012T153931Z LEG APPLY closed: plan 0 to add, 1 to change, 0 to destroy (by6_plan.out; s3_object_version kwFo21Dq... -> pHqpZEyjzx1PPaeKAGgJUIB.1hQUU.v
- 20261012T153931Z LEG ARMS closed: served package read back (by6_package.out): lambda_function.py sha256 1778584a... == git show 31590746f1 == repo file; U
- 20261012T153931Z CLOSED -- all 4 legs proven

# Deploy Completion Record
**Date opened:** 2026-09-14T18:41:56.077829+00:00
**Status:** OPEN
**Deploy:** POSN_ASTTAX B1: deploy yang-generate-positioning + yang-generate-allocation-summary with labelled-zero benchmark rows
**Authored by:** 0.9.0_WK_POSN_ASTTAX~19
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | SITEZ commit of both lambda_function.py | commit hash | commit e89fca26e2 on wk-posn_asttax-5-19 (LOCAL), author 0.9.0_WK_POSN_ASTTAX~19 -- both lambda_function.py, commit-gate clean 2 of 2, msg-verify MATCH len=2335 | CLOSED 20260914T191633Z |
| L2 | s3-prefix | opal-313476888478-lambda-artifacts yang-pipeline/ both zips | build-and-upload sha256 lines | build-and-upload.sh yang-pipeline: yang-generate-positioning.zip sha256 yCdQVNMOoSqvTvWIc+d3RjDqe7yy25dCs/h50Ge9K9s= VersionId LCmMHmpdHvv0P3FB76_anxuuors0CIlr size 33934 (built from source commits e89fca26e2 + dbe34de7b0, under the script's documented BAU_MANIFEST_SKIP=1 with the standalone probe printed rc=1 first); yang-generate-allocation-summary.zip sha256 8ok3+P8z/w2hDmcnMSLPWTmSlp5pXBEqY86hDiPl3A4= VersionId BxWpvrT9AKAV4p6Bl1o9vPYcz98NESHc (first run, unchanged). Both head-object reads carry Metadata content-sha256 matching. | CLOSED 20260914T201543Z |
| L3 | verify | plan scoped to the two modules | plan summary 0 add 2 change 0 destroy | terraform -chdir=infra/aws/terraform/yang-pipeline plan -target=module.generate_positioning -target=module.generate_allocation_summary -out=C:/tmp/wk-posn-5-19/.scratch/b1.tfplan -> Plan: 0 to add, 2 to change, 0 to destroy; exactly 2 resource action lines (module.generate_allocation_summary.aws_lambda_function.this, module.generate_positioning.aws_lambda_function.this), both updated in-place on s3_object_version + source_code_hash. | CLOSED 20260914T201543Z |
| L4 | activation | safe-apply | apply summary | safe-apply.sh -chdir=infra/aws/terraform/yang-pipeline apply C:/tmp/wk-posn-5-19/.scratch/b1.tfplan -> Apply complete! Resources: 0 added, 2 changed, 0 destroyed (20260914T2019Z). HALTGT checkpoint above the apply: identity 0.9.0_WK_POSN_ASTTAX~19 resolved, issuer 2.0.0_SA_COO~Z inbox scanned, comp-tagauthz PASSED, tombstone-gate CLEAN. | CLOSED 20260914T202102Z |
| L5 | verify | 0-diff re-plan | No changes | terraform -chdir=infra/aws/terraform/yang-pipeline plan -target=module.generate_positioning -target=module.generate_allocation_summary -> 'No changes. Your infrastructure matches the configuration.' Plus V1-AC10: live CodeSha256 yang-generate-positioning yCdQVNMOoSqvTvWIc+d3RjDqe7yy25dCs/h50Ge9K9s= and yang-generate-allocation-summary 8ok3+P8z/w2hDmcnMSLPWTmSlp5pXBEqY86hDiPl3A4=, both LastModified 2026-09-14T20:19:41Z. | CLOSED 20260914T202102Z |
| L6 | git | record-terraform-deploy | commit hash | record-terraform-deploy.sh yang-pipeline --plan C:/tmp/wk-posn-5-19/.scratch/b1.tfplan -> commit 56accb9417 'ci: record deploy yang-pipeline @ acf74be3 [skip ci]', author 0.9.0_WK_POSN_ASTTAX~19, VERIFIED BY GIT (git show --stat HEAD lists infra/aws/lambda/ci/lambda-source-map.json ONLY -- the recorder's CHANGELOG helper cannot run on this device, W23-S4, and its success banner is false). Source map at that commit carries last_deployed_commit for exactly the two functions: yang-generate-positioning dbe34de7b0, yang-generate-allocation-summary e89fca26e2 (semantic diff vs the prior commit: 7 leaves, all in the two function rows plus the global _last_deploy_recorded stamp). The CHANGELOG.json entry untagged-acf74be3 was written by hand in the helper's shape (record-terraform-deploy.sh:690-701) and rides the next commit on this branch with the source map's pure-ASCII restoration (detector 0, 0 semantic differences). | CLOSED 20260914T203733Z |
| L7 | verify | served positioning_data.json + allocation_summary.json regenerated | five-class keys + labelled-zero rows, non-class payload byte-identical |  | OPEN |

## Log

- 20260914T184156Z OPENED by 0.9.0_WK_POSN_ASTTAX~19 with 7 leg(s)
- 20260914T191633Z LEG L1 closed: commit e89fca26e2 on wk-posn_asttax-5-19 (LOCAL), author 0.9.0_WK_POSN_ASTTAX~19 -- both lambda_function.py, commit-gate
- 20260914T201543Z LEG L2 closed: build-and-upload.sh yang-pipeline: yang-generate-positioning.zip sha256 yCdQVNMOoSqvTvWIc+d3RjDqe7yy25dCs/h50Ge9K9s= Ver
- 20260914T201543Z LEG L3 closed: terraform -chdir=infra/aws/terraform/yang-pipeline plan -target=module.generate_positioning -target=module.generate_allo
- 20260914T202102Z LEG L4 closed: safe-apply.sh -chdir=infra/aws/terraform/yang-pipeline apply C:/tmp/wk-posn-5-19/.scratch/b1.tfplan -> Apply complete! R
- 20260914T202102Z LEG L5 closed: terraform -chdir=infra/aws/terraform/yang-pipeline plan -target=module.generate_positioning -target=module.generate_allo
- 20260914T203733Z LEG L6 closed: record-terraform-deploy.sh yang-pipeline --plan C:/tmp/wk-posn-5-19/.scratch/b1.tfplan -> commit 56accb9417 'ci: record 

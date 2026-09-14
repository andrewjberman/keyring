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
| L4 | activation | safe-apply | apply summary |  | OPEN |
| L5 | verify | 0-diff re-plan | No changes |  | OPEN |
| L6 | git | record-terraform-deploy | commit hash |  | OPEN |
| L7 | verify | served positioning_data.json + allocation_summary.json regenerated | five-class keys + labelled-zero rows, non-class payload byte-identical |  | OPEN |

## Log

- 20260914T184156Z OPENED by 0.9.0_WK_POSN_ASTTAX~19 with 7 leg(s)
- 20260914T191633Z LEG L1 closed: commit e89fca26e2 on wk-posn_asttax-5-19 (LOCAL), author 0.9.0_WK_POSN_ASTTAX~19 -- both lambda_function.py, commit-gate
- 20260914T201543Z LEG L2 closed: build-and-upload.sh yang-pipeline: yang-generate-positioning.zip sha256 yCdQVNMOoSqvTvWIc+d3RjDqe7yy25dCs/h50Ge9K9s= Ver
- 20260914T201543Z LEG L3 closed: terraform -chdir=infra/aws/terraform/yang-pipeline plan -target=module.generate_positioning -target=module.generate_allo

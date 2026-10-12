# Deploy Completion Record
**Date opened:** 2026-10-12T01:26:59.981076+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261012T020325Z
**Deploy:** NFRA_OPLGTW OG-ap-11: OG-fd-1's per-family DLQ drain on the SCHWAB converter ONLY -- PARTIAL ROLL-OUT. After this deploy only the schwab sweep is per-family; the etf, blackdiamond, orion and eclipse sweeps STILL DRAIN THE WHOLE SHARED QUEUE until their own signed pairs land (CTO half @aafc1640e8). Row Z-S91 stays open until every sweeping family is per-family.
**Authored by:** 0.7.0_AE_CloudOps~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | box/sitez commit moving local.silver_build_commit.schwab in infra/aws/terraform/opal-assets/silver.tf plus the lambda-source-map.json schwab entry | commit hash | commit 2bf592c84189: local.silver_build_commit.schwab b3e481b261 -> a11240c01c in infra/aws/terraform/opal-assets/silver.tf, plus the re-vendored package (exactly one file's content changed, schwab_runtime.py). Pin verified the OG-ap-5 way: git log a11240c01c..HEAD = 0 commits over data/assets/scripts/silver/, data/assets/scripts/lib/ AND the package dir; all 11 BUILD_MANIFEST vendored modules byte-equal to that commit's blobs (11 of 11). The lambda-source-map.json schwab entry (last_deployed_commit a11240c01c5f273651c7af73a5abc173946efd61, last_deployed_at 2026-10-12T01:59:28Z, artifact_sha256 YeLmNn/Tkz+HYVVrCS/PeE+mISSAnH/8ilUUxPEnCmk=) rides the ledger-close commit. | CLOSED 20261012T020108Z |
| L2 | activation | terraform apply via .tools/safe-apply.sh -target the one schwab function: code fields plus the single OPAL_BUILD_COMMIT env value, 1 resource changed and no other row | saved-plan summary plus apply result | SAFE_APPLY_TERRAFORM=<resolved terraform v1.15.8; no .tools/terraform.exe on site Z> .tools/safe-apply.sh -chdir=infra/aws/terraform/opal-assets apply with the SAVED plan, rc=0, 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.' The saved plan read 'Plan: 0 to add, 1 to change, 0 to destroy' on ONE resource, module.silver_converter[schwab].aws_lambda_function.this updated in-place, and its ONLY changed fields were the code fields (s3_object_version, source_code_hash uibjggn93MPPtuIh33Yvehv1xECqrfhPxsWLdmcdYjE= -> YeLmNn/Tkz+HYVVrCS/PeE+mISSAnH/8ilUUxPEnCmk=, last_modified known-after-apply) plus the single environment value OPAL_BUILD_COMMIT b3e481b261 -> a11240c01c, with 28 attributes, 3 env elements and 3 blocks all unchanged -- no other row, so no STOP. Applied 01:51Z, outside [09:15,11:35) [12:00,12:50) [21:15,23:35)Z. No aws lambda update-function-code. | CLOSED 20261012T020109Z |
| L3 | verify | live read-back of opal-assets-silver-schwab: CodeSha256 equals the recorded build and differs from the prior, State Active, LastUpdateStatus Successful | get-function-configuration output | Live get-function-configuration on opal-assets-silver-schwab, rc=0: CodeSha256 YeLmNn/Tkz+HYVVrCS/PeE+mISSAnH/8ilUUxPEnCmk= EQUALS the recorded build and DIFFERS from the prior uibjggn93MPPtuIh33Yvehv1xECqrfhPxsWLdmcdYjE=; State Active; LastUpdateStatus Successful; Environment OPAL_BUILD_COMMIT a11240c01c. Targeted re-plan afterwards: rc=0, 'No changes. Your infrastructure matches the configuration.' | CLOSED 20261012T020109Z |

## Log

- 20261012T012659Z OPENED by 0.7.0_AE_CloudOps~Z with 3 leg(s)
- 20261012T020108Z LEG L1 closed: commit 2bf592c84189: local.silver_build_commit.schwab b3e481b261 -> a11240c01c in infra/aws/terraform/opal-assets/silver
- 20261012T020109Z LEG L2 closed: SAFE_APPLY_TERRAFORM=<resolved terraform v1.15.8; no .tools/terraform.exe on site Z> .tools/safe-apply.sh -chdir=infra/a
- 20261012T020109Z LEG L3 closed: Live get-function-configuration on opal-assets-silver-schwab, rc=0: CodeSha256 YeLmNn/Tkz+HYVVrCS/PeE+mISSAnH/8ilUUxPEnC
- 20261012T020325Z CLOSED -- all 3 legs proven

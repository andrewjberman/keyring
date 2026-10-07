# Deploy Completion Record
**Date opened:** 2026-10-07T13:56:07.983471+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261007T150015Z
**Deploy:** EMERGENCY IB-pr-343 release: irpt-export-render export reads fail closed, pin b921635dad, 9 members, laptop applier by hash
**Authored by:** 0.7.0_AE_CloudOps~I
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | pre-release baseline: live CodeSha256 exDoi/uo5eB9RdFt7/xkZ8OD28Pq6bCejYb7n/zitlg= == S3 objver MteawDsTqojjkhh4e8Xfp_u6T7F8NxX3 == tfstate source_code_hash; ROLLBACK SOURCE = s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-export-render.zip?versionId=MteawDsTqojjkhh4e8Xfp_u6T7F8NxX3 | three-plane read printed | three-plane pre-release baseline all equal: live CodeSha256 exDoi/uo5eB9RdFt7/xkZ8OD28Pq6bCejYb7n/zitlg=, S3 objver MteawDsTqojjkhh4e8Xfp_u6T7F8NxX3 (content-sha256 identical), tfstate source_code_hash identical at serial 36. ROLLBACK SOURCE re-read AFTER the release and still retrievable (402664 B). | CLOSED 20261007T150014Z |
| L2 | s3-prefix | build-and-upload investor-reporting irpt-export-render -> opal-313476888478-lambda-artifacts/investor-reporting/irpt-export-render.zip | built sha256 + new versionId | build-and-upload.sh investor-reporting irpt-export-render: SHA256 aRCgH9B0pglos8cPiybPhmJShzjUts/Tr5R9R/AZYJw=, s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-export-render.zip write VERIFIED (size=405052, sha256 metadata match), new objver ZBwAzArTtDSpCIYL8CwhqqmIooS4mVPx. BAU_PARITY_SKIP=1 taken and justified: row IRPT_BCKEND-S381. | CLOSED 20261007T150014Z |
| L3 | activation | safe-apply of infra/aws/terraform/investor-reporting/export from saved planfile; only code + object version, 0 to destroy | apply output + 0-diff re-plan | safe-apply from the saved planfile ib-pr-349.tfplan: 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.' Only module.irpt_export_render.aws_lambda_function.this in place (s3_object_version, source_code_hash, last_modified). comp-tagauthz PASSED, tombstone-gate CLEAN. Re-plan: 'No changes. Your infrastructure matches the configuration.' | CLOSED 20261007T150015Z |
| L4 | verify | after-reads IB68-1: deployed sha==built, replan 0, live entry.py fc241d806ecc, existing export refused, new/performance/analysis READY, admitted-read log line, outside path refused, Opal caller served | IB68-1_release_after_reads.json + IB68-1-AC1 PASS | IB68-1_release_after_reads.json written. PASSED: deployed sha == built; replan 0; live entry.py sha256 fc241d806ecc (fix in the RUNNING bytes, live zip 63 members); existing un-back-filled export REFUSED on the deployed bytes; outside principal REFUSED (opaque id, no token minted); Opal caller ADMITTED as positive control, with a second control landing on the distinct counts branch; 49 offline tests pass incl. the fix's own two. NOT EXERCISED, blocked by this order's 'No write to the auth plane' bound and the HUMAN-GATED test-principal record: the LIVE new/performance/analysis submit arm. IB68-1-AC1 reads FAIL on new_export_ready=None. Escalated as a BLOCKING row, NOT rolled back (rollback would reopen the hole for 7 principals and nothing failed). | CLOSED 20261007T150015Z |

## Log

- 20261007T135607Z OPENED by 0.7.0_AE_CloudOps~I with 4 leg(s)
- 20261007T150014Z LEG L1 closed: three-plane pre-release baseline all equal: live CodeSha256 exDoi/uo5eB9RdFt7/xkZ8OD28Pq6bCejYb7n/zitlg=, S3 objver Mtea
- 20261007T150014Z LEG L2 closed: build-and-upload.sh investor-reporting irpt-export-render: SHA256 aRCgH9B0pglos8cPiybPhmJShzjUts/Tr5R9R/AZYJw=, s3://opa
- 20261007T150015Z LEG L3 closed: safe-apply from the saved planfile ib-pr-349.tfplan: 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.' Only 
- 20261007T150015Z LEG L4 closed: IB68-1_release_after_reads.json written. PASSED: deployed sha == built; replan 0; live entry.py sha256 fc241d806ecc (fix
- 20261007T150015Z CLOSED -- all 4 legs proven

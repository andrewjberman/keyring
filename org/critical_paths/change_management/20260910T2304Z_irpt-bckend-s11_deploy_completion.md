# Deploy Completion Record
**Date opened:** 2026-09-10T23:04:21.488222+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260910T231202Z
**Deploy:** IRPT_BCKEND IB-s-11 -- performance adapter Lambda + role, first apply of the investor-reporting/performance root
**Authored by:** 0.9.0_WK_IRPT_BCKEND~4
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | worktree branch wk-irpt_bckend-1-4 commit of the adapter package, terraform root and source-map entry | commit hash | commit de87f0976d on wk-irpt_bckend-1-4 (LOCAL, never pushed by a worker): 21 files, adapter package + terraform root + source-map entry + this ledger sentinel | CLOSED 20260910T231147Z |
| L2 | s3-prefix | s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-performance-adapter.zip | head-object ContentLength + content-sha256 equal to the built zip | build-and-upload.sh investor-reporting: SHA256 Tl+NwcWAWl46YWeCrHShPpjoX5RgGUWm2UVQPLRJdFM= size 60793; write VERIFIED by head-object (ContentLength=60793, content-sha256 metadata match) at s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-performance-adapter.zip | CLOSED 20260910T231147Z |
| L3 | activation | terraform apply of infra/aws/terraform/investor-reporting/performance (aws_iam_role.performance_adapter + module.irpt_performance_adapter) | safe-apply output | safe-apply.sh -chdir=infra/aws/terraform/investor-reporting/performance apply: 'Apply complete! Resources: 4 added, 0 changed, 0 destroyed.' rc=0; outputs function_name=irpt-performance-adapter role_arn=arn:aws:iam::313476888478:role/irpt-performance-adapter-role | CLOSED 20260910T231148Z |
| L4 | verify | get-function-configuration CodeSha256 equals the built zip sha256, and a 0-diff plan on the root | verbatim CLI output | get-function-configuration CodeSha256=Tl+NwcWAWl46YWeCrHShPpjoX5RgGUWm2UVQPLRJdFM= equals the built zip sha256 byte for byte; State=Active LastUpdateStatus=Successful Runtime=python3.12 Handler=handler.lambda_handler. 0-diff plan: 'No changes. Your infrastructure matches the configuration.' rc=0 | CLOSED 20260910T231148Z |

## Log

- 20260910T230421Z OPENED by 0.9.0_WK_IRPT_BCKEND~4 with 4 leg(s)
- 20260910T231147Z LEG L1 closed: commit de87f0976d on wk-irpt_bckend-1-4 (LOCAL, never pushed by a worker): 21 files, adapter package + terraform root + 
- 20260910T231147Z LEG L2 closed: build-and-upload.sh investor-reporting: SHA256 Tl+NwcWAWl46YWeCrHShPpjoX5RgGUWm2UVQPLRJdFM= size 60793; write VERIFIED b
- 20260910T231148Z LEG L3 closed: safe-apply.sh -chdir=infra/aws/terraform/investor-reporting/performance apply: 'Apply complete! Resources: 4 added, 0 ch
- 20260910T231148Z LEG L4 closed: get-function-configuration CodeSha256=Tl+NwcWAWl46YWeCrHShPpjoX5RgGUWm2UVQPLRJdFM= equals the built zip sha256 byte for 
- 20260910T231202Z CLOSED -- all 4 legs proven

# Deploy Completion Record
**Date opened:** 2026-09-10T20:56:03.261151+00:00
**Status:** OPEN
**Deploy:** NFRA_CLDGRPH Act A: rebuild incremental_updater.zip from the post-fix lambda_function.py (five-class key collision), upload to the lambda-artifacts bucket, safe-apply so source_code_hash moves. Andrew-direct 2026-09-10 ~20:2xZ 'Rec (a) for call 1' authorizes the deploy and the SNS/SMS pages it causes. Handoff: org/tier1_exec/2.0.0_SA_COO~A/deliverables/HANDOFF_CLDGRPH_DEPLOY_20260910T2040Z.md
**Authored by:** 0.8.0_AE_CloudComp
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD: rebuilt incremental_updater.zip carrying the post-fix lambda_function.py (worktree 41520 B) + _provenance.py pinned at DEPLOYED bytes (27072 B) so the only delta is the collision fix | commit hash + rebuilt zip sha256 + member readback |  | OPEN |
| L2 | s3-prefix | s3://opal-313476888478-lambda-artifacts/globgrph/incremental_updater.zip | head-object sha256/ETag matching the rebuilt local zip |  | OPEN |
| L3 | activation | safe-apply infra/aws/terraform/globgrph so aws_lambda_function.globgrph_incremental_updater source_code_hash moves off 2e4693a3 | get-function-configuration CodeSha256 == base64(sha256(rebuilt zip)) + targeted 0-diff replan |  | OPEN |
| L4 | verify | Live acceptance: i1_settle.py DESTROYED_BEFORE stops growing once an S3 write flows through the updater; all FIVE class pairs move, not just bucket/policy | settle harness reading pre vs post |  | OPEN |

## Log

- 20260910T205603Z OPENED by 0.8.0_AE_CloudComp with 4 leg(s)

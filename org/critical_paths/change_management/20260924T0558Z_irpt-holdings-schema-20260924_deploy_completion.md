# Deploy Completion Record
**Date opened:** 2026-09-24T05:58:47.599865+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260924T060625Z
**Deploy:** irpt-holdings repackage carrying the HoldingsSnapshot schema copy at b3e3bcb044 (display + CUSTODY_UNITS), code unchanged (CTO 100172 step 3, 100241, batch 27 item 1)
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A1 | activation | module.irpt_holdings.aws_lambda_function.this | safe-apply of saved plan 0/1/0, readback CodeSha256 kZygK57y | safe-apply (tools terraform 1.9.8, backend holdings root) of the saved plan 0/1/0: source_code_hash C69BErK1 -> kZygK57y, s3_object_version J2UrwQmt -> ZbLWvaO1; Apply complete 0/1/0 rc=0 at 06:00:15Z, log ae7c63bdfd1d6dea; readback CodeSha256 kZygK57yXxZBaC3t5Wr+y04tDKx6tDJdjCwPm87kdYE= LastModified 06:00:10Z Active Successful | CLOSED 20260924T060115Z |
| V1 | verify | holdings re-plan + readback | 0-diff re-plan, LastUpdateStatus Successful | re-plan -detailed-exitcode rc=0 No changes at 06:00Z; LastUpdateStatus Successful | CLOSED 20260924T060115Z |
| R1 | git | deploy recorder | record-terraform-deploy commit | record-terraform-deploy.sh investor-reporting --function irpt-holdings: commit 59e8231599 on irpt-p-publish-20260923 (map aab522ed92) | CLOSED 20260924T060625Z |

## Log

- 20260924T055847Z OPENED by 2.0.0_SA_COO~P with 3 leg(s)
- 20260924T060115Z LEG A1 closed: safe-apply (tools terraform 1.9.8, backend holdings root) of the saved plan 0/1/0: source_code_hash C69BErK1 -> kZygK57y
- 20260924T060115Z LEG V1 closed: re-plan -detailed-exitcode rc=0 No changes at 06:00Z; LastUpdateStatus Successful
- 20260924T060625Z LEG R1 closed: record-terraform-deploy.sh investor-reporting --function irpt-holdings: commit 59e8231599 on irpt-p-publish-20260923 (ma
- 20260924T060625Z CLOSED -- all 3 legs proven

# Deploy Completion Record
**Date opened:** 2026-09-27T19:26:01.463311+00:00
**Status:** OPEN
**Deploy:** irpt-export-render 3EST/hewG -> async submit + withheld rejected prose (backend ac4eb443b3 + f3995c0d31; publish 1b8ead8cbf + e8b32494c9; CTO 102026, 102031 (a)); code + IAM + event-invoke-config; halves pending
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | verify | artifact build + upload | census vs live 3EST/hewG: only entry.py, submit_async.py (new), narrative_build.py, evidence.py, prose.py differ; content-sha256 recorded; not served until D1 | publish e8b32494c9 (cherry-picks 1b8ead8cbf = backend ac4eb443b3, e8b32494c9 = f3995c0d31; bytes EQ on all 6 touched files); source map: submit_async.py added, narrative handler/evidence/prose re-pinned 83e8b9577a -> 1b8ead8cbf; build-and-upload rc 0; s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-export-render.zip VersionId kN5tj1K0eQqWVfp4KGeXEBoAQY9a8wcu, content-sha256 8nkjGpT0gWLD.. (= body sha). Census vs live 3EST/hewG: 58 -> 59 members; differ entry.py, evidence.py, narrative_build.py, prose.py; added submit_async.py; removed none. Flat extract-and-import: entry, submit_async, narrative_build, prose import; lambda_handler callable; marked event routed. NOT served until D1. | CLOSED 20260927T193059Z |
| D1 | activation | export root safe-apply | both halves at HEAD naming the packet blob; plan = code + policy (pending.json, self-invoke) + event_invoke_config (retries 0, age 60) + env IRPT_EXPORT_FUNCTION_TIMEOUT_S, nothing destroyed; safe-apply; readback CodeSha + get-function-event-invoke-config MaximumRetryAttempts 0; replan 0 | Both halves at HEAD naming packet blob dd91065c (@e8c43a3fff): CTO @625b7dc1de 102037 (conditions: safe-apply only with live readback; arm 1 timed from the HAR; one hop by invocation count) and CRO @db22c99603 102039 (follow-on ask: bind run to accept's principal + permitted-set digest). Live before: CodeSha 3EST/hewG. safe-apply of async.tfplan (export root, backend worktree f3995c0d31): Apply complete, 1 added, 2 changed, 0 destroyed. AWS readback: CodeSha256 8nkjGpT0gWLDo0gRDixsVO549rk7y3mleMWZlHMqiOw= Active/Successful, Timeout 120, env IRPT_EXPORT_FUNCTION_TIMEOUT_S=120; get-function-event-invoke-config MaximumRetryAttempts 0, MaximumEventAgeInSeconds 60; submit policy Sid InvokeThisFunctionAsyncForTheExportBuild Resource = the function's own ARN only. Re-plan: No changes (detailed-exitcode 0). No-write live probe: a marked event with no BUILDING pointer (exr_0x24, 49financial) -> AsyncSubmitRefused 'no BUILDING pointer for this revision' (req f35f32e5, 1.37 s); pointer census for that revision 0 under 49financial/cottonwood/inflection (positive control: 49F generations page 2 keys). | CLOSED 20260927T194514Z |
| A1 | verify | next K8 window | ONE POST answers QUEUED with an exr_ revision in under 29 s; the pointer goes BUILDING -> SUBMITTED; the receipt goes NOT_READY -> READY %PDF (or a named FAILED); the grant and receipt name the caller (reopen-rule arm 4); nothing outside the export's write set |  | OPEN |

## Log

- 20260927T192601Z OPENED by 2.0.0_SA_COO~P with 3 leg(s)
- 20260927T193059Z LEG U1 closed: publish e8b32494c9 (cherry-picks 1b8ead8cbf = backend ac4eb443b3, e8b32494c9 = f3995c0d31; bytes EQ on all 6 touched fil
- 20260927T194514Z LEG D1 closed: Both halves at HEAD naming packet blob dd91065c (@e8c43a3fff): CTO @625b7dc1de 102037 (conditions: safe-apply only with 

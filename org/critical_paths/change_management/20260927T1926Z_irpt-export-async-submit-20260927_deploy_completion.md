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
| U1 | verify | artifact build + upload | census vs live 3EST/hewG: only entry.py, submit_async.py (new), narrative_build.py, evidence.py, prose.py differ; content-sha256 recorded; not served until D1 |  | OPEN |
| D1 | activation | export root safe-apply | both halves at HEAD naming the packet blob; plan = code + policy (pending.json, self-invoke) + event_invoke_config (retries 0, age 60) + env IRPT_EXPORT_FUNCTION_TIMEOUT_S, nothing destroyed; safe-apply; readback CodeSha + get-function-event-invoke-config MaximumRetryAttempts 0; replan 0 |  | OPEN |
| A1 | verify | next K8 window | ONE POST answers QUEUED with an exr_ revision in under 29 s; the pointer goes BUILDING -> SUBMITTED; the receipt goes NOT_READY -> READY %PDF (or a named FAILED); the grant and receipt name the caller (reopen-rule arm 4); nothing outside the export's write set |  | OPEN |

## Log

- 20260927T192601Z OPENED by 2.0.0_SA_COO~P with 3 leg(s)

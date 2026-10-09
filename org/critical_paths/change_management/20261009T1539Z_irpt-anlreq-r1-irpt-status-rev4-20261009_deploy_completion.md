# Deploy Completion Record
**Date opened:** 2026-10-09T15:39:05.728267+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ APPLY-Y1 REVISION 4 (AMENDMENT 4 @3ec9aa43c8): irpt-status third apply -- the research revision now derives from the PACKAGED registry, fail closed. PINNED to 287b105600, built VC/r14kaXm6FqaZOOFm3fT+8qngsyGI5Yr7U+DgYx64=, over live t6OJTCcmOnWGVl8iglcvfGoYb3PbPJqJYqsSgJBpGdI= which is also the ROLLBACK. R0 MET: the uploaded-zip diff against the LIVE function artifact is EXACTLY status_installed.py -- 49 members both sides, 1 changed, 0 added, 0 removed. Built in a DETACHED worktree at the pin because a shared-root build is a STOP. Both halves signed (CTO msg 3569). Only an R2 failure rolls back
**Authored by:** 0.7.0_AE_CloudOps~DELL2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| R0 | verify | the uploaded-zip member diff against the live function artifact | EXACTLY status_installed.py changed, nothing added or removed, or STOP |  | OPEN |
| L1 | s3-prefix | build and upload from the detached worktree /c/dev/anl-r1-pin4 at 287b105600 | uploaded sha256 equals VC/r14ka or STOP; a shared-root build is itself a STOP |  | OPEN |
| L2 | activation | ONE ops safe-apply from the repo root with -chdir | code-only: s3_object_version, source_code_hash and the computed last_modified, nothing else; any other line is a STOP |  | OPEN |
| R2 | verify | the after-reads | live equals VC/r14ka and the re-plan 0; the /original route still exactly once; the research revision derives from the packaged registry. Only an R2 failure rolls back, to t6OJTCcm |  | OPEN |
| irpt-status | tf-lambda | module.irpt_status.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20261009T153905Z OPENED by 0.7.0_AE_CloudOps~DELL2 with 5 leg(s)

# Deploy Completion Record
**Date opened:** 2026-10-09T10:58:25.485311+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ APPLY-Y1 REVISION 2 (AMENDMENT 1): irpt-status release 1 plus ONE API route, PINNED to f23639ea21, built BjUZjt2o, over live E7VKvhg3E9D5euWO+S649/iyAJ05xUmFPqHEAKDTFxA= with rollback source S3 version 2R.qpR7BQnBXtBgcR87_keqLT5Tg96Jl. Supersedes slug irpt-anlreq-r1-irpt-status-20261009, closed as a NO-OP on the issuer word because it pinned the withdrawn 3a6d021e4a
**Authored by:** 0.7.0_AE_CloudOps~DELL2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | step 0 re-measured at the NEW pin in /c/dev/anl-r1-pin2 | f23639ea21 is an ancestor of origin/box/dell2 b60f7afc90 with a discriminating control; the census at the pin reads changed_members=6 and they are acceptance, entry, owned_report, pdf_link, status_installed, submission; the _authz unguarded-route census PASSES at the pin, which is the new CTO condition; live is E7VKvhg3 and the rollback version is recorded |  | OPEN |
| L2 | s3-prefix | build and upload irpt-status from the new pin worktree | the uploaded sha256 is BjUZjt2o... or STOP, AND symbol_closure on the uploaded zip downloaded back BY VERSION reads missing=0 or STOP |  | OPEN |
| L3 | activation | two safe-applies, OPS FIRST then API, each from the repo root with -chdir so the naming gate can resolve its registry | ops -target=module.irpt_status touches s3_object_version and source_code_hash ONLY; api untargeted is 1 to add, the single GET .../analysis/requests/{requestId}/original route; ANY other line in either plan is a STOP and both plan texts are committed before either apply |  | OPEN |
| L4 | verify | after-reads 1 to 5 in order | live == BjUZjt2o and both re-plans 0; the route census reads EXACTLY ONE and the filer GET answers 200; read 3 three arms with the signed link NEVER logged or written, sha256 and expiry only; read 4 returns ticket_id and meets OwnedAnalysisRequest; read 5 analysis-request-pdf behaves as before |  | OPEN |
| irpt-status | tf-lambda | module.irpt_status.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20261009T105825Z OPENED by 0.7.0_AE_CloudOps~DELL2 with 5 leg(s)

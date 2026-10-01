# Deploy Completion Record
**Date opened:** 2026-10-01T07:54:38.353256+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261001T083308Z
**Deploy:** irpt-performance-adapter: the reopen path serves OPAL_HOLDINGS reports only and a firm not yet on the holdings basis answers OBJECT_NOT_COVERED -- retained.py and entry.py at b15f0ed7df (CTO batch 66 items 2-3, batch 67 item 4, decision 103586; row S247)
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| F1 | tf-lambda | module.irpt_performance_adapter.aws_lambda_function.this | TF apply 0 add 1 change 0 destroy + 0-diff replan + deployed CodeSha256 equals the uploaded sha + member census: retained.py and entry.py the only changed members | safe-apply targeted module.irpt_performance_adapter.aws_lambda_function.this 08:18:08Z-08:20:36Z: Plan 0 add 1 change 0 destroy, Apply complete 0 added 1 changed 0 destroyed; live CodeSha256 cdbFZDJAW5g4ym+3wl9kyD9WVfYmm6AVZBuwd0c6eJI= (LastModified 2026-10-01T08:20:26Z, equals the uploaded sha; bytes downloaded from Lambda hash to it, 70 members); full-root re-plan No changes at 08:22Z; census 70 to 70 members, changed entry.py and retained.py only; one-use vendor plan read DISARMED at 08:16Z (IRPT_PERFORMANCE_APPROVED_PLAN absent from the live configuration, 7 variables listed) -- CTO half item 7 | CLOSED 20261001T082326Z |
| V1 | verify | the three retained vendor-figure reports and the public code | after the apply none of the three reopens (service-level run on the deployed bytes) and the adapter log's next vendor-path refusal reads OBJECT_NOT_COVERED; row S247 disarmed by its owner's read | packet 3 conditions 2-5, read after the 08:20:26Z apply: (2) invokes BEFORE and AFTER equal -- empty headers CONTRACT_VERSION, trusted headers for cottonwood with a non-existent user naming performance-report NOT_AUTHORIZED with a business date; no FunctionError, no errorMessage. (3) CodeSha256 cdbFZDJA... equals AFTER; full-root re-plan No changes 08:22Z. (4) retained_reopen_before_after.py with AFTER = the bytes downloaded from Lambda (sha equal to CodeSha256): reopen Inflection RPT (ORION) REOPENED -> ProviderPathNotComposed OBJECT_NOT_COVERED; reopen Cottonwood RPT x2 (BLACK_DIAMOND) REOPENED -> RetainedVendorFigureRefused OBJECT_NOT_COVERED; fresh Inflection and fresh Cottonwood DEPENDENCY_UNAVAILABLE -> OBJECT_NOT_COVERED; control 49 Financial OPAL_HOLDINGS reopens on both: six rows equal to the packet's section 3. (5) log 08:20:26Z..08:30:26Z, window complete: 9 events, 2 invocations (this seat's two probes), 0 TypeError/ImportModuleError/Traceback/timeout lines, 0 UNEXPECTED. NOT OBSERVED: a real vendor-path request in the window (0 arrived), so the log's own OBJECT_NOT_COVERED line is not yet seen; the code is measured by (4). (6) row S247 disarmed by row IRPT_BCKEND-S249, same turn. | CLOSED 20261001T083241Z |

## Log

- 20261001T075438Z OPENED by 2.0.0_SA_COO~P with 2 leg(s)
- 20261001T082326Z LEG F1 closed: safe-apply targeted module.irpt_performance_adapter.aws_lambda_function.this 08:18:08Z-08:20:36Z: Plan 0 add 1 change 0 
- 20261001T083241Z LEG V1 closed: packet 3 conditions 2-5, read after the 08:20:26Z apply: (2) invokes BEFORE and AFTER equal -- empty headers CONTRACT_VE
- 20261001T083308Z CLOSED -- all 2 legs proven

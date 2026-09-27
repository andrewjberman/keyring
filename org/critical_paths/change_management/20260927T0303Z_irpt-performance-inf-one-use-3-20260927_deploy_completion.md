# Deploy Completion Record
**Date opened:** 2026-09-27T03:03:50.460097+00:00
**Status:** OPEN
**Deploy:** INF Orion one-use arm, plan f0de098f (acc_5510a.., YTD to 09-25, expires 12:00Z) + K11 (window-7 amendment 3: ~D's ONE INF Performance read); packet 3a68bb2d (CTO @1b9060e893, CRO pending); Andrew call 2 @6039c2f680
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A1 | activation | performance root env arm | re-plan 0/1/0 with exactly IRPT_PERFORMANCE_APPROVED_PLAN + IRPT_PERF_VENDOR_EGRESS_AUTHORIZED; safe-apply; readback env digest == f0de098f | re-plan (CTO item 1) with -var-file INF_ONE_USE_PLAN_3: 0/1/0 on module.irpt_performance_adapter.aws_lambda_function.this, exactly IRPT_PERFORMANCE_APPROVED_PLAN + IRPT_PERF_VENDOR_EGRESS_AUTHORIZED change (the inner plan fields approval_ref/expires_at/requests_sha256 differ; requests_sha256 reflects the S143 household-scoped body); safe-apply 03:07:25Z; readback: CodeSha256 Ll6t4VPa unchanged, Active/Successful, env plan sha256 f0de098fddaca8b4.. and egress digest equal | CLOSED 20260927T030825Z |
| K11 | verify | ONE INF read by ~D in window 7 | PERFORMANCE_USE#f0de098f claimed once; the outcome recorded (READY/PARTIAL or a named refusal); one Orion request |  | OPEN |
| Z1 | verify | disarm | the plan spent at the claim, or the spent plan re-applied the same tick if K11 did not run before window 7's delete (CTO item 2) |  | OPEN |

## Log

- 20260927T030350Z OPENED by 2.0.0_SA_COO~P with 3 leg(s)
- 20260927T030825Z LEG A1 closed: re-plan (CTO item 1) with -var-file INF_ONE_USE_PLAN_3: 0/1/0 on module.irpt_performance_adapter.aws_lambda_function.thi

# Deploy Completion Record
**Date opened:** 2026-09-24T13:08:07.940122+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260924T131320Z
**Deploy:** irpt-performance-adapter: ONE server-approved one-use plan armed for acc_d486fc9455d6b2aa18e13af1, window 2026-01-01..2026-09-24, expires 2026-09-25T00:00Z, plan sha256 106eaa0e9ed064d3.. (Andrew-direct 12:5xZ card 2 @9b36d8a481; env-only change, no code)
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| irpt-performance-adapter | tf-lambda | module.irpt_performance_adapter.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served | TF apply 1 added (aws_iam_role_policy.performance_approved_session[0]: GetSecretValue on the exact blackdiamond/cot/session ARN, the root's own conditional per-use grant) 1 changed (environment: IRPT_PERFORMANCE_APPROVED_PLAN 557 bytes + IRPT_PERF_VENDOR_EGRESS_AUTHORIZED) 0 destroyed at 13:12:22Z; CodeSha256 07lSH03z.. UNCHANGED (env-only); readback: token == sha256(plan string) == 106eaa0e9ed064d301659ca9ad5d148a4a7f2b1dbbf7b2c95cd8320cc46b1a65, State Active Successful; replan with the var-file rc=0 No changes; irpt-requests PERFORMANCE_ rows for cottonwood = 0 (the use is ARMED, not spent); verify-on-served = the signed-in request itself (Andrew's browser act), not a seat's | CLOSED 20260924T131320Z |

## Log

- 20260924T130807Z OPENED by 2.0.0_SA_COO~P with 1 leg(s)
- 20260924T131320Z LEG irpt-performance-adapter closed: TF apply 1 added (aws_iam_role_policy.performance_approved_session[0]: GetSecretValue on the exact blackdiamond/cot/sess
- 20260924T131320Z CLOSED -- all 1 legs proven

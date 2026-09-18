# Deploy Completion Record
**Date opened:** 2026-09-18T12:42:29.561419+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260918T134439Z
**Deploy:** IRPT_BCKEND IB-rtd-8: the firm check restored on holdings/enforce.py -- row W1-S16 fix (re-staged enforce.py member only)
**Authored by:** 0.9.0_WK_IRPT_BCKEND~1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L2 | verify | live route proof (M of M guarded routes, other-firm advisor refused / own-firm admitted) | the round-1 harness (real signed post-authorizer requests) output | battery_ib_rtd_8.py arm (d), this run: enumerated the 12 published routes / 7 functions from routes.json fresh; read infra/aws/terraform/investor-reporting/api/integrations.tf fresh -- HTTP API v2, payload_format_version=2.0, NO request template, so a real Lambda event never carries object_kind unless AWS itself sets one, and it does not; source-censused every real enforcer.guard(...) call site across every non-test .py file under infra/aws/lambda/investor-reporting/ this run -- 0 of M name object_kind=advisor. M of M = 0 of 7, VACUOUS (measured, never assumed a pass). The mechanism itself (own-firm admitted / other-firm refused) is proven directly against the real Enforcer by arm (b)'s six-swap census, 12 of 12, with the mutant proven discriminating (4 of 4 flips). Full battery output: org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/IB-rtd-8_R48-AC1_battery_output.txt | CLOSED 20260918T134439Z |
| irpt-holdings | tf-lambda | module.irpt_holdings.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served | TF apply module.irpt_holdings.aws_lambda_function.this: 0 added, 1 changed, 0 destroyed. served CodeSha256 UllXBBuvOzO+7SMQIUUsld1IlClqkk2cOAy8UxHx8h0= == build-and-upload.sh's artifact_sha256 (S3 write VERIFIED size=71682) == lambda-source-map.json's recorded value. Re-plan post-apply: No changes (0-diff). Downloaded the LIVE served zip fresh post-apply and hashed its enforce.py member: 69808e78... (the fixed content, byte-identical to the committed holdings/enforce.py); served.py/loaders.py/snapshot.py/errors.py/resolve.py/handler.py/entry.py/stage.py/contract confirmed byte-identical to the pre-apply served artifact (only enforce.py moved). | CLOSED 20260918T132757Z |

## Log

- 20260918T124229Z OPENED by 0.9.0_WK_IRPT_BCKEND~1 with 2 leg(s)
- 20260918T132757Z LEG irpt-holdings closed: TF apply module.irpt_holdings.aws_lambda_function.this: 0 added, 1 changed, 0 destroyed. served CodeSha256 UllXBBuvOzO+7
- 20260918T134439Z LEG L2 closed: battery_ib_rtd_8.py arm (d), this run: enumerated the 12 published routes / 7 functions from routes.json fresh; read inf
- 20260918T134439Z CLOSED -- all 2 legs proven

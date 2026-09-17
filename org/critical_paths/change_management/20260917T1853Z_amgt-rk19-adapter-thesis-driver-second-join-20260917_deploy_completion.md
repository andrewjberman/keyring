# Deploy Completion Record
**Date opened:** 2026-09-17T18:53:57.120621+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260917T193447Z
**Deploy:** AMGT-rk-19 adapter: thesis_driver_chart second join (excerpt-verified filing points), co-signed rk-19 pair (CTO e3fc4495cf, COO dispatch msg)
**Authored by:** 0.9.0_WK_AMGT_RESAPP~27
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| opal-amgt-scoped-api | tf-lambda | module.scoped_amgt_api.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served | TF apply -target=module.scoped_amgt_api.aws_lambda_function.this: Resources: 0 added, 1 changed, 0 destroyed (source_code_hash zHmPoWu9jZqUUqlK9zwvfoZk/aFg+rOoOLbuJwHGRHA= -> zuWM8IZziIL4u/0n2sXeeF+ZdW7hTKoHrtDHTHOqrzQ=, matches build-and-upload-scoped-amgt.sh local sha256 exactly, s3 VersionId DZ_9GSNC5kbJoKC6AvdG17ZQo85JB7z6). Post-apply targeted 0-diff replan: 'No changes. Your infrastructure matches the configuration.'. Live get-function-configuration post-act: CodeSha256 zuWM8IZziIL4u/0n2sXeeF+ZdW7hTKoHrtDHTHOqrzQ=, LastModified 2026-09-17T19:23:42.000+0000, CodeSize 782668, Layers/MemorySize(512)/Timeout(29)/Environment unchanged. Verify-on-served: 13 of 13 GET routes invoked live (rawPath+x-firm-id shape) pre and post act, LOST=[] GAINED=[]; order's own AC1 planted-negative PASSES (points_count 0); AC2 does NOT pass -- served drafting/v1/BA_US_Equity.json cache still carries the pre-verification points shape with no span/passage_id fields (STOP 6 of the CTO half names this cache rebuild explicitly out of scope), so the second branch's verified-points bar is not cleared by design; this is a genuine upstream-data gap, not a deploy defect. | CLOSED 20260917T193424Z |

## Log

- 20260917T185357Z OPENED by 0.9.0_WK_AMGT_RESAPP~27 with 1 leg(s)
- 20260917T193424Z LEG opal-amgt-scoped-api closed: TF apply -target=module.scoped_amgt_api.aws_lambda_function.this: Resources: 0 added, 1 changed, 0 destroyed (source_cod
- 20260917T193447Z CLOSED -- all 1 legs proven

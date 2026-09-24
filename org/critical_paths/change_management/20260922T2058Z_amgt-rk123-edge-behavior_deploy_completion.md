# Deploy Completion Record
**Date opened:** 2026-09-22T20:58:25.742643+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260922T212649Z
**Deploy:** AMGT_RESAPP AMGT-rk-123: append ONE ordered_cache_behavior for /api/scoped/amgt/* on CloudFront EVTSA9VEHNZVH (origin APIGateway-portal, caching disabled, viewer-request auth-validator-edge) -- unblanks the Security Analysis page
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| tf-commit | git | infra/aws/terraform/portal-auth/cloudfront-distribution.tf | true | 8c038da7e7 (0.7.0_AE_CloudOps) cloudfront-distribution terraform +36/-0, merged to SITEZ at 6c41b5d70e; lane check PASSED at commit (owned-paths gate PERMIT this serial, REFUSE 2.0.0_SA_COO~Z as negative control); apply: Apply complete! Resources: 0 added, 2 changed, 0 destroyed | CLOSED 20260922T212649Z |
| edge-verify | verify | EVTSA9VEHNZVH cache behaviors 28->29 + served amgt paths JSON not HTML | true | LIVE post-act: CacheBehaviors.Quantity 28->29; exactly 1 amgt pattern /api/scoped/amgt/* at index 28 = LAST; TargetOriginId APIGateway-portal; CachePolicyId 4135ea2d (CachingDisabled); viewer-request arn:aws:lambda:us-east-1:313476888478:function:auth-validator-edge:20; 8 of 8 fields identical to template /api/scoped/investor-reporting/*; 28 pre-existing patterns intact, order preserved, 0 duplicates; served read1+read2 both: amgt lists/freshness/BA_US_Equity/992_HK_Equity all 401 application/json 51b (was 200 text/html 1000b), controls advisor-intelligence/ping + general/health unmoved at 401 application/json 51b; WAF 0 of 18 rule-fields moved vs plan removed-side; Status=Deployed 2026-09-22T21:04:05Z | CLOSED 20260922T212649Z |

## Log

- 20260922T205825Z OPENED by 0.7.0_AE_CloudOps with 2 leg(s)
- 20260922T212649Z LEG tf-commit closed: 8c038da7e7 (0.7.0_AE_CloudOps) cloudfront-distribution terraform +36/-0, merged to SITEZ at 6c41b5d70e; lane check PASSE
- 20260922T212649Z LEG edge-verify closed: LIVE post-act: CacheBehaviors.Quantity 28->29; exactly 1 amgt pattern /api/scoped/amgt/* at index 28 = LAST; TargetOrigi
- 20260922T212649Z CLOSED -- all 2 legs proven

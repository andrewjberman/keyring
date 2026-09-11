# Deploy Completion Record
**Date opened:** 2026-09-11T09:40:43.825196+00:00
**Status:** OPEN
**Deploy:** IRPT IB-s-15 RESUME: the ONE ordered_cache_behavior for /api/scoped/investor-reporting/* on EVTSA9VEHNZVH, under the bound WIDENED FOR THIS APPLY ONLY by CTO ruling 95933 to 'ONE change plus the classified WAF read-normalisation no-op'. Supersedes 20260911T0855Z_irpt-bckend-s15-cloudfront, which closed on NON-EXECUTION when this cell's own STOP fired.
**Authored by:** 0.9.0_WK_IRPT_BCKEND~2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | the behavior block already committed at d0a61c6acb plus this entry's OPEN sentinel | commit hash on wk-irpt_bckend-1-2 (LOCAL); the behavior itself is UNCHANGED from the refused attempt -- nothing was re-edited, only re-planned |  | OPEN |
| L2 | verify | the pre-apply plan CONFORMS to the widened bound: 0 to add, 2 to change, 0 to destroy naming ONLY aws_cloudfront_distribution.portal (exactly one + ordered_cache_behavior, appended last) and aws_wafv2_web_acl.opal_cloudfront_protection (six rules; three managed-rule blocks differing ONLY in version) | plan saved verbatim; ANY other line is Branch B of the COO half -- STOP, no safe-apply, re-arm the row |  | OPEN |
| L3 | activation | safe-apply on infra/aws/terraform/portal-auth adding the one behavior | apply output; this is a SERVED SURFACE fronting 28 behaviors, so 0 destroyed is not the test -- the before/after reads below are |  | OPEN |
| L4 | verify | get-distribution-config behaviors 27 -> 28 with the one new path and the prior 27 unchanged IN ORDER | pattern-list diff = exactly one appended line |  | OPEN |
| L5 | verify | get-web-acl Rules JSON identical before and after, LockToken excepted | diff empty -- the classified no-op changed no rule |  | OPEN |
| L6 | verify | the unauthenticated difference control: the request that returned the SPA (HTTP 200 text/html, 1068 bytes) before the behavior now returns 401 or 403 | both statuses recorded |  | OPEN |

## Log

- 20260911T094043Z OPENED by 0.9.0_WK_IRPT_BCKEND~2 with 6 leg(s)

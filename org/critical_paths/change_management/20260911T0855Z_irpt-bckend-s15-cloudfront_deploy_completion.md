# Deploy Completion Record
**Date opened:** 2026-09-11T08:55:05.333823+00:00
**Status:** OPEN
**Deploy:** IRPT IB-s-15: ONE ordered_cache_behavior for /api/scoped/investor-reporting/* on distribution EVTSA9VEHNZVH (portal-auth root, a SERVED SURFACE fronting 28 behaviors)
**Authored by:** 0.9.0_WK_IRPT_BCKEND~2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | wk-irpt_bckend-1-2 source commit for the one behavior in infra/aws/terraform/portal-auth/cloudfront-distribution.tf | commit hash on the worker branch (LOCAL, never pushed) |  | OPEN |
| L2 | verify | the PRE-APPLY plan on portal-auth shows EXACTLY ONE change and nothing else | plan output printed verbatim; any other line is a STOP and a BLOCKING row, never an apply |  | OPEN |
| L3 | activation | terraform apply of infra/aws/terraform/portal-auth adding the behavior | safe-apply output; the distribution is the whole portal so 0 destroyed is not enough -- the behavior COUNT and the 27 existing path patterns are diffed before and after |  | OPEN |
| L4 | verify | get-distribution-config BEFORE vs AFTER: the 27 existing behaviors read delta 0 and the new one is present with its edge association | the two configs diffed, counts printed |  | OPEN |
| L5 | verify | the unauthenticated difference control: the same request that returned the SPA before the behavior now returns 401 or 403 | both statuses and first bytes recorded |  | OPEN |

## Log

- 20260911T085505Z OPENED by 0.9.0_WK_IRPT_BCKEND~2 with 5 leg(s)

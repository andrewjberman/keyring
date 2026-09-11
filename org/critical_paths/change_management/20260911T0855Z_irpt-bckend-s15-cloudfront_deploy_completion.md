# Deploy Completion Record
**Date opened:** 2026-09-11T08:55:05.333823+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260911T090030Z
**Deploy:** IRPT IB-s-15: ONE ordered_cache_behavior for /api/scoped/investor-reporting/* on distribution EVTSA9VEHNZVH (portal-auth root, a SERVED SURFACE fronting 28 behaviors)
**Authored by:** 0.9.0_WK_IRPT_BCKEND~2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | wk-irpt_bckend-1-2 source commit for the one behavior in infra/aws/terraform/portal-auth/cloudfront-distribution.tf | commit hash on the worker branch (LOCAL, never pushed) | d0a61c6acb on wk-irpt_bckend-1-2 (LOCAL; a worker never pushes). The one behavior, 38 insertions and 0 deletions in cloudfront-distribution.tf, appended at the END of the ordered list so no existing block shifts. The OPEN sentinel rode this commit, before the plan. | CLOSED 20260911T085600Z |
| L2 | verify | the PRE-APPLY plan on portal-auth shows EXACTLY ONE change and nothing else | plan output printed verbatim; any other line is a STOP and a BLOCKING row, never an apply | REFUSED BY ITS OWN GATE. The pre-apply plan on portal-auth reads 'Plan: 0 to add, 3 to change, 0 to destroy' and names THREE resources: aws_cloudfront_distribution.portal (MINE -- exactly one added ordered_cache_behavior for /api/scoped/investor-reporting/*, 1 of 1 block, no existing behavior touched), aws_cloudfront_function.spa_fallback (NOT mine -- a CRLF checkout artifact, MEASURED: spa-fallback-function.js is 26 CRLF / 0 bare LF on disk while the HEAD blob is 0 CRLF / 26 LF), and aws_wafv2_web_acl.opal_cloudfront_protection (NOT mine -- 3 managed-rule blocks removed and 3 re-added: common-rule-set p4, ip-reputation p3, known-bad-inputs p5). The face: a plan that touches any other behavior, origin or setting is a BLOCKING row, NEVER an apply. This leg is closed as the EVIDENCE it was opened to capture; L3/L4/L5 are not reachable and this entry is HELD. | CLOSED 20260911T085836Z |
| L3 | activation | terraform apply of infra/aws/terraform/portal-auth adding the behavior | safe-apply output; the distribution is the whole portal so 0 destroyed is not enough -- the behavior COUNT and the 27 existing path patterns are diffed before and after | NOT APPLIED -- THE ACT WAS REFUSED BEFORE IT STARTED, and the world is verified unchanged. safe-apply was never invoked on portal-auth. get-distribution-config on EVTSA9VEHNZVH taken AFTER the plan is BYTE-IDENTICAL to the one taken before any act: 27 ordered behaviors then and now, identical pattern list, investor-reporting present = False, full DistributionConfig json-identical. Nothing is half-landed because nothing landed. This leg closes as NON-EXECUTION so the entry can be HELD on its named gate rather than blaring as a stranded deploy. | CLOSED 20260911T085942Z |
| L4 | verify | get-distribution-config BEFORE vs AFTER: the 27 existing behaviors read delta 0 and the new one is present with its edge association | the two configs diffed, counts printed | NOT REACHED -- the before/after diff was taken anyway and is the non-execution evidence above: 27 behaviors before, 27 after, full config identical. The AFTER-APPLY form of this leg is the one the gate blocks. | CLOSED 20260911T085943Z |
| L5 | verify | the unauthenticated difference control: the same request that returned the SPA before the behavior now returns 401 or 403 | both statuses and first bytes recorded | NOT REACHED. The PRE half is recorded and stands as the difference control's first half: an unauthenticated GET to https://opalinvest.dev/api/scoped/investor-reporting/status returns HTTP 200 text/html, 1068 bytes of index.html (the SPA), because no behavior claims the prefix. The POST half needs the behavior this gate blocks. | CLOSED 20260911T085943Z |

## Log

- 20260911T085505Z OPENED by 0.9.0_WK_IRPT_BCKEND~2 with 5 leg(s)
- 20260911T085600Z LEG L1 closed: d0a61c6acb on wk-irpt_bckend-1-2 (LOCAL; a worker never pushes). The one behavior, 38 insertions and 0 deletions in clou
- 20260911T085836Z LEG L2 closed: REFUSED BY ITS OWN GATE. The pre-apply plan on portal-auth reads 'Plan: 0 to add, 3 to change, 0 to destroy' and names T
- 20260911T085942Z LEG L3 closed: NOT APPLIED -- THE ACT WAS REFUSED BEFORE IT STARTED, and the world is verified unchanged. safe-apply was never invoked 
- 20260911T085943Z LEG L4 closed: NOT REACHED -- the before/after diff was taken anyway and is the non-execution evidence above: 27 behaviors before, 27 a
- 20260911T085943Z LEG L5 closed: NOT REACHED. The PRE half is recorded and stands as the difference control's first half: an unauthenticated GET to https
- 20260911T090030Z CLOSED -- all 5 legs proven

---

## READ THIS BEFORE THE STATUS LINE: **NOTHING WAS APPLIED**

This entry reads CLOSED because the ledger's state machine has one word for "no leg is
outstanding", and every leg here closed on **non-execution**. The act this window was opened for
-- adding one `ordered_cache_behavior` to distribution `EVTSA9VEHNZVH` -- **did not happen and
must not be inferred from the word CLOSED.**

**WHY IT DID NOT HAPPEN.** The pre-apply plan on `portal-auth` read:

```
Plan: 0 to add, 3 to change, 0 to destroy.
  # aws_cloudfront_distribution.portal will be updated in-place
  # aws_cloudfront_function.spa_fallback will be updated in-place
  # aws_wafv2_web_acl.opal_cloudfront_protection will be updated in-place
```

The task order's bound is exact: *"The CloudFront plan shows exactly ONE change or you STOP ...
a plan that touches any other behavior, origin or setting is a BLOCKING row, never an apply."*
Two of those three resources are not this cell's and not this project's.

**WHAT EACH OF THE THREE IS, MEASURED:**

| resource | whose | what the diff is |
|---|---|---|
| `aws_cloudfront_distribution.portal` | THIS cell's | exactly ONE added `ordered_cache_behavior` (`/api/scoped/investor-reporting/*`), 1 of 1 block, no existing behavior touched -- the clean half |
| `aws_cloudfront_function.spa_fallback` | NOT this cell's | a CRLF checkout artifact. MEASURED: `spa-fallback-function.js` is 26 CRLF / 0 bare LF on disk while the HEAD blob is 0 CRLF / 26 LF. Every diff line shows identical text on both sides |
| `aws_wafv2_web_acl.opal_cloudfront_protection` | NOT this cell's | REAL churn: 3 managed-rule blocks removed and 3 re-added -- `common-rule-set` p4, `ip-reputation` p3, `known-bad-inputs` p5. This is the WAF protecting the whole portal |

**THE WORLD IS VERIFIED UNCHANGED.** `get-distribution-config` on `EVTSA9VEHNZVH` taken after the
plan is byte-identical to the one taken before any act: 27 ordered behaviors then and now,
identical pattern list, `investor-reporting` present = False, full `DistributionConfig` JSON
identical. Nothing is half-landed because nothing landed.

**WHAT UN-BLOCKS IT:** the `portal-auth` root plans clean, or its two drifting resources are
dispositioned by that root's owner (lane `CLOUD_OPS_OR_ETL`, any AE agent -- this project does
not own that root). The behavior is COMMITTED and UNAPPLIED, so re-running the plan after the
drift clears is the whole remaining act.

**THE API HALF OF THIS CELL IS SEPARATE AND IS LIVE.** Ledger `irpt-bckend-s15` closed with 4 of
4 legs proven: 11 routes on `7k3ed8px20` under the existing `naqxlm` authorizer, applied 23
added / 0 changed / 0 destroyed. Only the CloudFront behavior is gated.

Surface: surprise row `IRPT_BCKEND-W2-S12`.

# Deploy Completion Record
**Date opened:** 2026-09-24T11:04:45.584826+00:00
**Status:** OPEN
**Deploy:** api root: the two owned-history GET routes DECLARED against irpt-status in routes.json (analysis-request-history, analysis-request-read) -- CTO batch 28 (iii) / 100535
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| history-routes | activation | aws_apigatewayv2_route.irpt[GET /api/scoped/investor-reporting/analysis/requests] + aws_apigatewayv2_route.irpt[GET /api/scoped/investor-reporting/analysis/requests/{requestId}] on API 7k3ed8px20 -> integrations/8ogp332 (irpt-status) | TF apply (2 add, 0 change, 0 destroy) + 0-diff replan + get-routes readback naming both keys with the irpt-status integration + verify-on-served (a signed-out HTTPS GET through the portal API answers the authorizer's refusal, not a 404) |  | OPEN |

## Log

- 20260924T110445Z OPENED by 2.0.0_SA_COO~P with 1 leg(s)

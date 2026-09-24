# Deploy Completion Record
**Date opened:** 2026-09-24T11:04:45.584826+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260924T110908Z
**Deploy:** api root: the two owned-history GET routes DECLARED against irpt-status in routes.json (analysis-request-history, analysis-request-read) -- CTO batch 28 (iii) / 100535
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| history-routes | activation | aws_apigatewayv2_route.irpt[GET /api/scoped/investor-reporting/analysis/requests] + aws_apigatewayv2_route.irpt[GET /api/scoped/investor-reporting/analysis/requests/{requestId}] on API 7k3ed8px20 -> integrations/8ogp332 (irpt-status) | TF apply (2 add, 0 change, 0 destroy) + 0-diff replan + get-routes readback naming both keys with the irpt-status integration + verify-on-served (a signed-out HTTPS GET through the portal API answers the authorizer's refusal, not a 404) | TF apply 2 added 0 changed 0 destroyed (safe-apply, history-routes.tfplan, 11:0xZ; route ids 7yo12g5, jjidb6b); replan rc=0 No changes; get-routes readback: both keys -> integrations/8ogp332 (irpt-status), authorizer naqxlm CUSTOM; 16 investor-reporting routes on the API == 16 DECLARED in routes.json @89204d4b2e; verify-on-served signed-out: 401 on both new routes AND 401 on the unrouted control (a catch-all authorizer answers before route matching), so the signed-out arm does not discriminate -- the served discriminator is get-routes (APPLIED) plus the function-level invoke of the history route (EXERCISED, request 328500fb-0bda-47f6-9330-b5a6f75873d7); the HTTP path is exercisable only signed-in | CLOSED 20260924T110908Z |

## Log

- 20260924T110445Z OPENED by 2.0.0_SA_COO~P with 1 leg(s)
- 20260924T110908Z LEG history-routes closed: TF apply 2 added 0 changed 0 destroyed (safe-apply, history-routes.tfplan, 11:0xZ; route ids 7yo12g5, jjidb6b); replan r
- 20260924T110908Z CLOSED -- all 1 legs proven

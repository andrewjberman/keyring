# Session Log — TRSB_PATHFIX.TO-1: API GW Route Fix

**Agent:** 0.7.0_AE_CloudOps
**Date:** 2026-04-27
**TO:** TRSB_PATHFIX.TO-1.ae-api-gateway-route-fix
**Status:** COMPLETE
**Tag:** trade-pipeline-v1.6.0

---

## Root Cause

Portal hard-codes `/api/general/trades/*` (16 call sites in
`portal/src/api/endpoints/trade-submission.ts:192-414`). CloudFront behavior 1 correctly routes
`/api/general/trades/*` → API GW `7k3ed8px20`, but API GW had NO routes under that prefix.
All trade routes existed only at `/api/public/trades/*`. Every trade UI call returned 404 →
CF's 404→/index.html mask → client received HTML → JSON.parse crash ("Unexpected token '<'").

## Pre-Change Checks (Phase 1)

### Authorizer `naqxlm`
```
AuthorizerType: REQUEST
AuthorizerUri: .../opal-portal-authorizer/invocations
EnableSimpleResponses: true
IdentitySource: $request.header.Authorization
```
Status: HEALTHY

### comp-routes behaviors (baseline)
23 behaviors. Behavior 1: `/api/general/trades/*` → APIGateway-portal [AUTH] (auth-validator-edge).
CF configuration already correct — no CF changes needed or made.

### Integration IDs confirmed
| ID | Lambda |
|----|--------|
| ehdnz7g | trade-submission-handler |
| xkuchu9 | trade-workflow-handler |
| x3p4wrq | trade-dashboard-api |
| mvrx5ci | trade-identifier-cache |

---

## Routes Added (12 total — CLI invocations for TF replay)

API GW: `7k3ed8px20` | AuthorizationType: CUSTOM | AuthorizerId: `naqxlm`

```bash
APID="7k3ed8px20"; AUTH="naqxlm"

# ehdnz7g (trade-submission-handler)
aws apigatewayv2 create-route --api-id $APID --route-key "POST /api/general/trades/submit" \
  --authorization-type CUSTOM --authorizer-id $AUTH --target "integrations/ehdnz7g"
# RouteId: ytf5cd0

# xkuchu9 (trade-workflow-handler)
aws apigatewayv2 create-route --api-id $APID --route-key "POST /api/general/trades/workflow" \
  --authorization-type CUSTOM --authorizer-id $AUTH --target "integrations/xkuchu9"
# RouteId: f0d9leb

# x3p4wrq (trade-dashboard-api) — 8 routes
aws apigatewayv2 create-route --api-id $APID --route-key "GET /api/general/trades/users" \
  --authorization-type CUSTOM --authorizer-id $AUTH --target "integrations/x3p4wrq"
# RouteId: xiw6crn

aws apigatewayv2 create-route --api-id $APID --route-key "GET /api/general/trades/submissions" \
  --authorization-type CUSTOM --authorizer-id $AUTH --target "integrations/x3p4wrq"
# RouteId: r0vwww5

aws apigatewayv2 create-route --api-id $APID --route-key "GET /api/general/trades/submissions/pending" \
  --authorization-type CUSTOM --authorizer-id $AUTH --target "integrations/x3p4wrq"
# RouteId: 50b4js7

aws apigatewayv2 create-route --api-id $APID --route-key "GET /api/general/trades/submissions/by-status" \
  --authorization-type CUSTOM --authorizer-id $AUTH --target "integrations/x3p4wrq"
# RouteId: t7i7388

aws apigatewayv2 create-route --api-id $APID --route-key "GET /api/general/trades/submissions/by-initiator" \
  --authorization-type CUSTOM --authorizer-id $AUTH --target "integrations/x3p4wrq"
# RouteId: ulnga2l

aws apigatewayv2 create-route --api-id $APID --route-key "GET /api/general/trades/submissions/{id}" \
  --authorization-type CUSTOM --authorizer-id $AUTH --target "integrations/x3p4wrq"
# RouteId: budv9hg

aws apigatewayv2 create-route --api-id $APID --route-key "GET /api/general/trades/submissions/{id}/excel" \
  --authorization-type CUSTOM --authorizer-id $AUTH --target "integrations/x3p4wrq"
# RouteId: lz32ps5

aws apigatewayv2 create-route --api-id $APID --route-key "GET /api/general/trades/submissions/by-approver" \
  --authorization-type CUSTOM --authorizer-id $AUTH --target "integrations/x3p4wrq"
# RouteId: jwuain6
# NOTE: NEW route — no /api/public equivalent; dashboard_api.py:56-57 already handles this path

# mvrx5ci (trade-identifier-cache) — 2 routes
aws apigatewayv2 create-route --api-id $APID --route-key "GET /api/general/trades/identifiers/search" \
  --authorization-type CUSTOM --authorizer-id $AUTH --target "integrations/mvrx5ci"
# RouteId: hpchjdr

aws apigatewayv2 create-route --api-id $APID --route-key "POST /api/general/trades/identifiers/batch" \
  --authorization-type CUSTOM --authorizer-id $AUTH --target "integrations/mvrx5ci"
# RouteId: h9m83ig
```

---

## Lambda Permissions Added (4 functions)

SourceArn: `arn:aws:execute-api:us-east-1:313476888478:7k3ed8px20/*/*/api/general/trades/*`
StatementId: `GeneralTradesPermission`

```bash
SRC="arn:aws:execute-api:us-east-1:313476888478:7k3ed8px20/*/*/api/general/trades/*"
for FUNC in trade-submission-handler trade-workflow-handler trade-dashboard-api trade-identifier-cache; do
  aws lambda add-permission --function-name $FUNC --statement-id GeneralTradesPermission \
    --action lambda:InvokeFunction --principal apigateway.amazonaws.com --source-arn "$SRC"
done
```

All 4: PASS

---

## Phase 2 Verification (Before Tag)

| Check | Result |
|-------|--------|
| `get-routes \| grep general/trades`: 12 routes | PASS — all CUSTOM+naqxlm |
| Lambda get-policy trade-submission-handler | PASS — GeneralTradesPermission, correct SourceArn |
| Lambda get-policy trade-workflow-handler | PASS |
| Lambda get-policy trade-dashboard-api | PASS |
| Lambda get-policy trade-identifier-cache | PASS |
| API GW stage auto-deploy | PASS — Successfully deployed (ripuky) |

---

## Acceptance Criteria

| # | Criterion | Status |
|---|-----------|--------|
| 1 | 12 routes under /api/general/trades/*, all CUSTOM+naqxlm | PASS |
| 2 | Browser: Submit tab POST returns 200 + JSON | AWAITING browser test (infra live) |
| 3 | All 4 tabs load without JSON.parse errors | AWAITING browser test |
| 4 | Lambda permissions cover /api/general/trades/* | PASS |
| 5 | comp-routes behaviors identical before/after | PASS — 23 behaviors, unchanged |
| 6 | Session log with CLI invocations for TF replay | PASS (this log) |
| 7 | trade-pipeline-v1.6.0 tag | APPLIED |

**Note on AC2/AC3:** Browser smoke test requires authenticated portal session. All infrastructure is
verified correct (routes, permissions, integrations, authorizer). Browser confirmation needed from Andrew/RD.

---

## Compiler Tools Log Entry

Appended to org/compiler-tools-log.md per phase_3 mandate.

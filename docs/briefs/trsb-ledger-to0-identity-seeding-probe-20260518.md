# TRSB_LEDGER TO-0 — Identity & Seeding Probe (Phase 0 Brief)

**Project:** TRSB_LEDGER (Trade Submission executor-authorization + audit-trail hardening)
**TO:** TRSB_LEDGER.000 — ae-identity-seeding-probe
**Author:** 0.7.0_AE_CloudOps
**Date:** 2026-05-18
**Status:** COMPLETE — read-only probe; no code shipped.

Confirms or refutes the two load-bearing assumptions Phase 1 locks against (PRD §3.4/A5
authorizer identity; §3.1 groups-canonical seeding), per TO-0. Method: direct AWS-CLI +
Terraform/source read — the trade pipeline is uninstrumented in the compiler graph (PRD §5),
so direct read is the sanctioned substitute.

---

## VERDICT (one-line each)

- **§3.4 / A5 — does the trade API Gateway authorizer pass a usable acting-party identity into
  `event.requestContext.authorizer`?** — **YES.** A REST-API-v2 REQUEST authorizer
  (`portal-jwt-authorizer`) RS256-verifies the JWT and passes a verified `email` (+ role, tier,
  firmId, ...) into `event.requestContext.authorizer.lambda.*`. TO-2 can repoint actor derivation
  to it. **§7-Q5 fork is NOT triggered.**
- **§3.1 — do existing `trade-users` rows carry a populated `groups` list?** — **YES.** All 9 live
  rows carry a populated `groups` list. No seeding/backfill needed before TO-1.
- **NEW high-severity finding (not in the TO's assumption set):** the `/api/public/trades/*`
  routes bypass the authorizer entirely (`authorization_type = NONE`) and hit the SAME Lambda
  integrations as their authenticated `/api/general/` twins. TO-2's repoint is defeated unless the
  handler hard-rejects requests with no authorizer context, and/or the `/api/public/trades/*`
  routes are removed. See §3.

---

## 1. Phase 0a — Authorizer claims (§3.4 / A5)

### 1.1 The authorizer

`infra/aws/terraform/shared-infra/apigateway-portal/main.tf` — `aws_apigatewayv2_authorizer.portal_jwt`:

| Property | Value |
|----------|-------|
| name | `portal-jwt-authorizer` |
| authorizer_type | `REQUEST` (Lambda authorizer — despite the "jwt" name, it is NOT a native JWT authorizer) |
| authorizer_payload_format_version | `2.0` |
| enable_simple_responses | `true` |
| identity_sources | `$request.header.Authorization` |
| backing Lambda | `opal-portal-authorizer` |
| API | `7k3ed8px20` (opal-portal-data-proxy-api, HTTP API v2) |

The backing Lambda source is `infra/aws/lambda/portal_authorizer/index.mjs` (Node.js — note: the
0.7.0 prompt.md still describes a "Python authorizer at portal_authorizer/"; that is STALE — the
deployed authorizer is the Node.js `index.mjs`).

### 1.2 What the authorizer returns

`index.mjs` `handler()`: extracts the Bearer token from the `Authorization` header, fetches the
RS256 public key from Secrets Manager (`opal/auth/jwt-public-key`), and `jwt.verify`s it with
`algorithms:['RS256'], issuer:'opal-portal-auth', audience:'opal-portal-api'`. On success it
returns the HTTP-API-v2 simple-response shape:

```js
return { isAuthorized: true, context: {
  email: decoded.sub, name, tier, role,
  firmId, officeId, regionId, advisorId
}};
```

With `enable_simple_responses = true` + payload format 2.0, the `context` map is delivered to the
backend Lambda at **`event.requestContext.authorizer.lambda.{key}`**. So a request on an
authorizer-protected route arrives at trade-workflow-handler with:

```
event['requestContext']['authorizer']['lambda']['email']  <- RS256-verified acting-party email (JWT sub)
event['requestContext']['authorizer']['lambda']['role']   <- JWT role claim
                                                ['tier'], ['firmId'], ['advisorId'], ...
```

`context.email` is a usable, cryptographically-verified acting-party identity. **AC2 = YES.**

### 1.3 Empirical confirmation

`opal-portal-authorizer` CloudWatch log group is live — last event 2026-05-18T16:42:31Z; three
`Token verified successfully` events in the preceding 6h, e.g. `email: 'austin@opalinvest.com',
tier: 'internal', role: ...` (`austin@opalinvest.com` is a live `trade-users` row). The authorizer
is in active production use, not dormant.

### 1.4 The trade routes behind it

`infra/aws/terraform/shared-infra/apigateway-portal/routes.tf`:

| Route | auth | integration |
|-------|------|-------------|
| `POST /api/general/trades/submit` | CUSTOM (portal_jwt) | i_ehdnz7g (submission-handler) |
| `POST /api/general/trades/workflow` | CUSTOM (portal_jwt) | i_xkuchu9 (workflow-handler) |
| `GET /api/general/trades/submissions*` (8 routes) | CUSTOM (portal_jwt) | i_x3p4wrq (dashboard-api) |
| `GET /api/general/trades/identifiers/search`, `POST .../identifiers/batch` | CUSTOM (portal_jwt) | i_mvrx5ci |

The approve/reject/execute actions all arrive via `POST /api/general/trades/workflow` — behind the
authorizer. The assumption §3.4 holds for the `/api/general/` route family.

### 1.5 Current handler behavior — the A5 hole, confirmed

`infra/aws/lambda/trade-pipeline/trade-workflow-handler/src/workflow_handler.py` `lambda_handler`:

```python
body = event.get('body', {})
if isinstance(body, str): body = json.loads(body)
action       = body.get('action', '').lower()
submission_id= body.get('submission_id')
user_email   = body.get('user_email', '').lower()   # line 100 — actor identity FROM THE BODY
```

Confirmed at line 100: the acting party is `body.user_email` — a client-asserted value. The
handler **never references `event['requestContext']['authorizer']`** anywhere. The segregation-of-
duties checks (initiator != approver != executor, lines 118-138) and the `trade-users` lookup all
key off this body-supplied email. A caller can assert any `user_email`. This is PRD §2.A A5.

TO-2 fix is sound: derive the actor from `event.requestContext.authorizer.lambda.email` instead of
`body.user_email`. The authorizer supplies exactly the needed claim.

## 2. §7-Q5 fork — NOT triggered

The TO-2 fork (authorizer-change vs accepted-risk-deferral, CTO~B-adjudicated) triggers only if
the authorizer passes NO usable identity. It passes a verified `email`. **No fork — TO-2 proceeds
to the standard repoint.** No CTO~B escalation owed on this criterion.

## 3. NEW FINDING (high severity) — the `/api/public/trades/*` authorizer bypass

`routes.tf` defines a full parallel `/api/public/trades/*` route family with
`authorization_type = "NONE"`, pointing at the **same integrations** as the `/api/general/` twins:

| Public route (NONE auth) | same integration as |
|--------------------------|----------------------|
| `POST /api/public/trades/submit` | `/api/general/trades/submit` (i_ehdnz7g) |
| `POST /api/public/trades/workflow` | `/api/general/trades/workflow` (i_xkuchu9) |
| `GET /api/public/trades/submissions*` (8) | the `/api/general/` submissions routes (i_x3p4wrq) |
| `POST /api/public/trades/identifiers/batch`, `GET .../search` | i_mvrx5ci |

Consequence: trade-workflow-handler (and submission-handler, dashboard-api) is reachable
**unauthenticated** via `/api/public/trades/workflow`. A request on that route arrives with NO
`requestContext.authorizer` block at all.

Bearing on TO-2: repointing actor derivation to `requestContext.authorizer.lambda.email` is
correct, but if a `/api/public/` request reaches the handler there is no authorizer context to
read — the repoint would either crash or fall back. **TO-2 (or TO-1) must hard-reject any request
whose `requestContext.authorizer` is absent** — that is the structural catch for the public twin —
and/or the `/api/public/trades/*` routes should be removed/secured. As wired today this is a live
unauthenticated trade-submit / approve / reject / execute exposure.

Recommendation: COO~B should decide whether `/api/public/trades/*` route removal is folded into
TO-1/TO-2 scope or split to a separate TO. It is NOT the §7-Q5 fork (that is about authorizer
identity content, which is fine) — it is a distinct route-surface defect. Flagging for routing.

## 4. Phase 0b — `trade-users` seeding (§3.1)

`aws dynamodb scan trade-users` (read-only) — 9 live rows, all `active = true`:

| email | role | groups |
|-------|------|--------|
| andrew@opalinvest.com | dev | `[executors]` |
| menachem@opalinvest.com | executor | `[executors]` |
| manav@opalinvest.com | executor | `[executors]` |
| austin@opalinvest.com | approver | `[approvers, executors]` |
| lauren@opalinvest.com | approver | `[approvers, executors]` |
| alyssa@opalinvest.com | user | `[executors]` |
| yang@opalinvest.com | approver | `[approvers, executors]` |
| adam@opalinvest.com | approver | `[approvers, executors]` |
| aj@opalinvest.com | user | `[executors]` |

| Metric | Value |
|--------|-------|
| live rows | 9 |
| rows with a populated `groups` list | 9 / 9 |
| distinct group values | `approvers`, `executors` |
| in `approvers` | 4 (austin, lauren, yang, adam) |
| in `executors` | 9 (all) |
| in both | 4 |
| in neither | 0 |
| rows with empty/absent `groups` but a non-empty `role` | 0 |

**§3.1 holds — every row carries a populated `groups` list. No seeding or backfill is needed
before TO-1's group-canonical checks.** `email_utils.get_users_by_group()` already queries the
attribute (`FilterExpression='contains(#groups,:group) AND #active=:active'`), so TO-1 has both
data and a working query path.

Note for TO-1 design: `role` and `groups` are independent axes. `role` (the `by-role` GSI hash
key; drives `can_bypass_segregation` for `role==dev`) does not always agree with `groups` — e.g.
`alyssa` is `role=user` but `groups=[executors]`; `andrew` is `role=dev` / `groups=[executors]`.
If TO-1 canonicalizes authorization on `groups`, the `role` attribute remains relevant only for
the dev segregation-bypass — TO-1 should be explicit about which axis governs which decision.

## 5. Compiler Tools

| Tool | Use | Result |
|------|-----|--------|
| comp-blast / comp-iam / comp-routes | trade-* Lambdas | Not modeled (PRD §5) — direct Terraform + source read used as the sanctioned substitute, per the TO compiler mandate. |
| Direct read | apigateway.tf, apigateway-portal/{main,routes}.tf, portal_authorizer/index.mjs, workflow_handler.py | Authorizer identified; body-trust of `user_email` confirmed at workflow_handler.py:100. |
| `aws dynamodb scan trade-users` | §3.1 census | 9 rows, all `groups`-populated (read-only). |
| `aws logs` (boto3) on `/aws/lambda/opal-portal-authorizer` | liveness confirm | Authorizer active; last event 16:42Z; verified-token events present. |

## 6. Hand-off to TO-2 / TO-1

- TO-2: repoint actor identity from `body.user_email` to
  `event['requestContext']['authorizer']['lambda']['email']`. Proceed — no §7-Q5 fork.
  MUST also hard-reject requests with no `requestContext.authorizer` (the `/api/public/` twin).
- TO-1: group-canonical authorization has data — all 9 `trade-users` rows carry `groups`.
  No seeding step required. Be explicit about `groups` vs `role` axis ownership.
- COO~B routing decision owed: `/api/public/trades/*` NONE-auth route removal — fold into
  TO-1/TO-2 or a separate TO (§3).

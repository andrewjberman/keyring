# NEVER-1 co-sign, ROUND 1 -- the CTO half: auth-validator-edge refuses the Opal-only aggregate outside Opal

**Signer:** `1.0.0_SA_CTO~Z` | **Date:** 2026-09-15 ~19:2xZ | **Act covered:** `POSN_AGGFIX.TO-C1-1` (cell `AF1-s-11`): the ONE edge deploy
through `infra/aws/terraform/portal-auth/`. **Counterpart:** `2.0.0_SA_COO~Z`, `ledger/NEVER_WIDEN_ROUND1_EDGE_GATE_COO_HALF.md` @ `ed1db8f1db`.
**Rule:** CLAUDE.md NEVER-1.

> **SIGNED ON THREE CONDITIONS, each a change to TO-C1-1's criteria landed BEFORE C1-AC7, the first deploy leg. With any condition
> unmet this half is NOT SIGNED, and C1-AC6's two-file check does not by itself make it signed.**

---

## THE RADIUS IS 25 BEHAVIOURS, NOT TWO URLS

`infra/aws/terraform/portal-auth/cloudfront-distribution.tf` carries **25** `lambda_arn = local.auth_validator_edge_arn` associations
(counted by native search, this seat), and `local.auth_validator_edge_arn` at `:65` is the function's `qualified_arn`. So the one new
published version re-points all 25 at once. That covers every authenticated API path of the portal:
- `/api/general/*` and `/api/general/json-tiered/*`;
- eleven `/api/scoped/advisor-intelligence/*` behaviours;
- `/api/scoped/satellites/*` and `/api/scoped/investor-reporting/*`;
- the tickets, portal-content, data-refresh and partners paths;
- `/api/private/*`, `/api/private/portfolio*`, `/v1/*` and `/api/general/trades/*`.

The COO half's served-behaviour row changes two URLs. That is the INTENDED delta, and this half agrees with it. **The RADIUS is 25
behaviours:** a fault that throws at module load, or before the gate's URI test, fails every one of them. Rollback is a re-publish plus
edge replication, so it takes minutes, not seconds.

## What this half AGREES with, read independently

| claim | this seat's read |
|---|---|
| the admit predicate is the page's | portal `edf85ce503` `src/contexts/AuthContext.tsx:736-737` `isInternal` = `claims.firmId === 'opal-capital'`; `:750-751` `isDev` = `claims.userType === 'Dev'` |
| the edge holds both claims | `infra/aws/lambda-edge/auth-validator-edge/index.mjs:9-10` (claims list); used at `:243-244` and injected at `:387-388` |
| no tier branch runs on this path today | `infra/aws/lambda-edge/public-data-router/index.mjs`, read whole (71 lines): prefix rewrites only |
| both URL forms reach the key | `comp-routes trace` on `/api/general/positioning/opal_aggregate.json` and `/api/general/json/positioning/opal_aggregate.json`: behaviour `/api/general/*`, viewer-request `auth-validator-edge`, origin-request `public-data-router`, key `json/positioning/opal_aggregate.json` |
| writers of the viewer-request decision: 1 | `/api/general/*` (`:710-721`) associates auth-validator-edge at viewer-request. The bare `/json/positioning/...` form matches no specific behaviour, and the distribution's default origin is `S3-opalinvest-portal` (`:273`), a different bucket; the tool's catch-all is a DEFAULT, not a resolution, so C1-AC1's live census settles it. `/json-tiered/*` (`:696`) has no auth association but serves only the `json-tiered/` prefix |
| the plan shape and the WAF drift kept out | AGREED as the COO half states them |

## CONDITION 1 -- the gate decides on the path the origin will resolve

S3 resolves a percent-encoded object path to its decoded key. So `/api/general/positioning/opal%5Faggregate.json` can reach
`json/positioning/opal_aggregate.json` if the gate compares the raw `request.uri` string. Whether the edge presents the URI encoded is
INFERRED, and the harness row is what discriminates.
- The gate percent-decodes the URI and ignores the query string before it matches either aggregate form.
- C1-AC4 (unit) and C1-AC13 (live) ADD rows for the advisor and client classes on at least:
  - `/api/general/positioning/opal%5Faggregate.json`
  - `/api/general/positioning/opal%5faggregate.json`
  - `/api/general/json/positioning/opal%5Faggregate.json`
  - `/api/general/positioning/opal_aggregate.json?v=1`
  - `/api/general/positioning//opal_aggregate.json`
- Every row must be 401 or must not return the aggregate's bytes. **An advisor or client row that returns the aggregate is Branch B.**
- C1-AC4's negative control covers the new rows too: the scratch copy without the gate lets them through, so the rows can fail.

## CONDITION 2 -- the other 24 behaviours are proven unmoved

- C1-AC5's diff shows the gate's module has no top-level side effect. The gate's first statement is the URI test, which returns
  pass-through for every other URI.
- C1-AC13 ADDS, for the advisor class and the Opal-staff class, one authenticated request before the apply and one after Deployed on each
  of at least three behaviour families other than `/api/general/*`:
  - an S3-backed `/api/scoped/advisor-intelligence/*` behaviour;
  - an API-Gateway-backed behaviour (`/api/private/*` or `/v1/*`);
  - `/api/scoped/satellites/*`.
- Status and body hash must be equal before and after. **Any difference is Branch B.**

## CONDITION 3 -- the rollback target is known before the apply

Before C1-AC10, print from the LIVE distribution config the version every one of the 25 auth-validator-edge associations points at, with
the line `AUTH-VALIDATOR ASSOCIATIONS 25 -- AT VERSION <v> 25 of 25`. `<v>` is the rollback target. The COO half's rollback stands:
restore the artifact's prior VersionId and re-apply, which publishes a new version carrying the old code. A Branch B after Deployed runs it
the same turn.

## Both branches

- **Branch A** is the COO half's Branch A plus Conditions 1 and 2's rows all as expected.
- **Branch B** is any row outside that. The function rollback runs at once, the act stops on a row, and the distribution is re-read to
  25 of 25 at the restored code.

## Provenance

PRD v0.2 @ `cbd85e5cff`: C-OPAL-ONLY-DATA, C-EXISTING-PREDICATE, C-NEVER-WIDEN. Decomposition @ `605c03f81f` s.1.2. Task order
`POSN_AGGFIX.TO-C1-1` at SITEZ HEAD. Push state: LOCAL.

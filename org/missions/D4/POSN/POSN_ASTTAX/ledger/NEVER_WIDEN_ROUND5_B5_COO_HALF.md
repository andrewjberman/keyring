# POSN_ASTTAX round 5, cell B5 (AT5-s-9) -- NEVER#1 NEVER-WIDEN SIGN-OFF, THE COO HALF

**Seat:** `2.0.0_SA_COO~Z`. **Date:** 2026-09-14 ~18:2xZ. **The other half:** `1.0.0_SA_CTO~Z`,
`ledger/NEVER_WIDEN_ROUND5_B5_CTO_HALF.md` @`f5a744f412`. **Authority for the act:** Andrew ~18:1xZ at the `1.0.0_SA_CTO~Z` terminal,
VERBATIM *"I am fine with the recs as youve listed them but have questions on call 2"* -- call 1 = B5 (record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260914_181xZ_OPEN_CALLS_RECS_APPROVED_B5_YES_CALL2_QUESTIONED.md`
@`730b3309fa`, relayed 22888). This sign-off names what MOVES; it is not a second authorization.

## 1. THE RADIUS -- measured by THIS seat on a DIFFERENT instrument from the CTO half, and it AGREES: FIVE

The CTO half read `cloudfront-distribution.tf` by hand (association lines `:342`, `:373`, `:404`, `:634`, `:882`). This seat ran
`comp-routes behaviors` (the estate's parsed serving-path model: Terraform + the committed edge routers; **DESIRED plane, stated by
the tool itself**) and counted associations programmatically over its full output:

```
CLOUDFRONT BEHAVIORS (denominator) ............ 29 (incl. the /* default)
edge associations, all functions ............... 39
shared-advisor-router, origin-request .......... 5   <- THE RADIUS
    2   /api/scoped/advisor-intelligence/artifacts/*/*
    3   /api/scoped/advisor-intelligence/artifacts/*
    4   /api/scoped/advisor-intelligence/entities/*/*
   16   /api/scoped/advisor-intelligence/*.json
   27   /api/scoped/satellites/*
shared-advisor-router-response, origin-response  5   (the same five; NOT touched by B5)
```
**Five, not one.** A new published version of `shared-advisor-router`, associated through `local.shared_advisor_router_arn`
(`cloudfront-distribution.tf:66`), re-points ALL FIVE at once. Behaviors 2, 3, 4 and 16 are the live Advisor Intelligence serving
path for every partner firm. **So the act is signed ONLY AS BOUNDED** (s.2), exactly as the CTO half bounds it.

⚠ **PLANE, stated:** both halves' censuses are DESIRED (parsed Terraform). The raw live read (`aws cloudfront get-distribution-config`)
was rail-routed to `comp-routes` at this seat, correctly -- so the LIVE association set is read by the CELL, before the apply
(item 2 below), and a live count other than five is Branch B before anything moves.

## 2. WHAT MOVES, AND THE BOUND ON IT

| object | moves how | rollback |
|---|---|---|
| `infra/aws/lambda-edge/shared-advisor-router/index.mjs` | ONE hunk family: the satellites branch (`:330-360`) and its constants (`:89-101`) -- `SATELLITES_REGISTRY_LEAF` becomes a leaf ALLOWLIST `{registry.json, holdings.json, characteristics.json}` -> `platinum/satellites/<leaf>`; same prefix, same bucket resolution, same firm assertion, the refusal branch KEPT for every other leaf. **No byte outside that family** (`git diff --stat` + hunk headers printed by the cell). | `git revert` of the one commit |
| artifact `portal-auth/shared-advisor-router.zip` (bucket `opal-313476888478-lambda-artifacts`, versioning ENABLED) | one new object version; current `VersionId N3w_OHAikHzTkuf.iIGPCXPM8_4ygJlL`, `content-sha256 qrL3PFqRnq5RUyQ4SDJvZQWDreLnl7rmNWZ25IF8cx0=` (2026-08-28T02:25:36Z) | re-point to that VersionId |
| `aws_lambda_function.shared_advisor_router` | ONE new published version (`publish = true`; `qualified_arn` pin dropped @`1fb2ad4abb`/`573690efd6`, so the distribution follows) | re-associate the PRIOR qualified ARN -- the cell READS it from the LIVE distribution config and PRINTS it BEFORE the apply |
| `aws_cloudfront_distribution.portal` (`EVTSA9VEHNZVH`) | the FIVE origin-request associations move from the prior qualified ARN to the new one; **no behavior, origin, cache policy, path pattern, TTL or error rule changes** | re-associate the prior ARN on all five, re-apply |
| `aws_wafv2_web_acl.opal_cloudfront_protection` | may plan as the classified `version ""` vs `null` normalisation no-op (IRPT_BCKEND IB-s-15 precedent) | none |
| `shared-advisor-router-response`, `auth-validator-edge`, `public-data-router`, `cache-control-injector`, every other behavior, origin or resource | **NOT SIGNED -- must not appear in the plan** | -- |

**Both branches covered.** Branch A: the plan shows the function version + the five associations (+ at most the WAF no-op) and,
after the distribution reads Deployed, (i) `registry.json` 200 byte-identical to before; (ii) `holdings.json` / `characteristics.json`
200 once B2/B4 have landed, else the S3 404 envelope (NOT the router's 404 -- the two are distinguishable and the cell prints which);
(iii) a non-allowlisted leaf still 404 `unknown_satellites_resource`; (iv) ONE authenticated request per Advisor Intelligence
behavior (2, 3, 4, 16) BEFORE and AFTER, same firm, same key, status + body hash IDENTICAL. Branch B: any plan line outside the
bound -> STOP before `safe-apply`; any post-apply read outside (i)-(iv) -> re-associate the prior version on all five the same turn,
then the row. The change-management ledger entry opens BEFORE the publish; Lambda@Edge replication is not instant and the verify
legs wait on the distribution's own `Deployed` status, never on a clock.

## 3. WHAT DOES NOT MOVE

The portal gitlink `e85f6eb84f`; DEV/PROD; every served key (the router REWRITES paths, it writes no object); the response-side edge;
the auth edge; API Gateway behaviors; the WAF's rules. The freeze reading on an API-plane edge deploy was put to Andrew by
`1.0.0_SA_CTO~Z` in the same card that approved B5.

## 4. SIGNED -- COO HALF GIVEN

```
NEVER#1   "never move served output without never-widen sign-off (CTO+COO)"
ACT       B5: one new published version of shared-advisor-router, associated on FIVE behaviors
RADIUS    5 of 29 behaviors (comp-routes, DESIRED); the live count is read by the cell before the apply
DELTA     the satellites branch admits three leaves instead of one; the four Advisor Intelligence behaviors MUST read identical
COO half  2.0.0_SA_COO~Z, GIVEN. SIGNED 2026-09-14 ~18:2xZ.
CTO half  1.0.0_SA_CTO~Z @f5a744f412 -- the two censuses agree at five on two instruments
```
The B5 order cites both halves by path@commit; a deploy leg reached without both at HEAD is refused with a row.

-- `2.0.0_SA_COO~Z`

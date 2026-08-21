# DEPLOY-COMPLETION LEDGER -- OPAL_ADVIPOINTERS P4R-3 remedy (A): the platinum/advi/{firm}/ route act

**Opened:** 2026-08-21T15:57:32Z (BEFORE the first deploy act -- the bucket-policy leg -- per NEVER#6)
**Operator:** 0.7.0_AE_CloudOps (AE lane; Rule 26 builder-applies, on this device)
**Authorizing chain:** LD-0442 -- CTO arch ruling (A) + BINDING tenant-assertion amendment -- COO ruling/routing
**Status:** CLOSED 2026-08-21T16:28:12Z -- all 5 close conditions discharged (see Close record)

## What and why
DE's P4R-3 found the CVO-certified ADVI advisor twins UNREACHABLE from every portal route family:
`shared-advisor-router` resolves the origin bucket SOLELY from the validated firmId
(`FIRM_CONFIG['49financial'] = opal-data-bd`), while DS~B published the twins to the ratified
CLAUDE.md 17b serving tier, `opal-data-portal-v2/platinum/advi/49financial/`. Independently
re-measured at this seat before any edit: 10 twins live in portal-v2; `opal-data-bd` has NO
`platinum/advi/` prefix at all -- so every flipped key would be a certain 404.

Remedy (A) -- doubly ruled (CTO on architecture, COO independently on security) -- teaches the
advisor router the canonical serving bucket for that ONE path class, keeping auth-validator-edge
and per-firm scoping intact. (B) (move to the public family) was REFUSED on security posture:
`partner_analytics_*` embeds `clients[].label` and `cumulative_chart` carries
"Last, First (zXXXXXXXX)", and the public family's sibling `/json-tiered/*` carries no auth
Lambda. A third option (republish into opal-data-bd) was rejected in writing by COO.

## Legs (each must close)
1. **Bucket-policy leg** -- grant OAI `E139998VWH0PD` (the identity the advisor origin carries)
   `s3:GetObject` on `arn:aws:s3:::opal-data-portal-v2/platinum/advi/*`. Prefix-scoped, NOT
   whole-bucket. Sequenced FIRST because it is inert until the router points there.
2. **Router leg** -- `shared-advisor-router` v14: path-class override + the BINDING tenant
   assertion (`{firm}` segment asserted against the caller's validated tenant, REFUSE on
   mismatch). Built via `build-nodejs-lambda.sh`, deployed by Terraform only (Rule 1),
   applied through `safe-apply.sh` (NEVER#4 / Rule 18).
3. **TF reflection leg** -- drift assertions in `firm-bucket-cross-ref.tf` for BOTH the OAI
   principal and the `platinum/advi/*` resource scope (a principal-only check would pass on a
   silently widened grant).

## Close conditions
1. Bucket policy live and read back with all 3 statements, the 2 pre-existing serving statements
   byte-unchanged.
2. `bun run test` gate GREEN on the router, and the negative controls proven to discriminate by
   MUTANT (disarm the assertion / drop the trailing slash) -- a control that cannot fail is not a control.
3. Lambda built, TF applied via safe-apply, re-plan clean, new edge version live on all 4 behaviors.
4. **EXERCISED fetch through the auth path** -- not a config read -- and the REQUIRED cross-firm
   negative control run as its OWN ISOLATED INVOCATION (CTO 64843).
5. Report to CTO/COO/MSTR/DE; DE's P4R-3 flip unblocked or the residual named.

## Close record

**1. BUCKET-POLICY LEG -- CLOSED.** `AllowAdvisorRouterOAIPlatinumAdvi` live on opal-data-portal-v2:
OAI `E139998VWH0PD`, `s3:GetObject`, resource `arn:aws:s3:::opal-data-portal-v2/platinum/advi/*`
(prefix-scoped, tighter than the whole-bucket grants the firm buckets carry). Read back from the
live primitive: 3 statements, and BOTH pre-existing serving statements byte-identical to the
pre-change backup. Public serving re-confirmed unbroken through CloudFront: a live json-tiered
key returned 200/584 B, a nonexistent key 403 -- so the probe discriminates.

**2. TEST GATES -- CLOSED, AND THEY DISCRIMINATE.** router 17 pass; response guard 35 pass
across 2 spec files. Proven by MUTATION, not asserted:
  - disarm the router tenant assertion              -> 7 fail (all 4 negative controls)
  - drop the trailing slash from the prefix const   -> 4 fail (incl. the trailing-slash control)
  - naive guard ("any platinum/advi may be portal-v2") -> exactly the 2 guard negative controls fail
RECORDED HONESTLY: the PREFIX COLLISION test passes with AND without the slash (the PII branch
returns first), so it guards that block but does NOT control the prefix -- a separate
discriminating test was added for that. A control that cannot fail is not a control.

**3. BUILD + APPLY -- CLOSED.** Both functions built via build-nodejs-lambda.sh with the gate
GREEN; Terraform-only (Rule 1), applied through safe-apply (NEVER#4/Rule 18); re-plan
**"No changes. Your infrastructure matches the configuration."** Live edge, read from the live
distribution (not the DESIRED-plane tool): shared-advisor-router **v24** x4,
shared-advisor-router-response **v5** x4, status Deployed. Deployed v24 bytes downloaded and
read: 5/5 change markers present, negative-control marker 0, CodeSha256 identical to the built
artifact and to the source map.

  >> THE TRAP THIS ACT NEARLY WALKED INTO, recorded because it is reusable: the first plan read
  0 add / 1 change / 0 destroy with `aws_cloudfront_distribution` explicitly **no-op**.
  `lifecycle { ignore_changes = [qualified_arn, ...] }` pinned the planned ARN at `:23`, so the
  new version would have published while CloudFront kept serving the OLD code -- passing
  DESIRED (clean plan + true 0-diff), APPLIED (a new version really exists) and EXERCISED (the
  route runs green, on the old bytes). Caught in the plan JSON before applying. Fixed for the
  two functions this act deploys. Measured for the other three: they are NOT version-drifted
  today, so the defect is LATENT for them -- routed to CTO, not chased here.

**4. EXERCISED FETCH + ISOLATED NEGATIVE CONTROL -- CLOSED. This is the condition that found the
real defect.** With the router deployed, the OAI grant live and the plan clean, the first
authenticated GET returned **502 firm_isolation_guard** -- the origin-RESPONSE function
independently re-derives the expected bucket and did not know portal-v2 was legitimate. Nothing
was misconfigured; no config-plane check could have found it. Guard taught the same rule by
INDEPENDENT re-derivation (sharing the router's decision would have collapsed two layers into
one), with the tenant assertion re-derived there too.
  - PRE-CONTROL, no token                        -> 401 (route is auth-gated)
  - POSITIVE, firmId=49financial -> own tenant   -> **200, 11,129 B, sha256 BYTE-IDENTICAL to
    the certified S3 twin**, payload firm_id=49financial, data_as_of=2026-08-20
  - **ALL 10 certified twins                     -> 10/10 HTTP 200**, every byte count matching
    the S3 listing exactly
  - **NEGATIVE CONTROL (isolated invocation, CTO 64843): 49F token -> platinum/advi/inflection/
    -> 401 {"error":"Firm scope mismatch"}, zero artifact content in the body**
  - unknown tenant segment                       -> 401 Firm scope mismatch
  - NEVER-WIDEN: the 4 HELD keys + d14 still serve 200 from legacy platinum/firm/ (unmoved)
  - platinum/advisors/{id}/summary.json          -> still blocked (PII block intact)
Identities were short-TTL (300s) RS256 tokens minted by the estate's own precedented method
(the D8 battery's, used at this seat 2026-08-20); key material and tokens scrubbed from the
scratchpad at close.

**5. REPORT -- delivered to CTO/COO/MSTR/DE.** DE's P4R-3 flip is UNBLOCKED: all 10 keys are
reachable and byte-identical at their new URLs. The LD-0441 DT trigger is no longer
KNOWN-UNREACHABLE.

### Residuals named (none blocking)
- The other 3 edge lambdas still carry the `qualified_arn` pin. Latent, zero current drift
  (measured). Routed to CTO.
- `comp-routes edge-versions` reports all 5 as "DYNAMIC -- auto-update on terraform apply",
  which is exactly backwards for a pinned function. DESIRED-plane tool, cannot see the plan
  graph. Routed to CTO as declarative drift.
- Interpretation surfaced for overturn: the tenant assertion compares the path segment's
  resolved bucket against the caller's ALREADY-RESOLVED bucket, not `pathFirm === firmId`.
  This reproduces today's tenancy boundary exactly; a bare equality test would have refused
  both the mockadv alias and the opal-capital staff proxy. One line to change if CTO reads the
  bound more strictly.

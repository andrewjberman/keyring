# DEPLOY-COMPLETION LEDGER -- OPAL_ADVIPOINTERS P4R-3 remedy (A): the platinum/advi/{firm}/ route act

**Opened:** 2026-08-21T15:57:32Z (BEFORE the first deploy act -- the bucket-policy leg -- per NEVER#6)
**Operator:** 0.7.0_AE_CloudOps (AE lane; Rule 26 builder-applies, on this device)
**Authorizing chain:** LD-0442 -- CTO arch ruling (A) + BINDING tenant-assertion amendment -- COO ruling/routing
**Status:** OPEN

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
(pending)

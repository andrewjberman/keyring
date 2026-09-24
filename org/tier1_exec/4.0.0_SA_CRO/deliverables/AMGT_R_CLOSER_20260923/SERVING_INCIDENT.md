# No-span serving incident — 2026-09-23

Owner: 4.0.0_SA_CRO~Z (R). Status: ARMED; repair under local verification, no deployment.

The deployed `opal-amgt-scoped-api` serves prose that the ratified no-span HOLD rule requires it to withhold. This is an observed serving incident, not merely prospective exposure. `SERVED_CENSUS.json` records twelve actual Lambda GET invocations: 12/12 returned 200/SERVED, containing 389 sentences in aggregate, of which 179 have no quoted spans. Per-document affected counts range from 2 to 26. All twelve affected text-hash sets match the retained historical census. The missing-firm control returned 401.

## Scope and provenance

`HELD_CENSUS.json` recovers all twelve Sep19 ledger objects by exact SHA256 and S3 version. `INCIDENT_SCOPE.json` records a complete paginated listing of `opal-data-harvest/drafting/v1/` at 2026-09-23T17:16:29Z: exactly twelve current objects, identical keys. The deployed function has no drafting-root, pool-root, or drafting-bucket override. Thus the historical population also covers the full current stored drafting population at that observation; future writes require a new census.

The deployed package SHA256 (base64) was `r93CxQqrk8k8h2Q8KO4Iicn3pk8kyF4SFo47a9Cca5w=` before and after the probe; LastModified is 2026-09-22T10:07:44Z. Relevant deployed source and their hashes are preserved in `SERVED_CENSUS.json`. `_validate_drafting_document` performs schema, evidence, and source checks, but fails to apply the no-span HOLD; empty span lists pass vacuously. Calling this schema-only validation would be inaccurate.

The Sep19 `org/critical_paths/change_management/amgt-rk-41-verbatim-gate-hold-rebuild-20260919.md` already records two deployed BA GET probes returning 38 sentences, 21 without spans. The observed incident window therefore begins no later than Sep19. Neither object creation dates nor the current Lambda LastModified establish the first defective deployment.

## Reachability and measurement limits

Live CloudFront distribution EVTSA9VEHNZVH is enabled and Deployed for opalinvest.dev/www.opalinvest.dev. Its `/api/scoped/amgt/*` behavior targets API 7k3ed8px20. All sixteen AMGT routes use integration 352l7td to the affected Lambda and CUSTOM authorizer naqxlm (`portal-jwt-authorizer`, Authorization header). These are live configuration measurements, not an authenticated browser success. The Lambda probe used authorized engineering IAM invocation with the repository's firm-header fixture; it did not exercise the JWT authorizer. Human viewing and the first affected external request remain unmeasured. Authorizer and edge-policy tracing remains open.

## Repair and acceptance

The local candidate filters no-span and blank-span sentences at the reader boundary, preserves valid quoted siblings, separates reader-held from producer-held counts, and never rewrites stored objects. No offline figure claim automatically releases legacy prose: that separate discriminator releases 0/179. Its earlier zero-release result does not excuse the deployed reader defect.

Before cutover: replay all twelve exact retained objects through the candidate, complete regression checks, obtain CVO independent acceptance and the CTO+COO never-widen pair. Capture package/source hashes and rollback procedure in the exact deployment packet. Portal counter rendering is not yet implemented; API repair alone is not a completed browser journey. The surprise row AMGT_RESAPP-Z-S236 remains ARMED until independent deployed verification and explicit adjudication.

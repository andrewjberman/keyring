# Listing performance and Analysis runtime ruling

Owner/reviewer: 1.0.0_SA_CTO. Authority: Andrew's three-tab closer drive and delegated adjudication. Basis: CRO e4b28c17c4, directly read with loaders.py@bc3727b3a3 and current local portal index.tsx. Research timings/live topology are CRO observations, not a fresh CTO live measurement. Estimates are not acceptance results.

## P: bounded listing repair, preserving Reporting ownership

B3 APPROVED: immutable directory content, parsed representation, digest and sorted index may be reused only under a verified immutable identity (bucket/key plus exact VersionId or enforced content digest). A mutable key or unchecked self-declared version is insufficient. Bound memory and evict old versions. Re-read current pointer, ownership and policy on each request; fail closed on unavailable/mismatched current authority. Never cache authorization decisions or user-filtered results as universal directory data. Request-local reuse of one consistent directory/authority read is allowed; authorize every request against that current context. No shared edge cache or authorizer TTL change.

F1 APPROVED: token renewal for the same authenticated subject/session and materially unchanged authorization claims must not remount the whole workspace. Identify the principal by stable issuer/subject and real session boundary, not email alone. Logout/login, principal, effective firm/role/grant or entitlement revision changes must cancel pending requests, discard previous private data/selections and re-resolve. All calls use the current token; late responses from a prior context cannot repopulate the new one. No retention of raw token in keys/logs. Revalidation failure or revocation clears protected state.

P may implement B1/B2/B4/B5 and F2-F5 with these rules within existing owned surfaces. Speculative browse uses only a server-issued authorized firm catalogue, never guessed tenants; server re-authorizes. Merge returned Global pages deterministically, retaining firm labels; do not claim globally complete alphabetic ordering unless cursor merge proves it. Keep loaded rows during query progress without showing stale results as matches. An obsolete cursor triggers bounded refresh, not repeated retry. Per-session browse caching may retain display state only with explicit revalidation/invalidations; no staleTime that silently extends grants. Reusable SDK clients initialize lazily without import-time credential calls.

Return before/after same-account request counts, pointer/ownership revocation tests, version replacement and identity/token-refresh tests, plus real browser first-page/next-page/search measurements. Keep the existing real Reporting provider thread progressing; this is a bounded shared first-hop batch. Memory/config/keep-warm changes require an exact scoped runtime plan; no authorizer caching grant here. No claim of sub-second success from estimates.

## Y: finish the live Analysis connection

Consume CRO section4 as three separately verified runtime requirements: deployed submit source/config and exact queue SendMessage, a real consumer of irpt-generation, and the declared live-call configuration/session runner. Absence of an AWS Lambda event-source mapping alone does not prove absence of an EC2 poller; identify the actual chosen consumer and show its receipt. Also include the missing input and request-list/detail routes in the installation manifest. Supply the worker caller, durable lease/idempotency/recovery contract, exact artifacts and an executable upload-to-published-Overview test. P owns shared route/IAM/package integration; Y owns the complete product trace and returns concrete ready dependencies rather than status-only callbacks.

No always-on topology change or standing vendor-call permission is inferred from this research. Prepare one reviewable runtime plan with a single session owner and no parallel legacy probe. Reuse existing per-use authorization where it covers the exact run; name only genuinely missing authority. CRO continues its targeted SmartX interface research. No extra general research project.

## Status

Local implementation directions, not deployment or E2E acceptance. Reporting, Holdings and Analysis remain incomplete. Current contract v1.4 and CONTROL.md govern lane ownership; this ruling refines shared listing mechanics.

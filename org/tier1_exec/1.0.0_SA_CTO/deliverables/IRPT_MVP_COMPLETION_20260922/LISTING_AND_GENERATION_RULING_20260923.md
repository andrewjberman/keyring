# Listing performance and Analysis runtime ruling

Owner/reviewer: 1.0.0_SA_CTO. Authority: Andrew's three-tab closer drive and delegated adjudication. Basis: CRO e4b28c17c4, directly read with loaders.py@bc3727b3a3 and current local portal index.tsx. Research timings/live topology are CRO observations, not a fresh CTO live measurement. Estimates are not acceptance results.

## P: bounded listing repair, preserving Reporting ownership

B3 APPROVED: immutable directory content, parsed representation, digest and sorted index may be reused only under a verified immutable identity (bucket/key plus exact VersionId or enforced content digest). A mutable key or unchecked self-declared version is insufficient. Bound memory and evict old versions. Re-read current pointer, ownership and policy on each request; fail closed on unavailable/mismatched current authority. Never cache authorization decisions or user-filtered results as universal directory data. Request-local reuse of one consistent directory/authority read is allowed; authorize every request against that current context. No shared edge cache. Authorizer TTL is governed by the later Andrew-direct amendment below.

F1 APPROVED: token renewal for the same authenticated subject/session and materially unchanged authorization claims must not remount the whole workspace. Identify the principal by stable issuer/subject and real session boundary, not email alone. Logout/login, principal, effective firm/role/grant or entitlement revision changes must cancel pending requests, discard previous private data/selections and re-resolve. All calls use the current token; late responses from a prior context cannot repopulate the new one. No retention of raw token in keys/logs. Revalidation failure or revocation clears protected state.

P may implement B1/B2/B4/B5 and F2-F5 with these rules within existing owned surfaces. Speculative browse uses only a server-issued authorized firm catalogue, never guessed tenants; server re-authorizes. Merge returned Global pages deterministically, retaining firm labels; do not claim globally complete alphabetic ordering unless cursor merge proves it. Keep loaded rows during query progress without showing stale results as matches. An obsolete cursor triggers bounded refresh, not repeated retry. Per-session browse caching may retain display state only with explicit revalidation/invalidations; no staleTime that silently extends grants. Reusable SDK clients initialize lazily without import-time credential calls.

Return before/after same-account request counts, pointer/ownership revocation tests, version replacement and identity/token-refresh tests, plus real browser first-page/next-page/search measurements. Keep the existing real Reporting provider thread progressing; this is a bounded shared first-hop batch. Memory/config/keep-warm changes require an exact scoped runtime plan; authorizer caching follows the amendment below. No claim of sub-second success from estimates.

## Y: finish the live Analysis connection

Consume CRO section4 as three separately verified runtime requirements: deployed submit source/config and exact queue SendMessage, a real consumer of irpt-generation, and the declared live-call configuration/session runner. Absence of an AWS Lambda event-source mapping alone does not prove absence of an EC2 poller; identify the actual chosen consumer and show its receipt. Also include the missing input and request-list/detail routes in the installation manifest. Supply the worker caller, durable lease/idempotency/recovery contract, exact artifacts and an executable upload-to-published-Overview test. P owns shared route/IAM/package integration; Y owns the complete product trace and returns concrete ready dependencies rather than status-only callbacks.

SUPERSEDED authority boundary: Andrew subsequently approved option C and standing host workflow calls in6fc3f5f785, consumed below. Prepare and implement the exact runtime plan with one session owner and no parallel legacy probe; do not ask again for already-approved topology or first sign-in. CRO continues its targeted SmartX interface research. No extra general research project.

## Status

Local implementation directions, not deployment or E2E acceptance. Reporting, Holdings and Analysis remain incomplete. Current contract v1.4 and CONTROL.md govern lane ownership; this ruling refines shared listing mechanics.

## Andrew-direct amendment - 19:53 relay99724, authority6fc3f5f785

The exact CRO authorization record was read after the first ruling. Andrew approved the recommendations, including B1-B8/F1-F7, pagination and option C. This supersedes the earlier held topology/call boundary. The implementation constraints on current entitlements remain.

Y is accountable for always-on Analysis: irpt-ycharts-runner i-0167fd745ad906a66 stays running, dedicated with no inbound service, canonical session owner and irpt-generation consumer. Standing host calls cover automated sign-in/session maintenance, generation and sessionless upload ticker lookup, including D1. Agent ad hoc vendor calls remain outside this grant. Replace per-job power cycling and retire the separate six-hour probe at controlled cutover; do not create a second session path. D2 becomes durable session/operation recovery inside the resident service; fencing, reconciliation and bounded retry remain. No opal-gateway co-hosting.

P remains sole writer of shared IaC/route/IAM/package/header surfaces; Y supplies exact installer/service/consumer source and a ready manifest, P applies the bounded shared delta, Y proves the real upload-to-screen journey. Generation path first: pin the reviewed submit source (HEAD is not an immutable release identifier), exact SendMessage to irpt-generation, resident consumer, IRPT_LIVE_YCHARTS_CALL and missing inputs/requests routes. P prepares scope/hash/rollback and consumes this authority through canonical apply. No fresh user permission for these approved actions. M retains Holdings ownership. MSTR must preserve the running host.

B8 is approved in principle, not an arbitrary TTL: P prepares the smallest IRPT-compatible authorizer plan with existing owner/CloudOps review of cache identity/route keys and current entitlement enforcement. It must not grant stale firm access or weaken current downstream checks. It does not block generation or B1-B7/F1-F7. P continues Reporting alongside bounded shared batches; Y owns the runtime result, not merely forwarding ports to P.

# Opal and partner scope: narrow independent review

Reviewer: `3.0.0_SA_CVO~M`. Operative resume: exact CTO message `20260923T131715Z`, explicitly relaying Andrew's resumed session and authorizing this reviewer only for P's Opal/partner scope repair. Durable requirements read from `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/LOCAL_LIVE_PARTNER_SCOPE_20260923.md`, under `CONTRACT.md` in the same directory.

All other held work remains held. P owns implementation. CVO P owns browser/page/client serialization, signed-in context/cache, late responses, login/reload and Resolution confirmation. CVO M owns actual server principal, selected-tenant, cursor/cache and selection boundaries. No duplicate broad sweep or producer edits.

## Current status

**NOT_EVALUATED: immutable repair pins and concrete authority contract pending.** This document prepares the review; it supplies no candidate or live verdict. Prior M source closure `91d08f28ca` at `567a157ec8` and P's previous component evidence remain bounded historical results.

The CTO record reports an authenticated bootstrap refusal, HTTP 200 / UNAVAILABLE / UNEXPECTED, and a separate controlled reproduction against exact deployed bytes: Opal home firm leads to BucketUnmapped; a selected partner leads to FIRM_BINDING. These are attributed CTO findings, not new live measurements by this seat. Global must be an authorized cross-firm browsing context, not a bucket or an arbitrary first-firm fallback.

## Candidate handoff needed

P supplies immutable backend and Portal pins, relevant changed paths, focused actual Entry test invocation and packaged dependency composition. The authority handoff must identify the concrete server roster/identity source, permitted-firm catalogue source, freshness/version/revocation semantics, selected-firm wire grammar and downstream accepted-selection representation. Do not infer an expiry interval or grant missing from that contract.

## Actual-module controls

| Control | Positive and negative evidence required |
|---|---|
| Authoritative Opal identity | A verified principal with current server-authorized Opal membership can enter Global and choose only permitted partners. Missing/invalid/revoked membership cannot become Global through role strings, browser flags, home-firm spelling or catalogue labels. Test stale authority against the actual freshness contract. |
| Partner firm confinement | Partner advisor and operations roles remain in their verified own firm. Forged Global, foreign tenant, opaque/registry alias confusion and conflicting selectors refuse without reading foreign data. No UI-only permission enforcement. |
| Bootstrap independence | Actual initial request resolves authoritative context without requiring a previously resolved directory. Global does not load a bucket named global or opal-capital, fabricate scope, or choose an arbitrary partner. Missing authority/dependencies remain explicit. |
| Global query isolation | Spy on actual dependency calls: only authorized firms are queried or included. Test one/multiple/no permitted firms, per-firm empty results, missing directory and one-firm failure. Incomplete or unavailable results cannot be represented as complete Global data. |
| Firm attribution | Every Global row keeps authoritative firm identity. Identical display names and similar account identifiers across firms remain distinct; selecting one row cannot silently change or broaden its tenant. |
| Resolve and accepted selection | Carry selected tenant through resolve, browse/search, selected-set creation/resolution and applicable downstream scope checks. Exact account/client/relationship membership remains server-accepted. Reject foreign or mixed-tenant membership and stale selection context. |
| Cursor isolation | Exercise actual page continuation and exhaustion, bounded stable ordering, and changed principal, membership, tenant, query, page size, directory and entitlement revisions. A cursor never grants access; removed firms/accounts cannot survive via continuation. |
| Server cache isolation | Warm actual configured cache paths, then switch principal/tenant/authority/context. No previous user's or previous permitted set's bootstrap/search/selection becomes current. Record the actual cache path tested; fresh-instance tests cannot establish cache isolation. |
| Current authorization | Change or revoke authority between requests and verify fresh denial and no stale protected response. Test documented freshness boundaries; do not claim atomic revocation during every instruction without evidence. |
| Existing contract and refusals | Preserve real schema/Entry behavior, verified origin/contract negatives, exact selection semantics and malformed-input controls from M-BOOT-01. Use new candidate-specific evidence; do not transfer prior PASS. |

Tests will execute actual candidate modules with controlled external dependencies and synthetic data first. Capture hashes, exact commands, counts, sanitized request/response shapes and dependency-call assertions. Preserve failing assertions for unchanged correction retests. Route concrete failures to P and CTO; keep source, package and live verdicts distinct.

## Browser and operational boundary

CTO explicitly authorizes the current `localhost:5174` dev:live path, which forwards normal bearer authentication and host-only cookies through `d2n2nzpeqf34ge.cloudfront.net`. It retains gateway, edge auth and origin-secret checks and copies no secret. This supersedes the earlier blanket localhost restriction only for this exact current review path. Fixtures or bypass tokens cannot prove live data access. CVO P coordinates browser evidence; this plan starts no listener and edits no CTO worktree.

No cloud mutation or Portal production promotion is authorized. If runtime changes are necessary, P prepares a concrete minimal plan for CTO adjudication. Live data success and Andrew's smoke remain separate from source controls. No schedule, worker or unrelated held work is resumed.

## Principal design adjudication consumed: 20260923T132334Z

The exact CTO message and updated durable record admit COO P's `132215Z` design for implementation and review, not acceptance or deployment. These requirements settle the earlier pending authority/freshness questions; they do not require a new roster service, TTL, route or edge modification.

- Eligibility is exactly verified `firmId == opal-capital OR userType == Dev`, from the established edge predicate in `aggregate_gate.mjs`. Authenticated subject and verified origin remain prerequisites. Admin role, email suffix and browser labels alone cannot confer eligibility. Check both positive arms independently, negative combinations, and renderer/delegate restrictions even when an internal predicate arm is present.
- The resolver bridge is a request-local eligible-subject roster. Check the actual module Entry roster and cached state before and after an Opal request, then issue partner requests in the same warm process, including a same-subject request whose current verified claims no longer qualify. No persistent roster mutation or inherited Global eligibility is acceptable. This supplements the initial roster-control row without inventing an external service.
- Identity freshness is the current verified JWT lifetime. Tests can vary current verified request claims between calls; they cannot establish immediate revocation of a still-valid JWT. Directory ownership and entitlement checks remain current per request. Do not impose a new roster TTL or label the admitted lifetime boundary as an implementation defect.
- Global on the existing resolve route is an explicit discriminated directory-context response with per-firm outcomes/scopes. It must not fabricate a union ResolvedScope. CVO P owns the strict paired schema/parser arm; M verifies actual per-firm server outcomes, query isolation and absence of arbitrary default-partner behavior.
- `selected_tenant` is registry-slug request intent, never an opaque firm ID or a grant. Add conflicting carrier cases across body/query and other supported selectors, unknown slug, partner foreign/global intent, foreign selection references, cross-context cursors and account-tenant mismatches. Validate every relevant operation, including warm-cache paths; preserve user, selected tenant, filter and current directory/entitlement bindings.
- Failed firms remain failed/partial/unavailable in Global responses; an unavailable firm cannot be represented as an empty success. No partner is selected merely because none was requested.

Exact implementation/consumer pins are still pending. Controls are prepared and **NOT RUN** against a replacement candidate; no current-candidate PASS is claimed.

# IRPT local live-data partner selection repair

Owner/adjudicator: `1.0.0_SA_CTO`. Implementation: `2.0.0_SA_COO~P` under the
existing temporary live-scope ownership. Independent review: `3.0.0_SA_CVO~P`,
with selection review coordination through CVO~M. Parent: [CONTRACT.md](CONTRACT.md).

## Current user direction

Andrew resumed the session for a functional localhost with live data. Normal
login succeeded at `http://localhost:5174`, but IRPT showed `Resolving firm...`
and `Scope could not be resolved`. Andrew then supplied the Model Portfolios
`/portfolios` Select Partner control as the desired behavior: firm users see
their own firm only; Opal users default to Global; the existing Resolution area
confirms the search selection. This narrowly resumes this repair and its review.
Other held workstreams remain held.

## Measured failure, not a localhost connectivity failure

- Portal base: DEV `fac3b6a0c7cb55dd75d3c190a1382ce710030381`.
- Local launcher: isolated `codex/local-live-data-20260923`, commit `de405810`.
  Real auth/data go through CloudFront; no origin secret is copied locally.
- Actual authenticated browser bootstrap through the local proxy: HTTP 200,
  `ok:false`, `contract_version:v1`, status `UNAVAILABLE`, reason `UNEXPECTED`,
  no data or firm_id. The trace records response structure only, not credentials
  or investor data. This is a backend refusal, not authenticated data success.
- Live Lambda `irpt-directory-search` remains `entry.lambda_handler`, Python 3.12,
  Active, artifact SHA256 base64 `iqLKa1RWk9hlcSlAheuoAMgIY4R3VrStPX1eG5Qwq/s=`.
- CTO downloaded that exact deployed artifact read-only (149956 bytes), verified
  its hash and entry.py byte equality to repository source, and executed it
  locally with synthetic Opal headers and its actual directory bucket map.
  S3 calls were replaced with a fail-if-called stub; no investor data was read.
  A null firm selector reproduced `BucketUnmapped -> UNEXPECTED` for
  `opal-capital`; requesting `49financial` reproduced `FIRM_BINDING`.
- The runtime map has 49financial, inflection and cottonwood, not opal-capital.
  `comp-keys exists investor-reporting/directory/latest.json` measured a live
  pointer in all three mapped buckets. Existence does not prove freshness,
  readable target artifacts, grants or successful browse responses.
  These reproduction headers model an Opal principal; they are not a captured
  user token or proof of every field in Andrew's actual token.
- The current shared boundary requires a request firm to equal the edge-injected
  JWT home firm. Directory ENTRY does not wire an Opal principal roster.
- IRPT's dropdown waits for successful ResolvedScope before offering firms.
  Model Portfolios instead chooses its initial display from authenticated context:
  internal/Dev defaults Global; external uses its own firm. Its static UI options
  are not a substitute for backend entitlement enforcement.

## Binding product and security requirements

1. Initial partner selection must not depend on the directory resolution it is
   needed to request. Authenticated context may initialize the UI; it grants no
   data access on its own. Partner users start and remain in their own firm.
2. Opal users start in Global and may select a permitted partner. Global must be
   an explicit authorized cross-firm browsing context, never a directory bucket
   named global or opal-capital, and never an arbitrary first-firm fallback.
   Existing server registry/identity conventions remain authoritative.
3. Carry and verify the selected firm throughout resolve, browse/search,
   pagination, accepted selection and downstream reads. A firm choice is a
   request to authorize, not a trusted x-firm-id supplied by the browser.
   Preserve opaque firm IDs versus registry tenant IDs without conflating them.
4. Search results retain firm attribution. Resolution confirms the chosen
   client/relationship/accounts and accepted server selection. Do not introduce
   a separate entitlement step for the user or fabricate a ResolvedScope.
5. Clear identity/firm-bound selections, cursors and cached data on context
   changes; no previous user's bootstrap or search may survive as current data.
6. Global empty/partial/unavailable outcomes must be explicit. One failed firm
   cannot masquerade as a complete Global result. Unauthorized firms must never
   be queried or included. Reports continue to use accepted, tenant-bound IDs.

## Delivery and review

P owns the paired candidate and exact dependency/route/IaC/artifact delta.
Reuse the current Model Portfolios behavior and existing IRPT code where sound;
do not edit the CTO's live worktree. CVO~P independently tests exact replacement
pins, including actual Opal initial bootstrap, Global and partner switching,
firm-user lock, forged foreign/global selectors, context changes, pagination,
selection confirmation and reload. Prior fixture passes cannot close this gap.

No cloud apply or Portal production promotion is authorized by this record.
Prepare a concrete minimal runtime plan for CTO adjudication if the deployed
backend needs changes. Keep the localhost instance available for the next smoke.

## CTO design adjudication: COO P proposal 20260923T132215Z

Admitted for implementation and independent review. The established internal
predicate is exactly verified `firmId == opal-capital OR userType == Dev`;
`auth-validator-edge/aggregate_gate.mjs` defines it, and `index.mjs` overwrites
the downstream identity headers after JWT verification. An admin role, email
suffix, browser claim, or caller-supplied origin marker alone does not qualify.
This is a source-grounded design decision, not a new live edge-version verdict.

- Preserve the authenticated subject and verified origin prerequisite. Preserve
  the existing distinct renderer/delegate restrictions; the internal predicate
  must not elevate a render token into a full Global user.
- A request-local eligible-subject roster may bridge the existing scope resolver.
  Never mutate the module's Entry roster, a shared resolver or cached entitlement
  state. Test an Opal request followed by a partner request in the same warm process.
- Admit an explicit discriminated Global directory-context response on the
  existing resolve route: per-firm authorized outcomes/scopes, never a synthetic
  union ResolvedScope. Publish and test the paired schema/parser arm; existing
  single-firm success and refusal validation must remain strict.
- `selected_tenant` is a registry slug and request intent, separate from opaque
  IDs. Validate it against server authority on every relevant operation. Reject
  ambiguous/conflicting selector carriers, foreign-firm selection references and
  cross-context cursors; bind pagination/cache identity to user, selected tenant,
  filter and applicable entitlement/directory revisions.
- Keep partial Global outcomes visible. Do not render a failed firm as an empty
  success or use a default partner when no partner was requested.
- The current verified JWT lifetime is the identity freshness boundary. Do not
  claim immediate identity revocation during that lifetime. Current directory
  ownership/entitlement checks still apply on each request.

No new route, edge modification, roster service or TTL is required by this
design. P must identify any actual deployment/package delta in the candidate;
this admission grants no cloud apply or production promotion.

## CTO generation adjudication: COO P fork 20260923T135114Z

Admit a bounded **custody-only** owner/profile extension for a verified Opal
principal acting on a currently authorized, accepted partner account selection.
This implements the same selected-partner journey; it does not extend prospect
upload/input privileges or grant access from a browser-supplied owner record.

1. Keep actor and report tenant distinct. The principal is the real verified Opal
   subject, with its actual home firm preserved. The report/storage tenant is the
   explicitly selected, authorized partner. Do not rewrite the actor's home firm,
   substitute a partner advisor, or invent an advisor ID. An Opal owner may have
   a null advisor ID only in this admitted custody arm.
2. P owns the paired owner/source-binding schema extension and shared custody
   authorization/profile port; Y owns consuming it in generation assembly and
   submission. M's read-only producer audit remains non-overlapping. Prefer a
   distinct custody profile entry point using the maintained readers; do not
   broaden `resolve_prospect_owner` or its existing prospect callers.
3. Admission requires the guarded selected tenant and exact accepted custody
   account set/snapshot. Validate equality/binding through immutable composition,
   worker consumption, retained history/report reads and reopen. An `OPAL_GLOBAL`
   enum string by itself is no authority. Global discovery cannot generate a
   report without a concrete tenant-bound selection.
4. Preserve current input authorization before and after maintained profile
   reads. Resolve the actual active actor from the canonical user source using
   its home-firm binding. Prepared-by identity/organization must truthfully
   identify that actor and its maintained organization; selected partner remains
   report context, not an impersonated preparer. Source descriptors must express
   the real source scope separately from the authorized report binding. Freeze
   exact projections/digests for worker/retry use; no invented profile defaults.
5. Update schemas, validators, producer and consumers together. A blanket enum
   relaxation is insufficient: tests must reject Opal prospect inputs, fake
   owners, partner-admin Global elevation, home/target substitution, mixed or
   stale account sets, unrelated snapshots and retained cross-tenant references.
   Preserve existing partner advisor/operations behavior and renderer restrictions.
6. CVO~M reviews principal/owner/source-binding and source provenance controls;
   CVO~P reviews paired wire/schema/context and retained consumer behavior. Y
   supplies actual generation-module custody/prospect positives and negatives
   without vendor execution. Separate unmeasured live/vendor acceptance remains
   explicit; this is implementation authority, not a release PASS.

No new vendor egress, AWS write, IAM grant or production promotion is authorized.
Include this extension's exact source/package dependency delta in P's candidate.

## Product clarification relayed by COO Y, 20260923T135600Z

Y reports Andrew's exact direction: Opal users can select any firm client and
drill down to accounts directly from the Global default view, managed by the
upper-right Select Firm control, following Model Portfolios and the existing
`api/scoped` multi-tenant structure. This is consistent with the admitted Global
browsing requirement above. Do not require an Opal user to switch the dropdown
to a partner before selecting that partner's client from Global. Keep Global as
the discovery filter while the selected row supplies a server-verified concrete
tenant for drilldown, accepted account selection and report generation. Preserve
firm attribution and distinguish same-named clients across firms by verified
tenant and canonical IDs. P owns the shared UI/API implementation; Y consumes
the accepted concrete selection. This clarification is not a live PASS.

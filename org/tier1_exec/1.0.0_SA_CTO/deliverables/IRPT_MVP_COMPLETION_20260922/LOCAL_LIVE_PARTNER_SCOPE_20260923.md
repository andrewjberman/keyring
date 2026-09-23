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

## Exact source grant: COO P request 20260923T135842Z

Grant P ordinary commit access to the exact source path
`infra/aws/lambda/investor-reporting/holdings/entry.py`, using the existing
`IRPT_LIVE_SCOPE_P` lane. Scope is M-OPAL-01 request-local eligible-roster
continuity through the existing pre-read and post-read authorization checks.
Preserve actor, selected tenant, snapshot/account binding and revocation checks;
do not mutate a module roster. Other holdings paths remain M-owned. Existing M
and incumbent permissions are preserved; this does not hand shared scope back
to M or grant deployment authority.

`_scope/maintained_sources.py` already matches `_scope/**` in that same P lane.
Its custody-only profile-port work is admitted by the generation adjudication
above; no additional path grant or prospect authorization expansion is needed.
P must consume this registry change in its isolated worktree and use ordinary
pathspec safe-commit. No hook bypass is authorized or necessary. P's reported
73 passing checks are implementer evidence. M-OPAL-01 remains OPEN until CVO M
independently reruns the unchanged driver against the committed correction.

## Organization source adoption: M inventory 20260923T141619Z

M inventory `7015e0d626` reports a strongly consistent metadata-only read of
`opal-users-v2`, `FIRM#opal-capital` / `CONFIG#defaults` at 14:11:46Z. The
organization projection exists, with `firmName=Opal Capital`; its projected
receipt hash is `7cf0b38b85f49588bef4a8e4d2d783f3625074cc0bd751c7812ef45e966ed767`.
This is measured source existence, not an immutable upstream version or current
runtime-reader acceptance.

CTO admits this exact existing record as the Opal organization metadata source
for the already-authorized custody-only preparer profile. P owns the shared
integration and may implement the exact-key read-only reader in its existing
granted source surface, paired with Y's descriptor consumer. Derive the home
organization from the verified actor and current canonical user profile; never
from the selected report tenant or a browser-provided organization key. Restrict
the Opal arm to the admitted Opal home key. Project only required organization
identity/display metadata and explicitly identified provenance fields; do not
fetch provisioning defaults, security settings or unrelated user records. No
scan, write, deprecated provisioning invocation or hardcoded display fallback.

Preserve before/after custody authorization and actor-home checks. Missing,
malformed, mismatched or changed metadata must produce an explicit refusal or
the established bounded retry, never partner substitution. Freeze the exact
projection and digest under truthful source provenance for worker/retry use;
do not represent the mutable table row as an immutable upstream object. Preserve
existing partner and prospect semantics. CVO M independently verifies source,
home/tenant separation and change/refusal cases; CVO P/Y verify the paired schema
and actual consumer. The provisioning owner is CloudOps; request owner contract
confirmation through MSTR without expanding source scope.

This is source implementation/adoption authority only. P must supply exact
source paths, dependency/package changes and any narrowly scoped GetItem IAM
delta in the candidate. No new cloud permission, live apply or deployment is
granted. Additional shared paths still require an exact ownership grant.

Producer findings remain separate: stale directories require actual run,
dispatch/install and input-frontier evidence; INF's maintained advisor contract
must not inherit BD five-role semantics; COT's empty-map branch is a source risk
until linked to the same live run/output version; 49F needs owner-supported
crosswalk or producer re-keying proof, never a fallback authorization join.

## Andrew-direct review ownership, 2026-09-23 11:18 Eastern

Direct user message at the CTO terminal, verbatim:

> No independent review, you are the reviewer here

This later direction supersedes the separate CVO review assignments and CVO
approval requirements above for the current resumed IRPT scope/parser,
organization reader, custody factory and paired integration/package work.
CTO performs the code, test and artifact review directly. Existing CVO evidence
is retained as evidence, not a required additional gate. P/M/Y implementation
ownership remains unchanged; new candidates and findings go to CTO. No release
or cloud authorization changes. Relayed to CVO P/M/Y, COO P/Y and MSTR at
11:18 Eastern; separate CVO review runs instructed to stop and preserve work.

## CTO signed-value disposition, 2026-09-23 11:31 Eastern

Consumed Y proposal `5d7da1aa49`,
`CUSTODY_SIGNED_VALUE_PROPOSAL_20260923.md`, and M source handoff
`abfb3eaf8242cf5df26c7e1074e0e555245d969a`. Adopt the proposed conservative
eligibility boundary for the existing positive-only recipe. Preserve the exact
actual signed/zero source facts and refuse the whole selected portfolio when
any actual row is unsupported, before combining equal securities or accounts.
No absolute values, dropped rows, invented cash, model substitution or hidden
offsetting. Unknown value is never zero. This is an explicit current limitation,
not completion of signed-position reporting or a claim about vendor capability.

Do not globally relax the shared positive-number helpers, alter historical
frozen requests, create a new retained artifact family or add public refusal
enums under this disposition. Keep existing supported refusal envelopes;
P owns any future paired public mapping. A future signed recipe needs an
explicit economic policy and complete transport/readback/report proof.

The actual-position source proposal remains M's bounded read-only assignment.
Y may prepare owned eligibility controls against the original row census, but
must identify the concrete producer interface before implementation. P keeps
shared integration/package ownership. Production callbacks remain closed until
exact accepted snapshot identity and complete security-level custody source are
implemented and directly reviewed by CTO. The bounded source review at
`8653eb6cd4` does not lift this condition or authorize cloud changes.

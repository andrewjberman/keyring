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

**Author:** 4.0.0_SA_CRO (Chief Research Officer)
**Home:** org/tier1_exec/4.0.0_SA_CRO/
**For:** 1.0.0_SA_CTO msg 99458 (design research); Andrew-direct "Option 2 is preferable" (record @29d157110d). Becomes the IRPT_BCKEND round-17 PRD addendum input.
**Verified by this seat before publishing (read at @f8d94a3194):** V3 `auth-validator-edge/index.mjs:235` verifies with `{ algorithms: ["RS256"] }` only -- no aud/iss; V2 `portal-authorizer/index.mjs:200-203` checks issuer `opal-portal-auth` + audience `opal-portal-api`, and `:246` returns `generateSimpleResponse(true, context)` with no role check. Both match the table below.

# IRPT renderer auth -- design research for Option 2 (short-lived per-run "renderer" token)

Answers 1.0.0_SA_CTO msg 99458, weighted to Andrew's choice of Option 2. READ-ONLY: no code, config,
IAM or secret was changed.

Vintages:
- Workspace citations are @e6abd13f94 unless marked @f8d94a3194. HEAD moved during the research. The
  last four verifier reads (session-analytics, opal_auth, validator.py, validator.ts) were taken at
  f8d94a3194.
- Portal citations are portal@86ae054b.

## (a) Mint, verify, and every verifier

### Mint
One minter: infra/aws/opalinvest_dev/lambda/auth-handler/src/jwt.ts.
- It signs RS256 with the key in secret `opal/auth/jwt-private-key` (:8).
- Access token TTL is 15m and refresh token TTL is 7d. The claims are iss `opal-portal-auth` and aud
  `opal-portal-api` (:17-20).
- tier is derived from firmId, not asserted separately: `firmId==='opal-capital' ? 'internal' :
  'advisor'` (:168).
- Access payload (:172-193): sub, name, role, tier, firmId, userType?, advisor* fields, firmRole?,
  iss, aud.
- verifyAccessToken checks RS256 + issuer + audience (:251-261). verifyRefreshToken checks RS256 +
  type 'refresh' only, with no iss/aud check (:267-282).

### Verifier census
Method: two comp-find content sweeps.
- `jwtPublicKeys|verifyWithSlots|getJwtKeySlots|opal/auth/jwt-public-key` over infra: 75 hits across
  11,862 files.
- `jwt\.verify|jwtVerify|jose\.|verifyAccessToken|RS256` over infra + portal/src: 172 hits across
  12,721 files.

The hits were then read per file. There are 7 distinct server-side verifiers of the portal key:

| # | verifier | iss/aud checked? | on an unknown role / new claim |
|---|---|---|---|
| V1 | auth-handler index.ts authenticateRequest :156-166 -> verifyAccessToken | YES (jwt.ts:251-261) | only reads {sub, role} |
| V2 | portal-authorizer infra/aws/users/lambda/portal-authorizer/index.mjs | YES :200-203 | **DEFAULT-ALLOW**: always generateSimpleResponse(true) (:217-245); unknown role gets own-firm allowedFirmIds (:125-150) |
| V3 | Lambda@Edge infra/aws/lambda-edge/auth-validator-edge/index.mjs | **NO** -- `verifyWithSlots(jwt, token, slots, { algorithms: ["RS256"] })` :235 | **DEFAULT-ALLOW** of any validly signed token. Injects X-User-Role (default 'user'), X-User-Tier (default 'unknown') and X-Firm-Id=payload.firmId (:400-405). Admin bypass on role admin / firmRole admin / tier internal / userType Dev (:258-260) |
| V4 | session-analytics src/auth.ts @f8d94a3194 | YES :85-88 | admin = role 'admin' or 'internal' (:91); other roles are non-admin, so default-deny for its viewing endpoints |
| V5 | infra/aws/lambda/shared/opal_auth/__init__.py @f8d94a3194 | YES :106-112 | role compared to 'admin' (:67). A comp-find for importers returned only itself, so its live consumers were NOT verified |
| V6 | infra/aws/auth/validator.py @f8d94a3194 | YES :124-129 | tier hierarchy `.get(tier, 0)` (:73-74): an unknown tier ranks lowest |
| V7 | infra/aws/auth/validator.ts @f8d94a3194 | YES :134-137 | role defaults to 'user', tier to 'client' (:172-173) |

V6 and V7 have no code importers. comp-find `auth/validator` returned 2 hits, both in ARCHITECTURE.md
(DOC band). The opal-gateway uses a separate token system and is out of scope.

### Frontend
The frontend is not a verifier.
- portal/src/components/ProtectedRoute.tsx:39,44 is a client-side redirect on decoded claims:
  requireAdmin means role==='admin', and requireInternal means firmId==='opal-capital'.
- The print route is App.tsx:576.

### What this means for a new token
- If the render token carries a DISTINCT aud (e.g. `irpt-render`), V1, V2, V4, V5, V6 and V7 refuse
  it by default: an audience mismatch throws.
- V3 (edge) accepts it and treats it by its role/tier/firmId claims. V3 is therefore the one verifier
  that must be changed to refuse, or to scope, the new token.

## (b) Existing machine/service identities

None found solves headless rendering.
- Every verifier above is keyed only to human-login tokens minted by auth-handler.
- The census found no service-account mint path, no client-credentials flow and no second issuer on
  the portal key.
- Option 1 (a dedicated MFA-off portal user) would be the first such identity.
- NOT exhaustively verified: CI / ui-smoke auth stubs. See the last section.

## (c) API routes the print page reads

Code path:
- PrintEntry.tsx reads query params bundle, tenant, scope, revision, kind and narrative (:104-110).
- :124 (previewExportBundle) is RETIRED -- `export-preview` is in IR_RETIRED_OPERATIONS
  (investor-reporting.ts:220). It therefore issues NO network call and composes locally.
- It then calls resolveBundle (:139), which calls three getters (resolveBundle.ts:250, :261, :279).

Base `/api/scoped/investor-reporting` (investor-reporting.ts:109). Exactly THREE GET routes:

1. `GET .../performance/{accountSetId}` (:181)
2. `GET .../analysis/{jobId}/sections` (:183)
3. `GET .../narrative/{reportId}` (:184)

API Gateway details:
- All three are on HTTP API `7k3ed8px20` under CUSTOM authorizer `naqxlm` (portal-jwt-authorizer =
  V2). See infra/aws/terraform/investor-reporting/api/integrations.tf:14-20 and routes.tf:52-53.
- That authorizer is SHARED. The same id appears in the bd-pipeline, harvest, partners-api,
  portal-content and ticket-center Terraform. integrations.tf names "the 14 existing scoped routes".
- The authorizer is REQUEST type with simple responses and identity source `$request.header.Authorization`
  (shared-infra/apigateway-portal/main.tf:43-51). Result TTL is not set. Live get-authorizer returned
  ttl null.
- The page also loads its SPA assets through CloudFront (V3's viewer-request).

## (d) Signing key, rotation, separate render key

Key storage:
- The private key is in `opal/auth/jwt-private-key` (jwt.ts:8).
- The public key is in `opal/auth/jwt-public-key` as a two-slot {current, previous} envelope with no
  kid (jwtPublicKeys.mjs:57, :84-115).
- Verifiers cache it for 300s (:65) and try current then previous (verifyWithSlots :216-232). The
  signer reads current only (:170).
- The shared module is vendored byte-identically into auth-handler/src/lib/authkeys (sha c479b353...).
- Rotation is therefore two-slot overlap with a 5-minute cache, which is compatible with render TTLs
  of minutes.

Shared vs separate key:
- **Shared key** is cheapest: no new secret loads. Safety then rests entirely on aud scoping, and
  today V3 does NOT check aud. A render token signed with the portal key is accepted at the edge on
  its claims until V3 changes.
- **Separate key** (`opal/auth/irpt-render-jwt-{private,public}-key`) means a leaked or mis-scoped
  render token FAILS SIGNATURE at every verifier that never loads that key. That is structural
  default-deny across V1 and V4-V7, including any consumer this census missed. Only V2 and V3 need a
  second key load, and verifyWithSlots already takes the slots as a parameter, so it is one more
  getJwtKeySlots-style call per accepting verifier.
- It also keeps the render job's EC2 role off the portal private key. Minting with the shared key
  would require granting the runner read on the key that mints ADMIN tokens for every user.
  **That is the decisive point: a runner holding the portal private key can mint any human's token.**

## (e) Risks and design

- **Replay/TTL.** Set exp = 5 min and nbf/iat with 30-60s clock-skew leeway. One jti per render. Bind
  the render id and the (tenant, bundle, revision) in claims.
  - A jti is only replay-proof with a server-side seen-set. That is not needed if the TTL is short
    and the token is narrow, but it is recommended for the audit trail: log jti + render id at V2/V3
    on every accept.
- **Leaked-token blast radius.**
  - If minted with the SHARED key today, a leak reaches every CloudFront path V3 guards with the
    token's claims, and every API behind V2 whose handler trusts headers. Blast radius = whatever
    role/firmId the token claims.
  - With a SEPARATE key + aud + a route allowlist in V2 and V3, the radius is 3 GETs for one
    tenant/bundle for <=5 minutes.
- **Server-side enforcement.** ProtectedRoute is frontend-only and enforces nothing. Scope must be
  enforced in V2 by routeKey (the event carries routeKey), and in V3 by URI.
- **Authorizer caching.** Keep the TTL at 0. If caching is ever enabled with an Authorization-only
  identity source, one allow decision is reused across routes; add routeKey to the identity source if
  so.
- **FIRM_BINDING tension (UNRESOLVED).**
  - IRPT handlers take the firm ONLY from edge-injected X-Firm-Id and refuse a disagreeing
    body/query/path firm (investor-reporting/_authz/served.py:24-27, :34-40; enforce.py FirmBinding
    :28-35, :156-177).
  - The frontend requireInternal demands firmId 'opal-capital'.
  - So a render token whose firmId is the TENANT fails requireInternal, and one whose firmId is
    opal-capital may fail FIRM_BINDING for a tenant bundle.
  - How an internal user prints another firm's report today was NOT resolved here. The PRD addendum
    must state it.

## RECOMMENDATION

Option 2 with a SEPARATE render signing key, aud `irpt-render`, TTL <=5 min, a jti = render id, and
tenant/bundle/revision claims. The render job mints via a small minter; it never reads the portal
private key.

Verifiers that MUST ACCEPT it, scoped:
- **V2 portal-authorizer**: load the render public key; admit aud irpt-render ONLY when routeKey is
  one of the 3 GETs in (c) and the path ids match the claims; otherwise deny (it is default-allow
  today, so this must be an explicit branch). Keep the authorizer TTL at 0.
- **V3 auth-validator-edge**: admit the render key only for `/investor-reporting/print` + SPA assets
  + the 3 API paths. Separately ADD an aud check (`opal-portal-api`) on the existing path. It checks
  none today, which is a standing gap regardless.
- **Frontend**: ProtectedRoute needs a render-claim branch for :576 only. This is cosmetic, not a
  control.
- **IRPT handlers**: re-assert the scope as defence in depth, and resolve FIRM_BINDING for the
  render identity.

Verifiers that MUST REFUSE it:
- V1, V4, V5, V6 and V7. They refuse it with no code change, twice over: wrong key AND wrong aud.

Option 1 comparison, in one line: a standing credential with no expiry and full admin/internal reach
behind a password in a secret. It is strictly larger blast radius and not auditable per render.

## What this note did NOT verify

- The live deployed bytes of V2/V3 (repo source only) and the live CloudFront behaviours.
- Live consumers of opal_auth (V5): the importer search returned only itself.
- CI / ui-smoke / Playwright auth stubs as existing machine identities.
- How cross-firm internal prints satisfy FIRM_BINDING today.
- Whether any handler behind naqxlm authorizes on X-User-Role alone, which widens the shared-key case.
- The exact aud-mismatch behaviour of each library at runtime (inferred from the options passed, not
  exercised).

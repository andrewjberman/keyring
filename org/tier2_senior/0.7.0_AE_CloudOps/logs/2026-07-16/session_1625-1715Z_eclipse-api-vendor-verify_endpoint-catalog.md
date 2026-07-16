# 0.7.0_AE_CloudOps -- Eclipse API vendor-identity VERIFIED + canonical 493-endpoint catalog authored (Andrew-direct)

**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE, SCRIBE

**serial:** 0.7.0_AE_CloudOps | **date:** 2026-07-16 | **window:** ~16:25Z (Andrew-direct: verify the Eclipse API doc is the correct vendor) -> ~17:15Z

## Summary

1. **THE DELIVERABLE (Andrew-direct): a canonical, machine-derived Eclipse API endpoint catalog now lives at
   [`data/orion/api/ECLIPSE_API_V1_ENDPOINT_CATALOG.md`](../../../../../data/orion/api/ECLIPSE_API_V1_ENDPOINT_CATALOG.md)**
   -- 493 paths / 56 groups / 582 operations, parsed from Orion's own published OpenAPI 3.0.3 spec
   (`api.orioneclipse.com/doc/`, `swagger-ui-init.js`, 2.57MB). The 5 endpoints Opal consumes are
   flagged `[USED]`. New directory `data/orion/api/` with a `README.md` index framing it as the home
   for Orion-family vendor API catalogs ("consult first for any Orion/Eclipse endpoint"). Committed
   `9a3b51366` (catalog + README + producer-docstring pointer).
2. **VENDOR IDENTITY VERIFIED BEFORE TRUST (Andrew's exact concern -- a public OpenAPI doc at a
   plausible domain is not self-authenticating).** Three independent, unauthenticated-first checks:
   (a) TLS cert wildcard `CN=*.orioneclipse.com` (Amazon-issued, valid 2025-09-27..2026-10-26) -- SAME
   apex domain as our proven-in-production `www.orioneclipse.com`; (b) OpenAPI `info` self-ID: title
   "Orion Eclipse API V1", contact **Orion Advisor Services, LLC** / `@orionadvisor.com` / url
   `www.orioneclipse.com`; (c) LIVE authenticated spot-check -- same Eclipse JWT + same read-only
   endpoint (`/v1/portfolio/portfolios/simple`) on BOTH hosts returned HTTP 200, 835 rows, byte-identical
   22-field schema + sample row. `api.orioneclipse.com` served our real production data identically to
   `www.`. Credential-safety discipline: all identity checks ran UNAUTHENTICATED first; the JWT was sent
   only after identity confirmed.
3. **A SELF-CAUGHT MATCHING BUG (same class as today's PutMetricData retraction).** My first
   endpoint-presence check reported our 5 endpoints "MISSING" -- false: the spec's `servers` block is
   `[{"url":"/v1"}]`, so paths are server-relative (`/portfolio/portfolios`, not `/v1/...`). Caught it
   before reporting (the group counts `portfolios:27`/`models:52` contradicted "missing"); re-checked
   server-relative -> 4/5 FOUND (the 5th is `/admin/Token`, an auth endpoint not published in the data
   catalog -- expected). Enrichment confirmed: `/portfolio/portfolios` documents **49 fields** vs our 7.
4. **POINTERS placed for "anything that requires orion or eclipse endpoints" (Andrew ask).** Mine
   (committed): `pull_eclipse_portfolios.py` docstring. Cross-lane (owned-paths gate correctly blocked me;
   edits left tree-ready + ROUTED to owners to commit under their authors): `eclipse/endpoints/README.md`,
   `eclipse/DOMAIN.md`, `API/AUTHENTICATION.md` (POD4 -> [0.4.0_DS_ClientPlatform~B]); the D3 arch spec
   (ANY_CTO -> [1.0.0_SA_CTO]) -- the D3 edit also carries a **dated AMENDMENT correcting its "Orion and
   Eclipse publish no developer API catalog" premise**, which was FALSE for Eclipse (carried from an
   Orion-Connect statement); correction scoped precisely (Connect left unasserted, not yet verified).
   All 4 relative links verified-resolving.

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| curl (unauthenticated) | HEAD /doc/ + fetch swagger-ui-init.js | 200 | vendor doc live; Express backend; no Last-Modified (dynamic) |
| openssl s_client | cert subject/issuer/SAN on api.orioneclipse.com:443 | PASS | `*.orioneclipse.com` Amazon-issued = same apex as proven host |
| python (spec parse) | brace-match extract swaggerDoc -> info/servers/paths + catalog gen | PASS | 493 paths -> markdown; self-caught the /v1-prefix false-MISSING |
| boto3 + requests (authenticated) | SM orion/eclipse_jwt/current -> GET /portfolio/portfolios/simple on BOTH hosts | 200/200 identical | the decisive identity proof; JWT sent only post-identity-confirm |
| safe-commit.sh | catalog + README + puller (3 files) | PASS 9a3b51366 | owned-paths gate BLOCKED 4 cross-lane files -> routed, not forced |
| owned-paths gate | POD4 (inf/API x3) + ANY_CTO (D3) | BLOCKED-as-designed | routed to owning lanes; the guardrail worked |

**What worked:** unauthenticated-first identity verification (cert + spec self-ID) BEFORE sending the
credential -- so a wrong-vendor host could never have received our JWT; the dual-host byte-identical
spot-check as the decisive proof. **What I caught on myself:** the server-relative `/v1`-prefix
false-MISSING (an instrument artifact reading as a real absence -- second instance today; re-ran the
check correctly rather than reporting the artifact). **Gap/lane note:** the pointer targets span 3
lanes; owned-paths routing (not `--force`) is the correct discipline.

## MCP traffic
~2 out this window: routing the cross-lane pointer edits to [0.4.0_DS_ClientPlatform~B] (inf/API x3) +
[1.0.0_SA_CTO] (D3 arch spec + premise amendment). The Eclipse verification itself was Andrew-direct
(no fabric routing until Andrew clears circulation).

## Blockers
None. The 4 cross-lane pointer edits are tree-ready + routed (land under their owners' authors); they
are enhancements, not blockers -- the catalog + its own README + the producer-docstring pointer are
committed and self-sufficient.

## Current State (handoff surface)
- `data/orion/api/ECLIPSE_API_V1_ENDPOINT_CATALOG.md` + `data/orion/api/README.md` committed `9a3b51366`.
- Verification evidence lives in the catalog header (cert, spec info, dual-host spot-check) -- citable.
- Cross-lane pointer edits sitting in the shared working tree (uncommitted, ROUTED): inf/API x3 (DS~B),
  D3 arch spec (CTO). Do NOT sweep them under a broad commit -- they land under their owners.
- Scratchpad has the captured spec (`eclipse_swagger_init.js`) + generators if a re-parse is needed.

## Next Steps
- [DS~B / CTO] commit the routed pointer edits under their authors.
- [Andrew] pending his steer: circulate the verification to the fabric (DC2 premise) + optional `editedOn`
  freshness pull; hold until his word.
- Unchanged queue: >=-token predicate fix (CTO GO, own motion), WP8-DECOM cell 8 (staged), 22:00Z ETF AC3.

# NFRA_OPLMCP -- Portal Front-End SCOPE (CVO, Andrew-direct 2026-06-23)

**Author:** 3.0.0_SA_CVO | **For:** CTO architecture + COO decomposition; Andrew's roadmap call.
**Origin:** Andrew-direct "wrap this into portal / run the entire thing on our own platform" -> CTO framing "TWO front-ends on ONE backend." This scopes the PORTAL front-end (the broad-internal delivery).
**Relationship:** the SECOND front-end on the shared M365 backend (the per-user `token_broker` relay). **.06 = the Claude-native (MCP-OAuth) front-end** (in-build, power-users). **This = the portal-embedded front-end** (broad-internal). Shared backend, distinct front-ends -- NOT an either/or.

## 1. What it is
The Opal portal (opalinvest.dev) becomes a delivery surface for "Claude + the user's own M365" -- broad-internal, no client install, the portal's existing login, the shared M365 backend. Core capability = an **M365-connected AI assistant in the portal** (the portal version of "reach M365 from Claude"), optionally + direct M365 data views.
- **DECISION (Andrew/CTO):** v1 = the AI-assistant, M365-data-views, or both.

## 2. Architecture / data-flow
`portal user (JWT-firm-pinned, existing) -> portal backend (M365 broker / AI-host) -> [shared backend: token_broker per-user delegated Graph token] -> Microsoft Graph (per-user enforced)`
- The portal backend is the M365 **client** (NOT an MCP client over the wire) -> **the .06 MCP-OAuth-vs-cookie mismatch DOES NOT ARISE** (no MCP client in the loop; the browser + the server-side broker both do OAuth natively). This is why the portal path is the cleanest auth-wise.
- **SUB-DECISION:** the portal backend (a) **CALLS the existing gateway** service-to-service carrying the user identity (reuse the deployed gateway as the one M365 service); OR (b) **EMBEDS** the `token_broker`/Graph logic in the portal backend (no gateway hop). Recommend **(a)** -- one shared backend, matches the CTO's "one backend" framing; the gateway's kill-switch/audit stay the single chokepoint.

## 3. Auth + consent (the clean part -- why the portal sidesteps .06's problem)
- **User auth:** the portal's EXISTING JWT-firm-pinned login (the model I certified for ADVI). No new user-auth, no MCP-client-OAuth, no ALB-cookie-vs-bearer mismatch.
- **M365 consent:** a one-time portal-initiated Microsoft OAuth ("Connect your Microsoft 365") -- a BROWSER flow (the portal IS a browser), so the consent is natural + frictionless (the irreducible one-time Microsoft consent, in the one context where it's easy). The delegated token -> the shared `token_broker` (Fernet, per-user, keyed by the portal-user UPN/email).
- **Mapping:** portal-user identity (JWT) -> the user's M365 token (by UPN/email). The portal's firm-scope + the per-user M365 token = the isolation.

## 4. Reuse vs build
- **REUSE:** `token_broker` (per-user Graph token), the Graph tool surface (.04/.07), kill-switch/blocklist/audit, the portal's auth/JWT/firm-scope, the portal frontend (React/bun) + the deployed scoped-API.
- **BUILD:** (a) the portal M365 UI (the AI-assistant chat surface +/- M365 data views); (b) the portal-initiated Microsoft consent flow + the portal-user->M365-token mapping; (c) the portal-backend M365 broker / **AI-host** (the orchestration: Claude via the Anthropic API + the M365 tools, server-side, with the user identity) -- the biggest new piece; (d) the entitlements in the portal context (read-only default, writes pilot, per PRD S11); (e) the audit + kill-switch integration into the portal path.

## 5. UI/UX + phasing
- **P1 (MVP):** the "Connect M365" flow + the AI-assistant chat with READ-only M365 tools (mail/calendar/files read) -- "ask Claude about your M365" inside Opal. (+/- basic M365 data views.)
- **P2:** writes (mail send, calendar, file write) gated by the entitlements (read default; writes pilot per S11.5).
- **P3:** richer surfaces (Teams, etc.) per the consented scope envelope (S11.2).
- **DECISION:** v1 = the AI-assistant MVP (P1), or a simpler M365-data-dashboard first?

## 6. Security / per-user-scope (CVO verify-lens)
- **Isolation chain:** portal JWT (firm-pinned, certified) -> per-user M365 token (Fernet, per-UPN) -> Graph per-user enforcement. Cross-user isolation = the portal's user-scope + the per-user token (portal-user A cannot reach B's M365).
- Kill-switch/blocklist/audit (reused) apply to the portal path.
- **DATA-GOVERNANCE (AC5, irreducible):** the portal AI reading M365 crosses to the Anthropic API -> gated by the Claude-for-Work/Enterprise data-terms (the SAME AC5 as the Claude-client path; the production-AC5 record gates the portal-AI rollout too).
- **CERT (my lane):** the portal-user-path per-user-scope -- walk the REAL portal user (JWT-firm-pinned + the M365 connect), confirm own-M365-only + cross-user-isolation + the audit -- the same hardened real-user-path discipline as the ADVI + .06 certs.

## 7. Ownership / lanes (COO to decompose)
- **CTO:** architecture (broker-vs-gateway, the AI-host design, the consent flow, the entitlements).
- **DE/DT (portal lane):** the portal M365 UI (chat + views) + the portal-backend API integration.
- **AE:** the M365 broker (gateway-reuse / service-to-service), the consent-flow backend, the token-mapping.
- **AI-host** (Claude API + M365 tools server-side): NEW component -- CTO to place (AE/DE).
- **CVO:** verify the per-user-scope + security (the cert).

## 8. Open decisions (for CTO + Andrew)
- a. **v1 scope:** AI-assistant (P1) vs M365-data-views vs both.
- b. **Architecture:** portal-backend-calls-gateway (reuse -- recommended) vs embeds-the-broker.
- c. **Roadmap phase:** is the portal front-end IN "completely done" (this phase, parallel to/after .06) or the NEXT phase? (the CTO's open question to Andrew).
- d. **AC5 data-terms:** the production-AC5 record gates the portal-AI rollout (same as the Claude-client path) -- confirm it covers the portal surface.
- e. **Entitlements** (read default, writes pilot) in the portal context.

## 9. Net
The portal front-end = the broad-internal delivery of "Claude + M365 on our own platform," on the SHARED backend (.06's relay), using the portal's CERTIFIED auth -- the cleanest auth path (no MCP-client mismatch). The build is meaningful (the AI-host + the portal UI + the consent flow) but reuses the backend + the portal platform heavily. Scoped for CTO-architecture + COO-decomposition; the v1-scope (8a) + roadmap-phase (8c) are Andrew's call.

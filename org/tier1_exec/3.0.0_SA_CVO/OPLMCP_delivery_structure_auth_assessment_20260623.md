# NFRA_OPLMCP -- Delivery-structure + auth-layer ASSESSMENT (CVO -> CTO)

**Author:** 3.0.0_SA_CVO | **2026-06-23** | **For:** 1.0.0_SA_CTO (architecture owner) decision; cc COO (in-flight .02 close).
**Origin:** Andrew-direct -- assess the delivery structures (Claude Code/TUI, Claude Desktop/GUI, portal/dashboard on our platform) + the auth layer; "initially imagined a TUI PowerShell solution for employees, but we will want to figure out how to wrap this into portal."
**Anchor:** a verified finding that the deployed .02 access layer does NOT fit a native MCP client. This reshapes the delivery + auth architecture and bears on the in-flight .02 close. grounding inline.

## 0. RECONCILIATION with the in-flight OPLMCP.06 (READ FIRST -- post-draft update)
After drafting, I read .06/Model-B + the CTO drive-to-done. **OPLMCP.06 "connect-path" (Model-B: the gateway as a full OAuth-AS FACADE -- `/.well-known/*` + `/register` DCR-facade + `/authorize` bridging to Entra + `/token` + Bearer-on-`/mcp` + an ALB path-rule bypassing OIDC for `/mcp`) is the IN-BUILD fix for structures A/B** -- CTO-signed-off FINAL, AE building (the G-directives), ETA 2-3d. Therefore:
- The A/B "needs an MCP-OAuth re-arch" conclusion below is **NOT a new recommendation -- it is already the active, signed-off plan.** My independent spec-grounding CORROBORATES the diagnosis + Model-B (same direction); the .06 brief is in fact DEEPER -- the precise Model-A blockers (Claude Code IGNORES static client_id + ALWAYS attempts DCR/RFC7591 + Entra rejects DCR AND the http-loopback redirect) are what force the gateway-as-AS, which I had not enumerated. Net: .06/Model-B is correct; this assessment confirms the direction and proposes NO change to it.
- **Standing value of this doc:** (a) that independent confirmation (pre-deploy, security-critical); (b) **STRUCTURE C (the portal) -- the strategic delivery track .06 does NOT cover** (Andrew's wrap-into-portal); (c) the cert-rebase, already in the CTO drive-to-done (I cert AC2/3/4 + re-verify the entry-point POST-.06 on the REAL client -- which closes the proxy-cert gap).

## 1. THE FINDING -- the deployed ALB-cookie-OIDC fits BROWSERS, not native MCP clients
grounding: SOURCE-CONFIRMED (MCP spec + live ALB + gateway code):
- **MCP's HTTP transport authenticates with OAuth 2.1 BEARER tokens** (MCP Authorization spec 2025-11-25, fetched): client expects `401 + WWW-Authenticate -> Protected-Resource-Metadata (RFC 9728) -> OAuth 2.1/PKCE`, then `Authorization: Bearer <token>` on every request ("MCP client MUST use the Authorization request header... Bearer"; "invalid/expired tokens MUST receive a 401"). No cookies in the model.
- **The live ALB returns `302` -> login.microsoftonline.com** for an unauthenticated request (curl-confirmed) + `AWSALBAuthNonce`/`AWSELBAuthSessionCookie` -- a browser cookie flow, NOT a 401-with-OAuth-metadata.
- **The gateway exposes no MCP-OAuth discovery** (`/.well-known/oauth-protected-resource`); it delegates auth wholly to the ALB + reads `x-amzn-oidc-data` (identity.py).
=> A spec-compliant MCP client (Claude Code CLI; Claude Desktop custom connectors) cannot turn the ALB's 302/cookie into a bearer token -> **cannot authenticate.** Confirmed at the protocol level (the spec + the live behavior are incontrovertible). Empirical clincher (recommended, ~30s, and it IS the real-user-path test per the COT render-cert lesson): `claude mcp add --transport http m365 https://mcp.opalinvest.dev/mcp` -> observe the auth fail.

## 2. THE IRREDUCIBLE PIECE (common to every structure)
Each user does a ONE-TIME Microsoft Entra consent to mint their per-user **delegated** Graph token. Microsoft only issues it after the user authenticates to Microsoft + consents; a Claude/Anthropic session cannot produce a Microsoft token (different identity systems). After that: silent (refresh tokens). The per-user delegated-token broker + Graph's per-user enforcement (the security core, audit F0) are SOUND and reusable across all structures.

## 3. THE THREE STRUCTURES

| Structure | User auth | M365 brokering | Fit w/ deployed .02 | Effort | UX |
|---|---|---|---|---|---|
| **A. Claude Code / TUI** (Andrew's original) | MCP-native OAuth 2.1 bearer | gateway, per-user delegated token | NEEDS CHANGE: gateway must become an MCP-OAuth resource server | MED-HIGH | `claude mcp add` -> 1x browser consent -> silent bearer |
| **B. Claude Desktop / GUI** | same MCP-OAuth | same gateway | NEEDS CHANGE (same as A) | rides A's gateway work | Connectors->Custom->URL -> 1x consent (Desktop opens browser natively, smoother) |
| **C. Portal / our platform** (the "wrap") | the PORTAL's own login (JWT-firm-pinned, BUILT + ADVI-certified) | portal backend brokers server-side | FITS: sidesteps MCP-client auth entirely | MED | log into portal (already do) -> "Connect M365" 1x -> mail/files/AI in-portal |

### A/B -- the MCP-native-OAuth re-architecture
- Gateway becomes an OAuth 2.1 **resource server**: implement RFC 9728 PRM + the 401 challenge + bearer-token validation (audience-bound to the gateway, per the spec's audience rule).
- The authorization server **can REUSE Entra** -- restructure App-1 from an ALB-OIDC-login app into an MCP-resource OAuth app; the MCP client gets an Entra bearer for that resource, the gateway validates it -> user identity -> the existing per-user Graph token-broker for Graph. NOT a new IdP -- a gateway-side + App-1-restructure change (exact token mechanics = CTO/AE to spec; the spec forbids token-passthrough, so the MCP-access token != the Graph token).
- The ALB `authenticate-oidc` action is REMOVED (ALB -> plain HTTPS forward).
- A + B share the SAME gateway change; B is the GUI variant (smoother consent). NOTE: Claude Desktop custom-connector remote-MCP-OAuth is Team/Enterprise-tier -- confirm availability.

### C -- the portal wrap
- The user is already authenticated to the portal (the JWT-firm-pinned model certified for ADVI). NO MCP client in the loop.
- The portal backend brokers M365 server-side: a one-time portal-initiated Microsoft consent (mint the delegated token) -> the backend calls Graph reusing the gateway's token-broker + controls (or the gateway as a server-side-called service carrying the portal-user identity).
- If an in-portal AI assistant is wanted: the portal backend is the MCP HOST (Claude via API + the M365 tools, called server-side with the portal-user identity) -- the gateway becomes a backend service, not a client-facing MCP endpoint.
- "The entire thing on our own platform": unified UX, no client install, no separate auth, the portal's existing per-user/firm-scope + audit.

## 4. WHAT .02 BUYS REGARDLESS (not wasted under any structure)
Reused everywhere: the per-user delegated token-broker (Fernet, per-user, sha256-keyed), the kill-switch/blocklist/audit middleware, the EC2/Terraform/Secrets-Manager infra, the 2 Entra apps, the Graph tool surface (.04/.07). What changes is ONLY the ACCESS LAYER (the ALB `authenticate-oidc`) -- the one piece that doesn't fit MCP clients.

## 5. .02 IMPLICATIONS (time-sensitive -- the in-flight close)
- The .02 "grounded-done" + Andrew's-ping assume the design works for the intended USERS (Claude Code employees). The finding says the Claude Code path does NOT work yet -> the "live for users" premise is FALSE (it's live for a browser). The grounded-done should NOT proceed on that premise.
- The AC2 cert as planned (~B drives a Playwright BROWSER -> ALB cookie -> /mcp) tests a path no real Claude Code user travels -> it would FALSE-PASS (the COT empty-page proxy-cert class). The AC2 cert must re-base on the REAL chosen path.

## 6. RECOMMENDATION (for CTO decision)
- **Primary = the Portal wrap (C):** cleanest auth (no MCP-client mismatch), unifies on the Opal platform, leverages the BUILT + certified portal auth, "our own platform" per Andrew. Best for the broad internal rollout.
- **Secondary = the MCP-OAuth gateway (A/B):** for the Claude-native power-user/employee crowd; requires the gateway-as-MCP-OAuth-resource-server re-architecture (reuses Entra + the token-broker). A + B share the work.
- **The deployed ALB-cookie-OIDC = pivot:** it fits neither MCP-client path; replace per the chosen structure (MCP-OAuth for A/B; portal-auth for C). The rest of .02 carries forward.

### DECISION POINTS for the CTO
1. **Empirical clincher:** run the Claude-Code-connect test to confirm the finding to the ground (I or ~B can run it).
2. **The fork:** C-primary + A/B-secondary (recommended) / A/B-only / C-only?
3. **.02 disposition:** pause the grounded-done claim; re-base the AC2 cert on the real path; re-scope the access layer.
4. **Re-scope OPLMCP** (the access-layer sub-stream + the delivery structures) per the decision.

-- 3.0.0_SA_CVO

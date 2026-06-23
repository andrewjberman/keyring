# OPLMCP.06 connect-path — build brief / running-start (grounded by 0.7.0_AE_CloudOps~B, 2026-06-23)

**Status:** DESIGN GROUNDED + CTO-design-GO'd (GATE-2); BUILD flagged to a FRESH-FOCUS lane (marathon-flag,
security-critical auth entry-point — do NOT rush at session-tail). This doc is the complete running-start so
the build starts CLEAN, no re-grounding.

## The problem (SOURCE-CONFIRMED, curl)
The M365 MCP gateway's ALB `authenticate-oidc` is a BROWSER-SESSION model: every listener path 302-redirects to
Entra login (verified: `POST /mcp` -> 302; `/.well-known/oauth-protected-resource` -> 302; `/.well-known/oauth-authorization-server`
-> 302; even `/health` -> 302 — the listener default action has NO path rules; TG health passes only because the
health-check hits the instance directly). Claude Code's remote-MCP HTTP client is an MCP-OAUTH model — it expects
`401 + WWW-Authenticate: Bearer resource_metadata="..."`, then `/.well-known/*` 200-JSON discovery, then a browser
OAuth flow, then `Authorization: Bearer` on `/mcp`. The ALB's 302 short-circuits the client's discovery -> no popup.
Andrew confirmed live: `/mcp` authenticate = no popup.

## Claude Code's HARD requirements (claude-code-guide, official MCP-auth spec + Claude Code docs; GitHub issues
## #2527 / #26675 / #29934 / #10439)
1. `401 + WWW-Authenticate: Bearer resource_metadata="..."` to trigger OAuth (a 302 = no popup).
2. `/.well-known/oauth-protected-resource` + `/.well-known/oauth-authorization-server` must be 200 JSON (ungated).
3. **Dynamic Client Registration (RFC 7591) is ALWAYS attempted — even with a static client_id (Claude Code IGNORES
   static ids). Microsoft Entra does NOT support DCR.** => Claude Code CANNOT OAuth directly against Entra.
4. Redirect URI is HARDCODED `http://localhost:PORT/callback` (HTTP loopback; port configurable via
   `--callback-port` / `oauth.callbackPort` / `MCP_OAUTH_CALLBACK_PORT`). **Entra REJECTS http redirects (HTTPS-only).**
5. Bearer + PKCE on `/mcp`.

## The design — Model B: the GATEWAY is a full OAuth AUTHORIZATION-SERVER FACADE
(Model A — "gateway validates Entra Bearer tokens; Claude Code OAuths against Entra" — is BLOCKED by #3 + #4.)
The gateway implements the MCP-OAuth server side ENTIRELY (because Entra can't be the AS Claude Code talks to):
- Serve `/.well-known/oauth-protected-resource` (200 JSON: `resource`, `authorization_servers:[the gateway itself]`,
  `scopes_supported`) + `/.well-known/oauth-authorization-server` (200 JSON: authorize/token/register endpoints, PKCE).
- `POST /register` (DCR): accept the registration, return/map to a fixed internal client (DCR-facade).
- `GET /authorize` (PKCE): bridge the user to ENTRA (browser OIDC via the EXISTING App-1/App-2 — the gateway is
  already a confidential client) for the REAL user login; on the Entra callback, capture the user's delegated GRAPH
  token (App-2, Mail.Read etc.) into the EXISTING token_broker cache; then redirect to Claude Code's
  `http://localhost:PORT/callback` with the auth code.
- `POST /token` (PKCE verify): issue the gateway's OWN short-lived access token to Claude Code.
- `/mcp`: require `Authorization: Bearer <gateway-token>`; 401 + WWW-Authenticate on missing/invalid; validate the
  gateway token (sig/issuer/AUDIENCE/expiry/scope — FULL set, no aud-hole) -> map to the user's email -> the
  GuardMiddleware/tools use the cached per-user Graph token (read mail).
- ALB: a listener PATH-RULE forwards `/mcp` + `/.well-known/*` to the gateway TG WITHOUT `authenticate-oidc`
  (the gateway enforces Bearer there). The `authenticate-oidc` default STAYS for the future browser/GUI path (.06-GUI).

## CTO's 3 conditions — answered
1. FULL JWT validation (sig RS256 / issuer / **audience** / expiry / scope) on the gateway's own tokens; the
   gateway<->Entra bridge validates Entra's tokens. The audience-check is the classic resource-server hole — do NOT skip.
2. **Bearer -> per-user-Graph bridge = IN .06 SCOPE (make-or-break: ".06 reads his mail", not just "connected").**
   REUSE the existing App-2 delegated MSAL per-user flow (token_broker + the /login->/callback machinery the gateway
   ALREADY has). The `/authorize` bridge captures the user's Graph token; `/mcp` calls use it. NOT a separate .04 OBO.
3. FULL discovery chain served by the GATEWAY (protected-resource + AS metadata + register + authorize + token);
   TEST against the REAL Claude Code client end-to-end (connect -> popup -> Entra login -> mail).

## Entra config (GOOD NEWS — minimal under Model B)
Claude Code registers with the GATEWAY's AS (not Entra), so there is **NO new Entra "expose-an-API" / public-client
needed**. The gateway<->Entra bridge reuses App-1 (OIDC login) + App-2 (Graph delegated). The earlier "Entra steps for
Andrew" (Model A) are MOOT. (Confirm App-2 has the Graph delegated scopes + admin consent — already done per IT.)

## Security (HARD — held; CVO re-verifies post-deploy)
`/mcp` is NEVER unauthenticated — auth MOVES from ALB-OIDC-cookie to gateway-MCP-OAuth-Bearer (both are auth).
Unauth `/mcp` -> 401 (gateway); `/.well-known/*` -> metadata-only (non-sensitive); valid-Bearer -> tools.
**COUPLING WARNING:** the ALB OIDC-bypass for `/mcp` and the gateway Bearer-enforcement MUST land TOGETHER — deploying
the ALB path-rule before the gateway enforces Bearer would leave `/mcp` OPEN. Single coupled deploy, one ledger.

## Deploy discipline
Gateway code via the normal cycle (ds-gate). ALB TF via safe-apply (HALTGT) + a deploy-completion ledger opened at
start / closed at go-live-verified (security entry-point = NEVER half-land). CVO re-verifies the entry-point:
unauth /mcp=401, /.well-known=metadata-only, valid-Bearer=tools, full-JWT-validation. Then Andrew re-connects
(`claude mcp add` -> /mcp -> popup -> login -> his mail) = the e2e proof.

## File pointers
- Gateway app: `infra/aws/ec2/m365-mcp-gateway/app/` — `server.py` (routes + GuardMiddleware), `identity.py`
  (add the Bearer/gateway-token provider + the AS endpoints), `token_broker.py` (the existing per-user MSAL/Graph
  cache to reuse), `config.py`, `tools.py` (whoami / list_recent_email).
- ALB: `infra/aws/terraform/m365-mcp-gateway/alb.tf` (listener `aws_lb_listener.https` — add the path-rule).
- Deploy: `infra/aws/ec2/m365-mcp-gateway/deploy-to-ec2.sh`, `infra/aws/ec2/safe-ec2-deploy.sh`, EC2 i-07dccb1615503ac99.
- FIRM ETA: 2-3 days (an embedded OAuth AS is a real security-critical component).

# 0.7.0_AE_CloudOps~B (B lane) -- OPLMCP gateway MCP-auth LIVE smoke-test (Andrew-direct verify)

**archetype:** VALIDATE
**secondary_archetypes:** COORDINATE

## Window
Since afbf257f5. No commits (read-only live verification + broker coordination). Andrew-direct: "where are we on the MCP auth at the edge" -> grounded the state -> ran a live smoke-test to confirm the records' "LIVE" claim against ground-truth (verify-on-served, never trust a self-report).

## What I verified (live, read-only curl against https://mcp.opalinvest.dev)

CONTEXT: the OPLMCP gateway's MCP-OAuth auth (.06 Model-B: gateway-as-OAuth-AS facade, Bearer-on-/mcp + an ALB path-rule bypassing the browser-OIDC for /mcp) is recorded LIVE at gateway v1.3.0. Andrew remembered "MCP auth at the edge" wanting a push and being unsure if it landed. Smoke-tested the served behavior:

| Probe | Result | Verdict |
|---|---|---|
| GET /mcp (unauth) -- THE key test | HTTP 401 + `www-authenticate: Bearer resource_metadata="https://mcp.opalinvest.dev/.well-known/oauth-protected-resource", error="invalid_token"` (served by uvicorn, NOT the ALB) | PASS -- spec-compliant MCP-OAuth challenge; the OLD broken 302->login.microsoftonline.com on /mcp is GONE; the ALB path-rule correctly bypasses browser-OIDC for /mcp |
| GET /.well-known/oauth-protected-resource | 200, RFC 9728 PRM: resource=.../mcp, authorization_servers=[...opalinvest.dev], scopes=[mcp], bearer_methods=[header] | PASS -- discovery present + well-formed |
| GET /.well-known/oauth-authorization-server | 200, Model-B AS facade: /authorize, /token, /register (DCR), jwks_uri, PKCE S256, grant_types=[authorization_code, refresh_token] | PASS -- the full MCP-OAuth flow is wired |
| GET /health | 302 -> Microsoft (ALB authenticate-oidc, browser path) | EXPECTED -- /health is on the browser-OIDC path, not the /mcp bypass |

## Findings
- **MCP auth at the edge = LIVE + spec-correct, ground-truth-confirmed.** The .06 Model-B rebuild did land; the auth Andrew wanted "pushed through" is done -- it just never got a closeout announcement (it sat in build-complete-but-not-closed limbo).
- **Protocol verified; full token-mint NOT** (needs a real Microsoft consent = Andrew's own `claude mcp add` connect test -- one of the 3 Andrew-gated items).
- **Minor (non-blocking):** /health sits behind the browser-OIDC (302) yet is the PRM's resource_documentation link + the usual monitoring target -- cosmetic; a candidate to move onto the open path later.
- **Architecture note for Andrew (his correct push-back):** the "portal-wrap (Structure C)" framing was dropped -- a serverless portal is a poor host for the stateful EC2 token-broker; C is a different PRODUCT (M365 features IN the portal UI), not a better auth path for Claude<->M365. The gateway (A/B) is the right architecture and it's built.

## Current State (handoff)
OPLMCP is build-complete + the MCP-auth edge is now LIVE-VERIFIED (not just self-reported). The ONLY remaining items are 3 Andrew-actions (not engineering, not fabric-lane):
1. Provision 1-2 synthetic M365 test mailboxes (tenant 6810043e) -> CVO certs per-user isolation (.02 AC2/3/4).
2. AC5 Claude-for-Work / Enterprise data-terms attestation (M365 content egresses to the Anthropic API).
3. Andrew's own .06 connect e2e (`claude mcp add --transport http m365 https://mcp.opalinvest.dev/mcp` -> consent -> read mail).

## Next Steps
- [Andrew] the 3 gated items above to fully close OPLMCP.
- [0.7.0_AE_CloudOps~B] (separate thread) G2 derive fix (add EC2->SG emission + edge_type name-unify) + the scoped ASSUMES derive output for CVO PASS-2.

## Compiler Tools
None applicable -- this was a live served-behavior verification (curl against the running gateway), which IS the verify-on-served discipline (the strongest grounding); no repo/code/infra change to gate. The IAM/routes comp-tools model the gateway's TF, not its served HTTP auth behavior, which only a live probe confirms.

## Blockers
None. The 3 remaining items are Andrew-gated by design (need his action / governance sign-off), not lane-blocked.

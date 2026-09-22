# Claude for Financial Services -- MCP ENDPOINT DISCOVERY (unauthenticated), 2026-09-22 ~15:2xZ

**Seat:** `4.0.0_SA_CRO~F` (site Z). **Authority:** Andrew-direct 2026-09-22 ~14:5xZ at this terminal, step 1 verbatim
*"figure out the endpoint or if we have to download a MCP or whatever the case may be"* and step 2 *"Study the
MCP/endpoints"* (record `../ANDREW_DIRECT_20260922_145xZ_CLAUDE_FOR_FINANCE_RESAPP_RESEARCH_PROJECT.md`). **What was
sent:** for each of the 12 servers the core plugin declares, one `GET /.well-known/oauth-protected-resource` at the
origin, one at the declared path, and one unauthenticated MCP `initialize` POST (protocolVersion 2025-06-18, client
name `opal-endpoint-discovery`). **No credential, no Opal data, no security name, no payload beyond the handshake.**
Raw record: `mcp_endpoint_discovery_20260922.json` (this folder; HTML error bodies truncated to 200 chars, nothing else edited).

**Population:** the 12 `mcpServers` entries of `plugins/vertical-plugins/financial-analysis/.mcp.json` in
`anthropics/financial-services` @`574ed36` (2026-09-21 14:10:41 -0700), read from a clone, 12 of 12 probed. The two
partner plugins declare their own servers (LSEG `.../lfa/mcp/server-cl`, S&P `kfinance.kensho.com/integrations/mcp`);
the S&P one is the same URL as the core entry, the LSEG one is a sibling path NOT probed here.

| server | declared URL | `initialize` unauth | protected-resource metadata | authorization server(s) | scopes advertised |
|---|---|---|---|---|---|
| daloopa | `https://mcp.daloopa.com/server/mcp` | 401 + `WWW-Authenticate: Bearer resource_metadata=...` | root 200 | `https://mcp.daloopa.com` | (none listed) |
| morningstar | `https://mcp.morningstar.com/mcp` | 401 ("missing authorization") | root 200, path 200 | `https://mcp.morningstar.com/mcp` | `offline_access openid email profile` |
| sp-global | `https://kfinance.kensho.com/integrations/mcp` | 401 + `error="invalid_token"` | root 200, path 200 | `https://kfinance.kensho.com/integrations` | `kensho:app:kfinance offline_access` |
| factset | `https://mcp.factset.com/mcp` | 401 ("Authentication Failed") | root 200, path 200 | `https://auth.factset.com` | `openid mcp email`; bearer in header OR body |
| moodys | `https://api.moodys.com/genai-ready-data/m1/mcp` | 401 | root 200, path 200 | `https://api.moodys.com/genai-ready-data` | `mcp claudeai openid profile email mdcapp` |
| mtnewswire | `https://vast-mcp.blueskyapi.com/mtnewswires` | **404 Not Found** | root 200 (resource `https://vast-mcp.blueskyapi.com/`), path 404 | `https://mcp-auth-server-857389207619.us-central1.run.app/` | `user` |
| aiera | `https://mcp-pub.aiera.com` | 401 + `oauth_discovery_url=` | root 200 | `https://mcp-pub.aiera.com` | `openid profile email` |
| lseg | `https://api.analytics.lseg.com/lfa/mcp` | 401 + `resource_metadata=.../.well-known/oauth-protected-resource/lfa/mcp` | root 404, path 200 | `https://login.ciam.refinitiv.com` | (none listed) |
| pitchbook | `https://premium.mcp.pitchbook.com/mcp` | 401 + `resource_metadata=` | root 200, path 200 | `https://mcp.pitchbook.com` | `openid profile email offline_access` |
| chronograph | `https://ai.chronograph.pe/mcp` | 401 `missing_auth_header` | root 404, path 404 (Express "Cannot GET") | NOT DISCOVERABLE by RFC 9728 | -- |
| egnyte | `https://mcp-server.egnyte.com/mcp` | 401 + `resource_metadata=` | root 200 | `https://mcp-oauth.egnyte.com/egnyte-connect` | (none listed) |
| box | `https://mcp.box.com` | 401 `invalid_request` + `resource_metadata=` | root 200 (`resource_name: Box Model Context Protocol Server`) | `https://api.box.com/` | (none listed) |

**Read (measured, 12 of 12):** every server is a REMOTE Streamable-HTTP MCP server behind **OAuth 2.1 per the MCP
authorization spec** (RFC 9728 protected-resource metadata -> the vendor's own authorization server). Eleven of twelve
refuse the handshake with 401; ten of twelve publish resource metadata; **MT Newswires 404s at the declared path**
(the declared `/mtnewswires` path does not exist on that host today; the host's root metadata still answers);
Chronograph publishes no metadata and would need out-of-band OAuth configuration. **None accepts an API key at the MCP
layer** on the evidence here (Daloopa's docs say an `X-API-KEY` header alternative exists; not exercised).

**What this means for "where do we get access":** the plugin ships URLs, not access. Access = an OAuth grant against
EACH vendor's authorization server, which presupposes a subscription/account with that vendor (S&P names the
"LLM-ready API" subscription; FactSet/Morningstar/PitchBook/LSEG/Moody's are all entitlement-gated). The token is
per-user (Yang's login), obtained interactively in a browser -- exactly what the LLY pack's README says could not
happen in its non-interactive session.

**Not measured here:** `tools/list` (needs a token), rate limits, the Claude Enterprise/Cowork connector path (which
completes the same OAuth in the Claude UI), and whether Opal holds any of these subscriptions today (that is
Andrew's to answer; the Bloomberg terminal is the one paid data entitlement this seat can see in the estate).

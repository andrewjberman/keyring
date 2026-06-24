# M365 MCP gateway: connect-fix chain + full-envelope + Teams tools + /teams-assist re-architecture

**archetype:** DEPLOY
**secondary_archetypes:** DIAGNOSE, IMPLEMENT
**Session:** 2026-06-24 | **Agent:** 0.5.0_AE_OpalETL | **Andrew-direct** (live, in-session)
**Gateway:** m365-mcp-gateway (EC2 i-07dccb1615503ac99, mcp.opalinvest.dev) — base-AE's OPLMCP lane; I did all of this Andrew-direct + base-AE-looped per commit.

## Summary
Andrew's Claude Code couldn't connect the M365 MCP (a "request access" popup loop) despite IT having
granted admin consent. Took it from broken -> fully connected (read his live Outlook + Teams + sent a
Teams message) -> full consented scope envelope loaded -> Teams tools built -> the /teams-assist
monitor re-architected to the /watcher pattern. All grounded against source/live, never guessed
(especially the consent-exactness, after the Sites lesson).

## The connect-fix chain (3 stacked bugs, each hidden behind the prior — first end-to-end connect)
1. **Sites scope mismatch** (`8d3f089f9`): gateway requested `Sites.ReadWrite.All`; IT consented
   `Sites.Read.All` (Andrew's Azure screenshot = ground truth, NOT the ask-table). Microsoft consents
   EXACT scope strings -> the un-consented scope drove the request-access loop (same class as CVO
   154315Z on Mail, now on Sites). Fixed DOWN to `Sites.Read.All` (4-way pin: config.py default +
   .env.example + IT_REQUEST.md + consent). No IT round-trip.
2. **/mcp 307 redirect** (`e0f5c35c2`): Starlette `Mount("/mcp")` 307-redirects bare `/mcp` -> `/mcp/`
   and the Bearer drops on the hop -> 401 loop. GuardMiddleware now rewrites bare `/mcp` -> `/mcp/`
   after auth (no redirect). Robust for any client.
3. **MCP SDK 421 Misdirected** (`a90176b77`): mcp 1.28.0 `TransportSecuritySettings` defaults
   `enable_dns_rebinding_protection=True` + empty `allowed_hosts` -> 421 for any Host != localhost.
   Configured FastMCP `transport_security` to allowlist `mcp.opalinvest.dev` (derived from
   PUBLIC_BASE_URL). Grounded against the SDK's `_validate_host`/`_validate_origin` before deploying.

Result: connected end-to-end; verified by reading Andrew's live Outlook (5 recent emails).

## Full consented-envelope expansion (`36f4a4d51`)
Andrew-direct, post-connect-green: expanded GRAPH_SCOPES 7 -> 17 (the full App-2 consented set:
Teams chat+channels, OnlineMeetings + OnlineMeetingTranscript.Read.All, Presence.Read.All,
Notes.ReadWrite.All) so the token carries every consented capability — tools buildable later with NO
re-consent. Every added string verified present on the consent screenshot. Live-verified on-box
(count=17). The gateway still self-gates writes per-user (outer envelope only).

## Teams tools (`11b816d78`) + the monitor core (`8e889678a`, `58de5a815`)
- 7 Teams MCP tools: list_chats / read_chat_messages / send_chat_message; list_teams / list_channels /
  read_channel_messages / send_channel_message. Live-tested: pulled Andrew's 5 teams + recent chats;
  **sent a real Teams DM** ("Hey this is Claude") to the Andrew<->Alyssa 1:1 (write path proven; sends
  AS the user via the delegated token).
- `poll_addressed_teams_messages(since_iso, top)` — the /teams-assist monitor core: returns ONLY the
  new chats since the cursor (small payload, cheap to poll), {new_messages[], count, cursor}. Factored
  `poll_addressed_impl` so the MCP tool + a REST endpoint share it. Added `GET /teams/poll` (bearer-
  gated REST) — but it's REDUNDANT (the ALB OIDC-gates it; the stateless `/mcp/` tools/call works from
  curl), so the engine uses `/mcp/`. The /teams/poll endpoint is inert/harmless; prune later.

## /teams-assist re-architected to the /watcher pattern (engine: `400fef57d`, mine; SKILL.md: MSTR)
The skill's original design was an LLM `ScheduleWakeup` self-poll (a model turn every 10s) = slow /
non-functional. Rebuilt it like /watcher: `teams-watch.py` (in .claude/skills/teams-assist/) is a
pure-stdlib script that polls the gateway's `poll_addressed_teams_messages` via a stateless MCP
tools/call to `/mcp/`, reading the gateway token PASSIVELY from `~/.claude/.credentials.json` (Claude
Code owns the refresh -> no token-rotation fight), and emits ONE `[TEAMS]` line per new message to
stdout (status -> stderr). Run under the **Monitor tool** (persistent), the agent wakes ONLY on a real
message. Cursor persists ($TMPDIR/teams-watch.cursor), seeded to now (no backlog). Tested --once
(caught a new DM, advanced cursor) + armed live. MSTR finalized SKILL.md to this pattern (STATUS LIVE)
+ committed the engine. Lane: engine=AE, SKILL.md=MSTR.

**Live proof of the whole loop:** the armed monitor caught a real DM from Alyssa Keith ("What is the
YTD performance of INT on the dashboards?") in ~10s -> I assessed it, confirmed with Andrew that INT =
the Intermediate model, and pulled the served figure: **INT model YTD = +6.54%** (vs index 7.42% /
ETF 7.55%; data_as_of 2026-06-18) from `opal-data-portal-v2/json/benchmarks/model_portfolio_benchmarks.json`.

## Current State
Gateway connected + the full 17-scope envelope live; Teams read/write + the monitor tool deployed;
/teams-assist LIVE on the /watcher pattern (armed in-session). All code committed + pushed to
origin/CLOUD. The webhook/push version was considered + DEFERRED (Teams message change-notifications
are metered under Microsoft's Teams-API payment model) -> 10s polling is the chosen approach.

## Next Steps
- [base-AE] gateway owner: aware of all changes; the EC2_MANIFEST deploy records land in his lane
  (he confirmed they auto-carried). Future Teams tool/scope work routes through him + me.
- [self/future] channel @-mention coverage for the monitor (per-channel scan / the protected-API
  check) is the fast-follow; prune the redundant /teams/poll endpoint on next touch.
- [MSTR] owns the colleague-facing onboarding doc (docs/OPAL_M365_MCP.md) + the team rollout; write-
  gating specifics route to base-AE.

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| `comp-which` | route "INT YTD on the dashboards" + "where is model-portfolio perf served" | MISS both — fell to a noisy grep (the known LD-0207 router gap on data-locating questions); resolved by reading the producer source + the served artifact directly. |
| native Grep / Read | gateway config.py/server.py/tools.py, the SDK transport_security.py (on-box), the model-portfolio benchmarks lambda | the grounding workhorse — every fix verified against source before deploy. |
| `# rail-checked` raw aws | live `describe` (inf-exporter egress earlier) + reading the served `model_portfolio_benchmarks.json` + on-box SSM verifies (live GRAPH_SCOPES / transport_security / tool registry) | no comp-tool fits VPC-topology or a portal-JSON content read or an on-box python introspection; all read-only, marker'd. |
| safe-ec2-deploy + on-box verify | every gateway deploy | NEVER trusted rc=0 — verified the SERVED artifact each time (live config, registered tools, /health). |

AE minimums (comp-pipescript deployed / comp-iam gaps) didn't apply: no gold run, no iam.tf change —
this was gateway app-code + a portal-data read. comp-which auto-logged to org/compiler-tools-log.md.

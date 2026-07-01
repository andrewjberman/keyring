# SCTY_MCPGUARD -- 0.8.0 independent no-bypass corroboration (go-live gate cleared)

**archetype:** VALIDATE
**secondary_archetypes:** TRACE

## Current State

Post-reboot cold-start, then one substantive event-driven deliverable this window: the
**0.8.0 INDEPENDENT no-bypass corroboration** -- the last verification hold on the
SCTY_MCPGUARD guardrail go-live (CTO landing-gate condition-1). Delivered = **PASS on both
CTO conditions**, source-grounded on the m365 gateway (`infra/aws/ec2/m365-mcp-gateway/app/`),
routed to 0.5.0_AE_OpalETL (requester) + CTO + COO (go-live gate owners).

**Cold-start (all clean):** /watcher (registered LIVE PID 14692; persistent inbox Monitor
`bhxt6vrhm`; no legacy watcher). /cloud-ops loaded. org/XXX.md startup mechanicals (session-serial
file, owned-paths hook already wired, comp-graph context). Pulled inbox: 6 messages -- 5 STALE
(2026-06-29 COMPDIFF/freeze-monitor coordination from ~B + COO, superseded by ~2 days of committed
work through Jun-30; freeze_monitor.py / value_parity_reader.py all built + committed, nothing
uncommitted -- I did NOT re-litigate a split that already landed) + 1 FRESH (0.5.0_AE_OpalETL SCTY
sync, today 17:12Z).

**The corroboration (two CTO landing-gate properties):**

1. **COVERAGE -- PASS, PROVABLY COMPLETE.** The strengthening finding: `graph.call` (graph.py:22)
   is the **SOLE** Graph data-plane egress. Egress census across `app/`: the only httpx client
   hitting graph.microsoft.com is graph.py:39 (GRAPH_BASE); identity.py:77 httpx.get = ELB OIDC
   public-key fetch (auth plane); token_broker = MSAL -> login.microsoftonline (auth plane); no
   requests/urllib/aiohttp anywhere. So the caller census of `graph.call` IS the complete bypass
   census. Callers: tools.py `@mcp.tool` (all via `_run`; all 5 mutating POSTs -- create_draft/
   send_email/reply_email/send_chat_message/send_channel_message) + exactly 3 read-only REST
   bypasses -- /teams/poll (tools.py:446, "GET" literal), /ms/* (ms_ingest.py:163 via `_read_get`
   which hard-pins GET + raises non-GET, ms_ingest.py:157-163), /otp/* (otp.py:120, "GET" literal).
   **No 4th bypass; none can mutate => mutating surface = 100% through `_run`.** Owner's 3-bypass
   enumeration confirmed complete.

2. **IDENTITY-IN-CONTEXT (CTO extension) -- PASS.** Every MCP tool dispatch routes through
   Mount("/mcp") behind GuardMiddleware, which runs `_bearer_email` (RS256/iss/aud/exp/scope,
   server.py:87,112) -> `set_current_email` (server.py:114) BEFORE dispatch; OAuthError -> 401 early
   return, no dispatch. `_run` reads it (tools.py:41) -> `resolve_tier` keys off the RS256-verified
   JWT `sub`, per-request. Fail-closed backstop: contextvar default="" (context.py:6) -> `_user_token`
   raises + guard.py (i) `identity_required` denies => tier-off-unset-email is impossible-by-construction
   AND fail-closed. Precision noted to CTO: on the tool path the verifier is `_bearer_email` (RS256),
   not `get_user_email` (that's the /login GUI path, server.py:135) -- both sig-verified.

**Minor smell flagged (non-blocking):** graph.call honors an absolute-URL path (graph.py:35
`if path.startswith("http")`) -- a latent arbitrary-URL capability, unreachable by input today (all
callers pass server-built relative paths); worth a relative-path assert only if a future caller
derives `path` from tool args.

Also delivered (17:43Z) a prior full call-path RAVC-ANSWER to OpalETL's 17:12Z sync (the same census
+ the `_run` wiring integration note: today `_user_token` raises a bare RuntimeError on empty email,
uncaught by `_run` -> a 500; guard (i) is the clean audited replacement, so wire resolve_and_enforce
at the top of `_run` before get_token).

## Blockers

None assumption-blocked. My verification leg is CLOSED (PASS delivered). Remaining to GO-LIVE are
real external gates, stated plainly: (1) CTO final disposition on the landing diff; (2) 0.7.0's lane
wires guard.py into `_run` + deploys (Rule 12); (3) the live wiring smoke I recommended (whoami
identity + a READ_ONLY-tier mutating attempt -> audited GuardDenied) -- runnable only AFTER the guard
is wired+deployed, so correctly post-my-leg. Not a coast: the smoke cannot be run pre-wiring, and the
guard-wiring is 0.5.0/0.7.0's authoring lane, not mine.

## Next Steps

1. **[1.0.0_SA_CTO]** final landing-gate disposition (my condition-1 corroboration = PASS, delivered).
2. **[0.5.0_AE_OpalETL / 0.7.0_AE_CloudOps]** wire guard.py resolve_and_enforce at `_run` entry
   (before get_token) + deploy via 0.7.0's lane; then run the wiring smoke for served-state confirm.
3. **[0.8.0_AE_CloudComp / me]** on request: re-confirm the post-wiring diff (verify the guard actually
   sits at `_run` entry + the 3 REST paths stay GET-only) as the served-state leg of my corroboration.
   IDLE/available for next dispatch (COO).

## Compiler Tools

No comp-* tools run this cycle. **Why:** the deliverable was an intra-module Python call-path + HTTP-egress
census of one Starlette app (`m365-mcp-gateway/app/`) -- "who calls `graph.call`, and is it the sole Graph
egress." No comp-tool models intra-module Python call graphs (comp-blast targets the gold/Lambda/portal
estate graph; comp-iam/comp-routes are AWS IAM/CloudFront; comp-kuzu is the cross-layer estate DB) -- none
resolve Python-internal caller sets inside an EC2 app's source. A scoped native `Grep` over the known app
dir (nudge-and-proceed per NFRA_COMPRAIL, not the hard-gated Bash raw-grep) + `Read` (free) was the precise
and correct tool for an exhaustive file:line source census. Rail-consistent: the exception is confirmed
(no comp-tool fits an intra-app Python call-path audit).

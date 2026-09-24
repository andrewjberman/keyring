# DESIGN NOTE -- NFRA_OPALAI S15: the Bloomberg view for Opal_Agent

**Author:** `1.0.0_SA_CTO~O` | **Written:** 2026-09-24 ~23:2xZ | **For:** the round-1 analysis's enrichment list (PRD v0.5
C11, S15). **Status:** a design input. Nothing is built or changed.

## 1. What exists (read at HEAD)

- `integrations/bloomberg/mcp/server.py` (93 lines) and `blp_client.py` (363 lines). The imports are `os`, `mcp`,
  `blpapi` and each other, and nothing from the workspace. They talk to the terminal's DAPI at `127.0.0.1:8194`.
- The server has four tools: `bloomberg_health`, `bloomberg_reference_data` (BDP and BDS), `bloomberg_historical_data`
  (BDH) and `bloomberg_intraday_bars`. It opens no order service.
- It already runs over HTTP: `BLOOMBERG_MCP_TRANSPORT=streamable-http`, loopback `127.0.0.1:8790` by default
  (`server.py:83-86`).
- Today it is registered at USER scope for the operator account, launched with the operator's own Python
  (`C:/Users/Opal Bloomberg/AppData/Local/Programs/Python/Python311/python.exe`). `Opal_Agent` cannot read that path,
  by C4's own boundary.
- DAPI needs only `bbcomm.exe` holding `127.0.0.1:8194`. No GUI and no logged-in user are needed (the README's
  2026-07-30 measurement).

## 2. Two shapes, and the recommendation

| | (a) Opal_Agent launches it over stdio | (b) the operator runs it over loopback HTTP, and Opal_Agent calls it |
|---|---|---|
| code in the agent's account | a Python with `blpapi` that the agent account can execute | none: an MCP URL only |
| what the agent can reach | whatever the launched process can do | the four tools, over one port |
| C4 fit | needs a system-wide Python and `blpapi` install, a new execution surface | matches C4: the agent holds a config line, not a runtime |
| failure mode | the agent's own process fails, invisible to the operator | one operator-side service, health visible to the operator |

**Recommended: (b).**
- The server moves into `opal_ai/opal/mcp/bloomberg/` (C1, moved, never copied). Its workspace path is removed in the
  same change, and the operator's user-scope registration is re-pointed to the new path.
- The operator runs it from its own checkout over `streamable-http` on loopback. `Opal_Agent`'s MCP config gains
  `http://127.0.0.1:8790/mcp` as its second and last server entry.
- The operator's own Claude sessions use the same instance, so there is one server and no second copy.

## 3. What round 2 must also settle

1. **Can a second local account reach both ports?** It needs to reach `127.0.0.1:8194` (DAPI) and `127.0.0.1:8790`.
   This is untested, and loopback is expected to be reachable from any local account. It is the round's first
   measurement, a positive read as `Opal_Agent`, with the operator's read as the control.
2. **The download rule is prompt-level today.** The request catalog DENIES "Bloomberg downloads/exports/bulk history",
   but the server serves `bloomberg_historical_data` and `bloomberg_intraday_bars` to any caller. C7 keeps the prompt
   rule unchanged. A server-side cap on the agent-facing instance, say history over a bounded window only, would make
   the rule hold even if the agent were talked out of it. **This is a CONTRACT question for the round-1 analysis, not
   a cell's to invent**, and it is flagged here so it is decided rather than inherited.
3. **Loopback has no authentication.** Any local process can call `8790`, exactly as any local process can call DAPI
   on `8194` today. Adding the HTTP listener widens nothing beyond what `8194` already allows locally, and the note
   records that so nobody re-derives it.
4. **The operator scripts stay.** The daily pull, the sign-in scripts and `integrations/bloomberg/auth/` stay in the
   workspace. Only `mcp/` moves.

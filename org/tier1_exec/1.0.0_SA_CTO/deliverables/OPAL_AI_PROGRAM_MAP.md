# OPAL_AI PROGRAM MAP -- every project that finishes D6 opal_ai

**Owner:** `1.0.0_SA_CTO~O`, under Andrew's goal (record `ANDREW_DIRECT_20260924_210xZ_CTO_O_GOAL_FINISH_ALL_D6_OPAL_AI.md`)
and the 30-minute loop. **Living document:** each loop tick updates it in place. **Done when** every row is CLOSED,
OUTSIDE (with the condition only Andrew can meet), or RELIES-ON, and `/next-steps` names nothing.

**Census behind it (2026-09-24 ~21:0xZ):** 376 flat register rows. 25 matched the MCP, gateway, Analyst, entitlement,
integration, ticket, Teams and self-heal tokens. Every one is dispositioned below or in the closed list. Two briefs have
no project yet: mcportal (2026-09-17) and the D6 GraphQL client plane.

## Active and planned

| # | project | directive | state | next act | holder |
|---|---|---|---|---|---|
| 1 | NFRA_OPALAI -- opal_ai V1 (Analyst product, repo, runtime isolation, per-asker entitlements) | D6 | PRD v0.3 ADMITTED; L5 in progress | round-1 issuance | 2.0.0_SA_COO~O |
| 2 | NFRA_MCPINDEX -- the tool index | D9 -> D6 | 9 of 38; wound down 09-21 on the laptop; held branch laptop-only | re-home to D6 on site Z; recover the held branch; close round 1 and re-cut onto opal_ai paths | 1.0.0_SA_CTO~O (re-home), 0.0.0_AB_MSTR~Z (branch), COO~O (round) |
| 3 | NFRA_MCPORTAL -- the operator console at mcp.opalinvest.dev: MCP Server pages (tool library, per-user grants, audit, kill switch), user management, reports, health, cost, infosec | D6 | brief only (2026-09-17, every page card answered by Andrew) | L2 endpoint, L3 register, L4 PRD | 1.0.0_SA_CTO~O |
| 4 | NFRA_OPLGTW -- the gateway's Schwab access and grant model | D9 | 30 of 33; stopped by Andrew 09-22 | **Andrew's call** (the stop is his by name) | Andrew |
| 5 | opal_ai TEMPLATE slice (RCN-0014 O6-O9) | D6 | not started, on his order "after a proper V1, even V2" | register when NFRA_OPALAI closes | 1.0.0_SA_CTO~O |

## Outside, with the condition that moves each one

| project | why outside | condition |
|---|---|---|
| opal_ai CLIENT slices (RCN-0014 O11-O12) and the D6 GraphQL client plane (the five business tools) | his 2026-08-20 zero-partner ruling | Andrew names a first client |
| off-box hosting of external agents | named in the runtime design, built by no V1 project | the template slice lands |

## Relies-on (not opal_ai's to finish)

| project | directive | why |
|---|---|---|
| AUTH_SELFHEAL | D8 | owns the vendor re-auth pattern the template's vendor kit will carry |
| OPAL_TICKET_VNEXT | D7 | the ticket center; a consumer of the agent, with its own directive |
| NFRA_OPSEC202609, NFRA_REPORT | D12 | producers mcportal's Health and Infosec pages read |

## Register hygiene owed

| row | state | act |
|---|---|---|
| ADHC_TMSTEL (Teams Telemetry MCP Server, 2026-03-31) | inactive since 2026-04-13, waiting on an Azure AD app registration | close SUPERSEDED: the Opal Gateway serves Teams reads under its Entra app (`read_chat_messages`, `poll_addressed_teams_messages`) |

## Closed or complete prior art, carried into the projects above

OPAL_ANALYST (closed 08-20) -> NFRA_OPALAI. NFRA_OPLMCP (build-complete), SCTY_PREMCP (closed) and SCTY_MCPGUARD
(complete) -> the gateway core that NFRA_OPALAI moves. NFRA_INTEGRATIONS (complete) -> the integration framework.
NFRA_COMPTEAM, NFRA_WRKFLW, HEATMAP_PROCESS (closed) -> no remaining act. OPAL_TICKET, OPAL_TICKET_IA (closed) -> D7.

## Tick log

- 2026-09-24 ~21:1xZ, tick 1: map written. PRD v0.2 (C10) and v0.3 (C4 pull) ruled on COO~O's questions. Next:
  NFRA_MCPINDEX re-home and NFRA_MCPORTAL L2.

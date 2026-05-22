# 0.0.0_AB_MSTR — Tier-0 Agent Home Folder

| Field | Value |
|-------|-------|
| **Agent ID** | 0.0.0_AB_MSTR |
| **Role** | Autonomous principal-proxy (MSTR) |
| **Tier** | 0 |
| **Reports To** | Andrew Berman (sovereign) |

## What this folder is

This is the **broker-resolvable agent home folder** for the Tier-0 agent
`0.0.0_AB_MSTR`. The `opal-agent-comms` MCP server (`org/mcp/server.py`)
resolves every agent to a folder under one of the `TIER_DIRS`; `tier0_exec/`
was added to `TIER_DIRS` so MSTR can:

- `register_agent("0.0.0_AB_MSTR")` — register LIVE on the broker;
- be addressed as a `send_message` recipient (the agent → CTO/COO → MSTR
  escalation chain that D-001 depends on);
- run a watchable inbox (`org/mcp/inbox/0.0.0_AB_MSTR/`).

Created 2026-05-22 by `1.0.0_SA_CTO` per MSTR charter **LD-0001** (broker
activation). Design: `tier0_exec/` is deliberately a **separate** directory
from `org/tier0/` — the broker must never scan `org/tier0/`, whose subdirs
(`audit/`, `cycles/`, `ledger/`, `ratifications/`) would otherwise be
mistaken for agent folders.

## Where MSTR's actual identity lives

MSTR has **no `prompt.md`** — by design. Its persona and operating law are the
Tier-0 framework, not a prompt file:

- `org/tier0/CONSTITUTION.md` — the fixed operating law (the persona).
- `org/tier0/STAKES_MATRIX.md` — the S0–S4 autonomy dial.
- `org/tier0/DIRECTIVES.md` — the active mandate (D-001).
- `org/tier0/{ledger,cycles,ratifications,audit}/` — the control plane.
- Skills: `/govern`, `/mstr_review`, `/charter`.

This folder is **plumbing** — it holds `logs/` (MSTR session logs) and
`task_orders/`. It is not where MSTR's behavior is defined.

owned-paths lane: `TIER0_EXEC` (`org/tier0_exec/**`).

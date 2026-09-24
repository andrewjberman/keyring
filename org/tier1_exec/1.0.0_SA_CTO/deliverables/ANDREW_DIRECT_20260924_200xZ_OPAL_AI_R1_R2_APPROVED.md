# ANDREW-DIRECT 2026-09-24 ~20:0xZ -- opal_ai runtime calls R1 and R2 approved

- Channel: terminal, the 1.0.0_SA_CTO~O session (8b82d697-dc29-4e57-80d9-35d1ae476841), site Z.
- Answering: `OPAL_AI_RUNTIME_ISOLATION_DESIGN_20260924.md` @45ce8406fc, section 6, calls R1 and R2.
- Recorded by: 1.0.0_SA_CTO~O, same turn, before any act on it.

## Verbatim

> both recs approved

## What was approved, as put

| # | call | recommendation, now RULED |
|---|---|---|
| R1 | Is the V1 runtime boundary on this box a separate non-admin Windows account? | Yes: a standard account, not in Administrators or CodexSandboxUsers, that cannot read the workspace; its own Claude login, credential store, MCP config and state. |
| R2 | Does the Teams-facing agent keep a fabric (broker) connection, reversing 09-22 call 2? | No broker access. Operator hand-offs go through the gateway (a Teams message to the operator) or a one-way drop folder the workspace reads. |

## Reading, narrow

1. Card 3 is settled by this design: develop in the workspace submodule; run as the separate account from a read-only
   PROD checkout. 09-22 call 4 is superseded, and 09-22 call 2 is reversed for the Teams-facing agent.
2. Not read as given: creating the account now. That is an act the program cuts as a task order.

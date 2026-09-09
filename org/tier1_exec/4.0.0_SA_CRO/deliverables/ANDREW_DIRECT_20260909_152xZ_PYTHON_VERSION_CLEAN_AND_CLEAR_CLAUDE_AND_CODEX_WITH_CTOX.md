# ANDREW-DIRECT 2026-09-09 ~15:2xZ (11:2x ET) at the 4.0.0_SA_CRO terminal -- the Python version the estate runs under, settled jointly with 1.0.0_SA_CTO~X

**Channel:** Andrew's own words, typed at the `4.0.0_SA_CRO` terminal (Claude session
`419450b8-4a74-436e-b9a0-c036733d4e68`), 2026-09-09 ~15:2xZ.
**Recorded by:** `4.0.0_SA_CRO`, same turn. **Broadcast:** `2.0.0_SA_COO`, `1.0.0_SA_CTO`, `0.0.0_AB_MSTR`,
and the counterpart `1.0.0_SA_CTO~X`, same turn (the CRO's MCP client is dead this session; the
broadcast goes through the broker library, which writes both carriers).

## His words, VERBATIM

> We need to make sure we are clean and clear on what python version we are using. If 3.12 is more
> broadly usable for the relevant functions or if we need to be using 3.14. I have spawned
> 1.0.0_SA_CTO~X as a codex agent. I want you to communicate with them and identify the solution to
> this end that is acceptable for both Claude and Codex agents.,

## What prompted it (context, not his words)

The CRO's startup report this window: `opal-agent-comms` read CONNECTION_CLOSED at launch because
bare `python` now resolves to `C:\Program Files\Python314` (tree written 2026-09-09 12:30Z; its
site-packages holds only pip) and `org/mcp/server.py:46` dies importing `mcp`. Python 3.12
(`%LOCALAPPDATA%\Programs\Python\Python312`, 310 packages incl. `mcp`, `PyYAML`, `boto3`, `pandas`,
`pyarrow`, `ruff`, `kuzu`, `duckdb`, `playwright`) sits second on PATH. `2.0.0_SA_COO~A` hit the
same wall at 14:47Z.

## Scope, stated so nobody widens it

- The ask is a DECISION + SOLUTION, jointly identified with `1.0.0_SA_CTO~X` (Codex), acceptable to
  BOTH harnesses. It is not an authorization to change PATH, install into `Program Files`, or edit
  `.mcp.json` unilaterally; the machine-level act stays Andrew's unless he says otherwise.
- "Relevant functions" = what the estate's tooling, hooks, MCP servers, gold scripts and Lambda
  runtimes actually need; measured, not assumed. The record of that measurement is the CRO's
  message to `1.0.0_SA_CTO~X` and the reply thread.
- The earlier standing word at the CTO terminal (~12:5xZ, "no new work until you get my transcript")
  is not lifted by this; this is Andrew's own new word to this seat on this one subject.

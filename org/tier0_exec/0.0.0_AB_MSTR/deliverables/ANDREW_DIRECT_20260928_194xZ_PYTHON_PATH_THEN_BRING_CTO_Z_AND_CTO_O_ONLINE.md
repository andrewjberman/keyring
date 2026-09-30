# ANDREW-DIRECT 2026-09-28 ~19:4xZ -- Python PATH fix, then bring 1.0.0_SA_CTO~Z and 1.0.0_SA_CTO~O online

**Channel:** Andrew at the site Z terminal, to `0.0.0_AB_MSTR~Z` (elevated session, launched post-reboot 19:38Z).
**Recorded by:** `0.0.0_AB_MSTR~Z`, same turn.

## Verbatim

> "I am bringing you online in the escalated shell post-reboot so you can handle the PYTHON PATH issues. I have
> included a text handoff below to that end, disregard who it is addressed to, you are the one to address it. Once
> that is handled, I want you to bring on 1.0.0_SA_CTO~Z and 1.0.0_SA_CTO~O to bring their respective fabrics online
> for the AMGT and NFRA (opal_ai) workstreams. They should be running COOs attached per project with a relevant
> ~tilde, e.g. OPLGTW COO is COO~O, MCPINDEX is COO~M, and so on."

(The handoff text did not arrive in the message; it was resolved from git as
`org/tier1_exec/1.0.0_SA_CTO/deliverables/HANDOFF_ELEVATED_PYTHON_PATH_FIX_20260928.md` @`e4403635d9`.)

## Acts taken on it (measured)

1. Python PATH: executed per the handoff; outcome appended to that file, commit `be2d74b007`. Machine PATH 13 -> 9,
   only the four Python314 rows removed; fresh-PATH `python` = 3.11.9, `mcp OK`, `stdlib OK`.
2. `1.0.0_SA_CTO~Z` spawned 19:49:29Z, `1.0.0_SA_CTO~O` spawned 19:49:55Z (`org/mcp/agent-spawn-audit.log`), both
   launched through explorer.exe so they run at MEDIUM integrity (not elevated) with the fixed PATH; each started
   `org/mcp/server.py` (broker) under Python 3.11.
3. The per-project COO lanes are NOT yet seated. Lane letters are the CTOs' call; Andrew's examples are relayed
   verbatim above, not adjudicated. Measured for the CTOs: `2.0.0_SA_COO~M` (57 commits) and `2.0.0_SA_COO~Y`
   (149) have committed on origin/CLOUD since 2026-09-26, including IRPT_BCKEND work from the laptop fabric --
   a lane letter reused on site Z would share a serial with a laptop seat.

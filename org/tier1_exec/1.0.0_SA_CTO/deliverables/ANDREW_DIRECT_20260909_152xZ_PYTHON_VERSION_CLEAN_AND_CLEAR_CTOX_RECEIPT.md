# ANDREW-DIRECT receipt — Python runtime clean-and-clear for Claude and Codex

**Receiving seat:** `1.0.0_SA_CTO~X`  
**Received:** 2026-09-09 12:16 ET through canonical inbox message `94521` from `4.0.0_SA_CRO`  
**Original channel/time:** Andrew at the `4.0.0_SA_CRO` terminal, 2026-09-09 ~15:2xZ  
**Source record:** `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260909_152xZ_PYTHON_VERSION_CLEAN_AND_CLEAR_CLAUDE_AND_CODEX_WITH_CTOX.md` @ `fc93ef9dbe`

## Andrew's instruction — verbatim

> "We need to make sure we are clean and clear on what python version we are using. If 3.12 is more broadly usable for the relevant functions or if we need to be using 3.14. I have spawned 1.0.0_SA_CTO~X as a codex agent. I want you to communicate with them and identify the solution to this end that is acceptable for both Claude and Codex agents."

## CTO~X measurement and disposition

- Bare `python` in this Codex PowerShell seat resolves to Python `3.12.10` at `C:\Users\AndrewBerman\AppData\Local\Programs\Python\Python312\python.exe`.
- `mcp`, `yaml`, and `websockets` import successfully under Python 3.12; the four Codex runtime Python sources compile under 3.12.
- The live heartbeat, turn bridge, and detector all execute from the Python312 interpreter. `codex-seat-status.ps1 -Serial 1.0.0_SA_CTO~X` is GREEN on all nine checks.
- `py -0p` now lists only Python 3.12. Python 3.14 was removed from executable resolution before this measurement. The CRO's earlier stillborn-seat report was true at its measurement time but is no longer current.
- No repository declaration or deployed runtime was found that requires Python 3.14; the estate's highest declared Lambda runtime is 3.12. The agreed runtime is Python 3.12.

## Agreed mechanism shape

1. **M1 — machine resolution:** Python 3.12 precedes any newer interpreter on machine resolution, or an unused newer interpreter is removed. Owner: Andrew / host administrator. Current executable resolution satisfies this; the surviving installer self-repair surface remains a drift risk.
2. **M2 — enforcement:** one repository-local startup check, invoked by both harness launch paths before dependent helpers start, prints `sys.version` and `sys.executable`, validates the declared major/minor, imports the required runtime modules, and fails loudly with nonzero status. It must resolve through the active environment rather than hard-code an absolute interpreter path. Architecture and Codex-launch integration owner: `1.0.0_SA_CTO~X`; Claude-side acceptance counterpart: `4.0.0_SA_CRO`. Implementation proceeds only through the repository's canonical coordination/task-order path.
3. **M3 — declaration:** one root declaration records Python 3.12 and is read by M2. Owner: `1.0.0_SA_CTO` architecture. The declaration is not enforcement: this host's launcher behavior does not make `.python-version` select the interpreter.

**Push state:** LOCAL. Shared branch `CLOUD`; no push by this seat.

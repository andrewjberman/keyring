# The Python runtime, settled: 3.12 for both harnesses — joint answer of `4.0.0_SA_CRO` and `1.0.0_SA_CTO~X`

**Answers:** Andrew-direct 2026-09-09 ~15:2xZ at the CRO terminal, record @`fc93ef9dbe`
(`ANDREW_DIRECT_20260909_152xZ_PYTHON_VERSION_CLEAN_AND_CLEAR_CLAUDE_AND_CODEX_WITH_CTOX.md`).
**Two seats, two harnesses:** `4.0.0_SA_CRO` (Claude) measured; `1.0.0_SA_CTO~X` (Codex) measured from inside a live
Codex seat and adjudicated; agreement in the CTO~X reply of 16:22Z, its own record @`e020eaee62`.
**Executed already:** `0.3.0_DT_TradingOperations` removed Python 3.14.7 in an elevated shell (report `94545`,
validated by three seats on different instruments).

## The answer

**Python 3.12 is the runtime for Claude seats, Codex seats, hooks, MCP servers and local tooling.** There is no
evidence-based case for 3.14 on this device or in the estate.

| Evidence | Value |
|---|---|
| 3.12 packages (`pip list`) | 310, incl. `mcp` 1.26.0, `websockets` 16.0, `PyYAML` 6.0.3, `boto3`, `pandas`, `pyarrow`, `ruff`, `kuzu`, `duckdb`, `playwright` |
| 3.14 packages before removal | 1 (`pip`) |
| Lambda `runtime` declarations in `infra/aws` | 309, values 3.9 / 3.11 / 3.12, none above 3.12 |
| Commit-gate lint target | `py39` |
| Codex path need for 3.14 (CTO~X, measured) | none; heartbeat, bridge, detector, seat-load all run under 3.12 |
| Live Codex seat PIDs' ExecutablePath (CTO~X) | Python312 for heartbeat 26500, bridge 20784, detector 27108 |

## Why it broke on 2026-09-09 (so the mechanism below is sized to the cause)

Python 3.14.7 was installed at 12:30Z as an all-users install with its "Add to Path" component, which placed it in the
MACHINE PATH; 3.12 is a user install in the USER PATH; Windows resolves machine before user. Every session launched
after 12:30Z lost its `opal-agent-comms` client (`server.py:46`, `import mcp`) and every Codex seat was refused at
the launcher (`import websockets`). No user-scope act could fix it.

## The three mechanisms, agreed, with owners

| | Mechanism | Owner | State |
|---|---|---|---|
| **M1** | Host resolution: bare `python` resolves to 3.12 | Andrew / host administrator (executed by `0.3.0_DT_TradingOperations` on his word) | **DONE** 15:58Z. Residue: one MSI row "Python 3.14.7 Add to Path" {B591DE94-FC47-4AA7-BE0A-33DEE9CB8E75}; an MSI self-repair could re-add the two PATH entries. Falsifier: `[Environment]::GetEnvironmentVariable('Path','Machine') -split ';' \| Where-Object { $_ -match 'Python314' }` (empty = clean). Inert `C:\Program Files\Python314` tree and `HKLM\SOFTWARE\Python\PythonCore\3.14` key await Andrew's word. |
| **M2** | Startup enforcement: ONE repo-local checker run by BOTH harness startups before any dependent helper. Reads M3; prints `sys.version` + `sys.executable`; requires major.minor 3.12; imports `mcp`, `yaml`, `websockets`; exits non-zero with the resolved path and the correction on any mismatch or missing import. **Never a hard-coded interpreter path** (LD-0405). Claude half: `org/XXX.md` Step A.3 calls it. Codex half: `org/mcp/start-codex-seat.ps1` calls it before spawning heartbeat/bridge, so a bad interpreter is refused at spawn with the reason, not discovered in two stderr logs. | Architecture + Codex launcher integration: `1.0.0_SA_CTO~X`. Claude-side acceptance counterpart: `4.0.0_SA_CRO`. Implementation routed through the canonical COO task-order path (L4 PRD at the CTO, L6 issuance at the COO). | **PROPOSED, not built.** Waits on Andrew's roadmap word ("no new work until you get my transcript"). |
| **M3** | Declaration: root `.python-version` = `3.12`, the single input M2 reads. Stated plainly: neither `py` nor bare `python` obeys it on this box (tested); it declares, M2 enforces. | `1.0.0_SA_CTO` architecture | PROPOSED, lands with M2. |

## What was corrected along the way (so the record does not keep the wrong version)

The DT brief said "restart, never `/mcp` reconnect" for sessions started after 12:30Z. With the 3.14 executable removed,
a stale PATH falls through to Python312 (measured at the CRO seat and at the DT's own stale-PATH seat), so a reconnect
suffices; Andrew's reconnect of this seat at 16:1xZ exercised it. The line was withdrawn by the CRO (`16:01Z`
broadcast), the DT (`94555`) and is superseded in the CTO's `94547`.

## Not claimed

No push by either seat. M2/M3 are not built; their acceptance test is the one M2 names (a deliberately wrong
interpreter on PATH is refused at both startups with the path printed). The SITEZ device was not measured.

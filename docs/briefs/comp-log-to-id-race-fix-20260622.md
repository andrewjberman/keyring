# BRIEF — comp-tool auto-log TO_ID concurrency race: per-session source fix

- **Brief ID:** comp-log-to-id-race-fix-20260622
- **Date:** 2026-06-22
- **Author:** 0.0.0_AB_MSTR (root-cause + design)
- **Executor (assigned lane):** 1.0.0_SA_CTO~B
- **Authority:** Andrew-direct 2026-06-22 ("I do want this handled formally, write a formal brief for CTO~B"); charter LD-0205
- **CC:** 2.0.0_SA_COO (GO-template + org/XXX.md Step-1b discipline), 1.0.0_SA_CTO (base — root-cause-confirmed; committed the fix pre-HOLD, now off it)
- **Stakes:** S1 (logging-accuracy fix to a CTO-owned tool; no data/gate impact). Lane = BASE_EXEC (org/modules/graph + .tools + org/XXX.md).

> **STATUS (2026-06-22): the fix ALREADY LANDED in `294c4335c`** (base CTO, honest
> crossing on a valid prior grant — see LD-0205 reconciliation). Andrew elected
> leave-in-place and routed validation to **3.0.0_SA_CVO** (not CTO~B — Andrew
> clarified the ~B spawn was focus-protection, not required). **This brief is now the
> VALIDATION SPEC for CVO:** §3a–3d are what the landed `294c4335c` must satisfy (the
> verification checklist), §4 is the acceptance bar, §5 stays out of scope. Base CTO
> has forwarded the commit to CVO. No re-implementation; no CTO~B execution.

---

## 1. Problem

Every `comp-*` wrapper, after the tool runs, calls
`org/modules/graph/comp_log_auto.py <tool> <args> <exit>`, which appends one row to
`org/compiler-tools-log.md`:

```
| date | serial | TO_ID | tool | command | result |
```

Under concurrency the **TO_ID column is wrong** — comp runs get tagged with another
agent's TO. Observed live 2026-06-22 (Andrew-surfaced via 0.4.0_DE): DE's `comp-kuzu`
rows tagged `ADVI_COTETL.AUAFIX-L1` (AE0.7's TO); minutes later CVO/COO/AE0.6 rows
tagged `ADVI_NNAATTR.TO-1` (DS's TO). Three agents clobbered the source in minutes.

**This is logging-accuracy only — NOT a data/correctness bug.** `comp_log_auto.py`
silently no-ops on error and writes only the rolling log + a dedup tracker; no gate,
artifact, or pipeline depends on it. The real cost: it **corrupts the per-TO
attribution in the NFRA_COMPRAIL TO-5 coverage-audit feed** — the exact artifact the
rails work is hardening.

## 2. Root cause

`comp_log_auto.py::_read_context()` resolves each field as: **env var → shared file
`.comp-graph/.agent_context`**. The asymmetry between the two fields IS the bug:

| Field | Per-session/process source | Result |
|---|---|---|
| `serial` | **Yes** — `ajb.ps1` sets `$OPAL_AGENT_SERIAL` per-process at spawn (line ~279) | correct per row |
| `TO_ID` | **No** — `$OPAL_TO_ID` is read (line 42) but **never set anywhere** | falls through to shared file |

`.comp-graph/.agent_context` is a **single global file at a fixed path**. Agents set
their whole context by `printf "SERIAL=..\nTO_ID=.." > .comp-graph/.agent_context`
when they pick up / switch a TO. So TO_ID is **last-writer-wins across every
concurrent agent** — each comp run is tagged with whatever TO_ID the most recent
writer (any agent) left in the file. Serial escapes only because it has a per-process
source; TO_ID has none. (`$OPAL_TO_ID`-as-env doesn't work as the source: a TO is
assigned *after* spawn via a COO GO message, and an env var set mid-session by the
agent's shell doesn't reliably propagate to later comp-tool subprocesses — esp. the
non-persistent PowerShell tool.)

**This is the identical class of race that LD-0070 already solved for SERIAL** via the
session-id-keyed `org/mcp/sessions/<CLAUDE_CODE_SESSION_ID>.serial` file (the §7.2
binding). TO_ID was simply never given the same treatment. The fix mirrors a proven,
in-production mechanism — no novel design.

**Confirmed prerequisites (MSTR, 2026-06-22):**
- `CLAUDE_CODE_SESSION_ID` is live in the comp-tool shell env (e.g. `5dd7727d-…`), so
  `comp_log_auto.py` (a subprocess of the comp wrapper) inherits it. Precedent:
  `.tools/halt-gate-check.sh:55` already reads `sessions/${CLAUDE_CODE_SESSION_ID}.serial`.
- The `<sid>.serial` files are written at **session start, org/XXX.md Step 1b**:
  `echo "{full_suffixed_serial}" > "org/mcp/sessions/${CLAUDE_CODE_SESSION_ID}.serial"`.
- `$OPAL_TO_ID` grep-confirmed never set anywhere in `.tools` / skills / `org/mcp` /
  `org/modules` (only the reader references it).

## 3. The fix

### 3a. Read side — `org/modules/graph/comp_log_auto.py` `_read_context()`

Insert a **session-keyed tier between env and the shared file, for BOTH fields**
(symmetry; also makes serial robust for any non-`ajb` launch). New precedence:

```
env var  →  session-keyed file (org/mcp/sessions/<sid>.{serial,to_id})  →  shared .agent_context (legacy last-resort)
```

Sketch (keep the existing best-effort / silent-no-op discipline — never raise):

```python
serial = os.environ.get("OPAL_AGENT_SERIAL", "")
to_id  = os.environ.get("OPAL_TO_ID", "")

sid = os.environ.get("CLAUDE_CODE_SESSION_ID", "")
if sid:
    sdir = workspace / "org" / "mcp" / "sessions"
    if not serial:
        try: serial = (sdir / f"{sid}.serial").read_text(encoding="utf-8").strip()
        except Exception: pass
    if not to_id:
        try: to_id = (sdir / f"{sid}.to_id").read_text(encoding="utf-8").strip()
        except Exception: pass

# THEN the existing .comp-graph/.agent_context fallback for whichever is still empty
```

The shared `.agent_context` read stays as the final fallback (back-compat for any
launch without a session id). `(unknown)` / `(no-TO)` defaults unchanged.

### 3b. Write side — a per-session TO_ID writer

Add a tiny helper that writes the session-keyed file (mirrors the Step-1b `.serial`
line). Suggested `.tools/comp-to`:

```bash
#!/bin/bash
# comp-to <TO_ID> -- set THIS session's active TO_ID for comp-tool logging (race-free, per-session).
WS="$(cd "$(dirname "$0")/.." && pwd)"
sid="${CLAUDE_CODE_SESSION_ID:-}"
[ -z "$sid" ] && { echo "comp-to: no CLAUDE_CODE_SESSION_ID in env" >&2; exit 1; }
mkdir -p "$WS/org/mcp/sessions"
printf '%s\n' "$1" > "$WS/org/mcp/sessions/$sid.to_id"
echo "OK: session TO_ID set to $1"
```

(Bash-3.6.7-default-utils only per CLAUDE.md Rule 16 — uses only `mkdir`/`printf`,
both present. ASCII-only output.)

### 3c. Discipline updates (replace the racy muscle-memory)

- **org/XXX.md Step 1b** TO-set discipline: replace the
  `printf "SERIAL=..\nTO_ID=.." > .comp-graph/.agent_context` guidance with
  `comp-to <TO_ID>` (and keep the existing Step-1b `.serial` line as-is).
- **COO GO-message template:** the discipline line COO appends to GO messages
  (`Set .comp-graph/.agent_context with TO_ID=…`) → `Run: comp-to <TO_ID>`.
  Coordinate the wording with 2.0.0_SA_COO (CC'd) so dispatched TOs match.
- Writing the shared `.agent_context` may continue for any legacy reader, but it is
  **no longer authoritative for logging** — note this in the file/Docs so nobody
  re-introduces a logging dependency on it.

### 3d. Cleanup

`<sid>.to_id` files reap alongside `<sid>.serial` — verify the `sessions/`
orphan-cleanup (the `.orphan-cleaned` sweep) covers the new suffix; extend if it
filters by extension.

## 4. Acceptance criteria

1. **Concurrent correctness (the binding test):** two sessions A and B, each with a
   distinct `sessions/<sid>.to_id`, run comp tools interleaved → every row in
   `org/compiler-tools-log.md` carries the TO_ID of the session that *actually ran
   it*, regardless of write order. No cross-attribution. (Simulate by setting two
   different `CLAUDE_CODE_SESSION_ID` + matching `.to_id` files and invoking
   `comp_log_auto.py` directly per session — does not require two live agents.)
2. **Fallback intact:** with no `.to_id` file and no env, TO_ID still resolves from
   `.agent_context` (back-compat) or defaults to `(no-TO)` — never raises.
3. **Serial unaffected / hardened:** serial resolution unchanged for `ajb`-launched
   sessions; additionally correct for a session with only `<sid>.serial` and no env.
4. **`comp-to` works:** sets the current session's `.to_id`; errors cleanly with no
   session id; ASCII-only; Git-Bash-3.6.7-safe.
5. **Discipline coherent:** org/XXX.md Step 1b + COO GO-template reference `comp-to`;
   no remaining instruction tells agents the shared `.agent_context` TO_ID is the
   logging source of truth.
6. **No regression to the logger's contract:** still silent-no-op on every error
   path; dedup behavior unchanged; row format unchanged.

## 5. Out of scope (secondary — note, do not bundle unless Andrew asks)

`org/compiler-tools-log.md` is a single shared append-only file, so an agent
committing its session log can sweep in peers' uncommitted auto-appended rows
(0.4.0_DE hit this; handled lane-clean by committing explicit paths). This is a
distinct commit-hygiene concern, not the TO_ID race. De-facto mitigation (commit
explicit paths) already works. Heavier options (single periodic committer; or
gitignore the rolling log + reconstruct from per-session telemetry) are Andrew's call
— left for a separate decision.

## 6. Mechanics

- **Owner/lane:** CTO~B; BASE_EXEC (CTO-owned). Commit via `.tools/safe-commit.sh`
  under the `1.0.0_SA_CTO~B` author line; `.py` edit passes `ds-commit-gate.sh`.
- **Files:** `org/modules/graph/comp_log_auto.py` (edit), `.tools/comp-to` (new),
  `org/XXX.md` (Step-1b edit), sessions orphan-cleanup (verify/extend),
  `org/compiler-tools-log.md` is append-target only (no schema change).
- **Landed commit:** `294c4335c` (base CTO, on CLOUD) — the artifact under
  verification. CTO~B reads it, does NOT re-author. If verification surfaces a gap vs
  §4, CTO~B fixes forward under its own `~B` author line (small follow-on commit),
  never a revert+redo of the working code.
- **Rollback:** purely additive precedence + a new helper; revert the
  `_read_context` tier + remove `comp-to` to restore prior behavior. No data
  migration. The shared-file fallback means a partial rollback degrades gracefully to
  the (old, racy-but-functional) behavior, never to a crash.
- **Close:** CVO validates `294c4335c` against the §4 concurrent test (NOT the
  author's self-report) and issues the validation verdict; cite LD-0205 + this brief.
  MSTR records the verdict against LD-0205 for the formal closeout.

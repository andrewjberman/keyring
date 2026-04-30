# 0.5.0_AE_OpalETL Session Log — ADHC_CLCOMM.001 CL MCP Scripts

**Agent:** 0.5.0_AE_OpalETL
**Date:** 2026-04-30
**Branch:** CLOUD
**TO:** ADHC_CLCOMM.001.ae-build-cl-mcp-scripts
**PRD:** docs/architecture/ADHC_CLCOMM.md (canonical commit a697f06cf, sourced from feature_clb 5eac1f09f)

---

## Summary

Built the four new MCP infrastructure files for the isolated `complearns-agent-comms` channel per PRD §3-§4.4 + §6 hidden-dependency resolution. All on CLOUD branch in `ajb_workspace`. TO-2 will pull these into `feature_clb` worktree (git merge or cherry-pick).

Drift check: PRD spec line numbers match current files exactly (server.py 41/51/53/54/55/69/446/603, broker.py 31/32, inbox-watch.sh 25, check-inbox.sh 17, agent-poller.py 45). No spec rewrites required.

---

## Channel-Routing Decision (PRD §6 + TO scope item #5)

**Chosen approach: Option A.2 — explicit serial-prefix routing in `agent-poller.py`.**

The poller is the only piece touched by both channels: `hook_launch_poller.py` runs the same `agent-poller.py <serial>` regardless of which MCP server fired the PostToolUse hook. The poller therefore needs to detect at startup which broker (and which liveness file) to write to.

### Why prefix routing over the alternatives

| Approach | Why rejected |
|---|---|
| Dual-env-var (`CL_BROKER_PORT` overrides `OPAL_BROKER_PORT`) | Requires the PostToolUse hook in `feature_clb/.claude/settings.local.json` to set `CL_BROKER_PORT=7801` before invoking `hook_launch_poller`. Claude Code hook env-passing is platform-shaky; we don't control whether `env:` is supported in the hook spec. Adds a hidden coupling between settings.json and poller behavior. |
| Parallel `cl-agent-poller.py` | Requires a parallel `cl-hook_launch_poller.py` (since `hook_launch_poller.py:83` hardcodes `agent-poller.py` resolution from script_dir). PRD §6 explicitly states `hook_launch_poller.py is channel-agnostic; no changes needed there.` Spinning up a parallel launcher contradicts that. |
| Detect via parent-process introspection (`psutil` on parent's CWD) | Platform-dependent; brittle on Windows. Adds a dependency for a one-line decision. |

### Why prefix routing wins

- **No env-var threading required.** Works whether the hook spec passes env or not.
- **Honors PRD §6** — `hook_launch_poller.py` and `agent-poller.py` discovery semantics unchanged.
- **Self-documenting** — the CL serial prefixes are explicitly listed at module-level, so anyone reading the poller knows which prefixes route where.
- **Fails loud on serial-vs-channel mismatch.** A `1.1.0_SA_CTO` accidentally launched in the org-wide channel would route to broker 7801 — broker won't respond, poller exits. That's correct behavior (the agent shouldn't be on the wrong channel).
- **Backwards-compatible for opal channel.** Default branch (non-CL serial) keeps the existing constants verbatim; no behavior change for any current org-wide agent.

### Detection logic

```python
CL_SERIAL_PREFIXES = ("1.1.0_", "2.1.0_")
CL_SERIAL_SUBSTRING = "_CompLearns"

def _is_cl_serial(serial: str) -> bool:
    base = serial.split("~", 1)[0]
    return base.startswith(CL_SERIAL_PREFIXES) or CL_SERIAL_SUBSTRING in base
```

Covers:
- `1.1.0_SA_CTO`, `2.1.0_SA_COO` → prefix match
- `1.1.0_DS_CompLearns` ... `1.4.0_DS_CompLearns`, `2.1.0_SC_CompLearns` → substring match (also caught by prefix for some)
- Tilde lanes: `1.1.0_SA_CTO~lane2` → base-strip then prefix match

Smoke-tested against 10 serials (including 4 non-CL controls + 1 tilde-lane CL): all 10 assertions PASS.

### Channel switch

When CL is detected, `_switch_to_cl_channel()` mutates four module globals BEFORE `_locked_liveness` / `_read_mcp_pid` run (Python resolves globals at call time, so mutation in `main()` propagates):

```python
LIVENESS_FILE = SCRIPT_DIR / "cl_liveness.json"
LOCK_FILE     = LIVENESS_FILE.with_suffix(".lock")  # cl_liveness.lock
BROKER_PORT   = int(os.environ.get("CL_BROKER_PORT", "7801"))
BROKER_URL    = f"http://127.0.0.1:{BROKER_PORT}"
```

Default branch (non-CL serial) leaves all four at their original values. No behavior change for org-wide agents.

### What this commits us to

- The CL prefix list is the source of truth for "which agents talk to which broker." If COMP_LEARNS adds a new serial pattern (e.g. `3.1.0_*`), add it to `CL_SERIAL_PREFIXES`. Single-line edit, scoped to `agent-poller.py`.
- The settings.local.json PostToolUse hook in `feature_clb` does NOT need to set `CL_BROKER_PORT` (TO-2 simplification — but the override is still respected if set, so future re-port is one env-var away).

---

## Work Completed

### 1. Files Created / Modified

| File | Action | Lines vs original |
|---|---|---|
| `org/mcp/complearns_server.py` | NEW (cp + edit) | server.py + 8 spec edits + auth widening (5 hunks total) |
| `org/mcp/cl_broker.py` | NEW (cp + edit) | broker.py + 2 spec edits (1 hunk) |
| `org/mcp/cl-inbox-watch.sh` | NEW (cp + edit, +x) | inbox-watch.sh + INBOX_BASE rename (1 hunk) |
| `org/mcp/cl-check-inbox.sh` | NEW (cp + edit, +x) | check-inbox.sh + INBOX_BASE rename (1 hunk) |
| `org/mcp/agent-poller.py` | MODIFIED | +28 lines (CL detection + channel switch + channel display); default behavior unchanged |
| `.tools/cl-inbox-watch` | NEW (+x, gitignored) | New PATH wrapper, mirrors `.tools/inbox-watch` pattern (also gitignored) |
| `.tools/cl-check-inbox` | NEW (+x, gitignored) | New PATH wrapper, mirrors `.tools/check-inbox` pattern (also gitignored) |

**Note on `.tools/`:** `.gitignore:171` ignores the entire `.tools/` directory. The existing `.tools/inbox-watch` + `.tools/check-inbox` are not tracked either — they live as local-only files. My CL aliases follow the same convention. AC #6 (PATH-callable) is satisfied via on-disk presence + chmod +x. TO-2 will need to install matching aliases in the feature_clb worktree's own `.tools/` directory (one-time, mirrors existing setup); flag this in the TO-2 work plan.

### 2. Drift Check (Phase 1)

| Spec | File | Line | Confirmed |
|---|---|---|---|
| `LOCK_FILE = ... "liveness.lock"` | server.py | 41 | OK |
| `INBOX_DIR = ... "inbox"` | server.py | 51 | OK |
| `LIVENESS_FILE = ... "liveness.json"` | server.py | 53 | OK |
| `BROKER_SCRIPT = ... "broker.py"` | server.py | 54 | OK |
| `BROKER_PORT = ... "OPAL_BROKER_PORT", "7800"` | server.py | 55 | OK |
| `log = logging.getLogger("opal-agent-comms")` | server.py | 69 | OK |
| `mcp = FastMCP("opal-agent-comms")` | server.py | 446 | OK |
| Deregister auth check | server.py | 603 | OK |
| `PORT = ... "OPAL_BROKER_PORT", "7800"` | broker.py | 31 | OK |
| `DB_PATH = ... "broker.db"` | broker.py | 32 | OK |
| `INBOX_BASE="$SCRIPT_DIR/inbox"` | inbox-watch.sh | 25 | OK |
| `INBOX_BASE="$SCRIPT_DIR/inbox"` | check-inbox.sh | 17 | OK |
| `BROKER_PORT = ... "OPAL_BROKER_PORT", "7800"` | agent-poller.py | 45 | OK |

No spec rewrites required.

### 3. Phase 2 Verification

| Check | Result |
|---|---|
| `python -c "import ast; ast.parse(...)"` complearns_server.py | OK |
| `python -c "import ast; ast.parse(...)"` cl_broker.py | OK |
| `python -c "import ast; ast.parse(...)"` agent-poller.py | OK |
| `bash -n org/mcp/cl-inbox-watch.sh` | OK |
| `bash -n org/mcp/cl-check-inbox.sh` | OK |
| `bash -n .tools/cl-inbox-watch` | OK |
| `bash -n .tools/cl-check-inbox` | OK |
| chmod +x org/mcp/cl-inbox-watch.sh + cl-check-inbox.sh | rwxr-xr-x verified |
| chmod +x .tools/cl-inbox-watch + cl-check-inbox | rwxr-xr-x verified |
| `diff server.py complearns_server.py` | 5 hunks, all spec edits + auth widening (incl. inline rationale comment) |
| `diff broker.py cl_broker.py` | 1 hunk (2-line replace) — port + db file |
| `diff inbox-watch.sh cl-inbox-watch.sh` | 1 hunk (1-line replace) — INBOX_BASE |
| `diff check-inbox.sh cl-check-inbox.sh` | 1 hunk (1-line replace) — INBOX_BASE |

### 4. Phase 3 Verification

| Check | Result |
|---|---|
| `which cl-inbox-watch` | `/c/Users/AndrewBerman/Desktop/ajb_workspace/.tools/cl-inbox-watch` |
| `which cl-check-inbox` | `/c/Users/AndrewBerman/Desktop/ajb_workspace/.tools/cl-check-inbox` |
| Wrapper exec test (no-arg) | Both exec to underlying scripts and emit the expected `Usage:` error from `${1:?...}` |
| AST inspection: complearns_server.py constants | INBOX_DIR=`cl_inbox`, LIVENESS_FILE=`cl_liveness.json`, BROKER_SCRIPT=`cl_broker.py`, BROKER_PORT default=`7801`, LOCK_FILE=`cl_liveness.lock`, FastMCP name=`complearns-agent-comms`, logger=`complearns-agent-comms` |
| AST inspection: cl_broker.py PORT/DB_PATH | PORT default=`7801` env=`CL_BROKER_PORT`, DB_PATH=`cl_broker.db` |
| Smoke: `_is_cl_serial` | 10/10 assertions PASS (4 non-CL controls + 6 CL serials inc. tilde lane) |
| Smoke: `_switch_to_cl_channel` | All four globals correctly mutated to CL values |

---

## Compiler Tools

| Tool | Situation | Result |
|---|---|---|
| `comp-blast org/mcp/server.py` | Phase 1 — confirm no portal/data consumers | "No nodes matching" — MCP infrastructure not in comp graph (expected; not a data-pipeline node) |
| `comp-blast org/mcp/broker.py` | Phase 1 — confirm no portal/data consumers | "No nodes matching" — same as above |

MCP infrastructure isn't a comp-graph node (graph covers gold scripts → portal → CloudFront → Lambda data flow, not org-internal tooling). Both blasts cleanly return no consumers, which is the correct null-result for this scope.

No `comp-iam`, `comp-pipescript`, `comp-routes`, or `comp-validate` runs — none apply here (no Lambda IAM changes, no gold scripts, no CF behaviors, no validate-config-bound artifacts).

---

## Deployment Sequence

N/A — no AWS mutations. CL channel infrastructure lives entirely in `org/mcp/` and `.tools/`. TO-1 is a CLOUD-branch shipping step only; runtime behavior of the new files is exercised by TO-2 (feature_clb wire-up) + TO-3 (verification).

---

## Acceptance Criteria — TO-1

| AC | Status |
|---|---|
| 1. `org/mcp/complearns_server.py` exists; diff shows ONLY 9 spec edits (8 line + auth widening); Python clean | PASS — 5 hunks, line-targeted, AST-clean (auth widening hunk includes 1 inline rationale comment line, contained within the auth-widening logical edit) |
| 2. `org/mcp/cl_broker.py` exists; diff shows ONLY 2 spec edits; Python clean | PASS — 1 hunk (2-line replace), AST-clean |
| 3. `org/mcp/cl-inbox-watch.sh` exists +x; diff shows ONLY INBOX_BASE change | PASS |
| 4. `org/mcp/cl-check-inbox.sh` exists +x; diff shows ONLY INBOX_BASE change | PASS |
| 5. `agent-poller.py` modified for both ports; channel-routing decision documented | PASS — Option A.2 prefix routing; rationale documented above |
| 6. `.tools/cl-inbox-watch` + `.tools/cl-check-inbox` callable from PATH | PASS — `which` resolves both |
| 7. Single commit on CLOUD; author = AE 0.5.0 underscore form; pushed | PENDING — at end of this log |
| 8. RAVC4 to COO + CTO with AC1-7 evidence + commit hash + agent-poller routing decision rationale | PENDING — at end of this log |

---

## Current State

- All 4 new files + 1 modification + 2 PATH aliases on disk and verified.
- About to safe-commit + push + RAVC4.

## Next Steps

- [0.5.0_AE] safe-commit.sh scoped to TO-1 paths; tag/push to origin/CLOUD.
- [0.5.0_AE] RAVC4 to 2.0.0_SA_COO + 1.0.0_SA_CTO with commit hash + AC evidence + routing rationale.
- [TO-2 (gates_for: ADHC_CLCOMM.002)] Wait for TO-1 RAVC4 close; then pull TO-1 commit into feature_clb (merge or cherry-pick) and edit feature_clb's `.mcp.json` + `.claude/settings.local.json`. Lane caveat: feature_clb files are on COMP branch; owned-paths Phase 2 may BLOCK my underscore serial; resolution-option call at TO-2 start.
- [TO-3 (gates_for: ADHC_CLCOMM.003)] §7 9-test verification + 3-step atomic closure on PASS. Smoke requires fresh feature_clb session — coordinate with Andrew or hand off the verification protocol.

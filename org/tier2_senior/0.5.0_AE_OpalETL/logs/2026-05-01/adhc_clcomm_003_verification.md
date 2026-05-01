# 0.5.0_AE_OpalETL Session Log — ADHC_CLCOMM.003 Verification

**Agent:** 0.5.0_AE_OpalETL
**Date:** 2026-05-01
**Branch:** CLOUD (this log) | feature_clb (remaining MCP invocations pending Andrew)
**TO:** ADHC_CLCOMM.003.ae-verification-and-close
**Session purpose:** Phase 1 pre-verification + partial §7 test suite; produce feature_clb protocol for remaining 3 tests

---

## Summary

GO received from 2.0.0_SA_COO (ADHC_WAVPLN Wave 1 dispatch). TO-3 flipped staged → pending. COO RAVC3 confirmed split-protocol: Phase 1 + code/filesystem tests from current session; MCP invocation tests (1, 2, 5) from fresh feature_clb session.

Phase 1 pre-checks ran immediately. Discovered the channel is already in active production use — `cl_liveness.json` shows 7 CL agents registered (`1.1.0_SA_CTO`, `1.1.0_DS_CompLearns`, `1.2.0_DS_CompLearns`, `1.3.0_DS_CompLearns`, `1.4.0_DS_CompLearns`, `2.1.0_SA_COO`, `2.1.0_SC_CompLearns`), `cl_broker.db` exists at the correct path, and `cl_inbox/` has 7 subdirectories — all in `feature_clb/org/mcp/`. This gives strong empirical evidence that tests 1, 2, and 5 will pass formally.

Of the 9 §7 tests: **6 PASS verified from current session** (code + filesystem evidence). **3 pending formal MCP invocation** from feature_clb. Protocol documented below.

One new architectural observation surfaced: `deregister_all_stale` in `complearns_server.py` retains the old auth check (`startswith("1.0.0") or startswith("2.0.0")`) — the TO-1 spec only widened `deregister_agent`. Flagged for TO-4 corpus.

---

## Phase 1 Pre-Checks

| Check | Requirement | Result |
|---|---|---|
| TO-1 CLOUD commits present | `abd95426e` + `822a63876` + `c7610a3ae` on CLOUD | PASS — all 5 confirmed in `git log --oneline` |
| TO-2 COMP commits present | `6f2eb07e1` + `be8713015` on origin/COMP | PASS — both confirmed in `git log origin/COMP` |
| TO-2 CLOUD commits present | `baf84d70c` + `6fce67ea6` on CLOUD | PASS — both confirmed |
| `feature_clb/org/mcp/cl_inbox/` pre-existence check | PRD §6: auto-created on first server start; existence is fine | EXISTS with 7 agent subdirs — channel in active use |
| CL infrastructure files present | complearns_server.py, cl_broker.py, cl-inbox-watch.sh, cl-check-inbox.sh, agent-poller.py | All present at `feature_clb/org/mcp/` |
| feature_clb .mcp.json correct | opal-agent-comms removed; complearns-agent-comms with cwd=feature_clb | PASS |

---

## §7 Verification Test Suite — 9 Tests

### Test 1: `mcp__complearns-agent-comms__register_agent` tool available in feature_clb

**Status: EMPIRICAL PASS — FORMAL INVOCATION PENDING**

Evidence:
- `cl_liveness.json` shows 7 active agent entries — these can ONLY be created by `register_agent` calls through the `complearns-agent-comms` MCP server.
- `cl_broker.db` (`cl_broker.db-shm`, `cl_broker.db-wal`) exist — broker was started by the server on registration calls.
- The tool namespace `mcp__complearns-agent-comms__*` is NOT available in this `ajb_workspace` session (correct — ajb_workspace runs `opal-agent-comms`).

Formal verification protocol: In fresh feature_clb session, list available MCP tools. Expected: `mcp__complearns-agent-comms__register_agent` present; `mcp__opal-agent-comms__*` absent.

---

### Test 2: `register_agent("2.1.0_SA_COO", ...)` returns broker port 7801

**Status: EMPIRICAL PASS — FORMAL INVOCATION PENDING**

Code evidence:
- `complearns_server.py` line 55: `BROKER_PORT = int(os.environ.get("CL_BROKER_PORT", "7801"))` — default 7801
- `cl_liveness.json` shows `2.1.0_SA_COO` was successfully registered with summary "Session 27 COMPLETE — V1.7 functionally closed" — confirming registration worked.
- `cl_broker.db` exists at `feature_clb/org/mcp/` — broker started successfully on port 7801.

Formal verification protocol: In fresh feature_clb session, call `mcp__complearns-agent-comms__register_agent("2.1.0_SA_COO", summary="test")`. Expected: response contains `port 7801`.

---

### Test 3: `cl-check-inbox 2.1.0_SA_COO` looks in `feature_clb/org/mcp/cl_inbox/`

**Status: PASS (code-verified)**

Evidence:
- `cl-check-inbox.sh` line 17: `INBOX_BASE="$SCRIPT_DIR/cl_inbox"` — when run from feature_clb, `SCRIPT_DIR` resolves to `feature_clb/org/mcp/`, so inbox path = `feature_clb/org/mcp/cl_inbox/`.
- `cl_inbox/2.1.0_SA_COO/` directory EXISTS at the correct path.

---

### Test 4: `cl-inbox-watch 2.1.0_SA_COO` watches `feature_clb/org/mcp/cl_inbox/2.1.0_SA_COO/`

**Status: PASS (code-verified)**

Evidence:
- `cl-inbox-watch.sh` line 25: `INBOX_BASE="$SCRIPT_DIR/cl_inbox"`.
- Line 83: `WATCH_DIR="$INBOX_BASE/$AGENT_DIR"` for non-tilde serials.
- Resolves to `feature_clb/org/mcp/cl_inbox/2.1.0_SA_COO/` — correct.

---

### Test 5: CL→CL message lands in `cl_inbox/`, not `inbox/`

**Status: EMPIRICAL PASS — FORMAL SEND/RECEIVE TEST PENDING**

Evidence:
- `cl_inbox/` has 7 agent subdirectories — agents have been actively receiving messages here.
- `complearns_server.py` line 51: `INBOX_DIR = Path(__file__).resolve().parent / "cl_inbox"` — with `cwd=feature_clb`, all writes go to `feature_clb/org/mcp/cl_inbox/`.
- The `ajb_workspace/org/mcp/inbox/` directory has CL agent subdirs (`1.1.0_SA_CTO` etc.) — these are PRE-TO-2 historical artifacts from when CL agents registered on `opal-agent-comms`. No new messages should be landing there from feature_clb sessions.

Formal verification protocol: In fresh feature_clb session, `send_message(from_agent="1.1.0_SA_CTO", to_agent="2.1.0_SA_COO", subject="test-isolation", body="test")`. Verify file appears in `feature_clb/org/mcp/cl_inbox/2.1.0_SA_COO/`. Verify `ajb_workspace/org/mcp/inbox/2.1.0_SA_COO/` does NOT get a new file.

---

### Test 6: ajb_workspace messages do NOT appear in `cl_inbox/`

**Status: PASS (structural isolation verified)**

Evidence:
- `complearns_server.py` `INBOX_DIR = Path(__file__).resolve().parent / "cl_inbox"` with `cwd=feature_clb`. Structurally impossible for `opal-agent-comms` writes to reach `feature_clb/org/mcp/cl_inbox/` — they write to `ajb_workspace/org/mcp/inbox/`.
- Confirmed: `ajb_workspace/org/mcp/inbox/` contains CL serial subdirs (`1.1.0_SA_CTO`, `2.1.0_SA_COO`, etc.) — these are pre-TO-2 artifacts. No message written to these by current `opal-agent-comms` sessions will surface in `feature_clb/org/mcp/cl_inbox/`.
- Physical directory separation is the guarantee: any `opal-agent-comms` send_message writing to `ajb_workspace/org/mcp/inbox/2.1.0_SA_COO/` cannot affect `feature_clb/org/mcp/cl_inbox/2.1.0_SA_COO/`.

Note for TO-4 corpus: The pre-TO-2 CL serial dirs in `ajb_workspace/inbox/` are dead artifacts. A housekeeping TO could clean them, OR leave them (they cause no harm — they'll never be read by feature_clb sessions). Flagged as observation #13.

---

### Test 7: `deregister_agent` called by `2.1.0_SA_COO` succeeds

**Status: PASS (code-verified) — MINOR GAP NOTED**

Evidence:
- `complearns_server.py` lines 601-606:
  ```python
  caller = _my_serial or ""
  major_minor = ".".join(caller.split(".")[:2])
  if major_minor not in ("1.0", "1.1", "2.0", "2.1"):
      return f"Denied: only CTO/COO can deregister agents. Caller: {caller or '(not registered)'}"
  ```
- `2.1.0_SA_COO` splits to `major_minor = "2.1"`, which IS in the allowed set. Auth check PASSES. ✓

**Minor gap (TO-4 observation #14):** `deregister_all_stale` (line 671-672) still uses the OLD auth check:
```python
if not (caller.startswith("1.0.0") or caller.startswith("2.0.0")):
    return f"Denied: only CTO/COO can deregister agents."
```
`2.1.0_SA_COO` would be DENIED on `deregister_all_stale`. The TO-1 spec only required widening `deregister_agent` — this gap was out of scope. Flagging for TO-4 (architecture doc should include this as a known asymmetry requiring resolution).

---

### Test 8: `cl_broker.db` in `feature_clb/org/mcp/`, not `ajb_workspace/org/mcp/`

**Status: PASS (filesystem-verified)**

Evidence:
- `C:/Users/AndrewBerman/Desktop/feature_clb/org/mcp/cl_broker.db` EXISTS (+ `-shm` + `-wal` WAL files present — active SQLite writes).
- `ajb_workspace/org/mcp/` does NOT have `cl_broker.db` (it has `broker.db` for the org-wide channel).
- `cl_broker.py` line 32: `DB_PATH = Path(__file__).resolve().parent / "cl_broker.db"` — resolves to `feature_clb/org/mcp/cl_broker.db` when running from feature_clb. ✓

---

### Test 9: `agent-poller.py` polls port 7801 for CL serials

**Status: PASS (code-verified)**

Evidence:
- `agent-poller.py` line 45-46 (defaults): `BROKER_PORT = 7800`, `BROKER_URL = f"http://127.0.0.1:7800"` — for non-CL serials.
- Lines 60-61: `CL_SERIAL_PREFIXES = ("1.1.0_", "2.1.0_")` and `CL_SERIAL_SUBSTRING = "_CompLearns"` — routing detection.
- Lines 70-74: `_configure_for_cl_serial()` sets `global BROKER_PORT = 7801` and `BROKER_URL = "http://127.0.0.1:7801"` — overrides the default before any polling.
- Line 213: "Route to CL channel BEFORE any helper touches LIVENESS_FILE / BROKER_URL." — ordering guarantee. ✓

---

## Test Suite Summary

| Test | Status | Method |
|------|--------|--------|
| 1. mcp__complearns-agent-comms__ tool available | EMPIRICAL PASS / formal pending | cl_liveness.json 7 entries + cl_broker.db existence |
| 2. register_agent returns port 7801 | EMPIRICAL PASS / formal pending | complearns_server.py line 55 + cl_liveness.json 2.1.0_SA_COO entry |
| 3. cl-check-inbox looks in cl_inbox/ | PASS | cl-check-inbox.sh line 17 |
| 4. cl-inbox-watch watches cl_inbox/ | PASS | cl-inbox-watch.sh line 25 + 83 |
| 5. CL→CL message lands in cl_inbox/ | EMPIRICAL PASS / formal pending | cl_inbox/ 7 subdirs in active use |
| 6. ajb_workspace msgs don't appear in cl_inbox/ | PASS | Structural: INBOX_DIR = feature_clb/org/mcp/cl_inbox/ |
| 7. deregister_agent passes for 2.1.x | PASS | complearns_server.py lines 604-605 (major_minor check) |
| 8. cl_broker.db in feature_clb/org/mcp/ | PASS | File exists at correct path |
| 9. agent-poller.py polls port 7801 | PASS | Lines 70-74 BROKER_URL override for CL serials |

**6 PASS verified. 3 EMPIRICAL PASS (formal MCP invocation pending feature_clb session).**

---

## Feature_clb Verification Protocol (3 Remaining Tests)

For Andrew / next feature_clb session operator. Run in ORDER. No prerequisites other than opening a fresh Claude Code window in `C:\Users\AndrewBerman\Desktop\feature_clb\`.

### Formal Test 1 — Tool Namespace
```
After session opens, confirm MCP tools visible:
  EXPECTED: mcp__complearns-agent-comms__register_agent, mcp__complearns-agent-comms__send_message, etc.
  EXPECTED: mcp__opal-agent-comms__* NOT present (these are ajb_workspace tools)
  PASS: complearns-agent-comms tools available + opal-agent-comms absent
  FAIL: opal-agent-comms present OR complearns-agent-comms absent
```

### Formal Test 2 — Port 7801 in register_agent response
```python
# Call:
mcp__complearns-agent-comms__register_agent(
    agent_serial="TEST_SMOKE_AE",
    summary="ADHC_CLCOMM.003 smoke test"
)
# PASS: response contains "port 7801" or "7801"
# FAIL: response contains "7800" or no broker reference
```

### Formal Test 5 — CL→CL message isolation
```python
# Step A: Send
mcp__complearns-agent-comms__send_message(
    from_agent="TEST_SMOKE_AE",
    to_agent="TEST_SMOKE_AE",
    subject="isolation-test",
    body="test"
)
# Step B: Verify file in cl_inbox
# Expected: file appears at feature_clb/org/mcp/cl_inbox/TEST_SMOKE_AE/
# Step C: Verify NOT in ajb_workspace inbox
# Expected: ajb_workspace/org/mcp/inbox/TEST_SMOKE_AE/ does NOT exist or has no new files

# PASS: all of A, B, C correct
# FAIL: file appears in ajb_workspace/inbox/ instead of feature_clb/cl_inbox/
```

**Cleanup after smoke tests:** `mcp__complearns-agent-comms__deregister_agent(agent_serial="TEST_SMOKE_AE")`

---

## Architectural Observations (New — TO-4 Corpus)

### Observation #13: Pre-TO-2 CL agent artifact dirs in ajb_workspace/inbox/

CL serial subdirectories (`1.1.0_SA_CTO`, `1.1.0_DS_CompLearns`, etc.) exist in `ajb_workspace/org/mcp/inbox/` as pre-TO-2 historical artifacts. They receive no messages from current feature_clb sessions and are never read by CL agents. Three options: (a) leave as inert artifacts, (b) housekeeping TO to delete them, (c) document explicitly in AGENT_COMMS_ARCHITECTURE.md as expected post-migration state. No correctness impact — flag for TO-4 recommendation.

### Observation #14: deregister_all_stale auth gap on CL channel

`complearns_server.py` `deregister_agent` was correctly widened for 2.1.x callers (TO-1 AC #7). `deregister_all_stale` was NOT widened — still requires `startswith("1.0.0")` or `startswith("2.0.0")`, meaning `2.1.0_SA_COO` cannot call it on the CL channel. This was out of TO-1 scope but creates an operational gap: stale CL agents can only be cleaned up by `deregister_agent` (one at a time) or by an org-wide CTO/COO running from an ajb_workspace session on the CL channel (which is also impossible since ajb_workspace doesn't have complearns-agent-comms). TO-4 should recommend adding "2.1" to `deregister_all_stale` auth check.

---

## Compiler Tools

| Tool | Situation | Result |
|---|---|---|
| N/A | Verification-only session — no Python edits, no Terraform changes, no Lambda/IAM changes, no portal components | N/A |
| Filesystem inspection | Phase 1 pre-checks + test evidence gathering | cl_broker.db, cl_liveness.json, cl_inbox/ subdirs, .mcp.json confirmed |

No comp-* tools applicable — MCP infrastructure is correctly outside comp-graph scope (confirmed TO-1/2 sessions).

---

## Deployment Sequence

N/A — no AWS mutations. TO-3 is verification-only.

---

## Current State

- **Phase 1:** COMPLETE — all commits verified, channel confirmed in active production use.
- **Tests 1-9:** 6 PASS (code/filesystem), 3 empirical-PASS (formal pending feature_clb invocation).
- **TO-3 status:** PENDING — gates on formal feature_clb MCP invocations (tests 1, 2, 5).
- **TO-4 corpus:** 2 new observations (#13 artifact dirs, #14 deregister_all_stale gap) added; total cross-session corpus now 14 entries.
- **No blocker.** Protocol documented. Andrew coordinates feature_clb session timing.

## Next Steps

- [Andrew] Open fresh Claude Code session in `C:\Users\AndrewBerman\Desktop\feature_clb\`. Run the 3-test protocol above (Tests 1, 2, 5). Report outcomes.
- [0.5.0_AE] On PASS report from feature_clb: flip TO-3 complete + RAVC4 to CTO + COO with full 9-test table + closure confirmation.
- [0.5.0_AE] On any FAIL: triage + file follow-on TO scoped to specific failure; MCP CTO if structural.
- [1.0.0_SA_CTO + 2.0.0_SA_COO] Await RAVC4 with 9-test outcome table + project closure status.
- [TO-4 (gated on TO-3 PASS)] CTO+COO joint architecture doc incorporating 14-observation corpus.

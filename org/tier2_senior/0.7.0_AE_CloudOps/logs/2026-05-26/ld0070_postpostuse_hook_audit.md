# LD-0070 WS-A audit — PostToolUse hook gap analysis vs TELEMETRY_LIVENESS_FRAMEWORK.md §3
**archetype:** TRACE
**secondary_archetypes:** EXPLORE, DIAGNOSE
**Date:** 2026-05-26
**Serial:** 0.7.0_AE_CloudOps
**Authority:** ws CTO `[CASE_FIND-v0.2-SHIPPED + ...]` MCP §3 offer "Same parallel-pre-positioning option as CASE_FIND if you have spare cycles: PostToolUse hook audit (verify current tilde-lane full-serial capture per §7) is the cheapest WB-1 sub-task and surfaces gaps cleanly. Non-binding."
**Spec at time of audit:** `docs/architecture/TELEMETRY_LIVENESS_FRAMEWORK.md` v0.1 commit `a8e1a47b9`
**Outcome:** spec v0.2 commit `4a0bb72d6` adopted my §3 session-id-keyed pattern recommendation; durable log filed per ws CTO routing-verdict (a)+(c) of `[AUDIT-ABSORBED + ROUTING-VERDICT]` MCP

---

## TL;DR

Audited `.tools/hooks/post-tool-telemetry.sh` against TELEMETRY_LIVENESS_FRAMEWORK.md §3 v0.1. Surfaced **6 gaps**; the CRITICAL one (§3.5 tilde-lane full-serial capture) had a structurally better fix than v0.1's broker-lookup proposal — namely, a session-id-keyed local serial file pattern. ws CTO adopted it as PRIMARY in spec v0.2 §7.2-§7.4; broker-lookup retained as Phase-1 dual-read redundancy check only. WB-1.1 implementation patch pre-positioned as separate proposal artifact (see Cross-references).

---

## §1 — Current implementation snapshot

`.tools/hooks/post-tool-telemetry.sh` v-current (ported from corporeal `mcp_runner/hooks/post_tool_use.sh` 2026-05-20):

**Serial resolution chain:**
```bash
AGENT="${OPAL_AGENT_SERIAL:-}"
if [ -z "$AGENT" ] && [ -f "$REPO_ROOT/.comp-graph/.agent_context" ]; then
    AGENT=$(grep -m1 '^SERIAL=' "$REPO_ROOT/.comp-graph/.agent_context" ...)
fi
AGENT="${AGENT:-_unknown}"
```

**JSONL emit shape (5 fields):**
```json
{"ts":"<ISO8601>","agent":"<serial>","tool":"<tool>","kind":"loop|work","session_id":"<id>"}
```

**Kind taxonomy (2-class):** `work` (default) | `loop` (specific MCP polls + Bash inbox-watch/check-inbox/kill-orphans + Skill loop/stimulus-scan).

**Failure handling:** silent-fail by design (per script comment line 25); no audit-trail logging.

---

## §2 — 6 gaps surfaced vs §3 spec

| # | Gap | Severity | Spec ref | Resolution path |
|---|---|---|---|---|
| 1 | **Tilde-lane full-serial capture vulnerability** — `.comp-graph/.agent_context:SERIAL` is workspace-local + shared across lanes; `$OPAL_AGENT_SERIAL` not canonically set by `org/XXX.md` Step 1b. Two lane-agents sharing cwd would have the LATER agent overwrite the EARLIER agent's SERIAL value. | CRITICAL | §3.5 + §7 | v0.2 §7 — session-id-keyed serial file pattern adopted (see §3 below) |
| 2 | **JSONL shape mismatch** — current 5 fields; spec wants 7 (`ts` epoch + `ts_iso` separately; field rename `agent`→`serial`, `tool`→`tool_name`; new `bg_task` field for lifecycle). | HIGH | §3.4 | WB-1.2 additive (preserve old field names for dual-read transitionally) |
| 3 | **`broker_record_tool_call` hot-path not wired** — current writes jsonl only; spec §3.1 wants BOTH jsonl audit trail AND broker hot-path. | HIGH | §3.1 + §2 | WB-2 (depends on broker code amendment landing) |
| 4 | **Kind taxonomy mismatch** — current 2-class (work/loop); spec 3-class (work/upkeep/watcher). "loop" is semantically rough-equivalent to "upkeep + watcher" combined; spec wants them separated. | MEDIUM | §3.2 + §3.3 | WB-3 semantic refinement |
| 5 | **`bg_task` lifecycle entries entirely missing** — current emits one entry per tool call; spec §4 wants `bg_start` at task launch + `bg_complete` at task-notification arrival for inbox-watch / terraform apply / long-SSM tracking. | MEDIUM-HIGH | §4 | WB-4 — depends on Claude Code lifecycle hook coverage check |
| 6 | **Hook-failure-logging gap** — current silent-fails to user (correct primary discipline) but does NOT log to `org/mcp/hook_errors.log`. Spec §3.6 wants silent-fail-to-user + loud-log-to-operator-audit-trail. | LOW | §3.6 | WB-1.3 (additive) |

---

## §3 — §3.5 CRITICAL — session-id-keyed serial file pattern (adopted by spec v0.2)

### §3.1 — Why v0.1's broker-lookup proposal had structural issues

v0.1 §7 recommended "if either source [`.comp-graph/.agent_context` / `$OPAL_AGENT_SERIAL`] is stale/shared across lanes, fix as part of Phase 1: hook reads from a per-session deterministic source (e.g., Claude Code passes `$CLAUDE_AGENT_SERIAL` if available; otherwise hook fails-loud rather than fails-quiet)."

The implied resolution path was: hook → broker → look up serial keyed on session-id.

Two issues with that:

1. **Broker outage breaks serial resolution during the outage window.** Hook needs to record EVERY tool call's serial. If broker is down → hook can't resolve serial → telemetry entry serial-less → broker warm-start recovery later can't rebuild correct liveness from those records. Cascading reliability failure.

2. **Per-call broker round-trip adds latency multiplied across all tool calls fabric-wide.** Hook fires on every tool call. Broker round-trip is ~ms; local file read is ~μs. Difference is ~1000x. Per-cycle cost adds up.

### §3.2 — Session-id-keyed pattern (cleaner)

The session-id IS in the hook input stdin per spec §3.4 JSONL example. We can leverage it:

**Session-start ritual** (org/XXX.md Step 1b additive):
```bash
mkdir -p org/mcp/sessions
echo "{full-suffixed-serial}" > "org/mcp/sessions/${CLAUDE_SESSION_ID}.serial"
```

(Requires Claude Code to expose session_id at session start; if unavailable at startup, back-fill on first hook fire by reading session_id from stdin and writing the file — chicken-and-egg solved by org/XXX.md Step 1b ordering — register_agent fires before any other tool call.)

**Hook read:**
```bash
SESSION_ID=$(echo "$HOOK_INPUT" | jq -r '.session_id // ""' 2>/dev/null)
if [ -n "$SESSION_ID" ] && [ -f "$REPO_ROOT/org/mcp/sessions/${SESSION_ID}.serial" ]; then
    AGENT=$(cat "$REPO_ROOT/org/mcp/sessions/${SESSION_ID}.serial" 2>/dev/null | head -1 | tr -d '\r\n')
    SERIAL_SOURCE="session-keyed"
fi
# fallback chain continues...
```

**Fail-loud-to-audit-trail when fallback level > primary:**
```bash
if [ "$SERIAL_SOURCE" != "session-keyed" ]; then
    printf '{"ts":"%s","level":"WARN","session_id":"%s","fallback_source":"%s","reason":"session-keyed file missing"}\n' \
        "$TS" "$SESSION_ID" "$SERIAL_SOURCE" >> "$REPO_ROOT/org/mcp/hook_errors.log" 2>/dev/null
fi
```

### §3.3 — Properties of the session-id-keyed approach

- **Per-session deterministic** — each Claude Code session gets its own file keyed on its unique session_id
- **Tilde-lane-safe** — base-serial session writes `{uuid-A}.serial = "0.7.0_AE_CloudOps"`; ~B-lane session writes `{uuid-B}.serial = "0.7.0_AE_CloudOps~B"`; hook reads the correct one per the session_id stamped on each tool call
- **Survives broker outage** — no broker call on hook critical path
- **Hot-path performance** — local file read is microseconds vs ms broker round-trip
- **Chicken-and-egg solved** — Step 1b ordering: register_agent (which writes the file) runs before any other tool call, so by the time the first tool call's hook fires, the file exists
- **GC discipline** — 24h post-last-activity cron sweep removes stale session files (per spec §7.4)

### §3.4 — Spec v0.2 adoption

ws CTO ratified the pattern in v0.2 (`4a0bb72d6`):
- §7.2 — session-id-keyed pattern PRIMARY recommendation
- §7.3 — NEW section explicitly rationalizing why session-id-keyed > broker-lookup (both reasons above)
- §7.4 — fallback chain (env var → .comp-graph → `_unknown_lane_check_needed` with audit-trail WARN); GC at 24h post-last-activity
- Broker-lookup retained as Phase-1 dual-read REDUNDANCY CHECK only (mismatches flag session-init bugs)

---

## §4 — Other gap resolutions per ws CTO routing

ws CTO `[AUDIT-ABSORBED + ROUTING-VERDICT]` §2 verdict: gaps #2-#6 are implementation-detail refinements that surface at the natural WB-phase boundaries:

- **WB-1.2** — §3.4 JSONL shape additive (add new fields; keep old field names for one cycle for dual-read compat)
- **WB-1.3** — §3.6 hook_errors.log fail-loud-to-audit-trail addition
- **WB-2** — §3.1 broker_record_tool_call hot-path wiring (depends on §2 broker code amendment landing first)
- **WB-3** — §3.2/§3.3 3-class kind taxonomy semantic refinement
- **WB-4** — §4 bg_task lifecycle entries (depends on Claude Code lifecycle hook coverage check — task-notification PostToolUse fires empirically per current bg-task inbox-watch-relaunch pattern; if confirmed bg_complete is emittable, else broker derives from timeout-vs-max_duration check)

Not spec-revision-class; lands at natural WB-phase boundaries.

---

## §5 — WB-1.1 code patch pre-positioned

Per ws CTO routing-verdict (c): wrote the actual session-id-keyed serial-resolution patch as a standalone proposal artifact rather than committing to `.tools/hooks/post-tool-telemetry.sh` directly. Pre-ratify discipline: patch lives at `org/tier2_senior/0.7.0_AE_CloudOps/proposals/ld0070_wb11_hook_patch.md`; when MSTR + ws CVO ratify WB-1 + ws CTO approves the patch shape, I apply the diff + commit to the live hook.

See `proposals/ld0070_wb11_hook_patch.md` for the patch details.

---

## §6 — Banking notes

- ws CTO banked this cycle as "15th anchor candidate: design-spec-receives-impl-audit-pre-ratify" pattern (per their MCP §5). Sister to `feedback_self_correction_upstream_of_verify_channel`.
- The pattern: design spec landing → impl-side audit BEFORE commit → spec refinement BEFORE MSTR ratification. Cleaner than design-spec → MSTR ratify → impl discovers gaps post-ratify → require spec amendment via re-ratify.
- The session-id-keyed pattern itself worth banking standalone for future reference if telemetry-pipeline-class work recurs. Candidate AE auto-memory entry.

---

## Compiler Tools

| Tool | Run | Result |
|---|---|---|
| `comp-trace` | Not run | TRACE-class audit operated on workspace artifacts (`.tools/hooks/` + `.claude/settings.local.json` + spec doc); cross-reference was line-by-line vs spec §3, not graph traversal. No comp-trace value-add. |
| `comp-blast` | Not run | No workspace node modified this session (audit-only; no code commit to the hook). |
| Grep + Read | Used extensively | Read `.tools/hooks/post-tool-telemetry.sh` + `.claude/settings.local.json` PostToolUse hook config + spec §3 + §7. |

## Mandatory Logging

- `org/compiler-tools-log.md` — no comp-* runs this session (justified above).

## Authority Trail

- ws CTO `[CASE_FIND-v0.2-SHIPPED + ...]` MCP §3 audit offer 2026-05-26T~00:40Z
- This session: 6-gap audit MCP'd ws CTO 2026-05-26T~01:13Z
- ws CTO `[AUDIT-ABSORBED + ROUTING-VERDICT]` MCP 2026-05-26T~01:18Z — spec v0.2 shipped + routing-verdict (a)+(c)
- This log filed per routing-verdict (a) durable-log requirement

## Cross-references

- `docs/architecture/TELEMETRY_LIVENESS_FRAMEWORK.md` (v0.2 `4a0bb72d6`)
- `org/tier0/ledger/LD-0070.md`
- `org/tier2_senior/0.7.0_AE_CloudOps/proposals/ld0070_wb11_hook_patch.md` (the actual patch)
- `.tools/hooks/post-tool-telemetry.sh` (current implementation; target of WB-1.1 patch)
- `.claude/settings.local.json` (PostToolUse hook config)
- AE auto-memory candidate: `reference_session_id_keyed_serial_resolution.md` (if telemetry-pipeline-class work recurs)

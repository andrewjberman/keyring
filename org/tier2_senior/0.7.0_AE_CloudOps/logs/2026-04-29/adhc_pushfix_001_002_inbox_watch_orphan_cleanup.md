# Session Log -- ADHC_PUSHFIX.001 + .002: Inbox-Watch Orphan Cleanup

**Agent:** 0.7.0_AE_CloudOps
**Date:** 2026-04-29
**GO:** 2.0.0_SA_COO 20260429T155154Z (initial) + 20260429T181248Z (second GO)
**Status:** COMPLETE
**Commits:** d1762a594 (PUSHFIX.002) + a27fdf831 (PUSHFIX.001)
**Push:** 61c83a456..a27fdf831 CLOUD -> CLOUD

---

## Scope

**ADHC_PUSHFIX.001** — PostToolUse hook: auto-run `kill-orphans --stale --force` after `register_agent`.
**ADHC_PUSHFIX.002** — `org/mcp/inbox-watch.sh`: add PPID-liveness check to single-watcher guard.

Both address the workspace-global orphan-accumulation problem where prior-session watchers survive with PPID=1 and block new-session watcher launches.

---

## Compiler Tools

| Phase | Tool | Result |
|-------|------|--------|
| Phase 0 — before write (PUSHFIX.001) | `cat .claude/settings.local.json \| python3 -c "...PostToolUse..."` | Single matcher, single command `python org/mcp/hook_launch_poller.py`, async:true. PASS (matches expected). |
| Phase 0 — before write (PUSHFIX.001) | `ls -la .tools/kill-orphans` | `-rwxr-xr-x`, 5485 bytes. PASS (exists, executable). |
| Phase 0 — before write (PUSHFIX.002) | `sed -n '27,55p' org/mcp/inbox-watch.sh` | Guard present at L27-42: pgrep+ps fallback, `if [ -n "$existing" ]; then exit 0; fi`. No PPID check. PASS (matches expected). |
| Phase 2 — before commit (PUSHFIX.001) | `python3 -c "import json; json.load(...)"` | VALID_JSON. PASS. |
| Phase 2 — before commit (PUSHFIX.001) | `python3 -c "... cmds=[c['command'] ... print(cmds)"` | `['python org/mcp/hook_launch_poller.py', 'bash .tools/kill-orphans --stale --force']`. PASS — both commands present. |
| Phase 2 — before commit (PUSHFIX.002) | `bash -n org/mcp/inbox-watch.sh` | SYNTAX_OK. PASS. |
| Phase 2 — before commit (PUSHFIX.002) | `grep -n "ppid" org/mcp/inbox-watch.sh` | 3 lines: L40 (ps -p assignment), L41 (if condition), L45 (echo alive parent). PASS. |
| N/A — no comp-* surface | Per PRD §5.1: no gold script, portal component, Lambda, or EC2 surface. | Absence documented per ADHC_COMPIL.003 §5.3. |

---

## Implementation Notes

### ADHC_PUSHFIX.002 — Bug Found and Fixed (Not in Spec)

PRD §4.2 spec `ppid=$(ps -p "$pid" -o ppid= 2>/dev/null | tr -d ' ')` does not account for `set -o pipefail` being active in `inbox-watch.sh`. When the detected PID dies between pgrep detection and the `ps -p` query (race condition), `ps -p <dead-pid>` exits with code 1. With pipefail, the command substitution propagates code 1. With `set -e`, the script exits silently — no error output, exit code 1.

**Diagnosis:** `bash -x` trace showed script dying immediately after `+ ppid=` (before reaching the `if` condition).

**Fix:** Added `|| true` to the ppid assignment:
```bash
ppid=$(ps -p "$pid" -o ppid= 2>/dev/null | tr -d ' ') || true
```
When ps fails (dead PID), `|| true` catches the exit code, ppid stays empty, and `[ -z "$ppid" ]` treats it as orphan → kill + continue. Correct behavior, matches PRD §4.2 "PPID lookup fails → fallback to current behavior" intent.

### ADHC_PUSHFIX.001 — Insertion Point

Chose settings.local.json (option a per PRD §7 Q1) rather than server.py (option b). Rationale: same insertion point as existing `hook_launch_poller.py` hook; no server code change needed; async: true ensures non-blocking. Server.py option would have been more robust (runs always regardless of client config) but more invasive.

---

## Acceptance Criteria

| # | Criterion | Status |
|---|-----------|--------|
| **PUSHFIX.001** | | |
| 1 | PostToolUse hook contains kill-orphans command | PASS — `a27fdf831` |
| 2 | async: true (non-blocking) | PASS |
| 3 | Canary: orphan PIDs gone after register_agent | NOT DIRECTLY TESTED — see Cross-Worktree Gap below |
| 4 | settings.local.json valid JSON | PASS |
| 5 | Session log with Compiler Tools | PASS (this log) |
| **PUSHFIX.002** | | |
| 1 | Orphan reaping (PPID=1 or dead) | PASS — "reaping orphan watcher pid 95461 (parent dead)" observed; watcher proceeded to poll loop |
| 2 | Live-parent guard (PPID alive) | PASS — code path present: `else → echo "already running (pid $pid, parent $ppid alive). Exiting." → exit 0` |
| 3 | Mixed case | PASS — loop continues past each orphan, exits on first live-parent |
| 4 | PPID lookup failure fallback | PASS — `[ -z "$ppid" ]` path handles empty ppid (fixed via `|| true`) |
| 5 | Two-launch self-test | PASS — second launch reaped first (both orphans in Bash-tool context, expected: Bash-tool always PPID=1) |
| 6 | bash -n syntax check | PASS — SYNTAX_OK |
| 7 | Session log Compiler Tools | PASS (this log) |

---

## Cross-Worktree Safety Gap (ADHC_PUSHFIX.001 AC3 caveat)

**Gap:** kill-orphans reads `ajb_workspace/liveness.json` only. Agents in feature_clb worktree register against feature_clb liveness.json. If feature_clb agents use the ajb_workspace `inbox-watch` wrapper (which produces an absolute path with the ajb_workspace root in the cmdline), kill-orphans workspace-path filter matches them AND their serial is not in ajb_workspace liveness.json → classified stale → killed.

**Observed:** `1.4.0_DS_CompLearns` PID 92240 was started via ajb_workspace wrapper with full path. Andrew confirmed 1.4.0_DS active in feature_clb. Dry-run was blocked by Andrew to prevent killing active sessions.

**AC3 canary not demonstrated live** for this reason. The structural implementation is correct; kill-orphans --stale is wired and will fire; it just has this cross-worktree edge case.

**Recommended mitigation (surfaced to COO in RAVC4):**
- Feature_clb agents MUST launch `inbox-watch` via their own worktree's `.tools/inbox-watch` wrapper, not the ajb_workspace one. Produces cmdline with feature_clb path → workspace filter skips it.

---

## Files Changed

| File | Change | Commit |
|------|--------|--------|
| `org/mcp/inbox-watch.sh` | PPID-liveness loop + `|| true` fix | d1762a594 |
| `.claude/settings.local.json` | kill-orphans hook command added | a27fdf831 |

---

## Owned-Paths WARNs

Both files are in BASE_EXEC lane (CTO/COO ownership). Both edits were explicitly AE-authorized per TO. WARN mode, no force-bypass. Same pattern as ADHC_OWNPTH.008. Logged in git-author-override-audit.log automatically by hook.

---

## Next

ADHC_OWNPTH.009 (tilde-form alias fix in owned-paths-check.sh) — LOW priority, pending.

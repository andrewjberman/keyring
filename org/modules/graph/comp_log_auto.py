"""
comp_log_auto.py -- auto-append compiler tool runs to compiler-tools-log.md

Called by every comp-* wrapper after the tool finishes:
    python comp_log_auto.py <tool_name> <args_string> <exit_code>

Reads agent context from .comp-graph/.agent_context:
    SERIAL=0.4.0_DS_ClientPlatform
    TO_ID=ADVI_OFFICE.W1

Deduplicates: skips append if the same tool+args ran within 30 seconds.
Silently no-ops on any error -- never disrupts the calling tool.

NFRA_COMPLEARN AMD-P3c (ingestion honesty, 2026-07-10, 0.8.0_AE_CloudComp~E): a DROPPED emission is no
longer swallowed silently. "Silently no-ops" preserved for the CALLER (this logger never disrupts the tool
it logs), but a drop now leaves a DISCLOSURE (a count/marker in .comp-graph/.comp_log_drops, else stderr)
-- because a silent-noop writer means the loop's own freshness/health signal can undercount invisibly, and
an error log is a census of SURVIVED failures (R5/R7). See _disclose_drop.

Log row format (matches compiler-tools-log.md table):
    | DATE | AGENT | TO_ID | TOOL | COMMAND | RESULT |
"""

from __future__ import annotations

import os
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Optional


def _workspace() -> Path:
    """Resolve workspace root: three directories above this file.
    File lives at org/modules/graph/comp_log_auto.py
    .parent -> org/modules/graph
    .parent.parent -> org/modules
    .parent.parent.parent -> org
    .parent.parent.parent.parent -> workspace root
    """
    return Path(__file__).resolve().parent.parent.parent.parent


def _disclose_drop(workspace: Optional[Path], tool: str, reason: str) -> None:
    """NFRA_COMPLEARN AMD-P3c (R5/R7 ingestion honesty): a comp_log_auto emission that is DROPPED (log file
    absent, write failure, or any exception in the emission path) is DISCLOSED, not swallowed. Appends one
    record to <workspace>/.comp-graph/.comp_log_drops so a dropped row leaves a COUNT (line count) + MARKER
    (file existence) an audit / health check can read -- a silent-noop writer would let the loop's own
    freshness signal undercount invisibly (the very "census of survived failures" hole this project closes).

    GRADED + NEVER-RAISES (the 'never disrupt the caller' invariant is preserved): marker file -> stderr ->
    last-resort pass. The bare pass is reachable ONLY after a visible signal (stderr) was attempted, so the
    drop is never fully silent. Record format: ISO-ts|tool|reason (ASCII, one line)."""
    ts = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    line = f"{ts}|{tool}|{reason}\n"
    if workspace is not None:
        try:
            drop_file = workspace / ".comp-graph" / ".comp_log_drops"
            drop_file.parent.mkdir(parents=True, exist_ok=True)
            with open(drop_file, "a", encoding="utf-8") as fh:
                fh.write(line)
            return
        except Exception:
            pass  # marker unwritable -> fall through to the stderr last-resort (still not silent)
    try:
        sys.stderr.write(f"COMP_LOG_AUTO_DROP: {line}")
    except Exception:
        pass  # only reachable if BOTH the marker file AND stderr are unavailable


def _read_session_file(path: Path) -> str:
    """Read a single-value session-keyed file (org/mcp/sessions/<sid>.serial|.to_id).
    Returns the stripped first non-empty line, or '' on any error/absence."""
    try:
        if path.exists():
            for line in path.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if line:
                    return line
    except Exception:
        pass
    return ""


def _read_context(workspace: Path) -> tuple[str, str]:
    """Resolve SERIAL and TO_ID with precedence: env -> session-keyed file -> shared file.

    Precedence (MSTR-FINDING fix 2026-06-22, mirrors the LD-0070 session-keyed .serial
    mechanism): the shared .comp-graph/.agent_context is a SINGLE global file overwritten by
    every agent ("printf > .agent_context"), so it is last-writer-wins across concurrent
    agents -- TO_ID (assigned post-spawn, never an env var) got cross-attributed to whichever
    agent wrote .agent_context most recently, corrupting the per-TO coverage attribution.
    The fix: a per-session file org/mcp/sessions/<CLAUDE_CODE_SESSION_ID>.{serial,to_id}
    (race-free; the .serial half is already the canonical LD-0070 source). Shared file stays
    as a legacy last-resort so pre-fix launches still log.
    """
    serial = os.environ.get("OPAL_AGENT_SERIAL", "")
    to_id = os.environ.get("OPAL_TO_ID", "")
    to_id_source = "env" if to_id else None

    # session-keyed tier (race-free per-session source)
    sid = os.environ.get("CLAUDE_CODE_SESSION_ID", "")
    if sid:
        sess_dir = workspace / "org" / "mcp" / "sessions"
        if not serial:
            serial = _read_session_file(sess_dir / f"{sid}.serial")
        if not to_id:
            to_id = _read_session_file(sess_dir / f"{sid}.to_id")
            if to_id:
                to_id_source = "session"

    context_file = workspace / ".comp-graph" / ".agent_context"
    if context_file.exists():
        try:
            for line in context_file.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if "=" not in line:
                    continue
                key, _, val = line.partition("=")
                key = key.strip()
                val = val.strip()
                if key == "SERIAL" and not serial:
                    serial = val
                elif key == "TO_ID" and not to_id:
                    to_id = val
                    to_id_source = "shared"
        except Exception:
            pass

    # RACE-EXPOSED MARKER (CVO TO-5 spec 2026-06-22): a sid-having session that fell through to the
    # raceable shared .agent_context for TO_ID (didn't run comp-to) gets a "(shared)" tag, so TO-5
    # coverage analysis can filter/down-weight cross-attribution-prone rows. A clean TO_ID under a
    # set sid == race-safe (env/session-sourced). No sid (non-Claude-Code shell) -> plain, no marker.
    if sid and to_id and to_id_source == "shared":
        to_id = to_id + " (shared)"

    return (serial or "(unknown)", to_id or "(no-TO)")


def _is_duplicate(workspace: Path, dedup_key: str, window_secs: int = 30) -> bool:
    """Return True if this exact command ran within window_secs seconds.
    Also writes the current timestamp to the dedup tracker.
    """
    dedup_file = workspace / ".comp-graph" / ".comp_dedup"
    now = int(time.time())

    # Check for recent duplicate
    if dedup_file.exists():
        try:
            lines = dedup_file.read_text(encoding="utf-8").splitlines()
            for line in reversed(lines):
                # Format: timestamp|dedup_key
                if "|" not in line:
                    continue
                ts_str, _, stored_key = line.partition("|")
                if stored_key == dedup_key:
                    try:
                        ts = int(ts_str)
                        if (now - ts) < window_secs:
                            return True
                    except ValueError:
                        pass
                    break  # Found this key's last run; it's old enough
        except Exception:
            pass

    # Write new entry, keep last 200 entries
    try:
        dedup_file.parent.mkdir(parents=True, exist_ok=True)
        existing = []
        if dedup_file.exists():
            existing = dedup_file.read_text(encoding="utf-8").splitlines()
        existing.append(f"{now}|{dedup_key}")
        # Keep tail to prevent unbounded growth
        if len(existing) > 200:
            existing = existing[-200:]
        dedup_file.write_text("\n".join(existing) + "\n", encoding="utf-8")
    except Exception:
        pass

    return False


# NFRA_TOOLCHECK.P1/P2 (CTO refinement 2026-07-08, 0.8.0_AE_CloudComp~D): a nonzero exit is NOT a tool
# FAILURE for a tool whose exit code is a CONTRACTED VERDICT -- a tri-state integrity/parity result, or a
# gate firing on a real violation. Blanket-mapping nonzero -> "FAIL" (the old line) is what produced the
# false comp-drift 50% (its exit-2 = UNVERIFIABLE tri-state, working-as-designed, miscounted) and the
# gate-firing over-count. For these tools a nonzero exit records "VERDICT": result_class() maps an
# unrecognized label to 0.5-NEUTRAL (not 0.0-fail) AND the raw "| FAIL |" log-mining stops counting it, so
# both the health USED/EFFECTIVE axis and the fail-% stop miscounting. Regular tools keep PASS/FAIL -- a
# nonzero IS a failure for a tool with no verdict-exit contract. NOTE (CTO): a genuine crash of a VERDICT
# tool is indistinguishable from an honest verdict by exit-code alone; "VERDICT" honestly marks the row
# "not-a-clean-fail" rather than asserting PASS -- it neither hides a crash as success nor libels a working
# verdict as a failure. Set sourced from the comp-tools.yaml exit-contracts + the NFRA_TOOLCHECK P1 matrix.
VERDICT_EXIT_TOOLS = frozenset({
    "comp-drift", "comp-lambdamap", "comp-xray", "comp-parity",          # tri-state (integrity / parity / scope)
    "comp-validate", "comp-manifest-check", "comp-surface-check", "comp-honesty",  # gate-firing (real violation found)
})


def _classify_result(tool: str, exit_code: int) -> str:
    """PASS on exit 0; a contracted non-zero VERDICT (tri-state / gate-fired) for a VERDICT_EXIT_TOOL;
    else FAIL. This is the single-point fix for the exit-code miscount (was: nonzero -> FAIL for all)."""
    if exit_code == 0:
        return "PASS"
    if tool in VERDICT_EXIT_TOOLS:
        return "VERDICT"
    return "FAIL"


def _append_log(workspace: Path, tool: str, args: str, exit_code: int,
                serial: str, to_id: str) -> None:
    """Append one structured row to compiler-tools-log.md."""
    log_file = workspace / "org" / "compiler-tools-log.md"
    if not log_file.exists():
        # DISCLOSE, don't swallow (R5/R7): an absent log file silently drops EVERY emission -- exactly the
        # "loop freshness signal undercounts invisibly" hole. Surface it instead of a bare return.
        _disclose_drop(workspace, tool, "log-file-absent")
        return

    date = datetime.now().strftime("%Y-%m-%d")
    result = _classify_result(tool, exit_code)

    # Synthetic-fixture marking (NFRA_TOOLCHECK P2, log-signal-honesty): a DELIBERATE test-fixture run --
    # one engineered to FAIL to exercise a tool's failure path (e.g. `comp-validate definitely_not_a_thing`,
    # ADHC_COMPIL.012) -- sets COMP_SYNTHETIC_FIXTURE=1 so its row is tagged "(SYNTHETIC TEST FIXTURE)". The
    # fail-% mining + health analysis then EXCLUDE it, so a synthetic fail is no longer indistinguishable
    # from a real one (was 1/1302 marked -> the raw fail-% over-counted). Fixtures opt in via the env var;
    # a normal run is never tagged. The tag lives in the RESULT cell (grep-excludable by the miner).
    if os.environ.get("COMP_SYNTHETIC_FIXTURE", "").strip().lower() in ("1", "true", "yes", "on"):
        result = f"{result} (SYNTHETIC TEST FIXTURE)"

    # Truncate long arg strings for readability
    command = f"{tool} {args}".strip()
    if len(command) > 90:
        command = command[:87] + "..."

    row = f"| {date} | {serial} | {to_id} | {tool} | {command} | {result} |\n"

    try:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(row)
    except Exception as e:
        # DISCLOSE, don't swallow (R5/R7): a failed append is a dropped emission -- surface a count/marker.
        _disclose_drop(workspace, tool, f"append-failed: {type(e).__name__}")

    # SECOND-GRANULARITY RUN SINK (NFRA_COMPCLOSE 2026-07-14) -- the missing half of the
    # route->run outcome join. The markdown row above is DAY-granular by design, and the
    # charter-2 join window is 300 SECONDS: measured, 15,842 of 15,904 rolling-corpus rows
    # carried ts_epoch == midnight-ET, so the join returned no_signal on 6,508 of 6,509
    # joinable routes -- `outcome: null` on every training row was ARITHMETIC, not accident
    # (a window 288x finer than its corpus's clock can never match). This jsonl row carries
    # the real clock. Same caller-safety invariant: any failure discloses, never raises.
    try:
        import json as _json
        runs_sink = workspace / "org" / "mcp" / "comp-tool-runs.jsonl"
        rec = {"ts_epoch": time.time(), "serial": serial, "to_id": to_id, "tool": tool,
               "args_head": command[:80], "rc": exit_code, "result": result,
               "session_id": os.environ.get("CLAUDE_CODE_SESSION_ID", "")}
        with open(runs_sink, "a", encoding="utf-8") as f:
            f.write(_json.dumps(rec, ensure_ascii=True) + "\n")
    except Exception as e:
        _disclose_drop(workspace, tool, f"runs-sink-append-failed: {type(e).__name__}")


def main():
    if len(sys.argv) < 4:
        return  # Called with wrong args -- silent no-op

    tool = sys.argv[1]
    args = sys.argv[2]
    try:
        exit_code = int(sys.argv[3])
    except (ValueError, IndexError):
        exit_code = 0

    try:
        workspace = _workspace()
        serial, to_id = _read_context(workspace)

        # Dedup key: serial + to_id + tool + args (normalized). to_id is in the key (CVO TO-5 spec
        # 2026-06-22) so the SAME command run under TWO different TOs inside the 30s window both log
        # -- without it, a rapid comp-to switch + repeated command dedups away the new TO's first row.
        args_normalized = " ".join(args.split())  # collapse whitespace
        dedup_key = f"{serial}|{to_id}|{tool}|{args_normalized}"

        if _is_duplicate(workspace, dedup_key, window_secs=30):
            return  # Same agent ran same command within 30s -- skip

        _append_log(workspace, tool, args_normalized, exit_code, serial, to_id)

    except Exception as e:
        # DISCLOSE, don't swallow (R5/R7): a dropped emission surfaces a count/marker rather than a silent
        # pass. workspace may be UNBOUND if _workspace() itself raised -> locals().get returns None and
        # _disclose_drop falls back to stderr (never silent). tool is bound before the try, so it is safe.
        _disclose_drop(locals().get("workspace"), tool, f"main-exception: {type(e).__name__}")


if __name__ == "__main__":
    main()

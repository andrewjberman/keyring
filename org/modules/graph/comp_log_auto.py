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
from datetime import datetime, timezone
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
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")  # Law-11: explicit Z
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


def _seat_session_key(sid: str, seat: str) -> str:
    """<sid>.<serial sanitized as the launcher does> -- the key comp-to and comp-which write when a seat is known.
    A session id alone is not a seat: Codex children launched from one Claude seat share their parent's id."""
    import re as _re
    return "%s.%s" % (sid, _re.sub(r"[^A-Za-z0-9_.~-]", "_", seat)) if seat else sid


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
            # SEAT + SESSION KEY FIRST (2026-09-03, row NFRA_COMPEFFICACY-S28): Codex children launched from one
            # Claude seat inherit its session id, so the bare <sid>.to_id was last-writer-wins across ten lanes.
            # comp-to now writes <sid>.<serial>.to_id when OPAL_AGENT_SERIAL is set; the bare key is the legacy read.
            to_id = _read_session_file(sess_dir / f"{_seat_session_key(sid, serial)}.to_id") if serial else ""
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


# NFRA_MSBEFF.R1R3 / M3 (2026-07-23, 0.8.0_AE_CloudComp): the verdict-set is DERIVED, not frozen.
#
# A nonzero exit is NOT a tool FAILURE for a tool whose exit code is a CONTRACTED VERDICT (a tri-state
# integrity/parity result, a gate firing on a real violation) or a REFUSE (an honest could-not-check).
# Blanket-mapping nonzero -> "FAIL" (the original line) produced the false comp-drift 50% and the
# gate-firing over-count; a hand-frozen VERDICT_EXIT_TOOLS set then fixed that but DRIFTED from the source
# exit contracts silently (the 07-08 freeze + the 07-23 interim +3 were both hand-patches OF that frozen
# set). The M3 fix RETIRES the frozen set: classify_exit() now DERIVES the class from the enforced-complete
# output contracts (org/modules/graph/comp-output-contracts.yaml), and comp-manifest-check's output-contract
# member guarantees no tools_index tool goes undeclared. See comp_output_contract.py + that yaml's header for the
# full supersession history (condition c) -- do NOT re-freeze a verdict set here or anywhere.
#
# UNKNOWN IS NOT A VERDICT (condition b): a tool with no declared contract classifies its nonzero as UNKNOWN
# (loud, distinct from FAIL), never a defaulted PASS/FAIL. The fail-% miner and health axis must exclude
# UNKNOWN the same way they exclude VERDICT -- an undeclared tool's contracted nonzero is not a crash.
#
# FAIL-HONEST FALLBACK: if the derivation cannot load (yaml/helper unavailable), classification degrades to
# UNKNOWN for every nonzero rather than silently reverting to the buggy nonzero->FAIL blanket. A dropped
# derivation is DISCLOSED (never silently swallowed) -- a broken classifier that reads clean is the class
# this whole project closes.

try:
    from org.modules.graph import comp_output_contract as _oc
    _OC_OK = True
except Exception:  # pragma: no cover -- import-path fallback for direct-script invocation
    try:
        import comp_output_contract as _oc  # same-dir import when run as a bare script
        _OC_OK = True
    except Exception:
        _oc = None
        _OC_OK = False


def _classify_result(tool: str, exit_code: int) -> str:
    """PASS on exit 0; else the class DERIVED from the tool's declared output contract
    (VERDICT / REFUSE / FAIL), or UNKNOWN for an undeclared tool. Fail-honest: if the derivation is
    unavailable, an undeclared/unresolvable nonzero renders UNKNOWN, never a silent FAIL blanket."""
    if exit_code == 0:
        return "PASS"
    if _OC_OK and _oc is not None:
        try:
            return _oc.classify_exit(tool, exit_code)
        except Exception:
            return _oc.UNKNOWN if hasattr(_oc, "UNKNOWN") else "UNKNOWN"
    return "UNKNOWN"


# R8 (NFRA_VELOCITY_ESTATE WS-E6.R8, 2026-07-30) -- the CONSUME side of the route->run join.
# comp-which hands off `<route_id>|<emit_epoch>|<n_recommended>` to a race-free per-session file
# (org/mcp/sessions/<sid>.route); the NEXT comp-tool run stamps it here, so route->run becomes
# joinable. Before this, measured: 0 of 17,687 route events carried a serial and no run row
# carried a route id -- there was no key on EITHER side, so any conversion rate was fabricated.
#
# TTL, NOT SINGLE-USE (COO ruling 20260730T065315Z): a persistent id would let every later
# unrelated run inherit it and inflate conversion toward 100%; a single-use id under-credits a
# route that legitimately produced two runs. So the id survives for a generous window and the row
# records the route's AGE AT STAMP TIME -- a reader re-cuts the conversion window in analysis with
# no re-baseline. Same discriminator discipline as verdict_basis: keep the residue now, because it
# is unrecoverable later.
_ROUTE_TTL_S = 1800


def _carried_route(workspace: Path, tool: str) -> Optional[tuple]:
    """(route_id, age_seconds, n_recommended) for the route handed off to this run, or None.

    A comp-which row NEVER carries a route: a route must not convert itself. That is not
    bookkeeping -- self-conversion would make the rate rise with comp-which's own usage, which is
    precisely the quantity the rate is supposed to be measured AGAINST.
    """
    if tool == "comp-which":
        return None
    sid = os.environ.get("CLAUDE_CODE_SESSION_ID", "")
    if not sid:
        return None
    try:
        # seat+session key first (comp-which writes it when OPAL_AGENT_SERIAL is set), bare session key second
        seat = os.environ.get("OPAL_AGENT_SERIAL", "")
        p = workspace / "org" / "mcp" / "sessions" / f"{_seat_session_key(sid, seat)}.route" if seat else None
        if p is None or not p.exists():
            p = workspace / "org" / "mcp" / "sessions" / f"{sid}.route"
        if not p.exists():
            return None
        raw = p.read_text(encoding="utf-8").strip()
        if not raw:
            return None
        parts = raw.split("|")
        rid = parts[0].strip()
        emitted = float(parts[1]) if len(parts) > 1 else 0.0
        n = int(parts[2]) if len(parts) > 2 else 0
        age = time.time() - emitted
        if not rid or age < 0 or age > _ROUTE_TTL_S:
            return None  # expired or clock-inverted -> no claim, rather than a wrong claim
        return (rid, round(age, 3), n)
    except Exception:
        return None


def _append_log(workspace: Path, tool: str, args: str, exit_code: int,
                serial: str, to_id: str) -> None:
    """Append one run record to the JSONL run sink.

    MARKDOWN APPEND RETIRED 2026-07-29, ANDREW-DIRECT (verbatim: "we need to completely take out
    any doctrine or hook or anything that would say to write to that compiler-tools-log.md file,
    its just constant commit nonsense"). SCOPE GUARD: this removed the WRITE, not the file --
    `org/compiler-tools-log.md` IS PRESERVED at its committed state and is still readable history.
    What is gone is the per-run auto-append that re-dirtied a TRACKED file on every comp-tool call,
    which forced a commit-or-discard decision on every agent before every pull.

    CUSTODY, verified before the write was cut: the JSONL sink below is written in this same
    function on the same call, so it already carried every row the markdown did -- 10,147 rows,
    873 in the trailing 24h at cut time -- at FINER granularity (real ts_epoch vs the markdown's
    day-granular date). Nothing was single-copy at the moment of the cut.

    KNOW WHAT THIS SINK IS, THOUGH: `org/mcp/comp-tool-runs.jsonl` is GITIGNORED (.gitignore:447),
    so it is DEVICE-LOCAL. It is not a durable cross-device record and must never be cited as one
    -- each device sees only its own runs. That is acceptable because the telemetry was ruled
    low-value by the owner, but a completeness claim over "the estate's comp-tool runs" read from
    this file is short by every other device's traffic, silently.
    """
    result = _classify_result(tool, exit_code)

    # Synthetic-fixture marking (NFRA_TOOLCHECK P2, log-signal-honesty): a DELIBERATE test-fixture run --
    # one engineered to FAIL to exercise a tool's failure path (e.g. `comp-validate definitely_not_a_thing`,
    # ADHC_COMPIL.012) -- sets COMP_SYNTHETIC_FIXTURE=1 so its row is tagged "(SYNTHETIC TEST FIXTURE)". The
    # fail-% mining + health analysis then EXCLUDE it, so a synthetic fail is no longer indistinguishable
    # from a real one (was 1/1302 marked -> the raw fail-% over-counted). Fixtures opt in via the env var;
    # a normal run is never tagged. The tag lives in the RESULT cell (grep-excludable by the miner).
    synthetic = os.environ.get("COMP_SYNTHETIC_FIXTURE", "").strip().lower() in ("1", "true", "yes", "on")
    if synthetic:
        result = f"{result} (SYNTHETIC TEST FIXTURE)"

    # E4.2 (NFRA_VELOCITY_ESTATE WS-E4.2, 2026-07-30): the FAIL column's three meanings,
    # separated as a TYPED FIELD in the machine record rather than as a text suffix a miner
    # has to grep-exclude. The suffix above is PRESERVED for the existing miners that key on
    # it -- this is additive, so nothing downstream breaks -- but `fail_kind` is the field a
    # new consumer should read. Derived from the tool's own declared exit contract, never a
    # frozen list here (E4.1 condition 1 applies one level down).
    #
    # WHY IT MATTERS, in one line: a RISING FAIL count is today indistinguishable from
    # BETTER NEGATIVE-CONTROLLING, which is a good thing reading as a bad one.
    #
    # `fail_kind` is None (key omitted) for any non-FAIL row, so a consumer can never read a
    # kind off a PASS. Both "I do not know" values (undeclared_rc / kind_undeclared) are LOUD
    # and are never defaulted into one of the three meanings.
    fail_kind = None
    if _OC_OK and _oc is not None:
        try:
            fail_kind = _oc.classify_fail_kind(tool, exit_code, synthetic=synthetic)
        except Exception:
            fail_kind = None  # never disrupt the caller; absence is honest, a guess is not

    # Truncate long arg strings for readability
    command = f"{tool} {args}".strip()
    if len(command) > 90:
        command = command[:87] + "..."

    # SECOND-GRANULARITY RUN SINK (NFRA_COMPCLOSE 2026-07-14) -- now the ONLY sink, since the
    # day-granular markdown append above it was retired 2026-07-29. It was already the better
    # record: the charter-2 join window is 300 SECONDS, and measured, 15,842 of 15,904
    # rolling-corpus markdown rows carried ts_epoch == midnight-ET, so the join returned
    # no_signal on 6,508 of 6,509 joinable routes -- `outcome: null` on every training row was
    # ARITHMETIC, not accident (a window 288x finer than its corpus's clock can never match).
    # This jsonl row carries the real clock. Caller-safety invariant: any failure discloses,
    # never raises -- a telemetry sink must never break the tool it is measuring.
    try:
        import json as _json
        runs_sink = workspace / "org" / "mcp" / "comp-tool-runs.jsonl"
        rec = {"ts_epoch": time.time(), "serial": serial, "to_id": to_id, "tool": tool,
               "args_head": command[:80], "rc": exit_code, "result": result,
               "session_id": os.environ.get("CLAUDE_CODE_SESSION_ID", "")}
        # Additive OPTIONAL keys (E4.2). Omitted when not applicable rather than written null,
        # so a reader cannot mistake "not a fail" for "kind unknown". Keeping these optional is
        # also what leaves the WS-E6/R8 route-id path open: a later field needs no schema
        # migration and no telemetry re-baseline.
        # E4.3 ELEMENT 1 (COO GO 20260730T072044Z): stamp the VERDICT BASIS at WRITE time.
        # Not optional and not conditional -- every row from here on is permanently
        # self-describing, so no future contract change can ever require re-baselining it. Rows
        # written BEFORE this landed carry no basis; that is the honest seam, and E4.1.3's
        # dual-basis machinery is what covers them. `derived_basis_id()` is drawn from
        # comp_output_contract so the appender and the re-baseline cannot diverge (one function).
        # Degrades to a LOUD sentinel rather than omitting the field: a row with no basis at all
        # would be indistinguishable from a pre-E4.3 row, which is the ambiguity this closes.
        if _OC_OK and _oc is not None:
            try:
                rec["verdict_basis"] = _oc.derived_basis_id()
            except Exception:
                rec["verdict_basis"] = "UNKNOWN-basis-unavailable"
        else:
            rec["verdict_basis"] = "UNKNOWN-basis-unavailable"
        if fail_kind is not None:
            rec["fail_kind"] = fail_kind
        if synthetic:
            rec["synthetic"] = True
        # R8: the route this run converted, if any. Absent when no route was handed off -- an
        # honest absence, never a null or a guess. `route_n` is carried so an ALL-of-N rate stays
        # derivable without a re-baseline (COO ruled ANY-of-N CONVERTS, 065315Z).
        carried = _carried_route(workspace, tool)
        if carried is not None:
            rec["route_id"], rec["route_age_s"], rec["route_n"] = carried
            rec["route_ttl_s"] = _ROUTE_TTL_S
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

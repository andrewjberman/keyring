"""
comp_log_auto.py -- auto-append compiler tool runs to compiler-tools-log.md

Called by every comp-* wrapper after the tool finishes:
    python comp_log_auto.py <tool_name> <args_string> <exit_code>

Reads agent context from .comp-graph/.agent_context:
    SERIAL=0.4.0_DS_ClientPlatform
    TO_ID=ADVI_OFFICE.W1

Deduplicates: skips append if the same tool+args ran within 30 seconds.
Silently no-ops on any error -- never disrupts the calling tool.

Log row format (matches compiler-tools-log.md table):
    | DATE | AGENT | TO_ID | TOOL | COMMAND | RESULT |
"""

import os
import sys
import time
from datetime import datetime
from pathlib import Path


def _workspace() -> Path:
    """Resolve workspace root: three directories above this file.
    File lives at org/modules/graph/comp_log_auto.py
    .parent -> org/modules/graph
    .parent.parent -> org/modules
    .parent.parent.parent -> org
    .parent.parent.parent.parent -> workspace root
    """
    return Path(__file__).resolve().parent.parent.parent.parent


def _read_context(workspace: Path) -> tuple[str, str]:
    """Read SERIAL and TO_ID from .comp-graph/.agent_context.
    Env vars OPAL_AGENT_SERIAL and OPAL_TO_ID take precedence.
    Returns (serial, to_id).
    """
    serial = os.environ.get("OPAL_AGENT_SERIAL", "")
    to_id = os.environ.get("OPAL_TO_ID", "")

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
        except Exception:
            pass

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


def _append_log(workspace: Path, tool: str, args: str, exit_code: int,
                serial: str, to_id: str) -> None:
    """Append one structured row to compiler-tools-log.md."""
    log_file = workspace / "org" / "compiler-tools-log.md"
    if not log_file.exists():
        return

    date = datetime.now().strftime("%Y-%m-%d")
    result = "PASS" if exit_code == 0 else "FAIL"

    # Truncate long arg strings for readability
    command = f"{tool} {args}".strip()
    if len(command) > 90:
        command = command[:87] + "..."

    row = f"| {date} | {serial} | {to_id} | {tool} | {command} | {result} |\n"

    try:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(row)
    except Exception:
        pass


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

        # Dedup key: serial + tool + args (normalized)
        args_normalized = " ".join(args.split())  # collapse whitespace
        dedup_key = f"{serial}|{tool}|{args_normalized}"

        if _is_duplicate(workspace, dedup_key, window_secs=30):
            return  # Same agent ran same command within 30s -- skip

        _append_log(workspace, tool, args_normalized, exit_code, serial, to_id)

    except Exception:
        pass  # Never fail loudly -- this is a side-effect logger


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""coo-drive-tick-gate.py -- Stop hook: a COO turn that ran /canonical-drive and fired no act must have run the empty-tick rule.

Andrew-direct 2026-10-13 ~21:1xZ at the 1.0.0_SA_CTO terminal, on 2.0.0_SA_COO~C's tick that labelled a wait "drive forward"
and skipped `/next-calls --drive`: "is there any way to gate this and make sure it is actually done as intended?" then
"Yeah get it incorporated". Record:
org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_211xZ_KEEP_DRIVING_EMPTY_TICK_GATE.md.

The rule it enforces (`.claude/skills/canonical-drive/SKILL.md` section 1, EMPTY TICK; section 3 hard gate): a tick that fires
no act is EMPTY whatever its label; with the `/keep-driving` empty_tick switch ON, an empty tick runs
`/next-calls <CODE> --drive` and ends with `python .tools/unblock.py tick ...` (`--owed-ledger` / `--owed-call` /
`--wait-until` record a legitimate wait).

It reads the TURN, not the agent's label. The turn is everything after the last genuine prompt in the transcript.
- Ran /canonical-drive: the prompt names it, a Skill call loads canonical-drive or drive, or the skill body is injected.
- Fired an act: an Agent spawn; a Skill call to dispatch, mstr-spawn or closer-drive; a send_message; or a Bash command
  running safe-commit, safe-merge, crossbox-call open/issue, spawn-agent or safe-apply.
- Empty-tick rule run: a Skill call (or prompt) for next-calls AND a Bash command running `unblock.py tick`.

On a miss it prints {"decision": "block", "reason": ...}, so the seat finishes the rule before the turn ends. It blocks once per
turn: with `stop_hook_active` set it passes, so it can never loop.

Cost: one transcript read per COO turn end, plus a ~2 s read of the switch only when a drive turn fired nothing.
Non-application: any serial that is not 2.0.0_SA_COO*, any turn without /canonical-drive, the switch OFF.
Fails OPEN on its own errors (unreadable transcript, unreadable switch), with one stderr line: a broken gate must never trap a seat.
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys

DRIVE_SKILLS = {"canonical-drive", "drive"}
ACT_SKILLS = {"dispatch", "mstr-spawn", "closer-drive"}
ACT_BASH = re.compile(r"safe-commit\.sh|safe-merge\.sh|crossbox-call\.py\s+(open|issue)|spawn-agent|safe-apply")
UNBLOCK_TICK = re.compile(r"unblock\.py\s+tick\b")
SERIAL_TOOLS = ("register_agent", "heartbeat")


def _blocks(entry):
    c = (entry.get("message") or {}).get("content")
    return c if isinstance(c, list) else []


def _text_of(entry):
    c = (entry.get("message") or {}).get("content")
    if isinstance(c, str):
        return c
    return "\n".join(b.get("text", "") for b in c or [] if isinstance(b, dict) and b.get("type") == "text")


def _is_prompt(entry):
    """A genuine prompt: a user entry that is not a tool result and not an injected skill body."""
    if entry.get("type") != "user":
        return False
    c = (entry.get("message") or {}).get("content")
    if isinstance(c, list) and c and isinstance(c[0], dict) and c[0].get("type") == "tool_result":
        return False
    return not _text_of(entry).startswith("Base directory for this skill:")


def read_turn(path):
    """(serial, prompt_text, entries_after_prompt) from a Claude Code transcript JSONL."""
    entries, serial = [], None
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                e = json.loads(line)
            except ValueError:
                continue
            entries.append(e)
            if e.get("type") == "assistant":
                for b in _blocks(e):
                    if b.get("type") == "tool_use" and str(b.get("name", "")).endswith(SERIAL_TOOLS):
                        serial = (b.get("input") or {}).get("agent_serial") or serial
    start = max((i for i, e in enumerate(entries) if _is_prompt(e)), default=-1)
    prompt = _text_of(entries[start]) if start >= 0 else ""
    return serial, prompt, entries[start + 1:]


LOG_PATH = re.compile(r"(drive_log_|/logs/|drive_ticks/|session_log|/handoffs/)")


def _log_only_commit(cmd):
    """A safe-commit whose named paths are all logs records the tick; it does not fire one."""
    if "safe-commit" not in cmd or " -- " not in cmd or re.search(r"safe-merge|crossbox-call|spawn-agent|safe-apply", cmd):
        return False
    paths = [p for p in re.split(r"\s+", cmd.split(" -- ", 1)[1].split("&&")[0].split(";")[0].split("|")[0].strip()) if p]
    return bool(paths) and all(LOG_PATH.search(p.replace("\\", "/")) for p in paths)


def classify(prompt, turn):
    """(ran_drive, fired_act, ran_next_calls, ran_unblock_tick) for one turn."""
    ran_drive = bool(re.search(r"/(canonical-)?drive\b", prompt))
    ran_next = "/next-calls" in prompt
    fired = ran_unblock = False
    for e in turn:
        if e.get("type") == "user" and "Base directory for this skill:" in _text_of(e):
            m = re.search(r"skills[\\/]+([A-Za-z0-9_-]+)", _text_of(e))
            ran_drive = ran_drive or bool(m and m.group(1) in DRIVE_SKILLS)
            ran_next = ran_next or bool(m and m.group(1) == "next-calls")
        if e.get("type") != "assistant":
            continue
        for b in _blocks(e):
            if b.get("type") != "tool_use":
                continue
            name, inp = str(b.get("name", "")), b.get("input") or {}
            if name == "Skill":
                sk = str(inp.get("skill", ""))
                ran_drive = ran_drive or sk in DRIVE_SKILLS
                ran_next = ran_next or sk == "next-calls"
                fired = fired or sk in ACT_SKILLS
            elif name == "Agent":
                fired = True
            elif name.endswith("send_message"):
                fired = True
            elif name in ("Bash", "PowerShell"):
                cmd = str(inp.get("command", ""))
                fired = fired or (bool(ACT_BASH.search(cmd)) and not _log_only_commit(cmd))
                ran_unblock = ran_unblock or bool(UNBLOCK_TICK.search(cmd))
    return ran_drive, fired, ran_next, ran_unblock


def switch_on(root):
    out = subprocess.run([sys.executable, os.path.join(root, ".tools", "open-calls.py"), "mode", "get", "--part", "empty_tick"],
                         capture_output=True, text=True, timeout=30, cwd=root).stdout
    m = re.search(r"KEEP-DRIVING-MODE .*state=(\w+)", out)
    if not m:
        raise RuntimeError("switch unreadable")
    return m.group(1) == "on"


def verdict(hook, root, switch=switch_on):
    """None to pass, else the block reason."""
    if hook.get("stop_hook_active"):
        return None
    serial, prompt, turn = read_turn(hook["transcript_path"])
    if not serial or not serial.startswith("2.0.0_SA_COO"):
        return None
    ran_drive, fired, ran_next, ran_unblock = classify(prompt, turn)
    if not ran_drive or fired:
        return None
    if ran_next and ran_unblock:
        return None
    if not switch(root):
        return None
    missing = [s for s, ok in (("/next-calls <CODE> --drive", ran_next), ("python .tools/unblock.py tick ...", ran_unblock)) if not ok]
    return ("EMPTY TICK (coo-drive-tick-gate, Andrew-direct 2026-10-13): this /canonical-drive turn fired no act (no spawn, "
            "commit, merge, send, crossbox order or apply), so it is an empty tick whatever its label, and /keep-driving "
            "empty_tick is ON. Before ending the turn, run: %s. A wait on another seat's live deploy or a held call is "
            "recorded with `unblock.py tick --owed-ledger <slug> --owed-owner <serial>` or `--owed-call <id>`. "
            "(.claude/skills/canonical-drive/SKILL.md section 1 EMPTY TICK)" % " and ".join(missing))


def main():
    try:
        hook = json.load(sys.stdin)
        root = os.environ.get("CLAUDE_PROJECT_DIR") or hook.get("cwd") or os.getcwd()
        reason = verdict(hook, root)
    except Exception as exc:  # noqa: BLE001 -- fail open: a broken gate must never trap a seat
        print("WARN: coo-drive-tick-gate skipped (%s)" % exc, file=sys.stderr)
        return 0
    if reason:
        print(json.dumps({"decision": "block", "reason": reason}))
    return 0


if __name__ == "__main__":
    sys.exit(main())

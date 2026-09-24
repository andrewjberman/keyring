"""memory_write_guard -- the decision behind .tools/hooks/memory-write-guard.sh (Andrew-direct 2026-09-24 ~17:0xZ).

For a Write or Edit whose file sits in a `.claude/projects/<project>/memory/` directory:
  - any file other than MEMORY.md is refused (seats stop writing lessons to memory);
  - MEMORY.md is refused when the write leaves it over CEILING bytes AND larger than it was (preferences-sized index).
Anything it cannot read admits the write. `--self-test` runs the arms in a tempdir.
"""
import json
import os
import re
import sys

CEILING = 3072  # a preferences-only index is about 2 KB
MEMDIR_RE = re.compile(r"/\.claude/projects/[^/]+/memory/([^/]+)$")


def _after_size(tool, ti, text):
    if tool == "Write":
        return len(str(ti.get("content") or "").encode("utf-8"))
    old, new = str(ti.get("old_string") or ""), str(ti.get("new_string") or "")
    if not old or old not in text:
        return len(text.encode("utf-8"))
    after = text.replace(old, new) if ti.get("replace_all") else text.replace(old, new, 1)
    return len(after.encode("utf-8"))


def verdict(payload):
    tool = payload.get("tool_name")
    ti = payload.get("tool_input") or {}
    path = str(ti.get("file_path") or "")
    m = MEMDIR_RE.search(path.replace("\\", "/"))
    if tool not in ("Write", "Edit") or not m:
        return None
    if m.group(1) != "MEMORY.md":
        return ("BLOCKED: seats do not write lessons to memory (Andrew-direct 2026-09-24). A lesson that matters becomes "
                "a gate, field or skill fix by its owning seat; an incident stays in git history. MEMORY.md holds his "
                "stable preferences only.")
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            text = fh.read()
    except FileNotFoundError:
        text = ""
    current, after = len(text.encode("utf-8")), _after_size(tool, ti, text)
    if after > CEILING and after > current:
        return ("BLOCKED: MEMORY.md would be %d bytes (preferences-only ceiling %d; now %d). It holds Andrew's stable "
                "preferences only; a lesson goes to a gate, field or skill fix instead." % (after, CEILING, current))
    return None


def main():
    try:
        why = verdict(json.loads(sys.stdin.read() or "{}"))
    except Exception:  # noqa: BLE001 -- the guard never wedges a seat
        return 0
    if why:
        print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "deny",
                                                 "permissionDecisionReason": why}}))
    return 0


def self_test():
    import tempfile
    ok = True
    with tempfile.TemporaryDirectory() as d:
        mem = os.path.join(d, ".claude", "projects", "P", "memory")
        os.makedirs(mem)
        idx = os.path.join(mem, "MEMORY.md")
        with open(idx, "w", encoding="utf-8") as fh:
            fh.write("x" * 1900)
        arms = [
            ("a new lesson file is refused", {"tool_name": "Write", "tool_input": {
                "file_path": os.path.join(mem, "feedback_x.md"), "content": "a lesson"}}, True),
            ("an Edit to another memory file is refused", {"tool_name": "Edit", "tool_input": {
                "file_path": os.path.join(mem, "reference_y.md"), "old_string": "a", "new_string": "b"}}, True),
            ("a preference edit that stays under the ceiling is admitted", {"tool_name": "Edit", "tool_input": {
                "file_path": idx, "old_string": "x" * 10, "new_string": "y" * 200}}, False),
            ("an index grown past 3 KB is refused", {"tool_name": "Write", "tool_input": {
                "file_path": idx, "content": "y" * 4000}}, True),
            ("a file outside any memory directory is never graded", {"tool_name": "Write", "tool_input": {
                "file_path": os.path.join(d, "notes", "feedback_x.md"), "content": "y" * 9000}}, False),
            ("a Windows-style path is recognised", {"tool_name": "Write", "tool_input": {
                "file_path": mem.replace("/", "\\") + "\\lesson.md", "content": "z"}}, True),
        ]
        for name, payload, want in arms:
            got = verdict(payload) is not None
            ok = ok and got == want
            print("  [%s] %s" % ("PASS" if got == want else "FAIL", name))
    print("SELF-TEST: %s" % ("ALL HOLD" if ok else "BROKEN"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(self_test() if "--self-test" in sys.argv else main())

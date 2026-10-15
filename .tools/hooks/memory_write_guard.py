"""memory_write_guard -- the decision behind .tools/hooks/memory-write-guard.sh (Andrew-direct 2026-09-24 ~17:0xZ).

For a Write or Edit whose file sits in a `.claude/projects/<project>/memory/` directory:
  - any file other than MEMORY.md is refused (seats stop writing lessons to memory);
  - MEMORY.md is refused when the write leaves it over CEILING bytes AND larger than it was (preferences-sized index).
The same gate holds on a Bash or PowerShell command that WRITES into that directory (a `>`/`>>` redirect, `tee`,
`sed -i`, `cp`/`mv` onto it, or Set-Content/Add-Content/Out-File/New-Item): any file other than MEMORY.md is refused,
and MEMORY.md is refused while it is already over CEILING (a shell write cannot show its resulting size). A read, or a
write elsewhere, passes. Closes the Bash-append path around the same Andrew-directed gate (1.0.0_SA_CTO~Z msg 34396).
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


LESSON_REFUSAL = ("BLOCKED: seats do not write lessons to memory (Andrew-direct 2026-09-24). A lesson that matters becomes "
                  "a gate, field or skill fix by its owning seat; an incident stays in git history. MEMORY.md holds his "
                  "stable preferences only.")
SHELL_MEMPATH_RE = re.compile(r"(?:[A-Za-z]:|/[a-z]|~|\$HOME|\$env:USERPROFILE)?[^\s\"'<>|;&]*?/\.claude/projects/"
                              r"[^/\s\"']+/memory/([^/\s\"'<>|;&)]+)", re.IGNORECASE)
SHELL_PATH_ANY_RE = re.compile(r"/\.claude/projects/[^/\s\"']+/memory/([^/\s\"'<>|;&)]+)", re.IGNORECASE)
PS_WRITE_RE = re.compile(r"\b(Set-Content|Add-Content|Out-File|New-Item)\b", re.IGNORECASE)
SEGMENT_SPLIT_RE = re.compile(r"[;\n]|&&|\|\||(?<![>|])\|(?!\|)")


def _local_path(p):
    m = re.match(r"^/([a-zA-Z])/(.*)$", p)
    if m:
        return "%s:/%s" % (m.group(1).upper(), m.group(2))
    if p.startswith("~"):
        return os.path.expanduser(p)
    return p


def _shell_verdict(cmd):
    norm = cmd.replace("\\", "/")
    if "/.claude/projects/" not in norm or "/memory/" not in norm:
        return None
    for seg in SEGMENT_SPLIT_RE.split(norm):
        if not seg:
            continue
        for m in SHELL_PATH_ANY_RE.finditer(seg):
            before = seg[:m.start()]
            # rewind to the start of the path token so `> "<path>"` and `>> /c/Users/.../memory/x` both read as write.
            # A quoted path may hold spaces ("Opal Bloomberg"), so an open quote marks the token start, not a space.
            dq, sq = before.count("\""), before.count("'")
            if dq % 2:
                lead = before[:before.rfind("\"")]
            elif sq % 2:
                lead = before[:before.rfind("'")]
            else:
                ws = max(before.rfind(" "), before.rfind("\t"))
                lead = before[:ws + 1] if ws >= 0 else ""
            rest = seg[m.end():].strip()
            is_write = bool(re.search(r"(>>?|\btee\b(\s+-a)?)\s*[\"']?\s*$", lead, re.IGNORECASE)
                            or re.search(r"\bsed\s+(-\S*\s+)*-i", seg, re.IGNORECASE)
                            or (re.match(r"\s*(cp|mv|install)\b", seg, re.IGNORECASE) and not rest.strip("\"' "))
                            or PS_WRITE_RE.search(seg))
            if not is_write:
                continue
            name = m.group(1)
            if name != "MEMORY.md":
                return LESSON_REFUSAL
            full = SHELL_MEMPATH_RE.search(seg)
            try:
                size = os.path.getsize(_local_path(full.group(0))) if full else -1
            except OSError:
                size = -1
            if size > CEILING:
                return ("BLOCKED: MEMORY.md is %d bytes (preferences-only ceiling %d); a shell write cannot show its "
                        "resulting size, so it is refused while the index is over the ceiling. A lesson goes to a gate, "
                        "field or skill fix instead." % (size, CEILING))
    return None


def verdict(payload):
    tool = payload.get("tool_name")
    ti = payload.get("tool_input") or {}
    if tool in ("Bash", "PowerShell"):
        return _shell_verdict(str(ti.get("command") or ""))
    path = str(ti.get("file_path") or "")
    m = MEMDIR_RE.search(path.replace("\\", "/"))
    if tool not in ("Write", "Edit") or not m:
        return None
    if m.group(1) != "MEMORY.md":
        return LESSON_REFUSAL
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
        memf = mem.replace("\\", "/")
        big = os.path.join(d, ".claude", "projects", "Q", "memory")
        os.makedirs(big)
        with open(os.path.join(big, "MEMORY.md"), "w", encoding="utf-8") as fh:
            fh.write("x" * 5000)
        bigf = big.replace("\\", "/")

        def sh(cmd, tool="Bash"):
            return {"tool_name": tool, "tool_input": {"command": cmd}}
        arms += [
            ("Bash: a cat >> append to a lesson file is refused",
             sh('cat >> "%s/feedback_x.md" <<\'EOF\'\na lesson\nEOF' % memf), True),
            ("Bash: an echo > overwrite of a lesson file is refused", sh("echo hi > %s/lesson.md" % memf), True),
            ("Bash: tee -a onto a lesson file is refused", sh("printf x | tee -a %s/l.md" % memf), True),
            ("Bash: sed -i on a lesson file is refused", sh("sed -i 's/a/b/' %s/l.md" % memf), True),
            ("Bash: cp onto the memory dir is refused", sh("cp /tmp/x.md %s/x.md" % memf), True),
            ("Bash: >> onto MEMORY.md over the ceiling is refused", sh("echo y >> %s/MEMORY.md" % bigf), True),
            ("PowerShell: Add-Content onto a lesson file is refused",
             sh("Add-Content -Path '%s\\n.md' -Value x" % mem.replace("/", "\\"), "PowerShell"), True),
            ("Bash: >> onto MEMORY.md under the ceiling passes", sh("echo y >> %s/MEMORY.md" % memf), False),
            ("Bash: reading a memory file passes", sh("cat %s/feedback_x.md | grep x" % memf), False),
            ("Bash: copying a memory file OUT passes", sh("cp %s/feedback_x.md /tmp/x.md" % memf), False),
            ("Bash: a read whose output is redirected elsewhere passes",
             sh("grep -l x %s/a.md > /tmp/out.txt" % memf), False),
            ("Bash: an unrelated append passes", sh("echo y >> /tmp/notes/feedback_x.md"), False),
            ("Bash: >> onto a QUOTED path with a space is refused",
             sh('cat >> "/c/Users/Opal Bloomberg/.claude/projects/P/memory/lesson.md" <<\'EOF\'\nx\nEOF'), True),
            ("Bash: a read of a QUOTED path with a space passes",
             sh('cat "/c/Users/Opal Bloomberg/.claude/projects/P/memory/lesson.md"'), False),
            ("PowerShell: Out-File onto a Windows path with a space is refused",
             sh("'x' | Out-File -Append 'C:\\Users\\Opal Bloomberg\\.claude\\projects\\P\\memory\\l.md'", "PowerShell"),
             True),
        ]
        for name, payload, want in arms:
            got = verdict(payload) is not None
            ok = ok and got == want
            print("  [%s] %s" % ("PASS" if got == want else "FAIL", name))
    print("SELF-TEST: %s" % ("ALL HOLD" if ok else "BROKEN"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(self_test() if "--self-test" in sys.argv else main())

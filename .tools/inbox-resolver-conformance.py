#!/usr/bin/env python3
"""inbox-resolver-conformance -- do all five inbox-path resolvers agree where a lane's mail lives?

FIVE RESOLVERS, ONE PATH. A `~lane` serial's mail lives at `inbox/<base>/~<suffix>/`. Five
independent pieces of the fabric compute that path, and on 2026-07-09 three of them disagreed:

    org/mcp/server.py:1133        WRITER      nested   OK
    org/mcp/inbox-watch.sh:98     MONITOR     nested   OK
    .tools/operator.py:539        DISPATCHER  FLAT     WRONG -- writes a lane's GO where nothing watches
    .tools/fabric-check.py:132    CHECKER     FLAT     WRONG -- fixed in 331eb1a4a
    .tools/halt-gate-check.sh:148 INTERLOCK   FLAT     WRONG -- a lane cannot be halted by [STOP]

The flat dir `inbox/<base>~<suffix>/` EXISTS (operator.py mkdir's it on demand) and receives
nothing from the broker. Reading it returns `0 unread` forever. That is not blindness -- it is a
decoy that answers "healthy," which is strictly worse, because a blind instrument at least cannot
be quoted.

The INTERLOCK case is the dangerous one. `safe-apply` calls the halt gate at the last reversible
moment before `terraform apply`. For a `~lane` serial it scans the decoy and the base dir, never
the canonical nested dir -- so a `[STOP]` addressed to that lane is invisible to the gate. The lane
is not merely unreachable; it is UNHALTABLE, and not as a race: unconditionally, even with no
watcher running at all.

METHOD DISCLOSURE (COO 233808Z: "say in the test that you parsed rather than executed -- a test
that quietly downgrades its own method is the next instance"). Each resolver is checked either by
EXECUTING it in a sandbox (behavioral: we observe which directory it actually reaches for) or by
PARSING its source expression (textual). Both are printed per row and counted in the summary.

    A PARSED row asserts what the source SAYS. It cannot detect a resolver whose runtime path
    diverges from its source expression. An EXECUTED row asserts what the resolver DOES.

Exit: 0 = all five conform. 1 = at least one nonconformant. 2 = the harness itself is broken
(a control failed), which is NOT the same as "all conform" and must never be read as one.

Usage:
    inbox-resolver-conformance.py             # check all five, print the table
    inbox-resolver-conformance.py --self-test # positive control on the CHECKER itself
"""
from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

EXECUTED = "EXECUTED"
PARSED = "PARSED"

# Pin the interpreter ABSOLUTELY. Bare "bash" in a Windows child process resolves via CreateProcess
# PATH order and can land on WSL's C:\Windows\System32\bash.exe, which cannot see /c/... paths and
# dies with `execvpe(/bin/bash) failed`. Git Bash is the runtime every fabric script targets
# (CLAUDE.md Rule 16). An exercise run under the wrong shell is not an exercise.
BASH = shutil.which("bash") or "bash"


def canonical(serial: str, inbox_root: str) -> str:
    """The one true answer. Mirrors server.py:1133 + inbox-watch.sh:98."""
    if "~" in serial:
        base, suffix = serial.split("~", 1)
        return os.path.join(inbox_root, base, "~" + suffix)
    return os.path.join(inbox_root, serial)


def _posix(p: str) -> str:
    r"""Windows path -> MSYS/Git-Bash path. `C:\a\b` -> `/c/a/b`.

    NOT cosmetic. A Windows-style path handed to bash makes `[ -f "$f" ]` fail, and
    `halt_gate_is_stop_class` opens with exactly that test -- so a real `[STOP]` gets silently
    downgraded to "routine" and the gate returns rc=1 instead of rc=2. The harness would then have
    reported the INTERLOCK nonconformant for the wrong reason: a true verdict from a broken
    instrument. (Same MSYS mangling that turned COO's `git show origin/CLOUD:<path>` into
    `origin\CLOUD;<path>` and made `grep -c` count 0 matches inside a `fatal:` message.)
    """
    p = p.replace("\\", "/")
    if len(p) > 1 and p[1] == ":":
        p = "/" + p[0].lower() + p[2:]
    return p


# ---------------------------------------------------------------------------
# PARSED resolvers -- textual assertion against the real source line.
# ---------------------------------------------------------------------------

def _source_line(relpath: str, pattern: str) -> tuple[int, str]:
    """(lineno, text) of the first line matching `pattern`. Raises if absent --
    an assertion over a line that no longer exists is a green over an empty set."""
    path = os.path.join(ROOT, relpath)
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        for i, line in enumerate(f, 1):
            if re.search(pattern, line):
                return i, line.rstrip("\n")
    raise LookupError(f"{relpath}: no line matches /{pattern}/ -- resolver moved or renamed")


def parse_server_py() -> tuple[bool, int, str]:
    """server.py WRITER: `INBOX_DIR / to_folder.name / f"~{to_suffix}"` -> NESTED."""
    ln, txt = _source_line("org/mcp/server.py", r'inbox\s*=\s*INBOX_DIR\s*/\s*to_folder\.name\s*/\s*f"~')
    return True, ln, txt.strip()


def parse_operator_py() -> tuple[bool, int, str]:
    """operator.py DISPATCHER: `inbox_root / agent` where agent carries the ~lane suffix -> FLAT."""
    ln, txt = _source_line(".tools/operator.py", r"inbox_dir\s*=\s*inbox_root\s*/\s*agent\b")
    # Conformant only if it splits the suffix. `inbox_root / agent` does not.
    return False, ln, txt.strip()


# ---------------------------------------------------------------------------
# EXECUTED resolvers -- behavioral. We watch which directory they reach for.
# ---------------------------------------------------------------------------

def exec_fabric_check(inbox_root: str, serial: str) -> str:
    """Import the real lane_inbox_dir() and call it."""
    sys.path.insert(0, os.path.join(ROOT, ".tools"))
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "fabric_check", os.path.join(ROOT, ".tools", "fabric-check.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.INBOX_DIR = inbox_root
    return mod.lane_inbox_dir(serial)


def exec_inbox_watch(tmp: str, serial: str) -> tuple[str | None, str]:
    """Run the REAL inbox-watch.sh in a sandbox and observe which dir it drains.

    Returns (watched_dir_or_None, note). We plant one message in the canonical nested dir and one
    in the flat decoy, run `stream` briefly, and see which filename it emits.
    """
    base = serial.split("~", 1)[0]
    mcp = os.path.join(tmp, "mcp")
    os.makedirs(os.path.join(tmp, "tier2_senior", base), exist_ok=True)
    shutil.copy(os.path.join(ROOT, "org", "mcp", "inbox-watch.sh"),
                os.path.join(mcp, "inbox-watch.sh"))
    nested = canonical(serial, os.path.join(mcp, "inbox"))
    flat = os.path.join(mcp, "inbox", serial)
    os.makedirs(nested, exist_ok=True)
    os.makedirs(flat, exist_ok=True)
    with open(os.path.join(nested, "NESTED.md"), "w") as f:
        f.write("x")
    with open(os.path.join(flat, "FLAT.md"), "w") as f:
        f.write("x")
    # No external `timeout`: on Windows, shutil.which() resolves TIMEOUT.EXE (a console-pause
    # utility), not GNU coreutils. Stream mode never exits, so terminate it ourselves.
    proc = subprocess.Popen([BASH, _posix(os.path.join(mcp, "inbox-watch.sh")), serial, "stream"],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    try:
        out, err = proc.communicate(timeout=8)
    except subprocess.TimeoutExpired:
        proc.kill()
        out, err = proc.communicate()
    if "NESTED.md" in out and "FLAT.md" not in out:
        return nested, "emitted NESTED.md, ignored FLAT.md (exercised)"
    if "FLAT.md" in out:
        return flat, "emitted FLAT.md -- watches the decoy"
    return None, f"CONTROL FAILED: emitted neither (stdout={out!r} stderr={err.strip()[:110]!r})"


def exec_halt_gate(tmp: str, serial: str) -> tuple[bool, str]:
    """Exercise the REAL halt gate. Returns (conformant, note).

    Decisive test: plant a [STOP] in the CANONICAL nested dir. If the gate returns 0 (PASS) it
    cannot see the STOP -> a lane is unhaltable.

    CONTROL (tests the universe, not the instrument): plant the same [STOP] in the BASE dir and
    confirm the gate returns 2 (stop-block). Without this, a `0` above could mean "the harness
    never wired up a STOP at all" -- indistinguishable from the defect.
    """
    base = serial.split("~", 1)[0]
    root = os.path.join(tmp, "hg")
    inbox = os.path.join(root, "org", "mcp", "inbox")
    os.makedirs(os.path.join(root, ".comp-graph"), exist_ok=True)
    with open(os.path.join(root, ".comp-graph", ".agent_context"), "w") as f:
        f.write(f"SERIAL={serial}\nTO_ID=\n")

    def stop_msg(d: str) -> None:
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "stop.md"), "w") as f:
            f.write(f"# Message from 1.0.0_SA_CTO\n**To:** {serial}\n"
                    f"**Date:** 20260709T235900Z\n**Subject:** [STOP] do not apply\n\nhalt\n")

    def run() -> int:
        env = dict(os.environ)
        # POSIX paths: bash must be able to `[ -f ]` these, or the STOP classifier silently
        # downgrades a real [STOP] to "routine" and the harness draws a true conclusion from a
        # broken instrument.
        env.update({"HALT_GATE_REPO_ROOT": _posix(root), "HALT_GATE_INBOX_ROOT": _posix(inbox),
                    "HALT_GATE_CONTEXT_FILE": _posix(os.path.join(root, ".comp-graph", ".agent_context"))})
        env.pop("CLAUDE_CODE_SESSION_ID", None)
        env.pop("HALT_ACK", None)
        gate = _posix(os.path.join(ROOT, ".tools", "halt-gate-check.sh"))
        return subprocess.run([BASH, gate, "conformance-test"], env=env,
                              capture_output=True, text=True).returncode

    # CONTROL first: a STOP the gate is KNOWN to look at must block (rc=2).
    stop_msg(os.path.join(inbox, base))
    ctl = run()
    shutil.rmtree(os.path.join(inbox, base), ignore_errors=True)
    if ctl != 2:
        return False, f"HARNESS BROKEN: control STOP in base dir returned rc={ctl}, expected 2"

    # DECISIVE: the same STOP, in the canonical nested dir the lane actually receives mail in.
    stop_msg(canonical(serial, inbox))
    rc = run()
    if rc == 2:
        return True, "blocked on a nested-dir [STOP] (rc=2) -- reads the canonical dir"
    return False, (f"PASSED a nested-dir [STOP] (rc={rc}, control proved rc=2 is reachable) "
                   f"-- the lane is UNHALTABLE")


# ---------------------------------------------------------------------------

def check_all() -> int:
    serial = "A_AGENT~B"
    tmp = tempfile.mkdtemp(prefix="resolver-conf-")
    os.makedirs(os.path.join(tmp, "mcp"), exist_ok=True)
    rows = []
    harness_broken = False
    try:
        inbox_root = os.path.join(tmp, "inbox")
        want = canonical(serial, inbox_root)

        got = exec_fabric_check(inbox_root, serial)
        rows.append(("fabric-check.py", "CHECKER", EXECUTED, got == want,
                     "lane_inbox_dir() -> nested" if got == want else f"-> {got}"))

        watched, note = exec_inbox_watch(tmp, serial)
        if watched is None and note.startswith("CONTROL FAILED"):
            harness_broken = True
        want_w = canonical(serial, os.path.join(tmp, "mcp", "inbox"))
        rows.append(("inbox-watch.sh", "MONITOR", EXECUTED, watched == want_w, note))

        ok, note = exec_halt_gate(tmp, serial)
        if note.startswith("HARNESS BROKEN"):
            harness_broken = True
        rows.append(("halt-gate-check.sh", "INTERLOCK", EXECUTED, ok, note))

        ok, ln, txt = parse_server_py()
        rows.append(("server.py", "WRITER", PARSED, ok, f":{ln}  {txt[:64]}"))

        ok, ln, txt = parse_operator_py()
        rows.append(("operator.py", "DISPATCHER", PARSED, ok, f":{ln}  {txt[:64]}"))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    print(f"INBOX-RESOLVER CONFORMANCE -- do all resolvers agree for lane `{serial}`?")
    print(f"  canonical = inbox/{serial.split('~')[0]}/~{serial.split('~')[1]}/   "
          f"(server.py:1133 + inbox-watch.sh:98)\n")
    print(f"  {'resolver':<24}{'role':<12}{'method':<10}{'verdict':<13}note")
    print("  " + "-" * 108)
    bad = 0
    for name, role, method, ok, note in rows:
        if not ok:
            bad += 1
        print(f"  {name:<24}{role:<12}{method:<10}{('OK' if ok else 'NONCONFORM'):<13}{note}")

    n_exec = sum(1 for r in rows if r[2] == EXECUTED)
    n_parse = sum(1 for r in rows if r[2] == PARSED)
    print(f"\n  RESOLVER-COVERAGE: nonconformant={bad} over {len(rows)} resolvers "
          f"({n_exec} EXECUTED, {n_parse} PARSED)")
    if n_parse:
        print(f"  METHOD CAVEAT: {n_parse} resolver(s) asserted TEXTUALLY against their source line. "
              f"A parse cannot detect a\n"
              f"                 resolver whose runtime path diverges from its source expression. "
              f"Not equivalent to an exercise.")
    if harness_broken:
        print("\n  HARNESS BROKEN -- a control failed. This is NOT 'all conform'. "
              "A checker that cannot see and a checker that finds nothing print the same 0.")
        return 2
    if bad:
        print(f"\n  ACTION: {bad} resolver(s) disagree with the writer. A lane's mail is written to a path "
              f"they do not read.\n"
              f"          Fix the RESOLVERS, not the directories -- deleting the flat dirs destroys the "
              f"evidence and\n          operator.py re-creates them on the next dispatch.")
        return 1
    print("\n  All resolvers agree.")
    return 0


def self_test() -> int:
    """Positive control on the CHECKER. A conformance checker that cannot detect a nonconformant
    resolver is a green over an empty set. Exercise BOTH directions."""
    passed = failed = 0

    def check(name, got, want):
        nonlocal passed, failed
        if got == want:
            passed += 1
            print(f"  ok   {name}")
        else:
            failed += 1
            print(f"  FAIL {name}: got {got!r}, want {want!r}")

    root = "/inbox"
    check("canonical(lane) -> nested", canonical("A~B", root), os.path.join(root, "A", "~B"))
    check("canonical(base) -> flat", canonical("A", root), os.path.join(root, "A"))

    # The two directions the checker must distinguish.
    nested = os.path.join(root, "A", "~B")
    flat = os.path.join(root, "A~B")
    check("a NESTED resolver is judged conformant", nested == canonical("A~B", root), True)
    check("a FLAT resolver is judged NONCONFORMANT", flat == canonical("A~B", root), False)

    # The source-line assertions must FAIL LOUD if the line vanishes, never silently pass.
    try:
        _source_line(".tools/operator.py", r"this_pattern_cannot_match_anything_xyzzy")
        check("missing source line raises", False, True)
    except LookupError:
        check("missing source line raises (not a silent pass)", True, True)

    # The real source lines must still be findable -- else every PARSED row is vacuous.
    try:
        _, ln, _ = parse_server_py()
        check("server.py writer line found", ln > 0, True)
    except LookupError as e:
        check(f"server.py writer line found ({e})", False, True)
    try:
        _, ln, _ = parse_operator_py()
        check("operator.py dispatcher line found", ln > 0, True)
    except LookupError as e:
        check(f"operator.py dispatcher line found ({e})", False, True)

    print(f"\nself-test: {passed} passed, {failed} failed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(self_test() if "--self-test" in sys.argv[1:] else check_all())

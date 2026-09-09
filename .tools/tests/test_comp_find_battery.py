"""Battery for .tools/comp-find -- NFRA_COMPEFFICACY unit 3b (3.0.0_SA_CVO 92758; lane TOOL_BATTERIES).

WHY THIS EXISTS: comp-find is the estate's primary search instrument (3,722 rail rows / 30d) and
had NO battery. Its contract is asserted here from a MEASURED run, not from its docstring:

    comp-find [content] '<pattern>'
      DENOMINATOR: N hit(s) across M file(s) scanned in scope [corpus=all] | ...
      BANDS (true totals, not this page): DEF=4      (or: none)
      PAGE i of j  (showing a of b)

IMPORT IS INERT (the T-16 lesson): every subprocess lives in _run_battery(), called once per
process by test_all_arms_pass (pytest) or _report (direct). `pytest --collect-only` runs no search.

THE TOOL UNDER TEST is chosen by path, never edited: COMP_FIND_TOOL overrides the binary so a
PRODUCTION MUTANT can be planted in a temp copy. TWO FIXTURE DEFECTS FOUND ON THE FIRST RUN AND
FIXED HERE, recorded because both are the "a fixture that cannot represent the failure cannot
score it" class:
  1. The ABSENT token was a string literal in THIS file, and this file lives inside the search
     scope -- so comp-find found it (1 hit across 357 files) and the false-zero arm could never
     pass. The token is now BUILT AT RUNTIME; no literal search can find it.
  2. A mutant copy in the system temp dir cannot `import _comprail` (a sibling module resolved
     relative to the tool's own directory), so it CRASHED -- and the mutant arm read the crash as
     PASS because "no denominator line" is true of a crash too. A DEAD ARM. The copy now lives
     BESIDE the real tool (sibling imports resolve) and the arm asserts the mutant RAN (rc 0, the
     tool's own header printed) AND lacks the denominator. A crash now reads FAIL, never PASS.

ARM F/G (NFRA_COMPEFFICACY CE-t-1, Rule T's FORM -- PRD v0.4 s.4.4, the shared .tools/_compbudget
carrier): before this cell, the `--corpus aws` pull hard-coded timeout=600 against a 120s outer
harness ceiling (5x over, nothing at expiry said so). It is now `--budget <s>` (> env
COMP_BUDGET_S > default 90s), spent per UNIT: an explicit node_type pathspec makes each named
type its own unit (real --cursor resumability); an unscoped pull is one indivisible "ALL" unit
(a live measurement showed enumerating node_types first, to decompose even the unscoped case,
itself costs far more than the budget it would serve -- so that is a disclosed non-application,
never a faked cursor). F drives the REAL ceiling on the PRODUCTION binary directly (no mutant
needed to force it -- the ceiling is a flag, not a constant, so exercising it touches no bytes)
and asserts BUDGET REACHED is printed and TEXTUALLY DISTINCT from both a clean "NO HITS" zero
(F2) and a scoped WITHIN BUDGET completion (F3, the other unit-shape). G is the red-first
control: a mutant with the BUDGET REACHED marker text neutered must still RUN (not crash) and
FAIL F's own predicate. ALL SKIP (recorded, not silently omitted) if this box has no local Kuzu
DB/CLI to exercise (a fixture that cannot represent the failure cannot score it -- stated, not
silent).

ARM G5 (NFRA_COMPEFFICACY TO-CE-G-5, REPOINTED by NFRA_CLDGRPH TO-CG-D-7 / R7). The original
arms guarded an ORPHANED GRANDCHILD: the --corpus aws pull shelled out to a local CLI, which itself
spawned a loader, so a killed budgeted client reached only its DIRECT child and the grandchild
survived holding the shared rebuild mutex (measured: PID 25896, parent dead, 743s past its own
ceiling -- row NFRA_COMPEFFICACY-S6). THAT WHOLE CLASS IS NOW REMOVED BY CONSTRUCTION: the aws
corpus is ONE in-process HTTPS call to the served graph. There is no child, so no grandchild, so
no orphan and no mutex a bounded client could enter. The arms therefore pin the STRONGER property
-- the tool's aws path spawns NOTHING -- read from the tool's own source, with a POSITIVE CONTROL
running the same detector over a source that DOES spawn, so a zero is a measured absence rather
than a matcher that cannot fire.

Run: python .tools/tests/test_comp_find_battery.py    |    pytest -q .tools/tests/test_comp_find_battery.py
"""
from __future__ import annotations

import os
import re
import subprocess
import sys
import tempfile
import time
from pathlib import Path

RESULTS: list[tuple[str, bool | None, str]] = []
_WS_CACHE = None
_RAN = False

SCOPE = ".tools"                      # small (~360 files), fast (~1 s), contains the tool itself
PRESENT = "def _self_report"          # defined in comp-find, comp-read, comp-adversary (DEF band)
AWS_PATTERN = "opal-gateway"          # a real, present AWS-corpus term (34 hits / 2100 nodes measured)
DENOM_RE = re.compile(r"DENOMINATOR: (\d+) hit\(s\) across (\d+) file\(s\) scanned")
PAGE_RE = re.compile(r"PAGE (\d+) of (\d+)\s+\(showing (\d+) of (\d+)\)")
HEADER_RE = re.compile(r"^comp-find \[(content|name)\]", re.M)
AWS_HEADER_RE = re.compile(r"^comp-find \[aws", re.M)


def _aws_exercisable() -> bool:
    """MOVE-2-style precondition, not an assumption. TO-CG-D-7 (R7) retired the local Kuzu DB, so
    what must exist for `--corpus aws` to be exercisable is no longer a CLI file plus a DB
    directory on this box: it is the SERVED graph answering. Probed with the service's own health
    route through the one thin client. An unreachable service SKIPs these arms (they measure the
    budget contract, not the estate's connectivity) -- it never renders as a pass."""
    try:
        sys.path.insert(0, str(_ws() / "infra" / "aws" / "globgrph"))
        import projection_client  # noqa: PLC0415

        return bool(projection_client.health().get("vintage"))
    except Exception:   # noqa: BLE001
        return False


def _absent_token() -> str:
    """Built at runtime from parts, so the token never exists as a literal anywhere in the corpus --
    including in this file, which is inside SCOPE. Fixture defect 1."""
    return "ZZZ" + "_NOSUCH_" + "%d" % os.getpid() + "_" + "0902"


def _ws() -> Path:
    global _WS_CACHE
    if _WS_CACHE is None:
        _WS_CACHE = Path(subprocess.run(["git", "rev-parse", "--show-toplevel"],
                                        cwd=str(Path(__file__).resolve().parent),
                                        capture_output=True, text=True).stdout.strip())
    return _WS_CACHE


def _tool() -> Path:
    """COMP_FIND_TOOL overrides the binary under test; unset = the real .tools/comp-find.
    The override MUST live inside .tools/ (comp-find imports its sibling _comprail by its own
    directory) -- a copy elsewhere crashes on import and proves nothing. Fixture defect 2."""
    return Path(os.environ.get("COMP_FIND_TOOL") or (_ws() / ".tools" / "comp-find"))


def rec(tid: str, ok: bool, detail: str = "") -> None:
    RESULTS.append((tid, bool(ok), detail))


def run(args: list[str], tool: Path | None = None, timeout: int = 120) -> tuple[int, str]:
    r = subprocess.run([sys.executable, str(tool or _tool())] + args,
                       capture_output=True, text=True, timeout=timeout, cwd=str(_ws()))
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def _denom(out: str):
    m = DENOM_RE.search(out)
    return (int(m.group(1)), int(m.group(2))) if m else None


def _run_battery() -> None:
    global _RAN
    if _RAN:
        return
    _RAN = True

    # A1 -- a KNOWN-PRESENT token is found and the DENOMINATOR is printed with both numbers.
    rc, out = run([PRESENT, SCOPE, "--limit", "5"])
    d = _denom(out)
    rec("A1-PRESENT-FOUND", rc == 0 and d is not None and d[0] >= 1 and d[1] > 0, "rc=%s denom=%s" % (rc, d))
    # A2 -- the hit lands in the DEF band and the BANDS line is printed.
    rec("A2-DEF-BAND", "BANDS (true totals, not this page):" in out and "DEF=" in out and "[DEF]" in out, out[:300])
    # A3 -- THE FALSE-ZERO DISCRIMINATOR: an ABSENT token reports 0 hits across N>0 files SCANNED.
    #       A bare grep hands you '0' with no denominator; this line is what the tool exists to print.
    rc, out = run([_absent_token(), SCOPE])
    d = _denom(out)
    rec("A3-ABSENT-IS-MEASURED-ZERO", rc == 0 and d is not None and d[0] == 0 and d[1] > 0, "rc=%s denom=%s" % (rc, d))
    # A4 -- --name mode finds a file by BASENAME (content mode structurally cannot return the file
    #       whose name you typed unless that file also mentions its own name -- 2026-09-01 finding).
    rc, out = run(["--name", "comp-find", SCOPE])
    rec("A4-NAME-MODE-BASENAME", rc == 0 and ".tools/comp-find" in out and "[HEAD]" in out, out[:300])
    # A5 -- the PAGE line is printed and 'showing a of b' is consistent (a <= b, i <= j).
    rc, out = run([PRESENT, SCOPE, "--limit", "2"])
    m = PAGE_RE.search(out)
    rec("A5-PAGE-CONTRACT", m is not None and int(m.group(3)) <= int(m.group(4)) and int(m.group(1)) <= int(m.group(2)), out[:300])

    # E -- MUTANT: a copy of the tool BESIDE the real one, with the DENOMINATOR print neutered, must
    #      RUN (rc 0, its own header printed -- a crash is a DEAD arm, not a pass) and FAIL A1's predicate.
    src = _tool().read_text(encoding="utf-8", errors="replace")
    needle = "DENOMINATOR:"
    mp = _ws() / ".tools" / (".mutant-comp-find-%d" % os.getpid())
    if src.count(needle) == 0:
        rec("E-MUTANT-NO-DENOMINATOR", False, "mutation anchor absent from the tool under test")
    else:
        try:
            mp.write_text(src.replace(needle, "DENOMINATOR-MUTATED:"), encoding="utf-8")
            rc, out = run([PRESENT, SCOPE, "--limit", "5"], tool=mp)
            ran = rc == 0 and HEADER_RE.search(out) is not None
            rec("E-MUTANT-NO-DENOMINATOR", ran and _denom(out) is None,
                ("mutant did not RUN (rc=%s, header=%s) -> DEAD arm, not a pass" % (rc, bool(HEADER_RE.search(out))))
                if not ran else ("mutant still printed a denominator -> arm A1 is DEAD" if _denom(out) else "mutant ran and fails A1: OK"))
        finally:
            try:
                mp.unlink()
            except OSError:
                pass

    # F/G -- RULE T's FORM (PRD v0.4 s.4.4, landed mid-CE-t-1 -- superseded the T-16 interim shape
    # this file's first version tested): the --corpus aws budget ceiling via the shared
    # .tools/_compbudget carrier (--budget / env COMP_BUDGET_S / default 90s), its two terminal
    # tokens (WITHIN BUDGET / BUDGET REACHED), and the per-node_type unit loop.
    if not _aws_exercisable():
        skip = ("SKIP: the served cloud graph did not answer here -- --corpus aws not "
                "exercisable (this is a CONNECTIVITY skip, never a pass)")
        for tid in ("F-UNSCOPED-BUDGET-REACHED", "F2-CLEAN-EMPTY-DISCRIMINATOR",
                    "F3-SCOPED-DISCRIMINATOR", "G-MUTANT-NO-BUDGET-REACHED"):
            rec(tid, None, skip)
        return

    # F -- driven past its ceiling on the REAL PRODUCTION BINARY (no mutant needed: the ceiling is
    # a caller-supplied flag, not a hard-coded constant, so exercising it touches no bytes and
    # production sha is trivially unchanged -- itself evidence Rule T is doing its job). Unscoped
    # (no node_type pathspec) -> the NO-CURSOR branch: one indivisible "ALL" unit.
    rc, out = run(["--corpus", "aws", AWS_PATTERN, "--budget", "0.001"])
    f_ok = (rc == 0 and "BUDGET REACHED:" in out and "NO CURSOR:" in out
            and "WITHIN BUDGET:" not in out and "NO HITS" not in out)
    rec("F-UNSCOPED-BUDGET-REACHED", f_ok, "rc=%s out_has_reached=%s" % (rc, "BUDGET REACHED:" in out))

    # SIDE-BY-SIDE CONTROL (T1-AC3): a clean empty must never be able to produce the BUDGET
    # REACHED line, and D1/D2 (the token, and n==N vs n<N) must be mutually exclusive and self-
    # consistent. LATENCY-TOLERANT BY DESIGN: this calls the LIVE aws-backed comp-kuzu pull, whose
    # wall-clock is real infra latency this battery does not control (measured live 2026-09-03:
    # the same query ran ~8s repeatedly for ~20 minutes, then degraded to 90s+ -- see the project's
    # surprise-channel row). A GENEROUS explicit --budget (150s, comfortably past every measured
    # sample) plus a matched wrapper timeout gives the tool room to speak either way; the arm
    # asserts the CONTRACT (exactly one valid, self-consistent outcome), never "must complete
    # fast" -- a battery coupled to live external latency is the "wrong arm, not a dead arm" class
    # if it hard-requires the happy path.
    rc0, out0 = run(["--corpus", "aws", "ZZZ_NOSUCH_AWS_TERM_%d" % os.getpid(), "--budget", "150"],
                    timeout=170)
    within0, reached0 = "WITHIN BUDGET:" in out0, "BUDGET REACHED:" in out0
    ok0 = (rc0 == 0 and within0 != reached0 and (
        (within0 and "WITHIN BUDGET: scanned 1 of 1" in out0 and "NO HITS. This is a MEASURED zero" in out0)
        or (reached0 and "0 hit(s) shown -- NOT a measured zero" in out0
            and "NO HITS. This is a MEASURED zero" not in out0)))
    rec("F2-CLEAN-EMPTY-DISCRIMINATOR", ok0,
        "rc=%s within=%s reached=%s (live-latency-observed=%s)" % (rc0, within0, reached0, reached0))

    # F3 -- SCOPED unit path: an explicit node_type pathspec makes the unit a real node_type, not
    # the unscoped "ALL" -- a distinct code path (genuine --cursor resumability lives here, not in
    # the unscoped branch). Same latency tolerance as F2.
    rc3, out3 = run(["--corpus", "aws", AWS_PATTERN, "LAMBDA", "--budget", "150"], timeout=170)
    within3, reached3 = "WITHIN BUDGET: scanned 1 of 1 node_type" in out3, "BUDGET REACHED:" in out3
    ok3 = rc3 == 0 and within3 != reached3 and (within3 or "NO CURSOR YET" in out3)
    rec("F3-SCOPED-DISCRIMINATOR", ok3,
        "rc=%s within=%s reached=%s (live-latency-observed=%s)" % (rc3, within3, reached3, reached3))

    # G -- MUTANT, red-first: neuter the BUDGET REACHED marker text in a copy beside the real
    # tool. Must RUN (rc 0, its own aws header printed -- a crash is a DEAD arm, not a pass) and
    # FAIL F's own predicate (the marker must be ABSENT).
    marker = "BUDGET REACHED:"
    src = _tool().read_text(encoding="utf-8", errors="replace")
    mp2 = _ws() / ".tools" / (".mutant-comp-find-ceiling-%d" % os.getpid())
    if src.count(marker) == 0:
        rec("G-MUTANT-NO-BUDGET-REACHED", False, "mutation anchor absent from the tool under test")
    else:
        try:
            mp2.write_text(src.replace(marker, "MUTATED-BUDGET:"), encoding="utf-8")
            rc, out = run(["--corpus", "aws", AWS_PATTERN, "--budget", "0.001"], tool=mp2)
            ran = rc == 0 and AWS_HEADER_RE.search(out) is not None
            rec("G-MUTANT-NO-BUDGET-REACHED", ran and marker not in out,
                ("mutant did not RUN (rc=%s, header=%s) -> DEAD arm, not a pass"
                 % (rc, bool(AWS_HEADER_RE.search(out)))) if not ran
                else ("mutant still printed the marker -> arm F is DEAD" if marker in out
                      else "mutant ran and lacks the marker: OK"))
        finally:
            try:
                mp2.unlink()
            except OSError:
                pass

    _g5_arms()


_G5_CHILD_SRC = (
    "import sys, os, time\n"
    "with open(sys.argv[1], 'w') as f:\n"
    "    f.write(str(os.getpid()))\n"
    "time.sleep(90)\n"
)

_G5_WRAPPER_SRC = (
    "import sys\n"
    "sys.path.insert(0, sys.argv[1])\n"
    "import importlib\n"
    "mod = importlib.import_module(sys.argv[2])\n"
    "cmd = [sys.executable, sys.argv[3], sys.argv[4]]\n"
    "try:\n"
    "    mod._run_child_supervised(cmd, timeout=90)\n"
    "except Exception:\n"
    "    pass\n"
)

_G5_MUTANT_UNSUPERVISED_SRC = (
    "import subprocess\n"
    "def _run_child_supervised(cmd, timeout):\n"
    "    return subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)\n"
)


def _globgrph_dir() -> Path:
    return _ws() / "infra" / "aws" / "globgrph"


def _pid_alive(pid: int) -> bool:
    """OS-level truth via tasklist on Windows -- MSYS ps cannot see detached Win32 processes
    reliably (a documented estate trap); os.kill(pid, 0) on POSIX."""
    if sys.platform == "win32":
        out = subprocess.run(["tasklist", "/FI", "PID eq %d" % pid, "/FO", "CSV"],
                             capture_output=True, text=True).stdout
        return str(pid) in out
    try:
        os.kill(pid, 0)
        return True
    except OSError:
        return False


def _g5_no_orphan_check(module_dir: str, module_name: str) -> tuple[bool, str]:
    """Runs a wrapper as a REAL subprocess that calls <module_name>._run_child_supervised to spawn
    a long-running grandchild, then kills the WRAPPER externally (proc.kill(), the identical act
    comp-find performs on kuzu_cli.py) well before the grandchild's own 90s sleep or the
    supervised call's 90s timeout would fire on their own. Returns (no_orphan, detail) where
    no_orphan=True means the grandchild pid was NOT alive after the wrapper died -- read from the
    OS process table, never this process's own bookkeeping."""
    with tempfile.TemporaryDirectory() as d:
        marker = os.path.join(d, "g5_marker.txt")
        wrapper = os.path.join(d, "g5_wrapper.py")
        child = os.path.join(d, "g5_child.py")
        Path(wrapper).write_text(_G5_WRAPPER_SRC, encoding="utf-8")
        Path(child).write_text(_G5_CHILD_SRC, encoding="utf-8")
        proc = subprocess.Popen([sys.executable, wrapper, module_dir, module_name, child, marker])
        try:
            t0 = time.time()
            while not os.path.exists(marker) and time.time() - t0 < 15:
                time.sleep(0.2)
            if not os.path.exists(marker):
                return False, "grandchild never started (marker never appeared) -- fixture failure, not a pass"
            time.sleep(0.5)   # let the pid write flush
            gc_pid = int(Path(marker).read_text().strip())
            proc.kill()       # TerminateProcess on the WRAPPER -- comp-find's own act on kuzu_cli.py
            proc.wait(timeout=10)
            time.sleep(1.0)   # let the OS finish tearing down handles (job-close is not instantaneous)
            alive = _pid_alive(gc_pid)
            return (not alive), "grandchild pid=%d alive-after-parent-kill=%s" % (gc_pid, alive)
        finally:
            try:
                proc.kill()
                proc.wait(timeout=5)
            except Exception:
                pass


def _g5_arms() -> None:
    """G5, REPOINTED by TO-CG-D-7 (R7). The original three arms guarded an ORPHANED GRANDCHILD:
    `comp-find --corpus aws` shelled out to kuzu_cli.py, which itself spawned
    kuzu_incremental_refresh.py, so a TerminateProcess on the direct child left the grandchild
    running (NFRA_COMPEFFICACY-S6), and `_canonical._run_child_supervised` was the fix.

    THE CLASS IS NOW REMOVED BY CONSTRUCTION, NOT BY SUPERVISION: the aws corpus is one in-process
    HTTPS call through projection_client. There is no child, so there is no grandchild to orphan,
    and no mutex a bounded client could enter. That is a STRONGER property than the supervised
    spawn -- and it is the one worth pinning, because a future re-introduction of a subprocess on
    this path would silently restore the whole class.

    The arm therefore reads the tool's OWN aws-corpus source and asserts it spawns nothing. It
    carries a POSITIVE CONTROL on the same predicate over a source that DOES spawn, so a zero here
    is a measured absence rather than a broken matcher."""
    import re as _re   # noqa: PLC0415

    src = _tool().read_text(encoding="utf-8", errors="replace")
    start = src.find("def _aws_corpus(")
    if start < 0:
        rec("G5-AWS-PATH-SPAWNS-NOTHING", False,
            "the _aws_corpus function is absent from the tool under test -- fixture failure")
        rec("G5-SPAWN-DETECTOR-POSITIVE-CONTROL", False, "not evaluated: no _aws_corpus to scan")
        return
    end = src.find("\ndef ", start + 1)
    body = src[start:end if end > 0 else len(src)]
    spawn_rx = _re.compile(r"subprocess\.(run|Popen|call|check_output)|os\.(spawn|system)")
    found = spawn_rx.findall(body)
    rec("G5-AWS-PATH-SPAWNS-NOTHING", not found,
        "spawn calls in _aws_corpus: %d (%s) over %d lines scanned"
        % (len(found), found, body.count(chr(10))))

    # POSITIVE CONTROL on the SAME predicate and the SAME verb: this battery's own supervisor
    # helper DOES spawn, so the detector must return non-zero on it. Without this, a matcher that
    # can never fire reads identically to a genuine absence.
    own = Path(__file__).read_text(encoding="utf-8", errors="replace")
    ctrl_start = own.find("def _g5_no_orphan_check(")
    ctrl_body = own[ctrl_start:own.find("\ndef ", ctrl_start + 1)] if ctrl_start >= 0 else ""
    ctrl = spawn_rx.findall(ctrl_body)
    rec("G5-SPAWN-DETECTOR-POSITIVE-CONTROL", bool(ctrl),
        "control found %d spawn call(s) %s in this file's own _g5_no_orphan_check"
        % (len(ctrl), ctrl))


def _report() -> int:
    """PRE-EXISTING GAP FIXED HERE: the RESULTS type was declared `bool | None` (None = SKIP,
    neither pass nor fail) since this file's first version, but this printer had no branch for
    it -- `"PASS" if ok else "FAIL"` renders a None row as FAIL even though the fails-count below
    correctly excludes it. Never fired before F/G (the first arms to use None); fixed on first use
    rather than left to misrender silently."""
    _run_battery()
    fails = [r for r in RESULTS if r[1] is False]
    for tid, ok, detail in RESULTS:
        label = "SKIP" if ok is None else ("PASS" if ok else "FAIL")
        print("  [%s] %s%s" % (label, tid, "" if ok or ok is None else "  -- " + detail[:160]))
    print("COMP-FIND BATTERY: %d/%d PASS (denominator %d)" % (len(RESULTS) - len(fails), len(RESULTS), len(RESULTS)))
    return 1 if fails else 0


def test_all_arms_pass():
    """pytest entry. Fails on any FAIL row; the denominator is len(RESULTS)."""
    _run_battery()
    fails = [(t, d) for t, ok, d in RESULTS if ok is False]
    assert not fails, "comp-find battery arms failed (%d of %d): %r" % (len(fails), len(RESULTS), fails)


if __name__ == "__main__":
    sys.exit(_report())

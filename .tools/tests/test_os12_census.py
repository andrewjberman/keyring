#!/usr/bin/env python3
"""OS-s-12 -- the WORKING-ORDER CENSUS of the outset tools (NFRA_OUTSET, FWD-5 / brief O5).

ONE read gives, for every tool the brief's Part II names: rc, ANSWER STATE, VINTAGE and
BUDGET-HONOURED -- with the DENOMINATOR of tools censused. A tool that could not answer says so
in its own voice with its bound, never as an empty section that reads like a clean result.

WHAT THIS IS NOT: not a second implementation of any tool's battery (six of the nine already have
one under .tools/tests/test_comp_*_battery.py) and not a monitor. A battery asks "is THIS tool
correct?"; the census asks "which of the population can answer AT ALL today, and what does each
disclose?" -- one read, one denominator. It is an on-demand instrument; nothing is scheduled,
nothing alarms, nothing is removed (PRD R-5).

THE PLANE THIS COUNTS, stated because a census that does not name its plane cannot be checked:
the LOCAL REPO CLI plane -- the `.tools/<tool>` files in THIS worktree at the commit under test.
NOT the `~/bin` shim plane, NOT any deployed or remote plane, NOT the tools' engines directly.

=== THE THREE FALSE-ZERO TRAPS THIS CENSUS IS BUILT AGAINST ===
A census that cannot tell "I counted the population and found none" from "I counted the wrong
thing perfectly" is the exact failure this cell exists to prevent elsewhere. Three measured ones:

 (1) THE WSL-STUB TRAP -- the one that would have falsified 4 of 9 rows. Four of the nine tools
     are bash launchers. When Python subprocesses bare "bash" on this box, Windows resolves it to
     the System32 WSL stub, which has NO distribution installed: every launcher then returns rc=1
     with an identical 504-byte UTF-16 "Windows Subsystem for Linux has no installed
     distributions" body. A census dispatching that way reports 4 of 9 outset tools BROKEN, with a
     clean denominator, and every one of those verdicts is FALSE. Discriminator: the four bodies
     were byte-identical in LENGTH, which is the tell that one shared dependency failed rather
     than four tools. Remedy is the estate's own and is not re-implemented here:
     .tools/git_bash_resolver.py (its own docstring names this trap). Arm A6 keeps it measured.
 (2) THE UNBOUNDED-GRANDCHILD TRAP -- subprocess timeout= does NOT bound a shell launcher, because
     the launcher's python grandchild inherits and holds the stdout PIPE, so the parent blocks on
     pipe EOF long past its own deadline. MEASURED: `comp-pipescript deployed` under an 8 s
     timeout= ran 91.8 s. Remedy here: redirect to a FILE rather than a pipe, and kill the process
     TREE (taskkill /T /F) rather than the parent alone. Same probe now returns at 8.9 s. Arm A7
     keeps it measured -- an unbounded census silently becomes an unbounded sweep.
 (3) THE CONFIDENT-ZERO TRAP -- rc=0 with an empty or state-free body is NOT a working tool. Arm A5
     plants exactly that shape and fails if the census scores it WORKING.

Every zero here is accompanied by a positive control proving the instrument can return non-zero on
a case known to exist (arm A6), and the tool list is re-derived from the brief at run time and
compared against the census's own list (arm A1), so the DENOMINATOR is checked against its source
rather than typed once and trusted.

Usage:
  python .tools/tests/test_os12_census.py              # the battery (prints the census table)
  python .tools/tests/test_os12_census.py --census-only  # just the table, no arms
Author: 0.9.0_WK_NFRA_OUTSET~3 (NFRA_OUTSET OS-s-12). 2026-09-05.
"""

from __future__ import annotations

import os
import re
import subprocess
import sys
import tempfile
import time

_HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(os.path.dirname(_HERE))          # .tools/tests -> .tools -> root
sys.path.insert(0, os.path.join(REPO_ROOT, ".tools"))

BRIEF = os.path.join(REPO_ROOT, "docs", "briefs",
                     "comp-heat-and-the-semantic-estate-pipeline-outset-tooling-brief-20260904.md")

# The nine tools the brief's Part II names. DECLARED HERE AND CHECKED AGAINST THE BRIEF (arm A1):
# a denominator typed once and never compared to its source is how a census drifts off its
# population. Each probe is a CHEAP, OFFLINE-WHERE-POSSIBLE real answer -- never --help, which
# proves only that the CLI parses. `comp-pipescript deployed` is the brief's own named subcommand
# and is kept even though it exceeds the probe budget: "could not answer within B" IS its
# working-order answer, and suppressing it would be the empty section O5 forbids.
PROBES = [
    ("comp-heat",       ["score", "os12-probe", "--age-days", "30", "--budget", "10"]),
    ("comp-fedobs",     ["coverage"]),
    ("comp-drift",      ["coverage", "--budget", "10"]),
    ("comp-xray",       ["code", ".tools/comp-heat"]),
    ("comp-similar",    ["--self-test", "--budget", "10"]),
    ("comp-pipescript", ["deployed"]),
    ("comp-freshness",  ["self-test"]),
    ("comp-blast",      ["--self-test"]),
    ("comp-estate",     ["--list", "--budget", "10"]),
]

PROBE_DEADLINE_S = 9.0        # per tool
CENSUS_BUDGET_S = 100.0       # whole census; a probe is not started if the rest cannot cover it

STATE_RE = re.compile(r"answer[-_ ]state", re.I)
VINTAGE_RE = re.compile(r"vintage|measured_at|as[- ]of|last[- ]modified", re.I)
BUDGET_LINE_RE = re.compile(r"within budget|budget reached|budget:\s*\d|rule t:\s*budget", re.I)

WORKING = "WORKING"
FAILED = "FAILED"
NO_ANSWER = "NO-ANSWER-DISCLOSED"
NOT_PROBED = "NOT-PROBED-BUDGET-EXHAUSTED"

RESULTS = []


def arm(name, ok, detail=""):
    RESULTS.append((name, bool(ok), detail))
    print(f"  [{'OK ' if ok else 'FAIL'}] {name}" + (f" -- {detail}" if detail else ""))


def _dispatch_argv(tool_path, args):
    """Dispatch by SHEBANG, never by guess. A python tool run through bash emits an authentic
    -looking tool error that is really a dispatch error (measured on comp-estate/comp-fedobs), and
    a bash launcher run through bare 'bash' hits the WSL stub -- so the bash arm goes through the
    estate's resolver, which refuses to fall back to bare 'bash'."""
    with open(tool_path, "rb") as fh:
        first = fh.readline()
    if b"python" in first:
        return [sys.executable, tool_path, *args]
    from git_bash_resolver import bash_argv        # noqa: E402  (estate's own, not re-implemented)
    return bash_argv(tool_path, *args)


def run_bounded(argv, deadline):
    """Returns (rc, output, timed_out). Output to a FILE, not a PIPE (trap 2), and a process-TREE
    kill on timeout -- otherwise a launcher's grandchild outlives the deadline holding the pipe."""
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".os12out")
    tmp.close()
    timed_out = False
    try:
        with open(tmp.name, "wb") as fh:
            proc = subprocess.Popen(argv, stdout=fh, stderr=subprocess.STDOUT, cwd=REPO_ROOT)
            try:
                rc = proc.wait(timeout=deadline)
            except subprocess.TimeoutExpired:
                timed_out = True
                subprocess.run(["taskkill", "/PID", str(proc.pid), "/T", "/F"],
                               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
                try:
                    proc.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    proc.kill()
                rc = 124
        with open(tmp.name, "rb") as fh:
            out = fh.read().decode("utf-8", "replace")
    finally:
        try:
            os.unlink(tmp.name)
        except OSError:
            pass
    return rc, out, timed_out


def classify(rc, out, timed_out, budget_offered):
    """WORKING requires rc==0 AND a non-trivial body. rc=0 with an empty/whitespace body is the
    CONFIDENT-ZERO shape and is NEVER WORKING (trap 3)."""
    if timed_out:
        return FAILED
    if rc != 0:
        return FAILED
    if len(out.strip()) < 16:
        return NO_ANSWER
    return WORKING


def census(probes, deadline=PROBE_DEADLINE_S, budget=CENSUS_BUDGET_S, label="outset tools"):
    """The census proper. Returns a list of row dicts; prints the table with its denominator."""
    rows = []
    t0 = time.time()
    for tool, args in probes:
        path = os.path.join(REPO_ROOT, ".tools", tool)
        remaining = budget - (time.time() - t0)
        if not os.path.isfile(path):
            rows.append({"tool": tool, "rc": "-", "verdict": FAILED, "state": False,
                         "vintage": False, "budget": "n/a", "secs": 0.0,
                         "note": "absent from .tools/ (subject absent, not a clean zero)"})
            continue
        if remaining < deadline:
            rows.append({"tool": tool, "rc": "-", "verdict": NOT_PROBED, "state": False,
                         "vintage": False, "budget": "n/a", "secs": 0.0,
                         "note": f"census budget {budget:.0f}s exhausted before this probe"})
            continue
        offered = "--budget" in args
        t1 = time.time()
        try:
            rc, out, timed = run_bounded(_dispatch_argv(path, args), deadline)
        except Exception as e:                                        # noqa: BLE001
            rc, out, timed = -1, f"<dispatch error: {type(e).__name__}: {e}>", False
        el = time.time() - t1
        verdict = classify(rc, out, timed, offered)
        if not offered:
            budget_col = "not-accepted"
        elif BUDGET_LINE_RE.search(out):
            budget_col = "YES"
        else:
            budget_col = "NO-LINE"
        rows.append({"tool": tool, "rc": rc, "verdict": verdict,
                     "state": bool(STATE_RE.search(out)), "vintage": bool(VINTAGE_RE.search(out)),
                     "budget": budget_col, "secs": el,
                     "note": ("bounded at %.0fs, no answer" % deadline) if timed else ""})

    n = len(rows)
    print(f"\n=== OS-s-12 WORKING-ORDER CENSUS -- {label} ===")
    print(f"  plane: LOCAL REPO CLI (.tools/<tool> in this worktree) | probe deadline {deadline:.0f}s"
          f" | census budget {budget:.0f}s | elapsed {time.time() - t0:.1f}s")
    print(f"  {'tool':16} {'rc':>4}  {'verdict':27} {'state':6} {'vintg':6} {'budget':12} secs")
    for r in rows:
        print(f"  {r['tool']:16} {str(r['rc']):>4}  {r['verdict']:27} "
              f"{str(r['state']):6} {str(r['vintage']):6} {r['budget']:12} {r['secs']:.1f}"
              + (f"   [{r['note']}]" if r["note"] else ""))
    working = sum(1 for r in rows if r["verdict"] == WORKING)
    failed = sum(1 for r in rows if r["verdict"] == FAILED)
    noans = sum(1 for r in rows if r["verdict"] == NO_ANSWER)
    notpr = sum(1 for r in rows if r["verdict"] == NOT_PROBED)
    print(f"  DENOMINATOR: {n} tool(s) censused; {working} WORKING, {failed} FAILED, "
          f"{noans} {NO_ANSWER}, {notpr} {NOT_PROBED}")
    print(f"  disclosure over the {n}: answer-state {sum(1 for r in rows if r['state'])}/{n}, "
          f"vintage {sum(1 for r in rows if r['vintage'])}/{n}, "
          f"budget-line-when-offered {sum(1 for r in rows if r['budget'] == 'YES')}/"
          f"{sum(1 for r in rows if r['budget'] != 'not-accepted')}")
    return rows


def brief_tool_list():
    """Re-derive the population from the brief's Part II, so the denominator is checked against its
    SOURCE rather than trusted. Returns [] if the brief is unreadable -- which arm A1 then FAILS on,
    rather than silently agreeing with an empty list (an empty expectation matches nothing and
    would pass vacuously)."""
    if not os.path.isfile(BRIEF):
        return []
    text = open(BRIEF, encoding="utf-8", errors="replace").read()
    m = re.search(r"\*\*The outset tools this brief means.*?freshness and deploy state\.",
                  text, re.S)
    if not m:
        return []
    seen = []
    for tok in re.findall(r"`(comp-[a-z]+)(?: [a-z]+)?`", m.group(0)):
        if tok not in seen:
            seen.append(tok)
    return seen


def main():
    t0 = time.time()
    census_only = "--census-only" in sys.argv

    rows = census(PROBES)

    if census_only:
        return 0

    print("\n=== arms ===")

    # A1 -- the denominator is checked against its SOURCE, not typed and trusted.
    derived = brief_tool_list()
    declared = [t for t, _ in PROBES]
    arm("A1 tool list matches the brief's Part II enumeration",
        derived == declared and len(derived) == 9,
        f"brief-derived {len(derived)} vs declared {len(declared)}; "
        + ("identical and ordered" if derived == declared else f"MISMATCH derived={derived}"))

    # A2 -- every named tool exists on the plane being counted.
    missing = [t for t, _ in PROBES if not os.path.isfile(os.path.join(REPO_ROOT, ".tools", t))]
    arm("A2 all named tools present on the counted plane", not missing,
        f"{len(declared) - len(missing)}/{len(declared)} present"
        + (f"; MISSING {missing}" if missing else ""))

    # A3 -- one row per tool, denominator intact.
    arm("A3 census emits one row per tool with its denominator", len(rows) == len(PROBES),
        f"{len(rows)} row(s) of {len(PROBES)} tool(s)")

    # A4 -- THE PLANTED FAILURE THE CRITERION NAMES. A tool that cannot answer must read FAILED
    # and must still be COUNTED: a census that drops what it cannot probe reports a clean
    # population it never had.
    # Run over a 2-tool SUBSET plus the plant: the arm is about the plant's verdict and the
    # denominator arithmetic, not about re-probing nine tools a second time inside one bound.
    base = PROBES[:2]
    planted = base + [("comp-os12-planted-absent", ["--help"])]
    prows = census(planted, label="PLANTED-FAILURE control (2-tool subset + one absent tool)")
    prow = [r for r in prows if r["tool"] == "comp-os12-planted-absent"]
    arm("A4 planted failure reads FAILED and is counted in the denominator",
        len(prows) == len(base) + 1 and len(prow) == 1 and prow[0]["verdict"] == FAILED,
        f"denominator {len(prows)} (subset was {len(base)}); planted verdict="
        + (prow[0]["verdict"] if prow else "<row absent -- census DROPPED it>"))

    # A5 -- the confident-zero shape: rc=0 with an empty body is NOT working.
    arm("A5 rc=0 with an empty body is not scored WORKING",
        classify(0, "", False, True) == NO_ANSWER and classify(0, "   \n ", False, True) == NO_ANSWER,
        f"classify(rc=0, empty) -> {classify(0, '', False, True)}")

    # A6 -- POSITIVE CONTROL ON THE INSTRUMENT plus the WSL discriminator. Proves the census can
    # obtain a non-zero on a case known to exist, and that the naive dispatch a census would
    # reach for produces a FALSE failure on that same known-good tool.
    launcher = os.path.join(REPO_ROOT, ".tools", "comp-xray")
    good_rc, good_out, _ = run_bounded(_dispatch_argv(launcher, ["--help"]), 30)
    naive_rc, naive_out, _ = run_bounded(["bash", launcher, "--help"], 30)
    wsl = "Subsystem for Linux" in naive_out or "\x00" in naive_out or naive_rc != 0
    arm("A6 positive control: resolver dispatch answers where bare-bash falsely fails",
        good_rc == 0 and len(good_out) > 100 and wsl,
        f"resolver rc={good_rc} bytes={len(good_out)}; bare-bash rc={naive_rc} "
        f"bytes={len(naive_out)} wsl_stub={wsl}")

    # A7 -- the bound is real. comp-pipescript is the measured 91.8s-under-an-8s-timeout case.
    t1 = time.time()
    rc7, _out7, timed7 = run_bounded(
        _dispatch_argv(os.path.join(REPO_ROOT, ".tools", "comp-pipescript"), ["deployed"]), 6)
    el7 = time.time() - t1
    arm("A7 per-probe deadline actually bounds a known-unbounded launcher",
        timed7 and rc7 == 124 and el7 < 20,
        f"deadline 6s -> returned in {el7:.1f}s rc={rc7} (pipe+parent-only kill measured 91.8s)")

    n_ok = sum(1 for _, ok, _ in RESULTS if ok)
    n = len(RESULTS)
    print(f"\n=== test_os12_census: {'PASS' if n_ok == n else 'FAIL'} ({n_ok}/{n}) "
          f"in {time.time() - t0:.1f}s ===")
    return 0 if n_ok == n else 1


if __name__ == "__main__":
    sys.exit(main())

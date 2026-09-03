"""pytest wrapper for `.tools/missions-tree-index.py --self-test` -- the tool's own 18-arm battery,
invoked BY PATH, its printed contract pinned by four arms of this file.

2.0.0_SA_COO 92788 row 2 (TREE_PREREQ_COMPLETION_MANIFEST_20260902 residual row 3). Lane
TOOL_BATTERIES (.tools/tests/**). The tool is 2.0.0_SA_COO's (@cb6e93e7f8); this file changes
none of its refusal semantics -- if an arm here ever needs one, that is a COO edit, not a test edit.

THE CONTRACT THIS FILE PINS, measured 2026-09-02 22:50Z from one run by path (rc 0, 373 ms, 19 lines):
    <two spaces>PASS<two spaces><arm name>          one line per arm, 18 of them
    missions-tree-index --self-test: 18/18 PASS     the last line: numerator/denominator + verdict
The self-test builds every fixture inside tempfile.TemporaryDirectory() (:367) -- its write surface
is OFF the estate, so running it under every sweep touches nothing shared.

ARMS (each asserts a line the tool PRINTS):
    W1 RAN            rc 0 AND the verdict line present -- the tool was executed by path and reached
                      its own summary (a crash, a missing file, a stale import cannot satisfy this)
    W2 DENOMINATOR    numerator == denominator == EXPECTED_ARMS. The arm count is part of the contract:
                      a tool change that adds or removes an arm updates EXPECTED_ARMS in the same commit.
    W3 BODY-AGREES    the PASS lines in the body number exactly the numerator, and no FAIL line exists --
                      the summary and the body it summarises agree (terminal-honest / artifact-lies probe)
    E  MUTANT-RED     a COPY of the tool beside it, with the INDEX-MISSING assertion inverted, must RUN
                      (its own verdict line present) and be RED (rc != 0 or numerator < denominator).
                      Proves W1-W3 discriminate the TOOL and not the wrapper. The copy lives beside the
                      real tool so sibling imports resolve; a copy in the system temp dir crashes and a
                      crash is not a red (the 3b lesson, 1e6206a267). Removed after the run.

IMPORT IS INERT: every subprocess sits in _run_battery(), called once per process by
test_all_arms_pass() (pytest) or _report() (direct). collect-only must stay under 5 s.
MISSIONS_TREE_INDEX_TOOL selects the binary under test so a grader can aim the wrapper at a mutant
of their own without touching this file or the tool.

Direct: python .tools/tests/test_missions_tree_index_selftest.py   -> k/4 PASS (denominator 4), rc 0/1
pytest: python -m pytest -q .tools/tests/test_missions_tree_index_selftest.py
"""
import os
import re
import subprocess
import sys
from pathlib import Path

EXPECTED_ARMS = 18
VERDICT_RE = re.compile(r"^missions-tree-index --self-test: (\d+)/(\d+) (PASS|FAIL)\s*$", re.M)
ARM_RE = re.compile(r"^\s+(PASS|FAIL)\b", re.M)
MUTANT_ANCHOR = 'ids(viol) == ["INDEX-MISSING"]'
MUTANT_FLIP = 'ids(viol) != ["INDEX-MISSING"]'

_WS_CACHE = None
_RAN = None


def _ws():
    global _WS_CACHE
    if _WS_CACHE is None:
        r = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True,
                           cwd=str(Path(__file__).resolve().parent))
        _WS_CACHE = Path(r.stdout.strip() or Path(__file__).resolve().parents[2])
    return _WS_CACHE


def _tool():
    env = os.environ.get("MISSIONS_TREE_INDEX_TOOL")
    return Path(env) if env else _ws() / ".tools" / "missions-tree-index.py"


def _run(tool):
    r = subprocess.run([sys.executable, str(tool), "--self-test"], capture_output=True, text=True,
                       timeout=120, cwd=str(_ws()))
    out = (r.stdout or "") + (r.stderr or "")
    m = VERDICT_RE.search(out)
    num, den = (int(m.group(1)), int(m.group(2))) if m else (None, None)
    passes = sum(1 for x in ARM_RE.finditer(out) if x.group(1) == "PASS")
    fails = sum(1 for x in ARM_RE.finditer(out) if x.group(1) == "FAIL")
    return {"rc": r.returncode, "out": out, "verdict": bool(m), "num": num, "den": den,
            "pass_lines": passes, "fail_lines": fails}


def _run_battery():
    """One process, one run of the real tool, one run of a planted mutant. Cached."""
    global _RAN
    if _RAN is not None:
        return _RAN
    results = []

    def arm(name, ok, detail):
        results.append((name, bool(ok), detail))

    tool = _tool()
    real = _run(tool)
    arm("W1 RAN: rc 0 and verdict line present",
        real["rc"] == 0 and real["verdict"],
        "rc=%s verdict=%s" % (real["rc"], real["verdict"]))
    arm("W2 DENOMINATOR: %d/%d" % (EXPECTED_ARMS, EXPECTED_ARMS),
        real["num"] == EXPECTED_ARMS and real["den"] == EXPECTED_ARMS,
        "printed %s/%s" % (real["num"], real["den"]))
    arm("W3 BODY-AGREES: PASS lines == numerator, FAIL lines == 0",
        real["num"] is not None and real["pass_lines"] == real["num"] and real["fail_lines"] == 0,
        "pass_lines=%d fail_lines=%d num=%s" % (real["pass_lines"], real["fail_lines"], real["num"]))

    # E: a production mutant, planted in a COPY beside the tool, must run and go red.
    src = tool.read_text(encoding="utf-8")
    if src.count(MUTANT_ANCHOR) != 1:
        arm("E MUTANT-RED", False,
            "mutation anchor found %d time(s), expected 1 -- cannot plant; the tool changed or is "
            "already mutated" % src.count(MUTANT_ANCHOR))
    else:
        mpath = tool.parent / (".mutant-missions-tree-index-%d.py" % os.getpid())
        try:
            mpath.write_text(src.replace(MUTANT_ANCHOR, MUTANT_FLIP), encoding="utf-8")
            mut = _run(mpath)
            ran = mut["verdict"]
            red = mut["rc"] != 0 or (mut["num"] is not None and mut["num"] < mut["den"])
            arm("E MUTANT-RED: planted copy RAN and is RED", ran and red,
                "ran=%s rc=%s printed %s/%s" % (ran, mut["rc"], mut["num"], mut["den"]))
        finally:
            try:
                mpath.unlink()
            except OSError:
                pass
    _RAN = results
    return results


def _report():
    results = _run_battery()
    ok = sum(1 for _, p, _ in results if p)
    for name, p, detail in results:
        print("  %s  %s  (%s)" % ("PASS" if p else "FAIL", name, detail))
    print("MISSIONS-TREE-INDEX WRAPPER: %d/%d PASS (denominator %d)" % (ok, len(results), len(results)))
    return ok == len(results)


def test_all_arms_pass():
    results = _run_battery()
    failed = [(n, d) for n, p, d in results if not p]
    assert not failed, "arms failed (%d of %d): %s" % (len(failed), len(results), failed)
    print("MISSIONS-TREE-INDEX WRAPPER: %d/%d PASS (denominator %d)" % (len(results), len(results), len(results)))


if __name__ == "__main__":
    sys.exit(0 if _report() else 1)

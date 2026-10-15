#!/usr/bin/env python3
"""Round-20 hygiene cell CT-aj-4 (NFRA_CTLPLN W110-S1), --map: the risk reflex classes staged portal .tsx paths.

Run: python .tools/tests/test_round20_hygiene.py --map
     (LAST line: HYGIENE-MAP tsx_classed=<n> py_classed=<m> ok=<True|False>)
     or, when the tracked danger map is past comp-pulse's staleness limit (a precondition not met):
     (LAST line: HYGIENE-MAP SKIP map STALE age=<h>h, exit 0)

Run: python .tools/tests/test_round20_hygiene.py --stale
     Proves the SKIP arm: comp-pulse runs on a COPY of the tracked map whose mtime is set 100 h back, and the
     arm passes (exit 0, LAST line HYGIENE-MAP SKIP map STALE age=<h>h) only when comp-pulse reports the copy STALE.
     The copy lives in a temporary tree; the tracked map is never touched.

Builds a temporary repository, stages paths in it, and runs the REAL org/modules/graph/comp_pulse.py diff with that
repository as the caller's working directory (the script is run at its own path). The danger map is the tracked
org/modules/graph/nerves-risk-edges.json, read by comp_pulse at its own location. A path is CLASSED when comp-pulse
prints a hit line "  [HOLD|RISK] <path>" for it. Nothing is written into the real tree.

Required: one staged portal .tsx that the tracked map holds, and one staged .py that the tracked map holds, are both
classed. Control (printed, not required): a staged portal .tsx with NO map entry is reported as it is measured.
A stale map is a precondition not met (comp-pulse prints "danger map: <h>h old !! STALE"), not a defect of the
map edit: the arm prints the SKIP line and exits 0 without grading the classes.
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOOLS = HERE.parent
ROOT = TOOLS.parent
SCRIPT = ROOT / "org" / "modules" / "graph" / "comp_pulse.py"
MAPPED_TSX = "portal/src/components/BenchmarkHeatmap.tsx"   # tracked map: RISK
MAPPED_PY = ".tools/deploy_ledger.py"                        # tracked map: HOLD
UNMAPPED_TSX = "portal/src/x.tsx"                            # no tracked map entry: control only
HIT = re.compile(r"^  \[(HOLD|RISK)\] (.+)$")
STALE = re.compile(r"^  danger map: ([0-9.]+)h old\s+!! STALE", re.M)
STALE_COPY_AGE_H = 100   # past comp-pulse STALE_AFTER_HOURS (36)


def run(argv, cwd=None):
    r = subprocess.run(argv, cwd=cwd, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=180)
    return r.returncode, r.stdout + r.stderr


def git(repo, *args):
    rc, out = run(["git", "-c", "user.name=t", "-c", "user.email=t@t", "-C", str(repo), *args])
    if rc != 0:
        raise RuntimeError("git %s failed rc=%s: %s" % (" ".join(args), rc, out))
    return out


def diff_staged(repo, script):
    return run([sys.executable, str(script), "diff"], cwd=str(repo))


def classed(out):
    return [(m.group(1), m.group(2)) for m in (HIT.match(ln) for ln in out.splitlines()) if m]


def stale_tree(work):
    """--stale arm: a copy of comp_pulse.py and of the tracked map, the copy's mtime STALE_COPY_AGE_H hours back.
    comp_pulse reads the map at its own location, so the copy is laid out as a tree of its own."""
    ws = work / "ws"
    graph = ws / "org" / "modules" / "graph"
    graph.mkdir(parents=True)
    (ws / ".tools").mkdir()
    shutil.copy2(str(SCRIPT), str(graph / "comp_pulse.py"))
    shutil.copy2(str(TOOLS / "_compbudget.py"), str(ws / ".tools" / "_compbudget.py"))
    copy = graph / "nerves-risk-edges.json"
    shutil.copy2(str(SCRIPT.parent / "nerves-risk-edges.json"), str(copy))
    past = time.time() - STALE_COPY_AGE_H * 3600
    os.utime(str(copy), (past, past))
    return graph / "comp_pulse.py"


def main():
    args = sys.argv[1:]
    stale_arm = "--stale" in args
    if "--map" not in args and not stale_arm:
        print("usage: python .tools/tests/test_round20_hygiene.py --map | --stale")
        return 2
    if not SCRIPT.is_file():
        print("ERROR: missing %s" % SCRIPT)
        return 2
    tmp = Path(tempfile.mkdtemp(prefix="hygiene_map_"))
    try:
        script = stale_tree(tmp) if stale_arm else SCRIPT
        repo = tmp / "repo"
        run(["git", "init", "-q", "-b", "CLOUD", str(repo)])
        for rel in (MAPPED_TSX, MAPPED_PY, UNMAPPED_TSX):
            (repo / rel).parent.mkdir(parents=True, exist_ok=True)
            (repo / rel).write_text("// fixture\n", encoding="utf-8")

        git(repo, "add", "--", MAPPED_TSX, MAPPED_PY)
        rc, out = diff_staged(repo, script)
        stale = STALE.search(out)
        if stale:
            print("HYGIENE-MAP SKIP map STALE age=%sh" % stale.group(1))
            return 0
        if stale_arm:
            print("HYGIENE-MAP FAIL --stale: comp-pulse did not report the aged copy STALE")
            return 1
        print("STAGED %s, %s -> comp-pulse diff rc=%s" % (MAPPED_TSX, MAPPED_PY, rc))
        for ln in out.splitlines():
            if ln.startswith("  DENOMINATOR") or ln.startswith("  ANSWER STATE") or HIT.match(ln):
                print(ln)
        hits = classed(out)
        tsx_n = sum(1 for sev, p in hits if p == MAPPED_TSX)
        py_n = sum(1 for sev, p in hits if p == MAPPED_PY)

        git(repo, "reset", "-q")
        git(repo, "add", "--", UNMAPPED_TSX)
        rc_c, out_c = diff_staged(repo, script)
        print("CONTROL (not required) STAGED %s -> comp-pulse diff rc=%s" % (UNMAPPED_TSX, rc_c))
        for ln in out_c.splitlines():
            if ln.startswith("  DENOMINATOR") or ln.startswith("  ANSWER STATE") or HIT.match(ln):
                print(ln)

        ok = rc == 1 and tsx_n == 1 and py_n == 1
        print("HYGIENE-MAP tsx_classed=%d py_classed=%d ok=%s" % (tsx_n, py_n, ok))
        return 0 if ok else 1
    finally:
        shutil.rmtree(str(tmp), ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())

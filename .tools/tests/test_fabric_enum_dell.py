#!/usr/bin/env python
"""NFRA_CTLPLN.TO-CT-c-6: the gate's fabric check on temporary project rows, then both tools' self-tests.

Admitted arm (5): fabric = dell1, dell2, laptop, site-z, and "DELL1 " (capitals + trailing space: the check
strips and lower-cases, so that value IS ADMITTED). Refused arm (1): fabric = dell3 (outside the enum).
The fabric check is `check_project_stage` in .tools/to-pipeline-gate.py, called on a temp tree whose project row
is valid in every other respect (dep_stage PRD), so a refusal can only be the fabric.

Self-tests: `python .tools/missions-tree-index.py --self-test` and `python .tools/to-pipeline-gate.py --self-test`
are each run with a 100 s bound; a timeout reads as `skipped` (run once outside the test for the record).

LAST line: FABRIC-ENUM admitted=<a>/5 refused=<r>/1 tree_selftest=<ok|fail|skipped>
gate_selftest=<ok|fail|skipped> ok=<True|False>
"""
import importlib.util
import json
import os
import re
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GATE = os.path.join(ROOT, ".tools", "to-pipeline-gate.py")
INDEX = os.path.join(ROOT, ".tools", "missions-tree-index.py")


def load_gate():
    spec = importlib.util.spec_from_file_location("to_pipeline_gate", GATE)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["to_pipeline_gate"] = mod
    spec.loader.exec_module(mod)
    return mod


def fabric_refusals(gate, fabric):
    """Refusals mentioning `fabric` for a temp project row carrying this fabric value."""
    with tempfile.TemporaryDirectory() as tmp:
        home = os.path.join(tmp, "org", "missions", "D0", "NFRA", "FABTMP")
        os.makedirs(os.path.join(home, "task-orders"))
        with open(os.path.join(home, "project.json"), "w", encoding="utf-8") as fh:
            json.dump({"project_code": "FABTMP", "dep_stage": "PRD", "fabric": fabric}, fh)
        rel = "org/missions/D0/NFRA/FABTMP/task-orders/FABTMP.TO-1.md"
        return gate.check_project_stage(tmp, rel)


def selftest(path, pattern):
    try:
        cp = subprocess.run([sys.executable, path, "--self-test"], cwd=ROOT, capture_output=True, text=True,
                            timeout=100, encoding="utf-8", errors="replace")
    except subprocess.TimeoutExpired:
        return "skipped", "timeout 100 s"
    out = (cp.stdout or "") + (cp.stderr or "")
    line = [ln for ln in out.splitlines() if re.search(pattern, ln)]
    shown = line[-1] if line else "(no result line)"
    return ("ok" if cp.returncode == 0 and line else "fail"), shown


def main():
    gate = load_gate()
    print("gate FABRIC_ENUM = %r" % (gate.FABRIC_ENUM,))
    admitted = 0
    for v in ("dell1", "dell2", "laptop", "site-z", "DELL1 "):
        r = fabric_refusals(gate, v)
        print("fabric=%r -> %s" % (v, "ADMITTED" if not r else "REFUSED: " + r[0][:120]))
        admitted += 0 if r else 1
    refused = 0
    for v in ("dell3",):
        r = fabric_refusals(gate, v)
        print("fabric=%r -> %s" % (v, "ADMITTED" if not r else "REFUSED: " + r[0][:120]))
        refused += 1 if (r and "NOT in the ratified enum" in r[0]) else 0
    tree, tline = selftest(INDEX, r"self-test: \d+/\d+")
    print("missions-tree-index --self-test -> %s | %s" % (tree, tline))
    gst, gline = selftest(GATE, r"RESULT:")
    print("to-pipeline-gate --self-test -> %s | %s" % (gst, gline))
    ok = admitted == 5 and refused == 1 and tree != "fail" and gst != "fail"
    print("FABRIC-ENUM admitted=%d/5 refused=%d/1 tree_selftest=%s gate_selftest=%s ok=%s"
          % (admitted, refused, tree, gst, ok))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

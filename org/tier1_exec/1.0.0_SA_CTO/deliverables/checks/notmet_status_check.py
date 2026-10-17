#!/usr/bin/env python3
"""notmet_status_check.py -- the terminal NOT_MET task-order status (row AMGT_RESAPP-D1-S55; 1.0.0_SA_CTO ruling
org/tier1_exec/1.0.0_SA_CTO/deliverables/RULINGS_PARKED_BUS_ITEMS_20261017_1350Z.md item 2).

An order whose <status> leads with `not_met` ended with at least one criterion failed. It is TERMINAL (it is not open
anywhere) and NOT CLEAN (no reader shows it as complete or done). round-close-check names it on its own NOT-MET line and
leaves it out of the proof count, so its FAIL proof row is never read as proof_bad.

Arms (no network; temporary trees for round-close-check, pure calls for the rest):
  (a) round-close-check: a `not_met` order with a FAIL proof row reads 0 complete, 0 open, NOT-MET 1, proof_bad=0;
  (b) NEGATIVE CONTROL: the same order and proof with `complete` reads proof_bad=1 and verdict=REFUSED (the row's case);
  (c) to-check classifies `not_met -- AC5 failed` as NOT_MET, labels it NOT MET, and keeps it out of the open set;
  (d) prd-check classifies it as NOT_MET;
  (e) to-decomp-ref-lint reads a `not_met` order as not open; a `pending` one as open;
  (f) seat-list counts `not_met` as terminal;
  (g) to-pipeline-gate GATE (xi) refuses a NEW tree order born `not_met`.
LAST line: NOTMET-STATUS arms=<k>/<n> ok=<True|False>
"""
from __future__ import annotations

import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
# The workspace root is DERIVED (git rev-parse), never a fixed depth: this check lives in the CTO deliverables folder
# because .tools/tests/** is lane TOOL_BATTERIES, which this seat gates and does not author.
ROOT = subprocess.run(["git", "-C", HERE, "rev-parse", "--show-toplevel"], check=True, capture_output=True,
                      text=True).stdout.strip()
TOOLS = os.path.join(ROOT, ".tools")
PROJ = "org/missions/D0/TEST/TEST_PROJ"
NOW = 2000000000
CVO = "3.0.0_SA_CVO"
DOER = "2.0.0_SA_COO~C"


def order(status: str) -> str:
    return ("# TO\n<to_id>TEST_PROJ.TO-1</to_id>\n<issued_to>0.9.0_WK_TEST_PROJ~1</issued_to>\n"
            "<issued_by>2.0.0_SA_COO~C</issued_by>\n<status>%s</status>\n<round>1</round>\n"
            '<criterion id="AC1" cell_refs="X"/>\n'
            '<criterion id="AC5" cell_refs="X"/>\n' % status)


PROOF = {"to_id": "TEST_PROJ.TO-1", "acceptance": [
    {"criterion_id": "AC1", "status": "PASS"},
    {"criterion_id": "AC5", "status": "FAIL"}]}


def load(name: str, path: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


RCC = load("opal_rcc_notmet", os.path.join(TOOLS, "round-close-check.py"))
SL = load("opal_sl_notmet", os.path.join(TOOLS, "seat-list.py"))
TOC = load("opal_toc_notmet", os.path.join(TOOLS, "to-check.py"))
PRD = load("opal_prd_notmet", os.path.join(TOOLS, "prd-check.py"))
LINT = load("opal_lint_notmet", os.path.join(TOOLS, "to-decomp-ref-lint.py"))
GATE = load("opal_gate_notmet", os.path.join(TOOLS, "to-pipeline-gate.py"))
KIND_OF = RCC.make_kind_of(ROOT)

results: list = []


def arm(label: str, ok: bool, detail: str) -> None:
    results.append(ok)
    print("%s  %s -- %s" % ("PASS" if ok else "FAIL", label, detail))


def run(status: str):
    tmp = tempfile.mkdtemp(prefix="nmst_")

    def put(rel: str, text: str) -> None:
        p = os.path.join(tmp, rel.replace("/", os.sep))
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)

    put(PROJ + "/project.json", '{"project_code": "TEST_PROJ", "macro_code": "TEST"}')
    put(PROJ + "/task-orders/TEST_PROJ.TO-1.one.md", order(status))
    put(PROJ + "/deliverables/0.9.0_WK_TEST_PROJ~1/TEST_PROJ.TO-1.one.proof_of_spec.json", json.dumps(PROOF))
    put("now", str(NOW))
    put("org/mcp/liveness.json", json.dumps({DOER: {"last_seen_epoch": NOW - 5}, CVO: {"last_seen_epoch": NOW - 5}}))
    try:
        return RCC.check(tmp, SL, SL.Ctx(tmp), "TEST_PROJ", None, None, "testbox", "testbox", KIND_OF)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main() -> int:
    lines, last = run("not_met -- AC5 failed")
    body = "\n".join(lines)
    ok = ("0 complete, 0 not complete" in body and "NOT-MET orders" in body and "1 (TO-1)" in body
          and "proof_bad=0" in body)
    arm("(a) a not_met order is terminal, named, and outside the proof count", ok, last)

    lines_c, last_c = run("complete")
    ok = "proof_bad=1" in "\n".join(lines_c) and last_c.endswith("verdict=REFUSED")
    arm("(b) control: the same order flipped complete reads proof_bad=1 and REFUSED", ok, last_c)

    sc = TOC._classify_status("not_met -- AC5 failed")
    ok = sc == "NOT_MET" and TOC.STATUS_LABELS.get(sc) == "NOT MET" and sc in TOC.TERMINAL_CLASSES
    arm("(c) to-check: class NOT_MET, label NOT MET, terminal", ok, "%s / %s" % (sc, TOC.STATUS_LABELS.get(sc)))

    sc = PRD._classify_status("not_met -- AC5 failed")
    arm("(d) prd-check: class NOT_MET", sc == "NOT_MET" and sc in PRD.TERMINAL_CLASSES, sc)

    nm_open = LINT._is_open(order("not_met -- AC5 failed"))
    pend_open = LINT._is_open(order("pending"))
    arm("(e) to-decomp-ref-lint: not_met is not open, pending is open", (not nm_open) and pend_open,
        "not_met open=%s pending open=%s" % (nm_open, pend_open))

    arm("(f) seat-list: not_met is terminal", "not_met" in SL.TERMINAL, str(sorted(SL.TERMINAL)))

    v = GATE._status_element_violations(PROJ + "/task-orders/TEST_PROJ.TO-1.one.md", order("not_met"))
    arm("(g) to-pipeline-gate GATE (xi): born not_met is refused", bool(v) and "born terminal" in v[0], v[0] if v else "[]")

    n_ok = sum(1 for r in results if r)
    print("NOTMET-STATUS arms=%d/%d ok=%s" % (n_ok, len(results), n_ok == len(results)))
    return 0 if n_ok == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())

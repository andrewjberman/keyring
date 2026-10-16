#!/usr/bin/env python3
"""test_round30_not_met.py -- NFRA_CTLPLN round 30, cell CT-cb-1 (CTO round-29 ruling 5; the CVO's ruling C-S103 stands:
a NOT MET grade does not refuse a round close, it feeds the round analysis).

round-close-check.py prints not_met=<k> beside graded=<g> on its ROUND-CLOSE last line. k counts the GRADED judgment criteria
whose grade of record reads NOT MET. It changes no verdict. The field order is
    ... judgment=<j> graded=<g> not_met=<k> ungraded=<u> self_graded=<s> verdict=<v>

Arms (a)-(f) plant temporary project trees and run the checker's check() end to end (no network, no real adjudication file,
ASCII output):
  (a) one judgment criterion MET and one NOT MET, by adjudication rows: graded=2 not_met=1, and the verdict equals the verdict
      of the same tree with both MET (the NOT MET grade changes no verdict);
  (b) no NOT MET grade (both MET): not_met=0;
  (c) an ungraded criterion counts in neither graded nor not_met: one NOT MET and one with no row reads graded=1 not_met=1
      ungraded=1; one MET and one with no row reads graded=1 not_met=0 ungraded=1;
  (d) the grade of record decides: an older NOT MET superseded by a newer MET by surfaced_at reads not_met=0;
  (e) the field order of the ROUND-CLOSE line is ... graded=<g> not_met=<k> ungraded=<u> ... on a tree with a NOT MET grade;
  (f) the reviewer-only line (no project) carries graded=0 not_met=0 ungraded=0.
LAST line: NOT-MET-COUNT arms=<k>/<n> ok=<True|False>
"""
from __future__ import annotations

import importlib.util
import json
import os
import re
import shutil
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
TOOLS = os.path.dirname(HERE)
ROOT = os.path.dirname(TOOLS)
CHECKER = os.path.join(TOOLS, "round-close-check.py")
PROJ = "org/missions/D0/TEST/TEST_PROJ"
NOW = 2000000000
CVO = "3.0.0_SA_CVO"
DOER = "2.0.0_SA_COO~C"
ORDER = ("# TO\n<to_id>TEST_PROJ.TO-1</to_id>\n<issued_to>0.9.0_WK_TEST_PROJ~1</issued_to>\n"
         "<issued_by>2.0.0_SA_COO~C</issued_by>\n<status>complete</status>\n<round>1</round>\n"
         '<criterion id="AC3" cell_refs="X" judgment="true"/>\n'
         '<criterion id="AC4" cell_refs="X" judgment="true"/>\n')
PROOF = {"to_id": "TEST_PROJ.TO-1", "acceptance": [
    {"criterion_id": "AC3", "status": "UNVERIFIABLE-BY-INSTRUMENT", "judgment": True},
    {"criterion_id": "AC4", "status": "UNVERIFIABLE-BY-INSTRUMENT", "judgment": True}]}
ADJ = "adjudications/ADJUDICATION_v1.md"
AT_EARLY = "2026-10-16T10:00Z"
AT_LATE = "2026-10-16T12:00Z"
LINE = re.compile(r"ROUND-CLOSE project=TEST_PROJ device=testbox reviewer=\S+ orders=(\d+) judgment=(\d+) graded=(\d+) "
                  r"not_met=(\d+) ungraded=(\d+) self_graded=(\d+) verdict=(MAY-CLOSE|REFUSED)$")


def load(name: str, path: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


RCC = load("opal_rcc_not_met_r30", CHECKER)
SL = load("opal_sl_not_met_r30", os.path.join(TOOLS, "seat-list.py"))
KIND_OF = RCC.make_kind_of(ROOT)


def grade(rid: str, criterion: str, verdict: str, at: str = AT_LATE) -> dict:
    """An adjudication row by the CVO-kind non-doer that grades one criterion of TEST_PROJ.TO-1 with a verdict word."""
    return {"id": rid, "surfaced_by": CVO, "surfaced_at": at,
            "one_line": "TEST_PROJ.TO-1 %s: %s on this read." % (criterion, verdict)}


def block(rows: list) -> str:
    return "# rows\n\n```json\n%s\n```\n" % json.dumps(rows, indent=1)


def plant(rows: list) -> str:
    """A temporary project tree: one project, one complete order (judgment criteria AC3 and AC4), its proof, the given
    adjudication rows, and a liveness file that names a live CVO-kind seat and the issuer."""
    tmp = tempfile.mkdtemp(prefix="nm30_")

    def put(rel: str, text: str) -> None:
        p = os.path.join(tmp, rel.replace("/", os.sep))
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)

    put(PROJ + "/project.json", '{"project_code": "TEST_PROJ", "macro_code": "TEST"}')
    put(PROJ + "/task-orders/TEST_PROJ.TO-1.one.md", ORDER)
    put(PROJ + "/deliverables/0.9.0_WK_TEST_PROJ~1/TEST_PROJ.TO-1.one.proof_of_spec.json", json.dumps(PROOF))
    put("now", str(NOW))
    put("org/mcp/liveness.json", json.dumps({
        DOER: {"last_seen_epoch": NOW - 5}, CVO: {"last_seen_epoch": NOW - 5}}))
    if rows:
        put(PROJ + "/surprise-channel/" + ADJ, block(rows))
    return tmp


def run(rows: list):
    """(lines, last line) of the checker over a planted tree with the given adjudication rows."""
    tmp = plant(rows)
    try:
        return RCC.check(tmp, SL, SL.Ctx(tmp), "TEST_PROJ", None, None, "testbox", "testbox", KIND_OF)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def fields(last: str):
    m = LINE.match(last)
    if not m:
        return None
    orders, judgment, graded, not_met, ungraded, self_graded, verdict = m.groups()
    return {"judgment": int(judgment), "graded": int(graded), "not_met": int(not_met), "ungraded": int(ungraded),
            "self_graded": int(self_graded), "verdict": verdict}


MET_BOTH = [grade("TEST_PROJ-C-S1", "AC3", "MET"), grade("TEST_PROJ-C-S2", "AC4", "MET")]
ONE_NOT_MET = [grade("TEST_PROJ-C-S1", "AC3", "MET"), grade("TEST_PROJ-C-S2", "AC4", "NOT MET")]
AC3_NOT_MET_ONLY = [grade("TEST_PROJ-C-S1", "AC3", "NOT MET")]
AC3_MET_ONLY = [grade("TEST_PROJ-C-S1", "AC3", "MET")]
SUPERSEDED = [grade("TEST_PROJ-C-S1", "AC3", "MET"),
              grade("TEST_PROJ-C-S2", "AC4", "NOT MET", at=AT_EARLY),
              grade("TEST_PROJ-C-S3", "AC4", "MET", at=AT_LATE)]

RESULTS = []


def arm(label: str, ok: bool, detail: str) -> None:
    RESULTS.append(ok)
    print("%s  %s -- %s" % ("PASS" if ok else "FAIL", label, detail))


def arm_a():
    _l, nm_last = run(ONE_NOT_MET)
    _l, met_last = run(MET_BOTH)
    nm, met = fields(nm_last), fields(met_last)
    ok = (nm is not None and met is not None and nm["graded"] == 2 and nm["not_met"] == 1 and nm["ungraded"] == 0
          and met["not_met"] == 0 and nm["verdict"] == met["verdict"]
          and nm["self_graded"] == met["self_graded"] and nm["judgment"] == met["judgment"])
    arm("(a) a NOT MET grade is counted and changes no verdict (graded=2 not_met=1; verdict equals the both-MET tree)", ok,
        "NOT MET tree: %s | both-MET tree: %s" % (nm_last, met_last))


def arm_b():
    _l, last = run(MET_BOTH)
    f = fields(last)
    ok = f is not None and f["graded"] == 2 and f["not_met"] == 0
    arm("(b) no NOT MET grade reads not_met=0", ok, last)


def arm_c():
    _l, one_nm = run(AC3_NOT_MET_ONLY)
    _l, one_met = run(AC3_MET_ONLY)
    a, b = fields(one_nm), fields(one_met)
    ok = (a is not None and b is not None and a["graded"] == 1 and a["not_met"] == 1 and a["ungraded"] == 1
          and b["graded"] == 1 and b["not_met"] == 0 and b["ungraded"] == 1)
    arm("(c) an ungraded criterion counts in neither graded nor not_met", ok,
        "NOT MET + ungraded: %s | MET + ungraded: %s" % (one_nm, one_met))


def arm_d():
    _l, last = run(SUPERSEDED)
    f = fields(last)
    ok = f is not None and f["graded"] == 2 and f["not_met"] == 0
    arm("(d) the grade of record decides: an older NOT MET superseded by a newer MET reads not_met=0", ok, last)


def arm_e():
    _l, last = run(ONE_NOT_MET)
    ok = bool(re.search(r" graded=2 not_met=1 ungraded=0 self_graded=0 verdict=(MAY-CLOSE|REFUSED)$", last)) \
        and last.count("not_met=") == 1 and " judgment=2 graded=2 not_met=1 " in last
    arm("(e) the field order is ... graded=<g> not_met=<k> ungraded=<u> ...", ok, last)


def arm_f():
    # the reviewer-only line needs no project: the real checker, reviewer-only, over a planted liveness file and no project
    tmp = tempfile.mkdtemp(prefix="nm30_ro_")
    try:
        os.makedirs(os.path.join(tmp, "org", "mcp"), exist_ok=True)
        with open(os.path.join(tmp, "org", "mcp", "liveness.json"), "w", encoding="utf-8", newline="\n") as fh:
            fh.write(json.dumps({DOER: {"last_seen_epoch": NOW - 5}, CVO: {"last_seen_epoch": NOW - 5}}))
        with open(os.path.join(tmp, "now"), "w", encoding="utf-8", newline="\n") as fh:
            fh.write(str(NOW))
        _l, last = RCC.check(tmp, SL, SL.Ctx(tmp), None, None, None, "testbox", "testbox", KIND_OF, reviewer_only=True)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    ok = last.startswith("ROUND-CLOSE project=- ") and " graded=0 not_met=0 ungraded=0 self_graded=0 " in last
    arm("(f) the reviewer-only line carries graded=0 not_met=0 ungraded=0", ok, last)


def main() -> int:
    for fn in (arm_a, arm_b, arm_c, arm_d, arm_e, arm_f):
        try:
            fn()
        except Exception as exc:  # noqa: BLE001 - an arm that raises is a failed arm, named
            RESULTS.append(False)
            print("FAIL  %s raised %s: %s" % (fn.__name__, type(exc).__name__, exc))
    good = sum(1 for ok in RESULTS if ok)
    print("NOT-MET-COUNT arms=%d/%d ok=%s" % (good, len(RESULTS), bool(RESULTS) and good == len(RESULTS)))
    return 0 if RESULTS and good == len(RESULTS) else 1


if __name__ == "__main__":
    sys.exit(main())

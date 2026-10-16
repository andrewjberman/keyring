#!/usr/bin/env python3
"""test_round29_grade_of_record.py -- NFRA_CTLPLN round 29, cell CT-be-1 (cross-box call XB-20261016T121809Z-95c2).

round-close-check.py must read a judgment criterion's GRADE OF RECORD -- the CVO-kind, non-doer row with the latest
surfaced_at that grades it -- and not the first row that happens to grade it. A self-grade never becomes the record,
and a row without a parseable surfaced_at sorts before every dated row.

Arms (a)-(g) plant a temporary project tree and run the checker's check() end to end, reading the JUDGMENT line it
prints. Arm (h) runs the checker on the real NFRA_CTLPLN round 29 and reports its last line. Temporary trees only; no
network; ASCII output. LAST line: GRADE-OF-RECORD arms=<k>/<n> ok=<True|False>
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
TOOLS = os.path.dirname(HERE)
ROOT = os.path.dirname(TOOLS)
PROJ = "org/missions/D0/TEST/TEST_PROJ"
NOW = 2000000000
CVO = "3.0.0_SA_CVO"
DOER = "2.0.0_SA_COO~C"
ORDER = ("# TO\n<to_id>TEST_PROJ.TO-1</to_id>\n<issued_to>0.9.0_WK_TEST_PROJ~1</issued_to>\n"
         "<issued_by>2.0.0_SA_COO~C</issued_by>\n<status>complete</status>\n<round>1</round>\n"
         '<criterion id="AC3" cell_refs="X" judgment="true"/>\n')
PROOF = {"to_id": "TEST_PROJ.TO-1", "acceptance": [
    {"criterion_id": "AC3", "status": "UNVERIFIABLE-BY-INSTRUMENT", "judgment": True}]}


def load(name: str, path: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


RCC = load("opal_rcc_grade_of_record", os.path.join(TOOLS, "round-close-check.py"))
SL = load("opal_sl_grade_of_record", os.path.join(TOOLS, "seat-list.py"))


def row(rid: str, by: str, at=None, text: str = "", **extra) -> dict:
    doc = {"id": rid, "surfaced_by": by, "one_line": text}
    if at is not None:
        doc["surfaced_at"] = at
    doc.update(extra)
    return doc


def block(rows: list) -> str:
    return "# rows\n\n```json\n%s\n```\n" % json.dumps(rows, indent=1)


def plant(files: dict) -> str:
    """A temporary project tree: one project, one complete order (TO-1, judgment criterion AC3), the given
    surprise-channel files, and a liveness file that names a live CVO-kind seat."""
    tmp = tempfile.mkdtemp(prefix="gor29_")

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
    for rel, text in files.items():
        put(PROJ + "/surprise-channel/" + rel, text)
    return tmp


def run_check(tmp: str):
    """(JUDGMENT lines, last line) of the checker over the planted tree."""
    sl = SL
    kind_of = RCC.make_kind_of(ROOT)
    lines, last = RCC.check(tmp, sl, sl.Ctx(tmp), "TEST_PROJ", None, None, "testbox", "testbox", kind_of)
    return [ln for ln in lines if ln.startswith("  JUDGMENT ")], last


def is_grade(judg: list, row_id: str, verdict: str) -> bool:
    """True when the one JUDGMENT line reads GRADED by the named row, with the named verdict."""
    if len(judg) != 1:
        return False
    line = judg[0]
    return (" -> GRADED (" in line and ("row %s by " % row_id) in line and ("(verdict %s)" % verdict) in line)


def arm(label: str, files: dict, row_id: str, verdict: str):
    tmp = plant(files)
    try:
        judg, last = run_check(tmp)
        ok = is_grade(judg, row_id, verdict)
        print("%s  %s -> %s" % ("PASS" if ok else "FAIL", label, judg[0].strip() if len(judg) == 1 else judg))
        return ok
    except Exception as exc:  # noqa: BLE001 - an arm that raises is a failed arm, named
        print("FAIL  %s -> raised %s: %s" % (label, type(exc).__name__, exc))
        return False
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def arm_no_cvo_row() -> bool:
    """(f) no CVO-kind row names the criterion: UNGRADED, and the verdict is REFUSED."""
    tmp = plant({"adjudications/ADJUDICATION_v1.md": block([
        row("TEST_PROJ-C-S1", "1.0.0_SA_CTO", "2026-10-16T12:00Z", "TEST_PROJ.TO-1 AC3: MET on a CTO read.")])})
    try:
        judg, last = run_check(tmp)
        ok = len(judg) == 1 and "-> UNGRADED (" in judg[0] and "verdict=REFUSED" in last
        print("%s  (f) no CVO-kind row -> %s" % ("PASS" if ok else "FAIL", judg[0].strip() if len(judg) == 1 else judg))
        return ok
    except Exception as exc:  # noqa: BLE001
        print("FAIL  (f) no CVO-kind row -> raised %s: %s" % (type(exc).__name__, exc))
        return False
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def arm_real_round29() -> bool:
    """(h) the checker on the real NFRA_CTLPLN round 29: exit 0 and a ROUND-CLOSE last line for the project."""
    cmd = [sys.executable, os.path.join(TOOLS, "round-close-check.py"), "--project", "NFRA_CTLPLN", "--round", "29"]
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=250)
    out = r.stdout.strip().splitlines()
    last = out[-1] if out else ""
    ok = (r.returncode == 0 and last.startswith("ROUND-CLOSE project=NFRA_CTLPLN ")
          and ("verdict=MAY-CLOSE" in last or "verdict=REFUSED" in last))
    print("%s  (h) real NFRA_CTLPLN round 29 rc=%d -> %s" % ("PASS" if ok else "FAIL", r.returncode, last))
    return ok


def main() -> int:
    results = []
    # (a) an older NOT MET CVO row, then a newer MET CVO row: MET.
    results.append(arm("(a) older NOT MET then newer MET -> MET", {
        "adjudications/ADJUDICATION_v1.md": block([row("TEST_PROJ-C-S1", CVO, "2026-10-14T10:00Z",
                                                       "TEST_PROJ.TO-1 AC3: NOT MET on the first read.")]),
        "adjudications/ADJUDICATION_v2.md": block([row("TEST_PROJ-C-S2", CVO, "2026-10-16T12:00Z",
                                                       "TEST_PROJ.TO-1 AC3: MET on the regrade.")]),
    }, "TEST_PROJ-C-S2", "MET"))
    # (b) the reverse: an older MET, then a newer NOT MET: NOT MET.
    results.append(arm("(b) older MET then newer NOT MET -> NOT MET", {
        "adjudications/ADJUDICATION_v1.md": block([row("TEST_PROJ-C-S1", CVO, "2026-10-14T10:00Z",
                                                       "TEST_PROJ.TO-1 AC3: MET on the first read.")]),
        "adjudications/ADJUDICATION_v2.md": block([row("TEST_PROJ-C-S2", CVO, "2026-10-16T12:00Z",
                                                       "TEST_PROJ.TO-1 AC3: NOT MET on the regrade.")]),
    }, "TEST_PROJ-C-S2", "NOT MET"))
    # (c) three rows in one file, the newest in the middle: the newest wins whatever the file order.
    results.append(arm("(c) three rows, newest in the middle -> newest wins", {
        "adjudications/ADJUDICATION_v1.md": block([
            row("TEST_PROJ-C-S1", CVO, "2026-10-13T09:00Z", "TEST_PROJ.TO-1 AC3: MET on read one."),
            row("TEST_PROJ-C-S2", CVO, "2026-10-16T12:00Z", "TEST_PROJ.TO-1 AC3: NOT MET on read two."),
            row("TEST_PROJ-C-S3", CVO, "2026-10-15T08:00Z", "TEST_PROJ.TO-1 AC3: MET on read three."),
        ]),
    }, "TEST_PROJ-C-S2", "NOT MET"))
    # (d) a newer row by the order's own doer (a self-grade) does not supersede an older CVO row.
    results.append(arm("(d) newer self-grade does not supersede older CVO row", {
        "adjudications/ADJUDICATION_v1.md": block([row("TEST_PROJ-C-S1", CVO, "2026-10-14T10:00Z",
                                                       "TEST_PROJ.TO-1 AC3: NOT MET on the CVO read.")]),
        "adjudications/ADJUDICATION_v2.md": block([row("TEST_PROJ-C-S2", DOER, "2026-10-16T12:00Z",
                                                       "TEST_PROJ.TO-1 AC3: MET, the doer's own read.")]),
    }, "TEST_PROJ-C-S1", "NOT MET"))
    # (e) a CVO row for another order's AC3 never competes, even when it is the newest.
    results.append(arm("(e) another order's AC3 never competes", {
        "adjudications/ADJUDICATION_v1.md": block([row("TEST_PROJ-C-S1", CVO, "2026-10-14T10:00Z",
                                                       "TEST_PROJ.TO-1 AC3: NOT MET on this order.")]),
        "adjudications/ADJUDICATION_v2.md": block([row("TEST_PROJ-C-S2", CVO, "2026-10-16T12:00Z",
                                                       "TEST_PROJ.TO-9 AC3: MET on another order.")]),
    }, "TEST_PROJ-C-S1", "NOT MET"))
    # (f) no CVO-kind row names the criterion: UNGRADED.
    results.append(arm_no_cvo_row())
    # (g) a row without surfaced_at, first in the file, loses to a dated row later in the file.
    results.append(arm("(g) undated row loses to a dated row", {
        "adjudications/ADJUDICATION_v1.md": block([row("TEST_PROJ-C-S1", CVO, None,
                                                       "TEST_PROJ.TO-1 AC3: NOT MET, undated.")]),
        "adjudications/ADJUDICATION_v2.md": block([row("TEST_PROJ-C-S2", CVO, "2026-10-14T10:00Z",
                                                       "TEST_PROJ.TO-1 AC3: MET, dated.")]),
    }, "TEST_PROJ-C-S2", "MET"))
    # (h) the real project.
    results.append(arm_real_round29())
    k, n = sum(1 for x in results if x), len(results)
    ok = k == n
    print("GRADE-OF-RECORD arms=%d/%d ok=%s" % (k, n, ok))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

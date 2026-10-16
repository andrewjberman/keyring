#!/usr/bin/env python3
"""test_round29_grade_not_a_mention.py -- NFRA_CTLPLN round 29, cell CT-bf-1 AMENDMENT 2 (site Z follow-up to
XB-20261016T121809Z-95c2; the head-anchored rule of AMENDMENT 1 is withdrawn).

round-close-check.py takes the grade of record across the CVO-kind rows that already grade a criterion, with SOURCE
PRIORITY: an ADJUDICATION-file grade always outranks an INVESTIGATION-file grade, whatever their dates; within one source
the latest surfaced_at wins (CT-be-1). An investigation grade is read only when no adjudication row grades the criterion.
So a row that reports the checker's defect and quotes its old verdict ("... TEST_PROJ.TO-1 AC3 reads NOT MET ...", in an
investigation file, newer) does not displace the real adjudication grade ("TEST_PROJ.TO-1 AC3: MET", older).

Arms (a)-(f) plant a temporary project tree and run the checker's check() end to end, reading the JUDGMENT line it prints.
Arm (g) is the control: a mutant copy of the checker that restores plain recency across sources must read arm (a) as
NOT MET by the defect report, and the arm must fail on it. Temporary trees only; no network; ASCII output.
LAST line: GRADE-NOT-A-MENTION arms=<k>/<n> ok=<True|False>
"""
from __future__ import annotations

import importlib.util
import json
import os
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
         '<criterion id="AC3" cell_refs="X" judgment="true"/>\n')
PROOF = {"to_id": "TEST_PROJ.TO-1", "acceptance": [
    {"criterion_id": "AC3", "status": "UNVERIFIABLE-BY-INSTRUMENT", "judgment": True}]}
# The AMENDMENT 2 rule line (one exact match in the checker). The control replaces it with plain recency across sources.
SOURCE_PRIORITY_LINE = "        pool = adj_c or inv_c\n"
MUTANT_LINE = "        pool = cands  # MUTANT: plain recency across sources (the reading AMENDMENT 2 withdraws)\n"
# The shape of the site Z defect report (NFRA_OPLGTW-Z-S176): the head of its one_line (the real first 160 characters, with
# the order's id written as TEST_PROJ.TO-1 in place of TO-OG-ap-14, so the head is a little longer); the criterion sits
# past character 80 and the old NOT MET verdict follows it in the same one_line.
DEFECT_ONE_LINE = ("round-close-check credits each judgment criterion to the FIRST CVO-kind grading row in file order, so a "
                   "later superseding grade is invisible: TEST_PROJ.TO-1 AC3 reads NOT MET in its old output; that verdict "
                   "was wrong.")


def load(name: str, path: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


RCC = load("opal_rcc_not_a_mention", CHECKER)
SL = load("opal_sl_not_a_mention", os.path.join(TOOLS, "seat-list.py"))


def row(rid: str, by: str, at=None, text: str = "", **extra) -> dict:
    doc = {"id": rid, "surfaced_by": by, "one_line": text}
    if at is not None:
        doc["surfaced_at"] = at
    doc.update(extra)
    return doc


def block(rows: list) -> str:
    return "# rows\n\n```json\n%s\n```\n" % json.dumps(rows, indent=1)


def plant(files: dict) -> str:
    """A temporary project tree: one project, one complete order (TO-1, judgment criterion AC3), its proof, the given
    surprise-channel files, and a liveness file that names a live CVO-kind seat and the issuer."""
    tmp = tempfile.mkdtemp(prefix="gnm29_")

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


def run_check(tmp: str, rcc=None):
    """(JUDGMENT lines, last line) of the checker (rcc, default the real one) over the planted tree."""
    mod = rcc or RCC
    kind_of = mod.make_kind_of(ROOT)
    lines, last = mod.check(tmp, SL, SL.Ctx(tmp), "TEST_PROJ", None, None, "testbox", "testbox", kind_of)
    return [ln for ln in lines if ln.startswith("  JUDGMENT ")], last


def is_grade(judg: list, row_id: str, verdict: str) -> bool:
    """True when the one JUDGMENT line reads GRADED by the named row, with the named verdict."""
    if len(judg) != 1:
        return False
    line = judg[0]
    return " -> GRADED (" in line and ("row %s by " % row_id) in line and ("(verdict %s)" % verdict) in line


def shown(judg: list) -> str:
    return judg[0].strip() if len(judg) == 1 else repr(judg)


def arm(label: str, files: dict, row_id: str, verdict: str) -> bool:
    tmp = plant(files)
    try:
        judg, _last = run_check(tmp)
        ok = is_grade(judg, row_id, verdict)
        print("%s  %s -> %s" % ("PASS" if ok else "FAIL", label, shown(judg)))
        return ok
    except Exception as exc:  # noqa: BLE001 - an arm that raises is a failed arm, named
        print("FAIL  %s -> raised %s: %s" % (label, type(exc).__name__, exc))
        return False
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def mutant_checker():
    """A copy of the checker that restores plain recency across sources (the reading AMENDMENT 2 withdraws): the grade of
    record is taken over every candidate, adjudication and investigation alike. The rule line must match exactly once, or
    the control refuses to run."""
    with open(CHECKER, encoding="utf-8") as fh:
        src = fh.read()
    if src.count(SOURCE_PRIORITY_LINE) != 1:
        raise RuntimeError("the CT-bf-1 source-priority line matches %d times, not once" % src.count(SOURCE_PRIORITY_LINE))
    mutated = src.replace(SOURCE_PRIORITY_LINE, MUTANT_LINE)
    d = tempfile.mkdtemp(prefix="gnm29_mutant_")
    path = os.path.join(d, "round_close_check_mutant.py")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(mutated)
    try:
        return load("opal_rcc_mutant", path)
    finally:
        shutil.rmtree(d, ignore_errors=True)


SITE_Z_FILES = {
    # the real grade: a CVO adjudication row, MET, older (NFRA_OPLGTW-Z-C-S79).
    "adjudications/ADJUDICATION_v1.md": block([row("TEST_PROJ-C-S79", CVO, "2026-10-16T12:10Z",
                                                   "TEST_PROJ.TO-1 AC3: MET on the regrade.")]),
    # the defect report: a CVO investigation row, newer (NFRA_OPLGTW-Z-S176), that grades nothing and quotes the old NOT MET.
    "investigations/INVESTIGATION_v1.md": block([row("TEST_PROJ-C-S176", CVO, "2026-10-16T12:20Z", DEFECT_ONE_LINE)]),
}


def arm_a() -> bool:
    """(a) site Z's real shape: an older adjudication row MET; a newer investigation row whose one_line names the criterion
    past character 80 and quotes NOT MET. The adjudication grade is the grade of record: MET from C-S79."""
    if DEFECT_ONE_LINE.index("AC3") < 80:
        raise RuntimeError("the defect shape must put AC3 past character 80")
    return arm("(a) defect report quoting NOT MET in a newer investigation row does not displace the adjudication MET",
               SITE_Z_FILES, "TEST_PROJ-C-S79", "MET")


def arm_b() -> bool:
    """(b) an investigation row alone (no adjudication row) grades as before, and the newest wins among investigation rows:
    an older structured NOT MET, then a newer prose MET deep in the one_line. MET from the newer row."""
    return arm("(b) investigation rows alone: newest grade wins (structured older, prose newer)", {
        "investigations/INVESTIGATION_v1.md": block([
            row("TEST_PROJ-C-S1", CVO, "2026-10-14T10:00Z", "The first read of the regrade.",
                grades=[{"criterion": "AC3", "verdict": "NOT MET", "instance": "TEST_PROJ.TO-1"}]),
            row("TEST_PROJ-C-S2", CVO, "2026-10-16T12:00Z",
                "The regrade is recorded here: TEST_PROJ.TO-1 AC3 MET on the regrade, the first read superseded."),
        ]),
    }, "TEST_PROJ-C-S2", "MET")


def arm_c() -> bool:
    """(c) adjudication NOT MET (newer) over adjudication MET (older): NOT MET. Recency within one source, the CT-be-1 rule."""
    return arm("(c) adjudication rows: newer NOT MET over older MET -> NOT MET (recency within a source)", {
        "adjudications/ADJUDICATION_v1.md": block([row("TEST_PROJ-C-S1", CVO, "2026-10-14T10:00Z",
                                                       "TEST_PROJ.TO-1 AC3: MET on the first read.")]),
        "adjudications/ADJUDICATION_v2.md": block([row("TEST_PROJ-C-S2", CVO, "2026-10-16T12:00Z",
                                                       "TEST_PROJ.TO-1 AC3: NOT MET on the regrade.")]),
    }, "TEST_PROJ-C-S2", "NOT MET")


def arm_d() -> bool:
    """(d) an investigation row NEWER and different (structured MET) over an older adjudication NOT MET: the adjudication row
    wins, whatever the dates."""
    return arm("(d) newer investigation MET does not displace an older adjudication NOT MET", {
        "adjudications/ADJUDICATION_v1.md": block([row("TEST_PROJ-C-S1", CVO, "2026-10-14T10:00Z",
                                                       "TEST_PROJ.TO-1 AC3: NOT MET on the first read.")]),
        "investigations/INVESTIGATION_v1.md": block([row(
            "TEST_PROJ-C-S2", CVO, "2026-10-16T12:00Z", "The regrade of TEST_PROJ.TO-1 AC3 is recorded in the entry.",
            grades=[{"criterion": "AC3", "verdict": "MET", "instance": "TEST_PROJ.TO-1"}])]),
    }, "TEST_PROJ-C-S1", "NOT MET")


def arm_e() -> bool:
    """(e) a self-grade never competes: a newer adjudication row by the order's own issuer does not displace an older
    CVO MET."""
    return arm("(e) newer self-grade does not compete with older CVO MET", {
        "adjudications/ADJUDICATION_v1.md": block([row("TEST_PROJ-C-S1", CVO, "2026-10-14T10:00Z",
                                                       "TEST_PROJ.TO-1 AC3: MET on the CVO read.")]),
        "adjudications/ADJUDICATION_v2.md": block([row("TEST_PROJ-C-S2", DOER, "2026-10-16T12:00Z",
                                                       "TEST_PROJ.TO-1 AC3: NOT MET, the doer's own read.")]),
    }, "TEST_PROJ-C-S1", "MET")


def arm_f() -> bool:
    """(f) a generic AC3 of another order never competes: a newer investigation row with a structured MET for
    TEST_PROJ.TO-9 AC3 does not displace the older NOT MET for this order."""
    return arm("(f) another order's AC3 (structured, newer) never competes", {
        "adjudications/ADJUDICATION_v1.md": block([row("TEST_PROJ-C-S1", CVO, "2026-10-14T10:00Z",
                                                       "TEST_PROJ.TO-1 AC3: NOT MET on this order.")]),
        "investigations/INVESTIGATION_v1.md": block([row(
            "TEST_PROJ-C-S2", CVO, "2026-10-16T12:00Z", "TEST_PROJ.TO-9 AC3 regraded.",
            grades=[{"criterion": "AC3", "verdict": "MET", "instance": "TEST_PROJ.TO-9"}])]),
    }, "TEST_PROJ-C-S1", "NOT MET")


def arm_g() -> bool:
    """(g) control: a mutant that restores plain recency across sources reads arm (a) as NOT MET by the defect report, so
    arm (a) discriminates the source-priority rule from plain recency, and this arm fails on the mutant."""
    tmp = plant(SITE_Z_FILES)
    try:
        judg, _last = run_check(tmp, rcc=mutant_checker())
        ok = is_grade(judg, "TEST_PROJ-C-S176", "NOT MET") and not is_grade(judg, "TEST_PROJ-C-S79", "MET")
        print("%s  (g) control: plain-recency mutant reads (a) as NOT MET -> %s" % ("PASS" if ok else "FAIL", shown(judg)))
        return ok
    except Exception as exc:  # noqa: BLE001
        print("FAIL  (g) control -> raised %s: %s" % (type(exc).__name__, exc))
        return False
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main() -> int:
    results = [arm_a(), arm_b(), arm_c(), arm_d(), arm_e(), arm_f(), arm_g()]
    k, n = sum(1 for x in results if x), len(results)
    ok = k == n
    print("GRADE-NOT-A-MENTION arms=%d/%d ok=%s" % (k, n, ok))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

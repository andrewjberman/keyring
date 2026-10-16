#!/usr/bin/env python3
"""test_round29_grade_not_a_mention.py -- NFRA_CTLPLN round 29, cell CT-bf-1 AMENDMENT 1 (site Z follow-up to
XB-20261016T121809Z-95c2).

round-close-check.py reads a prose grade in an INVESTIGATION-file row only from the HEAD of the row: the criterion's
first character must be among the first HEAD_CHARS (80) characters of the row's one_line, with a verdict word after it
(verdict_after). A `grades` entry grades as before, and an ADJUDICATION-file row grades as before. A prose mention deeper
in a row is not a grade: a row that reports the checker's defect and quotes its old verdict ("... TEST_PROJ.TO-1 AC3
reads NOT MET ...", criterion past character 80) never becomes the grade of record. The CT-be-1 recency rule still holds.

Columns in this file are 1-based: "column 79" is the 79th character of the one_line.

Arms (a)-(f) and (h1)-(h2) plant a temporary project tree and run the checker's check() end to end, reading the JUDGMENT
line it prints. Arm (g) is the control: a mutant copy of the checker that restores the old rule (a prose mention anywhere
grades) must read arm (a) as NOT MET. Temporary trees only; no network; ASCII output.
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
OLD_RULE_LINE = '                if source == "investigation":\n'
HEAD_CHARS = 80
# The shape of the site Z defect report (NFRA_OPLGTW-Z-S176): the criterion sits past character 80, the old NOT MET verdict
# is quoted later in the same one_line, and the row grades nothing.
DEFECT_ONE_LINE = ("round-close-check credits each judgment criterion to the FIRST CVO-kind grading row in file order, so a "
                   "later superseding grade is invisible: TEST_PROJ.TO-1 AC3 reads NOT MET in its old output; that verdict "
                   "was wrong.")
ORDER_TOKEN = "TEST_PROJ.TO-1 "


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


def at_column(col: int, verdict: str = "MET") -> str:
    """A one_line whose criterion AC3 starts at 1-based column `col`: "L9 ", filler dashes, the order's name, then AC3."""
    n = col - 20
    one = "L9 " + "-" * n + " " + ORDER_TOKEN + "AC3 " + verdict + " on the regrade."
    if one.index("AC3") + 1 != col:
        raise RuntimeError("at_column(%d) puts AC3 at column %d" % (col, one.index("AC3") + 1))
    return one


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
    """A copy of the checker that restores the old rule: an investigation row grades by its verdict anywhere in the row
    (the CT-be-1 reading). The one line that carries the rule must match exactly once, or the control refuses to run."""
    with open(CHECKER, encoding="utf-8") as fh:
        src = fh.read()
    if src.count(OLD_RULE_LINE) != 1:
        raise RuntimeError("the CT-bf-1 rule line matches %d times, not once" % src.count(OLD_RULE_LINE))
    mutated = src.replace(OLD_RULE_LINE, "                if False:  # MUTANT: old rule\n")
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
    # the defect report: a CVO investigation row, newer (NFRA_OPLGTW-Z-S176), that quotes the old NOT MET past character 80.
    "investigations/INVESTIGATION_v1.md": block([row("TEST_PROJ-C-S176", CVO, "2026-10-16T12:20Z", DEFECT_ONE_LINE)]),
}


def arm_a() -> bool:
    """(a) site Z's shape, planted for real: MET in an older adjudication row; a newer investigation row whose one_line
    names the criterion past character 80 and quotes NOT MET: MET from the adjudication row."""
    if DEFECT_ONE_LINE.index("AC3") < HEAD_CHARS:
        raise RuntimeError("the defect shape must put AC3 past character 80")
    return arm("(a) defect report quoting NOT MET past character 80 does not grade; MET from adjudication row", SITE_Z_FILES,
               "TEST_PROJ-C-S79", "MET")


def arm_a2() -> bool:
    """(a2) a head-anchored prose grade still grades: an investigation row whose one_line starts "L9 <order> AC3 MET" is
    read from its head and wins by recency over an older adjudication NOT MET. (A generic id names its order before it,
    as the rule has always required, so the head carries the order's name.)"""
    return arm("(a2) head-anchored prose grade in a newer investigation row grades and wins by recency", {
        "adjudications/ADJUDICATION_v1.md": block([row("TEST_PROJ-C-S1", CVO, "2026-10-14T10:00Z",
                                                       "TEST_PROJ.TO-1 AC3: NOT MET on the first read.")]),
        "investigations/INVESTIGATION_v1.md": block([row(
            "TEST_PROJ-C-S2", CVO, "2026-10-16T12:00Z", "L9 TEST_PROJ.TO-1 AC3 MET on the regrade; the first read is superseded.")]),
    }, "TEST_PROJ-C-S2", "MET")


def arm_b() -> bool:
    """(b) an investigation row with a structured grades entry naming the criterion with a verdict still counts, and
    wins by recency over an older adjudication row. The prose of the row is a deep mention, so only the entry grades it."""
    return arm("(b) structured grades entry in a newer investigation row counts and wins by recency", {
        "adjudications/ADJUDICATION_v1.md": block([row("TEST_PROJ-C-S1", CVO, "2026-10-14T10:00Z",
                                                       "TEST_PROJ.TO-1 AC3: NOT MET on the first read.")]),
        "investigations/INVESTIGATION_v1.md": block([row(
            "TEST_PROJ-C-S2", CVO, "2026-10-16T12:00Z", "The regrade of TEST_PROJ.TO-1 AC3 is recorded in the entry.",
            grades=[{"criterion": "AC3", "verdict": "MET", "instance": "TEST_PROJ.TO-1"}])]),
    }, "TEST_PROJ-C-S2", "MET")


def arm_c() -> bool:
    """(c) an investigation-row prose mention past character 80, with a verdict, and NO adjudication row anywhere: UNGRADED,
    and the detail names the cause (a prose mention is not a grade)."""
    tmp = plant({"investigations/INVESTIGATION_v1.md": block([row("TEST_PROJ-C-S3", CVO, "2026-10-16T12:20Z", DEFECT_ONE_LINE)])})
    try:
        judg, last = run_check(tmp)
        ok = (len(judg) == 1 and " -> UNGRADED (" in judg[0] and "names it in prose only" in judg[0]
              and "a prose mention is not a grade" in judg[0] and "verdict=REFUSED" in last)
        print("%s  (c) investigation prose mention past the head only -> %s" % ("PASS" if ok else "FAIL", shown(judg)))
        return ok
    except Exception as exc:  # noqa: BLE001
        print("FAIL  (c) investigation prose mention only -> raised %s: %s" % (type(exc).__name__, exc))
        return False
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def arm_d() -> bool:
    """(d) the CT-be-1 planted pair, both in adjudication rows: older NOT MET then newer MET reads MET; the reverse
    reads NOT MET. Both orders must hold."""
    fwd = arm("(d1) CT-be-1 pair: older NOT MET, newer MET -> MET", {
        "adjudications/ADJUDICATION_v1.md": block([row("TEST_PROJ-C-S1", CVO, "2026-10-14T10:00Z",
                                                       "TEST_PROJ.TO-1 AC3: NOT MET on the first read.")]),
        "adjudications/ADJUDICATION_v2.md": block([row("TEST_PROJ-C-S2", CVO, "2026-10-16T12:00Z",
                                                       "TEST_PROJ.TO-1 AC3: MET on the regrade.")]),
    }, "TEST_PROJ-C-S2", "MET")
    rev = arm("(d2) CT-be-1 pair reversed: older MET, newer NOT MET -> NOT MET", {
        "adjudications/ADJUDICATION_v1.md": block([row("TEST_PROJ-C-S1", CVO, "2026-10-14T10:00Z",
                                                       "TEST_PROJ.TO-1 AC3: MET on the first read.")]),
        "adjudications/ADJUDICATION_v2.md": block([row("TEST_PROJ-C-S2", CVO, "2026-10-16T12:00Z",
                                                       "TEST_PROJ.TO-1 AC3: NOT MET on the regrade.")]),
    }, "TEST_PROJ-C-S2", "NOT MET")
    return fwd and rev


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
    """(g) control: a mutant that restores the old rule reads arm (a) as NOT MET by the defect report, so arm (a)
    discriminates the old rule from the new one."""
    tmp = plant(SITE_Z_FILES)
    try:
        judg, _last = run_check(tmp, rcc=mutant_checker())
        ok = is_grade(judg, "TEST_PROJ-C-S176", "NOT MET") and not is_grade(judg, "TEST_PROJ-C-S79", "MET")
        print("%s  (g) control: old-rule mutant reads (a) as NOT MET -> %s" % ("PASS" if ok else "FAIL", shown(judg)))
        return ok
    except Exception as exc:  # noqa: BLE001
        print("FAIL  (g) control -> raised %s: %s" % (type(exc).__name__, exc))
        return False
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def arm_h(col: int, grades: bool) -> bool:
    """(h1) the criterion at column 79 (its first character is the 79th of the one_line, inside the head) grades from the
    investigation row by its prose; (h2) at column 81 (outside the head) it does not: UNGRADED, cause named."""
    tmp = plant({"investigations/INVESTIGATION_v1.md": block([row("TEST_PROJ-C-S4", CVO, "2026-10-16T12:20Z", at_column(col))])})
    try:
        judg, last = run_check(tmp)
        if grades:
            ok = is_grade(judg, "TEST_PROJ-C-S4", "MET")
        else:
            ok = (len(judg) == 1 and " -> UNGRADED (" in judg[0] and "names it in prose only" in judg[0]
                  and "verdict=REFUSED" in last)
        label = "(h1) criterion at column 79 grades from the head" if grades else "(h2) criterion at column 81 does not grade"
        print("%s  %s -> %s" % ("PASS" if ok else "FAIL", label, shown(judg)))
        return ok
    except Exception as exc:  # noqa: BLE001
        print("FAIL  (h) edge column %d -> raised %s: %s" % (col, type(exc).__name__, exc))
        return False
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main() -> int:
    results = [arm_a(), arm_a2(), arm_b(), arm_c(), arm_d(), arm_e(), arm_f(), arm_h(79, True), arm_h(81, False), arm_g()]
    k, n = sum(1 for x in results if x), len(results)
    ok = k == n
    print("GRADE-NOT-A-MENTION arms=%d/%d ok=%s" % (k, n, ok))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

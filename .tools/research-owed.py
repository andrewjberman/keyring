#!/usr/bin/env python3
"""research-owed.py -- is research owed? Read from the class, never judged (NFRA_CTLPLN workstream SEATS, cell CT-s-8;
contract C-SEATS; FWD-24).

The CTO's ruling of call A, from Andrew's word: "Research is owed for an operation of stakes class S3 or above
(org/tier0/STAKES_MATRIX.md) or a task order classed WORLD. Below that, none."

    python .tools/research-owed.py --order <task order file>        reads the order's <risk> (and a <stakes> element, if present)
    python .tools/research-owed.py --stakes <S0|S1|S2|S3|S4>        a given operation class
    python .tools/research-owed.py --selftest

Prints  RESEARCH-OWED subject=<order id or class> risk=<LOCAL|SERVED|WORLD|-> stakes=<S0..S4|-> verdict=<OWED|NOT-OWED|UNCLASSED> rule=<...>
OWED when the order's <risk> is WORLD or the stakes class is S3 or S4; NOT-OWED otherwise. An order with no <risk> element, a
<risk> outside LOCAL/SERVED/WORLD, or a stakes class outside the matrix's table is UNCLASSED: exit 3, never guessed.
The stakes class of an OPERATION is GIVEN (the flag, or the order's <stakes> element); this tool does not classify an
operation, because the matrix is Andrew's and its classification rules are judgment. Class names and their order are read from
the class table of org/tier0/STAKES_MATRIX.md (READ ONLY); if that table no longer reads S0..S4 in order the tool stops
(exit 2) rather than apply a threshold to classes it does not know. Deterministic: same input, same line, any box.
Exit: 0 verdict printed (OWED or NOT-OWED) | 2 usage, or the matrix no longer reads as expected | 3 UNCLASSED.
Selftest LAST line: RESEARCH-OWED-SELFTEST cases=<k>/<n> ok=<True|False>.
"""
from __future__ import annotations

import argparse
import os
import re
import sys
import tempfile

TOOLS = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(TOOLS)
MATRIX = os.path.join(ROOT, "org", "tier0", "STAKES_MATRIX.md")
RISKS = ("LOCAL", "SERVED", "WORLD")
EXPECTED = ["S0", "S1", "S2", "S3", "S4"]
THRESHOLD = "S3"
CLASS_ROW = re.compile(r"^\|\s*\*\*(S\d+)\*\*", re.M)


class MatrixError(Exception):
    pass


def matrix_classes(text: str) -> list:
    """The class names of the matrix's class table, in table order."""
    found = CLASS_ROW.findall(text)
    if found != EXPECTED:
        raise MatrixError("the class table of org/tier0/STAKES_MATRIX.md reads %s, this tool was written for %s; "
                          "the rule is Andrew's and is not re-applied to classes it was not written for" % (found, EXPECTED))
    return found


def tag(text: str, name: str):
    hits = re.findall(r"^<%s>(.*?)</%s>" % (name, name), text, re.M)
    return hits


def decide(subject: str, risk, stakes, classes: list) -> tuple:
    """(line, rc). risk and stakes are strings or None (not given)."""
    if risk is not None and risk not in RISKS:
        return "RESEARCH-OWED subject=%s risk=- stakes=- verdict=UNCLASSED rule=<risk> %r is not one of %s" % (
            subject, risk, "/".join(RISKS)), 3
    if stakes is not None and stakes not in classes:
        return "RESEARCH-OWED subject=%s risk=- stakes=- verdict=UNCLASSED rule=stakes %r is not a class of the matrix (%s)" % (
            subject, stakes, "/".join(classes)), 3
    if risk is None and stakes is None:
        return "RESEARCH-OWED subject=%s risk=- stakes=- verdict=UNCLASSED rule=no <risk> element and no stakes class given" % subject, 3
    owed_by = []
    if risk == "WORLD":
        owed_by.append("task order classed WORLD")
    if stakes is not None and classes.index(stakes) >= classes.index(THRESHOLD):
        owed_by.append("stakes class %s is %s or above" % (stakes, THRESHOLD))
    verdict = "OWED" if owed_by else "NOT-OWED"
    rule = "; ".join(owed_by) if owed_by else "below S3 and not WORLD (org/tier0/STAKES_MATRIX.md; CTO ruling of call A)"
    return "RESEARCH-OWED subject=%s risk=%s stakes=%s verdict=%s rule=%s" % (
        subject, risk or "-", stakes or "-", verdict, rule), 0


def from_order(path: str, flag_stakes, classes: list) -> tuple:
    text = open(path, encoding="utf-8", errors="replace").read()
    ids = tag(text, "to_id")
    subject = ids[0].strip() if ids else os.path.basename(path)
    risks = tag(text, "risk")
    stakes_els = tag(text, "stakes")
    if len(risks) > 1 or len(stakes_els) > 1:
        return "RESEARCH-OWED subject=%s risk=- stakes=- verdict=UNCLASSED rule=more than one <risk> or <stakes> element" % subject, 3
    risk = risks[0].strip() if risks else None
    if risk is None:
        return "RESEARCH-OWED subject=%s risk=- stakes=- verdict=UNCLASSED rule=no <risk> element" % subject, 3
    stakes = flag_stakes or (stakes_els[0].strip() if stakes_els else None)
    return decide(subject, risk, stakes, classes)


def selftest() -> int:
    classes = matrix_classes(open(MATRIX, encoding="utf-8").read())
    results = []

    def case(name, got, want_verdict, want_rc):
        line, rc = got
        ok = ("verdict=%s" % want_verdict) in line and rc == want_rc
        results.append(ok)
        print("%s  %s -> %s (rc %d)" % ("PASS" if ok else "FAIL", name, line if not ok else "verdict=" + want_verdict, rc))

    for r, v in (("LOCAL", "NOT-OWED"), ("SERVED", "NOT-OWED"), ("WORLD", "OWED")):
        case("risk %s" % r, decide("probe", r, None, classes), v, 0)
    for s, v in (("S0", "NOT-OWED"), ("S1", "NOT-OWED"), ("S2", "NOT-OWED"), ("S3", "OWED"), ("S4", "OWED")):
        case("stakes %s" % s, decide("probe", None, s, classes), v, 0)
    tmp = tempfile.mkdtemp(prefix="research_owed_")
    paths = []
    try:
        def order(name, body):
            p = os.path.join(tmp, name)
            with open(p, "w", encoding="utf-8", newline="\n") as fh:
                fh.write(body)
            paths.append(p)
            return p
        case("an order with no <risk> element is UNCLASSED", from_order(order("a.md", "<to_id>X.TO-1</to_id>\n<status>issued</status>\n"), None, classes), "UNCLASSED", 3)
        case("an order with <risk> outside the enum is UNCLASSED", from_order(order("b.md", "<to_id>X.TO-2</to_id>\n<risk>PROD</risk>\n"), None, classes), "UNCLASSED", 3)
        case("a stakes class outside the table is UNCLASSED", decide("probe", None, "S9", classes), "UNCLASSED", 3)
        case("an order <risk>WORLD</risk> read from the file", from_order(order("c.md", "<to_id>X.TO-3</to_id>\n<risk>WORLD</risk>\n"), None, classes), "OWED", 0)
        case("an order <risk>LOCAL</risk> with a <stakes>S3</stakes> element", from_order(order("d.md", "<to_id>X.TO-4</to_id>\n<risk>LOCAL</risk>\n<stakes>S3</stakes>\n"), None, classes), "OWED", 0)
        case("an order <risk>SERVED</risk> alone", from_order(order("e.md", "<to_id>X.TO-5</to_id>\n<risk>SERVED</risk>\n"), None, classes), "NOT-OWED", 0)
        same = from_order(paths[2], None, classes) == from_order(paths[2], None, classes)
        results.append(same)
        print("%s  the same input gives the same line twice" % ("PASS" if same else "FAIL"))
        try:
            matrix_classes("| **S0** x |\n| **S1** x |\n| **S2** x |\n| **S3** x |\n| **S5** x |\n")
            renamed = False
        except MatrixError:
            renamed = True
        results.append(renamed)
        print("%s  a renamed class in the matrix table is caught, not applied" % ("PASS" if renamed else "FAIL"))
    finally:
        for p in paths:
            if os.path.exists(p):
                os.remove(p)
        os.rmdir(tmp)
    ok = all(results)
    print("RESEARCH-OWED-SELFTEST cases=%d/%d ok=%s" % (sum(results), len(results), ok))
    return 0 if ok else 1


def main(argv: list) -> int:
    ap = argparse.ArgumentParser(prog="research-owed.py", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--order")
    ap.add_argument("--stakes")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args(argv)
    try:
        if args.selftest:
            return selftest()
        classes = matrix_classes(open(MATRIX, encoding="utf-8").read())
    except (MatrixError, OSError) as exc:
        print("ERROR: %s" % exc, file=sys.stderr)
        return 2
    if bool(args.order) == bool(args.stakes) and not (args.order and args.stakes):
        print("ERROR: give --order <file> or --stakes <class>", file=sys.stderr)
        return 2
    if args.order:
        try:
            line, rc = from_order(args.order, args.stakes, classes)
        except OSError as exc:
            print("ERROR: %s" % exc, file=sys.stderr)
            return 2
    else:
        line, rc = decide(args.stakes, None, args.stakes, classes)
    print(line)
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

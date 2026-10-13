#!/usr/bin/env python3
"""NFRA_CTLPLN.TO-CT-ab-8 (FWD-2): the two hand-typed box lists in the tools derive from the device register.

The register is org/devices/DEVICES.json, read only through lib/devices.py. Arms (standard library only, AST reads
of the two files, no regex over source):
  1. gate: FABRIC_ENUM in .tools/to-pipeline-gate.py is not a literal, and its value equals placement_values().
  2. status report: BOXES in .tools/box-status-report-check.py is not a literal, and its value equals set(names()).
  3. no literal box list: neither file holds a tuple, list or set literal of two or more box names (box names =
     the register names, aliases and placement values, lower-cased).

LAST line: BOX-LISTS-FROM-REGISTER gate=<derived|literal> status_report=<derived|literal> ok=<True|False>
"""
import ast
import importlib.util
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GATE_REL = ".tools/to-pipeline-gate.py"
REPORT_REL = ".tools/box-status-report-check.py"
RESULTS = []


def case(name, ok, detail=""):
    RESULTS.append(bool(ok))
    print("%s  %s%s" % ("PASS" if ok else "FAIL", name, (" | " + detail) if detail else ""))


def load(name, rel):
    spec = importlib.util.spec_from_file_location(name, os.path.join(ROOT, *rel.split("/")))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def tree_of(rel):
    with open(os.path.join(ROOT, *rel.split("/")), encoding="utf-8") as fh:
        return ast.parse(fh.read())


def module_value(tree, symbol):
    """The value node of the module-level assignment to symbol, or None when the file does not assign it."""
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == symbol for t in node.targets):
            return node.value
    return None


def is_literal(node):
    try:
        ast.literal_eval(node)
        return True
    except (ValueError, TypeError):
        return False


def box_words(devices):
    words = set()
    for d in devices.devices():
        words.add(d["name"].lower())
        words.update(a.lower() for a in d.get("aliases", []))
    words.update(v.lower() for v in devices.placement_values())
    return words


def box_literal_lists(tree, words):
    """(containers scanned, line numbers of tuple/list/set literals holding two or more box names)."""
    scanned, hits = 0, []
    for node in ast.walk(tree):
        if isinstance(node, (ast.Tuple, ast.List, ast.Set)):
            scanned += 1
            strs = {e.value.lower() for e in node.elts if isinstance(e, ast.Constant) and isinstance(e.value, str)}
            if len(strs & words) >= 2:
                hits.append(node.lineno)
    return scanned, hits


def mode_of(node):
    if node is None:
        return "absent"
    return "literal" if is_literal(node) else "derived"


def main():
    devices = load("devices_for_box_lists", "lib/devices.py")
    gate = load("to_pipeline_gate_box_lists", GATE_REL)
    report = load("box_status_report_box_lists", REPORT_REL)
    words = box_words(devices)
    gate_tree, report_tree = tree_of(GATE_REL), tree_of(REPORT_REL)
    gate_mode = mode_of(module_value(gate_tree, "FABRIC_ENUM"))
    report_mode = mode_of(module_value(report_tree, "BOXES"))
    gate_value = tuple(gate.FABRIC_ENUM)
    gate_want = tuple(devices.placement_values())
    report_value = set(report.BOXES)
    report_want = set(devices.names())
    gate_scanned, gate_hits = box_literal_lists(gate_tree, words)
    report_scanned, report_hits = box_literal_lists(report_tree, words)

    case("gate FABRIC_ENUM is derived, not a literal (AST %s)" % gate_mode, gate_mode == "derived", gate_mode)
    case("gate FABRIC_ENUM equals lib/devices placement_values()", gate_value == gate_want,
         "%r vs %r" % (gate_value, gate_want))
    case("gate holds no literal box list (%d containers scanned)" % gate_scanned, not gate_hits,
         "literal box lists at lines %s" % gate_hits)
    case("status report BOXES is derived, not a literal (AST %s)" % report_mode, report_mode == "derived", report_mode)
    case("status report BOXES equals set(lib/devices names())", report_value == report_want,
         "%r vs %r" % (sorted(report_value), sorted(report_want)))
    case("status report holds no literal box list (%d containers scanned)" % report_scanned, not report_hits,
         "literal box lists at lines %s" % report_hits)
    ok = all(RESULTS)
    print("BOX-LISTS-FROM-REGISTER gate=%s status_report=%s ok=%s" % (gate_mode, report_mode, ok))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

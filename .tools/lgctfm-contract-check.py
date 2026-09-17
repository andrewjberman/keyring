#!/usr/bin/env python
"""lgctfm-contract-check.py -- the OWNING tool for the lgctfm-contract artifact type (LGIC_LGCTFM PRD DEC-11,
cell LT-s-2). `.tools/receiving-check.py` DISPATCHES to this tool as a subprocess for any run's
`workflows/legacy_transform/<subject>/<run-id>/contract.json` and any file ending `.lgctfm-contract.json`;
it re-implements nothing here, and this tool is what actually grades the artifact.

Schema: `org/standards/LGCTFM_CONTRACT.schema.json` (authored from `infra/logic/11_LGCTFM_CONTRACT_SCHEMA_RECORD.md`,
LT-s-1). A JSON Schema tells a reader THAT a document is malformed, never in this contract's own vocabulary --
so this tool runs two passes:

  1. A TARGETED WALK of the contract's own cell-shaped fields (trigger_denominator's two APIs; every
     RESOURCE/PLANE row's `current` and `desired` fields; every FORK row's `one_job` and `canonical_member`;
     every tension's `factors`; `subject.vintage`), printing one line per defect NAMING it with one of four
     tokens:
         bare-value            a field where a cell {value, status, evidence} belongs holds something else
         trigger-denominator   `list_rules` or `list_schedules` is missing from trigger_denominator
         evidence-instrument   a cell is present but its `evidence.instrument` is missing or empty
         vintage               `subject.vintage.repo_head` / `.graph_built` / `.registry_hash` is missing
  2. Full JSON-Schema validation against LGCTFM_CONTRACT.schema.json for everything the targeted walk does
     not name (wrong enum, missing top-level field, wrong row shape, ...), printed as `schema: <path>: <msg>`.

Exit 0 when both passes find nothing; exit 1 otherwise, having printed every defect found (never truncated
to the first).

Usage: python .tools/lgctfm-contract-check.py <contract.json>

ASCII only. LF endings.
"""
from __future__ import annotations

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
SCHEMA_PATH = os.path.join(REPO, "org", "standards", "LGCTFM_CONTRACT.schema.json")


def load_json(path):
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh), None
    except FileNotFoundError:
        return None, "absent: %s" % path
    except ValueError as exc:
        return None, "not JSON: %s (%s)" % (path, exc)


def is_cell(x):
    return isinstance(x, dict) and "value" in x and "status" in x and "evidence" in x


def cell_defects(path_label, x, defects):
    """`x` is a field where the schema requires a cell. Names bare-value or evidence-instrument."""
    if not is_cell(x):
        defects.append("bare-value: %s is a bare value where a cell {value, status, evidence} belongs (got %s)"
                        % (path_label, type(x).__name__ if not isinstance(x, dict) else "an object missing "
                           "value/status/evidence"))
        return
    ev = x.get("evidence")
    instrument = ev.get("instrument") if isinstance(ev, dict) else None
    if not instrument:
        defects.append("evidence-instrument: %s.evidence.instrument is missing" % path_label)


def walk_contract(doc):
    """The targeted walk. Returns a list of defect lines, each naming its token."""
    defects = []

    # trigger_denominator: both APIs must be present, each a cell.
    td = doc.get("trigger_denominator")
    if isinstance(td, dict):
        for api in ("list_rules", "list_schedules"):
            if api not in td:
                defects.append("trigger-denominator: %s is missing from trigger_denominator "
                                "(both APIs must be measured)" % api)
            else:
                cell_defects("trigger_denominator.%s" % api, td[api], defects)
        for extra, val in td.items():
            if extra not in ("list_rules", "list_schedules"):
                cell_defects("trigger_denominator.%s" % extra, val, defects)
    else:
        defects.append("trigger-denominator: trigger_denominator is missing or not an object")

    # subject.vintage: three plain-string fields, not cells.
    subject = doc.get("subject")
    vintage = subject.get("vintage") if isinstance(subject, dict) else None
    if isinstance(vintage, dict):
        for field in ("repo_head", "graph_built", "registry_hash"):
            if not vintage.get(field):
                defects.append("vintage: subject.vintage.%s is missing" % field)
    else:
        defects.append("vintage: subject.vintage is missing or not an object")

    # rows: RESOURCE/PLANE carry current + desired; FORK carries one_job + canonical_member.
    for i, row in enumerate(doc.get("rows") or []):
        if not isinstance(row, dict):
            continue
        label = "rows[%d]" % i
        kind = row.get("kind")
        if kind in ("RESOURCE", "PLANE"):
            for half in ("current", "desired"):
                block = row.get(half)
                if isinstance(block, dict):
                    for field, val in block.items():
                        cell_defects("%s.%s.%s" % (label, half, field), val, defects)
                elif half in row:
                    defects.append("bare-value: %s.%s is not an object of cells" % (label, half))
        elif kind == "FORK":
            for field in ("one_job", "canonical_member"):
                if field in row:
                    cell_defects("%s.%s" % (label, field), row[field], defects)

    # tensions: factors is a dict of cells.
    for i, tension in enumerate(doc.get("tensions") or []):
        if not isinstance(tension, dict):
            continue
        factors = tension.get("factors")
        if isinstance(factors, dict):
            for field, val in factors.items():
                cell_defects("tensions[%d].factors.%s" % (i, field), val, defects)

    return defects


def schema_errors(doc):
    """Full JSON-Schema validation, returning ('schema: <path>: <msg>', ...) or (None, why) on setup failure."""
    schema, why = load_json(SCHEMA_PATH)
    if schema is None:
        return None, why
    try:
        import jsonschema  # noqa: F401
        from jsonschema import validators
    except ImportError:
        return None, "jsonschema is not importable -- schema validation cannot run"
    try:
        cls = validators.validator_for(schema)
        cls.check_schema(schema)
        validator = cls(schema)
    except Exception as exc:  # noqa: BLE001
        return None, "the schema is not a valid JSON Schema: %s" % str(exc)[:200]
    errs = sorted(validator.iter_errors(doc), key=lambda e: list(e.path))
    lines = ["schema: %s: %s" % ("/".join(str(p) for p in e.path) or "<root>", e.message[:200]) for e in errs]
    return lines, None


def check(path):
    doc, why = load_json(path)
    if doc is None:
        print("FAIL: %s" % why)
        return 1
    defects = walk_contract(doc)
    sch_lines, sch_why = schema_errors(doc)
    if sch_lines is None:
        defects.append("schema: could not validate (%s)" % sch_why)
    else:
        defects.extend(sch_lines)
    if not defects:
        print("ACCEPT lgctfm-contract: %s" % path)
        print("VERDICT: 1 ACCEPT | 0 HAND BACK | 0 UNCHECKED")
        return 0
    print("HAND BACK lgctfm-contract: %s" % path)
    for line in defects:
        print("  %s" % line)
    print("VERDICT: 0 ACCEPT | 1 HAND BACK | 0 UNCHECKED")
    return 1


if __name__ == "__main__":
    argv = sys.argv[1:]
    if not argv:
        print(__doc__)
        sys.exit(2)
    sys.exit(check(argv[0]))

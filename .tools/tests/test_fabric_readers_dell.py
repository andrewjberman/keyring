#!/usr/bin/env python
"""NFRA_CTLPLN.TO-CT-d-6 (AMENDMENT 1): the two fabric readers handle a Dell.

ID arm (9): the surprise-row gate's id-to-fabric derivation (`_fabric_of_id` / `_fabric_identity_violations` in
.tools/surprise-row-gate.py) run against a TEMPORARY COPY of the device register (OPAL_DEVICE_REGISTER), eight id cases
and one case with the register path pointing nowhere:
  bare -> laptop | Z- -> site-z | D1- -> dell1 | D2- -> dell2 | D1-W3-S2 -> dell1 | -D3- -> refused (unregistered
  coordinate) | a D1- id whose row says dell2 -> refused | a bare id whose row says dell1 -> refused | no register -> refused.
Row-schema arm (8): whole row objects through the gate's OWN schema limb (`_check_row`, which runs the Draft-07 validator and the
closed-enum walk) against the two row schemas in org/surprise_channel/schemas/: investigation D1/dell1, D2-W3/dell2, Z/site-z,
bare/laptop and W9/laptop admitted; fabric dell3 refused; a lower-case coordinate id refused; a remediation row with a D1- id
admitted. A verdict reads only the complaints the schema limb raises (schema violation / ratified enum), because the gate's other
limbs (register agreement, owner, worker suffix) are graded by the id arm and by the gate's own --self-test.
Schema arm (5): one PRD header instance per fabric value validated against org/standards/PRD_HEADER.schema.json
(4 admitted) and one with dell3 (refused). Enum arm: the schema's fabric enum equals FABRIC_ENUM read from the source of
.tools/to-pipeline-gate.py. Gate arm: `python .tools/surprise-row-gate.py --self-test` result line.

LAST line: FABRIC-READERS ids_ok=<a>/9 schema_ok=<b>/5 rowschema_ok=<c>/8 enum_equal=<True|False> gate_selftest=<ok|fail> ok=<True|False>
"""
import ast
import importlib.util
import json
import os
import re
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GATE = os.path.join(ROOT, ".tools", "surprise-row-gate.py")
TOGATE = os.path.join(ROOT, ".tools", "to-pipeline-gate.py")
REGISTER = os.path.join(ROOT, "org", "devices", "DEVICES.json")
SCHEMA = os.path.join(ROOT, "org", "standards", "PRD_HEADER.schema.json")
ROW_SCHEMAS = os.path.join(ROOT, "org", "surprise_channel", "schemas")


def load_gate():
    spec = importlib.util.spec_from_file_location("surprise_row_gate_under_test", GATE)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["surprise_row_gate_under_test"] = mod
    spec.loader.exec_module(mod)
    return mod


def enum_from_source():
    with open(TOGATE, encoding="utf-8") as fh:
        m = re.search(r"^FABRIC_ENUM\s*=\s*(\(.*?\))\s*$", fh.read(), re.M)
    return list(ast.literal_eval(m.group(1))) if m else None


def id_cases(gate, enum, reg_copy, missing):
    """(label, ok, detail) per case; the register is the temporary copy unless the case says otherwise."""
    results = []
    os.environ["OPAL_DEVICE_REGISTER"] = reg_copy
    dev = gate._fabric_of_id("X_PRJ-S1")[1]
    to_box = {f: dev.resolve(f) for f in enum}
    box_of = {v: k for k, v in to_box.items()}   # box name -> fabric value, from the enum + the register

    def derives(rid, want):
        box, _d, _r, why = gate._fabric_of_id(rid)
        fab = box_of.get(box)
        ok = fab == want and gate._fabric_identity_violations(rid, want) == []
        results.append(("%s -> %s" % (rid, want), ok, "got %r %s" % (fab, why)))

    def refused(label, rid, fabric, needles):
        v = gate._fabric_identity_violations(rid, fabric)
        ok = bool(v) and all(n in v[0] for n in needles)
        results.append((label, ok, (v[0][:200] if v else "ADMITTED")))

    derives("X_PRJ-S1", "laptop")
    derives("X_PRJ-Z-S1", "site-z")
    derives("X_PRJ-D1-S1", "dell1")
    derives("X_PRJ-D2-S1", "dell2")
    derives("X_PRJ-D1-W3-S2", "dell1")
    refused("X_PRJ-D3-S1 (unregistered coordinate) refused", "X_PRJ-D3-S1", "dell1", ["'D3'", "'D1'", "'D2'", "'Z'"])
    refused("X_PRJ-D1-S1 with fabric dell2 refused", "X_PRJ-D1-S1", "dell2", ["dell1", "dell2"])
    refused("bare X_PRJ-S1 with fabric dell1 refused, names the id form", "X_PRJ-S1", "dell1",
            ["<CODE>-D1-S<n>", "laptop", "site-z", "dell1", "dell2"])
    os.environ["OPAL_DEVICE_REGISTER"] = missing
    refused("register path pointing nowhere refused loudly", "X_PRJ-S1", "laptop", ["REFUSED", "cannot be read"])
    return results


def schema_cases(enum):
    import jsonschema
    with open(SCHEMA, encoding="utf-8") as fh:
        schema = json.load(fh)
    base = {"project": "X_PRJ", "directive": "D0", "prd_version": "v0.1", "step": 4,
            "brief_ref": "docs/briefs/x.md@a77b65337e", "endpoint_outcomes": ["FWD-1"], "status": "DRAFT"}
    out = []
    for fab, expect in [(f, True) for f in enum] + [("dell3", False)]:
        errs = [e.message[:80] for e in jsonschema.Draft7Validator(schema).iter_errors(dict(base, fabric=fab))]
        good = (not errs) if expect else (len(errs) == 1 and "is not one of" in errs[0])   # a refusal must be the fabric alone
        out.append(("PRD header fabric=%s" % fab, good, "ADMITTED" if not errs else "REFUSED " + errs[0]))
    return out, schema["properties"]["fabric"]["enum"]


def rowschema_cases(gate):
    """Eight whole-row cases through gate._check_row; only the schema limb's complaints decide each verdict."""
    def load(name):
        with open(os.path.join(ROW_SCHEMAS, name), encoding="utf-8") as fh:
            return json.load(fh)
    inv, rem = load("investigation_item.schema.json"), load("remediation_row.schema.json")

    def inv_row(rid, fabric):
        return {"id": rid, "project": "X_PRJ", "fabric": fabric, "surfaced_by": "0.9.0_WK_X_PRJ~3",
                "surfaced_at": "2026-10-07T09:30:00Z", "one_line": "a well-formed test row for the schema arm",
                "class": "OBSERVATION", "hazard_standing": "INERT", "grounding": {"status": "INFERRED", "evidence": ["test evidence line"]},
                "disposition": "UNDER_INVESTIGATION", "spec_asserts": "the spec asserts a thing", "world_is": "the world is another thing"}

    def rem_row(rid, fabric):
        return {"id": rid, "project": "X_PRJ", "fabric": fabric, "class": "OBSERVATION", "hazard_standing": "INERT",
                "mechanism": "a well-formed test mechanism", "evidence": ["test evidence line"], "remedy": "a test remedy",
                "owner": "1.0.0_SA_CTO", "round": "v1", "remediation": {"state": "OPEN", "owner": "1.0.0_SA_CTO", "round": "v1"}}

    def schema_complaints(row, kind, schema):
        out = gate._check_row(row, kind, schema)
        return [c for c in out if "schema violation" in c or "ratified enum" in c]

    out = []
    for label, row, kind, schema, admit, where in [
        ("investigation X_PRJ-D1-S1 / dell1", inv_row("X_PRJ-D1-S1", "dell1"), "INVESTIGATION", inv, True, None),
        ("investigation X_PRJ-D2-W3-S2 / dell2", inv_row("X_PRJ-D2-W3-S2", "dell2"), "INVESTIGATION", inv, True, None),
        ("investigation X_PRJ-Z-S4 / site-z", inv_row("X_PRJ-Z-S4", "site-z"), "INVESTIGATION", inv, True, None),
        ("investigation X_PRJ-S5 / laptop", inv_row("X_PRJ-S5", "laptop"), "INVESTIGATION", inv, True, None),
        ("investigation X_PRJ-W9-S1 / laptop (worker form)", inv_row("X_PRJ-W9-S1", "laptop"), "INVESTIGATION", inv, True, None),
        ("investigation fabric dell3 refused", inv_row("X_PRJ-D1-S1", "dell3"), "INVESTIGATION", inv, False, "fabric"),
        ("investigation X_PRJ-d1-S1 (lower case) refused", inv_row("X_PRJ-d1-S1", "dell1"), "INVESTIGATION", inv, False, "id"),
        ("remediation X_PRJ-D1-S1 / dell1", rem_row("X_PRJ-D1-S1", "dell1"), "REMEDIATION", rem, True, None),
    ]:
        got = schema_complaints(row, kind, schema)
        if admit:
            good = not got
        else:   # a refusal must be the named field alone: a refusal for some other reason proves nothing
            good = bool(got) and all(("/" + where) in c or ("%s=" % where) in c for c in got)
        out.append((label, good, "ADMITTED" if not got else "REFUSED " + got[0][:150]))
    return out


def main():
    gate = load_gate()
    enum = enum_from_source()
    print("to-pipeline-gate FABRIC_ENUM (from source) = %r" % (enum,))
    with open(REGISTER, encoding="utf-8") as fh:
        reg = json.load(fh)
    with tempfile.TemporaryDirectory() as tmp:
        copy = os.path.join(tmp, "DEVICES.json")
        with open(copy, "w", encoding="utf-8") as fh:
            json.dump(reg, fh)
        ids = id_cases(gate, enum, copy, os.path.join(tmp, "no-such-register.json"))
    os.environ.pop("OPAL_DEVICE_REGISTER", None)
    for label, ok, detail in ids:
        print("%s  id: %s | %s" % ("PASS" if ok else "FAIL", label, detail))
    sch, sch_enum = schema_cases(enum)
    for label, ok, detail in sch:
        print("%s  schema: %s | %s" % ("PASS" if ok else "FAIL", label, detail))
    rows = rowschema_cases(gate)
    for label, ok, detail in rows:
        print("%s  rowschema: %s | %s" % ("PASS" if ok else "FAIL", label, detail))
    enum_equal = enum is not None and sch_enum == enum
    print("schema enum %r == FABRIC_ENUM %r -> %s" % (sch_enum, enum, enum_equal))
    cp = subprocess.run([sys.executable, GATE, "--self-test"], cwd=ROOT, capture_output=True, text=True, timeout=110,
                        encoding="utf-8", errors="replace")
    line = [ln for ln in (cp.stdout + cp.stderr).splitlines() if ln.startswith("RESULT:")]
    selftest = "ok" if cp.returncode == 0 and line else "fail"
    print("surprise-row-gate --self-test -> %s | rc=%d %s" % (selftest, cp.returncode, line[-1] if line else "(no result line)"))
    a = sum(1 for _l, ok, _d in ids if ok)
    b = sum(1 for _l, ok, _d in sch if ok)
    c = sum(1 for _l, ok, _d in rows if ok)
    ok = a == 9 and b == 5 and c == 8 and enum_equal and selftest == "ok"
    print("FABRIC-READERS ids_ok=%d/9 schema_ok=%d/5 rowschema_ok=%d/8 enum_equal=%s gate_selftest=%s ok=%s"
          % (a, b, c, enum_equal, selftest, ok))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

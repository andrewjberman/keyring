"""Controls for to-pipeline-gate.py LIMB 5 -- step-4 PRD conformance (Andrew-direct 2026-09-02,
/open-calls CALL 2, "All recs approved": ONE limb on the EXISTING step-6 gate, never a second gate).

The core (_prd_conformance) is pure, so these run on text with no git. The positive control is the
REAL ETFS_GUARDRAIL PRD, which also proves the FWD-9 QUOTATION in its ENDPOINT section does not
trip the definitions check. GATE_PATH points the harness at a copy of an older gate for red-first.
"""
import importlib.util
import json
import os
import re
import sys

GATE_PATH = os.environ.get("GATE_PATH", ".tools/to-pipeline-gate.py")
_spec = importlib.util.spec_from_file_location("togate", GATE_PATH)
gate = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(gate)

PRD = "docs/architecture/ETFS_GUARDRAIL_PRD.md"
SCHEMA = json.load(open("org/standards/PRD_HEADER.schema.json", encoding="utf-8"))
EXPECT = {"project": "ETFS_GUARDRAIL", "directive": "D8", "fabric": "laptop"}


def _line(ok, got, expect, name):
    print("  %-7s %-6s->%-6s  %s" % ("OK" if ok else "DEFECT", got, expect, name))


def _header(text):
    m = re.search(r"```json\s*(.*?)```", text, re.S)
    return json.loads(m.group(1)), m


def _with_header(text, new_header):
    _, m = _header(text)
    return text[:m.start(1)] + json.dumps(new_header, indent=1) + text[m.end(1):]


def run():
    if not hasattr(gate, "_prd_conformance"):
        print("  DEFECT  gate has no _prd_conformance -- limb 5 absent (step-4 shape unchecked)")
        return 8
    base = open(PRD, encoding="utf-8").read()
    hdr, _ = _header(base)
    assert "FWD-9" in base, "control precondition: the PRD must still contain the FWD-9 quotation"

    cases = [
        ("positive: the real ETFS_GUARDRAIL PRD (must PASS; FWD-9 quotation must NOT trip)", base, EXPECT, "PASS"),
        ("no PRD_HEADER block", re.sub(r"```json.*?```", "", base, count=1, flags=re.S), EXPECT, "REFUSE"),
        ("header.project mismatches the register row", base, dict(EXPECT, project="WRONG"), "REFUSE"),
        ("header.fabric mismatches the register row", base, dict(EXPECT, fabric="site-z"), "REFUSE"),
        ("no SURFACE MANIFEST section", base.replace("## 7. SURFACE MANIFEST", "## 7. SOMETHING ELSE"), EXPECT, "REFUSE"),
        ("header omits a DEFINED outcome (FWD-8)", _with_header(base, dict(hdr, endpoint_outcomes=hdr["endpoint_outcomes"][:-1])), EXPECT, "REFUSE"),
        ("header lists a PHANTOM outcome (FWD-9, mentioned only)", _with_header(base, dict(hdr, endpoint_outcomes=hdr["endpoint_outcomes"] + ["FWD-9"])), EXPECT, "REFUSE"),
        ("a possessive mention at LINE START ('FWD-7's message') is not a definition (must PASS)",
         base.replace("## ENDPOINT (step 2, `/endpoint --forward`)", "## ENDPOINT (step 2, `/endpoint --forward`)\nFWD-7's message carries the report content.", 1), EXPECT, "PASS"),
        ("header schema violation: step=5", _with_header(base, dict(hdr, step=5)), EXPECT, "REFUSE"),
    ]
    fails = 0
    for name, text, expect, want in cases:
        v = gate._prd_conformance(text, SCHEMA, expect)
        got = "PASS" if not v else "REFUSE"
        ok = got == want
        fails += int(not ok)
        _line(ok, got, want, name)
        if not ok and v:
            print("           first: %s" % v[0][:110])
    return fails


if __name__ == "__main__":
    print("== gate under test: %s ==" % GATE_PATH)
    n = run()
    print("DEFECTS: %d" % n)
    sys.exit(1 if n else 0)

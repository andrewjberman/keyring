"""Controls for to-pipeline-gate.py LIMB 5 -- step-4 PRD conformance (Andrew-direct 2026-09-02,
/open-calls CALL 2, "All recs approved": ONE limb on the EXISTING step-6 gate, never a second gate).

The core (_prd_conformance) is pure, so those run on text with no git. The positive control is the
REAL ETFS_GUARDRAIL PRD, which also proves the FWD-9 QUOTATION in its ENDPOINT section does not trip
the definitions check. The wrapper control monkeypatches _staged_blob so staged-vs-worktree can be
exercised without staging anything. GATE_PATH points the harness at a copy of an older gate for
red-first.

CVO~A re-grade @d019922d68 added: empty manifest heading; manifest heading only inside a fence;
staged project JSON disagreeing with the worktree; and the possessive case now ASSERTS its injection
landed (the first cut replaced a heading string that no longer existed and injected nothing).
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
ENDPOINT_TITLE = "## ENDPOINT (step 2, /endpoint --forward)"


def _line(ok, got, expect, name):
    print("  %-7s %-6s->%-6s  %s" % ("OK" if ok else "DEFECT", got, expect, name))


def _header(text):
    m = re.search(r"```json\s*(.*?)```", text, re.S)
    return json.loads(m.group(1)), m


def _with_header(text, new_header):
    _, m = _header(text)
    return text[:m.start(1)] + json.dumps(new_header, indent=1) + text[m.end(1):]


def _inject_after_endpoint(text, line):
    assert ENDPOINT_TITLE in text, "control precondition: the exact ENDPOINT title must be present"
    out = text.replace(ENDPOINT_TITLE, ENDPOINT_TITLE + "\n" + line, 1)
    assert line in out and out != text, "injection did not land"
    return out


def _empty_manifest(text):
    """Keep the heading, drop the section body up to the next top-level heading."""
    m = re.search(r"^## .*SURFACE MANIFEST.*$", text, re.M)
    assert m, "precondition: manifest heading present"
    nxt = text.find("\n## ", m.end())
    return text[:m.end()] + "\n\n" + (text[nxt:] if nxt != -1 else "")


def _fenced_manifest_only(text):
    """Remove the real manifest section; leave a heading-shaped line only inside a code fence."""
    t = _empty_manifest(text)
    t = re.sub(r"^## .*SURFACE MANIFEST.*$", "## 7. Something else", t, count=1, flags=re.M)
    return t + "\n\n```\n## 7. SURFACE MANIFEST (fenced, must not count)\n| S1 | FWD-1 | x |\n```\n"


def run_core():
    if not hasattr(gate, "_prd_conformance"):
        print("  DEFECT  gate has no _prd_conformance -- limb 5 absent (step-4 shape unchecked)")
        return 12
    base = open(PRD, encoding="utf-8").read()
    hdr, _ = _header(base)
    assert "FWD-9" in base, "control precondition: the PRD must still contain the FWD-9 quotation"
    cases = [
        ("positive: the real ETFS_GUARDRAIL PRD (must PASS; FWD-9 quotation must NOT trip)", base, EXPECT, "PASS"),
        ("no PRD_HEADER block", re.sub(r"```json.*?```", "", base, count=1, flags=re.S), EXPECT, "REFUSE"),
        ("header.project mismatches the register row", base, dict(EXPECT, project="WRONG"), "REFUSE"),
        ("header.fabric mismatches the register row", base, dict(EXPECT, fabric="site-z"), "REFUSE"),
        ("no SURFACE MANIFEST section at all", base.replace("## 7. SURFACE MANIFEST", "## 7. SOMETHING ELSE"), EXPECT, "REFUSE"),
        ("SURFACE MANIFEST heading present but section EMPTY", _empty_manifest(base), EXPECT, "REFUSE"),
        ("SURFACE MANIFEST heading only inside a code fence", _fenced_manifest_only(base), EXPECT, "REFUSE"),
        ("header omits a DEFINED outcome (FWD-8)", _with_header(base, dict(hdr, endpoint_outcomes=hdr["endpoint_outcomes"][:-1])), EXPECT, "REFUSE"),
        ("header lists a PHANTOM outcome (FWD-9, mentioned only)", _with_header(base, dict(hdr, endpoint_outcomes=hdr["endpoint_outcomes"] + ["FWD-9"])), EXPECT, "REFUSE"),
        ("a possessive at LINE START ('FWD-7's message') is not a definition (must PASS; injection asserted)",
         _inject_after_endpoint(base, "FWD-7's message carries the report content."), EXPECT, "PASS"),
        ("a real extra definition injected at line start IS counted (must REFUSE: phantom vs header)",
         _inject_after_endpoint(base, "  FWD-9  An injected ninth outcome the header does not list"), EXPECT, "REFUSE"),
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


def run_wrapper():
    """Staged-vs-worktree on the PROJECT JSON, without staging anything: monkeypatch _staged_blob."""
    if not hasattr(gate, "check_prd_conformance"):
        print("  DEFECT  gate has no check_prd_conformance wrapper")
        return 2
    root = os.path.abspath(".")
    rel = "org/projects/ETFS_GUARDRAIL/task_orders/ETFS_GUARDRAIL.TO-CTRL.synthetic.md"
    real = gate._staged_blob
    fails = 0
    try:
        v, n = gate.check_prd_conformance(root, rel)
        ok = not v and n and "graded 1" in n[0]
        _line(ok, "OK" if ok else "OTHER", "OK", "wrapper: real staged project row + real staged PRD -> graded 1, OK")
        fails += int(not ok)

        def patched(root_, rel_):
            txt = real(root_, rel_)
            if rel_.endswith("org/projects/ETFS_GUARDRAIL.json") and txt is not None:
                doc = json.loads(txt)
                doc["directive"] = "D9"          # staged says D9; the header (and worktree) say D8
                return json.dumps(doc)
            return txt
        gate._staged_blob = patched
        v, n = gate.check_prd_conformance(root, rel)
        ok = any("directive" in x and "D9" in x for x in v)
        _line(ok, "REFUSE" if v else "PASS", "REFUSE", "wrapper: STAGED project row says D9, header says D8 -> must REFUSE (index read, not worktree)")
        fails += int(not ok)
    finally:
        gate._staged_blob = real
    return fails


if __name__ == "__main__":
    print("== gate under test: %s ==" % GATE_PATH)
    print("== CORE ==")
    a = run_core()
    print("== WRAPPER ==")
    b = run_wrapper()
    print("DEFECTS: %d core + %d wrapper = %d" % (a, b, a + b))
    sys.exit(1 if a + b else 0)

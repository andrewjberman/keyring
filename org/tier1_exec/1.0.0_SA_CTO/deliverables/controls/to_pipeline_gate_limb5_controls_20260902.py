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
CVO~A re-grade @dddd96477d added: an ILLUSTRATIVE fenced ENDPOINT heading BEFORE the real one (the
template's own shape); a FULL INSTANTIATION of _PRD_TEMPLATE.md; and brief_ref traversal negatives.
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
TEMPLATE = "docs/architecture/_PRD_TEMPLATE.md"
SCHEMA_PATH = "org/standards/PRD_HEADER.schema.json"
SCHEMA = json.load(open(SCHEMA_PATH, encoding="utf-8"))
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
    m = re.search(r"^## .*SURFACE MANIFEST.*$", text, re.M)
    assert m, "precondition: manifest heading present"
    nxt = text.find("\n## ", m.end())
    return text[:m.end()] + "\n\n" + (text[nxt:] if nxt != -1 else "")


def _fenced_manifest_only(text):
    t = _empty_manifest(text)
    t = re.sub(r"^## .*SURFACE MANIFEST.*$", "## 7. Something else", t, count=1, flags=re.M)
    return t + "\n\n```\n## 7. SURFACE MANIFEST (fenced, must not count)\n| S1 | FWD-1 | x |\n```\n"


def _fenced_illustrative_endpoint_first(text):
    """The template's own shape: an illustrative ENDPOINT title INSIDE a fence, BEFORE the real one."""
    _, m = _header(text)
    decoy = "\n\n```\n" + ENDPOINT_TITLE + "\n  FWD-99  a decoy definition inside a fence\n```\n"
    out = text[:m.end()] + decoy + text[m.end():]
    assert out.count(ENDPOINT_TITLE) == 2
    return out


def _instantiate_template():
    """Fill _PRD_TEMPLATE.md's placeholders with ETFS_GUARDRAIL values; the result must pass limb 5."""
    t = open(TEMPLATE, encoding="utf-8").read()
    hdr = {"project": "ETFS_GUARDRAIL", "directive": "D8", "fabric": "laptop", "prd_version": "v0.1", "step": 4,
           "brief_ref": "docs/briefs/ETFS_COVERAGE_GUARDRAIL_BUILD_SPEC_20260901.md@1890d7785c",
           "endpoint_outcomes": ["FWD-1", "FWD-2"], "status": "DRAFT"}
    # The skeleton's header block is the LAST fenced json in the file (the rules preamble has none
    # of shape 'project'); replace the one that follows the '# {PROJECT_CODE}' H1.
    h1 = t.index("# {PROJECT_CODE}")
    m = re.compile(r"```json\s*(.*?)```", re.S).search(t, h1)
    t = t[:m.start(1)] + json.dumps(hdr, indent=1) + t[m.end(1):]
    # Give the skeleton's ENDPOINT section two real definitions in card form.
    cards = ("\n```\n  FWD-1  A first outcome\n         DONE WHEN  APPLIED\n         ACCEPT     x\n         SOURCE     brief s.1\n\n"
             "  FWD-2  A second outcome\n         DONE WHEN  EXERCISED\n         ACCEPT     y\n         SOURCE     brief s.2\n```\n")
    real_ep = t.rindex(ENDPOINT_TITLE)
    t = t[:real_ep + len(ENDPOINT_TITLE)] + cards + t[real_ep + len(ENDPOINT_TITLE):]
    return t


def run_core():
    if not hasattr(gate, "_prd_conformance"):
        print("  DEFECT  gate has no _prd_conformance -- limb 5 absent (step-4 shape unchecked)")
        return 14
    base = open(PRD, encoding="utf-8").read()
    hdr, _ = _header(base)
    assert "FWD-9" in base, "control precondition: the PRD must still contain the FWD-9 quotation"
    cases = [
        ("positive: the real ETFS_GUARDRAIL PRD (must PASS; FWD-9 quotation must NOT trip)", base, EXPECT, "PASS"),
        ("positive: ILLUSTRATIVE fenced ENDPOINT title BEFORE the real one (template shape) -- must PASS, decoy FWD-99 ignored",
         _fenced_illustrative_endpoint_first(base), EXPECT, "PASS"),
        ("positive: FULL INSTANTIATION of _PRD_TEMPLATE.md -- must PASS limb 5 by construction",
         _instantiate_template(), EXPECT, "PASS"),
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


def run_schema():
    """brief_ref: two admitted shapes, vintage required, NO traversal or cross-segment matches."""
    pat = re.compile(SCHEMA["properties"]["brief_ref"]["pattern"])
    cases = [
        ("POS docs/briefs", "docs/briefs/ETFS_COVERAGE_GUARDRAIL_BUILD_SPEC_20260901.md@1890d7785c", True),
        ("POS docs/briefs nested subdir", "docs/briefs/sub/x.md@1890d7785c", True),
        ("POS ANDREW_DIRECT record", "org/tier1_exec/3.0.0_SA_CVO/deliverables/ANDREW_DIRECT_20260902_1715Z_COMPTOOL_EFFICACY_PROJECT.md@f90ab3936b", True),
        ("NEG no vintage", "docs/briefs/x.md", False),
        ("NEG non-ANDREW_DIRECT deliverable", "org/tier1_exec/1.0.0_SA_CTO/deliverables/FINDING_X.md@abcdef1", False),
        ("NEG random path", "README.md@abcdef1", False),
        ("NEG short vintage", "docs/briefs/x.md@abc", False),
        ("NEG dot-traversal out of docs/briefs", "docs/briefs/../architecture/_PRD_TEMPLATE.md@abcdef0", False),
        ("NEG cross-segment ANDREW_DIRECT", "org/tier1_exec/X/deliverables/ANDREW_DIRECT_x/../../OTHER.md@abcdef0", False),
        ("NEG single-dot segment", "docs/briefs/./x.md@abcdef0", False),
    ]
    fails = 0
    for name, val, want in cases:
        got = bool(pat.match(val))
        ok = got == want
        fails += int(not ok)
        _line(ok, "ACCEPT" if got else "REFUSE", "ACCEPT" if want else "REFUSE", "brief_ref: " + name)
    return fails


def run_wrapper():
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
                doc["directive"] = "D9"
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
    print("== SCHEMA (brief_ref) ==")
    s = run_schema()
    print("== WRAPPER ==")
    b = run_wrapper()
    print("DEFECTS: %d core + %d schema + %d wrapper = %d" % (a, s, b, a + s + b))
    sys.exit(1 if a + s + b else 0)

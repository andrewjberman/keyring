#!/usr/bin/env python3
"""CT-ac-7 (NFRA_CTLPLN-D2-S5) -- the bound governing order's judgment="true" criteria are EXPECTED by proof-of-spec-check.

Subject: .tools/proof-of-spec-check.py coverage_check() with bound_judgment_ids() (the --governing-order binding).
Pairs with the self-test arms CT-ac-7 a-d; these four cases run the checker through its command line.

The checker resolves a bound order only under its OWN tree, so this test copies the checker and the schema it reads
into a temporary tree, writes a temporary bound order and per-case instances there, and runs the copy as a
subprocess. Nothing is written under the repository. Only the coverage limb is graded here: violation lines from the
other limbs are ignored by their prefix, so a schema or alignment line cannot change a coverage verdict.

CASES (the order carries AC1 (mechanical) and J1 (judgment="true"); expected set "AC1"):
  a  BOUND, instance carries AC1 and J1        -> 0 coverage violations; the NOTE names J1
  b  BOUND, instance carries AC1 only          -> 1 coverage violation: silent omission of J1; rc 1
  c  UNBOUND, instance carries AC1 and J1      -> 1 coverage violation: unexpected addition of J1; rc 1; no NOTE
  d  BOUND, instance carries AC1, J1 and X9    -> 1 coverage violation: unexpected addition of X9 only; NOTE names J1

Run: python .tools/tests/test_proof_judgment_expected.py
Prints: PROOF-JUDGMENT-EXPECTED cases=<k>/<n> ok=<True|False>
Exit 0 = every case as expected. Exit 1 otherwise.
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent
REPO = TOOLS.parent
CHECKER = TOOLS / "proof-of-spec-check.py"
SCHEMA = REPO / "org" / "standards" / "PROOF_OF_SPEC.schema.json"
ORDER_REL = "org/missions/D9/NFRA/NFRA_TESTPROJ/task-orders/NFRA_TESTPROJ.TO-X-1.md"
TO_ID = "NFRA_TESTPROJ.TO-X-1"
NOTE_HEAD = "NOTE: bound governing order's judgment criteria admitted"
COV_HEAD = "VIOLATION: coverage: "

ORDER_TEXT = (
    "<to_id>" + TO_ID + "</to_id>\n"
    "<status>pending</status>\n"
    '<criterion id="AC1" cell_refs="FIX-a-1"><invocation>echo ok</invocation><expect>ok</expect></criterion>\n'
    '<criterion id="J1" cell_refs="FIX-a-1" judgment="true"/>\n'
)

ROWS = {
    "AC1": {"criterion_id": "AC1", "criterion_verbatim": "the deciding line is printed", "method": "command",
            "invocation": "echo ok", "output_evidence": "ok", "denominator": "1 of 1", "status": "PASS"},
    "J1": {"criterion_id": "J1", "criterion_verbatim": "the judgment criterion", "method": "judgment",
           "status": "UNVERIFIABLE-BY-INSTRUMENT",
           "status_reason": "judgment criterion; graded by 3.0.0_SA_CVO at L9"},
    "X9": {"criterion_id": "X9", "criterion_verbatim": "a stray row", "method": "command",
           "invocation": "echo x", "output_evidence": "x", "denominator": "1 of 1", "status": "PASS"},
}


def _run_case(name: str, tree: Path, case_dir: Path, carried: list, bound: bool, expect: dict) -> tuple:
    """Write the instance under case_dir, run the copied checker under tree, grade the coverage lines.
    Returns (ok, one-line detail)."""
    inst = {"to_id": TO_ID, "acceptance": [ROWS[c] for c in carried]}
    inst_path = case_dir / "instance.json"
    inst_path.write_text(json.dumps(inst, indent=1), encoding="utf-8", newline="\n")
    cmd = [sys.executable, str(tree / ".tools" / "proof-of-spec-check.py"), str(inst_path), "AC1"]
    if bound:
        cmd += ["--governing-order", ORDER_REL]
    proc = subprocess.run(cmd, cwd=str(tree), capture_output=True, text=True, encoding="utf-8",
                          errors="replace", timeout=120)
    lines = (proc.stdout or "").splitlines()
    cov = [ln for ln in lines if ln.strip().startswith(COV_HEAD)]
    note = [ln for ln in lines if ln.startswith(NOTE_HEAD)]
    problems = []
    if len(cov) != expect["cov_n"]:
        problems.append("coverage violations=%d expected=%d" % (len(cov), expect["cov_n"]))
    for needle in expect.get("cov_has", ()):
        if not any(needle in ln for ln in cov):
            problems.append("no coverage line carries %r" % needle)
    for needle in expect.get("cov_lacks", ()):
        if any(needle in ln for ln in cov):
            problems.append("a coverage line carries %r but must not" % needle)
    if expect.get("note") and not any(expect["note"] in ln for ln in note):
        problems.append("no NOTE line names %r" % expect["note"])
    if expect.get("no_note") and note:
        problems.append("a NOTE line was printed but the run is UNBOUND")
    if expect.get("rc") is not None and proc.returncode != expect["rc"]:
        problems.append("rc=%d expected=%d" % (proc.returncode, expect["rc"]))
    detail = "%s | rc=%d coverage=%d note=%d" % (name, proc.returncode, len(cov), len(note))
    if cov:
        detail += " | first: " + cov[0].strip()[:100]
    if problems:
        detail += " | PROBLEMS: " + "; ".join(problems)
    return (not problems), detail


def main() -> int:
    cases = [
        ("a BOUND, AC1 and J1 carried", ["AC1", "J1"], True,
         {"cov_n": 0, "note": "J1", "cov_lacks": ("J1",)}),
        ("b BOUND, J1 absent", ["AC1"], True,
         {"cov_n": 1, "rc": 1, "cov_has": ("silent omission", "'J1'"), "cov_lacks": ("unexpected",)}),
        ("c UNBOUND, J1 carried", ["AC1", "J1"], False,
         {"cov_n": 1, "rc": 1, "cov_has": ("unexpected addition", "'J1'"), "no_note": True}),
        ("d BOUND, X9 stray beside J1", ["AC1", "J1", "X9"], True,
         {"cov_n": 1, "rc": 1, "cov_has": ("unexpected addition", "'X9'"), "cov_lacks": ("'J1'",), "note": "J1"}),
    ]
    tmp = Path(tempfile.mkdtemp(prefix="ct_ac7_judgment_"))
    results = []
    try:
        tree = tmp / "tree"
        (tree / ".tools").mkdir(parents=True)
        (tree / "org" / "standards").mkdir(parents=True)
        shutil.copyfile(str(CHECKER), str(tree / ".tools" / "proof-of-spec-check.py"))
        shutil.copyfile(str(SCHEMA), str(tree / "org" / "standards" / "PROOF_OF_SPEC.schema.json"))
        order_path = tree / ORDER_REL
        order_path.parent.mkdir(parents=True)
        order_path.write_text(ORDER_TEXT, encoding="utf-8", newline="\n")
        for idx, (name, carried, bound, expect) in enumerate(cases):
            case_dir = tmp / ("case%d" % idx)
            case_dir.mkdir()
            ok, detail = _run_case(name, tree, case_dir, carried, bound, expect)
            results.append(ok)
            print("  %s  %s" % ("PASS" if ok else "FAIL", detail))
    finally:
        shutil.rmtree(str(tmp), ignore_errors=True)
    k = sum(1 for r in results if r)
    n = len(cases)
    print("PROOF-JUDGMENT-EXPECTED cases=%d/%d ok=%s" % (k, n, k == n))
    return 0 if k == n else 1


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""PIPELINE GATE LAYER 2 -- the battery for to-decomp-ref-lint.

Subject: `.tools/to-decomp-ref-lint.py`, built 2026-08-24 by `0.8.0_AE_CloudComp~F` per
org/ref/DIRECTIVE_EXECUTION_PIPELINE.md:171 (build routed; Andrew's word granted in the
ratification).

    A GATE THAT REFUSES EVERYTHING IS NOT A GATE, AND NEITHER IS ONE THAT REFUSES NOTHING.

So the arms are deliberately paired: for every REFUSAL arm there is a control that must
PASS for a DIFFERENT reason (out of scope by project, by path, by newness, by ramp). The
packet's acceptance is "exercised both ways: a pipeline-registered TO without
<decomp_ref> REFUSED; a non-pipeline TO passes; the refusal names the rule" -- the third
clause is tested too, because a refusal that does not teach is just a wall.

The fixtures are SEALED into a temp workspace: the live estate's project registrations
change under this gate, and a battery that reads them would report on the estate rather
than on the gate.

Run: python .tools/tests/test_to_decomp_ref_lint.py
Exit 0 = all arms as expected. Exit 1 = at least one arm did not.
"""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent
LINT_SRC = TOOLS / "to-decomp-ref-lint.py"

PASS, FAIL = "PASS", "FAIL"
results: list[tuple[str, str, str]] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    results.append((name, PASS if ok else FAIL, detail))


TO_WITH_REF = """# TO {code}.TO-1
<task_order id="{code}.TO-1" project="{code}">
<decomp_ref>workflows/runs/fixture/DECOMP.md -- cells FIX-a-1, FIX-a-2</decomp_ref>
<status>ACTIVE</status>
</task_order>
"""

TO_NO_REF = """# TO {code}.TO-1
<task_order id="{code}.TO-1" project="{code}">
<status>ACTIVE</status>
</task_order>
"""

TO_REF_NO_CELLS = """# TO {code}.TO-1
<task_order id="{code}.TO-1" project="{code}">
<decomp_ref>workflows/runs/fixture/DECOMP.md</decomp_ref>
<status>ACTIVE</status>
</task_order>
"""


def _ws(tmp: Path, *, code: str, registered: bool, body: str,
        subdir: str = "org/tier2_senior/0.8.0_AE_CloudComp/task_orders") -> tuple[Path, str]:
    """Plant a sealed workspace containing a copy of the lint and one TO."""
    (tmp / ".tools").mkdir(parents=True, exist_ok=True)
    (tmp / ".tools" / "to-decomp-ref-lint.py").write_text(
        LINT_SRC.read_text(encoding="utf-8"), encoding="utf-8")
    (tmp / "org" / "projects").mkdir(parents=True, exist_ok=True)
    proj = {"code": code, "status": "active"}
    if registered:
        proj["dep_stage"] = "DECOMP"
    (tmp / "org" / "projects" / f"{code}.json").write_text(
        json.dumps(proj), encoding="utf-8")
    d = tmp / subdir
    d.mkdir(parents=True, exist_ok=True)
    rel = f"{subdir}/{code}.TO-1.fixture.md"
    (tmp / rel).write_text(body.format(code=code), encoding="utf-8")
    return tmp, rel


def _run(tmp: Path, rel: str, *extra: str) -> tuple[int, str]:
    r = subprocess.run(
        [sys.executable, str(tmp / ".tools" / "to-decomp-ref-lint.py"), *extra, rel],
        cwd=tmp, capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr


def main() -> int:
    # ---- ARM 1: REFUSAL -- pipeline-registered, no <decomp_ref> ----
    with tempfile.TemporaryDirectory() as d:
        tmp, rel = _ws(Path(d), code="FIXPIPE", registered=True, body=TO_NO_REF)
        rc, out = _run(tmp, rel, "--enforce")
        check("registered + no decomp_ref -> rc=1", rc == 1, out[:200])
        check("refusal names the RULE (the ref requirement)",
              "must carry <decomp_ref>" in out, out[:200])
        check("refusal names the FIX", "FIX:" in out, out[:200])
        check("refusal names the WHY (choke-point citation)",
              "CANONICAL_FABRIC_WORKFLOW_20260901.md L5/L6" in out, out[:200])
        check("refusal does NOT invite a silent shortcut",
              "PIPELINE FAILURE TO SURFACE" in out, out[:200])

    # ---- ARM 2: CONTROL -- pipeline-registered WITH <decomp_ref> ----
    with tempfile.TemporaryDirectory() as d:
        tmp, rel = _ws(Path(d), code="FIXPIPE", registered=True, body=TO_WITH_REF)
        rc, out = _run(tmp, rel, "--enforce")
        check("registered + decomp_ref -> rc=0", rc == 0, out[:200])
        check("conformant reports findings=0", "findings=0" in out, out[:200])

    # ---- ARM 3: CONTROL -- NOT pipeline-registered, no ref -> out of scope ----
    # If this went red the gate would tax all 316 non-pipeline projects.
    with tempfile.TemporaryDirectory() as d:
        tmp, rel = _ws(Path(d), code="FIXFREE", registered=False, body=TO_NO_REF)
        rc, out = _run(tmp, rel, "--enforce")
        check("unregistered project -> rc=0", rc == 0, out[:200])
        check("skip is COUNTED, not silent",
              "1 skipped (project not pipeline-registered)" in out, out[:200])

    # ---- ARM 4: CONTROL -- a non-task_orders path is out of scope ----
    with tempfile.TemporaryDirectory() as d:
        tmp, rel = _ws(Path(d), code="FIXPIPE", registered=True, body=TO_NO_REF,
                       subdir="org/tier2_senior/0.8.0_AE_CloudComp/deliverables")
        rc, out = _run(tmp, rel, "--enforce")
        check("path outside task_orders/ -> rc=0", rc == 0, out[:200])
        check("out-of-scope path reported as 0 under task_orders/",
              "0 under task_orders/" in out, out[:200])

    # ---- ARM 5: RAMP -- same defect, ANNOUNCE mode, must NOT block ----
    with tempfile.TemporaryDirectory() as d:
        tmp, rel = _ws(Path(d), code="FIXPIPE", registered=True, body=TO_NO_REF)
        rc, out = _run(tmp, rel)
        check("ANNOUNCE: finding present but rc=0",
              rc == 0 and "findings=1" in out, out[:200])
        check("ANNOUNCE says how to arm", "pipeline-gate2.enforce" in out, out[:200])

    # ---- ARM 6: RAMP -- the MARKER FILE arms it, with no --enforce flag ----
    # The marker is the authority; this proves the file itself flips the mode.
    with tempfile.TemporaryDirectory() as d:
        tmp, rel = _ws(Path(d), code="FIXPIPE", registered=True, body=TO_NO_REF)
        (tmp / "org" / "mcp").mkdir(parents=True, exist_ok=True)
        (tmp / "org" / "mcp" / "pipeline-gate2.enforce").write_text("armed", encoding="utf-8")
        rc, out = _run(tmp, rel)
        check("marker file alone flips ENFORCE", rc == 1 and "mode=ENFORCE" in out, out[:200])

    # ---- ARM 7: OVERRIDE -- audited, and it actually writes the audit line ----
    with tempfile.TemporaryDirectory() as d:
        tmp, rel = _ws(Path(d), code="FIXPIPE", registered=True, body=TO_NO_REF)
        rc, out = _run(tmp, rel, "--enforce", "--override-reason", "fixture reason")
        log = tmp / "org" / "mcp" / "pipeline-gate2-override.log"
        check("override -> rc=0", rc == 0, out[:200])
        check("override WRITES an audit line",
              log.is_file() and "fixture reason" in log.read_text(encoding="utf-8"),
              "audit log missing or empty")
        check("override warns that repeats are a coverage gap",
              "COVERAGE GAP" in out, out[:200])

    # ---- ARM 8: a <decomp_ref> naming NO cell ids is not a pass ----
    # A path with no cells cannot be joined to any criterion -- layer 1 would have
    # nothing to close against, so accepting it here would launder an empty ref.
    with tempfile.TemporaryDirectory() as d:
        tmp, rel = _ws(Path(d), code="FIXPIPE", registered=True, body=TO_REF_NO_CELLS)
        rc, out = _run(tmp, rel, "--enforce")
        check("decomp_ref with no cell ids -> rc=1",
              rc == 1 and "NO CELL IDS" in out, out[:200])

    width = max(len(n) for n, _, _ in results)
    for name, verdict, detail in results:
        line = f"  {verdict:4s} {name.ljust(width)}"
        if verdict == FAIL and detail:
            line += f"   <- {detail[:200]}"
        print(line)
    failed = [r for r in results if r[1] == FAIL]
    print(f"\nto-decomp-ref-lint battery: {len(results) - len(failed)}/{len(results)} arms as expected")
    if failed:
        print("BATTERY FAILED -- the gate does not behave as specified.")
        return 1
    print("BATTERY PASS -- refuses the defect, passes all four out-of-scope shapes, "
          "the ramp and the audited override both work, and the refusal teaches.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

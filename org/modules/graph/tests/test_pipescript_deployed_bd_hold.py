"""NFRA_TOOLPASS: comp-pipescript `deployed` bd branch is HELD (CTO ruling 20260710T233307Z).
_check_one does hashlib.md5(local_path.read_bytes()) over data/black_diamond/scripts/{gold,silver}
-- a bd SOURCE content read -- plus a head-object on opal-data-bd. So the bd branch is SKIPPED for a
normal agent invocation, NAMED as held (no silent drop), with COMP_PIPESCRIPT_INCLUDE_HELD=1 to
re-enable the DS deploy-verify path.

This test (synthetic, monkeypatched -- NEVER runs `deployed` against opal-data-bd) asserts:
  - default (no override): the bd branch is SKIPPED, NAMED as held, and opens ZERO held files.
  - non-vacuous: with COMP_PIPESCRIPT_INCLUDE_HELD=1 the guard does NOT skip (it proceeds past the
    guard); we stop it at aws-CLI-resolution (patched absent) so it still opens no held file.

# rail-checked: assurance oracle for comp-pipescript under test (NFRA_TOOLPASS sec.6)
Author: 3.0.0_SA_CVO~B.
"""

import io
import os
import shutil
import sys
from contextlib import redirect_stdout
from pathlib import Path
from types import SimpleNamespace

_HERE = os.path.dirname(os.path.abspath(__file__))
_WS = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(_HERE))))
for _p in (_WS, os.path.dirname(os.path.dirname(_HERE))):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import org.modules.graph.pipeline_cli as ps  # noqa: E402


def _run(include_held: bool):
    args = SimpleNamespace(pipeline="bd-gold", firm=None, script_id="")
    held_reads: list = []
    orig_rb = Path.read_bytes
    orig_which = shutil.which

    def _rb(self, *a, **k):
        s = str(self).replace("\\", "/")
        if "data/black_diamond/" in s:
            held_reads.append(s)
        return orig_rb(self, *a, **k)

    Path.read_bytes = _rb
    if include_held:
        os.environ["COMP_PIPESCRIPT_INCLUDE_HELD"] = "1"
        shutil.which = lambda *a, **k: None   # stop right after the guard (aws-not-found), before the loop
    else:
        os.environ.pop("COMP_PIPESCRIPT_INCLUDE_HELD", None)

    buf = io.StringIO()
    rc = None
    try:
        with redirect_stdout(buf):
            rc = ps.cmd_deployed(args)
    except SystemExit as e:
        rc = ("exit", e.code)
    finally:
        Path.read_bytes = orig_rb
        shutil.which = orig_which
        os.environ.pop("COMP_PIPESCRIPT_INCLUDE_HELD", None)
    return buf.getvalue(), rc, held_reads


def test_bd_branch_held_and_named_by_default():
    out, rc, held = _run(include_held=False)
    assert "SKIP: opal-data-bd" in out, f"bd branch must be NAMED as held (no silent drop): {out!r}"
    assert rc == 0, f"a held-skip returns 0, got {rc}"
    assert held == [], f"a held bd file was opened despite the skip: {held}"


def test_override_regates_the_bd_branch_non_vacuous():
    out, rc, held = _run(include_held=True)
    assert "SKIP: opal-data-bd" not in out, "with COMP_PIPESCRIPT_INCLUDE_HELD=1 the guard must NOT skip"
    assert rc == ("exit", 2), f"override proceeds PAST the guard to aws-not-found (exit 2), got {rc}"
    assert held == [], "the override arm must still not open a held file (stopped at aws-resolution)"


if __name__ == "__main__":
    o1, r1, h1 = _run(False)
    print(f"[default]  skip-note={'SKIP: opal-data-bd' in o1}  rc={r1}  held_reads={len(h1)}")
    test_bd_branch_held_and_named_by_default()
    print("PASS: bd branch HELD + NAMED by default, 0 held files opened")
    o2, r2, h2 = _run(True)
    print(f"[override] skip-note={'SKIP: opal-data-bd' in o2}  rc={r2}  held_reads={len(h2)}")
    test_override_regates_the_bd_branch_non_vacuous()
    print("PASS: COMP_PIPESCRIPT_INCLUDE_HELD=1 re-gates the branch (non-vacuous)")
    print("=== comp-pipescript deployed bd-hold: ALL PASS ===")

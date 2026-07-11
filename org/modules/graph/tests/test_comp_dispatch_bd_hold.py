"""NFRA_TOOLPASS C0 (census reader #1): comp-dispatch is agent-facing (.tools/comp-dispatch -> comp_dispatch.py);
`comp-dispatch bd` resolves to data/black_diamond/scripts/gold/gold_dispatch.sh and analyze() open+read its
CONTENT (:156-157) with NO held guard. FIX: path-based skip by default (cot/inf still work),
COMP_DISPATCH_INCLUDE_HELD=1 re-enables for the DS bd-dispatch path.

bd-SAFE + hermetic: monkeypatches find_dispatch to a SYNTHETIC tmp gold_dispatch.sh whose path contains
data/black_diamond/ -- NEVER the real bd tree. Non-vacuous: default -> held (no read); override -> reads.

# rail-checked: assurance oracle for comp-dispatch under test (NFRA_TOOLPASS sec.6)
Author: 3.0.0_SA_CVO~B.
"""

import importlib.util
import os
import tempfile
from pathlib import Path

_HERE = os.path.dirname(os.path.abspath(__file__))
_WS = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(_HERE))))
_MODULE = os.path.join(_WS, "org", "modules", "graph", "comp_dispatch.py")

_spec = importlib.util.spec_from_file_location("comp_dispatch_undertest", _MODULE)
cd = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(cd)

_DISPATCH = 'CATALOG="\nA_01 | a.py | \n"\n'


def test_is_held_predicate():
    assert cd._is_held("data/black_diamond/scripts/gold/gold_dispatch.sh") is True
    assert cd._is_held(r"C:\x\data\black_diamond\scripts\gold\gold_dispatch.sh") is True
    assert cd._is_held("data/canonical/schwab/silver/x.sh") is True
    assert cd._is_held("data/cot/scripts/gold/gold_dispatch.sh") is False
    assert cd._is_held("data/inf/scripts/gold/gold_dispatch.sh") is False


def _analyze_bd(include_held: bool):
    saved = cd.find_dispatch
    with tempfile.TemporaryDirectory() as d:
        gold = Path(d) / "data" / "black_diamond" / "scripts" / "gold"
        gold.mkdir(parents=True, exist_ok=True)
        f = gold / "gold_dispatch.sh"
        f.write_text(_DISPATCH, encoding="utf-8")
        cd.find_dispatch = lambda arg: (str(f), "black_diamond")
        if include_held:
            os.environ["COMP_DISPATCH_INCLUDE_HELD"] = "1"
        else:
            os.environ.pop("COMP_DISPATCH_INCLUDE_HELD", None)
        try:
            return cd.analyze("bd")
        finally:
            cd.find_dispatch = saved
            os.environ.pop("COMP_DISPATCH_INCLUDE_HELD", None)


def test_bd_dispatch_held_by_default_reads_under_override_nonvacuous():
    default = _analyze_bd(include_held=False)
    assert default.get("held") is True, f"a held bd dispatch must be SKIPPED by default: {default}"
    over = _analyze_bd(include_held=True)
    assert not over.get("held"), \
        f"COMP_DISPATCH_INCLUDE_HELD=1 must READ the bd dispatch (guard non-vacuous): {over}"


if __name__ == "__main__":
    test_is_held_predicate()
    print("PASS: _is_held -- bd/schwab held, cot/inf not")
    test_bd_dispatch_held_by_default_reads_under_override_nonvacuous()
    print("PASS: bd dispatch held by default, read under COMP_DISPATCH_INCLUDE_HELD=1 (non-vacuous)")
    print("=== comp-dispatch bd-hold: ALL PASS ===")

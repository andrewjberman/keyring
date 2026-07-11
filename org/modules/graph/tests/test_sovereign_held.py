"""NFRA_TOOLPASS C1: the STRONGEST test for the load-bearing sovereign-hold leaf (_sovereign_held.py).
Every bd-reader guard will import from this module, so a bug here un-guards everything -- hence:
  - boundary cases on both predicates (opal-data-bdx NOT held; opal-data-bd/x held; inf/cot NOT held),
  - include_held 3-arm precedence (canonical lifts all / a legacy var alone lifts its tool / neither holds),
  - the module's own invariant: it imports STDLIB ONLY (ast check over its import nodes) -- a load-bearing
    security leaf must never fail to import or move under a dependency change.

Pure-function + ast; hermetic + bd-safe (no file/AWS).

# rail-checked: assurance oracle for _sovereign_held under test (NFRA_TOOLPASS sec.6)
Author: 3.0.0_SA_CVO~B.
"""

import ast
import importlib.util
import os
from pathlib import Path

_HERE = os.path.dirname(os.path.abspath(__file__))
_WS = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(_HERE))))
_MODULE = os.path.join(_WS, "org", "modules", "graph", "sovereign_held.py")

_spec = importlib.util.spec_from_file_location("sovereign_held_undertest", _MODULE)
sh = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(sh)


def test_is_held_path_boundary():
    assert sh.is_held_path("data/black_diamond/scripts/gold/x.py") is True
    assert sh.is_held_path("data/canonical/schwab/silver/build_dim.py") is True
    assert sh.is_held_path("schwab/silver/rps.py") is True
    assert sh.is_held_path(r"C:\repo\data\black_diamond\scripts\gold\x.py") is True   # backslash + absolute
    # NOT held:
    assert sh.is_held_path("data/inf/scripts/gold/x.py") is False
    assert sh.is_held_path("data/cot/scripts/gold/x.py") is False
    assert sh.is_held_path("") is False
    assert sh.is_held_path(None) is False


def test_is_held_bucket_family_boundary():
    assert sh.is_held_bucket("opal-data-bd") is True             # exact
    assert sh.is_held_bucket("opal-data-bd-raw") is True         # <p>-*
    assert sh.is_held_bucket("opal-data-bd/platinum/x.json") is True   # <p>/*
    assert sh.is_held_bucket("s3://opal-data-bd/gold/x.parquet") is True   # s3:// scheme stripped
    assert sh.is_held_bucket("opal-data-schwab") is True
    # case-insensitive + whitespace-tolerant (matches freeze_monitor._bucket_is_held; a true no-op for its
    # migration; conservative -- lowercasing only ADDS held-matches):
    assert sh.is_held_bucket("OPAL-DATA-BD") is True
    assert sh.is_held_bucket("Opal-Data-BD/key") is True
    assert sh.is_held_bucket("  opal-data-bd  ") is True
    assert sh.is_held_bucket("S3://OPAL-DATA-SCHWAB/x") is True
    # NOT held -- the load-bearing boundary (preserved under .lower()):
    assert sh.is_held_bucket("opal-data-bdx") is False           # distinct bucket, NOT a prefix-family match
    assert sh.is_held_bucket("OPAL-DATA-BDX") is False           # ditto, case-insensitively
    assert sh.is_held_bucket("opal-data-inf") is False
    assert sh.is_held_bucket("opal-data-cot") is False
    assert sh.is_held_bucket("") is False
    assert sh.is_held_bucket(None) is False


def test_include_held_three_arm_precedence():
    for v in ("COMP_INCLUDE_HELD", "COMP_VALIDATE_INCLUDE_HELD", "COMP_OTHER_INCLUDE_HELD"):
        os.environ.pop(v, None)
    try:
        # arm 3: neither set -> held (False)
        assert sh.include_held("COMP_VALIDATE_INCLUDE_HELD") is False
        assert sh.include_held() is False
        # arm 2: a legacy var alone lifts ITS tool
        os.environ["COMP_VALIDATE_INCLUDE_HELD"] = "1"
        assert sh.include_held("COMP_VALIDATE_INCLUDE_HELD") is True
        # precision: a legacy var NOT passed does not lift (only the caller's own var counts)
        assert sh.include_held("COMP_OTHER_INCLUDE_HELD") is False
        os.environ.pop("COMP_VALIDATE_INCLUDE_HELD", None)
        # arm 1: the canonical var lifts ALL (even with no legacy vars passed)
        os.environ["COMP_INCLUDE_HELD"] = "1"
        assert sh.include_held() is True
        assert sh.include_held("COMP_VALIDATE_INCLUDE_HELD") is True
        # only "1" lifts (not any truthy value)
        os.environ["COMP_INCLUDE_HELD"] = "true"
        assert sh.include_held() is False
    finally:
        for v in ("COMP_INCLUDE_HELD", "COMP_VALIDATE_INCLUDE_HELD", "COMP_OTHER_INCLUDE_HELD"):
            os.environ.pop(v, None)


def test_module_imports_are_stdlib_only():
    """The load-bearing invariant: a security leaf every tool imports must never pull a non-stdlib dep."""
    tree = ast.parse(Path(_MODULE).read_text(encoding="utf-8"))
    mods = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for n in node.names:
                mods.add(n.name.split(".")[0])
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                mods.add(node.module.split(".")[0])
    allowed = {"os", "__future__"}
    assert mods <= allowed, f"_sovereign_held must import STDLIB ONLY; found non-allowed: {mods - allowed}"


if __name__ == "__main__":
    test_is_held_path_boundary()
    test_is_held_bucket_family_boundary()
    test_include_held_three_arm_precedence()
    test_module_imports_are_stdlib_only()
    print("=== _sovereign_held: predicates + include_held precedence + stdlib-only invariant: ALL PASS ===")

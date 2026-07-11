"""NFRA_TOOLPASS C0 (census readers #3,#4): the recognizer PARITY HARNESSES read REAL bd source --
comp_recognizers_code._edges_for (open+read gold_dispatch.sh/s3_layout/A_00/A_01) and
comp_recognizers_config.ConfigYamlFrontEnd.build_trees (open+yaml.compose bd gold_freshness_config.yaml).
Both are __main__-only parity runners (not on the comp rail), but a __main__ IS agent-runnable ->
DEFENSIVE path-based skip (CTO 031353Z: cheap str-skip, consistency beats a redundant guard).
COMP_RECOGNIZERS_INCLUDE_HELD=1 re-enables (DS/parity path).

bd-SAFE + hermetic: patches os.path.exists -> True and spies `open` (raises if reached), so a held path
is NEVER actually opened -- even a broken guard cannot read real bd here (the spy intercepts first).
Non-vacuous: with the guard, open is NOT reached for a held path by default; the mutant (neuter the
guard) reaches open -> the spy raises -> the test fails.

# rail-checked: assurance oracle for the recognizer parity harnesses under test (NFRA_TOOLPASS sec.6)
Author: 3.0.0_SA_CVO~B.
"""

import importlib.util
import os
from unittest import mock

_HERE = os.path.dirname(os.path.abspath(__file__))
_WS = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(_HERE))))


def _load(name, filename):
    path = os.path.join(_WS, "org", "modules", "graph", filename)
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


rc = _load("comp_recognizers_code_ut", "comp_recognizers_code.py")
rg = _load("comp_recognizers_config_ut", "comp_recognizers_config.py")


def test_is_held_both_modules():
    for mod in (rc, rg):
        assert mod._is_held("data/black_diamond/scripts/gold/gold_dispatch.sh") is True
        assert mod._is_held("data/canonical/schwab/silver/x.yaml") is True
        assert mod._is_held("data/inf/scripts/gold/x.sh") is False
        assert mod._is_held("data/cot/scripts/gold/x.sh") is False


def test_include_held_flag_both_modules():
    os.environ.pop("COMP_RECOGNIZERS_INCLUDE_HELD", None)
    assert rc._recognizers_include_held() is False and rg._recognizers_include_held() is False
    os.environ["COMP_RECOGNIZERS_INCLUDE_HELD"] = "1"
    try:
        assert rc._recognizers_include_held() is True and rg._recognizers_include_held() is True
    finally:
        os.environ.pop("COMP_RECOGNIZERS_INCLUDE_HELD", None)


def _spy_open(*a, **k):
    raise AssertionError(f"open() must NOT be reached for a held path by default: {a[0] if a else '?'}")


def test_code_edges_for_held_not_read_by_default():
    os.environ.pop("COMP_RECOGNIZERS_INCLUDE_HELD", None)
    saved = getattr(rc, "open", None)
    with mock.patch.object(rc.os.path, "exists", return_value=True):
        rc.open = _spy_open
        try:
            edges, cov = rc._edges_for(object(), "data/black_diamond/scripts/gold/gold_dispatch.sh", "")
            assert edges == [] and cov is None, f"held path must yield ([], None) without reading: {edges}"
        finally:
            if saved is None:
                delattr(rc, "open")
            else:
                rc.open = saved


def test_config_build_trees_held_not_read_by_default():
    os.environ.pop("COMP_RECOGNIZERS_INCLUDE_HELD", None)
    saved = getattr(rg, "open", None)
    with mock.patch.object(rg.os.path, "exists", return_value=True):
        rg.open = _spy_open
        try:
            fe = rg.ConfigYamlFrontEnd()
            trees = list(fe.build_trees(["data/black_diamond/scripts/gold/gold_freshness_config.yaml"]))
            assert trees == [], f"held config must be skipped (no tree) without reading: {trees}"
        finally:
            if saved is None:
                delattr(rg, "open")
            else:
                rg.open = saved


if __name__ == "__main__":
    test_is_held_both_modules()
    test_include_held_flag_both_modules()
    test_code_edges_for_held_not_read_by_default()
    test_config_build_trees_held_not_read_by_default()
    print("=== comp_recognizers code+config bd-hold: ALL PASS (held source never read by default) ===")

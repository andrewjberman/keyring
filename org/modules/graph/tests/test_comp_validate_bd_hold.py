"""NFRA_TOOLPASS: comp-validate (validate_cli.py) is the 7th/final bd-reader. _load_raw_validate_configs
read BOTH _BD_VALIDATE_CONFIG (data/black_diamond/scripts/gold/gold_validate_config.yaml) and the inf
config UNCONDITIONALLY (alias map at :384/:802, cmd_list, every non-INF validation, --list), and
_find_standalone_validator statted/dispatched data/black_diamond/scripts/validators/ -- so INF/cot work
auto-read bd SOURCE. FIX (sovereign held-exclusion, NAMED): skip the bd config + bd validators dir by
default; COMP_VALIDATE_INCLUDE_HELD=1 re-enables them for the DS bd-validate/deploy cycle (Rule 13).

This test is bd-SAFE: it redirects _BD_VALIDATE_CONFIG / _INF_VALIDATE_CONFIG / STANDALONE_VALIDATORS_DIR
to SYNTHETIC tmp files -- it NEVER reads the real bd config. It proves the guard by OUTCOME: under the
default hold the synthetic bd stanza is ABSENT from the merged map (bd not read); under the override it
is PRESENT (non-vacuous). If the guard failed, the synthetic bd stanza would appear by default.

# rail-checked: assurance oracle for comp-validate under test (NFRA_TOOLPASS sec.6)
Author: 3.0.0_SA_CVO~B.
"""

import importlib.util
import os
import tempfile
from pathlib import Path

_HERE = os.path.dirname(os.path.abspath(__file__))
_WS = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(_HERE))))
_MODULE = os.path.join(_WS, "org", "modules", "graph", "validate_cli.py")

_spec = importlib.util.spec_from_file_location("validate_cli_undertest", _MODULE)
vc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(vc)


def _synth_configs(tmp):
    bd = Path(tmp) / "bd_gold_validate_config.yaml"
    inf = Path(tmp) / "inf_gold_validate_config.yaml"
    bd.write_text("scripts:\n  BD_ONLY_SENTINEL:\n    checks: []\n", encoding="utf-8")
    inf.write_text("scripts:\n  INF_ONLY_SENTINEL:\n    checks: []\n", encoding="utf-8")
    return bd, inf


def _run_load_raw(include_held: bool):
    saved = (vc._BD_VALIDATE_CONFIG, vc._INF_VALIDATE_CONFIG, vc._bd_skip_noted)
    with tempfile.TemporaryDirectory() as d:
        bd, inf = _synth_configs(d)
        vc._BD_VALIDATE_CONFIG = bd
        vc._INF_VALIDATE_CONFIG = inf
        vc._bd_skip_noted = False
        if include_held:
            os.environ["COMP_VALIDATE_INCLUDE_HELD"] = "1"
        else:
            os.environ.pop("COMP_VALIDATE_INCLUDE_HELD", None)
        try:
            result = vc._load_raw_validate_configs()
        finally:
            (vc._BD_VALIDATE_CONFIG, vc._INF_VALIDATE_CONFIG, vc._bd_skip_noted) = saved
            os.environ.pop("COMP_VALIDATE_INCLUDE_HELD", None)
    return result


def test_load_raw_configs_excludes_bd_by_default():
    result = _run_load_raw(include_held=False)
    assert "INF_ONLY_SENTINEL" in result, f"inf config must still load (bd hold must not break inf): {list(result)}"
    assert "BD_ONLY_SENTINEL" not in result, \
        f"bd config was READ under the default hold (guard failed): {list(result)}"


def test_override_includes_bd_nonvacuous():
    result = _run_load_raw(include_held=True)
    assert "BD_ONLY_SENTINEL" in result, \
        f"COMP_VALIDATE_INCLUDE_HELD=1 must re-read the bd config (proves the guard gates -- non-vacuous): {list(result)}"
    assert "INF_ONLY_SENTINEL" in result, f"inf must still load under override: {list(result)}"


def _run_find_standalone(include_held: bool):
    saved = (vc.STANDALONE_VALIDATORS_DIR, vc._bd_skip_noted)
    with tempfile.TemporaryDirectory() as d:
        (Path(d) / "validate_TESTID.py").write_text("# synthetic standalone validator\n", encoding="utf-8")
        vc.STANDALONE_VALIDATORS_DIR = Path(d)
        vc._bd_skip_noted = False
        if include_held:
            os.environ["COMP_VALIDATE_INCLUDE_HELD"] = "1"
        else:
            os.environ.pop("COMP_VALIDATE_INCLUDE_HELD", None)
        try:
            found = vc._find_standalone_validator("TESTID")
        finally:
            (vc.STANDALONE_VALIDATORS_DIR, vc._bd_skip_noted) = saved
            os.environ.pop("COMP_VALIDATE_INCLUDE_HELD", None)
    return found


def test_find_standalone_validator_skips_bd_dir_by_default_nonvacuous():
    # the synthetic validator file EXISTS -- default must still return None (guard), override finds it.
    assert _run_find_standalone(include_held=False) is None, \
        "bd standalone validators dir must be SKIPPED by default even when the file exists (guard)"
    assert _run_find_standalone(include_held=True) is not None, \
        "COMP_VALIDATE_INCLUDE_HELD=1 must find the bd standalone validator (non-vacuous)"


def test_is_held_bd_path_catches_explicit_config_hole():
    # closes the --config bypass: an explicit --config into the held bd/schwab tree is a held read.
    assert vc._is_held_bd_path("data/black_diamond/scripts/gold/gold_validate_config.yaml") is True
    assert vc._is_held_bd_path(r"data\black_diamond\scripts\gold\gold_validate_config.yaml") is True
    assert vc._is_held_bd_path("data/canonical/schwab/silver/build_dim.yaml") is True
    # in-scope pipelines must NOT be caught.
    assert vc._is_held_bd_path("data/inf/scripts/gold/gold_validate_config.yaml") is False
    assert vc._is_held_bd_path("data/cot/scripts/gold/gold_validate_config.yaml") is False


if __name__ == "__main__":
    test_load_raw_configs_excludes_bd_by_default()
    print("PASS: _load_raw_validate_configs excludes the bd config by default (inf still loads)")
    test_override_includes_bd_nonvacuous()
    print("PASS: COMP_VALIDATE_INCLUDE_HELD=1 re-reads the bd config (non-vacuous)")
    test_find_standalone_validator_skips_bd_dir_by_default_nonvacuous()
    print("PASS: _find_standalone_validator skips the bd validators dir by default (override finds it)")
    test_is_held_bd_path_catches_explicit_config_hole()
    print("PASS: _is_held_bd_path catches an explicit --config into the held bd/schwab tree")
    print("=== comp-validate bd-hold: ALL PASS ===")

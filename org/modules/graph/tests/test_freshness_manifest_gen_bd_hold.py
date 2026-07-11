"""NFRA_TOOLPASS C0 (census reader #5): .tools/freshness_manifest_gen.py is a PATH-runnable generator;
_load_yaml_list (:107) yaml.safe_load(open()) the bd-gold freshness config
(data/black_diamond/scripts/gold/gold_freshness_config.yaml, CONFIG_FILES :57) with NO held guard --
while the SIBLING comp-freshness guards the SAME file via COMP_FRESHNESS_PIPELINE. FIX: honor the SAME
flag so one signal re-enables both; skip the held config by default (inf/cot/served pass through).

bd-SAFE + hermetic: monkeypatches ROOT to a tmp dir with SYNTHETIC bd + inf configs -- NEVER the real
bd tree. Non-vacuous: the held config -> [] by default, reads under COMP_FRESHNESS_PIPELINE=1 (same file).

# rail-checked: assurance oracle for freshness_manifest_gen under test (NFRA_TOOLPASS sec.6)
Author: 3.0.0_SA_CVO~B.
"""

import importlib.util
import os
import tempfile
from pathlib import Path

_HERE = os.path.dirname(os.path.abspath(__file__))
_WS = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(_HERE))))
_MODULE = os.path.join(_WS, ".tools", "freshness_manifest_gen.py")

_spec = importlib.util.spec_from_file_location("freshness_manifest_gen_undertest", _MODULE)
fmg = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(fmg)

_BD_REL = "data/black_diamond/scripts/gold/gold_freshness_config.yaml"
_INF_REL = "data/inf/scripts/gold/gold_freshness_config.yaml"
_YAML = "- artifact_id: x\n  cadence: daily\n"


def test_is_held_predicate():
    assert fmg._is_held(_BD_REL) is True
    assert fmg._is_held("data/canonical/schwab/silver/x.yaml") is True
    assert fmg._is_held(_INF_REL) is False
    assert fmg._is_held("data/cot/scripts/gold/gold_freshness_config.yaml") is False


def _load(rel, include_held):
    saved_root = fmg.ROOT
    with tempfile.TemporaryDirectory() as d:
        f = Path(d) / rel
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(_YAML, encoding="utf-8")
        fmg.ROOT = d
        if include_held:
            os.environ["COMP_FRESHNESS_PIPELINE"] = "1"
        else:
            os.environ.pop("COMP_FRESHNESS_PIPELINE", None)
        try:
            return fmg._load_yaml_list(rel)
        finally:
            fmg.ROOT = saved_root
            os.environ.pop("COMP_FRESHNESS_PIPELINE", None)


def test_bd_config_held_by_default_reads_under_flag_nonvacuous():
    assert _load(_BD_REL, include_held=False) == [], "held bd config must be skipped by default (guard)"
    assert _load(_BD_REL, include_held=True), \
        "COMP_FRESHNESS_PIPELINE=1 must READ the bd config (non-vacuous; same file, only the flag differs)"


def test_inf_config_always_read():
    assert _load(_INF_REL, include_held=False), "inf config is not held -> must read regardless of the flag"


if __name__ == "__main__":
    test_is_held_predicate()
    print("PASS: _is_held -- bd/schwab held, inf/cot not")
    test_bd_config_held_by_default_reads_under_flag_nonvacuous()
    print("PASS: bd freshness config held by default, read under COMP_FRESHNESS_PIPELINE=1 (non-vacuous)")
    test_inf_config_always_read()
    print("PASS: inf config always read (not held)")
    print("=== freshness_manifest_gen bd-hold: ALL PASS ===")

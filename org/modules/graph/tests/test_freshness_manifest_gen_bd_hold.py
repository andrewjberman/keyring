"""freshness_manifest_gen held-config GUARD MECHANISM oracle (post-lift form).

HISTORY: authored by 3.0.0_SA_CVO~B under NFRA_TOOLPASS C0 while the 2026-07-09 hold was live;
the hold-era assertions (bd config held-by-default) went stale-red after the retraction landed
(SOVEREIGN_HELD_PATHS=() @7a07814b94, the 13-file predicate-split wave -- the ENGINE is right,
the tests were stale; dial F11, TO ADHOC.graph-tests-hygiene-f11-family).

TRUTH DETERMINATION (grounded at HEAD before this repair): LIFTED, mechanism retained --
.tools/freshness_manifest_gen.py:117 still guards via `_is_held(rel_path)` delegated to
sovereign_held.is_held_path, which resolves SOVEREIGN_HELD_PATHS at CALL time; the set is
empty, so nothing is held. Repaired to post-lift truth + INJECTED-mechanism cases
(monkeypatch on the predicate's own globals -- never the governance set).

bd-SAFE + hermetic as before: tmp-dir ROOT, synthetic configs, real trees never touched.
# rail-checked: assurance oracle for freshness_manifest_gen (dial F11 repair)
Original author: 3.0.0_SA_CVO~B. F11 repair: 0.8.0_AE_CloudComp~D.
"""
from __future__ import annotations

import importlib.util
import os
import tempfile
from pathlib import Path

import pytest

_HERE = os.path.dirname(os.path.abspath(__file__))
_WS = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(_HERE))))
_MODULE = os.path.join(_WS, ".tools", "freshness_manifest_gen.py")

_spec = importlib.util.spec_from_file_location("freshness_manifest_gen_undertest", _MODULE)
fmg = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(fmg)

_BD_REL = "data/black_diamond/scripts/gold/gold_freshness_config.yaml"
_INF_REL = "data/inf/scripts/gold/gold_freshness_config.yaml"
_YAML = "- artifact_id: x\n  cadence: daily\n"


# SYNTHETIC injection marker (substring semantics, sovereign_held.py:80).
_SYNTH = "synthetic_held_zone_f11"


@pytest.fixture
def injected_hold(monkeypatch):
    """Inject a synthetic held marker into the predicate's OWN module globals --
    fmg._is_held IS sovereign_held.is_held_path, which reads SOVEREIGN_HELD_PATHS from its
    defining module's globals at call time; patching those globals arms the mechanism without
    touching the (correctly empty) governance state."""
    monkeypatch.setitem(fmg._is_held.__globals__, "SOVEREIGN_HELD_PATHS", (_SYNTH + "/",))


def test_is_held_predicate_post_lift_and_under_injection(injected_hold):
    # POST-LIFT TRUTH for the real trees: nothing is held (the retraction emptied the set).
    assert fmg._is_held(_BD_REL) is False, "post-lift: bd is NOT held (SOVEREIGN_HELD_PATHS=())"
    assert fmg._is_held(_INF_REL) is False
    # MECHANISM: the injected marker IS held -- the predicate still discriminates.
    assert fmg._is_held(_SYNTH + "/scripts/gold/x.yaml") is True, \
        "injected marker must register as held (the mechanism, not governance)"


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


def test_bd_config_read_post_lift():
    """POST-LIFT TRUTH: the bd config READS by default now -- nothing is held."""
    assert _load(_BD_REL, include_held=False), \
        "post-lift: the bd freshness config must be READ by default (the retraction emptied the set)"


def test_injected_held_config_skipped_and_reads_under_flag(injected_hold):
    """THE MECHANISM under injection: a config under the injected marker is skipped by default
    and READS under COMP_FRESHNESS_PIPELINE=1 -- the non-vacuous flag pair, same file."""
    rel = _SYNTH + "/scripts/gold/gold_freshness_config.yaml"
    assert _load(rel, include_held=False) == [], \
        "a config under the INJECTED held marker must be skipped by default (guard mechanism)"
    assert _load(rel, include_held=True), \
        "COMP_FRESHNESS_PIPELINE=1 must READ the same config under injection (non-vacuous)"


def test_inf_config_always_read():
    assert _load(_INF_REL, include_held=False), "inf config is not held -> must read regardless of the flag"

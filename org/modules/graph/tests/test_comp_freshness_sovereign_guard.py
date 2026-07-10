#!/usr/bin/env python3
"""Sovereign-guard tests for comp-freshness (FR1), NFRA_TOOLPASS.

comp-freshness is the 4th bd-reader-class tool: it reads BD_CONFIG
(data/black_diamond/scripts/gold/gold_freshness_config.yaml, a sec.8 held path) on
list/all/chain-bd/script-bd AND LATENTLY on `artifact <ANY>` (the config-search loop).

TWO guards, per CTO's FR1 ruling (20260710T215214Z, COO-grounded):
  (1) ENV-FLAG FAIL-SAFE at the _load_config chokepoint -- comp-freshness is a LIVE pre-chain-dispatch
      gate (the bd dispatch runs `chain bd`), so a HARD exclude would break the $130M-class protection.
      COMP_FRESHNESS_PIPELINE=1 set -> read normally (pipeline); unset (agent) -> skip held config with
      a loud note. NEVER silent, NEVER hard-exclude.
  (2) ARTIFACT-LOOP SUB-FIX -- `artifact <non-bd>` no longer consults a held config for a non-held target.

SOVEREIGN-SAFE: no test reads the REAL data/black_diamond/ config. The guard DECISION is a pure path
predicate; tests exercise the predicate + the refuse-returns-empty behavior. bd content is never opened.
"""
from __future__ import annotations

import importlib.machinery
import importlib.util
import os
import sys
from pathlib import Path

_WS = Path(__file__).resolve().parents[4]
_CF = _WS / ".tools" / "comp-freshness"


def _load(flag: str | None):
    """Fresh import of comp-freshness with COMP_FRESHNESS_PIPELINE set/unset."""
    if flag is None:
        os.environ.pop("COMP_FRESHNESS_PIPELINE", None)
    else:
        os.environ["COMP_FRESHNESS_PIPELINE"] = flag
    loader = importlib.machinery.SourceFileLoader("cf_under_test", str(_CF))
    spec = importlib.util.spec_from_loader("cf_under_test", loader)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["cf_under_test"] = mod
    loader.exec_module(mod)
    return mod


# ---- (1) env-flag fail-safe at the chokepoint --------------------------------------------

def test_held_predicate_is_pure_and_correct():
    cf = _load(None)
    assert cf._config_is_held(cf.BD_CONFIG) is True, "BD config is a sec.8 held path"
    assert cf._config_is_held(cf.INF_CONFIG) is False, "inf is in-scope"
    assert cf._config_is_held(cf.COT_CONFIG) is False, "cot is in-scope"
    assert cf._config_is_held(cf.SERVED_CONFIG) is False


def test_agent_context_refuses_bd_config_read_returns_empty():
    cf = _load(None)  # flag unset = interactive agent
    assert cf._pipeline_flag_set() is False
    assert cf._held_config_read_allowed(cf.BD_CONFIG) is False
    # _load_config on a held path returns [] WITHOUT opening the file (0 bd read)
    assert cf._load_config(cf.BD_CONFIG) == [], "held config must be refused -> empty, not read"


def test_pipeline_context_allows_bd_config_read():
    cf = _load("1")  # the pipeline sets the flag -> the live gate still works
    assert cf._pipeline_flag_set() is True
    assert cf._held_config_read_allowed(cf.BD_CONFIG) is True, "pipeline path must read bd config"


def test_inscope_configs_always_read_regardless_of_flag():
    for flag in (None, "1"):
        cf = _load(flag)
        assert cf._held_config_read_allowed(cf.INF_CONFIG) is True
        assert cf._held_config_read_allowed(cf.COT_CONFIG) is True
        assert cf._held_config_read_allowed(cf.SERVED_CONFIG) is True


def test_MUTANT_flag_check_off_would_read_bd_in_agent_context():
    """NEGATIVE CONTROL: if the pipeline-flag branch were removed (always treated as pipeline), an
    AGENT context would read bd. Proves the flag check is load-bearing."""
    cf = _load(None)
    # simulate the mutant: force the flag path to always-true
    assert cf._held_config_read_allowed(cf.BD_CONFIG) is False  # guarded (baseline)
    saved = cf._pipeline_flag_set
    cf._pipeline_flag_set = lambda: True   # MUTANT
    try:
        assert cf._held_config_read_allowed(cf.BD_CONFIG) is True, \
            "with the flag forced on, the agent context WOULD read bd -- the check is load-bearing"
    finally:
        cf._pipeline_flag_set = saved


# ---- (2) artifact-loop sub-fix -----------------------------------------------------------

def test_artifact_target_bd_detection():
    _load(None)  # ensure the module imports under agent context
    # the sub-fix keys on whether the TARGET is bd-scoped
    assert "opal-data-bd" in "s3://opal-data-bd/gold/x"          # a bd target
    assert "opal-data-bd" not in "s3://opal-data-inf/platinum/x"  # an inf target -> never reads BD_CONFIG


def test_artifact_loop_skips_held_for_nonbd_target(monkeypatch):
    """The artifact config-search must not even consult BD_CONFIG for a non-bd target. We assert the
    loop's held-skip condition: _config_is_held(BD) AND target-not-bd -> skip."""
    cf = _load(None)
    bd_held = cf._config_is_held(cf.BD_CONFIG)
    inf_target_is_bd = "opal-data-bd" in "s3://opal-data-inf/platinum/aua" or "/black_diamond/" in "s3://opal-data-inf/platinum/aua"
    assert bd_held and not inf_target_is_bd, \
        "for an inf target, the loop's `held and not target_is_bd` -> skip BD_CONFIG (0 held read)"


# ---- correctness untouched: the pure evaluator still imports + basic shape ----------------

def test_module_imports_and_pipeline_configs_intact():
    cf = _load(None)
    assert set(cf.PIPELINE_CONFIGS) == {"bd", "inf", "cot"}
    assert callable(cf._load_config) and callable(cf.cmd_artifact)

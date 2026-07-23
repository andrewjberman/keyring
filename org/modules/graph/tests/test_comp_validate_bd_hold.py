"""comp-validate bd-config exclusion -- PREDICATE-BOUND contract (Law-8 fix, CVO~Z tick-26).

HISTORY: the 07-09 sovereign hold justified a DEFAULT bd-config skip; the hold was RETRACTED
07-14 ("verification here is DEMANDED") and the canonical predicate (sovereign_held.
SOVEREIGN_HELD_PATHS) correctly emptied -- but validate_cli's default consulted only the env
flag and this suite locked the HOLD-ERA behavior (one test even asserted is_held_path=True
against the retracted predicate, red since the split wave landed). The contract now under test:

  exclusion == is_held_path(<bd config>) AND NOT include_held(...)

  - RETRACTED (live today): bd config INCLUDED by default, no skip note, flag irrelevant.
  - RE-ARMED (simulated with the documented RETRACTED_* re-arm values): bd EXCLUDED by
    default (loud), env override re-includes (non-vacuous) -- the DS Rule-13 cycle preserved.

bd-SAFE: synthetic tmp configs only; the re-arm is a MONKEYPATCH of the predicate's marker
tuples, never a real re-hold. Original hold-era suite: 3.0.0_SA_CVO~B; this revision:
0.8.0_AE_CloudComp per tick-26.

# rail-checked: assurance oracle for comp-validate under test (NFRA_TOOLPASS sec.6)
"""

import importlib.util
import os
import tempfile
from contextlib import contextmanager
from pathlib import Path

_HERE = os.path.dirname(os.path.abspath(__file__))
_WS = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(_HERE))))
_MODULE = os.path.join(_WS, "org", "modules", "graph", "validate_cli.py")

_spec = importlib.util.spec_from_file_location("validate_cli_undertest", _MODULE)
vc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(vc)

# The canonical predicate module AS validate_cli binds it (is_held_path reads these globals at
# call time, so patching the tuples flips the predicate for every delegate).
import sys  # noqa: E402

sys.path.insert(0, _WS) if _WS not in sys.path else None
from org.modules.graph import sovereign_held as sh  # noqa: E402


@contextmanager
def _rearmed():
    """Simulate a LIVE hold using the documented re-arm values. Never touches real state."""
    saved = (sh.SOVEREIGN_HELD_PATHS, sh.SOVEREIGN_HELD_BUCKETS)
    sh.SOVEREIGN_HELD_PATHS = sh.RETRACTED_20260709_PATHS
    sh.SOVEREIGN_HELD_BUCKETS = sh.RETRACTED_20260709_BUCKETS
    try:
        yield
    finally:
        sh.SOVEREIGN_HELD_PATHS, sh.SOVEREIGN_HELD_BUCKETS = saved


def _synth_configs(tmp):
    # The bd synthetic nests under a data/black_diamond/ segment INSIDE tmp: still bd-safe
    # (never the real tree), but the path carries the shape the canonical predicate keys on
    # (substring markers) -- a bare tmp filename would silently bypass a re-armed hold and
    # make the exclusion tests vacuous.
    bd = Path(tmp) / "data" / "black_diamond" / "scripts" / "gold" / "gold_validate_config.yaml"
    bd.parent.mkdir(parents=True)
    inf = Path(tmp) / "inf_gold_validate_config.yaml"
    bd.write_text("scripts:\n  BD_ONLY_SENTINEL:\n    checks: []\n", encoding="utf-8")
    inf.write_text("scripts:\n  INF_ONLY_SENTINEL:\n    checks: []\n", encoding="utf-8")
    return bd, inf


def _run_load_raw(include_held_flag: bool):
    saved = (vc._BD_VALIDATE_CONFIG, vc._INF_VALIDATE_CONFIG, vc._bd_skip_noted)
    with tempfile.TemporaryDirectory() as d:
        bd, inf = _synth_configs(d)
        vc._BD_VALIDATE_CONFIG = bd
        vc._INF_VALIDATE_CONFIG = inf
        vc._bd_skip_noted = False
        if include_held_flag:
            os.environ["COMP_VALIDATE_INCLUDE_HELD"] = "1"
        else:
            os.environ.pop("COMP_VALIDATE_INCLUDE_HELD", None)
        try:
            result = vc._load_raw_validate_configs()
        finally:
            (vc._BD_VALIDATE_CONFIG, vc._INF_VALIDATE_CONFIG, vc._bd_skip_noted) = saved
            os.environ.pop("COMP_VALIDATE_INCLUDE_HELD", None)
    return result


# ---------------------------------------------------------- RETRACTED (live today)
def test_retracted_default_INCLUDES_bd():
    # Law-8: with the hold retracted, the tool must verify bd by default -- a skip here
    # is the tick-26 defect (an independent default asserting a retracted hold).
    result = _run_load_raw(include_held_flag=False)
    assert "BD_ONLY_SENTINEL" in result, \
        f"bd config EXCLUDED under a retracted hold (Law-8 regression): {list(result)}"
    assert "INF_ONLY_SENTINEL" in result


def test_retracted_no_skip_note_fires():
    vc._bd_skip_noted = False
    assert vc._bd_held_excluded() is False
    # _note_bd_held_skip is only reachable behind _bd_held_excluded; the flag proves no fire.
    assert vc._bd_skip_noted is False


def test_retracted_is_held_bd_path_is_False():
    # The --config bypass guard delegates to the canonical predicate: retracted -> not held.
    assert vc._is_held_bd_path("data/black_diamond/scripts/gold/gold_validate_config.yaml") is False


# ---------------------------------------------------------- RE-ARMED (simulated)
def test_rearmed_default_EXCLUDES_bd_and_inf_still_loads():
    with _rearmed():
        result = _run_load_raw(include_held_flag=False)
    assert "BD_ONLY_SENTINEL" not in result, \
        f"bd config READ under a LIVE (re-armed) hold -- guard failed: {list(result)}"
    assert "INF_ONLY_SENTINEL" in result, "a bd hold must never break inf"


def test_rearmed_override_reincludes_bd_nonvacuous():
    with _rearmed():
        result = _run_load_raw(include_held_flag=True)
    assert "BD_ONLY_SENTINEL" in result, \
        "COMP_VALIDATE_INCLUDE_HELD=1 must re-read the bd config under a live hold (Rule 13 cycle)"


def test_rearmed_is_held_bd_path_catches_explicit_config_hole():
    # The --config bypass stays closed UNDER A LIVE HOLD; in-scope pipelines never caught.
    with _rearmed():
        assert vc._is_held_bd_path("data/black_diamond/scripts/gold/gold_validate_config.yaml") is True
        assert vc._is_held_bd_path(r"data\black_diamond\scripts\gold\gold_validate_config.yaml") is True
        assert vc._is_held_bd_path("data/canonical/schwab/silver/build_dim.yaml") is True
        assert vc._is_held_bd_path("data/inf/scripts/gold/gold_validate_config.yaml") is False
        assert vc._is_held_bd_path("data/cot/scripts/gold/gold_validate_config.yaml") is False


def test_rearm_simulation_is_discriminating():
    # The simulation itself must flip the predicate (a control that cannot fail is not a control).
    assert sh.is_held_path("data/black_diamond/x.py") is False
    with _rearmed():
        assert sh.is_held_path("data/black_diamond/x.py") is True
    assert sh.is_held_path("data/black_diamond/x.py") is False

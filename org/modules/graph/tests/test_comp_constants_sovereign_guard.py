#!/usr/bin/env python3
"""CC2 sovereign-held-surface guard tests for comp-constants (NFRA_TOOLPASS).

comp-constants ast-parses EVERY file in EVERY search_surface on a full run (bare
`check`, `--lane`, `new`, `index`). `--lane` scopes the COMPARISON (cmd_check
filters constants by lane), NEVER the SCAN -- scan_all(only_file=None) globs+parses
all surfaces. So a config whose search_surfaces name a sovereign-held path
(data/black_diamond/, ...) turns the tool into a latent bd-scanner for ANY caller.
The CC2 guard makes the hold STRUCTURAL: it REFUSES (exit 3) any such invocation
BEFORE it scans, and refuses `check --file <held path>`; `check --file <non-held>`
stays allowed; `--allow-held-scan` overrides (loud + audited).

SAFETY: every fixture uses a NON-EXISTENT held path (cc2_nonexistent/data/black_diamond/...).
The guard fires on the config PATTERN STRING before any glob, so these tests never
touch the real data/black_diamond tree -- asserted by test_fixtures_never_hit_real_bd.
"""
from __future__ import annotations

import subprocess
import sys
import textwrap
from pathlib import Path

import pytest

_CLI = Path(__file__).resolve().parents[1] / "comp_constants_cli.py"
_SRC = _CLI.read_text(encoding="utf-8")

# The fixture config DECLARES the hold via `sovereign_held_markers:`. Before the 2026-07-14 retraction
# these tests leaned on the module's live marker tuple; that coupled the MECHANISM tests to a specific
# live PROHIBITION, so the suite would have failed the retraction and re-argued a hold Andrew had already
# lifted. Declaring the markers in the fixture tests the machinery WITHOUT asserting any live hold --
# and doubles as the re-arm proof: this is exactly how a future hold is declared.
_HELD_CONFIG = textwrap.dedent("""\
    sovereign_held_markers:
    - data/black_diamond/
    - schwab/silver/
    - opal-data-bd
    - opal-data-schwab
    search_surfaces:
      bd:
      - cc2_nonexistent/data/black_diamond/scripts/**/*.py
      inf:
      - cc2_nonexistent/inf/**/*.py
    constants:
    - name: FIXTURE_CONST
      lane: inf
      canonical_value: "'x'"
    """)


def _run(cfg: Path, *args) -> tuple[int, str, str]:
    r = subprocess.run([sys.executable, str(_CLI), "--config", str(cfg), *args],
                       capture_output=True, text=True, timeout=60)
    return r.returncode, r.stdout, r.stderr


@pytest.fixture
def held_cfg(tmp_path) -> Path:
    cfg = tmp_path / "held.yaml"
    cfg.write_text(_HELD_CONFIG, encoding="utf-8")
    return cfg


# ---- STATIC: the guard exists and is wired ---------------------------------

def test_live_default_is_RETRACTED_not_enforcing():
    """The 2026-07-09 49F/Schwab/bd hold was LIFTED COMPLETELY by Andrew on 2026-07-14. This test
    REPLACED one that asserted those markers were PRESENT -- i.e. a test that would have failed the
    retraction and re-argued a prohibition the sovereign had already withdrawn. A control must not
    outlive the rule it enforces, and must never resist its own removal."""
    from org.modules.graph.comp_constants_cli import SOVEREIGN_HELD_MARKERS
    assert SOVEREIGN_HELD_MARKERS == (), (
        "the 2026-07-09 hold is RETRACTED; comp-constants must enforce no markers by default")


def test_retracted_markers_are_RETAINED_so_the_guard_can_be_re_armed():
    """A guard you cannot re-arm is not a fix, it is a removal. The lifted set stays in source so a
    future hold is a one-line re-point, not a rebuild."""
    from org.modules.graph.comp_constants_cli import _RETRACTED_20260709_MARKERS
    for marker in ("data/black_diamond/", "schwab/silver/", "opal-data-bd", "opal-data-schwab"):
        assert marker in _RETRACTED_20260709_MARKERS, f"re-arm set must retain {marker!r}"


def test_guard_MECHANISM_still_fires_when_a_hold_is_declared(held_cfg):
    """The machinery is intact: declare markers and the guard refuses exactly as before. This is the
    property the retired assertion was really protecting -- separated from any live prohibition."""
    rc, _out, err = _run(held_cfg, "check")
    assert rc == 3 and "SOVEREIGN-HELD" in err, "a DECLARED hold must still REFUSE (exit 3)"


def test_no_hold_declared_means_no_refusal(tmp_path):
    """The negative control the old suite never had: with no declared markers, a config naming a
    formerly-held surface must NOT refuse. Without this, 'the guard is off' was untested."""
    cfg = tmp_path / "unheld.yaml"
    cfg.write_text(textwrap.dedent("""\
        search_surfaces:
          bd:
          - cc2_nonexistent/data/black_diamond/scripts/**/*.py
        constants:
        - name: FIXTURE_CONST
          lane: bd
          canonical_value: "'x'"
        """), encoding="utf-8")
    rc, _out, err = _run(cfg, "check")
    assert rc != 3, f"no declared hold must not REFUSE; got rc={rc} err={err!r}"
    assert "SOVEREIGN-HELD" not in err


def test_guard_is_called_in_main_before_dispatch():
    assert "_sovereign_guard(args, config)" in _SRC, "main() must call _sovereign_guard before args.func"


# ---- DYNAMIC: full-scan modes REFUSE on a held config ----------------------

@pytest.mark.parametrize("mode", [["check"], ["check", "--lane", "inf"], ["new"], ["index"]])
def test_full_scan_modes_refuse_on_held_config(held_cfg, mode):
    rc, out, err = _run(held_cfg, *mode)
    assert rc == 3, f"{mode} must REFUSE (exit 3) on a held-surface config; got rc={rc} out={out!r} err={err!r}"
    assert "SOVEREIGN-HELD" in err, f"{mode} refusal must name SOVEREIGN-HELD"
    assert "data/black_diamond/" in err, f"{mode} refusal must name the held surface"


def test_lane_flag_is_not_a_scan_scoper(held_cfg):
    """The footgun that tripped the original breach: --lane LOOKS like it scopes to
    inf, but it scopes the COMPARISON -- the scan still globs bd. The guard refuses it."""
    rc, _out, err = _run(held_cfg, "check", "--lane", "inf")
    assert rc == 3 and "SOVEREIGN-HELD" in err


def test_index_refuses_before_mutating_config(held_cfg):
    """index rewrites the config; the guard must refuse BEFORE it runs, leaving the config intact."""
    before = held_cfg.read_text(encoding="utf-8")
    rc, _out, err = _run(held_cfg, "index")
    assert rc == 3 and "SOVEREIGN-HELD" in err
    assert held_cfg.read_text(encoding="utf-8") == before, "index must not mutate the config when refused"


# ---- DYNAMIC: check --file behavior ----------------------------------------

def test_check_file_non_held_is_allowed(held_cfg, tmp_path):
    f = tmp_path / "safe_const.py"
    f.write_text("FIXTURE_CONST = 'x'\n", encoding="utf-8")
    rc, _out, err = _run(held_cfg, "check", "--file", str(f))
    assert rc != 3, "check --file <non-held> must NOT be refused"
    assert "SOVEREIGN-HELD" not in err


def test_check_file_under_held_path_refuses(held_cfg):
    rc, _out, err = _run(held_cfg, "check", "--file", "some/data/black_diamond/scripts/x.py")
    assert rc == 3, "check --file <held path> must REFUSE"
    assert "SOVEREIGN-HELD" in err and "data/black_diamond/" in err


# ---- DYNAMIC: the audited override -----------------------------------------

def test_allow_held_scan_overrides_with_a_loud_warn(held_cfg):
    """--allow-held-scan bypasses the guard (audited). The held pattern is non-existent
    so this globs nothing real -- it must WARN loudly and NOT refuse."""
    rc, _out, err = _run(held_cfg, "--allow-held-scan", "check")
    assert rc != 3, "override must not be refused"
    assert "OVERRIDE" in err and "--allow-held-scan" in err, "override must WARN loudly (the audit signal)"


# ---- SAFETY: the tests themselves never trigger a real bd scan -------------

def test_fixtures_never_hit_real_bd():
    """Guard-rail on the guard's OWN tests: no fixture pattern may glob the repo's real
    data/black_diamond tree.

    SHARPENED 2026-07-22: this asserted on raw config LINES, which cannot tell a glob PATTERN
    (globbed -> touches the filesystem) from a `sovereign_held_markers:` entry (an inert substring
    the guard string-matches, never globbed). It fired on the marker declaration added with the
    retraction. Parsing the YAML and asserting on search_surfaces -- the only key whose values are
    ever globbed -- is STRICTLY STRONGER than the prefix heuristic it replaces: it now checks EVERY
    surface pattern, not just lines that happen to mention black_diamond."""
    import yaml
    cfg = yaml.safe_load(_HELD_CONFIG)
    patterns = [p for pats in (cfg.get("search_surfaces") or {}).values() for p in (pats or [])]
    assert patterns, "fixture must declare search_surfaces or this test asserts nothing"
    assert any("data/black_diamond/" in p for p in patterns), \
        "fixture must still exercise a held-looking surface, else the guard test is vacuous"
    for p in patterns:
        assert p.startswith("cc2_nonexistent/"), \
            f"every fixture GLOB pattern must be the non-existent sentinel, got {p!r}"
    # The markers block is inert by construction: _held_surface_hits() string-matches it against the
    # patterns above and never globs it. Assert it is not mistaken for a surface.
    assert "data/black_diamond/" not in patterns

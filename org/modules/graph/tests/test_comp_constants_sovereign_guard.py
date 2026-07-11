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

_HELD_CONFIG = textwrap.dedent("""\
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

def test_markers_cover_the_sovereign_held_paths():
    # C7 consolidation: the marker literals moved out of this module's SOURCE into the canonical leaf
    # (sovereign_held); comp_constants now DERIVES SOVEREIGN_HELD_MARKERS from it. Check the RUNTIME tuple.
    from org.modules.graph.comp_constants_cli import SOVEREIGN_HELD_MARKERS
    for marker in ("data/black_diamond/", "schwab/silver/", "opal-data-bd", "opal-data-schwab"):
        assert marker in SOVEREIGN_HELD_MARKERS, f"SOVEREIGN_HELD_MARKERS must include {marker!r}"


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
    """Guard-rail on the guard's OWN tests: the held pattern is the non-existent fixture
    sentinel, never the repo's real data/black_diamond tree."""
    assert "cc2_nonexistent/data/black_diamond/" in _HELD_CONFIG
    for line in _HELD_CONFIG.splitlines():
        stripped = line.strip()
        if "data/black_diamond/" in stripped:
            assert stripped.startswith("- cc2_nonexistent/"), \
                f"a held fixture pattern must be the non-existent sentinel, got {stripped!r}"

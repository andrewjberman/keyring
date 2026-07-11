#!/usr/bin/env python3
"""comp-shell standing discrimination test: bare forbidden util -> ERROR, guarded -> WARN.

Author: 3.0.0_SA_CVO~A. NFRA_TOOLPASS comp-shell (CTO GO 20260710T235231Z).

comp-shell (Rule 16) flags Git Bash 3.6.7-missing utilities (pgrep/pkill/flock/pidof/setsid/
wget) in local-runtime shell scripts. The LOAD-BEARING semantic is the WARN/ERROR discriminator
(guard-awareness): a BARE forbidden util is an ERROR (rc=1, blocks); a GUARDED one
(`command -v <util>` / `which <util>` before the call) is a WARN (rc=0). A regression that
classified BARE-as-WARN would SILENTLY DEFEAT Rule 16; one that classified GUARDED-as-ERROR
would flood noise. The tool front-passed CLEAN + was proven non-vacuous in scratch, but had NO
committed test of the discrimination -- this is the standing guard.

bd-CLEAN: synthetic .sh fixtures in pytest tmp_path; the --all exemption is exercised by pointing
a synthetic _WORKSPACE at tmp_path. This test NEVER scans a real data/black_diamond file. It
imports the module directly (no CLI subprocess -> no pytest.ini bd-pythonpath landmine).

NOTE recorded for CTO (not this test's concern): _is_exempt(data/) is applied in --all mode
(_collect_sh_files:247) but NOT to an EXPLICIT file arg (:251-261) -- so `scan data/x.sh` would
read a bd .sh. Per CTO that is a deliberate user Read-equivalent, not auto-reading; default/--all
is bd-safe. Flagged, not fixed here.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

_GRAPH = Path(__file__).resolve().parents[4] / "org" / "modules" / "graph"
sys.path.insert(0, str(_GRAPH))


def _load():
    spec = importlib.util.spec_from_file_location("shell_cli_sut", _GRAPH / "shell_cli.py")
    m = importlib.util.module_from_spec(spec)
    sys.modules["shell_cli_sut"] = m
    spec.loader.exec_module(m)
    return m


M = _load()
_UTILS = sorted(M.FORBIDDEN)   # pgrep, pkill, flock, pidof, setsid, wget


def _sevs(findings, util):
    return {f["severity"] for f in findings if f["utility"] == util}


@pytest.mark.parametrize("util", _UTILS)
def test_bare_forbidden_util_is_error(util, tmp_path):
    """A BARE forbidden util -> ERROR (never WARN). Misclassifying bare-as-WARN silently defeats Rule 16."""
    p = tmp_path / "bare.sh"
    p.write_text(f"#!/bin/bash\n{util} --do-something arg\n", encoding="utf-8")
    sevs = _sevs(M.scan_file(p), util)
    assert "ERROR" in sevs, f"bare `{util}` was not flagged ERROR (sevs={sevs}) -- Rule 16 defeated"
    assert "WARN" not in sevs, f"bare `{util}` misclassified as WARN (sevs={sevs}) -- the dangerous direction"


@pytest.mark.parametrize("util", _UTILS)
def test_guarded_util_is_warn_not_error(util, tmp_path):
    """A GUARDED forbidden util (command -v guard in the lookback) -> WARN, NOT ERROR.
    Misclassifying guarded-as-ERROR floods noise and gets the gate ignored."""
    p = tmp_path / "guarded.sh"
    p.write_text(
        f"#!/bin/bash\nif command -v {util} >/dev/null 2>&1; then\n    {util} --do-something arg\nfi\n",
        encoding="utf-8")
    sevs = _sevs(M.scan_file(p), util)
    assert "WARN" in sevs, f"guarded `{util}` produced no WARN (sevs={sevs})"
    assert "ERROR" not in sevs, f"guarded `{util}` misclassified as ERROR (sevs={sevs}) -- noise flood"


def test_which_guard_also_counts(tmp_path):
    """The other accepted guard form: `which <util>` before the call -> WARN not ERROR."""
    p = tmp_path / "which_guard.sh"
    p.write_text("#!/bin/bash\nwhich pgrep >/dev/null 2>&1 && pgrep -f x\n", encoding="utf-8")
    assert _sevs(M.scan_file(p), "pgrep") == {"WARN"}, "a `which` guard must also downgrade to WARN"


def test_clean_script_has_no_findings(tmp_path):
    """NEGATIVE CONTROL: a script with no forbidden utils yields nothing (no false ERROR)."""
    p = tmp_path / "clean.sh"
    p.write_text("#!/bin/bash\nps -ef | awk '{print $2}'\necho hello\n", encoding="utf-8")
    assert M.scan_file(p) == [], "a clean script produced spurious findings"


def test_scan_all_exempts_the_data_prefix(tmp_path, monkeypatch):
    """--all must SKIP data/ (Rule 16 EC2/data-pipeline exemption -- the bd-safety property):
    a bare-forbidden .sh under data/ is NOT collected, while one under org/mcp/ IS."""
    monkeypatch.setattr(M, "_WORKSPACE", tmp_path)
    (tmp_path / "data" / "black_diamond" / "scripts").mkdir(parents=True)
    (tmp_path / "org" / "mcp").mkdir(parents=True)
    (tmp_path / "data" / "black_diamond" / "scripts" / "held.sh").write_text("#!/bin/bash\nwget x\n", encoding="utf-8")
    (tmp_path / "org" / "mcp" / "local.sh").write_text("#!/bin/bash\nwget x\n", encoding="utf-8")
    collected = {str(p.relative_to(tmp_path)).replace("\\", "/") for p in M._collect_sh_files([], all_mode=True)}
    assert "org/mcp/local.sh" in collected, "an in-scope local .sh must be scanned by --all"
    assert "data/black_diamond/scripts/held.sh" not in collected, (
        "SOVEREIGN: a data/ .sh was collected by --all -- the Rule-16 data/ exemption failed"
    )
    assert M._is_exempt(tmp_path / "data" / "black_diamond" / "x.sh") is True
    assert M._is_exempt(tmp_path / "org" / "mcp" / "x.sh") is False

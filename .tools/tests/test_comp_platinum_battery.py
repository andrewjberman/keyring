"""T-24 controls for comp-platinum's answer states and one shared Rule-T carrier."""
from __future__ import annotations

import pathlib
import subprocess
import sys


ROOT = pathlib.Path(__file__).resolve().parents[2]
ENGINE = ROOT / "org" / "modules" / "graph" / "platinum_cli.py"


def run(*args):
    return subprocess.run([sys.executable, str(ENGINE), *args], cwd=ROOT,
                          text=True, capture_output=True, timeout=30)


def test_absent_component_is_a_distinct_answer_state():
    result = run("page", "T24_ABSENT_COMPONENT_93999", "--budget", "0")
    assert result.returncode == 1
    assert "ANSWER-STATE: SUBJECT_ABSENT_FROM_CORPUS" in result.stdout


def test_tiny_budget_carries_partial_upward_not_no_script():
    result = run("page", "FactorTilts", "--budget", "0.000001")
    assert result.returncode == 0
    assert "BUDGET REACHED" in result.stdout
    assert "ANSWER-STATE: PARTIAL_OR_BLIND" in result.stdout
    assert "no-script is not inferred" in result.stdout


def test_complete_page_prints_shared_budget_denominator():
    result = run("page", "FactorTilts", "--budget", "0")
    assert result.returncode == 0
    assert "WITHIN BUDGET: scanned 3 of 3 component" in result.stdout
    assert "DEFERRED: 0 of 3 component" in result.stdout


if __name__ == "__main__":
    raise SystemExit(__import__("pytest").main([__file__, "-q"]))

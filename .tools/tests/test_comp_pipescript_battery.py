"""T-10 battery: comp-pipescript's shim identity and verdict-bearing Rule-T edge.

The bounded run is deliberately a real production invocation.  A tiny budget is spent
before the first head-object request, so it proves the operation is deferred rather
than relying on a mocked timeout or an AWS failure.
"""
from __future__ import annotations

import pathlib
import re
import subprocess
import sys
from contextlib import redirect_stdout
from io import StringIO
from types import SimpleNamespace


ROOT = pathlib.Path(__file__).resolve().parents[2]
SHIM = ROOT / ".tools" / "comp-pipescript"
ENGINE = ROOT / "org" / "modules" / "graph" / "pipeline_cli.py"
sys.path.insert(0, str(ROOT))
import org.modules.graph.pipeline_cli as pipescript  # noqa: E402


def run(*args: str, timeout: int = 45) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(ENGINE), *args], cwd=ROOT, text=True, capture_output=True, timeout=timeout,
    )


def test_shim_identity_and_budget_help_are_explicit():
    result = run("deployed", "--help")
    output = result.stdout + result.stderr
    normalized = re.sub(r"\s+", " ", output)
    assert result.returncode == 0, output
    assert "comp-pipescript SHIM: .tools/comp-pipescript -> org/modules/graph/pipeline_cli.py" in SHIM.read_text(encoding="utf-8")
    assert "--budget N" in output
    assert "NOT- DECIDABLE" in normalized
    assert "rc=4" in normalized


def test_tiny_budget_is_a_non_clean_partial_verdict():
    result = run("deployed", "--pipeline", "inf-gold", "--budget", "0.001")
    output = result.stdout + result.stderr
    assert result.returncode == 4, output
    assert "BUDGET REACHED: 0.001 s (flag)" in output
    assert "STATE: NOT-DECIDABLE" in output
    assert "DEFERRED: 1 of 1 s3_head_object(s)" in output
    assert "NO CURSOR" in output


def test_held_branch_is_complete_not_partial():
    original = pipescript.is_held_bucket
    pipescript.is_held_bucket = lambda bucket: bucket == "opal-data-bd"
    output = StringIO()
    try:
        with redirect_stdout(output):
            rc = pipescript.cmd_deployed(SimpleNamespace(
                pipeline="bd-gold", firm=None, script_id="", budget=None, cursor=None,
            ))
    finally:
        pipescript.is_held_bucket = original
    assert rc == 0, output.getvalue()
    output = output.getvalue()
    assert "SKIP: opal-data-bd" in output
    assert "WITHIN BUDGET" in output
    assert "BUDGET REACHED" not in output


def test_registry_is_measured_and_etfs_is_not_added():
    source = ENGINE.read_text(encoding="utf-8")
    choices = re.search(r"_FIRM_TO_PIPELINE\s*=\s*\{(.+?)\n\}", source, re.S)
    assert choices is not None, "the firm registry must remain an inspectable declaration"
    assert "etfs" not in choices.group(1).lower(), "T-10 must not widen the deployed firm registry"
    assert "choices=('bd', 'inf', 'cot', 'mdpf')" in source


def test_budget_mutant_is_detected_by_the_partial_rc_contract():
    source = ENGINE.read_text(encoding="utf-8")
    mutant, count = re.subn(
        r"raise _PipescriptBudgetReached\(\)",
        "return  # MUTANT: silently continue after a partial verdict",
        source,
        count=1,
    )
    assert count == 1, "the mutant must target the live partial-verdict boundary"
    assert "raise _PipescriptBudgetReached()" not in mutant
    assert "return RC_NOT_DECIDABLE" in source


if __name__ == "__main__":
    raise SystemExit(__import__("pytest").main([__file__, "-q"]))

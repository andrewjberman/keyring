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
import types
from contextlib import redirect_stdout
from hashlib import md5
from io import StringIO
from types import SimpleNamespace
from unittest.mock import patch


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
    assert "ANSWER-STATE: PARTIAL_OR_BLIND" in output
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
    assert "ANSWER-STATE: NOT_APPLICABLE" in output
    assert "WITHIN BUDGET" in output
    assert "BUDGET REACHED" not in output


def test_deployed_planted_absent_and_present_zero_states_are_distinct():
    """Exercise both complete answer-state branches without letting AWS decide the test."""
    dag = pipescript._build_dag("inf-gold")
    script_id, script = next(
        item for item in sorted(dag.scripts.items(), key=lambda item: item[1].run_order)
        if item[0] == "INF_API_PULL_TXN"
    )
    etag = md5((ROOT / script.file_path).read_bytes()).hexdigest()

    def fake_aws(argv, **_kwargs):
        if "head-object" in argv:
            return SimpleNamespace(returncode=0, stdout='"%s"\n' % etag, stderr="")
        return SimpleNamespace(returncode=0, stdout="", stderr="")

    def invoke(script_filter: str):
        output = StringIO()
        with patch("shutil.which", return_value="aws"), patch("subprocess.run", side_effect=fake_aws), \
             redirect_stdout(output):
            rc = pipescript.cmd_deployed(SimpleNamespace(
                pipeline="inf-gold", firm=None, script_id=script_filter, budget="0", cursor=None,
            ))
        return rc, output.getvalue()

    absent_rc, absent = invoke("T10_ABSENT_SPECIMEN_93999")
    present_rc, present = invoke(script_id)
    assert absent_rc == 0, absent
    assert present_rc == 0, present
    assert "ANSWER-STATE: SUBJECT_ABSENT_FROM_CORPUS" in absent
    assert "ANSWER-STATE: PRESENT_WITH_ZERO_RESULTS" in present
    assert "SUBJECT_ABSENT_FROM_CORPUS" not in present
    assert "PRESENT_WITH_ZERO_RESULTS" not in absent


def test_registry_is_measured_and_etfs_is_not_added():
    source = ENGINE.read_text(encoding="utf-8")
    choices = re.search(r"_FIRM_TO_PIPELINE\s*=\s*\{(.+?)\n\}", source, re.S)
    assert choices is not None, "the firm registry must remain an inspectable declaration"
    assert "etfs" not in choices.group(1).lower(), "T-10 must not widen the deployed firm registry"
    assert "choices=('bd', 'inf', 'cot', 'mdpf')" in source


def test_verdict_rc_mutant_returns_clean_at_expiry_and_is_detected():
    """Run a planted FWD-10 violation, rather than merely inspecting its text.

    The mutant shares the production module's ``__file__`` so its workspace
    calculation and imports remain real.  Its tiny-budget invocation reaches
    the same deferred head-object boundary as the production control, but the
    mutated public boundary returns clean rc=0.  That is the RED condition this
    test suite is required to catch.
    """
    source = ENGINE.read_text(encoding="utf-8")
    mutant, count = re.subn(
        r"except _PipescriptBudgetReached:\n        return RC_NOT_DECIDABLE",
        "except _PipescriptBudgetReached:\n        return 0  # MUTANT: FWD-10 clean partial",
        source,
        count=1,
    )
    assert count == 1, "the mutant must target the live verdict-bearing boundary"

    module = types.ModuleType("pipescript_t10_fwd10_mutant")
    module.__file__ = str(ENGINE)
    exec(compile(mutant, str(ENGINE), "exec"), module.__dict__)
    output = StringIO()
    with redirect_stdout(output):
        mutant_rc = module.cmd_deployed(SimpleNamespace(
            pipeline="inf-gold", firm=None, script_id="", budget="0.001", cursor=None,
        ))
    assert "BUDGET REACHED: 0.001 s (flag)" in output.getvalue()
    assert mutant_rc == 0, (
        "the planted FWD-10 violation must be observably RED (clean rc from a partial run); "
        "if this fails, the test no longer proves the production rc=4 contract"
    )


if __name__ == "__main__":
    raise SystemExit(__import__("pytest").main([__file__, "-q"]))

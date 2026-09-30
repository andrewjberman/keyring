"""R23 ~Y cell IB-yr-231 check: the resident NAMES the eviction it saw, and names a job's terminal ATTENTION.

Why (row IRPT_BCKEND-S218, CTO 102967 as amended at 102970). W24 returned zero reports: both jobs that reached the
vendor died ATTENTION SESSION_REFRESH_ALREADY_USED. That code does not mean a stale session --
resident_worker.refresh_session() is reachable only from step() on an eviction_verdict, so it means the job was
EVICTED TWICE, the first eviction spending the one admitted refresh. Which verdict matched is recorded nowhere: not
in the irpt-jobs row, and not in the journal (row IRPT_BCKEND-S207, re-confirmed across W24's 124 journal lines).
The CTO amended its own decision on that reading: observe first, discriminate second, remedy third. This cell is the
observation, and it changes no behaviour.

Run from the repo root:
    python -m pytest -q -p no:cacheprovider org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/R23_CHECKS/test_r23_y1_eviction_named.py::<test>

- names_the_matched_verdict: on an eviction, stdout carries a line naming the matched verdict AND the job id. At the
  base nothing names it, so an operator reading the journal cannot tell a pre-job session rejection from a per-call
  eviction. FAILS at the base.
- names_the_job_attention:   a job that ends ATTENTION prints its job_detail code. At the base the code reaches only
  the irpt-jobs row (S207). FAILS at the base.
- no_behaviour_change:       the CONTROL. One eviction still recovers and reaches READY; two still end ATTENTION
  SESSION_REFRESH_ALREADY_USED with no downloads. The one-refresh allowance does not move in any branch (CTO 102970).
  PASSES at the base and must keep passing.
"""
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

ROOT = Path(__file__).resolve().parents[6]
GEN = ROOT / "infra/aws/lambda/investor-reporting/ycharts/generate"
sys.path[:0] = [str(GEN / "tests"), str(GEN)]

import test_resident_worker as base  # noqa: E402  (the suite's world/installed fixtures and replay script)

world = base.world
retention_world = base.retention_world

EVICTED = {"status": 403, "content_type": "text/html",
           "body": "You have been signed out due to a concurrent sign in using your credentials"}
ROUTE = ("GET", "/model_portfolios/2332060/status")


def _run(world, monkeypatch, capsys, second_eviction):
    """Drive one job whose vendor read is evicted once or twice; return (result, stdout).

    Driven exactly as the suite's own eviction test does (test_resident_worker.py:243-262): the session capture is
    replaced so the refresh advances generation and fence offline, and the run goes through assembly.execute.
    """
    r = base.installed(world, monkeypatch)
    valid = r.replay.script[ROUTE][0]
    r.replay.script[ROUTE] = [EVICTED, EVICTED if second_eviction else valid]

    def capture():
        r.bundle.update(generation="offline-fresh-session", fence=2)

    r.assembly.session.capture_workflow = SimpleNamespace(capture=capture)
    result = r.assembly.execute(r.message, lambda: None)
    return result, capsys.readouterr().out


def test_names_the_matched_verdict(world, monkeypatch, capsys):
    """An eviction is journalled with the verdict that matched and the job id."""
    result, out = _run(world, monkeypatch, capsys, second_eviction=False)
    lines = [ln for ln in out.splitlines() if "IRPT_RESIDENT_EVICTION" in ln]
    assert lines, ("no IRPT_RESIDENT_EVICTION line was printed; an operator reading the journal cannot tell which "
                   "eviction_verdict matched. stdout was:\n" + out)
    line = lines[0]
    assert "verdict=" in line, "the eviction line must NAME the matched verdict: " + line
    assert "job=" in line, "the eviction line must carry the job id: " + line
    # the payload is a verdict name and a job id, never vendor material
    for forbidden in ("Cookie", "cookie", "Set-Cookie", "http", "credentials"):
        assert forbidden not in line, "the eviction line must not carry vendor material: " + line


def test_names_the_job_attention(world, monkeypatch, capsys):
    """A job that ends ATTENTION prints its job_detail code, so the journal alone explains the stop."""
    result, out = _run(world, monkeypatch, capsys, second_eviction=True)
    assert result["state"] == "ATTENTION"
    assert result["detail"]["code"] == "SESSION_REFRESH_ALREADY_USED"
    lines = [ln for ln in out.splitlines() if "IRPT_RESIDENT_ATTENTION" in ln]
    assert lines, ("no IRPT_RESIDENT_ATTENTION line was printed; the code reaches only the irpt-jobs row, which is "
                   "row IRPT_BCKEND-S207. stdout was:\n" + out)
    assert "SESSION_REFRESH_ALREADY_USED" in lines[0], "the ATTENTION line must carry the code: " + lines[0]


@pytest.mark.parametrize("second_eviction", [False, True])
def test_no_behaviour_change(world, monkeypatch, capsys, second_eviction):
    """CONTROL: the allowance and the outcomes are exactly what they were (CTO 102970 -- one refresh, unchanged)."""
    result, _out = _run(world, monkeypatch, capsys, second_eviction)
    assert result["state"] == ("ATTENTION" if second_eviction else "READY")
    if second_eviction:
        assert result["detail"]["code"] == "SESSION_REFRESH_ALREADY_USED"

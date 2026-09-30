"""R19 ~Y cell IB-yr-1 check: the saved portfolio's type refuses a tolerated setting BEFORE the vendor generates.

Run from the repo root:
    python -m pytest -q org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/R19_CHECKS/test_r19_y1_pregen_static.py

Arms (the harness is ycharts/generate/tests/test_resident_worker.py's, unchanged):
- NOT_FIXED: saved read says model_portfolio_type="dynamic" with level_as_of_type tolerated -> ATTENTION
  TOLERANCE_REQUIRES_STATIC, and NO report generation POST and NO PDF download (the new, earlier refusal).
- FIXED: saved read says "fixed" -> the existing printed-type check still decides (Static prints -> READY).
- ABSENT: saved read carries no model_portfolio_type -> the existing printed-type check still decides (READY on Static).
FIXED and ABSENT are the controls and pass at the base; NOT_FIXED fails at the base (the vendor generates first).
"""
import json
import sys
from pathlib import Path

GEN = Path(__file__).resolve().parents[6] / "infra/aws/lambda/investor-reporting/ycharts/generate"
sys.path[:0] = [str(GEN / "tests"), str(GEN)]

import pytest  # noqa: E402

import test_resident_worker as harness  # noqa: E402  (first: it sets the suite's sys.path)
import resident_worker  # noqa: E402

installed = harness.installed
retention_world, world = harness.retention_world, harness.world

SAVED = ("GET", "/model_portfolios/fixed/2332060")


def _generate_posts(r):
    return [c for c in r.replay.sent_headers
            if c["method"] == "POST" and c["route"].startswith("/custom_pdf_reports/")
            and not c["route"].startswith("/custom_pdf_reports/validate_report_securities/")]


def _run(world, monkeypatch, saved_type):
    r = installed(world, monkeypatch)
    portfolio = r.replay.script[SAVED][0]["body"]["portfolio"]
    portfolio["level_as_of_type"] = "custom_date"
    if saved_type is None:
        portfolio.pop("model_portfolio_type", None)
    else:
        portfolio["model_portfolio_type"] = saved_type
    monkeypatch.setattr(resident_worker.extract, "calculation_settings",
                        lambda data, name: {"type": "Static", "as_of": "Custom"})
    return r, r.assembly.execute(r.message, lambda: None)


def test_not_fixed_refuses_before_generation(world, monkeypatch):
    r, result = _run(world, monkeypatch, "dynamic")
    assert result["state"] == "ATTENTION"
    assert "TOLERANCE_REQUIRES_STATIC" in json.dumps(r.row)
    assert _generate_posts(r) == [] and r.downloads == []
    assert "checkpoint_pdf" not in r.row and not r.transactions


@pytest.mark.parametrize("saved_type", ["fixed", None])
def test_fixed_or_absent_defers_to_the_printed_type(world, monkeypatch, saved_type):
    r, result = _run(world, monkeypatch, saved_type)
    assert result["state"] == "READY"
    assert len(_generate_posts(r)) == 1 and len(r.downloads) == 1 and len(r.transactions) == 1

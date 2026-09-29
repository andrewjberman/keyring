"""R20 ~Y cell IB-yr-201 check: a Comparison names its compared models to the vendor, and a Comparison PDF that prints
none of them is refused before retention (rows S194, S196).

Run from the repo root:
    python -m pytest -q -p no:cacheprovider org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/R20_CHECKS/test_r20_y1_comparison.py -k <arm>

Arms:
- ids:     recipe.report_security_ids(model_portfolio_id, comparisons, template) returns [primary] + each comparison's
           vendor_id, refuses a count the template does not take, and refuses a duplicate id (the research builder's
           rule, docs/research/investor_reporting_ycharts_variants_20260911/recipe_contract.py:211-218).
- wiring:  the resident calls report_security_ids once per generation and sends its result to validate and generate
           (spied on the harness's Overview run, whose comparisons are empty).
- printed: resident_worker.missing_comparisons(pdf_bytes, comparisons) lists the chosen names a PDF does NOT print:
           [] on the synthetic comparison.pdf (prints 'Opal Long-Term'), ['Opal Long-Term'] on overview.pdf.
All three fail at the base (neither function exists).
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
GEN = ROOT / "infra/aws/lambda/investor-reporting/ycharts/generate"
PDFS = ROOT / "infra/aws/lambda/investor-reporting/ycharts/extract/fixtures/synthetic_pdf"
sys.path[:0] = [str(GEN / "tests"), str(GEN)]

import pytest  # noqa: E402

import test_resident_worker as harness  # noqa: E402  (first: it sets the suite's sys.path)
import recipe  # noqa: E402
import resident_worker  # noqa: E402

installed = harness.installed
retention_world, world = harness.retention_world, harness.world

LONG = {"vendor_id": "P:1728413", "name": "Opal Long-Term"}
SHORT = {"vendor_id": "P:1728415", "name": "Opal Short-Term"}


def _template(variant, lo, hi):
    return {"template_id": "t", "variant": variant, "comparison_securities": {"min": lo, "max": hi}}


def test_ids_primary_then_comparisons_with_the_template_count():
    assert recipe.report_security_ids(2366779, [LONG], _template("COMPARISON", 1, 1)) == ["P:2366779", "P:1728413"]
    assert recipe.report_security_ids(7, [LONG, SHORT], _template("MULTI", 2, 5)) == ["P:7", "P:1728413", "P:1728415"]
    assert recipe.report_security_ids(7, [], _template("OVERVIEW", 0, 0)) == ["P:7"]
    with pytest.raises(recipe.RecipeRefused):
        recipe.report_security_ids(7, [], _template("COMPARISON", 1, 1))
    with pytest.raises(recipe.RecipeRefused):
        recipe.report_security_ids(1728413, [LONG], _template("COMPARISON", 1, 1))


def test_wiring_the_resident_sends_report_security_ids(world, monkeypatch):
    calls = []
    real = getattr(recipe, "report_security_ids", None)

    def spy(model_portfolio_id, comparisons, template):
        calls.append((model_portfolio_id, list(comparisons)))
        return real(model_portfolio_id, comparisons, template) if real else ["P:" + str(model_portfolio_id)]

    monkeypatch.setattr(recipe, "report_security_ids", spy, raising=False)
    r = installed(world, monkeypatch)
    result = r.assembly.execute(r.message, lambda: None)
    assert result["state"] == "READY"
    assert calls == [(2332060, [])]


def test_printed_missing_comparisons_on_real_pdfs():
    prints = (PDFS / "comparison.pdf").read_bytes()
    alone = (PDFS / "overview.pdf").read_bytes()
    assert resident_worker.missing_comparisons(prints, [LONG]) == []
    assert resident_worker.missing_comparisons(alone, [LONG]) == ["Opal Long-Term"]
    assert resident_worker.missing_comparisons(alone, []) == []

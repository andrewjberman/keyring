"""MDPF_SECCLASS item 6 (CTO round-6 order; rulings batch 68 items 6-7): the canonical row for CEMIX.

CEMIX is the Causeway Emerging Markets Fund, Institutional class (Cottonwood's custody description reads
"CAUSEWAY EMERGING MARKETS INSTL"). Before this row the table held nothing for it and the retiring
bd-securities fallback answered fixed_income / International through a name alias.

The seed source is the ONE place a row is added (PRD O3); the seed script derives the item from it.
"""
import importlib.util
import os
import subprocess
import sys

ROOT = subprocess.check_output(["git", "rev-parse", "--show-toplevel"], cwd=os.path.dirname(os.path.abspath(__file__)),
                               text=True).strip()
SHARED = os.path.join(ROOT, "infra", "aws", "lambda", "v2_portal", "_shared")
SEED = os.path.join(ROOT, "infra", "aws", "lambda", "v2_portal", "yang_pipeline", "seed-etf-classifications.py")


def _seed_module():
    if SHARED not in sys.path:
        sys.path.insert(0, SHARED)
    spec = importlib.util.spec_from_file_location("seed_etf_classifications_cemix", SEED)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_module_asserts_cemix_as_an_emerging_markets_equity_fund():
    seed = _seed_module()
    assert seed.module_values("CEMIX") == {
        "asset_class": "equity",
        "sub_asset_class": "EM",
        "management_style": "active",
        "sector": "Emerging Markets",
        "name": "Causeway Emerging Markets Fund Institutional Class",
        "instrument_kind": "fund",
        "industry": None,
    }


def test_seed_item_for_a_ticker_the_table_does_not_hold():
    seed = _seed_module()
    item, preserved, conflicts = seed.merge_item("CEMIX", None, "2026-10-01T00:00:00Z")
    assert conflicts == [] and preserved == []
    assert item == {
        "ticker": "CEMIX",
        "asset_class": "equity",
        "sub_asset_class": "EM",
        "management_style": "active",
        "sector": "Emerging Markets",
        "name": "Causeway Emerging Markets Fund Institutional Class",
        "instrument_kind": "fund",
        "last_updated": "2026-10-01T00:00:00Z",
        "updated_by": "seed-script",
        "classified_by": "seed",
    }


def test_same_class_as_the_other_emerging_markets_equity_funds():
    """The control: CEMIX sits where IEMG, VWO and EEM sit on the two axes a page groups by."""
    seed = _seed_module()
    want = (seed.module_values("IEMG")["asset_class"], seed.module_values("IEMG")["sub_asset_class"])
    assert want == ("equity", "EM")
    for ticker in ("VWO", "EEM", "CEMIX"):
        got = seed.module_values(ticker)
        assert (got["asset_class"], got["sub_asset_class"]) == want

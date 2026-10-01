"""MDPF_SECCLASS, the Cottonwood thread (CTO rulings batch 86 item 6, batch 90 item 2): the 19 seed rows for the
tickers that carry most of the dollars the canonical table lacked on Cottonwood's gold positions (2026-09-30).
No cash row: cash is the caller's rule read from the feed's flag (batch 93 item 1), so FCASH and FIGXX are absent.

Each row follows a SEED peer of its own kind: the test reads the peer from the same module and requires the new
row to sit in the peer's class and sub class. A row whose peer moved would fail here before it reached the table.
"""
import importlib.util
import os
import subprocess
import sys

import pytest

ROOT = subprocess.check_output(["git", "rev-parse", "--show-toplevel"], cwd=os.path.dirname(os.path.abspath(__file__)),
                               text=True).strip()
SHARED = os.path.join(ROOT, "infra", "aws", "lambda", "v2_portal", "_shared")
SEED = os.path.join(ROOT, "infra", "aws", "lambda", "v2_portal", "yang_pipeline", "seed-etf-classifications.py")

# ticker -> (seed peer, instrument_kind)
ROWS = {
    "MEAR": ("VTES", "fund"), "EVSM": ("VTES", "fund"), "VMLUX": ("VTES", "fund"),
    "CDSIX": ("VCSH", "fund"), "FPNIX": ("VCSH", "fund"),
    "PRTMX": ("MUB", "fund"), "PFMIX": ("MUB", "fund"), "EIHYX": ("MUB", "fund"),
    "PAAA": ("JAAA", "fund"), "EIBIX": ("HYG", "fund"),
    "MFEIX": ("IVV", "fund"), "FSPGX": ("IVV", "fund"), "FLCOX": ("IVV", "fund"),
    "FTHSX": ("IJR", "fund"), "FSSZX": ("IJR", "fund"),
    "PSLV": ("SLV", "fund"), "SPYI": ("JEPI", "fund"),
    "BRK.B": ("WMT", "single_security"), "BRK.A": ("WMT", "single_security"),
}


@pytest.fixture(scope="module")
def seed():
    if SHARED not in sys.path:
        sys.path.insert(0, SHARED)
    spec = importlib.util.spec_from_file_location("seed_etf_classifications_cot_rows", SEED)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_there_are_19_rows(seed):
    assert len(ROWS) == 19


@pytest.mark.parametrize("ticker", sorted(ROWS))
def test_row_sits_in_its_seed_peers_class_and_sub_class(seed, ticker):
    peer, kind = ROWS[ticker]
    got, want = seed.module_values(ticker), seed.module_values(peer)
    assert want["asset_class"] != "unknown" and want["sub_asset_class"], "the peer %s is not a full seed row" % peer
    assert (got["asset_class"], got["sub_asset_class"]) == (want["asset_class"], want["sub_asset_class"])
    assert got["instrument_kind"] == kind
    assert got["name"] != ticker, "a seed row without a name seeds the ticker as its name"


def test_each_item_is_a_plain_seed_row_with_no_model_fields(seed):
    for ticker in ROWS:
        item, preserved, conflicts = seed.merge_item(ticker, None, "2026-10-01T00:00:00Z")
        assert conflicts == [] and preserved == []
        assert item["classified_by"] == "seed" and item["updated_by"] == "seed-script"
        assert "classification_confidence" not in item and "low_confidence" not in item
        assert all(v not in (None, "") for v in item.values())


def test_no_cash_row_is_seeded(seed):
    for ticker in ("FCASH", "FIGXX"):
        assert seed.module_values(ticker)["asset_class"] == "unknown", "cash is the caller's rule, never a seed row"

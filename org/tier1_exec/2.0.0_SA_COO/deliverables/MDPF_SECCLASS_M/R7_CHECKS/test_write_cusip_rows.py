"""MDPF_SECCLASS (CTO rulings batch 93 item 2): the writer for operator-named `CUSIP:` rows.

Covers:
  - a valid line plans a `CUSIP:` key with identifier_namespace CUSIP, classified_by scheduled, no empty sub class;
  - a Black Diamond 8-character identifier and a masked CUSIP are refused, never written into the CUSIP namespace;
  - a class or sub class outside the table's vocabulary, a duplicate and a missing name are refused;
  - a key the table already holds is PRESENT and left alone;
  - --write lands nothing when any line is refused, and puts only under attribute_not_exists(ticker).

Run: python -m pytest org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R7_CHECKS/test_write_cusip_rows.py -q -p no:cacheprovider
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

_HERE = Path(__file__).resolve().parent
_SHARED = _HERE.parents[5] / "infra" / "aws" / "lambda" / "v2_portal" / "_shared"

sys.path.insert(0, str(_SHARED))

from etf_classification_scheduled import TableVocabulary  # noqa: E402


def _load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, str(path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture(scope="module")
def writer():
    return _load_module(_HERE / "write_cusip_rows.py", "write_cusip_rows")


VOCAB = TableVocabulary.from_mapping({"fixed_income": ["Short Duration", "Municipal"], "equity": ["US Large Cap"]})


def test_valid_line_plans_a_cusip_row(writer):
    rows, refused, present = writer.plan_rows(
        [(1, ["98970LTE3", "fixed_income", "", "ZIONS BANCORPORATION NATL ASSN 3.95% 2026"])], VOCAB, set())
    assert refused == [] and present == []
    assert rows == [{
        "ticker": "CUSIP:98970LTE3", "identifier_namespace": "CUSIP", "asset_class": "fixed_income",
        "sub_asset_class": None, "name": "ZIONS BANCORPORATION NATL ASSN 3.95% 2026",
        "classified_by": "scheduled", "updated_by": "mdpf-secclass-cusip-rows"}]


@pytest.mark.parametrize("ident", ["BD4HOKI9", "03xxxxEY7", "98970lte3", "98970LTE"])
def test_not_a_cusip_is_refused(writer, ident):
    rows, refused, _ = writer.plan_rows([(3, [ident, "fixed_income", "", "a name"])], VOCAB, set())
    assert rows == [] and refused and refused[0][1].startswith("NOT-A-CUSIP")


def test_vocabulary_duplicate_and_name_refusals(writer):
    lines = [
        (1, ["98970LTE3", "bonds", "", "x"]),
        (2, ["90983WCD1", "fixed_income", "Investment Grade", "x"]),
        (3, ["31986HAK1", "fixed_income", "", ""]),
        (4, ["5380366P4", "fixed_income", "Short Duration", "LIVE OAK"]),
        (5, ["5380366P4", "fixed_income", "Short Duration", "LIVE OAK"]),
        (6, ["38150V5M7", "fixed_income", ""]),
    ]
    rows, refused, _ = writer.plan_rows(lines, VOCAB, set())
    reasons = [r.split(":", 1)[0] for _, r in refused]
    assert reasons == ["CLASS-NOT-IN-VOCABULARY", "SUB-CLASS-NOT-IN-VOCABULARY", "NO-NAME", "DUPLICATE", "SHAPE"]
    assert [r["ticker"] for r in rows] == ["CUSIP:5380366P4"]


def test_a_non_ascii_name_is_refused(writer):
    # MDPF_SECCLASS-S15: CUSIP:025083882 was written as 'AMERICAN CENTURY ULTRA® INV'; a served-table name is ASCII.
    rows, refused, _ = writer.plan_rows([(1, ["025083882", "equity", "US Large Cap", "AMERICAN CENTURY ULTRA® INV"])],
                                        VOCAB, set())
    assert rows == [] and refused and refused[0][1].startswith("NON-ASCII-NAME")
    rows, refused, _ = writer.plan_rows([(1, ["025083882", "equity", "US Large Cap", "AMERICAN CENTURY ULTRA(R) INV"])],
                                        VOCAB, set())
    assert refused == [] and rows[0]["name"] == "AMERICAN CENTURY ULTRA(R) INV"


def test_present_key_is_left_alone(writer):
    rows, refused, present = writer.plan_rows(
        [(1, ["66476QFV5", "fixed_income", "", "NORTHERN BANK"])], VOCAB, {"CUSIP:66476QFV5"})
    assert rows == [] and refused == [] and present == ["CUSIP:66476QFV5"]


class _FakeTable:
    def __init__(self):
        self.puts = []

    def put_item(self, Item, ConditionExpression):
        self.puts.append((Item, ConditionExpression))


def _run_main(writer, monkeypatch, tmp_path, text, write):
    set_file = tmp_path / "set.txt"
    set_file.write_text(text, encoding="utf-8")
    table = _FakeTable()

    class _Classifier:
        pass

    monkeypatch.setattr(writer, "ETFClassifier", _Classifier)
    monkeypatch.setattr(writer.TableVocabulary, "from_live_table", classmethod(lambda cls, c: VOCAB))
    monkeypatch.setattr(writer, "existing_tickers", lambda c: set())
    real_write = writer.scheduled.write
    monkeypatch.setattr(writer.scheduled, "write", lambda rows: real_write(rows, table=table))
    argv = ["--set-file", str(set_file)] + (["--write"] if write else [])
    return writer.main(argv), table


def test_write_refuses_whole_set_on_any_refusal(writer, monkeypatch, tmp_path):
    rc, table = _run_main(writer, monkeypatch, tmp_path,
                          "98970LTE3\tfixed_income\t\tZIONS\nBD4HOKI9\tfixed_income\t\tVOYA\n", write=True)
    assert rc == 3 and table.puts == []


def test_write_puts_only_on_absence(writer, monkeypatch, tmp_path):
    rc, table = _run_main(writer, monkeypatch, tmp_path,
                          "# comment\n98970LTE3\tfixed_income\t\tZIONS 3.95% 2026\n", write=True)
    assert rc == 0 and len(table.puts) == 1
    item, condition = table.puts[0]
    assert condition == "attribute_not_exists(ticker)"
    assert item["ticker"] == "CUSIP:98970LTE3" and item["identifier_namespace"] == "CUSIP"
    assert "sub_asset_class" not in item and item["classified_by"] == "scheduled"


def test_dry_run_puts_nothing(writer, monkeypatch, tmp_path):
    rc, table = _run_main(writer, monkeypatch, tmp_path, "98970LTE3\tfixed_income\t\tZIONS\n", write=False)
    assert rc == 0 and table.puts == []

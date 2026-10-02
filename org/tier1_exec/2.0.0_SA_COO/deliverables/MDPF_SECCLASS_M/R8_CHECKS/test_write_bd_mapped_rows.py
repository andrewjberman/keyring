"""MDPF_SECCLASS BD forward fix 2 (CTO rulings batch 139): the one-act writer for bd-securities-mapped ticker rows.

Run: python -m pytest org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R8_CHECKS/test_write_bd_mapped_rows.py -q -p no:cacheprovider
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE.parents[5] / "infra" / "aws" / "lambda" / "v2_portal" / "_shared"))
from etf_classification_scheduled import TableVocabulary  # noqa: E402

spec = importlib.util.spec_from_file_location("write_bd_mapped_rows", str(_HERE / "write_bd_mapped_rows.py"))
W = importlib.util.module_from_spec(spec)
spec.loader.exec_module(W)

VOCAB = TableVocabulary.from_mapping({"fixed_income": ["Intermediate"], "equity": ["EM"]})


def _line(*f):
    return (1, list(f))


def test_plans_the_stated_pair_as_a_scheduled_row():
    rows, refused, present = W.plan_rows([_line("VBTIX", "fixed_income", "", "VANGUARD TOTAL BOND", "fixed_income / Investment Grade", "class_kept")], VOCAB, set())
    assert refused == [] and present == []
    assert rows == [{"ticker": "VBTIX", "asset_class": "fixed_income", "sub_asset_class": None, "name": "VANGUARD TOTAL BOND",
                     "classified_by": "scheduled", "updated_by": "mdpf-secclass-bd-mapped"}]


@pytest.mark.parametrize("t", ["", "vbtix", "CUSIP:98970LTE3", "TOOLONGTICKER1", "A B"])
def test_refuses_what_is_not_a_ticker(t):
    rows, refused, _ = W.plan_rows([_line(t, "fixed_income", "", "x", "p", "d")], VOCAB, set())
    assert rows == [] and refused[0][1].startswith("NOT-A-TICKER")


def test_refuses_vocabulary_name_shape_and_duplicates_and_leaves_present_rows():
    lines = [(1, ["AAA", "bonds", "", "x", "p", "d"]), (2, ["BBB", "fixed_income", "Investment Grade", "x", "p", "d"]),
             (3, ["CCC", "fixed_income", "", "", "p", "d"]), (4, ["DDD", "equity", "EM"]),
             (5, ["EEE", "equity", "EM", "x", "p", "d"]), (6, ["EEE", "equity", "EM", "x", "p", "d"]),
             (7, ["FFF", "equity", "EM", "x", "p", "d"])]
    rows, refused, present = W.plan_rows(lines, VOCAB, {"FFF"})
    assert [r.split(":")[0] for _, r in refused] == ["CLASS-NOT-IN-VOCABULARY", "SUB-CLASS-NOT-IN-VOCABULARY", "NO-NAME", "SHAPE", "DUPLICATE"]
    assert [r["ticker"] for r in rows] == ["EEE"] and present == ["FFF"]


def test_write_puts_only_on_absence_and_refuses_the_whole_set_on_one_refusal(monkeypatch, tmp_path):
    puts = []

    class _T:
        def put_item(self, Item, ConditionExpression):
            puts.append((Item, ConditionExpression))

    monkeypatch.setattr(W, "ETFClassifier", type("C", (), {}))
    monkeypatch.setattr(W.TableVocabulary, "from_live_table", classmethod(lambda cls, c: VOCAB))
    monkeypatch.setattr(W, "existing_tickers", lambda c: set())
    real = W.scheduled.write
    monkeypatch.setattr(W.scheduled, "write", lambda rows: real(rows, table=_T()))
    bad = tmp_path / "bad.tsv"
    bad.write_text("VBTIX\tfixed_income\t\tVANGUARD\tp\td\nvbtix\tfixed_income\t\tx\tp\td\n", encoding="utf-8")
    assert W.main(["--set-file", str(bad), "--write"]) == 3 and puts == []
    good = tmp_path / "good.tsv"
    good.write_text("# c\nVBTIX\tfixed_income\t\tVANGUARD\tp\td\n", encoding="utf-8")
    assert W.main(["--set-file", str(good), "--write"]) == 0
    assert len(puts) == 1 and puts[0][1] == "attribute_not_exists(ticker)" and "sub_asset_class" not in puts[0][0]

"""MDPF_SECCLASS item 9 (CTO rulings batch 75 items 2-3): write-model-rows.py, the model path's writer.

No AWS call: the table, the vocabulary read and the existing-ticker read are stubs.
"""
import importlib.util
import json
import os
import subprocess
import sys
from decimal import Decimal

import pytest

ROOT = subprocess.check_output(["git", "rev-parse", "--show-toplevel"],
                               cwd=os.path.dirname(os.path.abspath(__file__)), text=True).strip()
SHARED = os.path.join(ROOT, "infra", "aws", "lambda", "v2_portal", "_shared")
WRITER = os.path.join(ROOT, "infra", "aws", "lambda", "v2_portal", "yang_pipeline", "write-model-rows.py")
CENSUS = os.path.join(ROOT, "org", "tier1_exec", "2.0.0_SA_COO", "deliverables", "MDPF_SECCLASS_M",
                      "R4_MODEL_CLASSIFY_CENSUS_20260930.json")

VOCAB = {"fixed_income": ["Intermediate", "Short Duration", "International"],
         "equity": ["EM", "Global"],
         "alternatives": ["Real Estate"],
         "commodities": ["Commodities"]}


class StubTable:
    def __init__(self, present=()):
        self.present = set(present)
        self.calls = []

    def put_item(self, **kwargs):
        self.calls.append(("put_item", kwargs))
        ticker = kwargs["Item"]["ticker"]
        if ticker in self.present:
            from botocore.exceptions import ClientError
            raise ClientError({"Error": {"Code": "ConditionalCheckFailedException"}}, "PutItem")
        self.present.add(ticker)

    def __getattr__(self, name):  # any other table verb is a defect: record it loudly
        def _call(**kwargs):
            self.calls.append((name, kwargs))
            raise AssertionError("the writer called %s" % name)
        return _call


@pytest.fixture()
def writer(monkeypatch):
    if SHARED not in sys.path:
        sys.path.insert(0, SHARED)
    spec = importlib.util.spec_from_file_location("write_model_rows_under_test", WRITER)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    table = StubTable()
    existing = {"VNQ", "DBC"}
    monkeypatch.setattr(mod, "ETFClassifier", lambda *a, **k: object())
    monkeypatch.setattr(mod.TableVocabulary, "from_live_table",
                        classmethod(lambda cls, classifier=None: cls.from_mapping(VOCAB)))
    monkeypatch.setattr(mod, "existing_tickers", lambda classifier=None: set(existing))

    class _Resource:
        def Table(self, name):
            assert name == "etf-classifications"
            return table

    monkeypatch.setattr(mod.scheduled.boto3, "resource", lambda *a, **k: _Resource())
    mod._table = table
    mod._existing = existing
    return mod


def _candidates(writer):
    return writer.load_candidates(CENSUS)


def test_census_holds_the_26_candidates_of_the_half(writer):
    cands = _candidates(writer)
    assert len(cands) == 26
    assert sum(1 for c in cands.values() if c["low_confidence"]) == 11


def test_plan_keeps_a_candidate_and_refuses_the_rest_by_name(writer):
    cands = _candidates(writer)
    vocab = writer.TableVocabulary.from_mapping(VOCAB)
    rows, refused, present = writer.plan_rows(
        ["BAGIX", "USRT", "RLY", "NOSUCH", "VNQ"], cands, vocab, existing={"VNQ"})
    assert [r["ticker"] for r in rows] == ["BAGIX", "USRT"]
    bagix = rows[0]
    assert bagix["classified_by"] == "model" and bagix["updated_by"] == "mdpf-secclass-model"
    assert bagix["classification_confidence"] == Decimal("0.85") and bagix["low_confidence"] is False
    assert bagix["name"] is None, "a census name that repeats the ticker is not written as a name"
    reasons = dict(refused)
    assert reasons["RLY"].startswith("LOW-CONFIDENCE")
    assert reasons["NOSUCH"].startswith("NOT-A-CANDIDATE")
    assert reasons["VNQ"].startswith("NOT-A-CANDIDATE"), "a ticker outside the census is never planned"
    assert present == []


def test_an_existing_candidate_is_reported_present_not_planned(writer):
    cands = _candidates(writer)
    vocab = writer.TableVocabulary.from_mapping(VOCAB)
    rows, refused, present = writer.plan_rows(["DODIX"], cands, vocab, existing={"DODIX"})
    assert rows == [] and refused == [] and present == ["DODIX"]


def test_a_class_or_sub_class_outside_the_vocabulary_is_refused(writer):
    cands = _candidates(writer)
    vocab = writer.TableVocabulary.from_mapping({"fixed_income": ["Short Duration"]})
    rows, refused, _ = writer.plan_rows(["BAGIX", "USRT"], cands, vocab, existing=set())
    reasons = dict(refused)
    assert rows == []
    assert reasons["BAGIX"].startswith("SUB-CLASS-NOT-IN-VOCABULARY")
    assert reasons["USRT"].startswith("CLASS-NOT-IN-VOCABULARY")


def test_no_ticker_named_is_a_refusal(writer, capsys):
    assert writer.main([]) == 2
    assert "never derives a plan" in capsys.readouterr().out


def test_dry_run_is_the_default_and_writes_nothing(writer, capsys):
    assert writer.main(["--census", CENSUS, "--ticker", "BAGIX", "--ticker", "DODIX"]) == 0
    out = capsys.readouterr().out
    assert "MODEL-ROWS named=2 plan=2 already_present=0 refused=0" in out
    assert "DRY RUN: nothing written" in out
    assert writer._table.calls == []


def test_write_is_blocked_while_the_shared_put_drops_the_model_fields(writer, monkeypatch, capsys):
    monkeypatch.setattr(writer.scheduled, "_WRITE_FIELDS",
                        ("ticker", "asset_class", "sub_asset_class", "classified_by", "updated_by", "name"))
    assert writer.main(["--census", CENSUS, "--ticker", "BAGIX", "--write"]) == 4
    assert "would drop" in capsys.readouterr().out
    assert writer._table.calls == []


def test_write_is_all_or_nothing_when_a_named_ticker_is_refused(writer, monkeypatch, capsys):
    monkeypatch.setattr(writer.scheduled, "_WRITE_FIELDS",
                        tuple(writer.scheduled._WRITE_FIELDS) + writer.MODEL_FIELDS)
    assert writer.main(["--census", CENSUS, "--ticker", "BAGIX", "--ticker", "RLY", "--write"]) == 3
    assert "nothing written" in capsys.readouterr().out
    assert writer._table.calls == []


def test_write_puts_each_row_conditionally_with_the_model_fields(writer, monkeypatch, capsys):
    fields = tuple(f for f in writer.scheduled._WRITE_FIELDS if f not in writer.MODEL_FIELDS) + writer.MODEL_FIELDS
    monkeypatch.setattr(writer.scheduled, "_WRITE_FIELDS", fields)
    assert writer.main(["--census", CENSUS, "--ticker", "USRT", "--ticker", "VCMDX", "--write"]) == 0
    out = capsys.readouterr().out
    assert "WRITTEN 2 of 2: USRT VCMDX" in out
    calls = writer._table.calls
    assert [name for name, _ in calls] == ["put_item", "put_item"], "puts only: no update, no delete"
    for _, kwargs in calls:
        assert kwargs["ConditionExpression"] == "attribute_not_exists(ticker)"
        item = kwargs["Item"]
        assert item["classified_by"] == "model" and item["updated_by"] == "mdpf-secclass-model"
        assert isinstance(item["classification_confidence"], Decimal) and item["low_confidence"] is False
        assert "name" not in item and "last_updated" in item
    usrt = calls[0][1]["Item"]
    assert (usrt["asset_class"], usrt["sub_asset_class"]) == ("alternatives", "Real Estate")


def test_a_row_that_appears_between_plan_and_put_is_left_alone(writer, monkeypatch, capsys):
    fields = tuple(f for f in writer.scheduled._WRITE_FIELDS if f not in writer.MODEL_FIELDS) + writer.MODEL_FIELDS
    monkeypatch.setattr(writer.scheduled, "_WRITE_FIELDS", fields)
    writer._table.present.add("USRT")          # the table gained it after the plan's read
    assert writer.main(["--census", CENSUS, "--ticker", "USRT", "--write"]) == 0
    out = capsys.readouterr().out
    assert "WRITTEN 0 of 1" in out and "left alone: USRT" in out


def test_the_file_has_no_overwrite_and_no_delete_path():
    text = open(WRITER, encoding="utf-8").read()
    code = text.split('"""', 2)[2]   # everything after the module docstring
    for verb in ("delete_item", "update_item", "batch_writer", "put_item", "DeleteItem", "UpdateItem"):
        assert verb not in code, "%s appears in the writer's code" % verb
    assert "scheduled.write(rows)" in code
    assert json.dumps("--force") not in code and "--overwrite" not in code

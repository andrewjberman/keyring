"""CTO rulings batch 78 items 6-8: `_WRITE_FIELDS` of etf_classification_scheduled.py gains the two
model fields, and a SCHEDULED row's written item is identical before and after the change, with
neither field appearing on it -- not even as null.

"Before" is the module at the commit before the change, read with `git show` (the pin below); "after"
is the module in this worktree. Both are loaded as modules and their write() is run over the same
scheduled plan against a recording stub table. No AWS call.
"""
import importlib.util
import os
import subprocess
import sys
from decimal import Decimal

ROOT = subprocess.check_output(["git", "rev-parse", "--show-toplevel"],
                               cwd=os.path.dirname(os.path.abspath(__file__)), text=True).strip()
SHARED = os.path.join(ROOT, "infra", "aws", "lambda", "v2_portal", "_shared")
REL = "infra/aws/lambda/v2_portal/_shared/etf_classification_scheduled.py"
BEFORE_PIN = "b9fe6986c5"          # CLOUD before the two names were added
MODEL_FIELDS = ("classification_confidence", "low_confidence")


class Recorder:
    def __init__(self):
        self.items = []

    def put_item(self, **kwargs):
        self.items.append(kwargs)


def _load(path, name):
    if SHARED not in sys.path:
        sys.path.insert(0, SHARED)
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod            # a dataclass resolves its annotations through sys.modules
    spec.loader.exec_module(mod)
    return mod


def _before(tmp_path):
    body = subprocess.check_output(["git", "show", "%s:%s" % (BEFORE_PIN, REL)], cwd=ROOT)
    assert body, "the pinned module read empty"
    path = tmp_path / "etf_classification_scheduled_before.py"
    path.write_bytes(body)
    return _load(str(path), "etf_classification_scheduled_before")


def _after():
    return _load(os.path.join(SHARED, "etf_classification_scheduled.py"), "etf_classification_scheduled_after")


def _scheduled_plan(mod):
    """A real scheduled plan: plan_rows over two new tickers, one of them a CUSIP-free fund."""
    vocab = mod.TableVocabulary.from_mapping({"equity": ["US Large Cap"], "fixed_income": ["Intermediate"]})
    lookup = {"NEWA": {"ticker": "NEWA", "asset_class": "equity", "sub_asset_class": "US Large Cap"},
              "NEWB": {"ticker": "NEWB", "asset_class": "fixed_income", "sub_asset_class": "Intermediate"}}
    rows, unresolved, seed_pending = mod.plan_rows(
        [("NEWA", "New A Inc"), ("NEWB", "New B Bond Fund")], vocab=vocab, existing_tickers=set(),
        bd_securities_lookup=lambda t: lookup.get(t), updated_by="e18-scheduled")
    assert unresolved == [] and seed_pending == []
    return rows


def _written(mod, plan):
    table = Recorder()
    results = mod.write(plan, table=table)
    items = []
    for call in table.items:
        item = dict(call["Item"])
        item.pop("last_updated")               # the one value that is a clock, not the row
        items.append((item, call["ConditionExpression"]))
    return results, items


def test_the_list_names_the_two_model_fields_after_and_not_before(tmp_path):
    before, after = _before(tmp_path), _after()
    assert all(name not in before._WRITE_FIELDS for name in MODEL_FIELDS)      # control: the pin is "before"
    assert all(name in after._WRITE_FIELDS for name in MODEL_FIELDS)
    assert tuple(f for f in after._WRITE_FIELDS if f not in MODEL_FIELDS) == tuple(before._WRITE_FIELDS)


def test_a_scheduled_row_writes_the_identical_item_before_and_after(tmp_path):
    before, after = _before(tmp_path), _after()
    plan_before, plan_after = _scheduled_plan(before), _scheduled_plan(after)
    assert len(plan_before) == 2 and plan_before == plan_after
    results_before, items_before = _written(before, plan_before)
    results_after, items_after = _written(after, plan_after)
    assert results_before == results_after == [("NEWA", "written"), ("NEWB", "written")]
    assert items_before == items_after
    for item, condition in items_after:
        assert condition == "attribute_not_exists(ticker)"
        assert item["classified_by"] == "scheduled"
        for name in MODEL_FIELDS:
            assert name not in item, "%s appears on a scheduled item" % name


def test_a_scheduled_row_with_the_keys_set_to_none_still_writes_neither(tmp_path):
    """Not even as null: a planned dict that carries the keys with None writes no such attribute."""
    after = _after()
    plan = [dict(row, classification_confidence=None, low_confidence=None) for row in _scheduled_plan(after)]
    _, items = _written(after, plan)
    for item, _ in items:
        assert all(name not in item for name in MODEL_FIELDS)


def test_a_model_row_now_keeps_both_fields(tmp_path):
    """The difference the change exists for: before, the put drops them; after, it writes them."""
    before, after = _before(tmp_path), _after()
    row = {"ticker": "MODELX", "asset_class": "equity", "sub_asset_class": "US Large Cap",
           "classified_by": "model", "updated_by": "mdpf-secclass-model",
           "classification_confidence": Decimal("0.85"), "low_confidence": False}
    _, items_before = _written(before, [row])
    _, items_after = _written(after, [row])
    assert all(name not in items_before[0][0] for name in MODEL_FIELDS)
    assert items_after[0][0]["classification_confidence"] == Decimal("0.85")
    assert items_after[0][0]["low_confidence"] is False

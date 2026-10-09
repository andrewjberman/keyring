"""MDPF_SECCLASS round 16 cell SC-e-81 check (row D1-S18): seed-etf-classifications.py --dry-run says DRY RUN and "would write N" in its
summary, never "Items written", and puts nothing.

No AWS: boto3.resource and read_existing are stubbed; an empty table makes every module ticker a row to write.
Run: python -m pytest -q org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R16_CHECKS/test_r16_seed_dry_run_words.py
"""
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
SEED = ROOT / "infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-classifications.py"


class _Batch:
    def __init__(self, sink):
        self.sink = sink

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False

    def put_item(self, Item):
        self.sink.append(Item)


class _Table:
    def __init__(self, sink):
        self.sink = sink

    def batch_writer(self):
        return _Batch(self.sink)


class _Resource:
    def __init__(self, sink):
        self.sink = sink

    def Table(self, name):
        return _Table(self.sink)


def _load():
    spec = importlib.util.spec_from_file_location("seed_etf_classifications", SEED)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def _run(m, monkeypatch, dry_run):
    puts = []
    monkeypatch.setattr(m.boto3, "resource", lambda *a, **k: _Resource(puts))
    monkeypatch.setattr(m, "read_existing", lambda table: {})
    m.seed_table(dry_run=dry_run)
    return puts


def test_dry_run_summary_says_would_write_and_puts_nothing(monkeypatch, capsys):
    m = _load()
    puts = _run(m, monkeypatch, dry_run=True)
    out = capsys.readouterr().out
    assert puts == []
    assert "Items written" not in out, "a dry run must not report items written"
    assert "would write" in out.lower()
    assert "DRY RUN" in out.split("MERGE SUMMARY")[-1], "the summary after the merge must carry DRY RUN"


def test_real_run_still_reports_items_written(monkeypatch, capsys):
    m = _load()
    puts = _run(m, monkeypatch, dry_run=False)
    out = capsys.readouterr().out
    assert len(puts) > 0
    assert "Items written" in out

#!/usr/bin/env python3
"""ai_classifier_dry_run.py -- MDPF_SECCLASS round 8, cell SC-e-31 (criterion SC8-e31-AC3): the AI classifier runner, dry
run, against one real firm's held input.

READS ONLY. It runs `yang_pipeline/classify-residual-model.py` `run()` in dry run (the stub model, no write) over one firm's
held (ticker, name) pairs, reading the live `etf-classifications` table for presence and vocabulary (consistent-enough
paginated scans, the same reads the scheduled classifier makes). The table handle and the model transport are wrapped with
counters: any put / update / delete / batch-write is counted AND refused, and the transport counts every call.

THE HELD INPUT: Inflection's held (ticker, name) pairs from the R2 unresolved-review file
(org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R2_UNRESOLVED_REVIEW_20260930.json, firm = inflection, entries that
carry a ticker). Why this one: it is the one held-securities list in the tree for a firm that is keyed by ticker (the bd and
49financial entries carry no ticker, so the runner could not key them) and it is readable with no write and no S3 address.
It is the set of Inflection's held names the 2026-09-30 plan left unresolved, a point-in-time input, not today's full
held set; the runner takes today's held set from the firm's own source in service.

Prints one line:
  AI-DRY-RUN held=<n> present=<n> direct=<n> to_model=<n> would_land=0 model_calls=0 index_address=<address>
and exits non-zero (printing AI-DRY-RUN-BAD) if model_calls != 0, a put was attempted, or would_land != 0.
"""
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
SHARED = ROOT / "infra/aws/lambda/v2_portal/_shared"
RUNNER = ROOT / "infra/aws/lambda/v2_portal/yang_pipeline/classify-residual-model.py"
HELD_FILE = ROOT / "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R2_UNRESOLVED_REVIEW_20260930.json"
FIRM = "inflection"
REGION = "us-east-1"
BLOCKED = ("put_item", "update_item", "delete_item", "batch_write_item", "batch_writer")


class GuardedTable:
    """Delegates reads; counts and refuses every write."""

    def __init__(self, inner):
        self._inner = inner
        self.write_attempts = 0

    def __getattr__(self, name):
        if name in BLOCKED:
            def refuse(*_a, **_k):
                self.write_attempts += 1
                raise RuntimeError("REFUSED: the dry run attempted %s" % name)
            return refuse
        return getattr(self._inner, name)


class CountingSend:
    def __init__(self):
        self.calls = 0

    def __call__(self, payload, **_kw):
        self.calls += 1
        raise RuntimeError("REFUSED: the dry run called the model transport")


def held_pairs():
    doc = json.loads(HELD_FILE.read_text(encoding="utf-8"))
    return [(e["ticker"], e.get("name")) for e in doc["entries"] if e.get("firm") == FIRM and e.get("ticker")]


def main():
    sys.path.insert(0, str(SHARED))
    spec = importlib.util.spec_from_file_location("classify_residual_model_dry", RUNNER)
    runner = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(runner)
    from etf_classification_scheduled import TableVocabulary, existing_tickers
    from etf_classifications_dynamodb import ETFClassifier

    classifier = ETFClassifier(region=REGION)
    guard = GuardedTable(classifier.table)
    classifier.table = guard
    vocab = TableVocabulary.from_live_table(classifier)
    existing = existing_tickers(classifier, region=REGION)
    send = CountingSend()
    held = held_pairs()
    rep = runner.run(held, vocab=vocab, existing=existing, table=None, s3=None, send=send, api_key=None,
                     use_model=False, do_write=False)
    print("FIRM %s held_source=%s pairs=%d table_tickers=%d live_classes=%s"
          % (FIRM, HELD_FILE.name, len(held), len(existing), sorted(vocab.asset_classes)))
    for ticker, why in rep["left_unresolved"][:5]:
        print("  UNRESOLVED (stub) %s: %s" % (ticker, why))
    bad = []
    if send.calls != 0 or rep["model_calls"] != 0:
        bad.append("model_calls=%d/%d" % (send.calls, rep["model_calls"]))
    if guard.write_attempts != 0:
        bad.append("put_attempts=%d" % guard.write_attempts)
    if rep["would_land"] != 0:
        bad.append("would_land=%d" % rep["would_land"])
    if bad:
        print("AI-DRY-RUN-BAD " + " ".join(bad))
        return 1
    print("AI-DRY-RUN held=%d present=%d direct=%d to_model=%d would_land=%d model_calls=%d index_address=%s"
          % (rep["held"], rep["present"], rep["direct"], rep["to_model"], rep["would_land"], send.calls,
             rep["index_address"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())

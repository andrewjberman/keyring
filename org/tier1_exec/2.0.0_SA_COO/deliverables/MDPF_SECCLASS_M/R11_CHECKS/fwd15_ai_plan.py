#!/usr/bin/env python3
"""fwd15_ai_plan.py -- MDPF_SECCLASS round 9, cell SC-e-49 (FWD-15 via FWD-11, analysis ruling 2.3): the AI classifier's plan over
each firm's missing list, held-first, after the direct-match plan.

READ-ONLY against AWS (consistent paginated DynamoDB scans of bd-securities and etf-classifications). NO model call, NO table
write. The model client is never constructed: the runner's own `run()` is driven in its stub mode with a transport that counts
and refuses every call, and the planner asserts the count is 0. Writes three local files:
  M/FWD15_AI_PLAN_<firm>_20261007.json
  {"firm", "as_of", "source", "claim", "missing_list", "model_calls", "planned_model_calls", "entries": [{"key", "amount", "route", ...}]}

For each firm in {49financial, cottonwood, inflection}, the newest M/MISSING_LIST_<firm>_*.json (SC-e-33) is read; every entry is
routed, in this order:
  PRESENT       its shared key (or its own key) is now a key of etf-classifications (a fresh consistent read; never touched)
  UNPLACED-KEY  no declared key form fits it (contract `identifier_namespace`): a ticker-shaped key is itself, a 9-character
                CUSIP-shaped key is CUSIP:<9>, `CUSIP:<9>` is itself, `NAME::<anything>` is NAME::<slug> (slug = name upper-cased,
                each run outside A-Z 0-9 - replaced by ONE space, trimmed, first 80 characters; empty = no key), any other form
                has none
  DIRECT        the direct-match plan (etf_classification_scheduled.classify_asset_class, the plan SC-e-32 used: the old list's
                row as input) places it AND its class is one of the six AND its sub-class is a member of the contract's closed
                list for that class (ruling 2.5: `fields.sub_asset_class.values_by_class`)
  AI            everything else: the runner (classify-residual-model.py) would send it to the model. The runner's own `run()`
                dry run is the cross-check: its `to_model` must equal this count and its `direct` the DIRECT count.
Entries are ordered by `amount`, largest first (held-first: every entry is a held security). Carried, not fixed (round 8): the
runner sends the key to the model as its "ticker", so a NAME:: key is sent as the "ticker" (W26-S7, `name_key_as_ticker`); the AI
runner builds no identifier_namespace (W26-S5, `identifier_namespace_written` = null for every AI entry).

Usage (repo root):  python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R11_CHECKS/fwd15_ai_plan.py [--out-dir DIR]
Prints  FWD15-AI-PLAN firms=3 entries=<n> direct=<n> ai=<n> unplaced_key=<n> present=<n> model_calls=0
"""
from __future__ import annotations

import argparse
import collections
import glob
import importlib.util
import json
import re
import sys
from pathlib import Path

import boto3

HERE = Path(__file__).resolve().parent
M = HERE.parent
ROOT = HERE.parents[5]
SHARED = ROOT / "infra/aws/lambda/v2_portal/_shared"
RUNNER = ROOT / "infra/aws/lambda/v2_portal/yang_pipeline/classify-residual-model.py"
CONTRACT = ROOT / "org/standards/MDPF_SECCLASS_CONTRACT.json"
FIRMS = ("49financial", "cottonwood", "inflection")
SIX = ("cash", "fixed_income", "equity", "structured", "alternatives", "commodities")
REGION = "us-east-1"
DATE = "20261007"
TICKER_RE = re.compile(r"[A-Z0-9]{1,6}([.\-][A-Z0-9]{1,4})?")
CUSIP_RE = re.compile(r"[A-Z0-9]{9}")
NAME_PREFIX = "NAME::"
CUSIP_PREFIX = "CUSIP:"
MAX_ATTEMPTS = 2  # etf_classification_model.classify_one: attempts in (1, 2)


def slug(name):
    n = "".join(c if c.isalnum() or c == "-" else " " for c in str(name).upper())
    return " ".join(n.split())[:80]


def scan_items(table_name):
    table = boto3.resource("dynamodb", region_name=REGION).Table(table_name)
    items, kw = [], {"ConsistentRead": True}
    while True:
        resp = table.scan(**kw)
        items.extend(resp.get("Items", []))
        if "LastEvaluatedKey" not in resp:
            return items
        kw["ExclusiveStartKey"] = resp["LastEvaluatedKey"]


def derive_shared_key(key, shared_keys):
    """(shared_key or "", key_form). The declared forms only."""
    if key.startswith(NAME_PREFIX):
        s = slug(key[len(NAME_PREFIX):])
        return (NAME_PREFIX + s if s else ""), "NAME"
    if key.startswith(CUSIP_PREFIX):
        return key, "CUSIP"
    if TICKER_RE.fullmatch(key):
        return key, "TICKER"
    if CUSIP_RE.fullmatch(key):
        return CUSIP_PREFIX + key, "CUSIP"
    if key in shared_keys:
        return key, "PRESENT-OTHER"
    return "", "NONE"


def load_runner():
    sys.path.insert(0, str(SHARED))
    spec = importlib.util.spec_from_file_location("classify_residual_model_plan", str(RUNNER))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class CountingSend:
    """The transport the model client would use. Counts and refuses; the planner asserts the count is 0."""

    def __init__(self):
        self.calls = 0

    def __call__(self, payload, **_kw):
        self.calls += 1
        raise RuntimeError("REFUSED: the planner called the model transport")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--out-dir", default=str(M))
    a = ap.parse_args(argv)
    out_dir = Path(a.out_dir)

    runner = load_runner()
    from etf_classification_scheduled import TableVocabulary, classify_asset_class
    from etf_classification import ETF_CLASSIFICATIONS

    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    closed = {c: set(v) for c, v in contract["fields"]["sub_asset_class"]["values_by_class"].items()}
    assert set(closed) == set(SIX), sorted(closed)

    old_rows = scan_items("bd-securities")
    shared_rows = scan_items("etf-classifications")
    shared_keys = {r["ticker"] for r in shared_rows}
    old_by_key = {r["ticker"]: r for r in old_rows}
    print(f"DENOMINATOR old={len(old_rows)} shared={len(shared_keys)} contract={contract.get('contract_version')}", flush=True)

    live = TableVocabulary.from_live_table()
    live_not_closed = {c: sorted(live.sub_asset_classes.get(c, set()) - closed[c]) for c in SIX}
    # the vocabulary the direct plan matches against: the live table's, the six classes, inside the contract's closed list
    vocab = TableVocabulary(
        asset_classes={c for c in live.asset_classes if c in SIX},
        sub_asset_classes={c: set(live.sub_asset_classes.get(c, set())) & closed[c] for c in SIX})

    def bd_lookup(k):
        """The old list's row for a missing key: the key itself, or the bare 9-character CUSIP behind CUSIP:<9>."""
        for cand in (k, k[len(CUSIP_PREFIX):] if k.startswith(CUSIP_PREFIX) else None):
            if cand and cand in old_by_key:
                return old_by_key[cand]
        return None

    totals = collections.Counter()
    for firm in FIRMS:
        ml_path = sorted(glob.glob(str(M / f"MISSING_LIST_{firm}_*.json")))[-1]
        ml = json.loads(Path(ml_path).read_text(encoding="utf-8"))
        missing = ml["missing"]
        assert len(missing) == ml["total"], (firm, len(missing), ml["total"])
        assert len({m["key"] for m in missing}) == len(missing), f"{firm}: duplicate keys in the missing list"

        entries, ai_pairs = [], []
        for m in missing:
            key = m["key"]
            sk, form = derive_shared_key(key, shared_keys)
            e = {"key": key, "amount": m.get("amount") or 0.0, "route": None, "name": m.get("name"), "cusip": m.get("cusip"),
                 "shared_key": sk or None, "key_form": form}
            if sk and (sk in shared_keys or key in shared_keys):
                e["route"] = "PRESENT"
            elif not sk:
                e["route"] = "UNPLACED-KEY"
            else:
                ac, sac, _ = classify_asset_class(sk, vocab=vocab, bd_securities_lookup=bd_lookup)
                if ac in SIX and (sac is None or sac in closed[ac]) and ac is not None:
                    e["route"] = "DIRECT"
                    e["asset_class"], e["sub_asset_class"] = ac, sac
                else:
                    e["route"] = "AI"
                    e["name_key_as_ticker"] = sk.startswith(NAME_PREFIX)
                    e["in_old_list"] = bd_lookup(sk) is not None  # also in SC-e-32's old-list set (one put wins; a later one is refused)
                    e["identifier_namespace_written"] = None
                    ai_pairs.append((sk, m.get("name")))
            entries.append(e)
        entries.sort(key=lambda e: -float(e["amount"] or 0))  # stable: ties keep the list's order

        # cross-check: the runner's own dry run (stub model, counting transport, no table, no s3) over the keyed, non-PRESENT pairs
        send = CountingSend()
        keyed = [(e["shared_key"], e["name"]) for e in entries if e["route"] in ("DIRECT", "AI")]
        rep = runner.run(keyed, vocab=vocab, existing=shared_keys, table=None, s3=None, send=send, api_key=None,
                         use_model=False, do_write=False, seed_tickers=set(ETF_CLASSIFICATIONS.keys()), bd_lookup=bd_lookup)
        n = collections.Counter(e["route"] for e in entries)
        assert send.calls == 0 and rep["model_calls"] == 0, (firm, send.calls, rep["model_calls"])
        assert rep["direct"] + rep["seed_pending"] == n["DIRECT"] and rep["to_model"] == n["AI"], \
            (firm, rep["direct"], rep["seed_pending"], rep["to_model"], dict(n))
        n_ai = n["AI"]
        n_name = sum(1 for e in entries if e["route"] == "AI" and e["name_key_as_ticker"])
        amt = {r: round(sum(float(e["amount"] or 0) for e in entries if e["route"] == r), 2) for r in n}
        plan = {
            "firm": firm, "as_of": ml["as_of"],
            "source": f"direct-match plan + AI runner dry run over {Path(ml_path).name}, bd-securities and etf-classifications "
                      f"scanned read-only 2026-10-07; held set = {ml['source']}",
            "claim": "inferred", "missing_list": Path(ml_path).name, "model_calls": 0,
            "planned_model_calls": n_ai, "at_most_model_calls_with_retry": n_ai * MAX_ATTEMPTS,
            "runner_dry_run": {"held": rep["held"], "direct": rep["direct"], "to_model": rep["to_model"],
                               "seed_pending": rep["seed_pending"], "would_land": rep["would_land"],
                               "model_calls": rep["model_calls"], "transport_calls": send.calls},
            "route_counts": dict(n), "route_amount_usd": amt, "ai_entries_with_name_key": n_name,
            "ai_entries_also_in_old_list": sum(1 for e in entries if e["route"] == "AI" and e["in_old_list"]),
            "ai_entries_without_identifier_namespace": n_ai,
            "denominator": {"bd_securities_rows": len(old_rows), "etf_classifications_rows": len(shared_keys),
                            "missing_entries": len(missing)},
            "contract_version": contract.get("contract_version"),
            "live_subclasses_outside_the_contract_closed_list": live_not_closed,
            "entries": entries,
        }
        out = out_dir / f"FWD15_AI_PLAN_{firm}_{DATE}.json"
        out.write_text(json.dumps(plan, indent=1, ensure_ascii=True) + "\n", encoding="ascii")
        print(f"FIRM {firm} entries={len(entries)} routes={dict(n)} planned_model_calls={n_ai} at_most={n_ai * MAX_ATTEMPTS} "
              f"name_key_ai={n_name} ai_in_old_list={plan['ai_entries_also_in_old_list']} amount_usd={amt}", flush=True)
        totals["entries"] += len(entries)
        for r, c in n.items():
            totals[r] += c
    print(f"FWD15-AI-PLAN firms=3 entries={totals['entries']} direct={totals['DIRECT']} ai={totals['AI']} "
          f"unplaced_key={totals['UNPLACED-KEY']} present={totals['PRESENT']} model_calls=0")
    return 0


if __name__ == "__main__":
    sys.exit(main())

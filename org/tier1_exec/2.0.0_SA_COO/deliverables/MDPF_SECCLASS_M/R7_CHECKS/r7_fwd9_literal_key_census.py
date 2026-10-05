#!/usr/bin/env python3
"""r7_fwd9_literal_key_census.py -- CTO batch 261's condition on the FWD-9 rows half, BRANCH 1 (READ-ONLY).

Before `r7_fwd9_write.py --write --namespace BLOOMBERG`, every BBG key of the WRITE set that holds `/`, `-` or `*` is run
through SC-e-16's reader harness (r7_bbg_reader_census.py, imported, never copied) as a LITERAL key:
  - the harness's KEY, row shape A (the key's own planned item from FWD9_ROW_SET_20261005.tsv) and shape B (no
    sub_asset_class, low_confidence true) are re-bound per key;
  - beside the harness's controls, two mis-key controls are added in the fixed_income class: the key's bare Bloomberg
    ticker verbatim (e.g. `BP/`) and the same with every non-alphanumeric character removed (e.g. `BP`). A reader that
    strips the key to either answers fixed_income and is graded MISKEYS by the harness's own class_verdict;
  - every one of the harness's READERS runs through its own run_one (threaded, with its timeout).
The baseline key `BBG:REL:LN` runs first, unchanged: it must reproduce SC-e-16's grade (TOLERATES 34, READ-ONLY 11), or
the re-binding is wrong and the check prints INSTRUMENT-FAULT and grades nothing.

TWO PASSES per key. The harness's exercises name the REL fixture's sub-class in two places (find_by_sub_asset_class
("Developed") and the vocabulary check for "Developed"), so a literal row in another sub-class fails those two expectations
whatever its key. Pass 1 runs the literal row; pass 2 runs the same key with sub_asset_class pinned to the fixture's
"Developed". A key is TOLERATED when pass 2 reads every reader TOLERATES or READ-ONLY AND every pass-1 failure is one of
the two fixture expectations (FIXTURE_EVIDENCE); otherwise it is HELD, named with each failing reader.
Writes R7_FWD9_LITERAL_KEY_CENSUS_20261005.json beside this file and prints one line per key and
`FWD9-LITERAL-KEYS keys=<n> tolerated=<n> held=<n>`. No AWS call; nothing is written to any table.

Usage (repo root): python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R7_CHECKS/r7_fwd9_literal_key_census.py
"""
from __future__ import annotations

import collections
import copy
import importlib.util
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SET_FILE = HERE / "FWD9_ROW_SET_20261005.tsv"
OUT = HERE / "R7_FWD9_LITERAL_KEY_CENSUS_20261005.json"
CLEAN = ("TOLERATES", "READ-ONLY")
FIXTURE_SUB = "Developed"
FIXTURE_EVIDENCE = ("find_by_sub_asset_class(Developed)", "vocabulary sub classes")
SPECIAL = re.compile(r"[/*-]")


def load_harness():
    spec = importlib.util.spec_from_file_location("r7_bbg_harness", str(HERE / "r7_bbg_reader_census.py"))
    mod = importlib.util.module_from_spec(spec)
    sys.modules["r7_bbg_harness"] = mod
    spec.loader.exec_module(mod)
    return mod


def literal_keys():
    """{key: planned item} for the BBG WRITE lines whose key holds / - or *."""
    keys = {}
    for line in SET_FILE.read_text(encoding="utf-8").splitlines():
        f = line.split("\t")
        if len(f) == 5 and f[0] == "WRITE" and f[1].startswith("BBG:") and SPECIAL.search(f[1]):
            item = json.loads(f[4])
            item.pop("days", None)
            keys[f[1]] = item
    return keys


def bind(h, key, row_a, base_controls):
    """Re-bind the harness's module globals to one key; its functions read them at call time."""
    row_b = {k: v for k, v in row_a.items() if k != "sub_asset_class"}
    row_b["low_confidence"] = True
    h.KEY, h.ROW_A, h.ROW_B = key, row_a, row_b
    h.VARIANTS = [("A", row_a), ("B", row_b)]
    controls = copy.deepcopy(base_controls)
    have = {c["ticker"] for c in controls}
    if key != "BBG:REL:LN":
        bare = key.split(":")[1]
        for t in (bare, re.sub(r"[^A-Za-z0-9]", "", bare)):
            if t and t not in have:
                controls.append({"ticker": t, "asset_class": "fixed_income", "sub_asset_class": "Short Duration",
                                 "management_style": "active", "name": "Control bare %s" % t, "classified_by": "seed"})
                have.add(t)
    h.CONTROLS = controls


def run_readers(h):
    out = []
    for path, func, fn in h.READERS:
        verdict, evidence = h.run_one(fn)
        out.append({"path": path, "function": func, "verdict": verdict, "evidence": evidence})
    return out


def main() -> int:
    h = load_harness()
    base_controls = copy.deepcopy(h.CONTROLS)
    base_row = copy.deepcopy(h.ROW_A)
    bind(h, "BBG:REL:LN", base_row, base_controls)
    baseline = run_readers(h)
    base_counts = collections.Counter(r["verdict"] for r in baseline)
    print("BASELINE BBG:REL:LN %s" % dict(sorted(base_counts.items())), flush=True)
    doc = {"what": "CTO batch 261: the FWD-9 BBG keys holding / - * run through SC-e-16's reader harness as literal keys",
           "claim": "measured (the harness's own exercises, table stubbed; no AWS call)",
           "baseline": {"key": "BBG:REL:LN", "counts": dict(base_counts)}, "keys": {}}
    if base_counts.get("TOLERATES") != 34 or base_counts.get("READ-ONLY") != 11 or len(baseline) != 45:
        doc["instrument_fault"] = [r for r in baseline if r["verdict"] not in CLEAN]
        OUT.write_text(json.dumps(doc, indent=1) + "\n", encoding="utf-8")
        print("INSTRUMENT-FAULT: the baseline does not reproduce SC-e-16 (TOLERATES 34, READ-ONLY 11); nothing graded")
        return 2
    tolerated, held = [], []
    for key, item in sorted(literal_keys().items()):
        bind(h, key, item, base_controls)
        p1 = [r for r in run_readers(h) if r["verdict"] not in CLEAN]
        p1_other = [r for r in p1 if not (r["verdict"] == "FAILS-CONTRACT"
                                          and any(e in r["evidence"] for e in FIXTURE_EVIDENCE))]
        bind(h, key, dict(item, sub_asset_class=FIXTURE_SUB), base_controls)
        p2_readers = run_readers(h)
        p2 = [r for r in p2_readers if r["verdict"] not in CLEAN]
        counts = collections.Counter(r["verdict"] for r in p2_readers)
        bad = p2 + p1_other
        doc["keys"][key] = {"security_bloomberg": item.get("security_bloomberg"),
                            "sub_asset_class": item.get("sub_asset_class"), "pass2_counts": dict(counts),
                            "pass1_fixture_only_failures": len(p1) - len(p1_other),
                            "status": "HELD" if bad else "TOLERATED", "failing": bad}
        (held if bad else tolerated).append(key)
        print("KEY %-16s %-9s pass2=%s pass1_fixture_only=%d%s" % (
            key, "HELD" if bad else "TOLERATED", dict(sorted(counts.items())), len(p1) - len(p1_other),
            "" if not bad else " :: " + "; ".join("%s %s" % (r["verdict"], r["path"]) for r in bad)), flush=True)
    doc["summary"] = {"keys": len(doc["keys"]), "tolerated": tolerated, "held": held}
    OUT.write_text(json.dumps(doc, indent=1) + "\n", encoding="utf-8")
    print("FWD9-LITERAL-KEYS keys=%d tolerated=%d held=%d" % (len(doc["keys"]), len(tolerated), len(held)))
    return 0


if __name__ == "__main__":
    sys.exit(main())

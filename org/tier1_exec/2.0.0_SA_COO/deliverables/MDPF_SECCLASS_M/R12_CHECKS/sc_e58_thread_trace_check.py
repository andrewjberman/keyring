#!/usr/bin/env python3
"""sc_e58_thread_trace_check.py -- MDPF_SECCLASS round 10 SC-e-58: the BD pages trace record is complete.

READ-ONLY. Reads M/BD_PAGES_THREAD_TRACE_20261007.json and prints SC-E58 ok=<bool> with the reason. ok requires: at least 7
hops in journey order (page, api, platinum_key, gold_producer, silver_dim, classifier_lib, canonical_source); every hop graded
PASS / FAIL / UNREAD with non-empty evidence; GLD, PHYS and VXX each read on every hop that is not UNREAD; first_failing_hop
equal to the first FAIL hop's name (or "NONE" when no hop fails), and a FAIL hop names fix_file and fix_line.
"""
import json
import sys
from pathlib import Path

HOPS = ["page", "api", "platinum_key", "gold_producer", "silver_dim", "classifier_lib", "canonical_source"]
REC = Path.cwd() / "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M" / "BD_PAGES_THREAD_TRACE_20261007.json"


def grade(doc):
    hops = doc.get("hops") or []
    names = [h.get("name") for h in hops]
    if names[:len(HOPS)] != HOPS:
        return False, f"hops={names}"
    first = "NONE"
    for h in hops:
        g = h.get("grade")
        if g not in ("PASS", "FAIL", "UNREAD") or not str(h.get("evidence") or "").strip():
            return False, f"hop {h.get('name')} grade={g} evidence empty or grade off-enum"
        if g != "UNREAD":
            reads = h.get("tickers") or {}
            missing = [t for t in ("GLD", "PHYS", "VXX") if t not in reads]
            if missing:
                return False, f"hop {h.get('name')} missing tickers {missing}"
        if g == "FAIL" and first == "NONE":
            first = h["name"]
            if not h.get("fix_file") or not h.get("fix_line"):
                return False, f"failing hop {first} names no fix_file/fix_line"
    if doc.get("first_failing_hop") != first:
        return False, f"first_failing_hop={doc.get('first_failing_hop')} measured={first}"
    return True, f"hops={len(hops)} first_failing_hop={first}"


def main():
    if not REC.is_file():
        print(f"SC-E58 ok=False reason=absent {REC.name}")
        return 1
    ok, why = grade(json.loads(REC.read_text(encoding="utf-8")))
    print(f"SC-E58 ok={ok} {why}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

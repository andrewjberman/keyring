#!/usr/bin/env python3
"""unplaced_key_census.py -- MDPF_SECCLASS round 12, cell SC-e-70: READ-ONLY census of FWD-15's UNPLACED-KEY entries.

Reads the three plan files  e49_replan/FWD15_AI_PLAN_<firm>_20261007.json  (beside this script), takes every entry whose
`route` is UNPLACED-KEY, assigns each to EXACTLY ONE (firm, pattern) group (first matching rule in PATTERNS, else "other"),
and writes ../UNPLACED_KEY_CENSUS_20261008.json with, per group: count, amount (USD, signed sum), abs_usd and up to 5 examples
(largest absolute amount first). No AWS call, no table write, no model call.

Prints  UNPLACED-CENSUS ok=<bool> total=<n> firms=<n> patterns=<n> usd=<sum>
ok = total is 99 AND every entry is in exactly one group (group counts sum to total, no (firm,key) repeated).
`patterns` counts distinct pattern labels across firms.

Usage (repo root):  python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R12_CHECKS/unplaced_key_census.py
"""
from __future__ import annotations

import glob
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PLAN_GLOB = str(HERE / "e49_replan" / "FWD15_AI_PLAN_*_20261007.json")
OUT = HERE.parent / "UNPLACED_KEY_CENSUS_20261008.json"
EXPECTED_TOTAL = 99

# (label, predicate(key, entry)) -- first match wins, so a key is in exactly one pattern.
PATTERNS = [
    ("<digits>_<word>", lambda k, e: re.fullmatch(r"\d+_[A-Z0-9_]+", k) is not None),
    ("CXMANUAL_*", lambda k, e: k.startswith("CXMANUAL_")),
    ("BA- FIDELITY.*", lambda k, e: k.startswith("BA- FIDELITY.")),
    ("BA- <other>", lambda k, e: k.startswith("BA- ")),
    ("<10 digits>", lambda k, e: re.fullmatch(r"\d{10}", k) is not None),
    ("BD<6 alnum> (key = cusip column)", lambda k, e: re.fullmatch(r"BD[0-9A-Z]{6}", k) is not None and e.get("cusip") == k),
    ("<8 alnum> other (key = cusip column)", lambda k, e: re.fullmatch(r"[0-9A-Z]{8}", k) is not None and e.get("cusip") == k),
    ("CGF-<alnum>", lambda k, e: re.fullmatch(r"CGF-[0-9A-Z]+", k) is not None),
    ("<ticker>-OLD<mmddyyyy>", lambda k, e: re.fullmatch(r"[A-Z]{1,5}-OLD\d{8}", k) is not None),
    ("cash pseudo-key", lambda k, e: re.search(r"(^|[_:])CASH$", k) is not None),
    ("<ticker><space><class letter>", lambda k, e: re.fullmatch(r"[A-Z]{1,5} [A-Z]", k) is not None),
    ("<ticker>+<suffix>", lambda k, e: re.fullmatch(r"[A-Z]{1,5}\+[A-Z]", k) is not None),
    ("dotted ticker", lambda k, e: re.fullmatch(r"[A-Z]{1,5}(\.[A-Z]{1,3})+", k) is not None),
]


def pattern_of(key: str, entry: dict) -> str:
    for label, pred in PATTERNS:
        if pred(key, entry):
            return label
    return "other"


def main() -> int:
    files = sorted(glob.glob(PLAN_GLOB))
    entries = []
    for f in files:
        d = json.load(open(f, encoding="utf-8"))
        for e in d["entries"]:
            if e.get("route") == "UNPLACED-KEY":
                entries.append((d["firm"], e))
    total = len(entries)

    groups: dict = {}
    seen = set()
    dup = 0
    for firm, e in entries:
        ident = (firm, e["key"])
        if ident in seen:
            dup += 1
        seen.add(ident)
        g = groups.setdefault((firm, pattern_of(e["key"], e)), [])
        g.append(e)

    out_groups = []
    for (firm, pat), es in sorted(groups.items(), key=lambda kv: (kv[0][0], -sum(x["amount"] for x in kv[1]))):
        top = sorted(es, key=lambda x: -abs(x["amount"]))[:5]
        out_groups.append({
            "firm": firm, "pattern": pat, "count": len(es),
            "usd": round(sum(x["amount"] for x in es), 2),
            "abs_usd": round(sum(abs(x["amount"]) for x in es), 2),
            "examples": [{"key": x["key"], "name": x["name"], "amount": x["amount"], "cusip": x.get("cusip")} for x in top],
        })

    in_groups = sum(g["count"] for g in out_groups)
    firms = sorted({g["firm"] for g in out_groups})
    pats = sorted({g["pattern"] for g in out_groups})
    usd = round(sum(g["usd"] for g in out_groups), 2)
    ok = (total == EXPECTED_TOTAL) and (in_groups == total) and dup == 0

    firm_tot = {}
    for g in out_groups:
        t = firm_tot.setdefault(g["firm"], {"count": 0, "usd": 0.0})
        t["count"] += g["count"]
        t["usd"] = round(t["usd"] + g["usd"], 2)

    doc = {
        "claim": "measured: read-only census of route=UNPLACED-KEY entries in the three FWD15_AI_PLAN files (e49_replan, 20261007)",
        "sources": [Path(f).name for f in files],
        "total": total, "expected_total": EXPECTED_TOTAL, "entries_in_groups": in_groups, "duplicate_firm_key": dup,
        "firms": firm_tot, "usd_signed_sum": usd,
        "pattern_labels": pats, "groups": out_groups, "ok": ok,
    }
    OUT.write_text(json.dumps(doc, indent=2, ensure_ascii=True) + "\n", encoding="ascii")
    print("UNPLACED-CENSUS ok=%s total=%d firms=%d patterns=%d usd=%.2f" % (ok, total, len(firms), len(pats), usd))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

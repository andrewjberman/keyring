#!/usr/bin/env python3
"""fwd15_plan_check.py -- MDPF_SECCLASS round 9, cell SC-e-49 (FWD-15 via FWD-11, analysis ruling 2.3): the issuer's check of the
per-firm AI plans over SC-e-33's missing lists. The worker does not edit this file. READ-ONLY (files only).

For each firm in {49financial, cottonwood, inflection} reads the newest M/MISSING_LIST_<firm>_*.json (SC-e-33's list) and the newest
M/FWD15_AI_PLAN_<firm>_*.json (the worker's plan, shape {"firm", "as_of", "source", "claim", "missing_list": "<file>",
"model_calls": 0, "planned_model_calls": N, "entries": [{"key", "amount", "route", ...}]}) and PASSES only if, per firm:
  - the plan's keys are exactly the missing list's keys, each once;
  - every route is one of DIRECT, AI, UNPLACED-KEY, PRESENT;
  - entries are held-first: ordered by amount, largest first (ties in any order);
  - model_calls == 0 and planned_model_calls == the number of AI entries;
  - claim is `inferred` (dell1 cannot read the served bytes; ruling 2.9).
Prints FWD15-PLAN ok=True|False firms=<n of 3> entries=<n> ai=<n> direct=<n> problems=<first three>.
"""
import glob
import json
import sys
from pathlib import Path

HOME = Path(__file__).resolve().parents[1]
FIRMS = ("49financial", "cottonwood", "inflection")
ROUTES = {"DIRECT", "AI", "UNPLACED-KEY", "PRESENT"}


def newest(pattern):
    hits = sorted(glob.glob(str(HOME / pattern)))
    return hits[-1] if hits else None


def main():
    probs, firms_ok, total, ai, direct = [], 0, 0, 0, 0
    for firm in FIRMS:
        ml, pl = newest(f"MISSING_LIST_{firm}_*.json"), newest(f"FWD15_AI_PLAN_{firm}_*.json")
        if not ml or not pl:
            probs.append(f"{firm}:absent")
            continue
        with open(ml, encoding="utf-8") as fh:
            want = [m["key"] for m in json.load(fh)["missing"]]
        with open(pl, encoding="utf-8") as fh:
            plan = json.load(fh)
        ents = plan.get("entries") or []
        keys = [e.get("key") for e in ents]
        before = len(probs)
        if sorted(keys) != sorted(want) or len(set(keys)) != len(keys):
            probs.append(f"{firm}:keys")
        if any(e.get("route") not in ROUTES for e in ents):
            probs.append(f"{firm}:route")
        amts = [float(e.get("amount") or 0) for e in ents]
        if amts != sorted(amts, reverse=True):
            probs.append(f"{firm}:order")
        n_ai = sum(1 for e in ents if e.get("route") == "AI")
        if plan.get("model_calls") != 0 or plan.get("planned_model_calls") != n_ai:
            probs.append(f"{firm}:calls")
        if plan.get("claim") != "inferred":
            probs.append(f"{firm}:claim")
        firms_ok += len(probs) == before
        total += len(ents)
        ai += n_ai
        direct += sum(1 for e in ents if e.get("route") == "DIRECT")
    ok = not probs and firms_ok == len(FIRMS)
    print(f"FWD15-PLAN ok={ok} firms={firms_ok} of 3 entries={total} ai={ai} direct={direct} problems={probs[:3]}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""issuer_check_sc_e26.py -- MDPF_SECCLASS round 8 issuer check for cell SC-e-26 (FWD-17, FWD-15: the old list measured).

Modes (one verdict token each; run from the repo root; read-only against DynamoDB):
  census  -- the newest M/OLD_LIST_CENSUS_*.json carries a denominator, two partitions that each sum to it, and a
             denominator within 25 rows of a fresh consistent count of DynamoDB bd-securities (us-east-1), the seam probe
             against the real table. Prints SC-E26-CENSUS ok=True|False.
  keyform -- the newest M/KEY_FORM_PROPOSAL_*.md carries one 'PROPOSED KEY FORM:' line and the four postulates
             (MECE, SAME GRAIN, INTENT COHERENCE, STATE COHERENCE). Prints SC-E26-KEYFORM ok=True|False.

Expected JSON shape (the worker's deliverable):
  {"scanned_at": "...", "table": "bd-securities", "denominator": N,
   "by_membership": {"in_both_lists": a, "held_today_not_in_shared": b, "rest": c},     # a+b+c == N
   "by_key_form": {"ticker": w, "CUSIP:": x, "NAME::": y, "none_or_other": z},          # w+x+y+z == N
   "held_source": "<the served artifact(s) read for 'held today', with date>"}
"""
import glob
import json
import os
import sys

M = os.path.join("org", "tier1_exec", "2.0.0_SA_COO", "deliverables", "MDPF_SECCLASS_M")
TOLERANCE = 25


def newest(pattern):
    hits = sorted(glob.glob(os.path.join(M, pattern)))
    return hits[-1] if hits else None


def live_count():
    import boto3
    ddb = boto3.client("dynamodb", region_name="us-east-1")
    n = 0
    for page in ddb.get_paginator("scan").paginate(TableName="bd-securities", Select="COUNT", ConsistentRead=True):
        n += page["Count"]
    return n


def check_census():
    path = newest("OLD_LIST_CENSUS_*.json")
    if not path:
        return False, "no OLD_LIST_CENSUS_*.json"
    with open(path, encoding="utf-8") as fh:
        doc = json.load(fh)
    n = doc.get("denominator")
    if not isinstance(n, int) or n <= 0:
        return False, "no denominator"
    for part, members in (("by_membership", ("in_both_lists", "held_today_not_in_shared", "rest")),
                          ("by_key_form", ("ticker", "CUSIP:", "NAME::", "none_or_other"))):
        p = doc.get(part) or {}
        if set(p) != set(members):
            return False, f"{part} members {sorted(p)} != {sorted(members)}"
        if sum(p.values()) != n:
            return False, f"{part!s} sums to {int(sum(p.values()))}, denominator {int(n)}"
    if not doc.get("held_source"):
        return False, "held_source not named"
    live = live_count()
    if abs(live - n) > TOLERANCE:
        return False, f"denominator {int(n)} vs live count {int(live)} (tolerance {int(TOLERANCE)})"
    return True, f"file={os.path.basename(path)!s} denominator={int(n)} live={int(live)}"


def check_keyform():
    path = newest("KEY_FORM_PROPOSAL_*.md")
    if not path:
        return False, "no KEY_FORM_PROPOSAL_*.md"
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    if text.count("PROPOSED KEY FORM:") != 1:
        return False, "expected exactly one 'PROPOSED KEY FORM:' line"
    low = text.lower()
    for marker in ("mece", "same grain", "intent coherence", "state coherence"):
        if marker not in low:
            return False, f"postulate '{marker}' missing"
    return True, f"file={os.path.basename(path)}"


def main(argv):
    mode = argv[0] if argv else ""
    if mode == "census":
        ok, why = check_census()
        print(f"SC-E26-CENSUS ok={ok} {why}")
    elif mode == "keyform":
        ok, why = check_keyform()
        print(f"SC-E26-KEYFORM ok={ok} {why}")
    else:
        print("usage: issuer_check_sc_e26.py census|keyform")
        return 2
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

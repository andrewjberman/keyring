#!/usr/bin/env python3
"""r32_delivered_read.py -- the acceptance checks of TO IRPT_BCKEND.TO-IB-m32-321 (cell IB-mr-321, E-M3).

One delivered FILE, pinned by commit AND content sha256 (1.0.0_SA_CTO~DELL2 ruling msg 191): laptop 3.0.0_SA_CVO's run of
r32m_multi_relationship_read.py @a533959eae (the producer's own Cottonwood build for 2026-10-05, under a read-only guard).
Read-only: one `git show`, nothing written.

    python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R32_CHECKS/r32_delivered_read.py m1|m2|m3

Last line is one token: M1-MULTI-RELATIONSHIP-NAMED / M2-RECONCILES / M3-OVERLAP-MEASURED on PASS, else NOT-<token>.
"""
import hashlib
import json
import subprocess
import sys

COMMIT = "09e0d7c89c"
PATH = "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_M/R32M_MULTI_RELATIONSHIP_READ.json"
SHA256 = "e2606081349ee91aef56ede3fac5c368f57cbcff057bae23922e92de1595f56a"
TOKENS = {"m1": "M1-MULTI-RELATIONSHIP-NAMED", "m2": "M2-RECONCILES", "m3": "M3-OVERLAP-MEASURED"}


def load():
    raw = subprocess.run(["git", "show", "%s:%s" % (COMMIT, PATH)], capture_output=True, check=True).stdout
    got = hashlib.sha256(raw).hexdigest()
    print("FILE %s@%s sha256 %s (pinned %s)" % (PATH, COMMIT, got, SHA256))
    return json.loads(raw) if got == SHA256 else None


def m1(d):
    r = d["m1"]
    print("m1: account %s in relationships %s; %s account(s) hold more than one Relationship ID of %s with relationship rows"
          % (r.get("account_node_id"), r.get("relationships"), r.get("instances_total"), d.get("accounts_with_relationship_rows")))
    return r.get("verdict") == "PASS" and r.get("found") is True and len(r.get("relationships") or []) > 1


def m2(d):
    r = d["m2"]
    print("m2: %s raw rows -> %s unique positions (%s duplicate relationship rows collapsed); subtree ties %s over %s partitions, "
          "%d unbalanced; rebuilt %s vs served %s (%s %s rev %s)" % (
              r.get("raw_rows"), r.get("unique_positions"), r.get("duplicate_relationship_rows_collapsed"), r.get("subtree_ties"),
              r.get("partitions"), len(r.get("partitions_unbalanced") or []), r.get("rebuilt_value"), r.get("served_value"),
              d["served_publication"].get("business_date"), d.get("build_date"), str(d["served_publication"].get("revision"))[:12]))
    return (r.get("verdict") == "PASS" and r.get("subtree_ties") is True and r.get("matches_served") is True
            and not r.get("partitions_unbalanced") and d.get("build_date") == d["served_publication"].get("business_date"))


def m3(d):
    g = d["m3"]["overlap"]
    cells = ("multi_model_and_multi_relationship", "multi_model_only", "multi_relationship_only", "neither")
    print("m3: of %s accounts -- both %s, multi-model only %s, multi-relationship only %s, neither %s" % (
        g.get("accounts"), *(g.get(c) for c in cells)))
    return d["m3"].get("verdict") == "PASS" and sum(g.get(c) or 0 for c in cells) == g.get("accounts") and g.get("accounts")


def main():
    which = sys.argv[1] if len(sys.argv) > 1 else ""
    if which not in TOKENS:
        print("usage: r32_delivered_read.py m1|m2|m3")
        return 2
    d = load()
    ok = d is not None and {"m1": m1, "m2": m2, "m3": m3}[which](d)
    print(TOKENS[which] if ok else "NOT-" + TOKENS[which])
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

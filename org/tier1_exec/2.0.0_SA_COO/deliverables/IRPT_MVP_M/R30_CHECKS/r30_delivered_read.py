#!/usr/bin/env python3
"""r30_delivered_read.py -- the acceptance checks of TO IRPT_BCKEND.TO-IB-m30-301 (cell IB-mr-301, E-M1).

The read itself ran on the laptop (row IRPT_BCKEND-S352: the dell2 identity is refused on the firm buckets); its result is
the delivered FILE, pinned here by commit AND content hash (1.0.0_SA_CTO~DELL2 ruling msg 191: criteria read from the
delivered file, naming its path and hash). Read-only: one `git show`, nothing written.

    python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R30_CHECKS/r30_delivered_read.py c1|c2|c3

Prints exactly one verdict token on its last line: C1-TIES / C2-TIES / C3-RECONCILES on PASS, else NOT-<token>.
"""
import hashlib
import json
import subprocess
import sys

COMMIT = "8b83fd1d6f"
PATH = "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_M/R30M_FWD5_REPLAY_READ_2.json"
SHA256 = "afa19a65eb338c6adc72be8684e81c51f9f4c2347fea7d5584e78b3cbe884c52"
FIRMS = ("49financial", "inflection", "cottonwood")
TOKENS = {"c1": "C1-TIES", "c2": "C2-TIES", "c3": "C3-RECONCILES"}


def load():
    raw = subprocess.run(["git", "show", "%s:%s" % (COMMIT, PATH)], capture_output=True, check=True).stdout
    got = hashlib.sha256(raw).hexdigest()
    print("FILE %s@%s sha256 %s (pinned %s)" % (PATH, COMMIT, got, SHA256))
    if got != SHA256:
        return None
    return json.loads(raw)


def c1(d):
    r = d["criteria"]["c1"]
    print("c1: account %s value %s, %s partitions, %d unbalanced, %d faults" % (
        r.get("account_node_id"), r.get("account_value"), r.get("partitions"),
        len(r.get("partitions_unbalanced") or []), len(r.get("faults") or [])))
    return r.get("verdict") == "PASS" and r.get("ties") is True and (r.get("partitions") or 0) > 0 \
        and not r.get("partitions_unbalanced") and not r.get("faults")


def c2(d):
    r = d["criteria"]["c2"]
    n, tied = r.get("accounts_holding_either") or 0, r.get("accounts_tied") or 0
    print("c2: %d of %d Cottonwood accounts holding SPYI or PSLV tie; per symbol %s" % (tied, n, r.get("per_symbol")))
    return r.get("verdict") == "PASS" and n > 0 and tied == n and not r.get("accounts_failing")


def c3(d):
    firms = d["criteria"]["c3"].get("firms") or {}
    ok = set(firms) == set(FIRMS)
    for f in FIRMS:
        r = firms.get(f) or {}
        arms = r.get("arms") or {}
        print("c3 %s: arms %s; account sum %s vs served custody total %s; %s partitions, %s unbalanced" % (
            f, arms, r.get("account_sum"), r.get("custody_total_served"), r.get("partitions"),
            r.get("partitions_unbalanced_count")))
        ok = ok and len(arms) == 3 and all(v == "PASS" for v in arms.values()) and r.get("reconciled") is True
    print("c3: firms denominator %d" % len(firms))
    return ok and d["criteria"]["c3"].get("verdict") == "PASS"


def main():
    which = sys.argv[1] if len(sys.argv) > 1 else ""
    if which not in TOKENS:
        print("usage: r30_delivered_read.py c1|c2|c3")
        return 2
    d = load()
    ok = d is not None and {"c1": c1, "c2": c2, "c3": c3}[which](d)
    print(TOKENS[which] if ok else "NOT-" + TOKENS[which])
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

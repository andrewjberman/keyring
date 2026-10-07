#!/usr/bin/env python3
"""r31_delivered_reads.py -- the acceptance checks of TO IRPT_BCKEND.TO-IB-m31-311 (cell IB-mr-311, E-M2, AMENDMENT 1).

Two delivered FILES, each pinned by commit AND content sha256 (1.0.0_SA_CTO~DELL2 ruling msg 191):
  CASES     the laptop 3.0.0_SA_CVO read of the four FWD-5 PROOF cases (2026-10-05 publications)
  RECHECK   the dell2 re-check of the UNASSIGNED case over every instance (row S366, same publication date)
Read-only: `git show`, nothing written.

    python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R31_CHECKS/r31_delivered_reads.py e1|e2|e3

Last line is one token: E1-CASES-NAMED / E2-CASES-RECONCILE / E3-COVERAGE-DENOMINATED on PASS, else NOT-<token>.
"""
import hashlib
import json
import subprocess
import sys

CASES = ("471da6f0b0",
         "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_M/R31M_FWD5_PROOF_CASES_READ.json",
         "2b61c5a833c761e60b581f4f983f4c2795bc84624494df3a063d45571865f3e5")
RECHECK = ("6458a5a9d3",
           "org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R31M_UNASSIGNED_RECHECK_20261007.json",
           "9eb9cff78f7721a07653606eb9624ad33ed46b86688ac04641e6c09bde64498e")
CASE_NAMES = ("unassigned", "unmatched_join", "blended_model", "multi_membership")
FIRMS = ("49financial", "inflection", "cottonwood")
TOKENS = {"e1": "E1-CASES-NAMED", "e2": "E2-CASES-RECONCILE", "e3": "E3-COVERAGE-DENOMINATED"}


def load(pin):
    commit, path, want = pin
    raw = subprocess.run(["git", "show", "%s:%s" % (commit, path)], capture_output=True, check=True).stdout
    got = hashlib.sha256(raw).hexdigest()
    print("FILE %s@%s sha256 %s (pinned %s)" % (path, commit, got, want))
    return json.loads(raw) if got == want else None


def e1(cases, _recheck):
    ok = True
    for c in CASE_NAMES:
        r = cases["cases"].get(c) or {}
        if r.get("found"):
            print("e1 %s: FOUND at %s, instance %s, %s instance(s) in total" % (c, r["firm"], r["instance"], r["instances_total"]))
        elif r.get("searched"):
            print("e1 %s: ABSENT at 3 of 3 firms, accounts searched %s" % (c, r["searched"]))
        else:
            print("e1 %s: neither found nor stated absent" % c)
            ok = False
    return ok


def e2(cases, recheck):
    ok = True
    for c in CASE_NAMES:
        r = cases["cases"].get(c) or {}
        if not r.get("found"):
            continue
        if c == "unassigned":
            u = recheck["e2_unassigned"]
            dates = {f: p.get("business_date") for f, p in recheck["publications"].items()}
            same = all(dates[f] == cases["publications"][f]["business_date"] for f in dates)
            print("e2 unassigned (re-check, every instance): %s, %d of %d pass, publications %s, same date as the cases read: %s"
                  % (u["verdict"], u["accounts_passing"], u["accounts_listed"], dates, same))
            for f, fr in recheck["firms"].items():
                print("e2 unassigned %s: %d of %d (zero-value %d, tie %d, no model node %d)" % (
                    f, fr["pass"], fr["listed"], fr["zero_value"], fr["tie"], fr["no_model_node"]))
            ok = ok and u["verdict"] == "PASS" and u["accounts_passing"] == u["accounts_listed"] > 0 and same
            continue
        chk = r.get("check") or {}
        passed = chk.get("reconciles", chk.get("ties")) is True
        print("e2 %s at %s: %s %s" % (c, r["firm"], "reconciles" if passed else "DOES NOT reconcile",
                                       {k: chk.get(k) for k in ("account_value", "partitions", "arms", "remainder") if k in chk}))
        ok = ok and passed
    return ok


def e3(cases, _recheck):
    ok = True
    for f in FIRMS:
        cen = (cases["firms"].get(f) or {}).get("census") or {}
        cov, awc = cen.get("coverage") or {}, cen.get("assigned_without_custody") or {}
        print("e3 %s: coverage %s resolved of %s attempted (%s unmatched), remainder %s; assigned_without_custody %s (%s)" % (
            f, cov.get("nodes_resolved"), cov.get("nodes_attempted"), cov.get("unmatched"),
            (cov.get("remainder") or {}).get("amount"), awc.get("account_count"), awc.get("denominator")))
        ok = ok and cov.get("nodes_attempted") is not None and awc.get("account_count") is not None
    return ok


def main():
    which = sys.argv[1] if len(sys.argv) > 1 else ""
    if which not in TOKENS:
        print("usage: r31_delivered_reads.py e1|e2|e3")
        return 2
    cases, recheck = load(CASES), load(RECHECK)
    ok = cases is not None and recheck is not None and {"e1": e1, "e2": e2, "e3": e3}[which](cases, recheck)
    print(TOKENS[which] if ok else "NOT-" + TOKENS[which])
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

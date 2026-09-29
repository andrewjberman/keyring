"""MDPF_SECCLASS round 1 checks SC1-t2-AC2 and SC1-t3-AC2: a real local BD build's class census (thread hops 2 and 3).

Usage: r1_bd_build_census.py <stage>, where stage is `silver` (the assets dimension, hop 2) or `gold` (the composition
artifacts and the client portal summary, hops 3-4). Reads
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R1_BD_<STAGE>_CENSUS_20260929.json, written from a REAL local
build of that stage on the latest BD day (no upload). Requires: rows > 0; every classified row's class came from the
canonical row (class_source 'etf-classifications'), none from bd-securities or a guess; unclassified rows counted and
named; the artifacts built listed; for gold, one real client's page values listed with each class and its source.

Prints BUILD-CENSUS <stage> rows=n unclassified=u or NOT-CENSUSED: <reason>.
"""
import json
import os
import sys


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in ("silver", "gold"):
        print("NOT-CENSUSED: usage r1_bd_build_census.py silver|gold")
        return 2
    stage = sys.argv[1]
    path = "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R1_BD_%s_CENSUS_20260929.json" % stage.upper()
    if not os.path.exists(path):
        print("NOT-CENSUSED: %s absent" % path)
        return 1
    with open(path, encoding="utf-8") as fh:
        d = json.load(fh)
    for k in ("as_of", "artifacts", "rows", "class_sources", "unclassified", "unclassified_names"):
        if k not in d:
            print("NOT-CENSUSED: census lacks %s" % k)
            return 1
    if not d["rows"] or not d["artifacts"]:
        print("NOT-CENSUSED: no rows or no artifacts built")
        return 1
    foreign = {s: n for s, n in d["class_sources"].items() if s != "etf-classifications" and n}
    if foreign:
        print("NOT-CENSUSED: classes from %s" % foreign)
        return 1
    if d["unclassified"] != len(d["unclassified_names"]):
        print("NOT-CENSUSED: unclassified %s but names %d" % (d["unclassified"], len(d["unclassified_names"])))
        return 1
    if stage == "gold":
        page = d.get("client_page") or {}
        if not page.get("client") or not page.get("values"):
            print("NOT-CENSUSED: gold census names no real client page and its values")
            return 1
        if any(v.get("class_source") != "etf-classifications" for v in page["values"] if v.get("asset_class")):
            print("NOT-CENSUSED: a classified page value came from outside the canonical table")
            return 1
    print("BUILD-CENSUS %s rows=%d unclassified=%d" % (stage, d["rows"], d["unclassified"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())

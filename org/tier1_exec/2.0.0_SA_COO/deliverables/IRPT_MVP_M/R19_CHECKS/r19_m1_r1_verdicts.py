"""Round 19 (~M) check IBM19-1-AC1: the three HELD ledgers' R1 legs are graded on served output.

Run from the repo (or worktree) root. Prints R1-GRADED or MISSING: <reason>.
"""
import json
import os
import sys

PATH = "org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R19_R1_READBACK_20260928.json"
SLUGS = {"cot-other-admission-m-20260925", "cot-cash-admission-m-20260925", "bd-securities-cot-new-p1-m-20260926"}
FIELDS = ("verdict", "expected", "measured", "served_objects", "run_evidence")


def main():
    if not os.path.exists(PATH):
        print("MISSING: %s absent" % PATH)
        return 1
    with open(PATH, encoding="utf-8") as fh:
        data = json.load(fh)
    legs = {row.get("slug"): row for row in data.get("legs") or []}
    if set(legs) != SLUGS:
        print("MISSING: legs %s != %s" % (sorted(legs), sorted(SLUGS)))
        return 1
    for slug, row in sorted(legs.items()):
        gaps = [f for f in FIELDS if not row.get(f)]
        if gaps:
            print("MISSING: %s lacks %s" % (slug, gaps))
            return 1
        if row["verdict"] not in ("PASS", "FAIL"):
            print("MISSING: %s verdict %r not PASS/FAIL" % (slug, row["verdict"]))
            return 1
        objs = row["served_objects"]
        if not all(o.get("uri", "").startswith("s3://") and o.get("version_id") for o in objs):
            print("MISSING: %s served_objects need uri + version_id each" % slug)
            return 1
    print("R1-GRADED " + " ".join("%s=%s" % (s, legs[s]["verdict"]) for s in sorted(legs)))
    return 0


if __name__ == "__main__":
    sys.exit(main())

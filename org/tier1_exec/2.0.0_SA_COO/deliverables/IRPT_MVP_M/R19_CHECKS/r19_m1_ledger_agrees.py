"""Round 19 (~M) check IBM19-1-AC2: each ledger's state agrees with its graded R1 verdict.

PASS -> the sentinel is gone and the entry reads CLOSED. FAIL -> the sentinel stays, R1 carries no proof, and the
verdict cites a surprise row id present in the investigation file. Run from the repo (or worktree) root.
Prints AGREES or DISAGREES: <reason>.
"""
import glob
import json
import os
import sys

VERDICTS = "org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R19_R1_READBACK_20260928.json"
SENTINEL = "org/critical_paths/.open_deploys/%s.json"
ENTRY = "org/critical_paths/change_management/*_%s_deploy_completion.md"
CHANNEL = "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md"


def main():
    if not os.path.exists(VERDICTS):
        print("DISAGREES: %s absent" % VERDICTS)
        return 1
    with open(VERDICTS, encoding="utf-8") as fh:
        legs = json.load(fh).get("legs") or []
    if len(legs) != 3:
        print("DISAGREES: %d legs graded, 3 expected" % len(legs))
        return 1
    with open(CHANNEL, encoding="utf-8") as fh:
        channel = fh.read()
    for row in legs:
        slug, verdict = row.get("slug"), row.get("verdict")
        entries = glob.glob(ENTRY % slug)
        if len(entries) != 1:
            print("DISAGREES: %s has %d entries" % (slug, len(entries)))
            return 1
        with open(entries[0], encoding="utf-8") as fh:
            closed = "**Status:** CLOSED" in fh.read()
        present = os.path.exists(SENTINEL % slug)
        if verdict == "PASS" and (present or not closed):
            print("DISAGREES: %s PASS but sentinel=%s closed=%s" % (slug, present, closed))
            return 1
        if verdict == "FAIL":
            if not present or closed:
                print("DISAGREES: %s FAIL but sentinel=%s closed=%s" % (slug, present, closed))
                return 1
            with open(SENTINEL % slug, encoding="utf-8") as fh:
                r1 = [leg for leg in json.load(fh)["legs"] if leg["id"] == "R1"]
            row_id = row.get("surprise_row") or ""
            if not r1 or r1[0].get("proof") or not row_id or row_id not in channel:
                print("DISAGREES: %s FAIL needs R1 unproven + a surprise row in the channel (row=%r)" % (slug, row_id))
                return 1
        if verdict not in ("PASS", "FAIL"):
            print("DISAGREES: %s verdict %r" % (slug, verdict))
            return 1
    print("AGREES " + " ".join("%s=%s" % (r["slug"], r["verdict"]) for r in legs))
    return 0


if __name__ == "__main__":
    sys.exit(main())

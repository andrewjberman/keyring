"""NFRA_TRNSPT -- address equality between two EXTRACTED transcripts bundles (2.0.0_SA_COO~T2).

  python addr_equal.py <extracted-old-bundle-dir> <extracted-new-bundle-dir>

Runs lib/opal_naming.address() from each bundle's own files (in a separate interpreter per bundle) for the Teams pull's 14
write addresses and the mail pull's 7, compares them, and runs a negative control (one altered address must break the
comparison). Prints ADDR-EQUAL-OK teams=14/14 mail=7/7 control=discriminates, or ADDR-EQUAL-FAIL <reason>; exit 0 / 1.
Reads only the two directories; no AWS, no network.
"""
import json
import subprocess
import sys

PROBE = r'''
import json, sys
sys.path.insert(0, sys.argv[1])
from lib import opal_naming as n
teams = []
for series in ("monday_meeting", "ocio_ic", "asset_management_ic", "research_meeting"):
    for tier, obj in (("bronze", "x.vtt"), ("bronze", "x.sidecar.json"), ("silver", "x.parquet")):
        teams.append(n.address("teams", "transcripts", tier, series, "date=2026-10-05", obj))
teams.append(n.address("teams", "transcripts", "state", "pull_runs", "run=2026-10-12T13:00:00Z", "run.json"))
teams.append(n.address("teams", "transcripts", "state", "listing_snapshots", "run=2026-10-12T13:00:00Z", "listing.json"))
mail = [
    n.address("outlook", "transcripts", "bronze", "analysis_commentary", "date=2026-10-08", "x.eml"),
    n.address("outlook", "transcripts", "bronze", "analysis_commentary", "date=2026-10-08", "x.sidecar.json"),
    n.address("outlook", "transcripts", "bronze", "analysis_commentary", "date=2026-10-08", "x.pdf"),
    n.address("outlook", "transcripts", "bronze", "analysis_commentary", "date=2026-10-08"),
    n.address("outlook", "transcripts", "silver", "analysis_commentary", "date=2026-10-08", "analysis_commentary.parquet"),
    n.address("outlook", "transcripts", "state", "pull_runs", "run=mail-20261008T233000Z", "run.json"),
    n.address("outlook", "transcripts", "state", "pull_runs", "run=mail-20261008T233000Z", "silver.json"),
]
print(json.dumps({"teams": teams, "mail": mail}))
'''


def probe(root):
    r = subprocess.run([sys.executable, "-c", PROBE, root], capture_output=True, text=True, timeout=120)
    if r.returncode != 0:
        raise RuntimeError("probe failed under %s: %s" % (root, (r.stderr or "").strip().splitlines()[-1:]))
    return json.loads(r.stdout)


def main(argv):
    if len(argv) != 3:
        print("usage: addr_equal.py <extracted-old-bundle-dir> <extracted-new-bundle-dir>")
        return 2
    try:
        old, new = probe(argv[1]), probe(argv[2])
    except Exception as exc:
        print("ADDR-EQUAL-FAIL %s" % exc)
        return 1
    t = sum(1 for a, b in zip(old["teams"], new["teams"]) if a == b)
    m = sum(1 for a, b in zip(old["mail"], new["mail"]) if a == b)
    altered = [a.replace("pull_runs", "pull_runz") for a in new["teams"]]
    control = altered != old["teams"]
    ok = (t == len(old["teams"]) == len(new["teams"]) == 14 and m == len(old["mail"]) == len(new["mail"]) == 7 and control)
    print("ADDR-EQUAL-%s teams=%d/%d mail=%d/%d control=%s" % (
        "OK" if ok else "FAIL", t, len(new["teams"]), m, len(new["mail"]), "discriminates" if control else "DID-NOT-DISCRIMINATE"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))

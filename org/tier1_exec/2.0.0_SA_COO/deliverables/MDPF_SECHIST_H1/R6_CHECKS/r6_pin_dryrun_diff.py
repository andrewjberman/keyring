"""MDPF_SECHIST round 6, SH-t-24 pair evidence: ONE dry run of the new gold + publisher code at HEAD, diffed against the page served today.

Read only. The S3 client is wrapped so any call other than get_object / list_objects_v2 / head_object raises; gold.run(publish=False) writes nothing;
the document is built in memory by the publisher's build_document and compared to platinum/etfs/positioning_data.json as served.

  python r6_pin_dryrun_diff.py <as_of>          (as_of must equal the served page's data_as_of for a like-for-like diff)
Prints, per portfolio and holding, every key whose value differs; ends with the counts and
  DRYRUN-DIFF <as_of> holdings=<n> changed_holdings=<k> new_holding_keys=<..> new_book_keys=<..> changed_cells=<c>
"""
from __future__ import annotations

import datetime as dt
import json
import subprocess
import sys
from pathlib import Path

import boto3

ROOT = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "data" / "etfs" / "scripts" / "gold"))
sys.path.insert(0, str(ROOT / "data" / "etfs" / "scripts" / "silver"))
sys.path.insert(0, str(ROOT / "infra" / "aws" / "lambda" / "v2_portal" / "_shared"))
import etf_positioning_gold as G  # noqa: E402
import etf_positioning_publisher as P  # noqa: E402

ALLOWED = ("get_object", "list_objects_v2", "head_object", "exceptions", "meta")


class ReadOnlyS3:
    def __init__(self, real):
        self._real = real

    def __getattr__(self, name):
        if name not in ALLOWED:
            raise RuntimeError("READ-ONLY GUARD: refused S3 call " + name)
        return getattr(self._real, name)


def main(as_of):
    real = boto3.client("s3")
    guard = ReadOnlyS3(real)
    G._s3 = lambda: guard
    P._s3 = lambda: guard
    served = json.loads(real.get_object(Bucket="opal-data-portal-v2", Key="platinum/etfs/positioning_data.json")["Body"].read())
    if as_of not in (served.get("data_as_of_spread") or []) and served.get("data_as_of") != as_of:
        print("DRYRUN-DIFF-BAD served page is not as of " + as_of + " (data_as_of=" + str(served.get("data_as_of")) + ")")
        return 1
    out = G.run(as_of_arg=as_of, publish=False)
    doc = P.build_document(out["book"], out["holding"], dt.datetime.now(dt.timezone.utc))
    new_h, new_b, cells, changed, total = set(), set(), 0, 0, 0
    for code, nb in doc["portfolios"].items():
        sb = (served.get("portfolios") or {}).get(code)
        if sb is None:
            print("NEW BOOK " + code)
            return 1
        for k in sorted(set(nb) | set(sb)):
            if k == "holdings":
                continue
            if k not in sb:
                new_b.add(k)
                print("book " + code + " NEW KEY " + k + " = " + json.dumps(nb[k], sort_keys=True))
            elif k not in nb:
                print("book " + code + " DROPPED KEY " + k)
                return 1
            elif nb[k] != sb[k]:
                print("book " + code + " key " + k + " DIFFERS")
                cells += 1
        shold = {h["ticker"]: h for h in sb.get("holdings") or []}
        nhold = {h["ticker"]: h for h in nb.get("holdings") or []}
        if set(shold) != set(nhold):
            print("book " + code + " holdings set differs: -" + str(sorted(set(shold) - set(nhold))) + " +" + str(sorted(set(nhold) - set(shold))))
            return 1
        for t, nh in nhold.items():
            total += 1
            sh = shold[t]
            diffs = []
            for k in sorted(set(nh) | set(sh)):
                if k not in sh:
                    new_h.add(k)
                    diffs.append("NEW " + k + "=" + json.dumps(nh[k]))
                elif k not in nh:
                    diffs.append("DROPPED " + k)
                elif nh[k] != sh[k]:
                    if k == "returns":
                        for w in sorted(nh[k]):
                            if nh[k][w] != sh[k].get(w):
                                cells += 1
                                diffs.append("returns." + w + " " + str(sh[k].get(w)) + " -> " + str(nh[k][w]))
                    else:
                        cells += 1
                        diffs.append(k + " " + json.dumps(sh[k]) + " -> " + json.dumps(nh[k]))
            if diffs:
                changed += 1
                print("holding " + code + "/" + t + ": " + "; ".join(diffs))
    print("DRYRUN-DIFF " + as_of + " holdings=" + str(total) + " changed_holdings=" + str(changed)
          + " new_holding_keys=" + ",".join(sorted(new_h)) + " new_book_keys=" + ",".join(sorted(new_b)) + " changed_cells=" + str(cells))
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("DRYRUN-DIFF-BAD usage: r6_pin_dryrun_diff.py <as_of>")
        sys.exit(2)
    sys.exit(main(sys.argv[1]))

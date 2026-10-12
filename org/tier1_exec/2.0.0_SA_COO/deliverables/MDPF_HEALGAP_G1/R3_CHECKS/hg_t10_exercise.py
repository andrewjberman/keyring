#!/usr/bin/env python3
"""HG-t-10 reads: the FWD-3 exercise on the sentinel target (half @de14a3a7b0, CTO ADDENDUM 7 @923099fc24). Read-only; AWS CLI reads only.

  python hg_t10_exercise.py target                      -> TARGET-CLEAR | TARGET-INDUCED   (rule cot-bronze-complete, target cot-rebalancer-runner-reattempt)
  python hg_t10_exercise.py partial  --date D           -> PARTIAL-OK | PARTIAL-BAD         (step 2: the induced hole)
  python hg_t10_exercise.py snapshot --date D --out F   -> SNAPSHOT-OK                      (key sets of the two PRESENT feeds, before the repair)
  python hg_t10_exercise.py healed   --date D --snapshot F -> HEALED-OK | HEALED-BAD        (step 4: exactly the named feed landed, nothing else changed)

Exit 0 on OK/CLEAR, 1 on BAD/INDUCED. Every verdict line prints its denominator.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys

ROOT = subprocess.check_output(["git", "rev-parse", "--show-toplevel"],
                               cwd=os.path.dirname(os.path.abspath(__file__))).decode().strip()
AWS = ["bash", os.path.join(ROOT, ".tools", "aws")]   # a shell script: python on Windows cannot exec it directly
BUCKET = "opal-data-assets"
SCOPE = "blackdiamond/cottonwood/"
BRONZE = SCOPE + "bronze/"
META = SCOPE + "meta/"
FEEDS = ("rebalancer_models", "rebalancer_accounts", "rebalancer_model_detail")
RULE = "cot-bronze-complete"
TARGET_ID = "cot-rebalancer-runner-reattempt"


def aws(*args):
    out = subprocess.run(AWS + list(args), capture_output=True, text=True)
    if out.returncode != 0:
        raise SystemExit("AWS-READ-FAILED rc=%d %s" % (out.returncode, out.stderr.strip()[:200]))
    return out.stdout


def get_json(key):
    path = os.path.join(os.environ.get("TEMP", "/tmp"), "hg_t10_%s.json" % key.replace("/", "_"))
    r = subprocess.run(AWS + ["s3api", "get-object", "--bucket", BUCKET, "--key", key, path],
                       capture_output=True, text=True)
    if r.returncode != 0:
        return None
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def keyset(feed, date):
    prefix = "%s%s/%s/" % (BRONZE, feed, date)
    out = aws("s3api", "list-objects-v2", "--bucket", BUCKET, "--prefix", prefix, "--output", "json")
    d = json.loads(out) if out.strip() else {}
    return sorted((o["Key"], o["Size"]) for o in (d.get("Contents") or []))


def stamp_exists(date):
    out = aws("s3api", "list-objects-v2", "--bucket", BUCKET, "--prefix", "%s%s-complete.json" % (META, date),
              "--output", "json")
    d = json.loads(out) if out.strip() else {}
    return bool(d.get("Contents"))


def cmd_target(_a):
    out = aws("events", "list-targets-by-rule", "--rule", RULE, "--output", "json")
    targets = json.loads(out).get("Targets", [])
    t = [x for x in targets if x.get("Id") == TARGET_ID]
    if len(t) != 1:
        print("TARGET-BAD target %s found %d time(s) among %d target(s) of rule %s" % (TARGET_ID, len(t), len(targets), RULE))
        return 1
    inp = t[0].get("Input")
    induced = "induce" in (inp or "")
    print("%s input=%s denominator=1 target of %d on rule %s" % ("TARGET-INDUCED" if induced else "TARGET-CLEAR", inp, len(targets), RULE))
    return 1 if induced else 0


def cmd_partial(a):
    res = get_json("%s%s-result.json" % (META, a.date))
    bad = []
    if res is None:
        print("PARTIAL-BAD no result object for %s" % a.date)
        return 1
    feeds = res.get("feeds") or {}
    if res.get("verdict") != "PARTIAL":
        bad.append("verdict %r, not PARTIAL" % res.get("verdict"))
    if (feeds.get("rebalancer_accounts") or {}).get("status") != "missing":
        bad.append("accounts status %r, not missing" % (feeds.get("rebalancer_accounts") or {}).get("status"))
    for f in ("rebalancer_models", "rebalancer_model_detail"):
        if (feeds.get(f) or {}).get("status") != "arrived":
            bad.append("%s status %r, not arrived" % (f, (feeds.get(f) or {}).get("status")))
    if stamp_exists(a.date):
        bad.append("a completion stamp exists for %s" % a.date)
    if keyset("rebalancer_accounts", a.date):
        bad.append("accounts keys are present under the day prefix")
    if bad:
        print("PARTIAL-BAD " + "; ".join(bad))
        return 1
    print("PARTIAL-OK %s: accounts missing, models and detail arrived, no stamp, no accounts keys (4 conditions of 4)" % a.date)
    return 0


def cmd_snapshot(a):
    snap = {f: keyset(f, a.date) for f in ("rebalancer_models", "rebalancer_model_detail")}
    with open(a.out, "w", encoding="utf-8", newline="\n") as fh:
        json.dump({"date": a.date, "present_feeds": snap}, fh, indent=2, sort_keys=True)
    print("SNAPSHOT-OK %s models=%d key(s) model_detail=%d key(s) -> %s"
          % (a.date, len(snap["rebalancer_models"]), len(snap["rebalancer_model_detail"]), a.out))
    return 0


def cmd_healed(a):
    snap = json.load(open(a.snapshot, encoding="utf-8"))
    bad = []
    if snap.get("date") != a.date:
        bad.append("snapshot is for %s, not %s" % (snap.get("date"), a.date))
    res = get_json("%s%s-result.json" % (META, a.date))
    if res is None:
        bad.append("no result object")
    else:
        if res.get("verdict") != "COMPLETE":
            bad.append("verdict %r, not COMPLETE" % res.get("verdict"))
        acc = (res.get("feeds") or {}).get("rebalancer_accounts") or {}
        if acc.get("healed_at") not in (None, ""):
            bad.append("accounts healed_at is %r (the R2-1 rule reads null live)" % acc.get("healed_at"))
    if not stamp_exists(a.date):
        bad.append("no completion stamp")
    if not keyset("rebalancer_accounts", a.date):
        bad.append("accounts keys absent")
    changed = []
    for f in ("rebalancer_models", "rebalancer_model_detail"):
        now = [tuple(x) for x in keyset(f, a.date)]
        was = [tuple(x) for x in snap["present_feeds"][f]]
        if now != was:
            changed.append("%s: %d key(s) before, %d after, differing %d"
                           % (f, len(was), len(now), len(set(now) ^ set(was))))
    if changed:
        bad.append("present feeds' (key, size) sets changed -- " + "; ".join(changed))
    if bad:
        print("HEALED-BAD " + "; ".join(bad))
        return 1
    print("HEALED-OK %s: COMPLETE, stamp present, accounts keys present, healed_at null, models and detail (key,size) sets "
          "equal to the pre-repair snapshot (6 conditions of 6)" % a.date)
    return 0


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("target")
    for name in ("partial", "snapshot", "healed"):
        p = sub.add_parser(name)
        p.add_argument("--date", required=True)
        if name == "snapshot":
            p.add_argument("--out", required=True)
        if name == "healed":
            p.add_argument("--snapshot", required=True)
    a = ap.parse_args()
    return {"target": cmd_target, "partial": cmd_partial, "snapshot": cmd_snapshot, "healed": cmd_healed}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())

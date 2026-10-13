#!/usr/bin/env python3
"""fabric-gitstate.py -- one GITSTATE record per box-sync pass, so a reader with S3 and no git can say where a commit is.

NFRA_MCPORTAL FWD-16 (1.0.0_SA_CTO~O ruling msg 32404, Q2 = a; R6_DECOMP_DRAFT.md @54c2fd91b6). Taken by 4.0.0_SA_CRO
(msg 107760). The MC portal's gateway reads S3 only, so it cannot run git; this record carries what git alone knows.
Called by .tools/box-sync.sh at the end of every non-dry pass (in the background, so the pass is not slowed). Reads the
refs box-sync just fetched; fetches nothing and writes nothing to git.

    python .tools/fabric-gitstate.py --mode box --rc 0 --serial <S> --note "<row note>"   put the record
    python .tools/fabric-gitstate.py --dry-run                                           print it, put nothing

THE RECORD, s3://opal-313476888478-globgrph/fabric/activity/v1/gitstate/box=<B>/<stamp>.json and .../latest.json:
  box_head        refs/heads/box/<B>          (committed on this box)
  origin_box_head refs/remotes/origin/box/<B> (pushed to its box branch)
  trunk_head      refs/remotes/origin/CLOUD   (on the trunk, as last fetched)
  unpushed            non-merge commits on box_head and not on origin_box_head
  pushed_not_on_trunk non-merge commits on origin_box_head and not on trunk_head
  behind_trunk        commits on trunk_head and not on box_head
Each list carries its full count and at most CAP shas (capped=true when cut). A commit of this box in neither list is on
the trunk, as of `at`. A ref this box cannot read is null and named in `unread`, never an empty list.
THE INTEGRATE POINTER, <PREFIX>/box=<B>/last_integrate.json = {"at","rc","note"}: written on --mode integrate ONLY (a box,
manual or dry pass never writes or deletes it), same bucket, PREFIX and client as the record; rc is the --rc box-sync
passed in, at is the stamped record's own at, note is the record's pass note cut to 200 chars. A failed pointer put fails
nothing else. Five conditions: org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/CONSENT_NFRA_MCPORTAL_C17_E1_LAST_INTEGRATE_POINTER_20261013.md
LAST line: FABRIC-GITSTATE box=<B> unpushed=<n> pushed_not_on_trunk=<n> behind_trunk=<n> put=<yes|no:<why>> pointer=<n/a|yes|no:<Exc>>
"""
from __future__ import annotations

import argparse
import datetime
import json
import os
import subprocess
import sys

TOOLS = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(TOOLS)
BUCKET = "opal-313476888478-globgrph"
PREFIX = "fabric/activity/v1/gitstate"
SCHEMA = "fabric-gitstate/1"
CAP = 500


def git(*args):
    r = subprocess.run(["git", "-C", ROOT] + list(args), capture_output=True, text=True, encoding="utf-8",
                       errors="replace", timeout=60)
    return r.returncode, r.stdout.strip()


def ref(name):
    rc, out = git("rev-parse", "-q", "--verify", name)
    return out if rc == 0 and out else None


def this_box():
    env = os.environ.get("AGENTBUS_DEVICE", "").strip()
    if env:
        return env
    sys.path.insert(0, os.path.join(ROOT, "lib"))
    try:
        import devices  # noqa: E402
        name, _basis = devices.this_device()
        return name
    except Exception:  # noqa: BLE001
        return None


def between(a, b, merges=False):
    """Commits on b and not on a: {count, shas (at most CAP), capped}, or None when either end is unreadable."""
    if not a or not b:
        return None
    flags = [] if merges else ["--no-merges"]
    rc, out = git("rev-list", *flags, "%s..%s" % (a, b))
    if rc != 0:
        return None
    shas = [s for s in out.splitlines() if s]
    return {"count": len(shas), "shas": shas[:CAP], "capped": len(shas) > CAP}


def record(box, mode, rc, serial, note, now):
    local, origin_box, trunk = ref("refs/heads/box/%s" % box), ref("refs/remotes/origin/box/%s" % box), \
        ref("refs/remotes/origin/CLOUD")
    unread = [n for n, v in (("box_head", local), ("origin_box_head", origin_box), ("trunk_head", trunk)) if v is None]
    behind = between(local, trunk, merges=True)
    return {"schema": SCHEMA, "box": box, "at": now.strftime("%Y-%m-%dT%H:%M:%SZ"), "pass": {"mode": mode, "rc": rc,
            "serial": serial, "note": note}, "box_branch": "box/%s" % box, "box_head": local, "origin_box_head": origin_box,
            "trunk_head": trunk, "unpushed": between(origin_box, local), "pushed_not_on_trunk": between(trunk, origin_box),
            "behind_trunk": behind["count"] if behind else None, "unread": unread}


def put(doc, now):
    import boto3
    from botocore.config import Config
    s3 = boto3.client("s3", config=Config(connect_timeout=5, read_timeout=15, retries={"max_attempts": 2}))
    body = (json.dumps(doc, indent=1, ensure_ascii=True) + "\n").encode("ascii")
    base = "%s/box=%s" % (PREFIX, doc["box"])
    for key in ("%s/%s.json" % (base, now.strftime("%Y%m%dT%H%M%SZ")), "%s/latest.json" % base):
        s3.put_object(Bucket=BUCKET, Key=key, Body=body, ContentType="application/json")
    if doc["pass"]["mode"] != "integrate":
        return "n/a"
    try:
        ptr = {"at": doc["at"], "rc": doc["pass"]["rc"], "note": str(doc["pass"]["note"])[:200]}
        pbody = (json.dumps(ptr, indent=1, ensure_ascii=True) + chr(10)).encode("ascii")
        s3.put_object(Bucket=BUCKET, Key="%s/last_integrate.json" % base, Body=pbody, ContentType="application/json")
        return "yes"
    except Exception as exc:  # noqa: BLE001
        return "no:%s" % type(exc).__name__


def main(argv):
    ap = argparse.ArgumentParser(prog="fabric-gitstate.py", description=__doc__.split("\n")[0])
    ap.add_argument("--mode", default="manual")
    ap.add_argument("--rc", type=int, default=0)
    ap.add_argument("--serial", default=os.environ.get("OPAL_AGENT_SERIAL", ""))
    ap.add_argument("--note", default="")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args(argv)
    box = this_box()
    if not box:
        print("FABRIC-GITSTATE box=unresolved put=no:box-unresolved")
        return 2
    now = datetime.datetime.now(datetime.timezone.utc)
    doc = record(box, args.mode, args.rc, args.serial, args.note, now)
    if args.dry_run:
        print(json.dumps(doc, indent=1)[:4000])
        verdict = "no:dry-run"
        pointer = "n/a"
    else:
        try:
            pointer = put(doc, now)
            verdict = "yes"
        except Exception as exc:  # noqa: BLE001
            verdict = "no:%s" % type(exc).__name__
            pointer = "n/a"

    def n(k):
        return "?" if doc[k] is None else doc[k]["count"]
    print("FABRIC-GITSTATE box=%s unpushed=%s pushed_not_on_trunk=%s behind_trunk=%s put=%s pointer=%s" % (
        box, n("unpushed"), n("pushed_not_on_trunk"), "?" if doc["behind_trunk"] is None else doc["behind_trunk"], verdict,
        pointer))
    return 0 if verdict in ("yes", "no:dry-run") else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

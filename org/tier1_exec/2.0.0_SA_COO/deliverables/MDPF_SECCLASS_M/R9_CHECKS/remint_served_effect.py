#!/usr/bin/env python3
"""remint_served_effect.py -- MDPF_SECCLASS batch 183 ONE packet, the half's owed measurement: the served effect of the
Holdings producer re-mint, ONE firm per run (Andrew-direct 2026-10-03 ~22:1xZ card 3: heavy reads one at a time, foreground).

READ-ONLY. No S3 write: each producer runs WITHOUT --upload (its publisher.begin/publish run only under upload) and lands its
bytes under a local scratch directory (--local-out).

A PAIRED build over the SAME live sources, back to back, so a re-captured source cannot read as a code effect (the first
version of this script compared against the served publication and every node differed on the overlay clock and amounts):
  served tree   the firm's SERVED producer bundle (irpt/<firm>/code/gold/investor-reporting-holdings.tar.gz, current
                version), extracted -- what the next scheduled publication would run today
  CLOUD tree    the SAME member paths at CLOUD HEAD (git show HEAD:<path>) -- what the re-mint ships
Both run holdings_snapshot.py --firms <firm> --as-of <the served publication's date> --local-out <scratch>.

Compares the two builds by node_id: counts (common / only-in-one / equal / differing), the flattened fields that differ
(tallied), every class-field change, the account totals, and the holdings of the packet's 32 rows (MOVE + WRITE keys of
MULTI_ASSET_ROW_SET_20261003.tsv). Writes REMINT_SERVED_EFFECT_<firm>_20261003.json.

Usage (repo root): python .../R9_CHECKS/remint_served_effect.py <49financial|inflection|cottonwood>
"""
from __future__ import annotations

import collections
import glob
import io
import json
import subprocess
import sys
import tarfile
import tempfile
from pathlib import Path

import boto3
import pyarrow.parquet as pq

FIRMS = {"49financial": "opal-data-49financial", "inflection": "opal-data-inflection", "cottonwood": "opal-data-cottonwood"}
ROOT = Path(__file__).resolve().parents[6]
PRODUCER_REL = Path("data/assets/scripts/gold/investor_reporting")
HERE = Path(__file__).resolve().parent
ROW_SET = HERE / "MULTI_ASSET_ROW_SET_20261003.tsv"
CLASS_FIELDS = ("asset_class", "asset_sub_class", "class", "sub_class", "classified_by")
s3 = boto3.client("s3", region_name="us-east-1")


def get(bucket, key, ver=None):
    kw = {"Bucket": bucket, "Key": key}
    if ver:
        kw["VersionId"] = ver
    for attempt in range(6):
        try:
            return s3.get_object(**kw)["Body"].read()
        except Exception:  # noqa: BLE001 -- body reads time out on this link; re-read
            if attempt == 5:
                raise


def nodes_of(parquet_bytes):
    return [json.loads(s) for s in pq.read_table(io.BytesIO(parquet_bytes), columns=["node_json"]).column("node_json").to_pylist()]


def served_date(firm):
    cur = json.loads(get(FIRMS[firm], f"irpt/{firm}/platinum/holdings/current/manifest.json"))
    return cur["latest_date"]


def served_tar(firm):
    key = f"irpt/{firm}/code/gold/investor-reporting-holdings.tar.gz"
    head = s3.head_object(Bucket=FIRMS[firm], Key=key)
    return key, head["VersionId"], tarfile.open(fileobj=io.BytesIO(get(FIRMS[firm], key, head["VersionId"])))


def build(tree, firm, date):
    out = Path(tree) / "_out"
    cmd = [sys.executable, "holdings_snapshot.py", "--firms", firm, "--as-of", date, "--local-out", str(out)]
    run = subprocess.run(cmd, cwd=str(Path(tree) / PRODUCER_REL), capture_output=True, text=True, timeout=3000)
    if run.returncode != 0:
        return None, {"rc": run.returncode, "stderr_tail": run.stderr.strip().splitlines()[-12:]}
    parquets = glob.glob(str(out / "**" / "*.parquet"), recursive=True)
    assert len(parquets) == 1, parquets
    try:
        res = json.loads(run.stdout[run.stdout.index("{"):])["results"][0]
    except Exception:  # noqa: BLE001
        res = {}
    meta = {k: res.get(k) for k in ("business_date", "node_count", "unique_account_count", "reconcile_ok",
                                    "reconcile_after", "schema_valid")}
    return nodes_of(Path(parquets[0]).read_bytes()), meta


def flat(d, pre=""):
    out = {}
    for k, v in (d or {}).items():
        key = f"{pre}{k}"
        if isinstance(v, dict):
            out.update(flat(v, key + "."))
        else:
            out[key] = json.dumps(v, sort_keys=True, default=str)
    return out


def row_keys():
    keys = {}
    for line in ROW_SET.read_text(encoding="utf-8").splitlines():
        if line.startswith("#") or not line.strip():
            continue
        parts = line.split("\t")
        if parts[0] in ("MOVE", "WRITE"):
            keys[parts[1].replace("CUSIP:", "")] = parts[0]
    return keys


def main(firm):
    date = served_date(firm)
    key, ver, tf = served_tar(firm)
    members = [m for m in tf.getmembers() if m.isfile()]
    print(f"{firm}: served date {date}; served bundle {key} {ver} ({len(members)} members)", flush=True)
    with tempfile.TemporaryDirectory(prefix=f"remint_{firm}_") as tmp:
        served_tree, cloud_tree = Path(tmp) / "served", Path(tmp) / "cloud"
        tf.extractall(served_tree, members=members)  # noqa: S202 -- our own served bundle, repo-relative member paths
        missing_at_head = []
        for m in members:
            blob = subprocess.run(["git", "-C", str(ROOT), "show", f"HEAD:{m.name}"], capture_output=True)
            if blob.returncode != 0:
                missing_at_head.append(m.name)
                continue
            dest = cloud_tree / m.name
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(blob.stdout)
        S, s_meta = build(served_tree, firm, date)
        print("served-tree build", s_meta, flush=True)
        B, b_meta = build(cloud_tree, firm, date)
        print("CLOUD-tree build", b_meta, flush=True)
    out = {"claim": "measured (paired local builds over the same live sources, no upload)", "firm": firm,
           "served_date": date, "served_bundle": {"key": key, "version": ver, "members": len(members)},
           "members_missing_at_head": missing_at_head, "served_tree_build": s_meta, "cloud_tree_build": b_meta}
    if S is not None and B is not None:
        Sm, Bm = {n["node_id"]: n for n in S}, {n["node_id"]: n for n in B}
        common = Sm.keys() & Bm.keys()
        fields, class_changes, differing = collections.Counter(), [], 0
        for nid in common:
            a, b = flat(Sm[nid]), flat(Bm[nid])
            changed = [k for k in a.keys() | b.keys() if a.get(k) != b.get(k)]
            if changed:
                differing += 1
                fields.update(changed)
                cls = [k for k in changed if k.rsplit(".", 1)[-1] in CLASS_FIELDS]
                if cls:
                    class_changes.append({"node_id": nid, "changes": {k: [a.get(k), b.get(k)] for k in cls}})

        def acct_totals(nodes):
            return {n["node_id"]: round(float((n.get("amount") or {}).get("value") or 0.0), 2)
                    for n in nodes if n.get("node_kind") == "ACCOUNT"}
        sa, ba = acct_totals(S), acct_totals(B)
        keys = row_keys()
        held = collections.defaultdict(lambda: [0, 0.0])
        for n in S:
            blob = json.dumps(n, default=str)
            for k in keys:
                if f'"{k}"' in blob:
                    held[k][0] += 1
                    held[k][1] = round(held[k][1] + float(((n.get("amount") or {}).get("value")) or 0.0), 2)
        out.update({
            "nodes": {"served_tree": len(Sm), "cloud_tree": len(Bm), "common": len(common),
                      "only_served_tree": len(Sm.keys() - Bm.keys()), "only_cloud_tree": len(Bm.keys() - Sm.keys()),
                      "equal": len(common) - differing, "differing": differing},
            "differing_fields_top": fields.most_common(25),
            "class_change_count": len(class_changes), "class_changes": class_changes[:200],
            "unmatched_by_account": dict(collections.Counter(nid.split(":")[0] for nid in
                                                         (Sm.keys() ^ Bm.keys())).most_common(25)),
            "unmatched_account_count": len({nid.split(":")[0] for nid in (Sm.keys() ^ Bm.keys())}),
            "only_served_tree_sample": sorted(Sm.keys() - Bm.keys())[:15],
            "only_cloud_tree_sample": sorted(Bm.keys() - Sm.keys())[:15],
            "account_totals": {"accounts": len(sa), "equal": sum(1 for a in sa if ba.get(a) == sa[a]),
                               "differ": sorted((a, sa[a], ba.get(a)) for a in sa if ba.get(a) != sa[a])[:25],
                               "sum_served_tree": round(sum(sa.values()), 2), "sum_cloud_tree": round(sum(ba.values()), 2)},
            "packet_rows_held": {k: v for k, v in held.items()},
        })
    path = HERE / f"REMINT_SERVED_EFFECT_{firm}_20261003.json"
    path.write_text(json.dumps(out, indent=1, default=str), encoding="utf-8")
    print(json.dumps({k: out.get(k) for k in ("nodes", "differing_fields_top", "class_change_count", "account_totals")},
                     indent=1, default=str)[:3000])
    print("WROTE", path)
    return 0 if (S is not None and B is not None) else 1


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in FIRMS:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1]))

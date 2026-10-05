#!/usr/bin/env python3
"""remint_served_effect_light.py -- the same paired measurement as remint_served_effect.py (CTO batch 244 method: the served
tree admits multi_asset, the one token of 4cc72587d6), in a LOW-MEMORY form for 49 Financial (Andrew-direct 2026-10-04
~22:0xZ card 4: this packet's 49F paired read, one firm at a time in the foreground; the first 49F run was stopped by the
memory reaper while its comparing process held one build's nodes as dicts).

READ-ONLY; no --upload; each tree builds in its own producer process. The comparing process never holds a whole build:
  pass 1  stream the served-tree parquet -> {node_id: sha1(node_json)}, ACCOUNT totals, the packet keys' holdings
  pass 2  stream the CLOUD-tree parquet  -> ids only in one side, ids whose hash differs (their JSON kept), ACCOUNT totals
  pass 3  stream the served-tree parquet -> the served JSON of the differing ids only; diff those field by field
Writes REMINT_SERVED_EFFECT_<firm>_LIGHT_20261004.json.

Usage (repo root): python .../R9_CHECKS/remint_served_effect_light.py <firm>
"""
from __future__ import annotations

import collections
import glob
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import pyarrow.parquet as pq

sys.path.insert(0, str(Path(__file__).resolve().parent))
import remint_served_effect as base  # noqa: E402

BATCH = 4000


def build(tree, firm, date, keep_dir):
    out = Path(tree) / "_out"
    cmd = [sys.executable, "holdings_snapshot.py", "--firms", firm, "--as-of", date, "--local-out", str(out)]
    run = subprocess.run(cmd, cwd=str(Path(tree) / base.PRODUCER_REL), capture_output=True, text=True, timeout=5400)
    if run.returncode != 0:
        return None, {"rc": run.returncode, "stderr_tail": run.stderr.strip().splitlines()[-12:]}
    parquets = glob.glob(str(out / "**" / "*.parquet"), recursive=True)
    assert len(parquets) == 1, parquets
    kept = Path(keep_dir) / (Path(tree).name + ".parquet")
    shutil.copyfile(parquets[0], kept)
    try:
        res = json.loads(run.stdout[run.stdout.index("{"):])["results"][0]
    except Exception:  # noqa: BLE001
        res = {}
    return kept, {k: res.get(k) for k in ("business_date", "node_count", "unique_account_count", "reconcile_ok",
                                          "reconcile_after", "schema_valid")}


def stream(path):
    for batch in pq.ParquetFile(str(path)).iter_batches(batch_size=BATCH, columns=["node_json"]):
        yield from batch.column(0).to_pylist()


def node_id(s):
    return json.loads(s)["node_id"]


def class_sum_compare(s_cls, b_cls, unmatched):
    """Per account, the SECURITY amount by asset_class on each side (cents). CTO batch 240 condition 2: each regrouped
    account shows 0 class change and an equal total -- read here as an equal class vector."""
    accts = {a for a, _ in s_cls} | {a for a, _ in b_cls}
    def vec(d, a):
        return {c: round(v, 2) for (aa, c), v in d.items() if aa == a and round(v, 2) != 0.0}
    differ = [a for a in sorted(accts) if vec(s_cls, a) != vec(b_cls, a)]
    return {"accounts": len(accts), "equal_class_vectors": len(accts) - len(differ),
            "differ": [{"account": a, "served": vec(s_cls, a), "cloud": vec(b_cls, a)} for a in differ[:15]],
            "regrouped_accounts": {a: {"equal": vec(s_cls, a) == vec(b_cls, a), "classes": vec(b_cls, a)}
                                   for a in sorted(unmatched)}}


def main(firm):
    date = base.served_date(firm)
    key, ver, tf = base.served_tar(firm)
    members = [m for m in tf.getmembers() if m.isfile()]
    print(f"{firm}: served date {date}; served bundle {key} {ver} ({len(members)} members)", flush=True)
    keep = Path(tempfile.mkdtemp(prefix=f"remint_light_{firm}_keep_"))
    with tempfile.TemporaryDirectory(prefix=f"remint_light_{firm}_") as tmp:
        served_tree, cloud_tree = Path(tmp) / "served", Path(tmp) / "cloud"
        tf.extractall(served_tree, members=members)  # noqa: S202 -- our own served bundle, repo-relative member paths
        del tf
        print("served tree: admit patch at line", base.admit_multi_asset(served_tree), flush=True)
        missing = []
        for m in members:
            blob = subprocess.run(["git", "-C", str(base.ROOT), "show", f"HEAD:{m.name}"], capture_output=True)
            if blob.returncode != 0:
                missing.append(m.name)
                continue
            dest = cloud_tree / m.name
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(blob.stdout)
        s_path, s_meta = build(served_tree, firm, date, keep)
        print("served-tree build", s_meta, flush=True)
        b_path, b_meta = build(cloud_tree, firm, date, keep) if s_path else (None, None)
        print("CLOUD-tree build", b_meta, flush=True)
    out = {"claim": "measured (paired local builds over the same live sources, no upload; streamed comparison)",
           "firm": firm, "method": "CTO batch 244: served tree admits multi_asset (4cc72587d6's one token)",
           "served_date": date, "served_bundle": {"key": key, "version": ver, "members": len(members)},
           "members_missing_at_head": missing, "served_tree_build": s_meta, "cloud_tree_build": b_meta}
    if s_path and b_path:
        keys = base.row_keys()
        s_hash, s_acct, held = {}, {}, collections.defaultdict(lambda: [0, 0.0])
        s_cls, b_cls = collections.defaultdict(float), collections.defaultdict(float)  # (account, class) -> SECURITY amount
        for s in stream(s_path):                                                   # pass 1
            d = json.loads(s)
            s_hash[d["node_id"]] = hashlib.sha1(s.encode("utf-8")).hexdigest()
            if d.get("node_kind") == "ACCOUNT":
                s_acct[d["node_id"]] = round(float((d.get("amount") or {}).get("value") or 0.0), 2)
            if d.get("node_kind") == "SECURITY":
                s_cls[(d["node_id"].split(":")[0], d.get("asset_class"))] += float((d.get("amount") or {}).get("value") or 0.0)
            for k in keys:
                if f'"{k}"' in s:
                    held[k][0] += 1
                    held[k][1] = round(held[k][1] + float((d.get("amount") or {}).get("value") or 0.0), 2)
            del d
        b_ids, b_acct, diff_json = set(), {}, {}
        for s in stream(b_path):                                                   # pass 2
            d = json.loads(s)
            nid = d["node_id"]
            b_ids.add(nid)
            if d.get("node_kind") == "ACCOUNT":
                b_acct[nid] = round(float((d.get("amount") or {}).get("value") or 0.0), 2)
            if d.get("node_kind") == "SECURITY":
                b_cls[(nid.split(":")[0], d.get("asset_class"))] += float((d.get("amount") or {}).get("value") or 0.0)
            if nid in s_hash and s_hash[nid] != hashlib.sha1(s.encode("utf-8")).hexdigest():
                diff_json[nid] = d
        served_diff = {}
        for s in stream(s_path):                                                   # pass 3
            nid = node_id(s)
            if nid in diff_json:
                served_diff[nid] = json.loads(s)
        fields, class_changes = collections.Counter(), []
        for nid, b in diff_json.items():
            a, bb = base.flat(served_diff[nid]), base.flat(b)
            changed = [k for k in a.keys() | bb.keys() if a.get(k) != bb.get(k)]
            fields.update(changed)
            cls = [k for k in changed if k.rsplit(".", 1)[-1] in base.CLASS_FIELDS]
            if cls:
                class_changes.append({"node_id": nid, "changes": {k: [a.get(k), bb.get(k)] for k in cls}})
        s_ids = set(s_hash)
        only_s, only_b = s_ids - b_ids, b_ids - s_ids
        unmatched_accts = collections.Counter(n.split(":")[0] for n in (only_s | only_b))
        out.update({
            "nodes": {"served_tree": len(s_ids), "cloud_tree": len(b_ids), "common": len(s_ids & b_ids),
                      "only_served_tree": len(only_s), "only_cloud_tree": len(only_b),
                      "equal": len(s_ids & b_ids) - len(diff_json), "differing": len(diff_json)},
            "differing_fields_top": fields.most_common(25),
            "class_change_count": len(class_changes), "class_changes": class_changes[:200],
            "unmatched_account_count": len(unmatched_accts), "unmatched_by_account": dict(unmatched_accts.most_common(25)),
            "account_totals": {"accounts": len(s_acct), "equal": sum(1 for a in s_acct if b_acct.get(a) == s_acct[a]),
                               "differ": sorted((a, s_acct[a], b_acct.get(a)) for a in s_acct if b_acct.get(a) != s_acct[a])[:25],
                               "sum_served_tree": round(sum(s_acct.values()), 2), "sum_cloud_tree": round(sum(b_acct.values()), 2)},
            "packet_rows_held": dict(held),
            "class_sums_by_account": class_sum_compare(s_cls, b_cls, set(unmatched_accts)),
        })
    shutil.rmtree(keep, ignore_errors=True)
    path = base.HERE / f"REMINT_SERVED_EFFECT_{firm}_LIGHT_20261004.json"
    path.write_text(json.dumps(out, indent=1, default=str), encoding="utf-8")
    print(json.dumps({k: out.get(k) for k in ("nodes", "class_change_count", "unmatched_account_count", "account_totals")},
                     indent=1, default=str)[:2500])
    print("WROTE", path)
    return 0 if (s_path and b_path) else 1


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in base.FIRMS:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1]))

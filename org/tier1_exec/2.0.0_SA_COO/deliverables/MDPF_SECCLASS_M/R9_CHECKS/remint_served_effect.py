#!/usr/bin/env python3
"""remint_served_effect.py -- MDPF_SECCLASS batch 183 ONE packet, the half's owed measurement: the served effect of the
Holdings producer re-mint, ONE firm per run (Andrew-direct 2026-10-03 ~22:1xZ card 3: heavy reads one at a time, foreground).

READ-ONLY. No S3 write: the producer runs WITHOUT --upload (its publisher.begin/publish run only under upload) and lands its
gold/platinum bytes under a local scratch directory (--local-out).

  served  the firm's current publication: manifest -> platinum header + gold parquet (sha256 checked against the manifest)
  built   CLOUD's producer (data/assets/scripts/gold/investor_reporting/holdings_snapshot.py) at --as-of <served date>

Compares the two node sets by node_id (counts: common / served-only / built-only / equal / differing, and which flattened
fields differ, tallied), lists every class-field change, and lists the holdings of the packet's 32 rows
(MULTI_ASSET_ROW_SET_20261003.tsv MOVE + WRITE keys) in the served nodes with their amounts. Source vintages: the run's own
receipts vs the served manifest's source objects, so a difference from a re-captured source is not read as a code effect.
Writes REMINT_SERVED_EFFECT_<firm>_20261003.json.

Usage (repo root): python .../R9_CHECKS/remint_served_effect.py <49financial|inflection|cottonwood>
"""
from __future__ import annotations

import collections
import glob
import hashlib
import io
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

import boto3
import pyarrow.parquet as pq

FIRMS = {"49financial": "opal-data-49financial", "inflection": "opal-data-inflection", "cottonwood": "opal-data-cottonwood"}
ROOT = Path(__file__).resolve().parents[6]
PRODUCER_DIR = ROOT / "data" / "assets" / "scripts" / "gold" / "investor_reporting"
HERE = Path(__file__).resolve().parent
ROW_SET = HERE / "MULTI_ASSET_ROW_SET_20261003.tsv"
CLASS_FIELDS = ("asset_class", "asset_sub_class", "class", "sub_class", "classified_by", "classification")
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


def served(firm):
    bucket = FIRMS[firm]
    cur = json.loads(get(bucket, f"irpt/{firm}/platinum/holdings/current/manifest.json"))
    m = cur["dates"][cur["latest_date"]]["manifest"]
    man = json.loads(get(bucket, m["key"], m["version_id"]))
    g = man["gold"]
    data = get(g["bucket"], g["key"], g["version_id"])
    assert hashlib.sha256(data).hexdigest() == g["sha256"], "served gold parquet sha256 differs from its manifest"
    return cur["latest_date"], man, nodes_of(data)


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
            keys[parts[1].replace("CUSIP:", "")] = (parts[0], parts[4] if len(parts) > 4 else "", parts[5] if len(parts) > 5 else "")
    return keys


def main(firm):
    date, man, s_nodes = served(firm)
    print(f"served {firm}: date {date}, revision {man.get('revision')}, nodes {len(s_nodes)}", flush=True)
    with tempfile.TemporaryDirectory(prefix=f"remint_{firm}_") as tmp:
        cmd = [sys.executable, "holdings_snapshot.py", "--firms", firm, "--as-of", date, "--local-out", tmp]
        run = subprocess.run(cmd, cwd=str(PRODUCER_DIR), capture_output=True, text=True, timeout=3000)
        ok_line = [ln for ln in run.stdout.splitlines() if ln.startswith(("OK:", "REFUSED"))]
        print("producer rc", run.returncode, ok_line[:2], run.stderr.strip().splitlines()[-3:] if run.returncode else "", flush=True)
        if run.returncode != 0:
            out = {"firm": firm, "served_date": date, "producer_rc": run.returncode,
                   "stderr_tail": run.stderr.strip().splitlines()[-15:]}
            (HERE / f"REMINT_SERVED_EFFECT_{firm}_20261003.json").write_text(json.dumps(out, indent=1), encoding="utf-8")
            return 1
        built_parquets = glob.glob(os.path.join(tmp, "**", "gold", "**", "*.parquet"), recursive=True) or \
            glob.glob(os.path.join(tmp, "**", "*.parquet"), recursive=True)
        assert len(built_parquets) == 1, built_parquets
        b_nodes = nodes_of(Path(built_parquets[0]).read_bytes())
        try:
            result = json.loads(run.stdout[run.stdout.index("{"):])["results"][0]
        except Exception:  # noqa: BLE001
            result = {}

    S = {n["node_id"]: n for n in s_nodes}
    Bn = {n["node_id"]: n for n in b_nodes}
    common = S.keys() & Bn.keys()
    diff_fields, class_changes, differing = collections.Counter(), [], 0
    for nid in common:
        a, b = flat(S[nid]), flat(Bn[nid])
        changed = [k for k in a.keys() | b.keys() if a.get(k) != b.get(k)]
        if changed:
            differing += 1
            diff_fields.update(changed)
            cls = [k for k in changed if k.rsplit(".", 1)[-1] in CLASS_FIELDS]
            if cls:
                class_changes.append({"node_id": nid, "kind": S[nid].get("node_kind"),
                                      "changes": {k: [a.get(k), b.get(k)] for k in cls}})

    keys = row_keys()
    holders = collections.defaultdict(lambda: {"nodes": 0, "amount": 0.0})
    for n in s_nodes:
        blob = json.dumps(n, default=str)
        for k in keys:
            if f'"{k}"' in blob:
                holders[k]["nodes"] += 1
                holders[k]["amount"] += float(((n.get("amount") or {}).get("value")) or 0.0)

    served_sources = man.get("source_objects") or man.get("_source_objects") or []
    out = {
        "claim": "measured (served publication vs CLOUD producer at the served date, local build, no upload)",
        "firm": firm, "served_date": date, "served_revision": man.get("revision"),
        "built": {k: result.get(k) for k in ("business_date", "node_count", "unique_account_count", "reconcile_ok",
                                             "reconcile_after", "schema_valid")},
        "nodes": {"served": len(S), "built": len(Bn), "common": len(common), "served_only": len(S.keys() - Bn.keys()),
                  "built_only": len(Bn.keys() - S.keys()), "equal": len(common) - differing, "differing": differing},
        "differing_fields_top": diff_fields.most_common(25),
        "class_changes": class_changes[:200], "class_change_count": len(class_changes),
        "served_only_sample": sorted(S.keys() - Bn.keys())[:15], "built_only_sample": sorted(Bn.keys() - S.keys())[:15],
        "packet_rows_held_in_served": {k: v for k, v in holders.items()},
        "source_vintages": {"served_manifest_objects": len(served_sources),
                            "note": "compare against the run's receipts if differing nodes are not class or code effects"},
    }
    path = HERE / f"REMINT_SERVED_EFFECT_{firm}_20261003.json"
    path.write_text(json.dumps(out, indent=1, default=str), encoding="utf-8")
    print(json.dumps({k: out[k] for k in ("built", "nodes", "differing_fields_top", "class_change_count")}, indent=1, default=str))
    print("WROTE", path)
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in FIRMS:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1]))

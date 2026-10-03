#!/usr/bin/env python3
"""target_fold_qa.py -- the TARGET fold's deploy proof (CTO batch 187): the deployed irpt-holdings route vs the candidate,
each running its OWN snapshot.project over every firm's served Holdings publication. Read-only; no AWS write.

  <old>  the deployed zip, unpacked (its CodeSha256 is checked by the caller against get-function)
  <new>  that zip with only snapshot.py, entry.py and contracts/HoldingsSnapshot.schema.json replaced by the candidate's

Per firm, over the newest served publication (the manifest's platinum header + its gold parquet, sha256 checked): every
account as a one-account selection, and the whole firm as one selection. Counts:
  equal_without_include   new(include=()) == old, compared as canonical JSON   -- must be every selection
  target_served           new(include={"target"}) carries both TARGET blocks
  target_nonempty         ... and they are non-empty (the selection holds a TARGET node)
  target_labelled         every TARGET item says basis TARGET
  target_weights_sum_1    the TARGET class weights sum to 1 (within 1e-9) where non-empty
  actual_unchanged        the actual blocks are identical with and without include
  invalid                 slices that fail the candidate's contract (jsonschema) with include
Usage (repo root): python .../R31_CHECKS/target_fold_qa.py <old_dir> <new_dir> [firm ...]
"""
from __future__ import annotations

import hashlib
import importlib.util
import io
import json
import os
import sys

import boto3
import pyarrow.parquet as pq

FIRMS = {"49financial": "opal-data-49financial", "inflection": "opal-data-inflection", "cottonwood": "opal-data-cottonwood"}
s3 = boto3.client("s3", region_name="us-east-1")


def load(dir_, name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(dir_, "snapshot.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def get(bucket, key, ver=None):
    kw = {"Bucket": bucket, "Key": key}
    if ver:
        kw["VersionId"] = ver
    return s3.get_object(**kw)["Body"].read()


def publication(firm, bucket):
    cur = json.loads(get(bucket, f"irpt/{firm}/platinum/holdings/current/manifest.json"))
    m = cur["dates"][cur["latest_date"]]["manifest"]
    man = json.loads(get(bucket, m["key"], m["version_id"]))
    h = man["platinum_header"]
    header = json.loads(get(h["bucket"], h["key"], h.get("version_id")))
    g = man["gold"]
    data = get(g["bucket"], g["key"], g["version_id"])
    assert hashlib.sha256(data).hexdigest() == g["sha256"], "gold parquet sha256 differs from its manifest"
    nodes = [json.loads(s) for s in pq.read_table(io.BytesIO(data), columns=["node_json"]).column("node_json").to_pylist()]
    snap = {k: v for k, v in header.items() if k != "nodes"}
    snap["nodes"] = nodes
    return cur["latest_date"], man["revision"], snap


def scope_for(ids, firm_id):
    return {"verified_request_firm_id": firm_id, "permitted_account_set": sorted(ids),
            "selected_account_ids": sorted(ids), "permitted_account_set_fingerprint": "a" * 64,
            "selected_account_set_fingerprint": "b" * 64, "principal_class": "FIRM_OPERATIONS"}


def canon(doc):
    return json.dumps(doc, sort_keys=True, default=str)


def main(old_dir, new_dir, firms):
    # The zip is flat (snapshot.py imports its siblings: enforce, errors, resolve ...); those siblings are byte-identical on
    # both sides, so the deployed directory serves both. ids/keys ride the shared layer: the repo's _ids and _keys stand in.
    fn = os.path.join(os.getcwd(), "infra", "aws", "lambda", "investor-reporting")
    for path in (os.path.join(fn, "_keys"), os.path.join(fn, "_ids"), old_dir):
        if path not in sys.path:
            sys.path.insert(0, path)
    old, new = load(old_dir, "snapshot_deployed"), load(new_dir, "snapshot_candidate")
    assert not hasattr(old, "target_selection") and hasattr(new, "target_selection")
    try:
        import jsonschema
        validator = jsonschema.Draft202012Validator(new.load_contract()[0])
    except Exception as exc:  # noqa: BLE001
        validator = None
        print("NOTE: no jsonschema validation:", exc)
    totals = {}
    for firm in firms:
        date, rev, snap = publication(firm, FIRMS[firm])
        firm_id = (snap.get("scope") or {}).get("firm_id")
        accounts = sorted(n["node_id"] for n in snap["nodes"] if n.get("node_kind") == "ACCOUNT")
        selections = [[a] for a in accounts] + [accounts]
        # A one-account selection is projected over ITS account's nodes plus every node with no account root (so the
        # projection's unresolved count is the full snapshot's); project() drops every other node, so the answer is the
        # same and the run is linear. The whole firm is projected over the full snapshot.
        parent_of = {n["node_id"]: n.get("parent_node_id") for n in snap["nodes"]}
        kind = {n["node_id"]: n.get("node_kind") for n in snap["nodes"]}

        def root(nid):
            for _ in range(64):
                if kind.get(nid) == "ACCOUNT":
                    return nid
                nid = parent_of.get(nid)
                if nid is None:
                    return None
            return None
        groups, rootless = {}, []
        for n in snap["nodes"]:
            r = root(n["node_id"])
            (groups.setdefault(r, []) if r else rootless).append(n)
        header = {k: v for k, v in snap.items() if k != "nodes"}

        def snap_for(sel):
            if len(sel) != 1:
                return snap
            return {**header, "nodes": groups.get(sel[0], []) + rootless}
        c = dict(selections=0, equal_without_include=0, target_served=0, target_nonempty=0, target_labelled=0,
                 target_weights_sum_1=0, target_zero_total=0, actual_unchanged=0, invalid=0, errors_old=0, errors_new=0)
        for sel in selections:
            c["selections"] += 1
            sc = scope_for(sel, firm_id)
            try:
                a = old.project(snap_for(sel), dict(sc))
            except Exception:  # noqa: BLE001 -- a refusal is compared too
                a = "REFUSED"
                c["errors_old"] += 1
            try:
                b = new.project(snap_for(sel), dict(sc))
                t = new.project(snap_for(sel), dict(sc), include={"target"})
            except Exception:  # noqa: BLE001
                b = t = "REFUSED"
                c["errors_new"] += 1
            if canon(a) == canon(b):
                c["equal_without_include"] += 1
            if isinstance(t, dict) and all(k in t for k in new.TARGET_BLOCKS):
                c["target_served"] += 1
                items = t["security_aggregates_target"] + t["class_totals_target"]
                if items:
                    c["target_nonempty"] += 1
                    weights = [r["weight"] for r in t["class_totals_target"]]
                    if any(w is None for w in weights):
                        c["target_zero_total"] += 1          # TARGET nodes all 0.00: weight null, as the contract allows
                    elif abs(sum(weights) - 1) <= 1e-9:
                        c["target_weights_sum_1"] += 1
                if all(r.get("basis") == "TARGET" for r in items):
                    c["target_labelled"] += 1
                if all(t.get(k) == b.get(k) for k in new.AGGREGATE_BLOCKS):
                    c["actual_unchanged"] += 1
                if validator is not None and any(True for _ in validator.iter_errors(
                        {k: v for k, v in t.items() if not k.startswith("_")})):
                    c["invalid"] += 1
        totals[firm] = {"business_date": date, "revision": rev[:12], **c}
        print(firm, json.dumps(totals[firm]), flush=True)
    return totals


if __name__ == "__main__":
    out = main(sys.argv[1], sys.argv[2], sys.argv[3:] or list(FIRMS))
    print("TARGET-FOLD-QA", json.dumps(out))
